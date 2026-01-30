#     Geography()
import streamlit as st
import pandas as pd
import pydeck as pdk
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def Geography():
    # Modern CSS with gradient backgrounds and glass morphism
    st.markdown("""
    <style>
        :root {
            --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            --secondary-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            --success-gradient: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            --warning-gradient: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
            --dark-gradient: linear-gradient(135deg, #2c3e50 0%, #3498db 100%);
            --glass-bg: rgba(255, 255, 255, 0.1);
            --glass-border: rgba(255, 255, 255, 0.2);
            --shadow-lg: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
            --shadow-sm: 0 4px 16px 0 rgba(31, 38, 135, 0.2);
        }
        
        .main {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            font-family: 'Inter', 'Segoe UI', sans-serif;
        }
        
        .dashboard-header {
            background: var(--primary-gradient);
            padding: 3rem 2rem;
            border-radius: 20px;
            margin-bottom: 2rem;
            color: white;
            text-align: center;
            box-shadow: var(--shadow-lg);
            position: relative;
            overflow: hidden;
        }
        
        .dashboard-header::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 100" fill="rgba(255,255,255,0.1)"><polygon points="0,0 1000,50 1000,100 0,100"/></svg>');
            background-size: cover;
        }
        
        .dashboard-title {
            font-size: 3rem;
            font-weight: 800;
            margin-bottom: 0.5rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        .dashboard-subtitle {
            font-size: 1.2rem;
            opacity: 0.9;
            font-weight: 300;
        }
        
        .glass-card {
            background: var(--glass-bg);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid var(--glass-border);
            border-radius: 20px;
            padding: 1.5rem;
            box-shadow: var(--shadow-sm);
            transition: all 0.3s ease;
        }
        
        .glass-card:hover {
            transform: translateY(-5px);
            box-shadow: var(--shadow-lg);
        }
        
        .metric-card {
            background: white;
            border-radius: 16px;
            padding: 1.5rem;
            box-shadow: 0 4px 20px rgba(0,0,0,0.08);
            border-left: 6px solid;
            transition: all 0.3s ease;
            height: 100%;
            position: relative;
            overflow: hidden;
        }
        
        .metric-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
          
        }
        
        .metric-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 30px rgba(0,0,0,0.12);
        }
        
        .metric-icon {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            opacity: 0.8;
        }
        
        .metric-value {
            font-size: 2.2rem;
            font-weight: 800;
            margin: 0.5rem 0;
            background: var(--primary-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        .metric-title {
            font-size: 0.9rem;
            color: #64748b;
            text-transform: uppercase;
            letter-spacing: 1px;
            font-weight: 600;
        }
        
        .section-header {
            font-size: 1.8rem;
            font-weight: 700;
            margin: 2rem 0 1rem 0;
            background: var(--dark-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            padding-bottom: 0.5rem;
            border-bottom: 3px solid;
            border-image: var(--primary-gradient) 1;
        }
        
        .subsection-header {
            font-size: 1.3rem;
            font-weight: 600;
            margin: 1.5rem 0 1rem 0;
            color: #2c3e50;
            padding-left: 0.5rem;
            border-left: 4px solid #667eea;
        }
        
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
            background: transparent;
        }
        
        .stTabs [data-baseweb="tab"] {
            background: white;
            border-radius: 12px 12px 0 0;
            padding: 12px 24px;
            margin: 0 4px;
            border: none;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        
        .stTabs [aria-selected="true"] {
    
        
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        }
        
        .stTabs [aria-selected="false"]:hover {
            background: #f8fafc !important;
            transform: translateY(-2px);
        }
        
        .map-container {
            border-radius: 20px;
            overflow: hidden;
            box-shadow: var(--shadow-lg);
            border: none;
            margin: 1rem 0;
        }
        
        .data-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
            margin: 1.5rem 0;
        }
        
        .stat-badge {
            background: var(--success-gradient);
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 25px;
            font-size: 0.8rem;
            font-weight: 600;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        /* Custom scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
        }
        
        ::-webkit-scrollbar-track {
           
            border-radius: 10px;
        }
        
        ::-webkit-scrollbar-thumb {
            
            border-radius: 10px;
        }
        
        /* Animation for cards */
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .glass-card, .metric-card {
            animation: fadeInUp 0.6s ease-out;
        }
        
        /* Responsive design */
        @media (max-width: 768px) {
            .dashboard-title {
                font-size: 2rem;
            }
            
            .metric-value {
                font-size: 1.8rem;
            }
            
            .data-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
    """, unsafe_allow_html=True)

    # 🔹 Remove Streamlit default top padding
    st.markdown("""
        <style>
            .block-container {
                padding-top: 1rem;
                padding-bottom: 3rem;
            }
        </style>
    """, unsafe_allow_html=True)

    # Modern Header with Gradient
    st.markdown("""
    <div style="margin-bottom: 2rem;">
        <h1 class="dashboard-title">🌍 ភូមិសាស្ត្រ</h1>
       <p style="font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
          color: #7f8c8d;
          font-size: 1rem;
          margin-bottom: 2rem;">
    Comprehensive geographic information system for the Kingdom of Cambodia
</p>
    </div>
    """, unsafe_allow_html=True) 

    # Load data with caching
    def load_data():
        file_path = "Excel files/Geographyfordatareader.parquet"
        df = pd.read_parquet(file_path).astype(str).fillna("")
        # df['EFFDT'] = pd.to_datetime(df['EFFDT'], errors='coerce')
        df['Effective_date'] = df['EFFDT_Year'].astype(str) + '-2025'
        df['EFF_STATUS'] = df['EFF_STATUS'].map({'A': 'Active', 'I': 'Inactive'})
        df[['Start_Year', 'End_Year']] = df['Effective_date'].str.split('-', expand=True)
        df['Start_Year'] = df['Start_Year'].astype(int)
        df['End_Year'] = df['End_Year'].astype(int)
        
        # Clean and standardize province names
        df['Province_Khmer'] = df['Province_Khmer'].str.strip()
        df['Province_English'] = df['Province_English'].str.strip().str.title()
 
        
        return df

    df = load_data()

    # Create modern tabs
    tab1, tab2 = st.tabs(["Dashboard", "Data Explorer"])

    with tab1:
        # Overview Metrics with Icons
        st.markdown('<div class="section-header">Executive Overview</div>', unsafe_allow_html=True)
        
        # Filter for current data
        current_data = df[(df['Start_Year'] <= 2025) & (df['End_Year'] >= 2025) & (df['EFF_STATUS'] == 'Active')]
        
        
        # # Create 5 columns
        # col1, col2, col3, col4, col5 = st.columns(5)

        # # Prepare the metrics data
        # metrics_data = [
        #     {"title": "Total Records", "value": len(current_data), "color": "#667eea"},
        #     {"title": "Provinces", "value": current_data['Province_English'].nunique(), "color": "#667eea"},
        #     {"title": "Districts", "value": len(current_data[current_data['group'] == 'District']),"color": "#667eea"},
        #     {"title": "Communes", "value": len(current_data[current_data['group'] == 'Communes']), "color": "#667eea"},
        #     {"title": "Schools", "value": len(current_data[current_data['group'] == 'School']), "color": "#667eea"}
        # ]

        # # Render the metrics in styled cards
        # for i, metric in enumerate(metrics_data):
        #     with [col1, col2, col3, col4, col5][i]:
        #         st.markdown(f"""
        #         <div class="metric-card" style="padding: 1rem; border-radius: 0.5rem; background-color: #f9fafb; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
        #             <h3 style="margin: 0; color: #6b7280; font-size: 0.9rem;">{metric['title']}</h3>
        #             <p style="margin: 0; color: {metric['color']}; font-size: 1.8rem; font-weight: 700;">{metric['value']:,}</p>
        #         </div>
        #         """, unsafe_allow_html=True)
        # col1, col2, col3, col4 = st.columns(4)

        # # Prepare the metrics data
        # metrics_data = [
        #     {"title": "Total Records", "value": len(current_data), "color": "#667eea"},
        #     {"title": "Provinces", "value": current_data['Province_English'].nunique(), "color": "#667eea"},
        #     {"title": "Districts", "value": len(current_data[current_data['group'] == 'District']), "color": "#667eea"},
        #     {"title": "Communes", "value": len(current_data[current_data['group'] == 'Communes']), "color": "#667eea"},
        #     {"title": "Schools", "value": len(current_data[current_data['group'] == 'School']), "color": "#667eea"}
        # ]

        # # Create a special metric card for District and School together
        # with col3:
        #     st.markdown(f"""
        #     <div class="metric-card" style="padding: 1rem; border-radius: 0.5rem; background-color: #f9fafb; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
        #         <h3 style="margin: 0; color: #6b7280; font-size: 0.9rem;">Districts & Schools</h3>
        #         <div style="display: flex; justify-content: space-between; margin-top: 0.5rem;">
        #             <div style="text-align: center;">
        #                 <p style="margin: 0; color: #667eea; font-size: 1.4rem; font-weight: 700;">{len(current_data[current_data['group'] == 'District']):,}</p>
        #                 <p style="margin: 0; color: #6b7280; font-size: 0.8rem;">Districts</p>
        #             </div>
        #             <div style="text-align: center;">
        #                 <p style="margin: 0; color: #667eea; font-size: 1.4rem; font-weight: 700;">{len(current_data[current_data['group'] == 'School']):,}</p>
        #                 <p style="margin: 0; color: #6b7280; font-size: 0.8rem;">Schools</p>
        #             </div>
        #         </div>
        #     </div>
        #     """, unsafe_allow_html=True)

        # # Render the other metrics in their respective columns
        # other_metrics = [
        #     {"title": "Total Records", "value": len(current_data), "color": "#667eea"},
        #     {"title": "Provinces", "value": current_data['Province_English'].nunique(), "color": "#667eea"},
        #     {"title": "Communes", "value": len(current_data[current_data['group'] == 'Communes']), "color": "#667eea"}
        # ]

        # # Place the other metrics in columns 1, 2, and 4, 5 (skipping column 3 which has the combined metric)
        # with col1:
        #     st.markdown(f"""
        #     <div class="metric-card" style="padding: 1rem; border-radius: 0.5rem; background-color: #f9fafb; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
        #         <h3 style="margin: 0; color: #6b7280; font-size: 0.9rem;">Total Records</h3>
        #         <p style="margin: 0; color: #667eea; font-size: 1.8rem; font-weight: 700;">{len(current_data):,}</p>
        #     </div>
        #     """, unsafe_allow_html=True)

        # with col2:
        #     st.markdown(f"""
        #     <div class="metric-card" style="padding: 1rem; border-radius: 0.5rem; background-color: #f9fafb; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
        #         <h3 style="margin: 0; color: #6b7280; font-size: 0.9rem;">Provinces</h3>
        #         <p style="margin: 0; color: #667eea; font-size: 1.8rem; font-weight: 700;">{current_data['Province_English'].nunique():,}</p>
        #     </div>
        #     """, unsafe_allow_html=True)

        # with col4:
        #     st.markdown(f"""
        #     <div class="metric-card" style="padding: 1rem; border-radius: 0.5rem; background-color: #f9fafb; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
        #         <h3 style="margin: 0; color: #6b7280; font-size: 0.9rem;">Communes</h3>
        #         <p style="margin: 0; color: #667eea; font-size: 1.8rem; font-weight: 700;">{len(current_data[current_data['group'] == 'Communes']):,}</p>
        #     </div>
        #     """, unsafe_allow_html=True)

        # Column 4 remains empty or you can add another metric if needed
        # col1, col2, col3, col4 = st.columns(4)

        # # Calculate values
        # total_records = len(current_data)
        # provinces = current_data['Province_English'].nunique()
        # districts = len(current_data[current_data['group'] == 'District'])
        # schools = len(current_data[current_data['group'] == 'School'])
        # communes = len(current_data[current_data['group'] == 'Communes'])

        # # Render metrics
        # with col1:
        #     st.markdown("""
        #     <div style="text-align: center; padding: 1.5rem 1rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 0.5rem; color: white;">
        #         <h3 style="margin: 0; font-size: 0.9rem; font-weight: 500;">Total Records</h3>
        #         <p style="margin: 0.5rem 0 0 0; font-size: 2rem; font-weight: 700;">{:,}</p>
        #     </div>
        #     """.format(total_records), unsafe_allow_html=True)

        # with col2:
        #     st.markdown("""
        #     <div style="text-align: center; padding: 1.5rem 1rem; background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%); border-radius: 0.5rem; color: white;">
        #         <h3 style="margin: 0; font-size: 0.9rem; font-weight: 500;">Provinces</h3>
        #         <p style="margin: 0.5rem 0 0 0; font-size: 2rem; font-weight: 700;">{:,}</p>
        #     </div>
        #     """.format(provinces), unsafe_allow_html=True)

        # with col3:
        #     st.markdown(f"""
        #     <div style="text-align: center; padding: 1.4rem 1rem; background: linear-gradient(135deg, #059669 0%, #10b981 100%); border-radius: 0.5rem; color: white;">
        #         <h3 style="margin: 0; font-size: 0.9rem; font-weight: 500;">Districts & Schools</h3>
        #         <div style="display: flex; justify-content: space-around; margin-top: 0.5rem;">
        #             <div>
        #                 <p style="margin: 0; font-size: 1.5rem; font-weight: 700;">{districts:,}</p>
        #                 <p style="margin: 0; font-size: 0.7rem; opacity: 0.9;">Districts</p>
        #             </div>
        #             <div>
        #                 <p style="margin: 0; font-size: 1.5rem; font-weight: 700;">{schools:,}</p>
        #                 <p style="margin: 0; font-size: 0.7rem; opacity: 0.9;">Schools</p>
        #             </div>
        #         </div>
        #     </div>
        #     """, unsafe_allow_html=True)

        # with col4:
        #     st.markdown("""
        #     <div style="text-align: center; padding: 1.5rem 1rem; background: linear-gradient(135deg, #dc2626 0%, #f97316 100%); border-radius: 0.5rem; color: white;">
        #         <h3 style="margin: 0; font-size: 0.9rem; font-weight: 500;">Communes</h3>
        #         <p style="margin: 0.5rem 0 0 0; font-size: 2rem; font-weight: 700;">{:,}</p>
        #     </div>
        #     """.format(communes), unsafe_allow_html=True)


        col1, col2, col3, col4 = st.columns(4)

        # Calculate values
        
        provinces = len(current_data['Province_Khmer'].unique())
        #provinces = len(current_data[current_data['group'] == 'Province'])
        districts = current_data[current_data['Len'] == "4"]['DESCRLONG_KHM'].nunique()
        schools = current_data[current_data['Len'] == "7"]['DESCRLONG_KHM'].nunique()
        communes = current_data[current_data['Len'] == "6"]['DESCRLONG_KHM'].nunique()
        departments = current_data[current_data['Len'] == "5"]['DESCRLONG_KHM'].nunique()
        total_records = provinces + districts + schools + communes + departments
        # Render metrics
        with col1:
            st.markdown("""
            <div style="text-align: center; padding: 1.5rem 1rem; background: white; border-radius: 10px; 
                        border: 1px solid #e5e7eb; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
                <h3 style="margin: 0; font-family: 'Inter', sans-serif;font-size: 0.9rem; font-weight: 600; color: #6b7280;">Total Records</h3>
                <p style="margin: 0.5rem 0 0 0; font-size: 2rem; font-weight: 700; color: #111827;">{:,}</p>
            </div>
            """.format(total_records), unsafe_allow_html=True)

        with col2:
            # st.markdown("""
            # <div style="text-align: center; padding: 1.5rem 1rem; background: white; border-radius: 10px; 
            #             border: 1px solid #e5e7eb; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
            #     <h3 style="margin: 0;font-family: 'Inter', sans-serif; font-size: 0.9rem; font-weight: 600; color: #6b7280;">Provinces</h3>
            #     <p style="margin: 0.5rem 0 0 0; font-size: 2rem; font-weight: 700; color: #111827;">{:,}</p>
            # </div>
            # """.format(provinces), unsafe_allow_html=True)
            st.markdown(f"""
            <div style="text-align: center; padding: 1.4rem 1rem; background: white; border-radius: 10px; 
                        border: 1px solid #e5e7eb; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
                <h3 style="margin: 0;font-family: 'Inter', sans-serif; font-size: 0.9rem; font-weight: 600; color: #6b7280;">Prov. & Health Dept.</h3>
                <div style="display: flex; justify-content: space-around; margin-top: 0.5rem;">
                    <div>
                        <p style="margin: 0; font-size: 1.5rem; font-weight: 700; color: #111827;">{provinces:,}</p>
                        <p style="margin: 0; font-size: 0.7rem; color: #9ca3af;">Provinces</p>
                    </div>
                    <div>
                        <p style="margin: 0; font-size: 1.5rem; font-weight: 700; color: #111827;">{departments:,}</p>
                        <p style="margin: 0; font-size: 0.7rem; color: #9ca3af;">Health Dept.</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
            <div style="text-align: center; padding: 1.4rem 1rem; background: white; border-radius: 10px; 
                        border: 1px solid #e5e7eb; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
                <h3 style="margin: 0;font-family: 'Inter', sans-serif; font-size: 0.9rem; font-weight: 600; color: #6b7280;">Districts & Schools</h3>
                <div style="display: flex; justify-content: space-around; margin-top: 0.5rem;">
                    <div>
                        <p style="margin: 0; font-size: 1.5rem; font-weight: 700; color: #111827;">{districts:,}</p>
                        <p style="margin: 0; font-size: 0.7rem; color: #9ca3af;">Districts</p>
                    </div>
                    <div>
                        <p style="margin: 0; font-size: 1.5rem; font-weight: 700; color: #111827;">{schools:,}</p>
                        <p style="margin: 0; font-size: 0.7rem; color: #9ca3af;">Schools</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with col4:
            st.markdown("""
            <div style="text-align: center; padding: 1.5rem 1rem; background: white; border-radius: 10px; 
                        border: 1px solid #e5e7eb; box-shadow: 0 1px 3px rgba(0,0,0,0.05);  ">
                <h3 style="margin: 0;font-family: 'Inter', sans-serif; font-size: 0.9rem; font-weight: 600; color: #6b7280;">Communes</h3>
                <p style="margin: 0.5rem 0 0 0; font-size: 2rem; font-weight: 700; color: #111827;">{:,}</p>
            </div>
            """.format(communes), unsafe_allow_html=True)


       
            


        # Charts Section
        st.markdown('<div class="section-header"></div>', unsafe_allow_html=True)
        
        # First Row: Distribution Charts
        st.markdown('<div class="subsection-header">Data Distribution</div>', unsafe_allow_html=True)
        col1, col2 = st.columns([2, 1])
        


        with col1:
            # Calculate values
            provinces = current_data['Province_Khmer'].nunique()
            districts = current_data[current_data['Len'] == "4"]['DESCRLONG_KHM'].nunique()
            schools = current_data[current_data['Len'] == "7"]['DESCRLONG_KHM'].nunique()
            communes = current_data[current_data['Len'] == "6"]['DESCRLONG_KHM'].nunique()
            departments = current_data[current_data['Len'] == "5"]['DESCRLONG_KHM'].nunique()

            # Create dataframe for pie chart
            group_data = pd.DataFrame({
                'Category': ['Provinces', 'Districts', 'Schools', 'Communes', 'Departments'],
                'Count': [provinces, districts, schools, communes, departments]
            })

            # Remove zero values (optional but recommended)
            group_data = group_data[group_data['Count'] > 0]

            # Create pie chart
            fig_pie = px.pie(
                group_data,
                values='Count',
                names='Category',
                hole=0.5,
                color_discrete_sequence=px.colors.sequential.Blues_r,
                template='plotly_white'
            )

            fig_pie.update_layout(
                height=400,
                showlegend=True,
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(size=12, family='Arial'),
                margin=dict(t=40, b=20, l=20, r=20),
                title=dict(
                    text='Data Distribution by Category',
                    x=0.5,
                    font=dict(size=16, color='#2c3e50')
                )
            )

            fig_pie.update_traces(
                textposition='inside',
                textinfo='percent+label',
                marker=dict(line=dict(color='white', width=2)),
                hovertemplate='<b>%{label}</b><br>Count: %{value}<br>Percentage: %{percent}'
            )

            st.plotly_chart(fig_pie, use_container_width=True)

        # with col1:
        #     # Enhanced pie chart with more details
        #     group_data = current_data['group'].value_counts().reset_index()
        #     group_data.columns = ['Category', 'Count']
        #     group_data = group_data[group_data['Category'] != 3]
            
        #     fig_pie = px.pie(
        #         group_data, 
        #         values='Count', 
        #         names='Category',
        #         hole=0.5,
        #         color_discrete_sequence=px.colors.sequential.Blues_r,
        #         template='plotly_white'
        #     )
            
        #     fig_pie.update_layout(
        #         height=400,
        #         showlegend=True,
        #         plot_bgcolor='rgba(0,0,0,0)',
        #         paper_bgcolor='rgba(0,0,0,0)',
        #         font=dict(size=12, family='Arial'),
        #         margin=dict(t=40, b=20, l=20, r=20),
        #         title=dict(
        #             text='Data Distribution by Category',
        #             x=0.5,
        #             font=dict(size=16, color='#2c3e50')
        #         )
        #     )
            
        #     fig_pie.update_traces(
        #         textposition='inside',
        #         textinfo='percent+label',
        #         marker=dict(line=dict(color='white', width=2)),
        #         hovertemplate='<b>%{label}</b><br>Count: %{value}<br>Percentage: %{percent}'
        #     )
            
        #     st.plotly_chart(fig_pie, use_container_width=True)

        with col2:
            # Province-wise distribution (Top 10)
            province_data = current_data['Province_English'].value_counts().head(10).reset_index()
            province_data.columns = ['Province', 'Count']
            
            fig_bar = px.bar(
                province_data,
                x='Count',
                y='Province',
                orientation='h',
                title='Top 10 Provinces by Record Count',
                color='Count',
                color_continuous_scale='Blues'
            )
            
            fig_bar.update_layout(
                height=350,
                xaxis_title='Number of Records',
                yaxis_title='Province',
                template='plotly_white',
                showlegend=False,
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)'
            )
            
            fig_bar.update_traces(
                marker=dict(line=dict(width=0))
            )
            
            st.plotly_chart(fig_bar, use_container_width=True)

                # Interactive Map Visualization
        st.markdown("---")
        st.markdown("""
        <div style="margin-bottom: 1.25rem;">
            <h2 class="section-header">Cambodia Province Map</h2>
        </div>
        """, unsafe_allow_html=True)
        
        # Prepare map data
        province_df = df.copy()
        province_df['Latitude'] = pd.to_numeric(province_df['Latitude'], errors='coerce')
        province_df['Longitude'] = pd.to_numeric(province_df['Longitude'], errors='coerce')
        province_df = province_df.dropna(subset=['Latitude', 'Longitude'])
        
        if not province_df.empty:
            # Calculate metrics for the map
            province_counts = province_df['Province_English'].value_counts().reset_index()
            province_counts.columns = ['Province_English', 'count']
            province_df = province_df.merge(province_counts, on='Province_English', how='left')
            province_df['size'] = province_df['count'] * 20
            
            # Create map layers
            layer = pdk.Layer(
                "ScatterplotLayer",
                province_df,
                pickable=True,
                opacity=0.8,
                stroked=True,
                filled=True,
                radius_scale=1,
                radius_min_pixels=8,
                radius_max_pixels=100,
                line_width_min_pixels=1,
                get_position=["Longitude", "Latitude"],
                get_radius="size",
                get_fill_color=[26, 115, 232, 200],
                get_line_color=[0, 0, 0, 180],
            )

            view_state = pdk.ViewState(
                latitude=12.5657,
                longitude=104.9910,
                zoom=6.2,
                pitch=0,
            )

            # Render the map
            with st.container():
                st.pydeck_chart(
                    pdk.Deck(
                        layers=[layer],
                        initial_view_state=view_state,
                        tooltip={
                            "html": """
                            <div class="map-tooltip" style="padding: 10px; background: white; border-radius: 6px; max-width: 280px;">
                                <h3 style="margin: 0 0 6px 0; color: #2c3e50; border-bottom: 1px solid #eee; padding-bottom: 6px; font-size: 1rem;">{Province_English}</h3>
                                <p style="margin: 4px 0; font-size: 0.85rem;"><b>Records:</b> <span style="color: #e91e63; font-weight: 600;">{count}</span></p>
                                <p style="margin: 4px 0; font-size: 0.85rem;"><b>Status:</b> <span style="color: {color}; font-weight: 500;">{EFF_STATUS}</span></p>
                                
                            </div>
                            """.replace("{color}", "'#27ae60'"),
                            "style": {
                                "fontFamily": "'Inter', Arial, sans-serif",
                                "boxShadow": "0 4px 12px rgba(0,0,0,0.1)"
                            },
                        },
                        map_style="light",
                    ),
                    use_container_width=True
                )
        else:
            st.warning("No geographic data available for the selected criteria.")            

    with tab2:

        # Create layout columns
        # col1, col2, col3, col4 = st.columns([30, 5, 5, 2])
        col1, col2, col3, col4 = st.columns([20, 5, 5, 5])
        

        # Text search
        with col1:
            text_search = st.text_input("និយមន័យពី ទិន្នន័យមេ ​​ស្វែងយល់បន្ថែម", value="")

        # Year selection
        # with col2:
        #     options = ("2000", "2023", "2024", "2025")
        #     option = st.selectbox("ឆ្នាំ", options, index=options.index("2025"))
        with col2:
            year_type_options = ("ឆ្នាំបង្កើត​​", "ឆ្នាំប្រសិទ្ធភាព")
            selected_year_type = st.selectbox("ប្រភេទឆ្នាំ", year_type_options, index=1)

        # Status selection
        # with col3:
        #     status_options = ("Active", "Inactive")
        #     selected_status = st.selectbox("ស្ថានភាព", status_options, index=0)
        with col3:
            year_options = sorted(df['EFFDT_Year'].astype(str).unique())
            options = ["All"] + year_options  

            option = st.selectbox(
                "ឆ្នាំ",
                options,
                index= 0,  # Default to 2025 if available
                placeholder="Select year...",
            )


        with col4:
            status_options = ("Active", "Inactive")
            selected_status = st.selectbox("ស្ថានភាព", status_options, index=0)  # Default to 'Active'



       

        if option != "All":
            selected_year = int(option)
            filtered_df = df[df['EFFDT_Year'].astype(int) == selected_year]
        else:
            filtered_df = df.copy()

        # Filter by status
        filtered_df = filtered_df[filtered_df['EFF_STATUS'] == selected_status]


        # Use the already loaded df from cache
        # Filter by year and status
        
        # selected_year = int(option)

        # filtered_df = df[(df['Start_Year'] <= selected_year) & (df['End_Year'] >= selected_year)]
        # filtered_df = filtered_df[filtered_df['EFF_STATUS'] == selected_status]
        
        if text_search:
            pattern = f"^{text_search}"

            if filtered_df["PRODUCT"].str.match(pattern, case=False, na=False).any():
                filtered_df = filtered_df[filtered_df["PRODUCT"].str.match(pattern, case=False, na=False)]
            elif filtered_df["DESCRLONG_KHM"].str.contains(text_search, case=False, na=False).any():
                filtered_df = filtered_df[filtered_df["DESCRLONG_KHM"].str.contains(text_search, case=False, na=False)]
            elif filtered_df["Province_English"].str.contains(text_search, case=False, na=False).any():
                filtered_df = filtered_df[filtered_df["Province_English"].str.contains(text_search, case=False, na=False)]
        # Filter by search text
        # if text_search:
        #     mask1 = filtered_df["DESCRLONG_KHM"].str.contains(text_search, case=False, na=False)
        #     mask2 = filtered_df["PRODUCT"].str.contains(text_search, case=False, na=False)
        #     mask3 = filtered_df["Province_English"].str.contains(text_search, case=False, na=False)
        #     filtered_df = filtered_df[mask1 | mask2 | mask3]

        # Display filtered results
        st.subheader("លទ្ធផល")
        if not filtered_df.empty:
            # Limit to first 12 records for better display
            filtered_df = filtered_df.head(12)

            num_cards = len(filtered_df)
            cards_per_col = (num_cards + 2) // 3

            col1_df = filtered_df.iloc[:cards_per_col]
            col2_df = filtered_df.iloc[cards_per_col:2*cards_per_col]
            col3_df = filtered_df.iloc[2*cards_per_col:]

            cols = st.columns(3)

            for i, col_df in enumerate([col1_df, col2_df, col3_df]):
                with cols[i]:
                    for _, row in col_df.iterrows():
                        # Get province information - adjust column name as needed
                        province_column = 'Province_English' if 'Province_English' in row else 'នៅក្រោមខេត្ត'
                        province = str(row[province_column]).strip() if pd.notna(row[province_column]) and str(row[province_column]).strip() != '' else None
                        
                        province_text = (
                            f"<p style='font-size: 16px;'><b style='color:#28a745;'>🏛 ស្ថិតនៅក្រោមខេត្ត:</b> {province}</p>"
                            if province else ""
                        )

                        # Dynamic year display
                        if selected_year_type == "ឆ្នាំបង្កើត​​":
                            year_display = f"{row['EFFDT_Year']}"
                            year_label = "📅 ឆ្នាំបង្កើត"
                        else:  # ឆ្នាំប្រសិទ្ធភាព
                            year_display = f"{row['EFFDT_Year']}-បច្ចុប្បន្ន"
                            year_label = "📅 កាលបរិច្ឆេទមានប្រសិទ្ធភាព"

                        card_html = f"""
                        <div style="border: 1px solid #ddd; border-radius: 10px; padding: 20px; margin-bottom: 20px; background-color: #f9f9f9; height: 280px; overflow-y: auto; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
                            <h4 style="color: #1f2937; font-size: 22px; height: 50px; overflow: hidden; text-overflow: ellipsis;">{row['PRODUCT']}</h4>
                            <p style="font-size: 18px;"><b style='color:#694a56;'>{year_label}</b> <span style="color: #FF6347;">{year_display}</span></p>
                            <p style="font-size: 18px;"><b style='color:#694a56;'>📖 បរិយាយ:</b> <span style="color: #858585;">{row['DESCRLONG_KHM']}</span></p>
                            <p style="font-size: 18px;"><b style='color:#694a56;'>ស្ថានភាព:</b> <span style="color:#694a56;">{row['EFF_STATUS']}</span></p>
                            {province_text}
                        </div>
                        """

                        st.markdown(card_html, unsafe_allow_html=True)
            
            # Download button
            if len(filtered_df) > 0:
                csv = filtered_df.to_csv(index=False)
                st.download_button(
                    label="📥 Download",
                    data=csv,
                    file_name=f"cambodia_geographic_data_{datetime.now().strftime('%Y%m%d')}.csv",
                    mime="text/csv",
                )
        else:
            st.info("គ្មានទិន្នន័យសម្រាប់ឆ្នាំនិងលក្ខណៈវិនិច្ឆ័យស្វែងរកដែលបានជ្រើសរើស។")

if __name__ == "__main__":
    Geography()



