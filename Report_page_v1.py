import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime


def Report():
    # 🔹 Remove Streamlit default top padding
    st.markdown("""
        <style>
            .block-container {
                padding-top: 1rem;
                padding-bottom: 3rem;
            }
        </style>
    """, unsafe_allow_html=True)

    # 🔹 Custom CSS for professional styling
    st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #1f2937;
        text-align: center;
        margin-bottom: 0.5rem;
        font-weight: 700;
    }
    .sub-header {
        text-align: center;
        color: #6b7280;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f9fafb;
        padding: 1.5rem;
        border-radius: 0.5rem;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    }
    .stSelectbox, .stMultiSelect {
        padding: 0.5rem;
        border-radius: 0.375rem;
    }
    .tab-container {
        background-color: white;
        padding: 1.5rem;
        border-radius: 0.5rem;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        margin-top: 1rem;
    }
    .download-btn {
        background-color: #2563eb;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 0.375rem;
        border: none;
        cursor: pointer;
        font-weight: 500;
    }
    .download-btn:hover {
        background-color: #1d4ed8;
    }
    </style>
    """, unsafe_allow_html=True)

    # 🔹 Page Header
    # st.markdown("""
    # <div style="margin-bottom:0.5rem;">
    #     <h1 style="font-size:2rem; color:#1f2937; text-align:center; margin:0; font-weight:700;">
    #         📘 របាយការណ៍ Report/Query
    #     </h1>
    #     <p style="font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    #               color:#7f8c8d; font-size:0.9rem; text-align:center; margin:0.2rem 0 0 0;">
    #         Semester 1 - 2025 | FMIS Report & User Performance Dashboard
    #     </p>
    # </div>
    # """, unsafe_allow_html=True)

    st.markdown("""
    <div style="margin-bottom: 2rem;">
        <h1 class="dashboard-title">📘 របាយការណ៍ Report/Query</h1>
       <p style="font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
          color: #7f8c8d;
          font-size: 1rem;
          margin-bottom: 2rem;">
     Semester 1 - 2025 | FMIS Report & User Performance Dashboard
</p>
    </div>
    """, unsafe_allow_html=True)


    

    # 🔹 Load data
    file_path = "Excel files/FMIS Report Query and User Performance_Data@2025Semester1.xlsx"
    df = pd.read_excel(file_path, dtype=str).fillna("")

    # Convert month to name
    month_map = {'01': 'January', '02': 'February', '03': 'March', '04': 'April',
                 '05': 'May', '06': 'June', '07': 'July', '08': 'August',
                 '09': 'September', '10': 'October', '11': 'November', '12': 'December'}
    df['Month Name'] = df['Month'].map(month_map)

    # 🔹 Filters (immediately under header)
    st.markdown("### 🔍 Filter Options", unsafe_allow_html=True)
    filter_col1, filter_col2, filter_col3 = st.columns(3)

    with filter_col1:
        name_options = ["All"] + sorted(list(df['Name of Report and Query'].unique()))
        selected_name = st.selectbox("Report/Query Name", name_options)

    with filter_col2:
        level_options = ["All"] + sorted(list(df['Level'].unique()))
        selected_level = st.selectbox("User Level", level_options)

    with filter_col3:
        month_options = ["All"] + list(df['Month Name'].unique())
        selected_month = st.selectbox("Month", month_options)

    # 🔹 Apply filters
    filtered_df = df.copy()
    if selected_name != "All":
        filtered_df = filtered_df[filtered_df['Name of Report and Query'] == selected_name]
    if selected_level != "All":
        filtered_df = filtered_df[filtered_df['Level'] == selected_level]
    if selected_month != "All":
        filtered_df = filtered_df[filtered_df['Month Name'] == selected_month]

    # 🔹 Tabs
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview", "📈 Distribution", "👥 User Analysis", "📋 Raw Data"])

    with tab1:
        st.subheader("Performance Summary")
        col1, col2, col3 = st.columns(3)

        with col1:
            total_usage = len(filtered_df)
            st.markdown(f"""
            <div class="metric-card">
                <h3 style="margin:0; color: #6b7280; font-size: 0.9rem;">Total Usage</h3>
                <p style="margin:0; color: #2563eb; font-size: 1.8rem; font-weight: 700;">{total_usage}</p>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            unique_users = filtered_df['User ID'].nunique()
            st.markdown(f"""
            <div class="metric-card">
                <h3 style="margin:0; color: #6b7280; font-size: 0.9rem;">Unique Users</h3>
                <p style="margin:0; color: #2563eb; font-size: 1.8rem; font-weight: 700;">{unique_users}</p>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            unique_reports = filtered_df['Report/Query'].nunique()
            st.markdown(f"""
            <div class="metric-card">
                <h3 style="margin:0; color: #6b7280; font-size: 0.9rem;">Unique Reports</h3>
                <p style="margin:0; color: #2563eb; font-size: 1.8rem; font-weight: 700;">{unique_reports}</p>
            </div>
            """, unsafe_allow_html=True)

        # Charts
        st.subheader("Usage Overview")
        col1, col2 = st.columns(2)

        with col1:
            report_counts = filtered_df['Name of Report and Query'].value_counts().reset_index()
            report_counts.columns = ['Name of Report and Query', 'Count']
            fig = px.bar(report_counts, x='Count', y='Name of Report and Query',
                         title="Top Reports by Usage",
                         orientation='h',
                         color='Count',
                         color_continuous_scale='blues')
            fig.update_layout(showlegend=False, yaxis_title="")
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            level_counts = filtered_df['Level'].value_counts().reset_index()
            level_counts.columns = ['Level', 'Count']
            fig = px.pie(level_counts, values='Count', names='Level',
                         title="Distribution by User Level",
                         color_discrete_sequence=px.colors.sequential.Blues_r)
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig, use_container_width=True)

        col1, col2 = st.columns(2)
        with col1:
            monthly_usage = filtered_df.groupby('Month Name').size().reset_index(name='Count')
            monthly_usage['Month Name'] = pd.Categorical(monthly_usage['Month Name'],
                                                         categories=list(month_map.values()),
                                                         ordered=True)
            monthly_usage = monthly_usage.sort_values('Month Name')
            fig = px.line(monthly_usage, x='Month Name', y='Count',
                          title="Monthly Usage Trend", markers=True, line_shape='spline')
            fig.update_traces(line=dict(width=3))
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            top_users = filtered_df['User ID'].value_counts().head(10).reset_index()
            top_users.columns = ['User ID', 'Count']
            fig = px.bar(top_users, x='Count', y='User ID', orientation='h',
                         title="Top Users by Report Usage",
                         color='Count',
                         color_continuous_scale='blues')
            fig.update_layout(yaxis_title="")
            st.plotly_chart(fig, use_container_width=True)

    with tab2:
        st.subheader("Distribution Analysis")
        col1, col2 = st.columns(2)

        with col1:
            entity_counts = filtered_df['Entity'].value_counts().reset_index()
            entity_counts.columns = ['Entity', 'Count']
            fig = px.pie(entity_counts, values='Count', names='Entity',
                         title="Distribution by Entity",
                         color_discrete_sequence=px.colors.sequential.Blues_r)
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            office_counts = filtered_df['Office'].value_counts().reset_index()
            office_counts.columns = ['Office', 'Count']
            fig = px.bar(office_counts, x='Count', y='Office', orientation='h',
                         title="Distribution by Office",
                         color='Count',
                         color_continuous_scale='Purples')   # ✅ fixed
            fig.update_layout(yaxis_title="")
            st.plotly_chart(fig, use_container_width=True)

        sub_office_counts = filtered_df['Sub Office'].value_counts().head(10).reset_index()
        sub_office_counts.columns = ['Sub Office', 'Count']
        fig = px.bar(sub_office_counts, x='Count', y='Sub Office', orientation='h',
                     title="Top 10 Sub Offices",
                     color='Count',
                     color_continuous_scale='sunset')
        fig.update_layout(yaxis_title="")
        st.plotly_chart(fig, use_container_width=True)

    with tab3:
        st.subheader("User Analysis")
        col1, col2 = st.columns(2)

        with col1:
            user_activity = filtered_df['User ID'].value_counts().head(15).reset_index()
            user_activity.columns = ['User ID', 'Count']
            fig = px.bar(user_activity, x='Count', y='User ID', orientation='h',
                         title="Top Active Users",
                         color='Count',
                         color_continuous_scale='blues')
            fig.update_layout(yaxis_title="")
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            user_level = filtered_df.groupby(['User ID', 'Level']).size().reset_index(name='Count')
            user_level_summary = user_level.groupby('Level').size().reset_index(name='User Count')
            fig = px.pie(user_level_summary, values='User Count', names='Level',
                         title="User Distribution by Level",
                         color_discrete_sequence=px.colors.sequential.Blues_r)
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig, use_container_width=True)

        user_report_pref = filtered_df.groupby(['User ID', 'Name of Report and Query']).size().reset_index(name='Count')
        top_user_reports = user_report_pref.sort_values('Count', ascending=False).head(15)
        fig = px.bar(top_user_reports, x='Count', y='User ID',
                     color='Name of Report and Query',
                     orientation='h',
                     title="Top User-Report Combinations",
                     color_discrete_sequence=px.colors.qualitative.Pastel)
        fig.update_layout(yaxis_title="")
        st.plotly_chart(fig, use_container_width=True)

    with tab4:
        st.subheader("Raw Data")
        st.info(f"Showing {len(filtered_df)} records based on current filters")
        st.dataframe(filtered_df, use_container_width=True, height=400, hide_index=True)
        csv = filtered_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Filtered Data as CSV",
            data=csv,
            file_name="fmis_filtered_data.csv",
            mime="text/csv",
            use_container_width=True
        )


if __name__ == "__main__":
    Report()