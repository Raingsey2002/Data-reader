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
        "activeEntities": []
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
        
    min_date = f"{df_raw['day'].min()}/{df_raw['month'].min()}/{df_raw['year'].min()}"
    max_date = f"{df_raw['day'].max()}/{df_raw['month'].max()}/{df_raw['year'].max()}"
    
    st.markdown(f"""
    <div>
        <h1 class="dashboard-title">📘 Report & Query Analytics Dashboard</h1>
        <p class="dashboard-subtitle">Coverage: {min_date} — {max_date}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 3. Filter Panel
    with st.expander("Filters", expanded=True):
        c1, c2, c3, c4 = st.columns(4)
        sel_levels = c1.multiselect("Levels", sorted(df_raw['level'].unique().astype(str)))
        
        if masters:
            all_entities = sorted([e['code'] for e in masters['entities']])
        else:
            all_entities = sorted(df_raw['norm_entity'].unique())
        sel_entities = c2.multiselect("Entities", all_entities)
        
        sel_years = c3.multiselect("Years", sorted(df_raw['year'].unique()))
        sel_months = c4.multiselect("Months", sorted(df_raw['month'].unique()))

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
        
    # 4. Calculate Summary Logic
    s = calculate_summary(df)
    
    # Inactive Logic
    universe_entities = sel_entities if sel_entities else (
        [e['code'] for e in masters['entities']] if masters else df_raw['norm_entity'].unique()
    )
    active_in_filter = set(df['norm_entity'].unique())
    inactive_entities = sorted(list(set(universe_entities) - active_in_filter))
    
    # Inactive Types Logic (Only if masters loaded)
    inactive_reports = []
    inactive_queries = []
    if masters:
        active_reps = set(df[df['type'] == 'Report']['code'].apply(norm).unique())
        active_ques = set(df[df['type'] == 'Query']['code'].apply(norm).unique())
        inactive_reports = sorted(list(set(masters['reportTypes']) - active_reps))
        inactive_queries = sorted(list(set(masters['queryTypes']) - active_ques))

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
        
    def chart_type_dist(data, title, color):
        df_chart = pd.DataFrame(data)
        if df_chart.empty: return None
        fig = px.bar(df_chart, x='value', y='name', orientation='h', title=title,
                     color_discrete_sequence=[color])
        fig.update_layout(yaxis={'categoryorder':'total ascending'}, xaxis_title="Count", yaxis_title="")
        return fig

    # --- TAB: OVERVIEW ---
    with t_over:
        # KPIs
        k1, k2, k3, k4 = st.columns(4)
        with k1: metric_card("Total Activities", f"{s['totals']['reports'] + s['totals']['queries']:,}", COLOR_MIXED)
        with k2: metric_card("Reports Generated", f"{s['totals']['reports']:,}", COLOR_REPORT)
        with k3: metric_card("Queries Generated", f"{s['totals']['queries']:,}", COLOR_QUERY)
        with k4: metric_card("Inactive Entities", f"{len(inactive_entities)}", "#ef4444")
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
            
        # Inactive Lists
        i1, i2, i3 = st.columns(3)
        with i1: 
            st.caption("Inactive Report Types")
            st.dataframe(pd.DataFrame(inactive_reports, columns=["Code"]), use_container_width=True, height=300)
        with i2:
            st.caption("Inactive Query Types")
            st.dataframe(pd.DataFrame(inactive_queries, columns=["Code"]), use_container_width=True, height=300)
        with i3:
            st.caption("Inactive Entities")
            st.dataframe(pd.DataFrame(inactive_entities, columns=["Code"]), use_container_width=True, height=300)

    # --- TAB: REPORTS ---
    with t_rep:
        # KPIs Specific
        rk1, rk2, rk3 = st.columns(3)
        with rk1: metric_card("Total Reports", f"{s['totals']['reports']:,}", COLOR_REPORT)
        with rk2: metric_card("Active Entities", f"{len(s['activeEntities']):,}", "black")
        with rk3: metric_card("Inactive Report Types", f"{len(inactive_reports)}", "#ef4444")
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
        
        fig_type = chart_type_dist(s['reportTypeDistribution'], "Report Type Distribution", COLOR_REPORT)
        if fig_type: st.plotly_chart(fig_type, use_container_width=True)
        else: st.info("No report type data")

    # --- TAB: QUERIES ---
    with t_que:
        # KPIs Specific
        qk1, qk2, qk3 = st.columns(3)
        with qk1: metric_card("Total Queries", f"{s['totals']['queries']:,}", COLOR_QUERY)
        with qk2: metric_card("Active Entities", f"{len(s['activeEntities']):,}", "black")
        with qk3: metric_card("Inactive Query Types", f"{len(inactive_queries)}", "#ef4444")
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
        
        fig_type = chart_type_dist(s['queryTypeDistribution'], "Query Type Distribution", COLOR_QUERY)
        if fig_type: st.plotly_chart(fig_type, use_container_width=True)
        else: st.info("No query type data")

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
