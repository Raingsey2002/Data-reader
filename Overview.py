import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# ─────────────────────────────────────────────
# Data loaders  (cached so they run only once)
# ─────────────────────────────────────────────

@st.cache_data(show_spinner=False)
def load_ou_data():
    df = pd.read_parquet("Excel files/OU_df_merged.parquet").fillna("")
    df = df.astype(str)
    df["EFF_STATUS"] = df["EFF_STATUS"].map({"A": "Active", "I": "Inactive"})
    return df


@st.cache_data(show_spinner=False)
def load_economic_data():
    df = pd.read_parquet("Excel files/Economic_df_merged.parquet").fillna("")
    df = df.astype(str)
    df["EFF_STATUS"] = df["EFF_STATUS"].map({"A": "Active", "I": "Inactive"})
    return df



@st.cache_data(show_spinner=False)
def load_program_data():
    df = pd.read_parquet("Excel files/Program_df_merged.parquet").fillna("")
    df = df.astype(str)
    df["EFF_STATUS"] = df["EFF_STATUS"].map({"A": "Active", "I": "Inactive"})
    return df


@st.cache_data(show_spinner=False)
def load_geo_data():
    df = pd.read_parquet("Excel files/Geographyfordatareader.parquet").fillna("")
    df= df.astype(str)
    df["EFF_STATUS"] = df["EFF_STATUS"].map({"A": "Active", "I": "Inactive"})
    return df


@st.cache_data(show_spinner=False)
def load_fmis_data():
    df = pd.read_parquet("Excel files/FMIS Entity all CMB01.parquet").fillna("")
    df = df.astype(str)
    df["EFF_STATUS"] = df["EFF_STATUS"].map({"A": "Active", "I": "Inactive"})
    return df


@st.cache_data(show_spinner=False)
def load_supplier_data():
    try:
        df = pd.read_parquet("Excel files/Supplier.parquet").fillna("")
        df = df.astype(str)
        df = df.rename(columns=lambda c: c.strip())
        rename_map = {
            "BUSINESS UNIT": "Business Unit",
            "VENDOR ID": "Vendor ID",
            "VENDOR DESCR": "Vendor Name",
            "VENDOR DESCRIPTION": "Vendor Name",
            "PO TYPE": "Po Type",
            "AMOUNT": "Amount",
            "AMOUNT ": "Amount",
            "YEAR": "Year",
        }
        df = df.rename(columns={k: v for k, v in rename_map.items() if k in df.columns})
        if "Amount" in df.columns:
            df["Amount"] = (
                df["Amount"]
                .astype(str)
                .str.replace(",", "", regex=False)
                .str.replace(" ", "", regex=False)
            )
            df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce").fillna(0)
        else:
            df["Amount"] = 0
        return df
    except Exception:
        return pd.DataFrame()


# ─────────────────────────────────────────────
# Helper: styled metric card (HTML)
# ─────────────────────────────────────────────

def metric_card(icon, title, value, subtitle="", color="#3b82f6"):
    return f"""
    <div style="
        background: white;
        border-radius: 14px;
        padding: 1.3rem 1.5rem;
        box-shadow: 0 2px 12px rgba(0,0,0,0.07);
        border-left: 5px solid {color};
        height: 100%;
        font-family: 'Noto Sans Khmer', 'Inter', Arial, sans-serif;
    ">
        <div style="font-size: 2rem; margin-bottom: 0.3rem;">{icon}</div>
        <div style="font-size: 0.8rem; font-weight: 600; color: #6b7280;
                    text-transform: uppercase; letter-spacing: 0.05em;">
            {title}
        </div>
        <div style="font-size: 2rem; font-weight: 800; color: #111827;
                    margin: 0.25rem 0 0.15rem 0; line-height:1.1;">
            {value}
        </div>
        <div style="font-size: 0.78rem; color: #9ca3af;">{subtitle}</div>
    </div>
    """


def section_header(text, emoji=""):
    st.markdown(
        f"""<div style="
            display: flex; align-items: center; gap: 0.5rem;
            margin: 2rem 0 1rem 0;
            border-bottom: 2px solid #e5e7eb;
            padding-bottom: 0.4rem;
        ">
            <span style="font-size:1.5rem;">{emoji}</span>
            <h2 style="margin:0; font-size:1.25rem; font-weight:700;
                       color:#1f2937; font-family:'Noto Sans Khmer',Arial,sans-serif;">
                {text}
            </h2>
        </div>""",
        unsafe_allow_html=True,
    )


# ─────────────────────────────────────────────
# Main page
# ─────────────────────────────────────────────

def Overview_page():
    # ── Page padding ──
    st.markdown(
        """
        <style>
            .block-container { padding-top: 1rem; padding-bottom: 3rem; }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # ── Hero header ──
    st.markdown(
        """
        <div style="font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
           <h1 style="
            margin:0;
            font-size:2.5rem;
            font-weight:700;
            margin-bottom:0.5rem;
            letter-spacing:-0.02em; ">
            📊 ទិដ្ឋភាពទូទៅ – Overview Dashboard
        </h1>
        
        <p style="font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;color: #7f8c8d;font-size: 1rem;margin-bottom: 2rem;">ព័ត៌មានសង្ខេបនៃប្រព័ន្ធ FMIS — Financial Management Information System</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ════════════════════════════════════════════
    # Load all datasets
    # ════════════════════════════════════════════
    with st.spinner("📂 កំពុងផ្ទុកទិន្នន័យ..."):
        try:
            ou_df        = load_ou_data()
            has_ou       = True
        except Exception:
            ou_df        = pd.DataFrame()
            has_ou       = False

        try:
            eco_df       = load_economic_data()
            has_eco      = True
        except Exception:
            eco_df       = pd.DataFrame()
            has_eco      = False

        try:
            prog_df      = load_program_data()
            has_prog     = True
        except Exception:
            prog_df      = pd.DataFrame()
            has_prog     = False

        try:
            geo_df       = load_geo_data()
            has_geo      = True
        except Exception:
            geo_df       = pd.DataFrame()
            has_geo      = False

        try:
            fmis_df      = load_fmis_data()
            has_fmis     = True
        except Exception:
            fmis_df      = pd.DataFrame()
            has_fmis     = False

        try:
            supplier_df  = load_supplier_data()
            has_supplier = not supplier_df.empty
        except Exception:
            supplier_df  = pd.DataFrame()
            has_supplier = False

    # ════════════════════════════════════════════
    # ── Section 1 : Top KPI Cards ──
    # ════════════════════════════════════════════
    section_header("ការណែនាំ KPI សំខាន់ – Key Metrics", "📌")

    # Compute values
    ou_active   = len(ou_df[ou_df["EFF_STATUS"] == "Active"]) if has_ou else "N/A"
    eco_active  = len(eco_df[eco_df["EFF_STATUS"] == "Active"]) if has_eco else "N/A"
    prog_active = len(prog_df[prog_df["EFF_STATUS"] == "Active"]) if has_prog else "N/A"
    geo_total   = len(geo_df) if has_geo else "N/A"

    fmis_bu     = fmis_df["BUSINESS_UNIT"].nunique() if has_fmis and "BUSINESS_UNIT" in fmis_df.columns else "N/A"
    fmis_ou     = fmis_df["OPERATING_UNIT"].nunique() if has_fmis and "OPERATING_UNIT" in fmis_df.columns else "N/A"

    vendor_count = supplier_df["Vendor ID"].nunique() if has_supplier and "Vendor ID" in supplier_df.columns else "N/A"
    total_spend  = supplier_df["Amount"].sum() if has_supplier else 0

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(
            metric_card("🏢", "អង្គភាពប្រតិបត្តិ (Active)", f"{ou_active:,}" if isinstance(ou_active, int) else ou_active,
                        "Operating Units – Active", "#2563eb"),
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            metric_card("📊", "មាតិកាគណនី (Active)", f"{eco_active:,}" if isinstance(eco_active, int) else eco_active,
                        "Economic Accounts – Active", "#7c3aed"),
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            metric_card("📋", "កម្មវិធី (Active)", f"{prog_active:,}" if isinstance(prog_active, int) else prog_active,
                        "Programs – Active", "#059669"),
            unsafe_allow_html=True,
        )
    with c4:
        st.markdown(
            metric_card("🌍", "ទីតាំងភូមិសាស្ត្រ", f"{geo_total:,}" if isinstance(geo_total, int) else geo_total,
                        "Geographic Locations (All)", "#d97706"),
            unsafe_allow_html=True,
        )

    st.markdown("<div style='margin-top:1rem;'></div>", unsafe_allow_html=True)

    c5, c6, c7, c8 = st.columns(4)
    with c5:
        st.markdown(
            metric_card("🏛️", "Business Units (FMIS)", f"{fmis_bu:,}" if isinstance(fmis_bu, int) else fmis_bu,
                        "FMIS Entity – All Levels", "#0891b2"),
            unsafe_allow_html=True,
        )
    with c6:
        st.markdown(
            metric_card("🏗️", "Operating Units (FMIS)", f"{fmis_ou:,}" if isinstance(fmis_ou, int) else fmis_ou,
                        "FMIS Entity – All Levels", "#6366f1"),
            unsafe_allow_html=True,
        )
    with c7:
        st.markdown(
            metric_card("🚚", "អ្នកផ្គត់ផ្គង់ (Vendors)", f"{vendor_count:,}" if isinstance(vendor_count, int) else vendor_count,
                        "Unique Supplier Vendors", "#be185d"),
            unsafe_allow_html=True,
        )
    with c8:
        spend_display = f"${total_spend/1_000_000:.1f}M" if isinstance(total_spend, (int, float)) and total_spend > 0 else "N/A"
        st.markdown(
            metric_card("💰", "សរុបការចំណាយ", spend_display,
                        "Total Supplier Spending", "#b45309"),
            unsafe_allow_html=True,
        )

    st.markdown("<div style='margin-top:1.5rem;'></div>", unsafe_allow_html=True)

    # ════════════════════════════════════════════
    # ── Section 2 : Status Breakdown per Module ──
    # ════════════════════════════════════════════
    section_header("ស្ថានភាព Active / Inactive – Status Breakdown", "📈")

    modules = []
    if has_ou and "EFF_STATUS" in ou_df.columns:
        vc = ou_df["EFF_STATUS"].value_counts()
        modules.append({"Module": "អង្គភាពប្រតិបត្តិ", "Active": vc.get("Active", 0), "Inactive": vc.get("Inactive", 0)})
    if has_eco and "EFF_STATUS" in eco_df.columns:
        vc = eco_df["EFF_STATUS"].value_counts()
        modules.append({"Module": "មាតិកាគណនី", "Active": vc.get("Active", 0), "Inactive": vc.get("Inactive", 0)})
    if has_prog and "EFF_STATUS" in prog_df.columns:
        vc = prog_df["EFF_STATUS"].value_counts()
        modules.append({"Module": "កម្មវិធី", "Active": vc.get("Active", 0), "Inactive": vc.get("Inactive", 0)})

    if modules:
        status_df = pd.DataFrame(modules)
        status_melted = status_df.melt(id_vars="Module", var_name="Status", value_name="Count")

        col_chart, col_pie = st.columns([3, 2])
        with col_chart:
            fig_bar = px.bar(
                status_melted,
                x="Module",
                y="Count",
                color="Status",
                barmode="group",
                color_discrete_map={"Active": "#22c55e", "Inactive": "#ef4444"},
                template="plotly_white",
                title="Active vs Inactive by Module",
            )
            fig_bar.update_layout(
                height=350,
                margin=dict(t=45, b=20, l=10, r=10),
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
                plot_bgcolor="rgba(0,0,0,0)",
                paper_bgcolor="rgba(0,0,0,0)",
                xaxis=dict(title=None),
                yaxis=dict(title="Count", gridcolor="#f3f4f6"),
            )
            st.plotly_chart(fig_bar, use_container_width=True)

        with col_pie:
            total_active   = sum(m["Active"] for m in modules)
            total_inactive = sum(m["Inactive"] for m in modules)
            fig_donut = px.pie(
                values=[total_active, total_inactive],
                names=["Active", "Inactive"],
                color_discrete_sequence=["#22c55e", "#ef4444"],
                hole=0.55,
                title="Overall Active Ratio",
            )
            fig_donut.update_layout(
                height=350,
                margin=dict(t=45, b=20, l=10, r=10),
                paper_bgcolor="rgba(0,0,0,0)",
                showlegend=True,
            )
            fig_donut.update_traces(
                textinfo="percent+label",
                hovertemplate="<b>%{label}</b><br>Count: %{value:,}<extra></extra>",
            )
            st.plotly_chart(fig_donut, use_container_width=True)
    else:
        st.info("ទិន្នន័យស្ថានភាពមិនអាចផ្ទុកបានទេ។")

    # ════════════════════════════════════════════
    # ── Section 3 : Geography & FMIS Entity ──
    # ════════════════════════════════════════════
    section_header("ទិន្នន័យភូមិសាស្ត្រ & ការតំណាងស្ថាប័ន", "🌏")

    col_geo, col_fmis = st.columns(2)

    with col_geo:
        if has_geo and "group" in geo_df.columns:
            group_counts = geo_df["group"].value_counts().reset_index()
            group_counts.columns = ["Category", "Count"]
            group_counts = group_counts[group_counts["Category"].astype(str) != "3"]

            fig_geo = px.pie(
                group_counts,
                values="Count",
                names="Category",
                hole=0.45,
                color_discrete_sequence=px.colors.sequential.Blues_r,
                template="plotly_white",
                title="Geographic Records by Category",
            )
            fig_geo.update_layout(
                height=340,
                margin=dict(t=45, b=10, l=10, r=10),
                paper_bgcolor="rgba(0,0,0,0)",
            )
            fig_geo.update_traces(
                textinfo="percent+label",
                marker=dict(line=dict(color="white", width=2)),
            )
            st.plotly_chart(fig_geo, use_container_width=True)
        else:
            st.info("ទិន្នន័យភូមិសាស្ត្រមិនអាចផ្ទុកបានទេ។")

    with col_fmis:
        if has_fmis and "National Level" in fmis_df.columns and "BUSINESS_UNIT" in fmis_df.columns:
            level_counts = (
                fmis_df.groupby("National Level")["BUSINESS_UNIT"]
                .nunique()
                .reset_index()
                .rename(columns={"BUSINESS_UNIT": "Business Units"})
            )
            fig_fmis = px.bar(
                level_counts,
                x="National Level",
                y="Business Units",
                color="Business Units",
                color_continuous_scale="Blues",
                template="plotly_white",
                title="Business Units per National Level",
                text="Business Units",
            )
            fig_fmis.update_layout(
                height=340,
                margin=dict(t=45, b=10, l=10, r=10),
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                coloraxis_showscale=False,
                xaxis=dict(title=None),
                yaxis=dict(title="Count", gridcolor="#f3f4f6"),
            )
            fig_fmis.update_traces(textposition="outside", marker_line_width=0)
            st.plotly_chart(fig_fmis, use_container_width=True)
        else:
            st.info("ទិន្នន័យ FMIS Entity មិនអាចផ្ទុកបានទេ។")

    # ════════════════════════════════════════════
    # ── Section 4 : Supplier / Spending ──
    # ════════════════════════════════════════════
    if has_supplier and not supplier_df.empty:
        section_header("ទិន្នន័យអ្នកផ្គត់ផ្គង់ – Supplier Overview", "🚚")

        col_s1, col_s2 = st.columns(2)

        with col_s1:
            if "Year" in supplier_df.columns:
                yearly = (
                    supplier_df[supplier_df["Year"].astype(str).str.match(r"^\d{4}$")]
                    .groupby("Year")["Amount"]
                    .sum()
                    .reset_index()
                    .sort_values("Year")
                )
                if not yearly.empty:
                    fig_year = px.bar(
                        yearly,
                        x="Year",
                        y="Amount",
                        template="plotly_white",
                        title="Total Spending by Year",
                        color="Amount",
                        color_continuous_scale="Blues",
                        text_auto=".2s",
                    )
                    fig_year.update_layout(
                        height=320,
                        margin=dict(t=45, b=10, l=10, r=10),
                        paper_bgcolor="rgba(0,0,0,0)",
                        plot_bgcolor="rgba(0,0,0,0)",
                        coloraxis_showscale=False,
                        xaxis=dict(title=None, type="category"),
                        yaxis=dict(title="Amount (៛)", gridcolor="#f3f4f6"),
                    )
                    st.plotly_chart(fig_year, use_container_width=True)

        with col_s2:
            if "Po Type" in supplier_df.columns:
                po_type = (
                    supplier_df.groupby("Po Type")["Amount"]
                    .sum()
                    .reset_index()
                    .sort_values("Amount", ascending=False)
                )
                if not po_type.empty:
                    fig_po = px.pie(
                        po_type,
                        names="Po Type",
                        values="Amount",
                        hole=0.45,
                        template="plotly_white",
                        title="Spending by PO Type",
                        color_discrete_sequence=px.colors.qualitative.Set2,
                    )
                    fig_po.update_layout(
                        height=320,
                        margin=dict(t=45, b=10, l=10, r=10),
                        paper_bgcolor="rgba(0,0,0,0)",
                    )
                    fig_po.update_traces(textinfo="percent+label")
                    st.plotly_chart(fig_po, use_container_width=True)

        # Top 10 vendors table
        if "Vendor Name" in supplier_df.columns:
            top_vendors = (
                supplier_df.groupby("Vendor Name")["Amount"]
                .sum()
                .nlargest(10)
                .reset_index()
                .rename(columns={"Amount": "Total Amount (៛)"})
            )
            top_vendors["Total Amount (៛)"] = top_vendors["Total Amount (៛)"].apply(
                lambda x: f"៛ {x:,.0f}"
            )
            st.markdown(
                "<h4 style='font-size:1rem; color:#374151; margin-bottom:0.5rem;'>🏆 Top 10 Vendors by Spending</h4>",
                unsafe_allow_html=True,
            )
            st.dataframe(top_vendors, use_container_width=True, hide_index=True)

    # ════════════════════════════════════════════
    # ── Section 5 : Module Summary Table ──
    # ════════════════════════════════════════════
    section_header("សង្ខេបម៉ូឌុល – Module Summary", "📋")

    rows = []
    if has_ou:
        rows.append({
            "ម៉ូឌុល": "🏢 អង្គភាពប្រតិបត្តិ",
            "ទំហំទិន្នន័យ": f"{len(ou_df):,}",
            "Active": f"{(ou_df['EFF_STATUS']=='Active').sum():,}" if 'EFF_STATUS' in ou_df.columns else "N/A",
            "Inactive": f"{(ou_df['EFF_STATUS']=='Inactive').sum():,}" if 'EFF_STATUS' in ou_df.columns else "N/A",
            "ឯកសារ (Excel)": "OU_df_merged.xlsx",
        })
    if has_eco:
        rows.append({
            "ម៉ូឌុល": "📊 មាតិកាគណនី",
            "ទំហំទិន្នន័យ": f"{len(eco_df):,}",
            "Active": f"{(eco_df['EFF_STATUS']=='Active').sum():,}" if 'EFF_STATUS' in eco_df.columns else "N/A",
            "Inactive": f"{(eco_df['EFF_STATUS']=='Inactive').sum():,}" if 'EFF_STATUS' in eco_df.columns else "N/A",
            "ឯកសារ (Excel)": "Economic_df_merged.xlsx",
        })
    if has_prog:
        rows.append({
            "ម៉ូឌុល": "📋 កម្មវិធី",
            "ទំហំទិន្នន័យ": f"{len(prog_df):,}",
            "Active": f"{(prog_df['EFF_STATUS']=='Active').sum():,}" if 'EFF_STATUS' in prog_df.columns else "N/A",
            "Inactive": f"{(prog_df['EFF_STATUS']=='Inactive').sum():,}" if 'EFF_STATUS' in prog_df.columns else "N/A",
            "ឯកសារ (Excel)": "Program for datareader.xlsx",
        })
    if has_geo:
        rows.append({
            "ម៉ូឌុល": "🌍 ភូមិសាស្ត្រ",
            "ទំហំទិន្នន័យ": f"{len(geo_df):,}",
            "Active": f"{(geo_df['EFF_STATUS']=='Active').sum():,}" if 'EFF_STATUS' in geo_df.columns else "N/A",
            "Inactive": f"{(geo_df['EFF_STATUS']=='Inactive').sum():,}" if 'EFF_STATUS' in geo_df.columns else "N/A",
            "ឯកសារ (Excel)": "Geographyfordatareader.xlsx",
        })
    if has_fmis:
        rows.append({
            "ម៉ូឌុល": "🏛️ FMIS Entity",
            "ទំហំទិន្នន័យ": f"{len(fmis_df):,}",
            "Active": "N/A",
            "Inactive": "N/A",
            "ឯកសារ (Excel)": "FMIS Entity all CMB01.xlsx",
        })
    if has_supplier:
        rows.append({
            "ម៉ូឌុល": "🚚 អ្នកផ្គត់ផ្គង់",
            "ទំហំទិន្នន័យ": f"{len(supplier_df):,}",
            "Active": "N/A",
            "Inactive": "N/A",
            "ឯកសារ (Excel)": "Supplier.xlsx",
        })

    if rows:
        st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
    else:
        st.warning("ទិន្នន័យម៉ូឌុលមិនអាចផ្ទុកបាន។")

   


# if __name__ == "__main__":
#     Overview()