import streamlit as st
import pandas as pd
import plotly.express as px


@st.cache_data(show_spinner=False)
def load_supplier_data():
    # supplier data path
    file_path = "Excel files/Supplier.xlsx"

    # Read as text first, then clean/convert
    df = pd.read_excel(file_path, dtype=str)

    # Strip spaces around column names (your AMOUNT column has spaces)
    df = df.rename(columns=lambda c: c.strip())

    # Standardize column names for easier use below
    rename_map = {
        "BUSINESS UNIT": "Business Unit",
        "OPERATING UNIT": "Operating Unit",
        "PO TYPE": "Po Type",           # name matches usage below
        "ACCOUNT": "Account",
        "VENDOR ID": "Vendor ID",
        "VENDOR DESCR": "Vendor Name",
        "PO DATE": "PO Date",
        "MONTH": "Month",
        "YEAR": "Year",
        "AMOUNT": "Amount",
        "AMOUNT ": "Amount",            # just in case there is a trailing space
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

    # Parse PO Date
    if "Po Date" in df.columns:
        # safeguard in case Excel changed name
        df["PO Date"] = df["Po Date"]
    if "PO Date" in df.columns:
        df["PO Date"] = pd.to_datetime(df["PO Date"], errors="coerce")

    # Ensure Month / Year as string
    if "Year" in df.columns:
        df["Year"] = df["Year"].astype(str)
    else:
        df["Year"] = df["PO Date"].dt.year.astype("Int64").astype(str)

    if "Month" in df.columns:
        df["Month"] = df["Month"].astype(str).str.zfill(2)
    else:
        df["Month"] = df["PO Date"].dt.month.astype("Int64").astype(str).str.zfill(2)

    # Period (YYYY-MM) for charts
    if "PO Date" in df.columns:
        df["Period"] = df["PO Date"].dt.to_period("M").astype(str)
    else:
        df["Period"] = df["Year"] + "-" + df["Month"]

    return df


def calculate_percentage_change(current, previous):
    if previous == 0:
        return 0  # Avoid division by zero
    return ((current - previous) / previous) * 100


def create_metric_card(title, value, delta, delta_color):
    """Creates a styled HTML card for a metric."""
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
        .metric-card {
            background: white;
            border-radius: 8px;
            padding: 1.5rem;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
            border: 1px solid #e0e0e0;
            transition: all 0.3s ease;
            height: 100%;
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
        }
        .metric-delta {
            font-size: 0.85rem;
            font-weight: 500;
            margin-top: 0.5rem;
        }
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
        /* Custom CSS for smaller Clear filters button */
        button[data-testid="stButton-clear_filters_button"] {
            padding: 0.2rem 0.5rem; /* Smaller padding */
            font-size: 0.7rem; /* Smaller font size */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # ------------- LOAD DATA -------------
    df = load_supplier_data()

    # ---------- FILTER SESSION STATE ----------
    if "supplier_bu" not in st.session_state:
        st.session_state["supplier_bu"] = []       # empty = all BUs
    if "supplier_po_type" not in st.session_state:
        st.session_state["supplier_po_type"] = []  # empty = all PO Types
    if "supplier_years" not in st.session_state:
        st.session_state["supplier_years"] = []    # empty = all Years
    if "supplier_months" not in st.session_state:
        st.session_state["supplier_months"] = []   # empty = all Months

    # If file is missing / empty
    if df.empty:
        st.error("No data found for Supplier. Please check the Excel file path.")
        return

    # ------------- HEADER -------------
    st.markdown("""
    <div style="margin-bottom: 2rem;">
        <h1 class="dashboard-title">🚚 Supplier Dashboard</h1>
        <p class="dashboard-subtitle">PO overview, vendor performance, and comparison dashboard</p>
    </div>
    """, unsafe_allow_html=True)

    # ------------- FILTER BAR (Business Unit / PO Type / Year / Month) -------------
    def clear_filters_callback():
        st.session_state["supplier_bu"] = []
        st.session_state["supplier_po_type"] = []
        st.session_state["supplier_years"] = []
        st.session_state["supplier_months"] = []

    # --- Clear button at top right, above the filter box ---
    clear_button_row_col1, clear_button_row_col2 = st.columns([0.85, 0.15])
    with clear_button_row_col1:
        st.markdown("""
        <div style="background-color: #e0f2f7; border-left: 5px solid #007bff; padding: 5px 10px; border-radius: 3px; display: inline-block;">
            <p style="font-size: 0.75rem; margin: 0; color: #0056b3;">No filters selected: displaying all available data.</p>
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
            year_options = sorted(df["Year"].astype(str).unique())
            st.multiselect(
                "Year",
                options=year_options,
                key="supplier_years",
                placeholder="All years",
            )
        
        with fcol4:
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
    # Calculate the most recent period and the previous period
    if not filtered.empty:
        latest_period = filtered["Period"].max()
        previous_period = str(int(latest_period.split("-")[0]) - 1) + "-" + latest_period.split("-")[1]

        # Calculate current and previous values for Total Vendors, Total PO Amount, and Average PO Value
        total_vendors = filtered[filtered["Period"] == latest_period]["Vendor ID"].nunique()
        prev_total_vendors = df[df["Period"] == previous_period]["Vendor ID"].nunique()
        total_po_count = filtered[filtered["Period"] == latest_period].shape[0]
        prev_total_po_count = df[df["Period"] == previous_period].shape[0]
        total_amount = filtered[filtered["Period"] == latest_period]["Amount"].sum()
        prev_total_amount = df[df["Period"] == previous_period]["Amount"].sum()

        # Calculate percentage changes
        vendor_change = calculate_percentage_change(total_vendors, prev_total_vendors)
        po_count_change = calculate_percentage_change(total_po_count, prev_total_po_count)
        po_amount_change = calculate_percentage_change(total_amount, prev_total_amount)
    else:
        total_vendors, vendor_change = 0, 0
        total_po_count, po_count_change = 0, 0
        total_amount, po_amount_change = 0, 0
        latest_period = "N/A"
        previous_period = "N/A"

    # Display cards with `st.metric` (showing current values + trends)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(create_metric_card(
            "Total Vendors",
            f"{total_vendors:,}",
            f"{vendor_change:+.1f}% vs {previous_period}",
            "#059669" if vendor_change >= 0 else "#ea580c"
        ), unsafe_allow_html=True)
    with col2:
        st.markdown(create_metric_card(
            "Total Purchase Orders",
            f"{total_po_count:,}",
            f"{po_count_change:+.1f}% vs {previous_period}",
            "#059669" if po_count_change >= 0 else "#ea580c"
        ), unsafe_allow_html=True)
    with col3:
        st.markdown(create_metric_card(
            "Total PO Amount",
            f"៛ {total_amount:,.0f}",
            f"{po_amount_change:+.1f}% vs {previous_period}",
            "#059669" if po_amount_change >= 0 else "#ea580c"
        ), unsafe_allow_html=True)

    # ------------- AGGREGATED DATA FOR CHARTS -------------
    # Monthly trend
    po_data = (
        filtered.groupby("Period", as_index=False)
        .agg(Amount=("Amount", "sum"), PO_Count=("Amount", "size"))
        .sort_values("Period")
    )

    # PO by Type
    if "Po Type" in filtered.columns:
        po_type_data = (
            filtered.groupby("Po Type", as_index=False)
            .agg(Amount=("Amount", "sum"))
            .sort_values("Amount", ascending=False)
        )
    else:
        po_type_data = pd.DataFrame(columns=["Po Type", "Amount"])

    # Spending by Business Unit
    if "Business Unit" in filtered.columns:
        business_unit_data = (
            filtered.groupby("Business Unit")
            .agg(Amount=("Amount", "sum"), Vendors=("Vendor ID", "nunique"))
            .reset_index()
            .sort_values("Amount", ascending=False)
            .head(10)  # Get top 10
        )
    else:
        business_unit_data = pd.DataFrame(columns=["Business Unit", "Amount", "Vendors"])

    # Vendor summary for stacked bar chart
    if "Vendor Name" in filtered.columns and "Po Type" in filtered.columns:
        # First, find the top 10 vendors by total amount
        top_vendors_names = filtered.groupby("Vendor Name")["Amount"].sum().nlargest(10).index
        
        # Filter the dataframe to only include these top vendors
        top_vendors_df = filtered[filtered["Vendor Name"].isin(top_vendors_names)]
        
        # Now, group by both Vendor Name and Po Type for stacking
        vendor_po_type_summary = (
            top_vendors_df.groupby(["Vendor Name", "Po Type"])
            .agg(Amount=("Amount", "sum"))
            .reset_index()
            .sort_values("Amount", ascending=False)
        )
    else:
        vendor_po_type_summary = pd.DataFrame(columns=["Vendor Name", "Po Type", "Amount"])

    # ------------- TABS -------------
    st.markdown('<div class="tabs-header"><h4>Views</h4></div>', unsafe_allow_html=True)
    tab_overview, tab_analysis, tab_comparison = st.tabs(
        ["📊 Overview", "📈 Detailed Analysis", "⚖️ Vendor Comparison"]
    )

    # ===== OVERVIEW TAB =====
    with tab_overview:
        c1, c2 = st.columns(2)

        with c1:
            st.subheader("Monthly PO Trends")
            if not po_data.empty:
                fig_line = px.line(
                    po_data,
                    x="Period",
                    y="Amount",
                    markers=True,
                    labels={"Amount": "PO Amount (៛)", "Period": "Period (YYYY-MM)"},
                )
                fig_line.update_layout(margin=dict(l=10, r=10, t=10, b=10), height=320)
                st.plotly_chart(fig_line, use_container_width=True)
            else:
                st.info("No data for current filters.")

        with c2:
            st.subheader("PO by Type")
            if not po_type_data.empty:
                fig_pie = px.pie(
                    po_type_data,
                    names="Po Type",
                    values="Amount",
                    hole=0.4,
                )
                fig_pie.update_layout(margin=dict(l=10, r=10, t=10, b=10), height=320)
                st.plotly_chart(fig_pie, use_container_width=True)
            else:
                st.info("No data for current filters.")

        st.markdown("---")

        c3, c4 = st.columns(2)

        with c3:
            st.subheader("Top 10 Spending by Business Unit")
            if not business_unit_data.empty:
                fig_bar = px.bar(
                    business_unit_data,
                    x="Business Unit",
                    y="Amount",
                    labels={"Amount": "Total Amount (៛)"},
                )
                fig_bar.update_layout(margin=dict(l=10, r=10, t=10, b=10), height=280)
                st.plotly_chart(fig_bar, use_container_width=True)
            else:
                st.info("No data for current filters.")

        with c4:
            st.subheader("Top 10 Vendors by Amount")
            if not vendor_po_type_summary.empty:
                fig_vendor_bar = px.bar(
                    vendor_po_type_summary,
                    x="Vendor Name",
                    y="Amount",
                    color="Po Type",  # This creates the stacking
                    labels={"Amount": "Total Amount (៛)", "Vendor Name": "Vendor"},
                )
                fig_vendor_bar.update_layout(margin=dict(l=10, r=10, t=10, b=10), height=280)
                st.plotly_chart(fig_vendor_bar, use_container_width=True)
            else:
                st.info("No data for current filters.")

        st.markdown("---")
        st.subheader("Purchase Order Details")
        display_cols = [
            c
            for c in [
                "Business Unit",
                "Operating Unit",
                "Po Type",
                "Account",
                "Vendor ID",
                "Vendor Name",
                "PO Date",
                "Month",
                "Year",
                "Amount",
            ]
            if c in filtered.columns
        ]
        st.dataframe(
            filtered[display_cols].sort_values("Amount", ascending=False),
            use_container_width=True,
            height=320,
        )
