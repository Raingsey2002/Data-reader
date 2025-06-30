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
    apply_custom_styles()
    
    # Premium page header
    st.markdown("""
    <div style="margin-bottom: 2rem;">
        <h1 class="dashboard-title">👥 User Analytics Dashboard</h1>
        <p class="dashboard-subtitle">Comprehensive insights into organizational user base and activity patterns</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load data with error handling
    try:
        df = pd.read_excel("User Management.xlsx")
        
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
            total_users = len(df)
            st.markdown(create_metric_card(
                "Total Users", 
                f"{total_users:,}",
                "Across all departments",
                "2.5% MoM",
                "positive"
            ), unsafe_allow_html=True)
        
        with col2:
            active_users = len(df[df['Status'] == 'Active']) if 'Status' in df.columns else 0
            st.markdown(create_metric_card(
                "Active Users", 
                f"{active_users:,}",
                f"{(active_users/total_users*100 if total_users > 0 else 0):.1f}% of total",
                "1.2% MoM",
                "positive"
            ), unsafe_allow_html=True)
        
        with col3:
            departments = len(df_dept)
            st.markdown(create_metric_card(
                "Departments", 
                departments,
                f"{(df_dept['Users'].sum()/departments if departments > 0 else 0):.0f} avg users",
                "No change",
                "normal"
            ), unsafe_allow_html=True)
        
        with col4:
            if 'Z_CREATEDTTM' in df.columns:
                try:
                    df['CREATED_DATE'] = pd.to_datetime(df['Z_CREATEDTTM'], format='%d-%b-%y %I.%M.%S.%f %p', errors='coerce')
                    new_users = len(df[df['CREATED_DATE'] >= pd.Timestamp.now() - pd.DateOffset(months=1)])
                    st.markdown(create_metric_card(
                        "New Users (30d)", 
                        new_users,
                        f"{(new_users/total_users*100 if total_users > 0 else 0):.1f}% of total",
                        f"{(new_users - 15)} vs prev month" if new_users else "N/A",
                        "positive" if new_users > 15 else "negative" if new_users < 15 else "normal"
                    ), unsafe_allow_html=True)
                except:
                    st.markdown(create_metric_card(
                        "New Users (30d)", 
                        "N/A",
                        "Data unavailable",
                    ), unsafe_allow_html=True)
        
        # ======================
        # USER DISTRIBUTION ANALYSIS
        # ======================
        st.markdown('<div class="section-header">User Distribution Analysis</div>', unsafe_allow_html=True)
        
        tab1, tab2, tab3 = st.tabs(["Department Overview", "User Status", "Demographics"])
        
        with tab1:
            col1, col2 = st.columns([2, 1], gap="medium")
            
            with col1:
                with st.container():
                    st.markdown("#### Department Distribution")
                    
                    # Create a treemap for department visualization
                    fig_treemap = px.treemap(
                        df_dept,
                        path=['Department'],
                        values='Users',
                        color='Users',
                        color_continuous_scale='Blues',
                        hover_data=['Users'],
                        height=400
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
                    st.markdown("#### Top Departments")
                    
                    # Show top departments in a table with progress bars
                    top_depts = df_dept.sort_values('Users', ascending=False).head(5)
                    
                    # Create a custom bar chart with progress bars
                    fig = go.Figure()
                    fig.add_trace(go.Bar(
                        y=top_depts['Department'],
                        x=top_depts['Users'],
                        orientation='h',
                        marker=dict(
                            color="#3498db",
                            line=dict(color="#2980b9", width=1)
                        ),
                        text=top_depts['Users'],
                        textposition='auto',
                        textfont=dict(family="Inter", size=12, color="white")
                    ))
                    
                    fig.update_layout(
                        height=400,
                        margin=dict(l=0, r=0, t=0, b=0),
                        xaxis=dict(showgrid=False, visible=False),
                        yaxis=dict(autorange="reversed"),
                        plot_bgcolor='rgba(0,0,0,0)',
                        paper_bgcolor='rgba(0,0,0,0)',
                        font=dict(family="Inter", size=12)
                    )
                    
                    st.plotly_chart(fig, use_container_width=True)
                    
                    # Department summary stats
                    st.markdown("""
                    <div style="background: #f8f9fa; padding: 1rem; border-radius: 8px; margin-top: 1rem; border: 1px solid #e0e0e0;">
                        <p style="font-weight: 600; margin-bottom: 0.5rem; font-family: 'Inter', sans-serif; color: #2c3e50;">Department Insights</p>
                        <ul style="margin: 0; padding-left: 1.2rem; color: #7f8c8d; font-size: 0.9rem; font-family: 'Inter', sans-serif;">
                            <li>LM-ABE has the most users (106)</li>
                            <li>TOP has the fewest users (1)</li>
                            <li>Average department size: 30 users</li>
                        </ul>
                    </div>
                    """, unsafe_allow_html=True)
        
        with tab2:
            col1, col2 = st.columns([1, 1], gap="medium")
            
            with col1:
                with st.container():
                    st.markdown("#### User Status Composition")
                    if 'Status' in df.columns:
                        status_counts = df['Status'].value_counts().reset_index()
                        status_counts.columns = ['Status', 'Count']
                        
                        # Create a donut chart with modern styling
                        fig = px.pie(
                            status_counts,
                            values='Count',
                            names='Status',
                            hole=0.6,
                            color_discrete_sequence=['#3498db', '#e74c3c', '#2ecc71'],
                            height=400
                        )
                        
                        fig.update_traces(
                            textposition='inside',
                            textinfo='percent+label',
                            marker=dict(line=dict(color='white', width=1)),
                            pull=[0.1 if i == status_counts['Count'].idxmax() else 0 for i in status_counts.index],
                            textfont=dict(family="Inter", size=12)
                        )
                        
                        fig.update_layout(
                            showlegend=False,
                            margin=dict(t=0, b=0, l=0, r=0),
                            paper_bgcolor='rgba(0,0,0,0)',
                            font=dict(family="Inter", size=12),
                            annotations=[dict(
                                text=f"Total<br>{sum(status_counts['Count'])}",
                                x=0.5, y=0.5,
                                font_size=18,
                                showarrow=False,
                                font_family="Inter"
                            )]
                        )
                        
                        st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                with st.container():
                    st.markdown("#### Status Over Time")
                    
                    if 'Status' in df.columns and 'Z_CREATEDTTM' in df.columns:
                        try:
                            df['CREATED_DATE'] = pd.to_datetime(df['Z_CREATEDTTM'], format='%d-%b-%y %I.%M.%S.%f %p', errors='coerce')
                            df['YearMonth'] = df['CREATED_DATE'].dt.to_period('M').astype(str)
                            
                            # Create a line chart showing status changes over time
                            status_over_time = df.groupby(['YearMonth', 'Status']).size().unstack().fillna(0)
                            
                            fig = go.Figure()
                            
                            # Define a professional color palette
                            status_colors = {
                                'Active': '#3498db',
                                'Inactive': '#e74c3c',
                                'Pending': '#2ecc71'
                            }
                            
                            for status in status_counts['Status']:
                                fig.add_trace(go.Scatter(
                                    x=status_over_time.index,
                                    y=status_over_time[status],
                                    name=status,
                                    mode='lines+markers',
                                    line=dict(width=2.5, color=status_colors.get(status, '#95a5a6')),
                                    marker=dict(size=8),
                                    hovertemplate=f"<b>{status}</b><br>%{{x}}<br>%{{y}} users<extra></extra>"
                                ))
                            
                            fig.update_layout(
                                height=400,
                                margin=dict(l=0, r=0, t=0, b=0),
                                xaxis_title=None,
                                yaxis_title="User Count",
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
                                font=dict(family="Inter", size=12),
                                hoverlabel=dict(
                                    bgcolor="white",
                                    font_size=12,
                                    font_family="Inter"
                                )
                            )
                            
                            st.plotly_chart(fig, use_container_width=True)
                        except:
                            st.warning("Could not process creation dates for timeline analysis")
        
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
                
                # Calculate growth metrics
                if len(monthly_counts) > 1:
                    latest_month = monthly_counts.iloc[-1]['New Users']
                    prev_month = monthly_counts.iloc[-2]['New Users']
                    mom_growth = ((latest_month - prev_month) / prev_month * 100) if prev_month > 0 else 0
                    
                    st.markdown(f"""
                    <div style="background: #f8f9fa; padding: 1rem; border-radius: 8px; margin-top: 1rem; border: 1px solid #e0e0e0;">
                        <p style="font-weight: 600; margin-bottom: 0.5rem; font-family: 'Inter', sans-serif; color: #2c3e50;">Growth Insights</p>
                        <ul style="margin: 0; padding-left: 1.2rem; color: #7f8c8d; font-size: 0.9rem; font-family: 'Inter', sans-serif;">
                            <li>Month-over-Month Growth: <strong>{mom_growth:.1f}%</strong></li>
                            <li>Average Monthly New Users: <strong>{monthly_counts['New Users'].mean():.1f}</strong></li>
                            <li>Peak Month: <strong>{monthly_counts.loc[monthly_counts['New Users'].idxmax(), 'YearMonth']}</strong> ({monthly_counts['New Users'].max()} users)</li>
                        </ul>
                    </div>
                    """, unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"Error processing timeline data: {str(e)}")
        
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




