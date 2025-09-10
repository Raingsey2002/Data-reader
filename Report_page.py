

# import streamlit as st
# import pandas as pd
# import plotly.express as px

# def Report():
#     # Page title
#     st.markdown(
#         """
#         <h1 style="text-align: center; color: #1f2937; font-size: 40px; font-weight: bold; padding: 10px;">
#            របាយការណ៍ប្រើប្រាស់ Report/Query
#         </h1>
#         <p style="text-align:center; color: gray; font-size:18px;">
#             Semester 1 - 2025 | FMIS Report & User Performance Dashboard
#         </p>
#         """,
#         unsafe_allow_html=True,
#     )

#     # Load data
#     file_path = "FMIS Report Query and User Performance_Data@2025Semester1.xlsx"
#     df = pd.read_excel(file_path, dtype=str).fillna("")
    
#     # Convert Count to numeric if available
#     if "Count" in df.columns:
#         df["Count"] = pd.to_numeric(df["Count"], errors="coerce").fillna(1)

#     # Sidebar filters
#     st.header("🔎 Filters")
#     report_filter = st.multiselect(
#         "Select Report/Query Name",
#         options=df["Name of Report and Query"].unique(),
#         default=df["Name of Report and Query"].unique()
#     )
#     level_filter = st.multiselect(
#         "Select Level",
#         options=df["Level"].unique(),
#         default=df["Level"].unique()
#     )
#     year_filter = st.multiselect(
#         "Select Year",
#         options=df["Year"].unique(),
#         default=df["Year"].unique()
#     )
#     month_filter = st.multiselect(
#         "Select Month",
#         options=df["Month"].unique(),
#         default=df["Month"].unique()
#     )

#     # Apply filters
#     filtered_df = df[
#         (df["Name of Report and Query"].isin(report_filter)) &
#         (df["Level"].isin(level_filter)) &
#         (df["Year"].isin(year_filter)) &
#         (df["Month"].isin(month_filter))
#     ]

#     # KPIs
#     total_records = len(filtered_df)
#     unique_users = filtered_df["User Alias"].nunique()
#     report_count = (filtered_df["Description"] == "Report").sum()
#     query_count = (filtered_df["Description"] == "Query").sum()

#     kpi1, kpi2, kpi3, kpi4 = st.columns(4)
#     kpi1.metric("📄 Total Records", total_records)
#     kpi2.metric("👤 Unique Users", unique_users)
#     kpi3.metric("📊 Reports", report_count)
#     kpi4.metric("🔍 Queries", query_count)

#     # Charts
#     st.subheader("📊 Visual Insights")

#     # Top Users
#     top_users = (
#         filtered_df.groupby("User Alias")["Count"]
#         .sum()
#         .sort_values(ascending=False)
#         .head(10)
#         .reset_index()
#     )
#     fig_users = px.bar(top_users, x="User Alias", y="Count",
#                        title="Top 10 Active Users", text="Count")
#     st.plotly_chart(fig_users, use_container_width=True)

#     # Report vs Query
#     fig_type = px.pie(
#         filtered_df,
#         names="Description",
#         title="Report vs Query Usage",
#     )
#     st.plotly_chart(fig_type, use_container_width=True)

#     # Trend by Month
#     trend = (
#         filtered_df.groupby(["Year", "Month"])["Count"]
#         .sum()
#         .reset_index()
#     )
#     fig_trend = px.line(trend, x="Month", y="Count", color="Year",
#                         markers=True, title="Usage Trend by Month")
#     st.plotly_chart(fig_trend, use_container_width=True)

#     # Breakdown by Entity
#     entity_usage = (
#         filtered_df.groupby("Entity")["Count"]
#         .sum()
#         .reset_index()
#         .sort_values(by="Count", ascending=False)
#     )
#     fig_entity = px.bar(entity_usage, x="Entity", y="Count",
#                         title="Usage by Entity", text="Count")
#     st.plotly_chart(fig_entity, use_container_width=True)

#     # Show filtered data
#     st.subheader("📋 Filtered Data Table")
#     st.dataframe(filtered_df)

#     # Download filtered data
#     st.download_button(
#         "📥 Download Data (CSV)",
#         data=filtered_df.to_csv(index=False).encode("utf-8"),
#         file_name="Filtered_Report_Data.csv",
#         mime="text/csv"
#     )




    
# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go
# from datetime import datetime

# def Report():
#     # Page title
#     st.markdown(
#         """
#         <h1 style="text-align: center; color: #1f2937; font-size: 40px; font-weight: bold; padding: 10px;">
#            របាយការណ៍ប្រើប្រាស់ Report/Query
#         </h1>
#         <p style="text-align:center; color: gray; font-size:18px;">
#             Semester 1 - 2025 | FMIS Report & User Performance Dashboard
#         </p>
#         """,
#         unsafe_allow_html=True,
#     )
    
#     # Load data
#     file_path = "FMIS Report Query and User Performance_Data@2025Semester1.xlsx"
#     df = pd.read_excel(file_path, dtype=str).fillna("")
    
#     # Convert month to name
#     month_map = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', 
#                  '05': 'May', '06': 'June', '07': 'July', '08': 'August', 
#                  '09': 'September', '10': 'October', '11': 'November', '12': 'December'}
#     df['Month Name'] = df['Month'].map(month_map)
    
#     # Create sidebar filters
#     st.header("Filter Data")
    
#     # # Report/Query filter
#     # report_options = ["All"] + list(df['Report/Query'].unique())
#     # selected_report = st.selectbox("Report/Query", report_options)
    
#     # Name of Report and Query filter
#     name_options = ["All"] + list(df['Name of Report and Query'].unique())
#     selected_name = st.selectbox("Report and Query", name_options)
    
#     # Level filter
#     level_options = ["All"] + list(df['Level'].unique())
#     selected_level = st.selectbox("Level", level_options)
    
#     # Month filter
#     month_options = ["All"] + list(df['Month Name'].unique())
#     selected_month = st.selectbox("Month", month_options)
    
#     # Apply filters
#     filtered_df = df.copy()
#     # if selected_report != "All":
#     #     filtered_df = filtered_df[filtered_df['Report/Query'] == selected_report]
#     if selected_name != "All":
#         filtered_df = filtered_df[filtered_df['Name of Report and Query'] == selected_name]
#     if selected_level != "All":
#         filtered_df = filtered_df[filtered_df['Level'] == selected_level]
#     if selected_month != "All":
#         filtered_df = filtered_df[filtered_df['Month Name'] == selected_month]
    
#     # Create tabs
#     tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Distribution Analysis", "User Analysis", "Raw Data"])
    
#     with tab1:
#         # Display key metrics
#         st.subheader("Key Performance Indicators")
#         col1, col2, col3 = st.columns(3)
        
#         with col1:
#             total_usage = len(filtered_df)
#             st.metric("Total Usage", total_usage)
        
#         with col2:
#             unique_users = filtered_df['User ID'].nunique()
#             st.metric("Unique Users", unique_users)
        
#         with col3:
#             unique_reports = filtered_df['Report/Query'].nunique()
#             st.metric("Unique Reports", unique_reports)
        
        
#         # First row of charts
#         st.subheader("Usage Overview")
#         col1, col2 = st.columns(2)
        
#         with col1:
#             # Usage by Report Type
#             report_counts = filtered_df['Name of Report and Query'].value_counts().reset_index()
#             report_counts.columns = ['Name of Report and Query', 'Count']
            
#             fig = px.bar(report_counts, x='Name of Report and Query', y='Count', 
#                          title="Usage by Report Type",
#                          color='Name of Report and Query')
#             fig.update_layout(showlegend=False)
#             st.plotly_chart(fig, use_container_width=True)
        
#         with col2:
#             # Level distribution
#             level_counts = filtered_df['Level'].value_counts().reset_index()
#             level_counts.columns = ['Level', 'Count']
            
#             fig = px.pie(level_counts, values='Count', names='Level', 
#                          title="Distribution by Level")
#             st.plotly_chart(fig, use_container_width=True)
        
#         # Second row of charts
#         col1, col2 = st.columns(2)
        
#         with col1:
#             # Monthly usage trend
#             monthly_usage = filtered_df.groupby('Month Name').size().reset_index(name='Count')
#             monthly_usage['Month Name'] = pd.Categorical(monthly_usage['Month Name'], 
#                                                         categories=['January', 'February', 'March', 'April', 
#                                                                    'May', 'June', 'July', 'August', 
#                                                                    'September', 'October', 'November', 'December'],
#                                                         ordered=True)
#             monthly_usage = monthly_usage.sort_values('Month Name')
            
#             fig = px.line(monthly_usage, x='Month Name', y='Count', 
#                           title="Monthly Usage Trend", markers=True)
#             st.plotly_chart(fig, use_container_width=True)
        
#         with col2:
#             # Top users
#             top_users = filtered_df['User ID'].value_counts().head(10).reset_index()
#             top_users.columns = ['User ID', 'Count']
            
#             fig = px.bar(top_users, x='Count', y='User ID', orientation='h',
#                          title="Top Users by Report Usage",
#                          color='Count')
#             st.plotly_chart(fig, use_container_width=True)
    
#     with tab2:
#         st.header("Distribution Analysis")
        
#         col1, col2 = st.columns(2)
        
#         with col1:
#             # Entity distribution
#             entity_counts = filtered_df['Entity'].value_counts().reset_index()
#             entity_counts.columns = ['Entity', 'Count']
            
#             fig = px.pie(entity_counts, values='Count', names='Entity', 
#                          title="Distribution by Entity")
#             st.plotly_chart(fig, use_container_width=True)
        
#         with col2:
#             # Office distribution
#             office_counts = filtered_df['Office'].value_counts().reset_index()
#             office_counts.columns = ['Office', 'Count']
            
#             fig = px.bar(office_counts, x='Office', y='Count', 
#                          title="Distribution by Office",
#                          color='Office')
#             fig.update_layout(showlegend=False)
#             st.plotly_chart(fig, use_container_width=True)
        
#         col1, col2 = st.columns(2)
        
#         with col1:
#             # Sub Office distribution
#             sub_office_counts = filtered_df['Sub Office'].value_counts().reset_index()
#             sub_office_counts.columns = ['Sub Office', 'Count']
            
#             fig = px.bar(sub_office_counts, x='Sub Office', y='Count', 
#                          title="Distribution by Sub Office",
#                          color='Sub Office')
#             fig.update_layout(showlegend=False, xaxis_tickangle=-45)
#             st.plotly_chart(fig, use_container_width=True)
        
#         # with col2:
#         #     # Report vs Query distribution
#         #     type_counts = filtered_df['Description'].value_counts().reset_index()
#         #     type_counts.columns = ['Type', 'Count']
            
#         #     fig = px.pie(type_counts, values='Count', names='Type', 
#         #                  title="Report vs Query Distribution")
#         #     st.plotly_chart(fig, use_container_width=True)
        
#         # # Operating Unit distribution
#         # operating_unit_counts = filtered_df['Operating Unit'].value_counts().reset_index()
#         # operating_unit_counts.columns = ['Operating Unit', 'Count']
        
#         # fig = px.bar(operating_unit_counts, x='Operating Unit', y='Count', 
#         #              title="Distribution by Operating Unit",
#         #              color='Operating Unit')
#         # fig.update_layout(showlegend=False, xaxis_tickangle=-45)
#         # st.plotly_chart(fig, use_container_width=True)
    
#     with tab3:
#         st.header("User Analysis")
        
#         col1, col2 = st.columns(2)
        
#         with col1:
#             # Top active users
#             user_activity = filtered_df['User ID'].value_counts().head(15).reset_index()
#             user_activity.columns = ['User ID', 'Count']
            
#             fig = px.bar(user_activity, x='Count', y='User ID', orientation='h',
#                          title="Top Active Users",
#                          color='Count')
#             st.plotly_chart(fig, use_container_width=True)
        
#         with col2:
#             # User distribution by level
#             user_level = filtered_df.groupby(['User ID', 'Level']).size().reset_index(name='Count')
#             user_level_summary = user_level.groupby('Level').size().reset_index(name='User Count')
            
#             fig = px.pie(user_level_summary, values='User Count', names='Level', 
#                          title="User Distribution by Level")
#             st.plotly_chart(fig, use_container_width=True)
        
#         # User report preferences
#         user_report_pref = filtered_df.groupby(['User ID', 'Report/Query']).size().reset_index(name='Count')
#         top_user_reports = user_report_pref.sort_values('Count', ascending=False).head(15)
        
#         fig = px.bar(top_user_reports, x='Count', y='User ID', color='Report/Query',
#                      orientation='h', title="Top User-Report Combinations")
#         st.plotly_chart(fig, use_container_width=True)
    
#     with tab4:
#         st.header("Raw Data")
#         st.dataframe(filtered_df, use_container_width=True)
        
#         # Download button
#         csv = filtered_df.to_csv(index=False).encode('utf-8')
#         st.download_button(
#             label="Download Filtered Data as CSV",
#             data=csv,
#             file_name="filtered_report_data.csv",
#             mime="text/csv",
#         )

# if __name__ == "__main__":
#     Report()




######back up code below::::::::

# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go
# from datetime import datetime



# def Report():
    
     

#     # Custom CSS for professional styling
#     st.markdown("""
                



#     <style>
#     .main-header {
#         font-size: 2.5rem;
#         color: #1f2937;
#         text-align: center;
#         margin-bottom: 0.5rem;
#         font-weight: 700;
#     }
#     .sub-header {
#         text-align: center;
#         color: #6b7280;
#         font-size: 1.1rem;
#         margin-bottom: 2rem;
#     }
#     .metric-card {
#         background-color: #f9fafb;
#         padding: 1.5rem;
#         border-radius: 0.5rem;
#         box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
#     }
#     .stSelectbox, .stMultiSelect {
#         padding: 0.5rem;
#         border-radius: 0.375rem;
#     }
#     .tab-container {
#         background-color: white;
#         padding: 1.5rem;
#         border-radius: 0.5rem;
#         box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
#         margin-top: 1rem;
#     }
#     .download-btn {
#         background-color: #2563eb;
#         color: white;
#         padding: 0.5rem 1rem;
#         border-radius: 0.375rem;
#         border: none;
#         cursor: pointer;
#         font-weight: 500;
#     }
#     .download-btn:hover {
#         background-color: #1d4ed8;
#     }
    
#     }
#     </style>
#     """, unsafe_allow_html=True)
    

#     # Premium page header
#     st.markdown("""
#     <div style="margin-bottom: 2rem;">
#         <h1 class="dashboard-title">📘 របាយការណ៍ Report/Query</h1>
#        <p style="font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
#           color: #7f8c8d;
#           font-size: 1rem;
#           margin-bottom: 2rem;">
#      Semester 1 - 2025 | FMIS Report & User Performance Dashboard
# </p>
#     </div>
#     """, unsafe_allow_html=True)

#     # st.markdown("""
#     # <div style="margin-bottom:0.5rem;">
#     #     <h1 style="font-size:2rem; color:#1f2937; text-align:center; margin:0; font-weight:700;">
#     #         📘 របាយការណ៍ Report/Query
#     #     </h1>
#     #     <p style="font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
#     #             color:#7f8c8d; font-size:0.9rem; text-align:center; margin:0.2rem 0 0 0;">
#     #         Semester 1 - 2025 | FMIS Report & User Performance Dashboard
#     #     </p>
#     # </div>
#     # """, unsafe_allow_html=True)
#     # Page title
#     # st.markdown(
#     #     """
#     #     <h1 class="main-header">
#     #        របាយការណ៍ប្រើប្រាស់ Report/Query
#     #     </h1>
#     #     <p class="sub-header">
#     #         Semester 1 - 2025 | FMIS Report & User Performance Dashboard
#     #     </p>
#     #     """,
#     #     unsafe_allow_html=True,
#     # )
    
#     # Load data
#     file_path = "FMIS Report Query and User Performance_Data@2025Semester1.xlsx"
#     df = pd.read_excel(file_path, dtype=str).fillna("")
    
#     # Convert month to name
#     month_map = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', 
#                  '05': 'May', '06': 'June', '07': 'July', '08': 'August', 
#                  '09': 'September', '10': 'October', '11': 'November', '12': 'December'}
#     df['Month Name'] = df['Month'].map(month_map)
    
#     # Create filter section below header
#     st.markdown('<div class="filter-section">', unsafe_allow_html=True)
#     st.markdown("### 🔍 Filter Options")
    
#     filter_col1, filter_col2, filter_col3 = st.columns(3)
    
#     with filter_col1:
#         # Name of Report and Query filter
#         name_options = ["All"] + sorted(list(df['Name of Report and Query'].unique()))
#         selected_name = st.selectbox("Report/Query Name", name_options)
        
#     with filter_col2:
#         # Level filter
#         level_options = ["All"] + sorted(list(df['Level'].unique()))
#         selected_level = st.selectbox("User Level", level_options)
        
#     with filter_col3:
#         # Month filter
#         month_options = ["All"] + list(df['Month Name'].unique())
#         selected_month = st.selectbox("Month", month_options)
    
#     # # Additional filters
#     # with st.expander("Advanced Filters"):
#     #     adv_col1, adv_col2 = st.columns(2)
        
#     #     with adv_col1:
#     #         # Entity filter
#     #         entity_options = ["All"] + sorted(list(df['Entity'].unique()))
#     #         selected_entity = st.selectbox("Entity", entity_options)
            
#     #     with adv_col2:
#     #         # Office filter
#     #         office_options = ["All"] + sorted(list(df['Office'].unique()))
#     #         selected_office = st.selectbox("Office", office_options)
    
#     # st.markdown('</div>', unsafe_allow_html=True)
    
#     # Apply filters
#     filtered_df = df.copy()
#     if selected_name != "All":
#         filtered_df = filtered_df[filtered_df['Name of Report and Query'] == selected_name]
#     if selected_level != "All":
#         filtered_df = filtered_df[filtered_df['Level'] == selected_level]
#     if selected_month != "All":
#         filtered_df = filtered_df[filtered_df['Month Name'] == selected_month]
#     if 'selected_entity' in locals() and selected_entity != "All":
#         filtered_df = filtered_df[filtered_df['Entity'] == selected_entity]
#     if 'selected_office' in locals() and selected_office != "All":
#         filtered_df = filtered_df[filtered_df['Office'] == selected_office]
    
#     # Create tabs with improved styling
#     tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview", "📈 Distribution", "👥 User Analysis", "📋 Raw Data"])
    
#     with tab1:
#         # Display key metrics in styled cards
#         st.subheader("Performance Summary")
#         col1, col2, col3 = st.columns(3)
        
#         with col1:
#             total_usage = len(filtered_df)
#             st.markdown(f"""
#             <div class="metric-card">
#                 <h3 style="margin:0; color: #6b7280; font-size: 0.9rem;">Total Usage</h3>
#                 <p style="margin:0; color: #2563eb; font-size: 1.8rem; font-weight: 700;">{total_usage}</p>
#             </div>
#             """, unsafe_allow_html=True)
        
#         with col2:
#             unique_users = filtered_df['User ID'].nunique()
#             st.markdown(f"""
#             <div class="metric-card">
#                 <h3 style="margin:0; color: #6b7280; font-size: 0.9rem;">Unique Users</h3>
#                 <p style="margin:0; color: #2563eb; font-size: 1.8rem; font-weight: 700;">{unique_users}</p>
#             </div>
#             """, unsafe_allow_html=True)
        
#         with col3:
#             unique_reports = filtered_df['Report/Query'].nunique()
#             st.markdown(f"""
#             <div class="metric-card">
#                 <h3 style="margin:0; color: #6b7280; font-size: 0.9rem;">Unique Reports</h3>
#                 <p style="margin:0; color: #2563eb; font-size: 1.8rem; font-weight: 700;">{unique_reports}</p>
#             </div>
#             """, unsafe_allow_html=True)
            
        
        
#         # First row of charts
#         st.subheader("Usage Overview")
#         col1, col2 = st.columns(2)
        
#         with col1:
#             # Usage by Report Type
#             report_counts = filtered_df['Name of Report and Query'].value_counts().reset_index()
#             report_counts.columns = ['Name of Report and Query', 'Count']
            
#             fig = px.bar(report_counts, x='Count', y='Name of Report and Query', 
#                          title="Top Reports by Usage",
#                          orientation='h',
#                          color='Count',
#                          color_continuous_scale='blues')
#             fig.update_layout(showlegend=False, yaxis_title="")
#             st.plotly_chart(fig, use_container_width=True)
        
#         with col2:
#             # Level distribution
#             level_counts = filtered_df['Level'].value_counts().reset_index()
#             level_counts.columns = ['Level', 'Count']
            
#             fig = px.pie(level_counts, values='Count', names='Level', 
#                          title="Distribution by User Level",
#                          color_discrete_sequence=px.colors.sequential.Blues_r)
#             fig.update_traces(textposition='inside', textinfo='percent+label')
#             st.plotly_chart(fig, use_container_width=True)
        
#         # Second row of charts
#         col1, col2 = st.columns(2)
        
#         with col1:
#             # Monthly usage trend
#             monthly_usage = filtered_df.groupby('Month Name').size().reset_index(name='Count')
#             monthly_usage['Month Name'] = pd.Categorical(monthly_usage['Month Name'], 
#                                                         categories=['January', 'February', 'March', 'April', 
#                                                                    'May', 'June', 'July', 'August', 
#                                                                    'September', 'October', 'November', 'December'],
#                                                         ordered=True)
#             monthly_usage = monthly_usage.sort_values('Month Name')
            
#             fig = px.line(monthly_usage, x='Month Name', y='Count', 
#                           title="Monthly Usage Trend", markers=True,
#                           line_shape='spline')
#             fig.update_traces(line=dict(width=3))
#             st.plotly_chart(fig, use_container_width=True)
        
#         with col2:
#             # Top users
#             top_users = filtered_df['User ID'].value_counts().head(10).reset_index()
#             top_users.columns = ['User ID', 'Count']
            
#             fig = px.bar(top_users, x='Count', y='User ID', orientation='h',
#                          title="Top Users by Report Usage",
#                          color='Count',
#                          color_continuous_scale='blues')
#             fig.update_layout(yaxis_title="")
#             st.plotly_chart(fig, use_container_width=True)
    
#     with tab2:
#         st.subheader("Distribution Analysis")
        
#         col1, col2 = st.columns(2)
        
#         with col1:
#             # Entity distribution
#             entity_counts = filtered_df['Entity'].value_counts().reset_index()
#             entity_counts.columns = ['Entity', 'Count']
            
#             fig = px.pie(entity_counts, values='Count', names='Entity', 
#                          title="Distribution by Entity",
#                          color_discrete_sequence=px.colors.sequential.Blues_r)
#             fig.update_traces(textposition='inside', textinfo='percent+label')
#             st.plotly_chart(fig, use_container_width=True)
        
#         with col2:
#             # Office distribution
#             office_counts = filtered_df['Office'].value_counts().reset_index()
#             office_counts.columns = ['Office', 'Count']
            
#             fig = px.bar(office_counts, x='Count', y='Office', orientation='h',
#                          title="Distribution by Office",
#                          color='Count',
#                          color_continuous_scale='purpor')
#             fig.update_layout(yaxis_title="")
#             st.plotly_chart(fig, use_container_width=True)

#         # Sub Office distribution
#         sub_office_counts = filtered_df['Sub Office'].value_counts().head(10).reset_index()
#         sub_office_counts.columns = ['Sub Office', 'Count']

#         fig = px.bar(
#             sub_office_counts,
#             x='Count',
#             y='Sub Office',
#             orientation='h',
#             title="Top 10 Sub Offices",
#             color='Count',
#             color_continuous_scale='sunset'
#         )
#         fig.update_layout(yaxis_title="")
#         st.plotly_chart(fig, use_container_width=True)
        
#         # col1, col2 = st.columns(2)
        
#         # with col1:
#         #     # Sub Office distribution
#         #     sub_office_counts = filtered_df['Sub Office'].value_counts().head(10).reset_index()
#         #     sub_office_counts.columns = ['Sub Office', 'Count']
            
#         #     fig = px.bar(sub_office_counts, x='Count', y='Sub Office', orientation='h',
#         #                  title="Top 10 Sub Offices",
#         #                  color='Count',
#         #                  color_continuous_scale='blues')
#         #     fig.update_layout(yaxis_title="")
#         #     st.plotly_chart(fig, use_container_width=True)
        
#         # with col2:
#         #     # Operating Unit distribution
#         #     if 'Operating Unit' in filtered_df.columns:
#         #         operating_unit_counts = filtered_df['Operating Unit'].value_counts().head(10).reset_index()
#         #         operating_unit_counts.columns = ['Operating Unit', 'Count']
                
#         #         fig = px.bar(operating_unit_counts, x='Count', y='Operating Unit', orientation='h',
#         #                      title="Top 10 Operating Units",
#         #                      color='Count',
#         #                      color_continuous_scale='blues')
#         #         fig.update_layout(yaxis_title="")
#         #         st.plotly_chart(fig, use_container_width=True)
    
#     with tab3:
#         st.subheader("User Analysis")
        
#         col1, col2 = st.columns(2)
        
#         with col1:
#             # Top active users
#             user_activity = filtered_df['User ID'].value_counts().head(15).reset_index()
#             user_activity.columns = ['User ID', 'Count']
            
#             fig = px.bar(user_activity, x='Count', y='User ID', orientation='h',
#                          title="Top Active Users",
#                          color='Count',
#                          color_continuous_scale='blues')
#             fig.update_layout(yaxis_title="")
#             st.plotly_chart(fig, use_container_width=True)
        
#         with col2:
#             # User distribution by level
#             user_level = filtered_df.groupby(['User ID', 'Level']).size().reset_index(name='Count')
#             user_level_summary = user_level.groupby('Level').size().reset_index(name='User Count')
            
#             fig = px.pie(user_level_summary, values='User Count', names='Level', 
#                          title="User Distribution by Level",
#                          color_discrete_sequence=px.colors.sequential.Blues_r)
#             fig.update_traces(textposition='inside', textinfo='percent+label')
#             st.plotly_chart(fig, use_container_width=True)
        
#         # User report preferences
#         user_report_pref = filtered_df.groupby(['User ID', 'Name of Report and Query']).size().reset_index(name='Count')
#         top_user_reports = user_report_pref.sort_values('Count', ascending=False).head(15)
        
#         fig = px.bar(top_user_reports, x='Count', y='User ID', color='Name of Report and Query',
#                      orientation='h', title="Top User-Report Combinations",
#                      color_discrete_sequence=px.colors.qualitative.Pastel)
#         fig.update_layout(yaxis_title="")
#         st.plotly_chart(fig, use_container_width=True)
    
#     with tab4:
#         st.subheader("Raw Data")
        
#         # Show filter summary
#         st.info(f"Showing {len(filtered_df)} records based on current filters")
        
#         # Display data with improved formatting
#         st.dataframe(
#             filtered_df, 
#             use_container_width=True,
#             height=400,
#             hide_index=True
#         )
        
#         # Download button with improved styling
#         csv = filtered_df.to_csv(index=False).encode('utf-8')
#         st.download_button(
#             label="📥 Download Filtered Data as CSV",
#             data=csv,
#             file_name="fmis_filtered_data.csv",
#             mime="text/csv",
#             use_container_width=True
#         )

# if __name__ == "__main__":
#     Report()




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
    file_path = "FMIS Report Query and User Performance_Data@2025Semester1.xlsx"
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
