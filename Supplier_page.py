import streamlit as st
import pandas as pd
import plotly.express as px


@st.cache_data
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


def Supplier():
    # ---- HIDE STREAMLIT SPINNER / "RUNNING..." ICON ----
    st.markdown(
        """
        <style>
        /* Hide "Running..." spinner under the title */
        .stSpinner, .stSpinner > div {
            display: none !important;
        }
        /* Hide the top-right running status widget */
        [data-testid="stStatusWidget"] {
            display: none !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # ------------- PAGE STYLES -------------
    st.markdown(
        """
        <style>
        .block-container {
            padding-top: 1rem;
            padding-bottom: 2rem;
            max-width: 1400px;
        }
        .supplier-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0.75rem 0 1rem 0;
            border-bottom: 1px solid #e5e7eb;
            margin-bottom: 0.75rem;
        }
        .supplier-title {
            display: flex;
            align-items: center;
            gap: 0.6rem;
        }
        .supplier-logo {
            width: 40px;
            height: 40px;
            border-radius: 999px;
            background: linear-gradient(135deg, #2563eb, #059669);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: 700;
            font-size: 0.9rem;
        }
        .supplier-title-text {
            font-size: 1.6rem;
            font-weight: 700;
            color: #111827;
        }
        .supplier-subtitle {
            font-size: 0.85rem;
            color: #6b7280;
        }
        .kpi-grid {
            display: grid;
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 0.75rem;
            margin-bottom: 0.75rem;
        }
        @media (max-width: 1100px) {
            .kpi-grid {
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }
        }
        @media (max-width: 700px) {
            .kpi-grid {
                grid-template-columns: 1fr;
            }
        }
        .kpi-card {
            background: white;
            border-radius: 0.75rem;
            border: 1px solid #e5e7eb;
            padding: 0.85rem 1rem;
            box-shadow: 0 8px 18px rgba(15, 23, 42, 0.03);
        }
        .kpi-label {
            font-size: 0.75rem;
            color: #6b7280;
            margin-bottom: 0.15rem;
        }
        .kpi-value {
            font-size: 1.4rem;
            font-weight: 700;
            color: #111827;
            margin-bottom: 0.15rem;
        }
        .kpi-trend {
            font-size: 0.75rem;
            font-weight: 600;
        }
        .kpi-trend-up {
            color: #059669;
        }
        .kpi-trend-down {
            color: #ea580c;
        }
        .filter-bar {
            background: #f9fafb;
            border-radius: 0.75rem;
            border: 1px solid #e5e7eb;
            padding: 0.8rem 1rem 0.2rem 1rem;
            margin-bottom: 0.9rem;
        }
        .filter-bar-title {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 0.4rem;
        }
        .filter-bar-title h3 {
            font-size: 0.95rem;
            font-weight: 600;
            margin: 0;
            color: #111827;
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

    # If file is missing / empty
    if df.empty:
        st.error("No data found for Supplier. Please check the Excel file path.")
        return

    # ------------- HEADER -------------
    st.markdown(
        """
        <div class="supplier-header">
            <div class="supplier-title">
                <div class="supplier-logo">FM</div>
                <div>
                    <div class="supplier-title-text">Supplier Management Workspace</div>
                    <div class="supplier-subtitle">PO overview, vendor performance, and comparison dashboard</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ------------- KPI CARDS (from real data) -------------
    total_vendors = df["Vendor ID"].nunique() if "Vendor ID" in df.columns else 0
    total_po = len(df)
    total_amount = df["Amount"].sum() if "Amount" in df.columns else 0
    avg_po_value = df["Amount"].mean() if "Amount" in df.columns and total_po > 0 else 0

    kpis = [
        {
            "label": "Total Vendors",
            "value": f"{total_vendors:,}",
            "trend": "+0.0%",
            "positive": True,
        },
        {
            "label": "Total Purchase Orders",
            "value": f"{total_po:,}",
            "trend": "+0.0%",
            "positive": True,
        },
        {
            "label": "Total PO Amount",
            "value": f"៛ {total_amount:,.0f}",
            "trend": "+0.0%",
            "positive": True,
        },
        {
            "label": "Average PO Value",
            "value": f"៛ {avg_po_value:,.0f}",
            "trend": "+0.0%",
            "positive": False,
        },
    ]

    st.markdown('<div class="kpi-grid">', unsafe_allow_html=True)
    for kpi in kpis:
        trend_class = "kpi-trend-up" if kpi["positive"] else "kpi-trend-down"
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-label">{kpi['label']}</div>
                <div class="kpi-value">{kpi['value']}</div>
                <div class="kpi-trend {trend_class}">{kpi['trend']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)

    # ------------- FILTER BAR (Business Unit / PO Type / Year) -------------
    st.markdown(
        """
        <div class="filter-bar">
            <div class="filter-bar-title">
                <h3>Filters</h3>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    header_col1, header_col2 = st.columns([4, 1])
    with header_col1:
        st.caption("Leave filters empty to show all data.")

    with header_col2:
        clear_clicked = st.button("Clear filters", key="clear_filters")

    # If user clicks clear → reset selections & rerun
    if clear_clicked:
        st.session_state["supplier_bu"] = []
        st.session_state["supplier_po_type"] = []
        st.session_state["supplier_years"] = []
        st.rerun()   # <--- updated for new Streamlit

    # --- Filter widgets ---
    fcol1, fcol2, fcol3, fcol4 = st.columns([2, 2, 2, 1])

    with fcol1:
        bu_options = sorted(df["Business Unit"].astype(str).unique()) if "Business Unit" in df.columns else []
        selected_bu = st.multiselect(
            "Business Unit",
            options=bu_options,
            key="supplier_bu",
            placeholder="All business units",
        )

    with fcol2:
        po_type_options = sorted(df["Po Type"].astype(str).unique()) if "Po Type" in df.columns else []
        selected_po_type = st.multiselect(
            "PO Type",
            options=po_type_options,
            key="supplier_po_type",
            placeholder="All PO types",
        )

    with fcol3:
        year_options = sorted(df["Year"].astype(str).unique())
        selected_years = st.multiselect(
            "Year",
            options=year_options,
            key="supplier_years",
            placeholder="All years",
        )

    with fcol4:
        st.write("")
        st.caption("Filters update automatically")

    # Apply filters
    filtered = df.copy()

    if selected_bu:
        filtered = filtered[filtered["Business Unit"].astype(str).isin(selected_bu)]
    if selected_po_type:
        filtered = filtered[filtered["Po Type"].astype(str).isin(selected_po_type)]
    if selected_years:
        filtered = filtered[filtered["Year"].astype(str).isin(selected_years)]

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
        )
    else:
        business_unit_data = pd.DataFrame(columns=["Business Unit", "Amount", "Vendors"])

    # Vendor summary
    if "Vendor Name" in filtered.columns:
        vendor_summary = (
            filtered.groupby("Vendor Name")
            .agg(Amount=("Amount", "sum"), OUs=("Operating Unit", "nunique"))
            .reset_index()
            .sort_values("Amount", ascending=False)
        )
        vendor_summary["Status"] = "Active"
    else:
        vendor_summary = pd.DataFrame(columns=["Vendor Name", "Amount", "OUs", "Status"])

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
            st.subheader("Spending by Business Unit")
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
            st.subheader("Top Vendors by Amount")
            if not vendor_summary.empty:
                top_vendors = vendor_summary.rename(columns={"Vendor Name": "Vendor"})
                st.dataframe(
                    top_vendors[["Vendor", "Amount", "OUs", "Status"]],
                    use_container_width=True,
                    height=280,
                )
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

    # ===== ANALYSIS TAB =====
    with tab_analysis:
        st.subheader("Procurement Analytics")

        inner_tab1, inner_tab2, inner_tab3 = st.tabs(["PO Count by BU", "Amount by BU", "Amount by PO Type"])

        with inner_tab1:
            if "Business Unit" in filtered.columns:
                tmp = (
                    filtered.groupby("Business Unit")
                    .size()
                    .reset_index(name="PO Count")
                    .sort_values("PO Count", ascending=False)
                )
                fig = px.bar(tmp, x="Business Unit", y="PO Count")
                fig.update_layout(margin=dict(l=10, r=10, t=10, b=10), height=320)
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("No data for current filters.")

        with inner_tab2:
            if "Business Unit" in filtered.columns:
                tmp = (
                    filtered.groupby("Business Unit")["Amount"]
                    .sum()
                    .reset_index()
                    .sort_values("Amount", ascending=False)
                )
                fig = px.bar(tmp, x="Business Unit", y="Amount", labels={"Amount": "Total Amount (៛)"})
                fig.update_layout(margin=dict(l=10, r=10, t=10, b=10), height=320)
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("No data for current filters.")

        with inner_tab3:
            if "Po Type" in filtered.columns:
                tmp = (
                    filtered.groupby("Po Type")["Amount"]
                    .sum()
                    .reset_index()
                    .sort_values("Amount", ascending=False)
                )
                fig = px.bar(tmp, x="Po Type", y="Amount", labels={"Amount": "Total Amount (៛)"})
                fig.update_layout(margin=dict(l=10, r=10, t=10, b=10), height=320)
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("No data for current filters.")

        st.markdown("---")
        st.subheader("Vendor Performance Metrics (placeholder)")

        metrics = [
            {"metric": "Unique Business Units", "value": df["Business Unit"].nunique(), "trend": ""},
            {"metric": "Unique Operating Units", "value": df["Operating Unit"].nunique(), "trend": ""},
            {"metric": "Median PO Amount", "value": f"៛ {df['Amount'].median():,.0f}", "trend": ""},
        ]

        for m in metrics:
            st.markdown(
                f"""
                <div style="
                    display:flex;
                    align-items:center;
                    justify-content:space-between;
                    padding:0.55rem 0.75rem;
                    margin-bottom:0.4rem;
                    border-radius:0.65rem;
                    border:1px solid #e5e7eb;
                    background:white;
                ">
                    <div>
                        <div style="font-size:0.9rem;font-weight:600;color:#111827;">{m['metric']}</div>
                        <div style="font-size:0.8rem;color:#6b7280;margin-top:0.1rem;">{m['value']}</div>
                    </div>
                    <span style="font-size:0.8rem;font-weight:600;color:#059669;">{m['trend']}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )

    # ===== COMPARISON TAB =====
    with tab_comparison:
        st.subheader("Vendor Comparison Table")

        if "Vendor Name" in df.columns:
            comp = (
                filtered.groupby("Vendor Name")
                .agg(
                    PO_Count=("Amount", "size"),
                    Amount=("Amount", "sum"),
                    Avg_PO=("Amount", "mean"),
                )
                .reset_index()
                .sort_values("Amount", ascending=False)
            ).head(15)

            comp["Total Amount"] = comp["Amount"].apply(lambda v: f"៛ {v:,.0f}")
            comp["Average PO Value"] = comp["Avg_PO"].apply(lambda v: f"៛ {v:,.0f}")

            comp_display = comp.rename(columns={"Vendor Name": "Vendor"})[
                ["Vendor", "PO_Count", "Total Amount", "Average PO Value"]
            ]

            st.dataframe(comp_display, use_container_width=True, height=360)
        else:
            st.info("Vendor information is not available.")
