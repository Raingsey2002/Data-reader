import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


@st.cache_data(show_spinner=False)
def load_supplier_data():
    """
    Loads, cleans, and standardizes the supplier data from Excel.
    """
    # supplier data path
    file_path = "Excel files/Supplier.xlsx"

    # Read as text first, then clean/convert
    try:
        df = pd.read_excel(file_path, dtype=str)
    except FileNotFoundError:
        return pd.DataFrame() # Return empty if file not found

    # Strip spaces around column names
    df = df.rename(columns=lambda c: c.strip())

    # Standardize column names
    rename_map = {
        "BUSINESS UNIT": "Business Unit",
        "OPERATING UNIT": "Operating Unit",
        "PO TYPE": "Po Type", 
        "ACCOUNT": "Account",
        "VENDOR ID": "Vendor ID",
        "VENDOR DESCR": "Vendor Name",
        "PO DATE": "PO Date",
        "MONTH": "Month",
        "YEAR": "Year",
        "AMOUNT": "Amount",
        "AMOUNT ": "Amount",
    }
    df = df.rename(columns={k: v for k, v in rename_map.items() if k in df.columns})

    # Clean Amount: remove commas & spaces, convert to number
    if "Amount" in df.columns:
        amt = (
            df["Amount"]
            .astype(str)
            .str.replace(",", "", regex=False)
            .str.replace(" ", "", regex=False)
        )
        df["Amount"] = pd.to_numeric(amt, errors="coerce").fillna(0)
    else:
        df["Amount"] = 0

    # Parse PO Date and ensure Month/Year columns exist
    if "PO Date" in df.columns:
        df["PO Date"] = pd.to_datetime(df["PO Date"], errors="coerce")
        
    if "Year" not in df.columns or df["Year"].isna().all():
        df["Year"] = df["PO Date"].dt.year.astype("Int64").astype(str).fillna('N/A')
        
    if "Month" not in df.columns or df["Month"].isna().all():
        df["Month"] = df["PO Date"].dt.month.astype("Int64").astype(str).str.zfill(2).fillna('00')

    # Period (YYYY-MM) for charts
    df["Period"] = df["Year"] + "-" + df["Month"]
    # Filter out invalid periods created by N/A or NaT dates
    df = df[~df['Period'].str.contains('N/A|00')]
    
    return df


def calculate_percentage_change(current, previous):
    """Calculates percentage change, handling division by zero."""
    if previous == 0:
        return 0
    return ((current - previous) / previous) * 100


def create_metric_card(title, value, delta=None, delta_color=None):
    """Creates a styled HTML card for a metric (used for the initial KPIs)."""
    # NOTE: This function is not used in the final version of the PO Type Breakdown
    # but kept here for potential future use or consistency with original structure.
    delta_html = ""
    if delta is not None:
        delta_html = f'<div class="metric-delta" style="color: {delta_color};">{delta}</div>'
    return f"""
    <div class="metric-card">
        <div class="metric-title">{title}</div>
        <div class="metric-value">{value}</div>
        {delta_html}
    </div>
    """


def Supplier():
    # ------------- PAGE STYLES -------------
    st.markdown(
        """
        <style>
        /* General Layout */
        .block-container {
            padding-top: 1rem;
            padding-bottom: 2rem;
            max-width: 1400px;
        }
        .dashboard-title {
            font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: #2c3e50;
            font-weight: 700;
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
        }
        .dashboard-subtitle {
            font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: #7f8c8d;
            font-size: 1rem;
            margin-bottom: 2rem;
        }

        /* KPI Card Styling (Used at the top) */
        .metric-card {
            background: white;
            border-radius: 8px;
            padding: 1.5rem;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
            border: 1px solid #e0e0e0;
            transition: all 0.3s ease;
            height: 120px;
            overflow: hidden;
        }
        .metric-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 15px rgba(0, 0, 0, 0.1);
        }
        .metric-title {
            font-size: 0.9rem;
            color: #7f8c8d;
            font-weight: 500;
            margin-bottom: 0.5rem;
        }
        .metric-value {
            font-size: 1.8rem;
            font-weight: 700;
            color: #2c3e50;
            word-wrap: break-word;
        }


        /* Tabs and Buttons */
        .tabs-header {
            margin-top: 0.5rem;
            margin-bottom: 0.1rem;
        }
        .tabs-header h4 {
            margin: 0;
            font-size: 0.9rem;
            color: #4b5563;
        }
        .stTabs [data-baseweb="tab-list"] {
            gap: 0.25rem;
        }
        .stTabs [data-baseweb="tab"] {
            padding-top: 0.35rem;
            padding-bottom: 0.35rem;
        }
        button[data-testid="stButton-clear_filters_button"] {
            padding: 0.2rem 0.5rem;
            font-size: 0.7rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # ------------- LOAD DATA -------------
    df = load_supplier_data()

    # ---------- FILTER SESSION STATE ----------
    if "supplier_bu" not in st.session_state:
        st.session_state["supplier_bu"] = []
    if "supplier_po_type" not in st.session_state:
        st.session_state["supplier_po_type"] = []
    if "supplier_years" not in st.session_state:
        st.session_state["supplier_years"] = []
    if "supplier_months" not in st.session_state:
        st.session_state["supplier_months"] = []

    # If file is missing / empty
    if df.empty:
        st.error("No data found for Supplier. Please check the Excel file path or content.")
        return

    # ------------- HEADER -------------
    st.markdown("""
    <div style="margin-bottom: 2rem;">
        <h1 class="dashboard-title">🚚 អ្នកផ្គត់ផ្គង់ - Supplier</h1>
        <p class="dashboard-subtitle">PO overview, vendor performance, and comparison dashboard</p>
    </div>
    """, unsafe_allow_html=True)

    # ------------- FILTER BAR (Business Unit / PO Type / Year / Month) -------------
    def clear_filters_callback():
        """Callback to reset all filter session states."""
        st.session_state["supplier_bu"] = []
        st.session_state["supplier_po_type"] = []
        st.session_state["supplier_years"] = []
        st.session_state["supplier_months"] = []

    # --- Clear button at top right, above the filter box ---
    clear_button_row_col1, clear_button_row_col2 = st.columns([0.85, 0.15])
    
    is_filtered = any([st.session_state["supplier_bu"], 
                        st.session_state["supplier_po_type"], 
                        st.session_state["supplier_years"], 
                        st.session_state["supplier_months"]])

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
        st.button("Clear filters", key="clear_filters_button", on_click=clear_filters_callback)

    with st.expander("Filters", expanded=True):
        # --- Filter widgets ---
        fcol1, fcol2, fcol3, fcol4 = st.columns(4)

        with fcol1:
            bu_options = sorted(df["Business Unit"].astype(str).unique()) if "Business Unit" in df.columns else []
            st.multiselect(
                "Business Unit",
                options=bu_options,
                key="supplier_bu",
                placeholder="All business units",
            )

        with fcol2:
            po_type_options = sorted(df["Po Type"].astype(str).unique()) if "Po Type" in df.columns else []
            st.multiselect(
                "PO Type",
                options=po_type_options,
                key="supplier_po_type",
                placeholder="All PO types",
            )

        with fcol3:
            year_options = sorted(df["Year"].astype(str).unique(), reverse=True)
            st.multiselect(
                "Year",
                options=year_options,
                key="supplier_years",
                placeholder="All years",
            )
        
        with fcol4:
            # Ensure months are sorted numerically for the selector
            month_options = sorted(df["Month"].astype(str).unique()) if "Month" in df.columns else []
            st.multiselect(
                "Month",
                options=month_options,
                key="supplier_months",
                placeholder="All months",
            )

    # Apply filters
    filtered = df.copy()

    if st.session_state["supplier_bu"]:
        filtered = filtered[filtered["Business Unit"].astype(str).isin(st.session_state["supplier_bu"])]
    if st.session_state["supplier_po_type"]:
        filtered = filtered[filtered["Po Type"].astype(str).isin(st.session_state["supplier_po_type"])]
    if st.session_state["supplier_years"]:
        filtered = filtered[filtered["Year"].astype(str).isin(st.session_state["supplier_years"])]
    if st.session_state["supplier_months"]:
        filtered = filtered[filtered["Month"].astype(str).isin(st.session_state["supplier_months"])]

    # ------------- KPI CARDS (from real data) -------------
    if not filtered.empty:
        total_spending = filtered["Amount"].sum()
        total_pos = len(filtered)
        vendor_count = filtered["Vendor ID"].nunique() if "Vendor ID" in filtered.columns else 0
        bu_count = filtered["Business Unit"].nunique() if "Business Unit" in filtered.columns else 0
    else:
        total_spending, total_pos, vendor_count, bu_count = 0, 0, 0, 0

    # Display cards with custom HTML
    col1, col2, col3, col4 = st.columns([1, 1, 1, 2])
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Business Units</div>
            <div class="metric-value">{bu_count:,}</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Vendor Count</div>
            <div class="metric-value">{vendor_count:,}</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Total POs</div>
            <div class="metric-value">{total_pos:,}</div>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Total Spending Amount</div>
            <div class="metric-value">៛ {total_spending:,.0f}</div>
        </div>
        """, unsafe_allow_html=True)

    # ------------- AGGREGATED DATA FOR CHARTS -------------
    # PO by Type
    if "Po Type" in filtered.columns:
        po_type_data = filtered.groupby("Po Type", as_index=False).agg(Amount=("Amount", "sum")).sort_values("Amount", ascending=False)
    else:
        po_type_data = pd.DataFrame(columns=["Po Type", "Amount"])

    # Spending by Business Unit
    if "Business Unit" in filtered.columns:
        business_unit_data = filtered.groupby("Business Unit").agg(Amount=("Amount", "sum")).reset_index().sort_values("Amount", ascending=False)
    else:
        business_unit_data = pd.DataFrame(columns=["Business Unit", "Amount"])

    # Top 10 Vendors
    if "Vendor Name" in filtered.columns:
        top_10_vendors = filtered.groupby("Vendor Name")["Amount"].sum().nlargest(10).reset_index()
    else:
        top_10_vendors = pd.DataFrame(columns=["Vendor Name", "Amount"])

    # Monthly trend
    po_data = filtered.groupby("Period", as_index=False).agg(Amount=("Amount", "sum")).sort_values("Period")

    # ------------- TABS -------------
    st.markdown('<div class="tabs-header"><h4>Views</h4></div>', unsafe_allow_html=True)
    tab_overview, tab_analysis, tab_vendor = st.tabs(
        ["📊 Overview ", "📈 Detailed Analysis", "⚖️ Vendors & Performance"]
    )

    # ===== OVERVIEW & TRANSACTIONS TAB =====
    with tab_overview:
        # --- Key Amount Spent Charts ---
        c1, c2 = st.columns(2)
        with c1:
            st.subheader("Amount Spent by PO Type")
            if not po_type_data.empty:
                fig_pie_type = px.pie(
                    po_type_data, 
                    names="Po Type", 
                    values="Amount", 
                    hole=0.4, 
                    title="Amount Spent by PO Type"
                )
                fig_pie_type.update_traces(textinfo='percent+label')
                fig_pie_type.update_layout(margin=dict(l=10, r=10, t=40, b=10), height=300, showlegend=True)
                st.plotly_chart(fig_pie_type, use_container_width=True)
            else:
                st.info("No data for PO types.")

        with c2:
            st.subheader("Amount Spent by Business Unit")

            if not business_unit_data.empty:
                fig_bu_bar = px.bar(
                    business_unit_data,
                    x="Business Unit",
                    y="Amount",
                    labels={
                        "Business Unit": "Business Unit",
                        "Amount": "Total Amount (៛)"
                    },
                    title="Amount Spent by Business Unit",
                )

                # Make the chart tall enough + very wide → page becomes horizontally scrollable
                chart_width = max(800, len(business_unit_data) * 100) # Dynamic width
                fig_bu_bar.update_layout(
                    height=400,
                    width=chart_width,
                    margin=dict(l=10, r=10, t=40, b=120),
                    xaxis_tickangle=-45
                )

                st.plotly_chart(fig_bu_bar, use_container_width=False)
            else:
                st.info("No data for business units.")

        
        st.markdown("---")

        # --- Top 10 Vendors and Monthly Trend ---
        c3, c4 = st.columns(2)
        with c3:
            st.subheader("Top 10 Vendors by Amount")
            if not top_10_vendors.empty:
                fig_bar_vendor = px.bar(
                    top_10_vendors, 
                    x="Vendor Name", 
                    y="Amount", 
                    labels={"Amount": "Total Amount (៛)"},
                    title="Top 10 Vendors by Amount"
                )
                fig_bar_vendor.update_layout(
                    margin=dict(l=10, r=10, t=40, b=10), 
                    height=320,
                    xaxis_tickangle=-45  # Rotate the x-axis labels to -45 degrees
                )
                st.plotly_chart(fig_bar_vendor, use_container_width=True)
            else:
                st.info("No data for vendors.")

        with c4:
            st.subheader("Monthly Spending Trend")
            if not po_data.empty:
                fig_area = px.area(
                    po_data, 
                    x="Period", 
                    y="Amount", 
                    markers=True, 
                    labels={"Amount": "PO Amount (៛)", "Period": "Period (YYYY-MM)"},
                    title="Monthly Spending Trend"
                )
                fig_area.update_layout(margin=dict(l=10, r=10, t=40, b=10), height=320)
                st.plotly_chart(fig_area, use_container_width=True)
            else:
                st.info("No data for monthly trends.")

        st.markdown("---")

        # --- Yearly Spending Comparison ---
        st.subheader("Yearly Spending Comparison")
        yearly_spending = filtered.groupby("Year")["Amount"].sum().reset_index()
        if not yearly_spending.empty:
            fig_yearly_spending = px.bar(
                yearly_spending,
                x="Year",
                y="Amount",
                labels={"Amount": "Total Amount (៛)"},
                title="Total Spending by Year"
            )
            st.plotly_chart(fig_yearly_spending, use_container_width=True)
        else:
            st.info("No data for yearly spending comparison.")

        st.markdown("---")
    
        # --- Supplier Detail Table ---
        st.subheader("Suppiler Detail Table")
        display_cols = [
            c for c in [
                "Business Unit", "Operating Unit", "Po Type", "Account", 
                "Vendor ID", "Vendor Name", "PO Date", "Month", "Year", "Amount"
            ] if c in filtered.columns
        ]
        
        # Format 'Amount' column for display
        display_df = filtered[display_cols].copy()
        display_df['Amount'] = display_df['Amount'].apply(lambda x: f"៛ {x:,.0f}")
        
        st.dataframe(
            display_df.sort_values(by="Amount", ascending=False), # Note: sorting on formatted string might be imperfect
            use_container_width=True,
            height=320,
        )

        
        # Format 'Amount' column for display
        display_df = filtered[display_cols].copy()
        display_df['Amount'] = display_df['Amount'].apply(lambda x: f"៛ {x:,.0f}")
        

    # ===== DETAILED ANALYSIS TAB =====
    with tab_analysis:
        if "Po Type" in filtered.columns and not filtered.empty:
            po_type_analysis = filtered.groupby("Po Type").agg(
                Total_Amount=("Amount", "sum"),
                Number_of_POs=("Amount", "count"),
                Average_PO_Value=("Amount", "mean")
            ).reset_index()
            # PO Type Comparison Bar Chart
            st.subheader("PO Type Comparison")
            # Separate the metrics for plotting
            po_type_analysis_melted = pd.melt(
                po_type_analysis, 
                id_vars='Po Type', 
                value_vars=['Number_of_POs', 'Total_Amount', 'Average_PO_Value'],
                var_name='Metric',
                value_name='Value'
            )
            
            # Create two separate charts for scale readability
            c_count, c_amount = st.columns(2)
            
            with c_count:
                count_data = po_type_analysis_melted[po_type_analysis_melted['Metric'] == 'Number_of_POs']
                fig_count_compare = px.bar(
                    count_data,
                    x="Po Type",
                    y="Value",
                    labels={"Value": "Number of POs"},
                    title="PO Count Comparison by Type",
                    color="Po Type"
                )
                fig_count_compare.update_layout(showlegend=False, margin=dict(t=40))
                st.plotly_chart(fig_count_compare, use_container_width=True)
            
            with c_amount:
                # Change this part to a Pie chart for Total Amount
                amount_data = po_type_analysis_melted[po_type_analysis_melted['Metric'] == 'Total_Amount']
                fig_amount_compare = px.pie(
                    amount_data,
                    names="Po Type",
                    values="Value",
                    title="Total Amount Comparison by PO Type",
                    color="Po Type"
                )
                fig_amount_compare.update_traces(textinfo='percent+label')  
                st.plotly_chart(fig_amount_compare, use_container_width=True)
        else:
            st.info("No PO Type data to analyze.")

        st.markdown("---")

        st.subheader("Business Unit Analysis")
        # Filtered Business Unit Performance Data
        if "Business Unit" in filtered.columns and not filtered.empty:
            # Spending Bar Chart - Top 10 Business Units
            # Group by Business Unit and calculate the total spending
            bu_spending = filtered.groupby("Business Unit")["Amount"].sum().reset_index()

            # Sort by total spending and select top 10 Business Units
            top_10_bu_spending = bu_spending.sort_values("Amount", ascending=False).head(10)

            # Ensure 'Business Unit' is treated as a string
            top_10_bu_spending['Business Unit'] = top_10_bu_spending['Business Unit'].astype(str)

            # Create a bar chart for the top 10 Business Units by spending
            fig_bu_spending = px.bar(
                top_10_bu_spending,
                x="Business Unit",
                y="Amount",
                title="Top 10 Business Units by Total Spending",
                labels={"Amount": "Total Amount (៛)", "Business Unit": "Business Unit"}
            )

            # Update layout: Increase margin for x-axis, rotate labels, and adjust font size
            fig_bu_spending.update_layout(
                xaxis_tickangle=-45,  # Rotate labels by 45 degrees for better readability
                title_font_size=19,   # Set title font size
                xaxis=dict(
                    tickmode='array', 
                    tickvals=top_10_bu_spending['Business Unit'],  
                    ticktext=top_10_bu_spending['Business Unit'],  
                    tickfont=dict(size=12)  
                ),
                margin=dict(l=10, r=10, t=40, b=150) 
            )

            # Display the chart
            st.plotly_chart(fig_bu_spending, use_container_width=True)

            
            # Stacked Bar Chart - PO Amount Spent by Business Unit
            bu_po_dist = filtered.groupby(["Business Unit", "Po Type"])["Amount"].sum().reset_index()
            fig_bu_stacked = px.bar(
                bu_po_dist,
                x="Business Unit",
                y="Amount",
                color="Po Type",
                title="Spending Amount Spent by PO Type per Business Unit",
                labels={"Amount": "Total Amount (៛)"}
            )
            fig_bu_stacked.update_layout(
                xaxis_tickangle=-45,
                title_font_size=19
            )

            st.plotly_chart(fig_bu_stacked, use_container_width=True)


            # Monthly Trend Line Chart
            bu_monthly_trend = filtered.groupby(["Period", "Business Unit"])["Amount"].sum().reset_index()
            fig_bu_trend = px.line(
                bu_monthly_trend,
                x="Period",
                y="Amount",
                color="Business Unit",
                title="Monthly Spending Trend by Business Unit",
                labels={"Amount": "Total Amount (៛)"}
            )
            fig_bu_trend.update_layout(xaxis_tickangle=-45, title_font_size=19  )
            st.plotly_chart(fig_bu_trend, use_container_width=True)
        else:
            st.info("No Business Unit data to analyze.")

        st.markdown("---")

        # --- Yearly Spending Trend ---
        st.subheader("Yearly Spending Trend")
        yearly_analysis = filtered.groupby("Year")["Amount"].sum().reset_index()

        if not yearly_analysis.empty:
            fig_yearly_analysis = px.bar(
                yearly_analysis,
                x="Year",
                y="Amount",
                labels={"Amount": "Total Spending (៛)"},
                title="Total Spending by Year"
            )
            st.plotly_chart(fig_yearly_analysis, use_container_width=True)
        else:
            st.info("No data for yearly spending trend.")

    # ===== VENDORS & PERFORMANCE TAB =====
    with tab_vendor:
        if "Vendor Name" in filtered.columns and not filtered.empty:
            # Top 10 Vendors Ranked List
            st.subheader("Top 10 Vendors Ranked List")
            vendor_performance = filtered.groupby("Vendor Name").agg(
                Total_Spending=("Amount", "sum"),
                Number_of_POs=("Amount", "count"),
                Average_PO_Value=("Amount", "mean")
            ).reset_index().sort_values("Total_Spending", ascending=False)
            
            # Format for display
            vendor_performance_display = vendor_performance.head(10).copy()
            vendor_performance_display['Total_Spending'] = vendor_performance_display['Total_Spending'].apply(lambda x: f"៛ {x:,.0f}")
            vendor_performance_display['Average_PO_Value'] = vendor_performance_display['Average_PO_Value'].apply(lambda x: f"៛ {x:,.0f}")
            
            st.dataframe(vendor_performance_display, use_container_width=True)

            st.markdown("---")

            # Vendor Amount Spent Pie Chart and Scatter Plot (Using Top 10 Data)
            top_10_vendors_for_charts = vendor_performance.head(10).copy()

            c1, = st.columns(1)   

            with c1:
                st.subheader("Top 10 Vendors by Amount Spent")
                fig_vendor_pie = px.pie(
                    top_10_vendors_for_charts,
                    names="Vendor Name",
                    values="Total_Spending",
                    title="Top 10 Vendors by Amount Spent"
                )
                fig_vendor_pie.update_traces(textinfo='percent')
                st.plotly_chart(fig_vendor_pie, use_container_width=True)

            st.markdown("---")


            # Vendor Performance Metrics by PO Type (Top 10 as Bar Chart)
            st.subheader("Top 10 Vendor by PO Types and Amount Spent")

            vendor_po_type_perf = filtered.groupby(["Vendor Name", "Po Type"]).agg(
                Total_Spending=("Amount", "sum"),
                Number_of_POs=("Amount", "count"),
                Average_PO_Value=("Amount", "mean")
            ).reset_index()

            if not vendor_po_type_perf.empty:
                # Get Top 10 by Total Spending
                top10_vendor_po = vendor_po_type_perf.sort_values(
                    "Total_Spending", ascending=False
                ).head(10)

                fig_vendor_po_bar = px.bar(
                    top10_vendor_po,
                    x="Vendor Name",
                    y="Total_Spending",
                    color="Po Type",
                    labels={
                        "Vendor Name": "Vendor",
                        "Total_Spending": "Total Spending (៛)",
                        "Po Type": "PO Type",
                    },
                    title="Top 10 Vendors by PO Type and Amount Spent",
                )

                fig_vendor_po_bar.update_layout(
                    xaxis_tickangle=-45,
                    title_font_size=19,
                    margin=dict(l=10, r=10, t=40, b=120),
                )

                st.plotly_chart(fig_vendor_po_bar, use_container_width=True)
            else:
                st.info("No vendor–PO type performance data to display.")


            st.markdown("---")

            # --- Top 10 Vendors by Year ---
            st.subheader("Top 10 Vendors by Year")
            top_vendors_by_year = filtered.groupby(["Year", "Vendor Name"])["Amount"].sum().reset_index()
            top_vendors_by_year = top_vendors_by_year.loc[top_vendors_by_year.groupby("Year")["Amount"].nlargest(10).reset_index(level=0, drop=True).index]

            if not top_vendors_by_year.empty:
                fig_top_vendors_by_year = px.bar(
                    top_vendors_by_year,
                    x="Year",
                    y="Amount",
                    color="Vendor Name",
                    labels={"Amount": "Total Amount (៛)"},
                    title="Top 10 Vendors by Spending Each Year"
                )
                st.plotly_chart(fig_top_vendors_by_year, use_container_width=True)
            else:
                st.info("No data for top vendors by year.")
        else:
            st.info("No Vendor data to analyze.")


# This ensures the Supplier function runs when the script is executed
if __name__ == "__main__":
    Supplier()