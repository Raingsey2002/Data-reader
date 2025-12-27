import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
import glob
import json
from datetime import datetime

# ==========================================
# CONFIGURATION & UTILS
# ==========================================
DATA_DIR = os.path.join(os.path.dirname(__file__), "Excel files", "report-data")
PARQUET_FILE = os.path.join(DATA_DIR, "report_data.parquet")
MASTERS_FILE = os.path.join(DATA_DIR, "masters.json")

# Colors matching the Next.js theme
COLOR_REPORT = "#10b981"  # Emerald-500
COLOR_QUERY = "#3b82f6"   # Blue-500
COLOR_MIXED = "#6366f1"   # Indigo-500

def norm(s):
    """Normalize string: Upper case, stripped."""
    if pd.isna(s): return ""
    return str(s).strip().upper()

def derive_type(code):
    """Derive Report/Query type from the code string."""
    c = str(code).upper()
    if 'RPT' in c: return 'Report'
    if 'QRY' in c: return 'Query'
    # Fallback heuristics
    if c.startswith('Q'): return 'Query'
    return 'Report' # Default

# ==========================================
# DATA LOADING
# ==========================================
@st.cache_data(show_spinner=False)
def load_masters():
    """Load master data from JSON or return empty structure."""
    if not os.path.exists(MASTERS_FILE):
        return None
    
    try:
        with open(MASTERS_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Normalize keys for easier lookups
        entities = []
        if 'entities' in data:
            for e in data['entities']:
                entities.append({
                    "code": norm(e.get("code", "")),
                    "desc": e.get("desc", ""),
                    "level": e.get("level", "")
                })
        
        report_types = [norm(r) for r in data.get('reportTypes', [])]
        query_types = [norm(q) for q in data.get('queryTypes', [])]
        
        return {
            "entities": entities,
            "reportTypes": report_types,
            "queryTypes": query_types
        }
    except Exception as e:
        st.error(f"Error loading masters.json: {e}")
        return None

@st.cache_data(show_spinner=True)
def load_data():
    """
    Load data from Parquet. If missing/stale, rebuild from Excel files.
    """
    # Force rebuild if column schema is wrong in cached file
    if os.path.exists(PARQUET_FILE):
        try:
            df = pd.read_parquet(PARQUET_FILE)
            if 'type' not in df.columns or df['type'].isnull().all():
                st.warning("⚠️ Cached data schema mismatch. Rebuilding...")
                raise ValueError("Invalid cache")
            return df
        except Exception:
            pass # Fall through to rebuild
    
    excel_files = glob.glob(os.path.join(DATA_DIR, "main_data_*.xlsx"))
    if not excel_files:
        st.error(f"❌ No Excel files found in {DATA_DIR}")
        return pd.DataFrame()

    all_dfs = []
    status = st.empty()
    status.info("⏳ Processing Excel files... This may take a minute.")
    
    for f in excel_files:
        try:
            temp_df = pd.read_excel(f, dtype=str)
            all_dfs.append(temp_df)
        except Exception as e:
            st.warning(f"Skipped {os.path.basename(f)} due to error: {e}")

    if not all_dfs:
        return pd.DataFrame()

    df = pd.concat(all_dfs, ignore_index=True)

    # Column Mapping
    # NOTE: "Report/Query" in Excel is actually the CODE (e.g. Z_RPT_...).
    col_map = {
        "Report/Query": "code",
        "Name of Report and Query": "name",
        "Description": "desc",
        "Count": "count",
        "User ID": "user",
        "Level": "level",
        "Entity": "entity",
        "Office": "office",
        "Operating Unit": "ou",
        "YEAR": "year",
        "MONTH": "month",
        "DAY": "day"
    }
    
    df.columns = [c.strip() for c in df.columns]
    # Check if mapped columns exist
    missing_cols = [k for k in col_map.keys() if k not in df.columns]
    if missing_cols:
        st.error(f"❌ Missing expected columns in Excel: {missing_cols}")
        st.write("Found columns:", df.columns.tolist())
        return pd.DataFrame()

    df = df.rename(columns=col_map)
    
    # Derive TYPE from CODE
    df['type'] = df['code'].apply(derive_type)
    
    # Ensure numeric columns
    df['year'] = pd.to_numeric(df['year'], errors='coerce').fillna(0).astype(int)
    df['month'] = pd.to_numeric(df['month'], errors='coerce').fillna(0).astype(int)
    df['day'] = pd.to_numeric(df['day'], errors='coerce').fillna(0).astype(int)
    
    # Normalization
    df['norm_entity'] = df['entity'].apply(norm)
    df['norm_code'] = df['name'].apply(norm) 
    
    try:
        df.to_parquet(PARQUET_FILE)
        status.success("✅ Data cache built successfully!")
    except Exception as e:
        status.warning(f"Could not save cache: {e}")
        
    return df

# ==========================================
# LOGIC & AGGREGATION (Matches data-service.ts)
# ==========================================
def calculate_summary(df):
    """
    Replicates the logic of summarize() from Next.js data-service.ts
    """
    summary = {
        "totals": {"reports": 0, "queries": 0},
        "levelDistribution": [],
        "entityPerformance": [],
        "monthlyTrends": [],
        "yearlyTotals": [],
        "monthlyComparison": [],
        "reportTypeDistribution": [],
        "queryTypeDistribution": [],
        "activeEntities": [],
        "topEntities": {
            "overall": {"code": "-", "count": 0},
            "reports": {"code": "-", "count": 0},
            "queries": {"code": "-", "count": 0}
        }
    }
    
    if df.empty:
        return summary
        
    # Basics
    reports = df[df['type'] == 'Report']
    queries = df[df['type'] == 'Query']
    summary["totals"]["reports"] = len(reports)
    summary["totals"]["queries"] = len(queries)
    
    # 1. Level Distribution
    # Group by Level and Type
    level_grp = df.groupby(['level', 'type']).size().unstack(fill_value=0)
    # Ensure all levels exist, columns might be missing if no reports/queries
    for col in ['Report', 'Query']:
        if col not in level_grp.columns:
            level_grp[col] = 0
            
    try:
        levels_order = ["National Level", "Sub-National Level", "APE"]
        level_dist = []
        for lvl in levels_order:
            if lvl in level_grp.index:
                r = int(level_grp.loc[lvl, 'Report'])
                q = int(level_grp.loc[lvl, 'Query'])
                level_dist.append({"name": lvl, "reports": r, "queries": q, "total": r + q})
            else:
                level_dist.append({"name": lvl, "reports": 0, "queries": 0, "total": 0})
        summary["levelDistribution"] = level_dist
    except Exception:
        pass # Handle grouping errors gracefully

    # 2. Monthly Trends (Current Year/Filters)
    month_grp = df.groupby(['month', 'type']).size().unstack(fill_value=0).reindex(range(1, 13), fill_value=0)
    for col in ['Report', 'Query']:
        if col not in month_grp.columns:
            month_grp[col] = 0
            
    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    monthly_trends = []
    for m_idx, m_name in enumerate(month_names, 1):
        r = int(month_grp.loc[m_idx, 'Report'])
        q = int(month_grp.loc[m_idx, 'Query'])
        monthly_trends.append({"month": m_name, "reports": r, "queries": q})
    summary["monthlyTrends"] = monthly_trends

    # 3. Monthly Comparison (Year over Year)
    if 'year' in df.columns:
        years = sorted(df['year'].unique())
        monthly_comp = []
        for y in years:
            df_y = df[df['year'] == y]
            m_grp_y = df_y.groupby(['month', 'type']).size().unstack(fill_value=0).reindex(range(1, 13), fill_value=0)
            
            reps = m_grp_y['Report'].tolist() if 'Report' in m_grp_y.columns else [0]*12
            ques = m_grp_y['Query'].tolist() if 'Query' in m_grp_y.columns else [0]*12
            
            monthly_comp.append({
                "year": int(y), 
                "reports": reps, 
                "queries": ques
            })
        summary["monthlyComparison"] = monthly_comp
        
        # 4. Yearly Totals
        yearly_grp = df.groupby(['year', 'type']).size().unstack(fill_value=0)
        yearly_totals = []
        for y in years:
            r = int(yearly_grp.loc[y, 'Report']) if 'Report' in yearly_grp.columns else 0
            q = int(yearly_grp.loc[y, 'Query']) if 'Query' in yearly_grp.columns else 0
            yearly_totals.append({"year": int(y), "reports": r, "queries": q})
        summary["yearlyTotals"] = yearly_totals

    # 5. Entity Performance
    ent_grp = df.groupby(['entity', 'type']).size().unstack(fill_value=0)
    if not ent_grp.empty:
        ent_grp['total'] = ent_grp.sum(axis=1)
        ent_grp = ent_grp.sort_values('total', ascending=False)
        
        ent_perf = []
        for ent, row in ent_grp.iterrows():
            r = int(row.get('Report', 0))
            q = int(row.get('Query', 0))
            t = int(row.get('total', 0))
            ent_perf.append({"entity": ent, "reports": r, "queries": q, "total": t})
        summary["entityPerformance"] = ent_perf
        summary["activeEntities"] = df['norm_entity'].unique().tolist()

    # 6. Type Distribution
    rep_types = reports['name'].value_counts().head(50).reset_index()
    rep_types.columns = ['name', 'value']
    summary["reportTypeDistribution"] = rep_types.to_dict('records')
    
    que_types = queries['name'].value_counts().head(50).reset_index()
    que_types.columns = ['name', 'value']
    summary["queryTypeDistribution"] = que_types.to_dict('records')

    # 7. Top Entities
    # Overall
    if not ent_grp.empty:
        top_overall = ent_grp.sort_values('total', ascending=False).iloc[0]
        summary["topEntities"]["overall"] = {"code": top_overall.name, "count": int(top_overall['total'])}
        
        # Reports
        if 'Report' in ent_grp.columns:
             top_rep = ent_grp.sort_values('Report', ascending=False).iloc[0]
             summary["topEntities"]["reports"] = {"code": top_rep.name, "count": int(top_rep['Report'])}
        
        # Queries
        if 'Query' in ent_grp.columns:
             top_que = ent_grp.sort_values('Query', ascending=False).iloc[0]
             summary["topEntities"]["queries"] = {"code": top_que.name, "count": int(top_que['Query'])}

    return summary

# ==========================================
# UI COMPONENTS
# ==========================================
def metric_card(title, value, color="black"):
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">{title}</div>
        <div class="metric-value" style="color: {color}">{value}</div>
    </div>
    """, unsafe_allow_html=True)

def Report():
    # 1. CSS Styles
    st.markdown("""
        <style>
        .block-container { padding-top: 1rem; padding-bottom: 2rem; max-width: 1400px; }
        .dashboard-title { font-family: 'Inter', sans-serif; color: #064e3b; font-weight: 700; font-size: 2rem; }
        .dashboard-subtitle { color: #065f46; font-size: 1rem; margin-bottom: 2rem; }
        .metric-card { background: white; border-radius: 8px; padding: 1.5rem; box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1); border: 1px solid #e5e7eb; height: 100%; }
        .metric-title { font-size: 0.875rem; color: #6b7280; font-weight: 500; }
        .metric-value { font-size: 2rem; font-weight: 700; margin-top: 0.5rem; }
        </style>
    """, unsafe_allow_html=True)

    # 2. Load Resources
    df_raw = load_data()
    masters = load_masters()
    
    if df_raw.empty:
        st.warning("No data available.")
        st.stop()
    
    # ---------- FILTER SESSION STATE ----------
    if "report_levels" not in st.session_state:
        st.session_state["report_levels"] = []
    if "report_entities" not in st.session_state:
        st.session_state["report_entities"] = []
    if "report_years" not in st.session_state:
        st.session_state["report_years"] = []
    if "report_months" not in st.session_state:
        st.session_state["report_months"] = []
        
    # Date Formatting
    months_map = {i: m for i, m in enumerate(MONTHS, 1)}
    
    # Sort to determine true min/max dates
    df_sorted = df_raw.sort_values(by=['year', 'month', 'day'])
    
    if not df_sorted.empty:
        min_row = df_sorted.iloc[0]
        max_row = df_sorted.iloc[-1]
        
        d_min, m_min, y_min = min_row['day'], min_row['month'], min_row['year']
        d_max, m_max, y_max = max_row['day'], max_row['month'], max_row['year']
    else:
        # Fallback if empty
        d_min, m_min, y_min = 0, 0, 0
        d_max, m_max, y_max = 0, 0, 0
    
    min_date_str = f"{int(d_min):02d} {months_map.get(int(m_min), '')} {int(y_min)}"
    max_date_str = f"{int(d_max):02d} {months_map.get(int(m_max), '')} {int(y_max)}"

    # New Header UI
    st.markdown(f"""
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
        <h1 class="dashboard-title" style="margin: 0;">📘 Report & Query Analytics Dashboard</h1>
        <div style="background-color: #047857; color: white; padding: 0.5rem 1rem; border-radius: 6px; font-family: 'Inter', sans-serif; font-size: 1rem; font-weight: 600; box-shadow: 0 1px 2px rgba(0,0,0,0.1);">
            <span style="margin-right: 6px;">📅</span> 
            Coverage: {min_date_str} — {max_date_str}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # 3. Filter Panel
    def clear_filters_callback():
        """Callback to reset all filter session states."""
        st.session_state["report_levels"] = []
        st.session_state["report_entities"] = []
        st.session_state["report_years"] = []
        st.session_state["report_months"] = []
        st.session_state["filter_types_combined"] = []

    # --- Clear button at top right, above the filter box ---
    clear_button_row_col1, clear_button_row_col2 = st.columns([0.90, 0.10])
    
    is_filtered = any([st.session_state["report_levels"], 
                        st.session_state["report_entities"], 
                        st.session_state["report_years"], 
                        st.session_state["report_months"],
                        st.session_state.get("filter_types_combined")])

    if is_filtered:
        message = "Active filters applied."
        style = "background-color: #ffe0e0; border-left: 5px solid #dc3545; color: #dc3545;"
    else:
        message = "No filters selected: displaying all available data."
        style = "background-color: #e0f2f7; border-left: 5px solid #007bff; color: #0056b3;"

    with clear_button_row_col1:
        st.markdown(f"""
        <div style="{style} padding: 5px 10px; border-radius: 3px; display: inline-block;">
            <p style="font-size: 0.75rem; margin: 0;">{message}</p>
        </div>
        """, unsafe_allow_html=True)
    with clear_button_row_col2:
        st.button("Clear filters", key="clear_report_filters_button", on_click=clear_filters_callback)

    with st.expander("Filters", expanded=True):
        # Layout: Levels | Entities | Types | Years | Months
        c1, c2, c3, c4, c5 = st.columns([1.2, 3, 1.7, 1.4, 0.9])
        
        # 1. Levels
        sel_levels = c1.multiselect(
            "Levels", 
            sorted(df_raw['level'].unique().astype(str)),
            key="report_levels"
        )
        
        # 2. Entities
        entity_desc_map = {}
        if masters:
            all_entities = sorted([e['code'] for e in masters['entities']])
            for e in masters['entities']:
                entity_desc_map[e['code']] = e['desc']
        else:
            all_entities = sorted(df_raw['norm_entity'].unique())
            
        def format_entity(code):
            desc = entity_desc_map.get(code, "")
            return f"{code} - {desc}" if desc else code

        sel_entities = c2.multiselect(
            "Entities", 
            all_entities, 
            format_func=format_entity,
            key="report_entities"
        )

        # 3. Report/Query Types (Moved Here)
        all_rep_types = masters['reportTypes'] if masters else sorted(df_raw[df_raw['type']=='Report']['name'].unique())
        all_que_types = masters['queryTypes'] if masters else sorted(df_raw[df_raw['type']=='Query']['name'].unique())
        all_types = sorted(list(set(all_rep_types + all_que_types)))
        
        sel_types_combined = c3.multiselect(
            "Report/Query Types", 
            all_types, 
            key="filter_types_combined"
        )
        
        # 4. Years
        sel_years = c4.multiselect(
            "Years", 
            sorted(df_raw['year'].unique()),
            key="report_years"
        )

        # 5. Months
        sel_months = c5.multiselect(
            "Months", 
            sorted(df_raw['month'].unique()),
            key="report_months"
        )

    # Apply Filters
    df = df_raw.copy()
    if sel_levels:
        df = df[df['level'].isin(sel_levels)]
    if sel_entities:
        df = df[df['norm_entity'].isin(sel_entities)]
    if sel_years:
        df = df[df['year'].isin(sel_years)]
    if sel_months:
        df = df[df['month'].isin(sel_months)]
    if sel_types_combined:
        df = df[df['name'].isin(sel_types_combined)]
        
    # 4. Calculate Summary Logic
    s = calculate_summary(df)
    
    # Inactive Logic
    # Inactive Logic
    # 1. Determine Universe of Entities (respecting Level filter if set, but Entity filter is empty)
    if sel_entities:
        universe_entities = sel_entities
    elif sel_levels:
        # If Level is selected but Entities are NOT, restrict universe to that Level
        if masters:
             universe_entities = [e['code'] for e in masters['entities'] if e['level'] in sel_levels]
        else:
             # Fallback if no masters
             universe_entities = df_raw[df_raw['level'].isin(sel_levels)]['norm_entity'].unique()
    else:
        # No hierarchy filters -> Full universe
        if masters:
            universe_entities = [e['code'] for e in masters['entities']]
        else:
             universe_entities = df_raw['norm_entity'].unique()
    active_in_filter = set(df['norm_entity'].unique())
    inactive_entities = sorted(list(set(universe_entities) - active_in_filter))
    
    # Inactive Types Logic (Only if masters loaded)
    inactive_reports = []
    inactive_queries = []
    if masters:
        # Use 'name' column for types (e.g. R01, Q01)
        active_reps = set(df[df['type'] == 'Report']['name'].apply(norm).unique())
        active_ques = set(df[df['type'] == 'Query']['name'].apply(norm).unique())
        
        # Determine Universe based on Filter
        if sel_types_combined:
             # If filter is applied, universe is the intersection of selection and valid types
             universe_reps = set(sel_types_combined).intersection(set(masters['reportTypes']))
             universe_ques = set(sel_types_combined).intersection(set(masters['queryTypes']))
        else:
             # If no filter, universe is ALL types
             universe_reps = set(masters['reportTypes'])
             universe_ques = set(masters['queryTypes'])

        inactive_reports = sorted(list(universe_reps - active_reps))
        inactive_queries = sorted(list(universe_ques - active_ques))

    # Construct Inactive Entities DataFrame with Description
    inactive_ent_data = []
    for code in inactive_entities:
        desc = entity_desc_map.get(code, "")
        inactive_ent_data.append({"Code": code, "Description": desc})
    df_inactive_ent = pd.DataFrame(inactive_ent_data)

    # 5. Tabs
    t_over, t_rep, t_que, t_data = st.tabs(["Overview", "Reports", "Queries", "Raw Data"])
    
    # --- SHARED CHART FUNCTIONS ---
    def chart_level_dist(data, mode="both"):
        df_chart = pd.DataFrame(data)
        if df_chart.empty: return None
        
        fig = go.Figure()
        if mode in ["both", "reports"]:
            fig.add_trace(go.Bar(name='Reports', x=df_chart['name'], y=df_chart['reports'], marker_color=COLOR_REPORT))
        if mode in ["both", "queries"]:
            fig.add_trace(go.Bar(name='Queries', x=df_chart['name'], y=df_chart['queries'], marker_color=COLOR_QUERY))
        fig.update_layout(barmode='group', title="Distribution by Level", xaxis_title="", yaxis_title="Count")
        return fig

    def chart_trends(data, mode="both"):
        df_chart = pd.DataFrame(data)
        if df_chart.empty: return None
        fig = go.Figure()
        if mode in ["both", "reports"]:
            fig.add_trace(go.Scatter(name='Reports', x=df_chart['month'], y=df_chart['reports'], line=dict(color=COLOR_REPORT, width=3)))
        if mode in ["both", "queries"]:
            fig.add_trace(go.Scatter(name='Queries', x=df_chart['month'], y=df_chart['queries'], line=dict(color=COLOR_QUERY, width=3)))
        fig.update_layout(title="Monthly Trends", xaxis_title="Month", yaxis_title="Count")
        return fig
        
    def chart_yearly(data, mode="both"):
        df_chart = pd.DataFrame(data)
        if df_chart.empty: return None
        fig = go.Figure()
        if mode in ["both", "reports"]:
            fig.add_trace(go.Bar(name='Reports', x=df_chart['year'], y=df_chart['reports'], marker_color=COLOR_REPORT))
        if mode in ["both", "queries"]:
            fig.add_trace(go.Bar(name='Queries', x=df_chart['year'], y=df_chart['queries'], marker_color=COLOR_QUERY))
        fig.update_layout(barmode='group', title="Yearly Comparison", xaxis_title="Year", yaxis_title="Count")
        return fig
        
    def chart_type_dist(data, title, color, height=None):
        df_chart = pd.DataFrame(data)
        if df_chart.empty: return None
        fig = px.bar(df_chart, x='value', y='name', orientation='h', title=title,
                     color_discrete_sequence=[color], height=height)
        fig.update_layout(yaxis={'categoryorder':'total ascending'}, xaxis_title="Count", yaxis_title="")
        return fig

    # --- TAB: OVERVIEW ---
    with t_over:
        # KPIs
        k1, k2, k3, k4, k5 = st.columns(5)
        with k1: metric_card("Total Activities", f"{s['totals']['reports'] + s['totals']['queries']:,}", COLOR_MIXED)
        with k2: metric_card("Reports Generated", f"{s['totals']['reports']:,}", COLOR_REPORT)
        with k3: metric_card("Queries Generated", f"{s['totals']['queries']:,}", COLOR_QUERY)
        with k4: metric_card("Top Active Entity", f"{s['topEntities']['overall']['code']}", "#d97706")
        with k5: metric_card("Inactive Entities", f"{len(inactive_entities)}", "#ef4444")
        st.markdown("---")
        
        r1c1, r1c2 = st.columns(2)
        with r1c1: 
            fig = chart_level_dist(s['levelDistribution'], "both")
            if fig: st.plotly_chart(fig, use_container_width=True)
            else: st.info("No level data")
        with r1c2: 
            fig = chart_trends(s['monthlyTrends'], "both")
            if fig: st.plotly_chart(fig, use_container_width=True)
            else: st.info("No trend data")
            
        r2c1, r2c2 = st.columns(2)
        with r2c1: 
            # Monthly Comparison (Year over Year) -> Complex Line/Bar combo
            if s['monthlyComparison']:
                fig_mc = go.Figure()
                # Iterate years
                for y_data in s['monthlyComparison']:
                    year = y_data['year']
                    total_act = [r+q for r,q in zip(y_data['reports'], y_data['queries'])]
                    fig_mc.add_trace(go.Scatter(x=MONTHS, y=total_act, name=str(year), mode='lines+markers'))
                fig_mc.update_layout(title="Monthly Comparison (Year-over-Year)", xaxis_title="Month")
                st.plotly_chart(fig_mc, use_container_width=True)
            else:
                st.info("No monthly comparison data")
            
        with r2c2: 
            fig = chart_yearly(s['yearlyTotals'], "both")
            if fig: st.plotly_chart(fig, use_container_width=True)
            else: st.info("No yearly data")

        # Entity Performance
        st.subheader("Entity Performance")
        df_ent = pd.DataFrame(s['entityPerformance']).head(10)
        if not df_ent.empty:
            fig_ent = px.bar(df_ent, y='entity', x=['reports', 'queries'], orientation='h', title="Top 10 Active Entities",
                             color_discrete_map={"reports": COLOR_REPORT, "queries": COLOR_QUERY}, barmode='stack')
            fig_ent.update_layout(yaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig_ent, use_container_width=True)
        else:
            st.info("No entity data")
        
        # Top 10 Generated Report / Query
        st.subheader("Report and Query Performance")
        tc1, tc2 = st.columns(2)
        with tc1:
            if s['reportTypeDistribution']:
                top10_rep = s['reportTypeDistribution'][:10]
                fig_top_rep = chart_type_dist(top10_rep, "Top 10 Most Generated Reports", COLOR_REPORT, height=400)
                st.plotly_chart(fig_top_rep, use_container_width=True)
            else:
                st.info("No report data")
        with tc2:
            if s['queryTypeDistribution']:
                top10_que = s['queryTypeDistribution'][:10]
                fig_top_que = chart_type_dist(top10_que, "Top 10 Most Generated Queries", COLOR_QUERY, height=400)
                st.plotly_chart(fig_top_que, use_container_width=True)
            else:
                st.info("No query data")
            
        # Inactive Lists
        st.markdown("---")
        st.subheader("Inactive Lists")
        i1, i2, i3 = st.columns(3)
        with i1: 
            st.caption(f"Inactive Report Types (Total: {len(inactive_reports)})")
            df_ir = pd.DataFrame(inactive_reports, columns=["Code"])
            df_ir.index += 1
            st.dataframe(df_ir, use_container_width=True, height=300)
        with i2:
            st.caption(f"Inactive Query Types (Total: {len(inactive_queries)})")
            df_iq = pd.DataFrame(inactive_queries, columns=["Code"])
            df_iq.index += 1
            st.dataframe(df_iq, use_container_width=True, height=300)
        with i3:
            st.caption(f"Inactive Entities (Total: {len(df_inactive_ent)})")
            df_ie = df_inactive_ent.copy()
            df_ie.index += 1
            st.dataframe(df_ie, use_container_width=True, height=300)

    # --- TAB: REPORTS ---
    with t_rep:
        # KPIs Specific
        rk1, rk2, rk3, rk4 = st.columns(4)
        with rk1: metric_card("Total Reports", f"{s['totals']['reports']:,}", COLOR_REPORT)
        with rk2: metric_card("Active Entities", f"{len(s['activeEntities']):,}", "black")
        with rk3: metric_card("Top Reporting Entity", f"{s['topEntities']['reports']['code']}", "#d97706")
        with rk4: metric_card("Inactive Report Types", f"{len(inactive_reports)}", "#ef4444")
        st.markdown("---")
        
        rr1, rr2 = st.columns(2)
        with rr1: 
            fig = chart_level_dist(s['levelDistribution'], "reports")
            if fig: st.plotly_chart(fig, use_container_width=True)
            else: st.info("No level data")
        with rr2: 
            fig = chart_trends(s['monthlyTrends'], "reports")
            if fig: st.plotly_chart(fig, use_container_width=True)
            else: st.info("No trend data")
        
        rr3, rr4 = st.columns(2)
        with rr3:
            # Monthly Comparison (Reports Only)
            if s['monthlyComparison']:
                fig_mcr = go.Figure()
                for y_data in s['monthlyComparison']:
                    fig_mcr.add_trace(go.Scatter(x=MONTHS, y=y_data['reports'], name=str(y_data['year']), mode='lines+markers'))
                fig_mcr.update_layout(title="Monthly Comparison (Year-over-Year) - Reports", xaxis_title="Month") 
                st.plotly_chart(fig_mcr, use_container_width=True)
            else:
                st.info("No comparison data")
        with rr4: 
            fig = chart_yearly(s['yearlyTotals'], "reports")
            if fig: st.plotly_chart(fig, use_container_width=True)
            else: st.info("No yearly data")

                # Top 10 Entities (Reports)
        st.subheader("Top 10 Entities Performance (Reports)")
        if s['entityPerformance']:
            df_ent_perf = pd.DataFrame(s['entityPerformance'])
            # Sort by reports descending
            df_ent_perf = df_ent_perf.sort_values('reports', ascending=False).head(10)
            fig_entr = px.bar(df_ent_perf, y='entity', x='reports', orientation='h', 
                             title="Entities by Report Volume", color_discrete_sequence=[COLOR_REPORT])
            fig_entr.update_layout(yaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig_entr, use_container_width=True)
        else:
            st.info("No entity performance data")    

        st.subheader("Report performance")
        # Report Type Distribution
        h_rep = max(400, len(s['reportTypeDistribution']) * 25)
        fig_type = chart_type_dist(s['reportTypeDistribution'], "Report Type Distribution", COLOR_REPORT, height=h_rep)
        if fig_type: st.plotly_chart(fig_type, use_container_width=True)
        else: st.info("No report type data")



        # Inactive Lists for Reports
        st.markdown("---")
        st.subheader("Inactive Lists")
        ir1, ir2 = st.columns(2)
        with ir1: 
            st.caption(f"Inactive Report Types (Total: {len(inactive_reports)})")
            df_ir = pd.DataFrame(inactive_reports, columns=["Code"])
            df_ir.index += 1
            st.dataframe(df_ir, use_container_width=True, height=300)
        with ir2:
            st.caption(f"Inactive Entities (Reports Context) (Total: {len(df_inactive_ent)})")
            df_ie = df_inactive_ent.copy()
            df_ie.index += 1
            st.dataframe(df_ie, use_container_width=True, height=300)

    # --- TAB: QUERIES ---
    with t_que:
        # KPIs Specific
        qk1, qk2, qk3, qk4 = st.columns(4)
        with qk1: metric_card("Total Queries", f"{s['totals']['queries']:,}", COLOR_QUERY)
        with qk2: metric_card("Active Entities", f"{len(s['activeEntities']):,}", "black")
        with qk3: metric_card("Top Querying Entity", f"{s['topEntities']['queries']['code']}", "#d97706")
        with qk4: metric_card("Inactive Query Types", f"{len(inactive_queries)}", "#ef4444")
        st.markdown("---")
        
        qr1, qr2 = st.columns(2)
        with qr1: 
            fig = chart_level_dist(s['levelDistribution'], "queries")
            if fig: st.plotly_chart(fig, use_container_width=True)
            else: st.info("No level data")
        with qr2: 
            fig = chart_trends(s['monthlyTrends'], "queries")
            if fig: st.plotly_chart(fig, use_container_width=True)
            else: st.info("No trend data")
        
        qr3, qr4 = st.columns(2)
        with qr3:
             # Monthly Comparison (Queries Only)
            if s['monthlyComparison']:
                fig_mcq = go.Figure()
                for y_data in s['monthlyComparison']:
                    fig_mcq.add_trace(go.Scatter(x=MONTHS, y=y_data['queries'], name=str(y_data['year']), mode='lines+markers'))
                fig_mcq.update_layout(title="Monthly Comparison (Year-over-Year) - Queries", xaxis_title="Month") 
                st.plotly_chart(fig_mcq, use_container_width=True)
            else:
                st.info("No comparison data")
        with qr4: 
            fig = chart_yearly(s['yearlyTotals'], "queries")
            if fig: st.plotly_chart(fig, use_container_width=True)
            else: st.info("No yearly data")

                # Top 10 Entities (Queries)
        st.subheader("Top 10 Entities Performance (Queries)")
        if s['entityPerformance']:
            df_ent_perf_q = pd.DataFrame(s['entityPerformance'])
            # Sort by queries descending
            df_ent_perf_q = df_ent_perf_q.sort_values('queries', ascending=False).head(10)
            fig_entq = px.bar(df_ent_perf_q, y='entity', x='queries', orientation='h', 
                             title="Entities by Query Volume", color_discrete_sequence=[COLOR_QUERY])
            fig_entq.update_layout(yaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig_entq, use_container_width=True)
        else:
            st.info("No entity performance data")

        # Query Type Distribution
        st.subheader("Query Performance")
        h_que = max(400, len(s['queryTypeDistribution']) * 35)
        fig_type = chart_type_dist(s['queryTypeDistribution'], "Query Type Distribution", COLOR_QUERY, height=h_que)
        if fig_type: st.plotly_chart(fig_type, use_container_width=True)
        else: st.info("No query type data")



        # Inactive Lists for Queries
        st.markdown("---")
        st.subheader("Inactive Lists")
        iq1, iq2 = st.columns(2)
        with iq1:
            st.caption(f"Inactive Query Types (Total: {len(inactive_queries)})")
            df_iq = pd.DataFrame(inactive_queries, columns=["Code"])
            df_iq.index += 1
            st.dataframe(df_iq, use_container_width=True, height=400)
        with iq2:
            st.caption(f"Inactive Entities (Queries Context) (Total: {len(df_inactive_ent)})")
            df_ie = df_inactive_ent.copy()
            df_ie.index += 1
            st.dataframe(df_ie, use_container_width=True, height=400)

    # --- TAB: RAW DATA ---
    with t_data:
        st.subheader("Data Explorer")
        search_term = st.text_input("Search (Name, User, Entity, Desc)", "")
        dff = df
        if search_term:
            s = search_term.upper()
            dff = dff[
                dff['name'].str.upper().str.contains(s) | 
                dff['user'].str.upper().str.contains(s) |
                dff['entity'].str.upper().str.contains(s) |
                dff['desc'].str.upper().str.contains(s)
            ]
        st.write(f"Showing {len(dff)} records")
        st.dataframe(dff, use_container_width=True, height=600)

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

if __name__ == "__main__":
    Report()
