import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
from streamlit_extras.metric_cards import style_metric_cards
import numpy as np

# Set page config (should be first Streamlit command)
# st.set_page_config(
#     page_title="User Analytics Dashboard",
#     page_icon="👥",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )



def apply_custom_styles():
    """Inject custom CSS for professional styling"""
    st.markdown("""
    <style>
        /* Main container styling */
        .main {
            background-color: #f8f9fa;
            padding: 0 2rem;
        }
        
        /* Title styling */
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
        
        /* Card styling */
        .metric-card {
            background: white;
            border-radius: 8px;
            padding: 1.5rem;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
            border: 1px solid #e0e0e0;
            transition: all 0.3s ease;
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
            letter-spacing: 0.5px;
        }
        
        .metric-value {
            font-size: 1.8rem;
            font-weight: 700;
            color: #2c3e50;
            margin-bottom: 0.25rem;
            font-family: 'Inter', sans-serif;
        }
        
        .metric-subtext {
            font-size: 0.75rem;
            color: #95a5a6;
            font-family: 'Inter', sans-serif;
        }
        
        /* Section headers */
        .section-header {
            font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: #2c3e50;
            font-weight: 600;
            font-size: 1.5rem;
            margin: 2rem 0 1rem 0;
            padding-bottom: 0.5rem;
            border-bottom: 1px solid #ecf0f1;
        }
        
        /* Data table styling */
        .stDataFrame {
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
            border: 1px solid #e0e0e0;
        }
        
       /* Clean white button styling */
        .stDownloadButton {
            display: flex;
            justify-content: flex-start !important;  /* Align to left */
            margin-left: 0 !important;
            padding-left: 0 !important;
        }

        .stDownloadButton button {
            background: white !important;
            color: #333 !important;
            border-radius: 4px !important;
            padding: 0.25rem 0.75rem !important;
            transition: all 0.2s ease !important;
            border: 1px solid #e0e0e0 !important;
            font-family: 'Inter', sans-serif !important;
            font-weight: 400 !important;
            font-size: 0.8rem !important;
            letter-spacing: 0.3px !important;
            box-shadow: 0 1px 2px rgba(0,0,0,0.05) !important;
            margin-left: 0 !important;
        }

        .stDownloadButton button:hover {
            background: #f8f8f8 !important;
            transform: none;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1) !important;
            border-color: #d0d0d0 !important;
        }
        
        /* Chart containers */
        .chart-container {
            background: white;
            border-radius: 8px;
            padding: 1.5rem;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
            border: 1px solid #e0e0e0;
        }
        
        /* Custom tabs for navigation */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            padding: 8px 16px;
            border-radius: 4px 4px 0 0;
            gap: 8px;
            font-family: 'Inter', sans-serif;
        }
    </style>
    """, unsafe_allow_html=True)


# Load data
df_su = pd.read_excel("Excel files/User Alias Data(Dec) from prod.xlsx")
    




def create_metric_card(title, value, subtext=None, delta=None, delta_color="normal"):
    """Create a professional metric card with optional delta indicator"""
    delta_html = ""
    if delta is not None:
        color = "#27ae60" if delta_color == "positive" else "#e74c3c" if delta_color == "negative" else "#7f8c8d"
        arrow = "↑" if delta_color == "positive" else "↓" if delta_color == "negative" else "→"
        delta_html = f"""<div style="display: flex; align-items: center; margin-top: 4px;">
                            <span style="color: {color}; font-size: 0.85rem; font-weight: 500; font-family: 'Inter', sans-serif;">
                                {arrow} {delta}
                            </span>
                        </div>"""
    
    subtext_html = f'<div class="metric-subtext">{subtext}</div>' if subtext else ""
    
    return f"""
    <div class="metric-card">
        <div class="metric-title">{title}</div>
        <div class="metric-value">{value}</div>
        {delta_html}
        {subtext_html}
    </div>
    """

def show():
    """Ultra-professional User Analytics Dashboard"""
     # 🔹 Remove Streamlit default top padding
    st.markdown("""
        <style>
            .block-container {
                padding-top: 1rem;
                padding-bottom: 3rem;
            }
        </style>
    """, unsafe_allow_html=True)
             


    apply_custom_styles()
    
    # Premium page header
    st.markdown("""
    <div style="margin-bottom: 2rem;">
        <h1 class="dashboard-title">👥 User Analytics Dashboard</h1>
        <p class="dashboard-subtitle">Comprehensive insights into entity user base and activity patterns</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load data with error handling
    try:
        df = pd.read_excel("Excel files/User Management.xlsx")
        
        # Data preprocessing
        df['Organization_Name'] = df[['PV_Description','PT_Description','DEF_Description','EPA_Description', 
                                    'GD_Description','BE_Description', 'GS_Description', 'ABE_Description',
                                    'DS_Description']].bfill(axis=1).iloc[:, 0]
        
        # Calculate department counts (mock data for example)
        department_data = {
            'Department': ['LM-GS', 'LM-ABE', 'GD', 'PT', 'DEF', 'PV', 'DS', 'EPA', 'LM-BE','TOP'],
            'Users': [38, 106, 9, 25, 25, 25, 44, 9, 19, 1]
        }
        df_dept = pd.DataFrame(department_data)
        
        # ======================
        # EXECUTIVE SUMMARY ROW
        # ======================
        st.markdown('<div class="section-header">Executive Summary</div>', unsafe_allow_html=True)
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            total_users = int(df_su["សរុប"].sum())
            st.markdown(create_metric_card(
                "Total Users", 
                f"{total_users:,}",
                # "Across all departments",
                # "2.5% MoM",
                # "positive"
            ), unsafe_allow_html=True)
        
        with col2:
            # active_users = len(df[df['Status'] == 'Active']) if 'Status' in df.columns else 0
            active_users = int(df_su["សកម្ម"].sum())
            st.markdown(create_metric_card(
                "Active Users", 
                f"{active_users:,}",
                # f"{(active_users/total_users*100 if total_users > 0 else 0):.1f}% of total",
                # "1.2% MoM",
                # "positive"
            ), unsafe_allow_html=True)
        
        with col3:
            inactive90 = int(df_su["អសកម្ម"].sum())
            st.markdown(create_metric_card(
                "Inactive Users (90 Days)", 
                inactive90,
                # f"{(df_dept['Users'].sum()/departments if departments > 0 else 0):.0f} avg users",
                # "No change",
                # "normal"
            ), unsafe_allow_html=True)
           
        with col4:
            Inactive = int(df_su["ឈប់ប្រើប្រាស់"].sum())
            st.markdown(create_metric_card(
                "Inactive", 
                Inactive,
                # "Users no longer active",
                # "0.5% MoM",
                # "negative"
            ), unsafe_allow_html=True)
        # ======================
        # USER DISTRIBUTION ANALYSIS
        # ======================
        st.markdown('<div class="section-header">User Distribution Analysis</div>', unsafe_allow_html=True)
        
        tab1, tab2, tab3 = st.tabs(["Entity Overview", "User Status", "Demographics"])
        
        with tab1:
            col1, col2 = st.columns([2, 1], gap="medium")
            
            # with col1:
            #     with st.container():
            #         st.markdown("#### Entity Distribution")
            #         # Count entities
            #         enti_counts = (
            #             df_su['ENTITY']
            #             .value_counts()
            #             .reset_index()
            #         )
            #         enti_counts.columns = ['ENTITY', 'COUNT']
            #         # top_entities = entity_counts.head(10)
            #         # Create a treemap for department visualization
            #         fig_treemap = px.treemap(
            #             enti_counts,
            #             path=['ENTITY'],
            #             values='COUNT',
            #             color='COUNT',
            #             color_continuous_scale='Blues',
            #             hover_data=['COUNT'],
            #             height=400
            #         )
            #         fig_treemap.update_layout(
            #             margin=dict(t=0, l=0, r=0, b=0),
            #             paper_bgcolor='rgba(0,0,0,0)',
            #             plot_bgcolor='rgba(0,0,0,0)',
            #             font=dict(family="Inter", size=12),
            #             hoverlabel=dict(
            #                 bgcolor="white",
            #                 font_size=12,
            #                 font_family="Inter"
            #             )
            #         )
            #         st.plotly_chart(fig_treemap, use_container_width=True)
            
            # with col2:
            #     with st.container():
            #         st.markdown("#### Top 5 Entities")

            #         # Count entities
            #         entity_counts = (
            #             df_su['ENTITY']
            #             .value_counts()
            #             .reset_index()
            #         )
            #         entity_counts.columns = ['ENTITY', 'COUNT']
            #         top_entities = entity_counts.head(5)

            #         fig = go.Figure()
            #         fig.add_trace(go.Bar(
            #             y=top_entities['ENTITY'],
            #             x=top_entities['COUNT'],
            #             orientation='h',
            #             marker=dict(
            #                 color="#3498db",
            #                 line=dict(color="#2980b9", width=1)
            #             ),
            #             text=top_entities['COUNT'],
            #             textposition='auto',
            #             textfont=dict(family="Inter", size=12, color="white")
            #         ))

            #         fig.update_layout(
            #             height=350,
            #             margin=dict(l=0, r=0, t=0, b=0),
            #             xaxis=dict(showgrid=False, visible=False),
            #             yaxis=dict(autorange="reversed"),
            #             plot_bgcolor='rgba(0,0,0,0)',
            #             paper_bgcolor='rgba(0,0,0,0)',
            #             font=dict(family="Inter", size=12)
            #         )

            #         st.plotly_chart(fig, use_container_width=True)



            with col1:
                with st.container():
                    st.markdown("#### Entity Distribution")

                    # =========================
                    # PREPARE ENTITY DATA
                    # =========================
                    entity_counts = (
                        df_su['ENTITY']
                        .value_counts()
                        .reset_index()
                    )
                    entity_counts.columns = ['ENTITY', 'COUNT']

                    entity_desc = (
                        df_su
                        .groupby('ENTITY')['អង្គភាពប្រើប្រាស់']
                        .unique()
                        .reset_index()
                    )

                    entity_desc['DESCRIPTION'] = entity_desc['អង្គភាពប្រើប្រាស់'].apply(
                        lambda x: ', '.join(x)
                    )

                    entity_final = entity_counts.merge(
                        entity_desc[['ENTITY', 'DESCRIPTION']],
                        on='ENTITY',
                        how='left'
                    )

                    # =========================
                    # TREEMAP
                    # =========================
                    fig_treemap = px.treemap(
                        entity_final,
                        path=['ENTITY'],
                        values='COUNT',
                        color='COUNT',
                        custom_data=['DESCRIPTION'],
                        color_continuous_scale='Blues',
                        height=400
                    )

                    fig_treemap.update_traces(
                        hovertemplate=
                            "<b>%{label}</b><br>" +
                            "Count: %{value}<br>" +
                            "Description:<br>%{customdata[0]}<extra></extra>"
                    )

                    fig_treemap.update_layout(
                        margin=dict(t=0, l=0, r=0, b=0),
                        paper_bgcolor='rgba(0,0,0,0)',
                        plot_bgcolor='rgba(0,0,0,0)',
                        font=dict(family="Inter", size=12),
                        hoverlabel=dict(
                            bgcolor="white",
                            font_size=12,
                            font_family="Inter"
                        )
                    )

                    st.plotly_chart(fig_treemap, use_container_width=True)


            with col2:
                with st.container():
                    st.markdown("#### Top 5 Entities")

                    top_entities = entity_final.head(5)

                    # =========================
                    # HORIZONTAL BAR CHART
                    # =========================
                    fig = go.Figure()
                    fig.add_trace(go.Bar(
                        y=top_entities['ENTITY'],
                        x=top_entities['COUNT'],
                        orientation='h',
                        customdata=top_entities['DESCRIPTION'],
                        marker=dict(
                            color="#3498db",
                            line=dict(color="#2980b9", width=1)
                        ),
                        text=top_entities['COUNT'],
                        textposition='auto',
                        textfont=dict(
                            family="Inter",
                            size=12,
                            color="white"
                        ),
                        hovertemplate=
                            "<b>%{y}</b><br>" +
                            "Count: %{x}<br>" +
                            "Description:<br>%{customdata}<extra></extra>"
                    ))

                    fig.update_layout(
                        height=350,
                        margin=dict(l=0, r=0, t=0, b=0),
                        xaxis=dict(showgrid=False, visible=False),
                        yaxis=dict(autorange="reversed"),
                        plot_bgcolor='rgba(0,0,0,0)',
                        paper_bgcolor='rgba(0,0,0,0)',
                        font=dict(family="Inter", size=12)
                    )

                    st.plotly_chart(fig, use_container_width=True)






            # with col2:
            #     with st.container():
            #         st.markdown("#### Top Entitys")
                    
            #         # Show top departments in a table with progress bars
            #         top_depts = df_dept.sort_values('ENTITY', ascending=False).head(5)
                    
            #         # Create a custom bar chart with progress bars
            #         fig = go.Figure()
            #         fig.add_trace(go.Bar(
            #             y=top_depts['ENTITY'],
            #             x=top_depts['ENTITY'].count,
            #             orientation='h',
            #             marker=dict(
            #                 color="#3498db",
            #                 line=dict(color="#2980b9", width=1)
            #             ),
            #             text=top_depts['ENTITY'],
            #             textposition='auto',
            #             textfont=dict(family="Inter", size=12, color="white")
            #         ))
                    
            #         fig.update_layout(
            #             height=400,
            #             margin=dict(l=0, r=0, t=0, b=0),
            #             xaxis=dict(showgrid=False, visible=False),
            #             yaxis=dict(autorange="reversed"),
            #             plot_bgcolor='rgba(0,0,0,0)',
            #             paper_bgcolor='rgba(0,0,0,0)',
            #             font=dict(family="Inter", size=12)
            #         )
                    
            #         st.plotly_chart(fig, use_container_width=True)
                    
                    # # Department summary stats
                    # st.markdown("""
                    # <div style="background: #f8f9fa; padding: 1rem; border-radius: 8px; margin-top: 1rem; border: 1px solid #e0e0e0;">
                    #     <p style="font-weight: 600; margin-bottom: 0.5rem; font-family: 'Inter', sans-serif; color: #2c3e50;">Entity Insights</p>
                    #     <ul style="margin: 0; padding-left: 1.2rem; color: #7f8c8d; font-size: 0.9rem; font-family: 'Inter', sans-serif;">
                    #         <li>LM-ABE has the most users (106)</li>
                    #         <li>TOP has the fewest users (1)</li>
                    #         <li>Average department size: 30 users</li>
                    #     </ul>
                    # </div>
                    # """, unsafe_allow_html=True)
        
        with tab2:
            col1, col2 = st.columns([1, 1.3], gap="medium")
            
            # with col1:
            #     with st.container():
            #         st.markdown("#### User Status Composition")
            #         if 'Status' in df.columns:
            #             status_counts = df['Status'].value_counts().reset_index()
            #             status_counts.columns = ['Status', 'Count']
                        
            #             # Create a donut chart with modern styling
            #             fig = px.pie(
            #                 status_counts,
            #                 values='Count',
            #                 names='Status',
            #                 hole=0.6,
            #                 color_discrete_sequence=['#3498db', '#e74c3c', '#2ecc71'],
            #                 height=400
            #             )
                        
            #             fig.update_traces(
            #                 textposition='inside',
            #                 textinfo='percent+label',
            #                 marker=dict(line=dict(color='white', width=1)),
            #                 pull=[0.1 if i == status_counts['Count'].idxmax() else 0 for i in status_counts.index],
            #                 textfont=dict(family="Inter", size=12)
            #             )
                        
            #             fig.update_layout(
            #                 showlegend=False,
            #                 margin=dict(t=0, b=0, l=0, r=0),
            #                 paper_bgcolor='rgba(0,0,0,0)',
            #                 font=dict(family="Inter", size=12),
            #                 annotations=[dict(
            #                     text=f"Total<br>{sum(status_counts['Count'])}",
            #                     x=0.5, y=0.5,
            #                     font_size=18,
            #                     showarrow=False,
            #                     font_family="Inter"
            #                 )]
            #             )
                        
            #             st.plotly_chart(fig, use_container_width=True)
                
        with col1:
            with st.container():
                st.markdown("#### User Status Composition")

                # Prepare status data from column sums
                status_data = {
                    "Status": [
                        "Active",
                        "Inactive",
                        "Inactive 90 Days"
                    ],
                    "Count": [
                        df_su['សកម្ម'].sum(),
                        df_su['ឈប់ប្រើប្រាស់'].sum(),
                        df_su['អសកម្ម'].sum()
                    ]
                }

                status_counts = pd.DataFrame(status_data)

                # Create donut chart
                fig = px.pie(
                    status_counts,
                    values='Count',
                    names='Status',
                    hole=0.6,
                    height=400,
                    color_discrete_sequence=['#3498db', '#e74c3c', '#2ecc71'],
                )

                fig.update_traces(
                    textposition='inside',
                    textinfo='percent+label',
                    marker=dict(line=dict(color='white', width=1)),
                    pull=[0.08, 0.08, 0.08],
                    textfont=dict(family="Inter", size=12)
                )

                fig.update_layout(
                    showlegend=False,
                    margin=dict(t=0, b=0, l=0, r=0),
                    paper_bgcolor='rgba(0,0,0,0)',
                    font=dict(family="Inter", size=12),
                    annotations=[dict(
                        text=f"Total<br>{status_counts['Count'].sum()}",
                        x=0.5, y=0.5,
                        font_size=18,
                        showarrow=False,
                        font_family="Inter"
                    )]
                )

                st.plotly_chart(fig, use_container_width=True)





            with col2:
                with st.container():

                    # df_melted = df_su.melt(
                    #     id_vars="អង្គភាពប្រើប្រាស់",
                    #     value_vars=["សកម្ម", "ឈប់ប្រើប្រាស់", "អសកម្ម"],
                    #     var_name="Status",
                    #     value_name="Users"
                    # )

                    # fig_bar = px.bar(
                    #     df_melted,
                    #     x="អង្គភាពប្រើប្រាស់",
                    #     y="Users",
                    #     color="Status",
                    #     barmode="stack",
                    #     height=400,
                    #     color_discrete_map={
                    #         "សកម្ម": "#2ecc71",
                    #         "ឈប់ប្រើប្រាស់": "#e74c3c",
                    #         "អសកម្ម": "#f1c40f"
                    #     }
                    # )

                    # fig_bar.update_layout(
                    #     xaxis_title="Organization",
                    #     yaxis_title="Number of Users",
                    #     legend_title="User Status",
                    #     margin=dict(t=30, b=30)
                    # )

                    # st.plotly_chart(fig_bar, use_container_width=True)
                    # Melt the data for stacked bar chart
                    # df_melted = df_su.melt(
                    #     id_vars="អង្គភាពប្រើប្រាស់",
                    #     value_vars=["សកម្ម", "ឈប់ប្រើប្រាស់", "អសកម្ម"],
                    #     var_name="Status",
                    #     value_name="Users"
                    # )

                    # # Create stacked bar chart with theme color
                    # fig_bar = px.bar(
                    #     df_melted,
                    #     x="អង្គភាពប្រើប្រាស់",
                    #     y="Users",
                    #     color="Status",
                    #     barmode="stack",
                    #     height=400,
                    #     color_discrete_map={
                    #         "សកម្ម": "#3498db",  # Your theme color for active users
                    #         "ឈប់ប្រើប្រាស់": "#e74c3c",  # Red for stopped
                    #         "អសកម្ម": "#f39c12"  # Orange for inactive
                    #     }
                    # )

                    # # Add count values on bars
                    # fig_bar.update_traces(
                    #     texttemplate='%{y}',
                    #     textposition='inside',
                    #     textfont=dict(
                    #         color='white',
                    #         size=11
                    #     ),
                    #     marker_line_width=0.5,
                    #     marker_line_color='white'
                    # )

                    # # Update layout for clean appearance
                    # fig_bar.update_layout(
                    #     xaxis_title="អង្គភាពប្រើប្រាស់",
                    #     yaxis_title="ចំនួនអ្នកប្រើប្រាស់",
                    #     legend_title="ស្ថានភាព",
                    #     margin=dict(t=30, b=30, l=0, r=0),
                    #     plot_bgcolor='white',
                    #     paper_bgcolor='white',
                    #     font=dict(
                    #         family='Arial, sans-serif',
                    #         size=12,
                    #         color='#2c3e50'
                    #     ),
                    #     xaxis=dict(
                    #         title_font=dict(size=14),
                    #         tickfont=dict(size=11),
                    #         showgrid=False,
                    #         linecolor='lightgray',
                    #         tickangle=0 if len(df_melted["អង្គភាពប្រើប្រាស់"].unique()) <= 10 else -45
                    #     ),
                    #     yaxis=dict(
                    #         title_font=dict(size=14),
                    #         tickfont=dict(size=11),
                    #         gridcolor='whitesmoke',
                    #         linecolor='lightgray'
                    #     ),
                    #     legend=dict(
                    #         title_font=dict(size=12),
                    #         font=dict(size=11),
                    #         orientation="h",
                    #         yanchor="bottom",
                    #         y=1.02,
                    #         xanchor="right",
                    #         x=1,
                    #         bgcolor='rgba(255, 255, 255, 0.8)',
                    #         bordercolor='lightgray',
                    #         borderwidth=1
                    #     ),
                    #     hovermode="x unified"
                    # )

                    # # Customize hover information
                    # fig_bar.update_traces(
                    #     hovertemplate='<b>%{x}</b><br>' +
                    #                 'ស្ថានភាព: %{data.name}<br>' +
                    #                 'ចំនួន: %{y}<br>' +
                    #                 '<extra></extra>'
                    # )

                    # st.plotly_chart(fig_bar, use_container_width=True)
            
# Melt the data for stacked bar chart
                    # df_melted = df_su.melt(
                    #     id_vars="អង្គភាពប្រើប្រាស់",
                    #     value_vars=["សកម្ម", "ឈប់ប្រើប្រាស់", "អសកម្ម"],
                    #     var_name="Status",
                    #     value_name="Users"
                    # )

                    # # Create stacked bar chart with theme color
                    # fig_bar = px.bar(
                    #     df_melted,
                    #     x="អង្គភាពប្រើប្រាស់",
                    #     y="Users",
                    #     color="Status",
                    #     barmode="stack",
                    #     height=400,
                    #     color_discrete_map={
                    #         "សកម្ម": "#3498db",  # Your theme color
                    #         "ឈប់ប្រើប្រាស់": "#e74c3c",
                    #         "អសកម្ម": "#f39c12"
                    #     }
                    # )

                    # # Add count values on each bar segment
                    # fig_bar.update_traces(
                    #     texttemplate='%{y}',
                    #     textposition='inside',
                    #     textfont=dict(
                    #         color='white',
                    #         size=11
                    #     ),
                    #     marker_line_width=0.5,
                    #     marker_line_color='white'
                    # )

                    # # Clean layout
                    # fig_bar.update_layout(
                    #     xaxis_title="អង្គភាពប្រើប្រាស់",
                    #     yaxis_title="ចំនួនអ្នកប្រើប្រាស់",
                    #     legend_title="ស្ថានភាព",
                    #     margin=dict(t=30, b=30, l=0, r=0),
                    #     plot_bgcolor='white',
                    #     paper_bgcolor='white',
                    #     font=dict(size=12),
                    #     xaxis=dict(
                    #         showgrid=False,
                    #         linecolor='lightgray'
                    #     ),
                    #     yaxis=dict(
                    #         gridcolor='whitesmoke',
                    #         linecolor='lightgray'
                    #     ),
                    #     legend=dict(
                    #         orientation="h",
                    #         yanchor="bottom",
                    #         y=1.02,
                    #         xanchor="right",
                    #         x=1
                    #     )
                    # )

                    # st.plotly_chart(fig_bar, use_container_width=True)
                    # # Melt the data
                    # df_melted = df_su.melt(
                    #     id_vars="អង្គភាពប្រើប្រាស់",
                    #     value_vars=["សកម្ម", "ឈប់ប្រើប្រាស់", "អសកម្ម"],
                    #     var_name="Status",
                    #     value_name="Users"
                    # )

                    # # Create stacked bar chart
                    # fig_bar = px.bar(
                    #     df_melted,
                    #     x="អង្គភាពប្រើប្រាស់",
                    #     y="Users",
                    #     color="Status",
                    #     barmode="stack",
                    #     height=400,
                    #     color_discrete_map={
                    #         "សកម្ម": "#3498db",
                    #         "ឈប់ប្រើប្រាស់": "#e74c3c",
                    #         "អសកម្ម": "#f39c12"
                    #     }
                    # )

                    # # Calculate totals for each organization
                    # totals = df_su.set_index("អង្គភាពប្រើប្រាស់")[["សកម្ម", "ឈប់ប្រើប្រាស់", "អសកម្ម"]].sum(axis=1)

                    # # Add total labels on top
                    # for i, org in enumerate(totals.index):
                    #     fig_bar.add_annotation(
                    #         x=org,
                    #         y=totals.iloc[i],
                    #         text=str(int(totals.iloc[i])),
                    #         showarrow=False,
                    #         yshift=10,
                    #         font=dict(size=11, color="#2c3e50")
                    #     )

                    # # Simple clean layout
                    # fig_bar.update_layout(
                    #     xaxis_title="អង្គភាពប្រើប្រាស់",
                    #     yaxis_title="ចំនួនអ្នកប្រើប្រាស់",
                    #     legend_title="ស្ថានភាព",
                    #     margin=dict(t=40, b=30, l=0, r=0),
                    #     plot_bgcolor='white',
                    #     paper_bgcolor='white',
                    #     showlegend=True
                    # )

                    # st.plotly_chart(fig_bar, use_container_width=True)
                    # Simple grouped bar chart
                    # fig = px.bar(
                    #     df_su,
                    #     x="អង្គភាពប្រើប្រាស់",
                    #     y=["សកម្ម", "ឈប់ប្រើប្រាស់", "អសកម្ម"],
                    #     barmode="group",
                    #     labels={
                    #         "value": "ចំនួនអ្នកប្រើប្រាស់",
                    #         "variable": "ស្ថានភាព"
                    #     },
                    #     color_discrete_sequence=["#3498db", "#e74c3c", "#f39c12"]
                    # )

                    # # Clean styling
                    # fig.update_traces(
                    #     texttemplate='%{y}',
                    #     textposition='inside',
                    #     textfont=dict(color='white'),
                    #     width=0.3
                    # )

                    # fig.update_layout(
                    #     height=500,
                    #     plot_bgcolor='white',
                    #     paper_bgcolor='white',
                    #     showlegend=True,
                    #     xaxis=dict(showgrid=False),
                    #     yaxis=dict(gridcolor='#f0f0f0')
                    # )

                    # st.plotly_chart(fig, use_container_width=True)


                                        # Group by organization and sum the values
                    df_grouped = df_su.groupby("អង្គភាពប្រើប្រាស់", as_index=False).agg({
                        "សកម្ម": "sum",
                        "ឈប់ប្រើប្រាស់": "sum", 
                        "អសកម្ម": "sum"
                    })

                    # Add total column
                    df_grouped['សរុប'] = df_grouped[["សកម្ម", "ឈប់ប្រើប្រាស់", "អសកម្ម"]].sum(axis=1)

                    # Sort by total (optional)
                    df_grouped = df_grouped.sort_values('សរុប', ascending=False)

                    # Create grouped bar chart
                    fig = px.bar(
                        df_grouped,
                        x="អង្គភាពប្រើប្រាស់",
                        y=["សកម្ម", "ឈប់ប្រើប្រាស់", "អសកម្ម"],
                        barmode="group",
                        labels={
                            "value": "ចំនួនអ្នកប្រើប្រាស់",
                            "variable": "ស្ថានភាព"
                        },
                        color_discrete_sequence=["#3498db", "#e74c3c", "#f39c12"]
                    )

                    # Add count values inside bars
                    fig.update_traces(
                        texttemplate='%{y}',
                        textposition='inside',
                        textfont=dict(
                            color='white',
                            size=11,
                            weight='bold'
                        ),
                        width=0.35,
                        marker_line_width=0.5,
                        marker_line_color="white"
                    )

                    # Add total labels on top
                    for i, row in df_grouped.iterrows():
                        fig.add_annotation(
                            x=row["អង្គភាពប្រើប្រាស់"],
                            y=row["សរុប"],
                            text=f"{int(row['សរុប'])}",
                            showarrow=False,
                            yshift=15,
                            font=dict(size=12, color="#2c3e50", weight="bold")
                        )

                    # Calculate y-axis max with padding
                    max_value = df_grouped[["សកម្ម", "ឈប់ប្រើប្រាស់", "អសកម្ម"]].max().max()
                    y_max = max_value * 1.2

                    # Update layout
                    fig.update_layout(
                        height=500,
                        margin=dict(l=0, r=0, t=40, b=0),
                        plot_bgcolor="white",
                        paper_bgcolor="white",
                        font=dict(family="Arial, sans-serif"),
                        xaxis=dict(
                            title_text="អង្គភាពប្រើប្រាស់",
                            title_font=dict(size=14),
                            tickfont=dict(size=12),
                            showgrid=False,
                            linecolor="lightgray"
                        ),
                        yaxis=dict(
                            title_text="ចំនួនអ្នកប្រើប្រាស់",
                            title_font=dict(size=14),
                            tickfont=dict(size=11),
                            gridcolor="whitesmoke",
                            linecolor="lightgray",
                            range=[0, y_max]
                        ),
                        legend=dict(
                            title_text="ស្ថានភាព",
                            title_font=dict(size=12),
                            font=dict(size=11),
                            orientation="h",
                            yanchor="bottom",
                            y=1.02,
                            xanchor="center",
                            x=0.5,
                            bgcolor="rgba(255, 255, 255, 0.8)",
                            bordercolor="lightgray",
                            borderwidth=1
                        ),
                        bargap=0.4,
                        bargroupgap=0.05,
                        hovermode="x unified"
                    )

                    # Add hover template
                    fig.update_traces(
                        hovertemplate="<b>%{data.name}</b><br>" +
                                    "អង្គភាព: %{x}<br>" +
                                    "ចំនួន: %{y}<br>" +
                                    "<extra></extra>"
                    )

                    st.plotly_chart(fig, use_container_width=True)
                    # # Grouped bar chart
                    # fig = px.bar(
                    #     df_su,
                    #     x="អង្គភាពប្រើប្រាស់",
                    #     y=["សកម្ម", "ឈប់ប្រើប្រាស់", "អសកម្ម"],
                    #     barmode="group",
                    #     labels={
                    #         "value": "ចំនួនអ្នកប្រើប្រាស់",
                    #         "variable": "ស្ថានភាព"
                    #     },
                    #     color_discrete_sequence=["#3498db", "#95a5a6", "#34495e"]  # Blue + neutral grays
                    # )

                    # # Add count values with better spacing
                    # fig.update_traces(
                    #     texttemplate='%{y}',
                    #     textposition='outside',
                    #     textfont=dict(size=10),  # Smaller font for labels
                    #     width=0.25,  # Thinner bars
                    #     marker_line_width=0.5,
                    #     marker_line_color="white"
                    # )

                    # # Calculate max value for better y-axis range
                    # max_value = df_su[["សកម្ម", "ឈប់ប្រើប្រាស់", "អសកម្ម"]].max().max()
                    # y_max = max_value * 1.15  # Add 15% padding for labels

                    # fig.update_layout(
                    #     height=500,
                    #     margin=dict(l=0, r=0, t=20, b=30),  # More bottom margin for x-labels
                    #     plot_bgcolor="white",
                    #     paper_bgcolor="white",
                    #     xaxis=dict(
                    #         showgrid=False,
                    #         tickfont=dict(size=10),  # Smaller x-axis labels
                    #         tickangle=-45,  # Rotate labels for better readability
                    #         automargin=True,  # Auto-adjust margins
                    #         title_text="អង្គភាពប្រើប្រាស់",
                    #         title_font=dict(size=12)
                    #     ),
                    #     yaxis=dict(
                    #         gridcolor="#f5f5f5",
                    #         range=[0, y_max],  # Set y-axis range with padding
                    #         title_text="ចំនួនអ្នកប្រើប្រាស់",
                    #         title_font=dict(size=12)
                    #     ),
                    #     legend=dict(
                    #         orientation="h",
                    #         yanchor="bottom",
                    #         y=1.02,
                    #         xanchor="center",
                    #         x=0.5,
                    #         font=dict(size=11)
                    #     ),
                    #     bargap=0.3,  # More gap between groups
                    #     bargroupgap=0.05  # Less gap within groups
                    # )

                    # st.plotly_chart(fig, use_container_width=True)


            #         st.markdown("#### Status Over Time")
                    
            #         if 'Status' in df.columns and 'Z_CREATEDTTM' in df.columns:
            #             try:
            #                 df['CREATED_DATE'] = pd.to_datetime(df['Z_CREATEDTTM'], format='%d-%b-%y %I.%M.%S.%f %p', errors='coerce')
            #                 df['YearMonth'] = df['CREATED_DATE'].dt.to_period('M').astype(str)
                            
            #                 # Create a line chart showing status changes over time
            #                 status_over_time = df.groupby(['YearMonth', 'Status']).size().unstack().fillna(0)
                            
            #                 fig = go.Figure()
                            
            #                 # Define a professional color palette
            #                 status_colors = {
            #                     'Active': '#3498db',
            #                     'Inactive': '#e74c3c',
            #                     'Pending': '#2ecc71'
            #                 }
                            
            #                 for status in status_counts['Status']:
            #                     fig.add_trace(go.Scatter(
            #                         x=status_over_time.index,
            #                         y=status_over_time[status],
            #                         name=status,
            #                         mode='lines+markers',
            #                         line=dict(width=2.5, color=status_colors.get(status, '#95a5a6')),
            #                         marker=dict(size=8),
            #                         hovertemplate=f"<b>{status}</b><br>%{{x}}<br>%{{y}} users<extra></extra>"
            #                     ))
                            
            #                 fig.update_layout(
            #                     height=400,
            #                     margin=dict(l=0, r=0, t=0, b=0),
            #                     xaxis_title=None,
            #                     yaxis_title="User Count",
            #                     legend=dict(
            #                         orientation="h",
            #                         yanchor="bottom",
            #                         y=-0.3,
            #                         xanchor="center",
            #                         x=0.5,
            #                         font=dict(family="Inter", size=12)
            #                     ),
            #                     plot_bgcolor='rgba(0,0,0,0)',
            #                     paper_bgcolor='rgba(0,0,0,0)',
            #                     font=dict(family="Inter", size=12),
            #                     hoverlabel=dict(
            #                         bgcolor="white",
            #                         font_size=12,
            #                         font_family="Inter"
            #                     )
            #                 )
                            
            #                 st.plotly_chart(fig, use_container_width=True)
            #             except:
            #                 st.warning("Could not process creation dates for timeline analysis")
        
        with tab3:
            col1, col2, col3 = st.columns([1, 1, 1], gap="medium")
            
            with col1:
                with st.container():
                    st.markdown("#### Gender Distribution")
                    
                    if 'GENDER' in df.columns:
                        gender_df = df.copy()
                        gender_mapping = {
                            'M': 'Male',
                            'F': 'Female',
                            '': 'Not Specified',
                            None: 'Not Specified'
                        }
                        gender_df['GENDER_LABEL'] = gender_df['GENDER'].map(gender_mapping).fillna('Not Specified')
                        gender_counts = gender_df['GENDER_LABEL'].value_counts().reset_index()
                        gender_counts.columns = ['Gender', 'Count']
                        
                        fig = px.bar(
                            gender_counts,
                            x='Gender',
                            y='Count',
                            color='Gender',
                            color_discrete_map={
                                'Male': '#3498db',
                                'Female': '#e74c3c',
                                'Not Specified': '#95a5a6'
                            },
                            text='Count'
                        )
                        fig.update_layout(
                            showlegend=False,
                            margin=dict(t=0, b=0, l=0, r=0),
                            xaxis_title=None,
                            yaxis_title=None,
                            plot_bgcolor='rgba(0,0,0,0)',
                            paper_bgcolor='rgba(0,0,0,0)',
                            font=dict(family="Inter", size=12)
                        )
                        fig.update_traces(
                            textposition='outside',
                            textfont=dict(family="Inter", size=12),
                            marker=dict(line=dict(width=0))
                        )
                        st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                with st.container():
                    st.markdown("#### Age Distribution")
                    
                    if 'Z_DOB' in df.columns:
                        try:
                            today = pd.Timestamp('today')
                            df['DOB'] = pd.to_datetime(df['Z_DOB'], errors='coerce')
                            df['Age'] = (today - df['DOB']).dt.days // 365
                            
                            bins = [0, 20, 30, 40, 50, 60, 70, 100]
                            labels = ['<20', '20-29', '30-39', '40-49', '50-59', '60-69', '70+']
                            df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)
                            df['Age Group'] = df['Age Group'].astype(object).fillna('Unknown')
                            
                            age_group_counts = df['Age Group'].value_counts().sort_index().reset_index()
                            age_group_counts.columns = ['Age Group', 'Count']
                            
                            fig = px.bar(
                                age_group_counts,
                                x='Age Group',
                                y='Count',
                                color='Age Group',
                                color_discrete_sequence=['#3498db', '#2980b9', '#1f618d', '#154360', '#0b2638', '#061a26', '#030d13'],
                                text='Count'
                            )
                            fig.update_layout(
                                showlegend=False,
                                margin=dict(t=0, b=0, l=0, r=0),
                                xaxis_title=None,
                                yaxis_title=None,
                                plot_bgcolor='rgba(0,0,0,0)',
                                paper_bgcolor='rgba(0,0,0,0)',
                                font=dict(family="Inter", size=12)
                            )
                            fig.update_traces(
                                textposition='outside',
                                textfont=dict(family="Inter", size=12),
                                marker=dict(line=dict(width=0))
                            )
                            st.plotly_chart(fig, use_container_width=True)
                        except:
                            st.warning("Could not process date of birth data")
            
            with col3:
                with st.container():
                    st.markdown("#### Position Levels")
                    
                    if 'Z_POSITION_LEVEL' in df.columns:
                        position_mapping = {
                            'HE': 'HE',
                            'MI': 'MI',
                            'MS': 'MS',
                            'MR': 'MR',
                            '': 'Not Specified',
                            None: 'Not Specified'
                        }
                        
                        df['POSITION_LABEL'] = df['Z_POSITION_LEVEL'].map(position_mapping).fillna('Not Specified')
                        position_counts = df['POSITION_LABEL'].value_counts().reset_index()
                        position_counts.columns = ['Position Level', 'Count']
                        
                        fig = px.pie(
                            position_counts,
                            values='Count',
                            names='Position Level',
                            hole=0.5,
                            color_discrete_sequence=['#3498db', '#2980b9', '#1f618d', '#154360', '#95a5a6']
                        )
                        fig.update_layout(
                            showlegend=True,
                            margin=dict(t=0, b=0, l=0, r=0),
                            legend=dict(
                                orientation="h",
                                yanchor="bottom",
                                y=-0.3,
                                xanchor="center",
                                x=0.5,
                                font=dict(family="Inter", size=10)
                            ),
                            font=dict(family="Inter", size=12)
                        )
                        fig.update_traces(
                            textposition='inside',
                            textinfo='percent+label',
                            textfont=dict(family="Inter", size=12),
                            marker=dict(line=dict(color='white', width=1))
                        )
                        st.plotly_chart(fig, use_container_width=True)
        
        # ======================
        # USER ACTIVITY TIMELINE
        # ======================
        st.markdown('<div class="section-header">User Activity Timeline</div>', unsafe_allow_html=True)
        
        if 'Z_CREATEDTTM' in df.columns:
            try:
                df['CREATED_DATE'] = pd.to_datetime(df['Z_CREATEDTTM'], format='%d-%b-%y %I.%M.%S.%f %p', errors='coerce')
                date_df = df.dropna(subset=['CREATED_DATE'])
                
                # Create monthly and quarterly aggregations
                date_df['YearMonth'] = date_df['CREATED_DATE'].dt.to_period('M').astype(str)
                date_df['YearQuarter'] = date_df['CREATED_DATE'].dt.to_period('Q').astype(str)
                
                # User acquisition trends
                monthly_counts = date_df['YearMonth'].value_counts().sort_index().reset_index()
                monthly_counts.columns = ['YearMonth', 'New Users']
                
                quarterly_counts = date_df['YearQuarter'].value_counts().sort_index().reset_index()
                quarterly_counts.columns = ['YearQuarter', 'New Users']
                
                # Create a dual-axis chart
                fig = go.Figure()
                
                # Add monthly bars
                fig.add_trace(go.Bar(
                    x=monthly_counts['YearMonth'],
                    y=monthly_counts['New Users'],
                    name='Monthly',
                    marker_color='#3498db',
                    opacity=0.8,
                    hovertemplate="<b>%{x}</b><br>%{y} new users<extra></extra>"
                ))
                
                # Add quarterly line
                fig.add_trace(go.Scatter(
                    x=quarterly_counts['YearQuarter'],
                    y=quarterly_counts['New Users'].rolling(2, min_periods=1).mean(),
                    name='Quarterly Trend',
                    line=dict(color='#2c3e50', width=3, dash='dot'),
                    mode='lines+markers',
                    marker=dict(size=8, color='#e74c3c'),
                    hovertemplate="<b>%{x}</b><br>%{y:.1f} avg users<extra></extra>"
                ))
                
                fig.update_layout(
                    height=400,
                    margin=dict(l=0, r=0, t=0, b=0),
                    xaxis_title=None,
                    yaxis_title="New Users",
                    legend=dict(
                        orientation="h",
                        yanchor="bottom",
                        y=-0.3,
                        xanchor="center",
                        x=0.5,
                        font=dict(family="Inter", size=12)
                    ),
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    barmode='group',
                    font=dict(family="Inter", size=12),
                    hoverlabel=dict(
                        bgcolor="white",
                        font_size=12,
                        font_family="Inter"
                    )
                )
                
                st.plotly_chart(fig, use_container_width=True)
            except Exception as e:
                st.error(f"Error processing timeline data: {str(e)}")  
                # # Calculate growth metrics
                # if len(monthly_counts) > 1:
                #     latest_month = monthly_counts.iloc[-1]['New Users']
                #     prev_month = monthly_counts.iloc[-2]['New Users']
                #     mom_growth = ((latest_month - prev_month) / prev_month * 100) if prev_month > 0 else 0
                    
                #     st.markdown(f"""
                #     <div style="background: #f8f9fa; padding: 1rem; border-radius: 8px; margin-top: 1rem; border: 1px solid #e0e0e0;">
                #         <p style="font-weight: 600; margin-bottom: 0.5rem; font-family: 'Inter', sans-serif; color: #2c3e50;">Growth Insights</p>
                #         <ul style="margin: 0; padding-left: 1.2rem; color: #7f8c8d; font-size: 0.9rem; font-family: 'Inter', sans-serif;">
                #             <li>Average Monthly New Users: <strong>{monthly_counts['New Users'].mean():.1f}</strong></li>
                #             <li>Peak Month: <strong>{monthly_counts.loc[monthly_counts['New Users'].idxmax(), 'YearMonth']}</strong> ({monthly_counts['New Users'].max()} users)</li>
                #         </ul>
                #     </div>
                #     """, unsafe_allow_html=True)
                # # <li>Month-over-Month Growth: <strong>{mom_growth:.1f}%</strong></li>
                


            st.markdown('<div class="section-header">User Summary Table by Organization</div>', unsafe_allow_html=True)
            # # Load data
            # df_su = pd.read_excel("Excel files/User Alias Data(Dec) from prod.xlsx")
            # int(df_summary["សកម្ម"].sum())

            numeric_cols = ["សកម្ម", "ឈប់ប្រើប្រាស់", "អសកម្ម"]
            df_su[numeric_cols] = df_su[numeric_cols].apply(
                pd.to_numeric, errors="coerce"
            ).fillna(0)

            # Calculate total
            df_su["សរុប"] = df_su["សកម្ម"] + df_su["ឈប់ប្រើប្រាស់"] + df_su["អសកម្ម"]

          
            # BUILD SUMMARY TABLE
            df_summary = (
                df_su.groupby("អង្គភាពប្រើប្រាស់", as_index=False)
                .agg(
                    ចំនួនការដ្ឋាន=("អង្គភាពប្រើប្រាស់", "count"),
                    សកម្ម=("សកម្ម", "sum"),
                    ឈប់ប្រើប្រាស់=("ឈប់ប្រើប្រាស់", "sum"),
                    អសកម្ម=("អសកម្ម", "sum"),
                    សរុប=("សរុប", "sum")
                )
            )
     
               
            df_display = df_summary.copy()

            # Replace 1 → N/A ONLY for display
            df_display["ចំនួនការដ្ឋាន"] = df_display["ចំនួនការដ្ឋាន"].apply(
                lambda x: "N/A" if x == 1 else x
)

                # Rename columns to Khmer
            df_summary = df_summary.rename(columns={
                "ENTITY": "ចំនួនការដ្ឋាន" 
            })
            # Add Khmer numbering for rows
            khmer_numbers = [
                "១","២","៣","៤","៥","៦","៧","៨","៩","១០",
                "១១","១២","១៣","១៤","១៥"
            ]

            df_display.insert(0, "ល.រ", khmer_numbers[:len(df_display)])

            # Add totals row
            totals_row = {
                    "ល.រ": "សរុប",
                    "អង្គភាពប្រើប្រាស់": "",
                    "ចំនួនការដ្ឋាន": int(df_summary["ចំនួនការដ្ឋាន"].sum()),
                    "សកម្ម": int(df_summary["សកម្ម"].sum()),
                    "ឈប់ប្រើប្រាស់": int(df_summary["ឈប់ប្រើប្រាស់"].sum()),
                    "អសកម្ម": int(df_summary["អសកម្ម"].sum()),
                    "សរុប": int(df_summary["សរុប"].sum()),
                }

            df_summary_with_totals = pd.concat(
                [df_display, pd.DataFrame([totals_row])],
                ignore_index=True
            )


            # TABS
            tab1, tab2 = st.tabs([ "Graph","Table"])

            with tab2:
                st.dataframe(
                    df_summary_with_totals,
                    use_container_width=True,
                    height=500,
                    hide_index=True,
                    column_config={
                        "ល.រ": st.column_config.TextColumn("ល.រ"),
                        "អង្គភាពប្រើប្រាស់": st.column_config.TextColumn("អង្គភាពប្រើប្រាស់"),
                        "ចំនួនការដ្ឋាន": st.column_config.NumberColumn("ចំនួនការដ្ឋាន"),
                        "សកម្ម": st.column_config.NumberColumn("សកម្ម"),
                        "ឈប់ប្រើប្រាស់": st.column_config.NumberColumn("ឈប់ប្រើប្រាស់"),
                        "អសកម្ម": st.column_config.NumberColumn("អសកម្ម"),
                        "សរុប": st.column_config.NumberColumn("សរុប"),
                    }
                )

            # GRAPH TAB

            with tab1:
                colors = ["#3498db", "#2ecc71", "#e74c3c"]
    
                fig = px.bar(
                    df_summary,
                    x="អង្គភាពប្រើប្រាស់",
                    y=["សកម្ម", "ឈប់ប្រើប្រាស់", "អសកម្ម"],
                    barmode="group",
                    labels={
                        "value": "ចំនួនអ្នកប្រើប្រាស់",
                        "variable": "ស្ថានភាព",
                        "អង្គភាពប្រើប្រាស់": "អង្គភាពប្រើប្រាស់"
                    },
                    color_discrete_sequence=colors
                )
                
                # Add different text styling for each trace
                for i, trace in enumerate(fig.data):
                    # Choose text position based on bar series
                    if i == 0:  # First series (សកម្ម) - usually largest, put inside
                        fig.data[i].textposition = 'inside'
                        fig.data[i].textfont = dict(color='white', size=11)
                    else:  # Other series - put outside if values are small
                        fig.data[i].textposition = 'outside'
                        fig.data[i].textfont = dict(size=10)
                    
                    fig.data[i].texttemplate = '%{y}'
                    fig.data[i].marker.line.width = 0.5
                    fig.data[i].marker.line.color = "white"
                    fig.data[i].width = 0.25
                
                fig.update_layout(
                    height=500,
                    margin=dict(l=0, r=0, t=20, b=20),
                    plot_bgcolor="white",
                    paper_bgcolor="white",
                    font=dict(size=12),
                    xaxis=dict(
                        title_font=dict(size=14),
                        tickfont=dict(size=12),
                        showgrid=False,
                        linecolor="lightgray"
                    ),
                    yaxis=dict(
                        title_font=dict(size=14),
                        tickfont=dict(size=12),
                        gridcolor="whitesmoke",
                        linecolor="lightgray"
                    ),
                    legend=dict(
                        title="ស្ថានភាព",
                        title_font=dict(size=12),
                        font=dict(size=11),
                        orientation="h",
                        yanchor="bottom",
                        y=1.02,
                        xanchor="right",
                        x=1
                    ),
                    bargap=0.15,
                    bargroupgap=0.1
                )
                
                st.plotly_chart(fig, use_container_width=True)
    

        # ======================
        # USER DETAILS TABLE
        # ======================
        st.markdown('<div class="section-header">User Details</div>', unsafe_allow_html=True)
        
        selected_columns = [
            'OPRID', 'NAME_KH', 'USERIDALIAS', 'Type', 'Status', 'Z_CREATEDTTM',
            'Organization_Name', 'GENDER', 'Z_POSITION_LEVEL'
        ]
        existing_columns = [col for col in selected_columns if col in df.columns]
        
        if existing_columns:
            # Add interactive filters
            with st.expander("🔍 Filter Options", expanded=False):
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    status_filter = st.multiselect(
                        "Filter by Status",
                        options=df['Status'].unique() if 'Status' in df.columns else [],
                        default=df['Status'].unique() if 'Status' in df.columns else []
                    )
                
                with col2:
                    type_filter = st.multiselect(
                        "Filter by Type",
                        options=df['Type'].unique() if 'Type' in df.columns else [],
                        default=df['Type'].unique() if 'Type' in df.columns else []
                    )
                
                with col3:
                    search_term = st.text_input("Search by Name or ID")
            
            # Apply filters
            filtered_df = df.copy()
            if 'Status' in df.columns and status_filter:
                filtered_df = filtered_df[filtered_df['Status'].isin(status_filter)]
            if 'Type' in df.columns and type_filter:
                filtered_df = filtered_df[filtered_df['Type'].isin(type_filter)]
            if search_term:
                filtered_df = filtered_df[
                    filtered_df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), 
                    axis=1)
                ]
            
            # Display the table with enhanced styling
            st.dataframe(
                filtered_df[existing_columns],
                use_container_width=True,
                height=500,
                column_config={
                    "OPRID": st.column_config.TextColumn("User ID"),
                    "NAME_KH": st.column_config.TextColumn("Name (KH)"),
                    "USERIDALIAS": st.column_config.TextColumn("Username"),
                    "Type": st.column_config.TextColumn("User Type"),
                    "Status": st.column_config.TextColumn("Status"),
                    "Z_CREATEDTTM": st.column_config.DatetimeColumn("Created Date"),
                    "Organization_Name": st.column_config.TextColumn("Organization"),
                    "GENDER": st.column_config.TextColumn("Gender"),
                    "Z_POSITION_LEVEL": st.column_config.TextColumn("Position Level")
                }
            )
            
            # Add export options
            st.download_button(
                label="📥 Export to CSV",
                data=filtered_df[existing_columns].to_csv(index=False).encode('utf-8'),
                file_name="user_analytics_export.csv",
                mime="text/csv",
                use_container_width=True
            )
    
    except FileNotFoundError:
        st.error("User data file not found. Please ensure 'User Management.xlsx' is in the correct location.")
    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}")



if __name__ == "__main__":
    show()







# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go
# from datetime import datetime
# import numpy as np

# def show():
#     """Professional User Analytics Dashboard"""
#     # Remove default padding
#     st.markdown("""
#         <style>
#             .block-container {
#                 padding-top: 1rem;
#                 padding-bottom: 3rem;
#             }
#         </style>
#     """, unsafe_allow_html=True)
    
#     # Dashboard header
#     st.title("👥 ផ្ទាំងព័ត៌មានអ្នកប្រើប្រាស់")
#     st.markdown("ការវិភាគទិន្នន័យអ្នកប្រើប្រាស់និងស្ថានភាពគណនី")
    
#     # ======================
#     # SUMMARY TABLE - USING STREAMLIT COMPONENTS
#     # ======================
#     st.markdown("---")
#     st.subheader("តារាងសង្ខេបអ្នកប្រើប្រាស់តាមអង្គភាព")
    
#     # Summary data
#     summary_data = [
#         ["១", "ច្បាប់សាធារណៈ", "N/A", 45, 3, 1, 49],
#         ["២", "អគ្គនាយកដ្ឋាន (៥)", 9, 59, 2, 26, 87],
#         ["៣", "ក្រសួង (៣៨)", 38, 521, 147, 270, 938],
#         ["៤", "អង្គភាពជាតិការងារបច្ចេកវិទ្យាព័ត៌មាន (១១៨)", 118, 621, 90, 196, 907],
#         ["៥", "អង្គភាពជាតិការងារបច្ចេកវិទ្យាព័ត៌មាន (១៨)", 18, 42, 1, 1, 44],
#         ["៦", "បច្ចេកវិទ្យា អាយធី-២៥ (២៥)", 25, 235, 46, 77, 358],
#         ["៧", "ស្ថាប័នអាយធី-២៥ (២៥)", 25, 297, 79, 19, 395],
#         ["៨", "ស្ថាប័នអាយធី-២៥ (២៥)", 25, 157, 28, 104, 289],
#         ["៩", "ក្រុមស្ថាបនាសេវា (៩)", 9, 59, 2, 26, 87],
#         ["១០", "ក្រុម គណៈ ឧបត្ថម្ភ (៩៥)", 95, 429, 14, 78, 521],
#         ["១១", "បច្ចេកវិទ្យា បណ្ដាញ និងទីផ្សារ អាយធី-២៥ (២៥)", 25, 161, 0, 0, 162],
#     ]

#     summary_columns = [
#         "ល.រ", "អង្គភាពប្រើប្រាស់", "ចំនួនកាតព្វកិច្ច",
#         "សរុប", "ប្រើប្រាស់", "មិនប្រើ", "សរុបចុងក្រោយ"
#     ]

#     df_summary = pd.DataFrame(summary_data, columns=summary_columns)
    
#     # Create a styled dataframe
#     styled_df = df_summary.copy()
    
#     # Calculate totals
#     styled_df['ចំនួនកាតព្វកិច្ច_numeric'] = pd.to_numeric(
#         df_summary['ចំនួនកាតព្វកិច្ច'], 
#         errors='coerce'
#     ).fillna(0).astype(int)
    
#     # Add totals row
#     totals_row = {
#         "ល.រ": "សរុប",
#         "អង្គភាពប្រើប្រាស់": "",
#         "ចំនួនកាតព្វកិច្ច": styled_df['ចំនួនកាតព្វកិច្ច_numeric'].sum(),
#         "សរុប": styled_df['សរុប'].sum(),
#         "ប្រើប្រាស់": styled_df['ប្រើប្រាស់'].sum(),
#         "មិនប្រើ": styled_df['មិនប្រើ'].sum(),
#         "សរុបចុងក្រោយ": styled_df['សរុបចុងក្រោយ'].sum(),
#     }
    
#     # Display as a nice table with custom styling
#     col1, col2, col3 = st.columns([1, 3, 1])
    
#     with col2:
#         st.dataframe(
#             df_summary,
#             use_container_width=True,
#             hide_index=True,
#             height=500,
#             column_config={
#                 "ល.រ": st.column_config.TextColumn(width="small"),
#                 "អង្គភាពប្រើប្រាស់": st.column_config.TextColumn(width="large"),
#                 "ចំនួនកាតព្វកិច្ច": st.column_config.TextColumn(width="medium"),
#                 "សរុប": st.column_config.NumberColumn(width="small"),
#                 "ប្រើប្រាស់": st.column_config.NumberColumn(width="small"),
#                 "មិនប្រើ": st.column_config.NumberColumn(width="small"),
#                 "សរុបចុងក្រោយ": st.column_config.NumberColumn(width="small"),
#             }
#         )
    
#     # Display totals in metrics
#     st.markdown("#### សង្ខេបសរុប")
#     total_duties = styled_df['ចំនួនកាតព្វកិច្ច_numeric'].sum()
#     total_final = styled_df['សរុបចុងក្រោយ'].sum()
#     total_active = styled_df['ប្រើប្រាស់'].sum()
#     total_inactive = styled_df['មិនប្រើ'].sum()
    
#     col1, col2, col3, col4 = st.columns(4)
#     with col1:
#         st.metric(label="សរុបអ្នកប្រើប្រាស់", value=f"{total_final:,}")
#     with col2:
#         usage_rate = (total_active / total_final * 100) if total_final > 0 else 0
#         st.metric(label="អត្រាប្រើប្រាស់", value=f"{usage_rate:.1f}%")
#     with col3:
#         st.metric(label="គណនីមិនប្រើប្រាស់", value=f"{total_inactive:,}")
#     with col4:
#         avg_per_duty = total_final / total_duties if total_duties > 0 else 0
#         st.metric(label="អ្នកប្រើជាមធ្យមក្នុងកាតព្វកិច្ច", value=f"{avg_per_duty:.1f}")
    
#     # ======================
#     # LOAD EXCEL DATA
#     # ======================
#     st.markdown("---")
#     st.subheader("ទិន្នន័យលម្អិតពីឯកសារ Excel")
    
#     try:
#         df = pd.read_excel("Excel files/User Management.xlsx")
        
#         # Data preprocessing
#         df['Organization_Name'] = df[['PV_Description','PT_Description','DEF_Description','EPA_Description', 
#                                     'GD_Description','BE_Description', 'GS_Description', 'ABE_Description',
#                                     'DS_Description']].bfill(axis=1).iloc[:, 0]
        
#         # Calculate department counts
#         department_data = {
#             'Department': ['LM-GS', 'LM-ABE', 'GD', 'PT', 'DEF', 'PV', 'DS', 'EPA', 'LM-BE','TOP'],
#             'Users': [38, 106, 9, 25, 25, 25, 44, 9, 19, 1]
#         }
#         df_dept = pd.DataFrame(department_data)
        
#         # Display metrics from Excel
#         col1, col2, col3 = st.columns(3)
#         with col1:
#             total_users = len(df)
#             st.metric(label="អ្នកប្រើប្រាស់សរុប (Excel)", value=f"{total_users:,}")
#         with col2:
#             active_users = len(df[df['Status'] == 'Active']) if 'Status' in df.columns else 0
#             st.metric(label="អ្នកប្រើប្រាស់សកម្ម", value=f"{active_users:,}")
#         with col3:
#             departments = len(df_dept)
#             st.metric(label="ចំនួនអង្គភាព", value=f"{departments}")
        
#         # User distribution visualization
#         st.markdown("#### ការចែកចាយអ្នកប្រើប្រាស់")
        
#         tab1, tab2, tab3 = st.tabs(["អង្គភាព", "ស្ថានភាព", "ទិន្នន័យប្រជាសាស្រ្ត"])
        
#         with tab1:
#             # Department treemap
#             fig = px.treemap(
#                 df_dept,
#                 path=['Department'],
#                 values='Users',
#                 color='Users',
#                 color_continuous_scale='Blues',
#                 title="ការចែកចាយតាមអង្គភាព"
#             )
#             st.plotly_chart(fig, use_container_width=True)
        
#         with tab2:
#             if 'Status' in df.columns:
#                 status_counts = df['Status'].value_counts().reset_index()
#                 status_counts.columns = ['Status', 'Count']
                
#                 fig = px.pie(
#                     status_counts,
#                     values='Count',
#                     names='Status',
#                     title="ស្ថានភាពអ្នកប្រើប្រាស់",
#                     color_discrete_sequence=['#3498db', '#e74c3c', '#2ecc71']
#                 )
#                 st.plotly_chart(fig, use_container_width=True)
        
#         with tab3:
#             # Display basic user info table
#             if 'NAME_KH' in df.columns and 'USERIDALIAS' in df.columns:
#                 st.dataframe(
#                     df[['NAME_KH', 'USERIDALIAS', 'Status', 'Organization_Name']].head(20),
#                     use_container_width=True,
#                     column_config={
#                         "NAME_KH": "ឈ្មោះ",
#                         "USERIDALIAS": "ឈ្មោះអ្នកប្រើ",
#                         "Status": "ស្ថានភាព",
#                         "Organization_Name": "អង្គភាព"
#                     }
#                 )
        
#         # Export option
#         st.download_button(
#             label="📥 ទាញយកទិន្នន័យ",
#             data=df.to_csv(index=False).encode('utf-8'),
#             file_name="user_data.csv",
#             mime="text/csv"
#         )
        
#     except FileNotFoundError:
#         st.error("❌ ឯកសារ Excel មិនត្រូវបានរកឃើញ។ សូមពិនិត្យថា 'User Management.xlsx' មាននៅក្នុងថត 'Excel files/'")
#         st.info("ទិន្នន័យសង្ខេបខាងលើនៅតែបង្ហាញដដែល។")
#     except Exception as e:
#         st.error(f"❌ កំហុស: {str(e)}")

# if __name__ == "__main__":
#     show()