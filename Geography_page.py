#############the real one is below here::::::___>>>>

# import streamlit as st
# import pandas as pd
# import pydeck as pdk
# from datetime import datetime

# def Geography():
#     # Custom CSS for professional styling
#     st.markdown("""
#     <style>
#         :root {
#             --primary-color: #1a73e8;
#             --primary-dark: #0d47a1;
#             --secondary-color: #2c3e50;
#             --accent-color: #e91e63;
#             --success-color: #27ae60;
#             --warning-color: #f39c12;
#             --light-bg: #f8f9fa;
#             --card-shadow: 0 4px 6px rgba(0,0,0,0.08);
#             --transition: all 0.3s ease;
#             --border-radius: 8px;
#         }
        
#         .main {
#             background-color: var(--light-bg);
#             font-family: 'Inter', Arial, sans-serif !important;
#         }
        
#         .stSelectbox, .stTextInput, .stSlider {
#             background-color: white;
#             border-radius: var(--border-radius);
#             box-shadow: var(--card-shadow);
#             border: 1px solid #e0e0e0;
#         }
        
#         .header-card {
#             background: linear-gradient(135deg, var(--primary-dark) 0%, var(--primary-color) 100%);
#             color: white;
#             border-radius: var(--border-radius);
#             padding: 2rem 1.5rem;
#             margin-bottom: 1.5rem;
#             box-shadow: var(--card-shadow);
#             border: none;
#         }
        
#         .metric-card {
#             background: white;
#             border-radius: var(--border-radius);
#             padding: 1.25rem;
#             box-shadow: var(--card-shadow);
#             transition: var(--transition);
#             border-left: 4px solid var(--primary-color);
#             height: 100%;
#             display: flex;
#             flex-direction: column;
#         }
        
#         .metric-card:hover {
#             transform: translateY(-3px);
#             box-shadow: 0 6px 12px rgba(0,0,0,0.1);
#         }
        
#         .metric-title {
#             font-size: 0.85rem;
#             color: #7f8c8d;
#             margin-bottom: 0.5rem;
#             font-weight: 500;
#             text-transform: uppercase;
#             letter-spacing: 0.5px;
#         }
        
#         .metric-value {
#             font-size: 1.75rem;
#             font-weight: 700;
#             color: var(--secondary-color);
#             line-height: 1.2;
#         }
        
#         .metric-description {
#             font-size: 0.8rem;
#             color: #95a5a6;
#             margin-top: auto;
#             padding-top: 0.5rem;
#         }
        
#         .data-card {
#             background: white;
#             border-radius: var(--border-radius);
#             padding: 1.25rem;
#             margin-bottom: 1rem;
#             box-shadow: var(--card-shadow);
#             border-left: 4px solid var(--primary-color);
#             height: 260px;
#             overflow-y: auto;
#             transition: var(--transition);
#         }
        
#         .data-card:hover {
#             box-shadow: 0 6px 12px rgba(0,0,0,0.1);
#         }
        
#         .data-card h4 {
#             color: var(--secondary-color);
#             font-size: 1.1rem;
#             margin-bottom: 0.75rem;
#             border-bottom: 1px solid #eee;
#             padding-bottom: 0.5rem;
#             font-weight: 600;
#         }
        
#         .data-card p {
#             margin-bottom: 0.6rem;
#             font-size: 0.9rem;
#             line-height: 1.4;
#         }
        
#         .map-container {
#             border-radius: var(--border-radius);
#             overflow: hidden;
#             box-shadow: 0 6px 12px rgba(0,0,0,0.1);
#             margin-top: 1.25rem;
#             border: 1px solid #e0e0e0;
#         }
        
#         .tab-content {
#             padding: 1.25rem 0;
#         }
        
#         .stTabs [data-baseweb="tab-list"] {
#             gap: 4px;
#             padding: 0 2px;
#         }
        
#         .stTabs [data-baseweb="tab"] {
#             background: white;
#             border-radius: 6px 6px 0 0 !important;
#             padding: 8px 16px;
#             transition: var(--transition);
#             border: 1px solid #e0e0e0;
#             margin-right: 0 !important;
#             font-weight: 500;
#             font-size: 0.9rem;
#         }
        
#         .stTabs [aria-selected="true"] {
#             background-color: var(--primary-color) !important;
#             color: white !important;
#             border-color: var(--primary-dark) !important;
#         }
        
#         .stTabs [aria-selected="false"]:hover {
#             background-color: #f8f9fa !important;
#         }
        
#         /* Section headers */
#         .section-header {
#             color: var(--secondary-color);
#             border-bottom: 2px solid var(--primary-color);
#             padding-bottom: 0.5rem;
#             margin-bottom: 1.25rem;
#             font-weight: 600;
#             font-size: 1.5rem;
#         }
        
#         .section-subheader {
#             color: #7f8c8d;
#             font-size: 0.95rem;
#             margin-top: -1rem;
#             margin-bottom: 1.25rem;
#         }
        
#         /* Remove Streamlit default top padding */
#         .block-container {
#             padding-top: 1rem;
#             padding-bottom: 2rem;
#         }
        
#         /* Custom scrollbar */
#         ::-webkit-scrollbar {
#             width: 6px;
#         }
        
#         ::-webkit-scrollbar-track {
#             background: #f1f1f1;
#             border-radius: 10px;
#         }
        
#         ::-webkit-scrollbar-thumb {
#             background: #ccc;
#             border-radius: 10px;
#         }
        
#         ::-webkit-scrollbar-thumb:hover {
#             background: #aaa;
#         }
        
#         /* Tooltip styling */
#         .map-tooltip {
#             font-family: 'Inter', Arial, sans-serif !important;
#             border-radius: var(--border-radius) !important;
#             box-shadow: 0 4px 12px rgba(0,0,0,0.15) !important;
#             border: none !important;
#         }
        
#         /* Responsive adjustments */
#         @media (max-width: 768px) {
#             .metric-value {
#                 font-size: 1.5rem;
#             }
            
#             .header-card {
#                 padding: 1.25rem 1rem;
#             }
#         }
#     </style>
#     """, unsafe_allow_html=True)

#     # Professional header
#     # st.markdown("""
#     # <div>
#     #     <h1 style="margin: 0; font-size: 2rem; font-weight: 700;">🌍 Cambodia Geographic Data</h1>
#     #     <p style="margin: 0.5rem 0 0 0; font-size: 1rem; opacity: 0.9;">
#     #         Comprehensive geographic information system for the Kingdom of Cambodia
#     #     </p>
#     # </div>
#     # """, unsafe_allow_html=True)
     
#     st.markdown("""
#     <div style="margin-bottom: 2rem;">
#         <h1 class="dashboard-title">🌍 ភូមិសាស្ត្រ</h1>
#        <p style="font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
#           color: #7f8c8d;
#           font-size: 1rem;
#           margin-bottom: 2rem;">
#     Comprehensive geographic information system for the Kingdom of Cambodia
# </p>
#     </div>
#     """, unsafe_allow_html=True) 



#     # Create tabs for different views
#     tab1, tab2 = st.tabs(["🗺️ Map & Analytics", "📊 Detailed Data"])

#     # Load data with caching
#     @st.cache_data
#     def load_data():
#         file_path = "Geographyfordatareader.xlsx"
#         df = pd.read_excel(file_path, dtype=str).fillna("")
#         df['EFFDT'] = pd.to_datetime(df['EFFDT'], errors='coerce')
#         df['Effective_date'] = df['EFFDT_Year'].astype(str) + '-2025'
#         df['EFF_STATUS'] = df['EFF_STATUS'].map({'A': 'Active', 'I': 'Inactive'})
#         df[['Start_Year', 'End_Year']] = df['Effective_date'].str.split('-', expand=True)
#         df['Start_Year'] = df['Start_Year'].astype(int)
#         df['End_Year'] = df['End_Year'].astype(int)
        
#         # Clean and standardize province names
#         df['Province_Khmer'] = df['Province_Khmer'].str.strip()
#         df['Province_English'] = df['Province_English'].str.strip().str.title()
        
#         return df

#     df = load_data()

#     # Tab 1: Map and Statistics
#     with tab1:
#         # Default filter values
#         selected_year = 2025
#         selected_status = "Active"
        
#         # Filter data based on default selections
#         filtered_df = df[(df['Start_Year'] <= selected_year) & (df['End_Year'] >= selected_year)]
#         filtered_df = filtered_df[filtered_df['EFF_STATUS'] == selected_status]
        
#         # Key Metrics Section
#         if not filtered_df.empty:
#             st.markdown("""
#             <div style="margin: 1.5rem 0 1rem 0;">
#                 <h3 class="section-header">Key Metrics</h3>
#                 <p class="section-subheader">Essential indicators from the geographic dataset</p>
#             </div>
#             """, unsafe_allow_html=True)
            
#             col1, col2, col3,  col4, col5= st.columns(5)
            
#             with col1:
#                 st.markdown(f"""
#                 <div class="metric-card">
#                     <div class="metric-title">Total Records</div>
#                     <div class="metric-value">{len(filtered_df):,}</div>
#                     <div class="metric-description">All geographic entries</div>
#                 </div>
#                 """, unsafe_allow_html=True)
            
#             with col2:
#                 st.markdown(f"""
#                 <div class="metric-card">
#                     <div class="metric-title">Provinces</div>
#                     <div class="metric-value" style="color: var(--accent-color);">
#                         {filtered_df['Province_English'].nunique():,}
#                     </div>
#                     <div class="metric-description">Covered provinces</div>
#                 </div>
#                 """, unsafe_allow_html=True)
            
#             # with col3:
#             #     st.markdown(f"""
#             #     <div class="metric-card">
#             #         <div class="metric-title">Selected Year</div>
#             #         <div class="metric-value" style="color: var(--success-color);">
#             #             {selected_year}
#             #         </div>
#             #         <div class="metric-description">Data validity period</div>
#             #     </div>
#             #     """, unsafe_allow_html=True)
#             with col3:
#                 #🤣 Count districts from group column where group == 'District'
#                 district_count = len(filtered_df[filtered_df['group'] == 'District'])
#                 st.markdown(f"""
#                 <div class="metric-card">
#                     <div class="metric-title">Districts</div>
#                     <div class="metric-value" style="color: var(--success-color);">
#                         {district_count:,}
#                     </div>
#                     <div class="metric-description">District records</div>
#                 </div>
#                 """, unsafe_allow_html=True)
                
#             with col4:

#                 #🤣 Count districts from group column where group == 'District'
#                 Communes_count = len(filtered_df[filtered_df['group'] == 'Communes'])
#                 st.markdown(f"""
#                 <div class="metric-card">
#                     <div class="metric-title">Communes</div>
#                     <div class="metric-value" style="color: var(--success-color);">
#                         {Communes_count:,}
#                     </div>
#                     <div class="metric-description">Communes records</div>
#                 </div>
#                 """, unsafe_allow_html=True)
#             with col5:
#                 #🤣 Count Schools from group column where group == 'school'
#                 Schools_count = len(filtered_df[filtered_df['group'] == 'School'])
#                 st.markdown(f"""
#                 <div class="metric-card">
#                     <div class="metric-title">Communes</div>
#                     <div class="metric-value" style="color: var(--success-color);">
#                         {Schools_count:,}
#                     </div>
#                     <div class="metric-description">Schools records </div>
#                 </div>
#                 """, unsafe_allow_html=True)
#                 # active_percentage = (len(filtered_df) / len(df)) * 100
#                 # st.markdown(f"""
#                 # <div class="metric-card">
#                 #     <div class="metric-title">Active Data</div>
#                 #     <div class="metric-value" style="color: var(--warning-color);">
#                 #         {active_percentage:.1f}%
#                 #     </div>
#                 #     <div class="metric-description">Active records from total</div>
#                 # </div>
#                 # """, unsafe_allow_html=True)
            
#             # Province Distribution Chart
#             st.markdown("---")
#             st.markdown("""
#             <div style="margin-bottom: 1.25rem;">
#                 <h3 class="section-header">Provincial Distribution</h3>
#                 <p class="section-subheader">Data concentration across provinces</p>
#             </div>
#             """, unsafe_allow_html=True)
            
#             top_provinces = filtered_df['Province_English'].value_counts().head(10).reset_index()
#             top_provinces.columns = ['Province', 'Count']
            
#             # Use columns to make the chart responsive
#             col1, col2 = st.columns([3, 1])
            
#             with col1:
#                 st.bar_chart(
#                     top_provinces.set_index('Province'),
#                     height=350,
#                     use_container_width=True,
#                     color='#1a73e8'
#                 )
            
#             with col2:
#                 st.markdown("""
#                 <div style="background: white; border-radius: var(--border-radius); padding: 1rem; box-shadow: var(--card-shadow); height: 100%;">
#                     <h4 style="color: var(--secondary-color); margin-top: 0; font-weight: 600; font-size: 1rem;">Top Provinces</h4>
#                     <ol style="padding-left: 1.2rem; margin-top: 0.75rem;">
#                 """, unsafe_allow_html=True)
                
#                 for i, row in top_provinces.iterrows():
#                     st.markdown(f"""
#                     <li style="margin-bottom: 0.6rem; padding-bottom: 0.4rem; border-bottom: 1px dashed #eee; font-size: 0.9rem;">
#                         <span style="font-weight: 500;">{row['Province']}</span>
#                         <span style="float: right; color: var(--accent-color); font-weight: 600;">{row['Count']:,}</span>
#                     </li>
#                     """, unsafe_allow_html=True)
                
#                 st.markdown("</ol></div>", unsafe_allow_html=True)
            
#             # Interactive Map Visualization
#             st.markdown("---")
#             st.markdown("""
#             <div style="margin-bottom: 1.25rem;">
#                 <h2 class="section-header">Cambodia Province Map</h2>
#                 <p class="section-subheader">Click on markers to view detailed information</p>
#             </div>
#             """, unsafe_allow_html=True)
            
#             # Prepare map data
#             province_df = filtered_df.copy()
#             province_df['Latitude'] = pd.to_numeric(province_df['Latitude'], errors='coerce')
#             province_df['Longitude'] = pd.to_numeric(province_df['Longitude'], errors='coerce')
#             province_df = province_df.dropna(subset=['Latitude', 'Longitude'])
            
#             if not province_df.empty:
#                 # Calculate metrics for the map
#                 province_counts = province_df['Province_English'].value_counts().reset_index()
#                 province_counts.columns = ['Province_English', 'count']
#                 province_df = province_df.merge(province_counts, on='Province_English', how='left')
#                 province_df['size'] = province_df['count'] * 20
                
#                 # Create map layers
#                 layer = pdk.Layer(
#                     "ScatterplotLayer",
#                     province_df,
#                     pickable=True,
#                     opacity=0.8,
#                     stroked=True,
#                     filled=True,
#                     radius_scale=1,
#                     radius_min_pixels=8,
#                     radius_max_pixels=100,
#                     line_width_min_pixels=1,
#                     get_position=["Longitude", "Latitude"],
#                     get_radius="size",
#                     get_fill_color=[26, 115, 232, 200],
#                     get_line_color=[0, 0, 0, 180],
#                 )

#                 view_state = pdk.ViewState(
#                     latitude=12.5657,
#                     longitude=104.9910,
#                     zoom=6.2,
#                     pitch=0,
#                 )

#                 # Render the map
#                 with st.container():
#                     st.pydeck_chart(
#                         pdk.Deck(
#                             layers=[layer],
#                             initial_view_state=view_state,
#                             tooltip={
#                                 "html": """
#                                 <div class="map-tooltip" style="padding: 10px; background: white; border-radius: 6px; max-width: 280px;">
#                                     <h3 style="margin: 0 0 6px 0; color: #2c3e50; border-bottom: 1px solid #eee; padding-bottom: 6px; font-size: 1rem;">{Province_English}</h3>
#                                     <p style="margin: 4px 0; font-size: 0.85rem;"><b>Records:</b> <span style="color: #e91e63; font-weight: 600;">{count}</span></p>
#                                     <p style="margin: 4px 0; font-size: 0.85rem;"><b>Status:</b> <span style="color: {color}; font-weight: 500;">{EFF_STATUS}</span></p>
#                                     <p style="margin: 4px 0 0 0; font-size: 0.8rem; color: #7f8c8d;">Click for more details</p>
#                                 </div>
#                                 """.replace("{color}", "'#27ae60'" if selected_status == "Active" else "'#e74c3c'"),
#                                 "style": {
#                                     "fontFamily": "'Inter', Arial, sans-serif",
#                                     "boxShadow": "0 4px 12px rgba(0,0,0,0.1)"
#                                 },
#                             },
#                             map_style="light",
#                         ),
#                         use_container_width=True
#                     )
#             else:
#                 st.warning("No geographic data available for the selected criteria.")
#         else:
#             st.info("No data available for the selected filters.")

#     # Tab 2: Detailed Data
#     with tab2:
#         st.markdown("""
#         <div style="margin-bottom: 1.5rem;">
#             <h2 class="section-header">Detailed Records</h2>
#             <p class="section-subheader">Comprehensive geographic information for Cambodia</p>
#         </div>
#         """, unsafe_allow_html=True)
        
#         # Filter controls
#         with st.container():
#             col1, col2, col3 = st.columns([2, 1, 1])
            
#             with col1:
#                 tab2_text_search = st.text_input(
#                     "Search records",
#                     value="",
#                     placeholder="Enter keyword...",
#                     key="tab2_search"
#                 )
            
#             with col2:
#                 year_options = ("2000", "2023", "2024", "2025")
#                 tab2_selected_year = st.selectbox(
#                     "Year",
#                     year_options,
#                     index=3,
#                     key="tab2_year"
#                 )
#                 tab2_selected_year = int(tab2_selected_year)
            
#             with col3:
#                 status_options = ("Active", "Inactive")
#                 tab2_selected_status = st.selectbox(
#                     "Status",
#                     status_options,
#                     index=0,
#                     key="tab2_status"
#                 )
        
#         # Filter data based on selections
#         tab2_filtered_df = df[(df['Start_Year'] <= tab2_selected_year) & (df['End_Year'] >= tab2_selected_year)]
#         tab2_filtered_df = tab2_filtered_df[tab2_filtered_df['EFF_STATUS'] == tab2_selected_status]
        
#         if tab2_text_search:
#             mask1 = tab2_filtered_df["DESCRLONG_KHM"].str.contains(tab2_text_search, case=False, na=False)
#             mask2 = tab2_filtered_df["PRODUCT"].str.contains(tab2_text_search, case=False, na=False)
#             tab2_filtered_df = tab2_filtered_df[mask1 | mask2]

#         # Data display
#         if not tab2_filtered_df.empty:
#             st.markdown(f"""
#             <div style="background: white; border-radius: var(--border-radius); padding: 0.75rem 1.25rem; margin-bottom: 1rem; box-shadow: var(--card-shadow);">
#                 <div style="display: flex; justify-content: space-between; align-items: center;">
#                     <p style="margin: 0; color: var(--secondary-color); font-weight: 500; font-size: 0.95rem;">
#                         Found: <strong style="color: var(--primary-color);">{len(tab2_filtered_df):,}</strong> records
#                     </p>
#                     <p style="margin: 0; color: #7f8c8d; font-size: 0.85rem;">
#                         Date: {datetime.now().strftime("%d %B %Y")}
#                     </p>
#                 </div>
#             </div>
#             """, unsafe_allow_html=True)
            
#             # Display filtered results in a responsive grid
#             cols = st.columns(3)
            
#             for idx, row in tab2_filtered_df.iterrows():
#                 with cols[idx % 3]:
#                     province = str(row['នៅក្រោមខេត្ត']).strip() if pd.notna(row['នៅក្រោមខេត្ត']) else None
#                     province_text = (
#                         f"""<p style="margin: 0.4rem 0; font-size: 0.85rem;">
#                             <span style="color: #7f8c8d;">🏛 Province:</span> 
#                             <span style="color: var(--success-color); font-weight: 500;">{province}</span>
#                         </p>"""
#                         if province else ""
#                     )

#                     status_color = "#27ae60" if row['EFF_STATUS'] == 'Active' else "#e74c3c"
#                     status_icon = "🟢" if row['EFF_STATUS'] == 'Active' else "🔴"
                    
#                     st.markdown(f"""
#                     <div class="data-card">
#                         <h4>{row['PRODUCT']}</h4>
#                         <p style="margin: 0.4rem 0;">
#                             <span style="color: #7f8c8d;">📅 Year:</span> 
#                             <span style="color: var(--primary-color); font-weight: 500;">{row['EFFDT_Year']}-2025</span>
#                         </p>
#                         <p style="margin: 0.4rem 0;">
#                             <span style="color: #7f8c8d;">{status_icon} Status:</span> 
#                             <span style="color: {status_color}; font-weight: 500;">
#                                 {row['EFF_STATUS']}
#                             </span>
#                         </p>
#                         <p style="margin: 0.4rem 0;">
#                             <span style="color: #7f8c8d;">📖 Description:</span> 
#                             <span style="color: var(--secondary-color); font-size: 0.85rem;">
#                                 {row['DESCRLONG_KHM'][:90]}{'...' if len(row['DESCRLONG_KHM']) > 90 else ''}
#                             </span>
#                         </p>
#                         {province_text}
#                         <div style="margin-top: 0.4rem; text-align: right;">
#                             <span style="font-size: 0.75rem; color: #7f8c8d; font-style: italic;">Record #{idx + 1}</span>
#                         </div>
#                     </div>
#                     """, unsafe_allow_html=True)
#         else:
#             st.info("No data found for the selected filters.")

# if __name__ == "__main__":
#     Geography()


# import streamlit as st
# import pandas as pd
# import pydeck as pdk
# from datetime import datetime
# import plotly.express as px
# import plotly.graph_objects as go
# from plotly.subplots import make_subplots

# def Geography():
#     # Modern CSS with gradient backgrounds and glass morphism
#     st.markdown("""
#     <style>
#         :root {
#             --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
#             --secondary-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
#             --success-gradient: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
#             --warning-gradient: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
#             --dark-gradient: linear-gradient(135deg, #2c3e50 0%, #3498db 100%);
#             --glass-bg: rgba(255, 255, 255, 0.1);
#             --glass-border: rgba(255, 255, 255, 0.2);
#             --shadow-lg: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
#             --shadow-sm: 0 4px 16px 0 rgba(31, 38, 135, 0.2);
#         }
        
#         .main {
#             background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
#             font-family: 'Inter', 'Segoe UI', sans-serif;
#         }
        
#         .dashboard-header {
#             background: var(--primary-gradient);
#             padding: 3rem 2rem;
#             border-radius: 20px;
#             margin-bottom: 2rem;
#             color: white;
#             text-align: center;
#             box-shadow: var(--shadow-lg);
#             position: relative;
#             overflow: hidden;
#         }
        
#         .dashboard-header::before {
#             content: '';
#             position: absolute;
#             top: 0;
#             left: 0;
#             right: 0;
#             bottom: 0;
#             background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 100" fill="rgba(255,255,255,0.1)"><polygon points="0,0 1000,50 1000,100 0,100"/></svg>');
#             background-size: cover;
#         }
        
#         .dashboard-title {
#             font-size: 3rem;
#             font-weight: 800;
#             margin-bottom: 0.5rem;
#             text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
#         }
        
#         .dashboard-subtitle {
#             font-size: 1.2rem;
#             opacity: 0.9;
#             font-weight: 300;
#         }
        
#         .glass-card {
#             background: var(--glass-bg);
#             backdrop-filter: blur(16px);
#             -webkit-backdrop-filter: blur(16px);
#             border: 1px solid var(--glass-border);
#             border-radius: 20px;
#             padding: 1.5rem;
#             box-shadow: var(--shadow-sm);
#             transition: all 0.3s ease;
#         }
        
#         .glass-card:hover {
#             transform: translateY(-5px);
#             box-shadow: var(--shadow-lg);
#         }
        
#         .metric-card {
#             background: white;
#             border-radius: 16px;
#             padding: 1.5rem;
#             box-shadow: 0 4px 20px rgba(0,0,0,0.08);
#             border-left: 6px solid;
#             transition: all 0.3s ease;
#             height: 100%;
#             position: relative;
#             overflow: hidden;
#         }
        
#         .metric-card::before {
#             content: '';
#             position: absolute;
#             top: 0;
#             left: 0;
#             right: 0;
#             height: 4px;
#             background: var(--primary-gradient);
#         }
        
#         .metric-card:hover {
#             transform: translateY(-3px);
#             box-shadow: 0 8px 30px rgba(0,0,0,0.12);
#         }
        
#         .metric-icon {
#             font-size: 2.5rem;
#             margin-bottom: 1rem;
#             opacity: 0.8;
#         }
        
#         .metric-value {
#             font-size: 2.2rem;
#             font-weight: 800;
#             margin: 0.5rem 0;
#             background: var(--primary-gradient);
#             -webkit-background-clip: text;
#             -webkit-text-fill-color: transparent;
#         }
        
#         .metric-title {
#             font-size: 0.9rem;
#             color: #64748b;
#             text-transform: uppercase;
#             letter-spacing: 1px;
#             font-weight: 600;
#         }
        
#         .section-header {
#             font-size: 1.8rem;
#             font-weight: 700;
#             margin: 2rem 0 1rem 0;
#             background: var(--dark-gradient);
#             -webkit-background-clip: text;
#             -webkit-text-fill-color: transparent;
#             padding-bottom: 0.5rem;
#             border-bottom: 3px solid;
#             border-image: var(--primary-gradient) 1;
#         }
        
#         .stTabs [data-baseweb="tab-list"] {
#             gap: 8px;
#             background: transparent;
#         }
        
#         .stTabs [data-baseweb="tab"] {
#             background: white;
#             border-radius: 12px 12px 0 0;
#             padding: 12px 24px;
#             margin: 0 4px;
#             border: none;
#             font-weight: 600;
#             transition: all 0.3s ease;
#             box-shadow: 0 2px 8px rgba(0,0,0,0.1);
#         }
        
#         .stTabs [aria-selected="true"] {
#             background: var(--primary-gradient) !important;
#             color: white !important;
#             box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
#         }
        
#         .stTabs [aria-selected="false"]:hover {
#             background: #f8fafc !important;
#             transform: translateY(-2px);
#         }
        
#         .map-container {
#             border-radius: 20px;
#             overflow: hidden;
#             box-shadow: var(--shadow-lg);
#             border: none;
#             margin: 1rem 0;
#         }
        
#         .data-grid {
#             display: grid;
#             grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
#             gap: 1.5rem;
#             margin: 1.5rem 0;
#         }
        
#         .stat-badge {
#             background: var(--success-gradient);
#             color: white;
#             padding: 0.5rem 1rem;
#             border-radius: 25px;
#             font-size: 0.8rem;
#             font-weight: 600;
#             display: inline-flex;
#             align-items: center;
#             gap: 0.5rem;
#         }
        
#         /* Custom scrollbar */
#         ::-webkit-scrollbar {
#             width: 8px;
#         }
        
#         ::-webkit-scrollbar-track {
#             background: #f1f5f9;
#             border-radius: 10px;
#         }
        
#         ::-webkit-scrollbar-thumb {
#             background: var(--primary-gradient);
#             border-radius: 10px;
#         }
        
#         /* Animation for cards */
#         @keyframes fadeInUp {
#             from {
#                 opacity: 0;
#                 transform: translateY(30px);
#             }
#             to {
#                 opacity: 1;
#                 transform: translateY(0);
#             }
#         }
        
#         .glass-card, .metric-card {
#             animation: fadeInUp 0.6s ease-out;
#         }
        
#         /* Responsive design */
#         @media (max-width: 768px) {
#             .dashboard-title {
#                 font-size: 2rem;
#             }
            
#             .metric-value {
#                 font-size: 1.8rem;
#             }
            
#             .data-grid {
#                 grid-template-columns: 1fr;
#             }
#         }
#     </style>
#     """, unsafe_allow_html=True)

#     # Modern Header with Gradient
#     st.markdown("""
#     <div class="dashboard-header">
#         <div style="position: relative; z-index: 2;">
#             <h1 class="dashboard-title">🌍 Cambodia Geographic Intelligence</h1>
#             <p class="dashboard-subtitle">Advanced GIS Analytics & Spatial Data Visualization</p>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     # Load data with caching
#     @st.cache_data
#     def load_data():
#         file_path = "Geographyfordatareader.xlsx"
#         df = pd.read_excel(file_path, dtype=str).fillna("")
#         df['EFFDT'] = pd.to_datetime(df['EFFDT'], errors='coerce')
#         df['Effective_date'] = df['EFFDT_Year'].astype(str) + '-2025'
#         df['EFF_STATUS'] = df['EFF_STATUS'].map({'A': 'Active', 'I': 'Inactive'})
#         df[['Start_Year', 'End_Year']] = df['Effective_date'].str.split('-', expand=True)
#         df['Start_Year'] = df['Start_Year'].astype(int)
#         df['End_Year'] = df['End_Year'].astype(int)
        
#         # Clean and standardize province names
#         df['Province_Khmer'] = df['Province_Khmer'].str.strip()
#         df['Province_English'] = df['Province_English'].str.strip().str.title()
        
#         return df

#     df = load_data()

#     # Create modern tabs
#     tab1, tab2, tab3 = st.tabs(["🏠 Dashboard", "🗺️ Spatial Analysis", "📈 Data Explorer"])

#     with tab1:
#         # Overview Metrics with Icons
#         st.markdown('<div class="section-header">Executive Overview</div>', unsafe_allow_html=True)
        
#         # Filter for current data
#         current_data = df[(df['Start_Year'] <= 2025) & (df['End_Year'] >= 2025) & (df['EFF_STATUS'] == 'Active')]
        
#         col1, col2, col3, col4, col5 = st.columns(5)
        
#         metrics_data = [
#             {"icon": "📊", "title": "Total Records", "value": len(current_data), "color": "#667eea"},
#             {"icon": "🏛️", "title": "Provinces", "value": current_data['Province_English'].nunique(), "color": "#f093fb"},
#             {"icon": "🗺️", "title": "Districts", "value": len(current_data[current_data['group'] == 'District']), "color": "#4facfe"},
#             {"icon": "🏘️", "title": "Communes", "value": len(current_data[current_data['group'] == 'Communes']), "color": "#43e97b"},
#             {"icon": "🏫", "title": "Schools", "value": len(current_data[current_data['group'] == 'School']), "color": "#ff9a9e"}
#         ]
        
#         for i, metric in enumerate(metrics_data):
#             with [col1, col2, col3, col4, col5][i]:
#                 st.markdown(f"""
#                 <div class="metric-card" style="border-left-color: {metric['color']}">
#                     <div class="metric-icon">{metric['icon']}</div>
#                     <div class="metric-value">{metric['value']:,}</div>
#                     <div class="metric-title">{metric['title']}</div>
#                 </div>
#                 """, unsafe_allow_html=True)

#         # Charts Row
#         col1, col2 = st.columns([2, 1])
        
#         with col1:
#             st.markdown('<div class="section-header">Data Distribution</div>', unsafe_allow_html=True)
            
#             # Create interactive pie chart
#             group_data = current_data['group'].value_counts().reset_index()
#             group_data.columns = ['Category', 'Count']
            
#             fig_pie = px.pie(
#                 group_data, 
#                 values='Count', 
#                 names='Category',
#                 hole=0.6,
#                 color_discrete_sequence=px.colors.sequential.Blues_r
#             )
            
#             fig_pie.update_layout(
#                 height=400,
#                 showlegend=True,
#                 plot_bgcolor='rgba(0,0,0,0)',
#                 paper_bgcolor='rgba(0,0,0,0)',
#                 font=dict(size=12),
#                 margin=dict(t=0, b=0, l=0, r=0)
#             )
            
#             fig_pie.update_traces(
#                 textposition='inside',
#                 textinfo='percent+label',
#                 marker=dict(line=dict(color='white', width=2))
#             )
            
#             st.plotly_chart(fig_pie, use_container_width=True)

#         with col2:
#             st.markdown('<div class="section-header">Status Overview</div>', unsafe_allow_html=True)
            
#             # Status metrics
#             active_count = len(current_data)
#             total_count = len(df)
#             inactive_count = total_count - active_count
            
#             fig_gauge = go.Figure(go.Indicator(
#                 mode = "gauge+number+delta",
#                 value = active_count,
#                 domain = {'x': [0, 1], 'y': [0, 1]},
#                 title = {'text': "Active Records", 'font': {'size': 20}},
#                 delta = {'reference': total_count, 'relative': True, 'position': "top"},
#                 gauge = {
#                     'axis': {'range': [None, total_count], 'tickwidth': 1, 'tickcolor': "darkblue"},
#                     'bar': {'color': "darkblue"},
#                     'bgcolor': "white",
#                     'borderwidth': 2,
#                     'bordercolor': "gray",
#                     'steps': [
#                         {'range': [0, inactive_count], 'color': 'lightgray'},
#                         {'range': [inactive_count, total_count], 'color': 'lightblue'}],
#                     'threshold': {
#                         'line': {'color': "red", 'width': 4},
#                         'thickness': 0.75,
#                         'value': total_count}}
#             ))
            
#             fig_gauge.update_layout(height=300, font={'color': "darkblue", 'family': "Arial"})
#             st.plotly_chart(fig_gauge, use_container_width=True)

#     with tab2:
#         st.markdown('<div class="section-header">Satial Distribution Map</div>', unsafe_allow_html=True)
        
#         # Map controls
#         col1, col2, col3 = st.columns([2, 1, 1])
        
#         with col1:
#             map_type = st.selectbox("Map Visualization", ["Cluster View", "Heatmap", "Point Distribution"])
        
#         with col2:
#             year_filter = st.selectbox("Year", [2025, 2024, 2023], index=0)
        
#         with col3:
#             status_filter = st.selectbox("Status", ["Active", "Inactive"], index=0)
        
#         # Filter data for map
#         map_data = df[(df['Start_Year'] <= year_filter) & (df['End_Year'] >= year_filter)]
#         map_data = map_data[map_data['EFF_STATUS'] == status_filter]
        
#         # Prepare map data
#         map_data['Latitude'] = pd.to_numeric(map_data['Latitude'], errors='coerce')
#         map_data['Longitude'] = pd.to_numeric(map_data['Longitude'], errors='coerce')
#         map_data = map_data.dropna(subset=['Latitude', 'Longitude'])
        
#         if not map_data.empty:
#             # Enhanced map with different visualization options
#             if map_type == "Cluster View":
#                 layer = pdk.Layer(
#                     "HexagonLayer",
#                     map_data,
#                     get_position=['Longitude', 'Latitude'],
#                     radius=10000,
#                     elevation_scale=50,
#                     elevation_range=[0, 1000],
#                     pickable=True,
#                     extruded=True,
#                     coverage=1,
#                 )
#             elif map_type == "Heatmap":
#                 layer = pdk.Layer(
#                     "HeatmapLayer",
#                     map_data,
#                     get_position=['Longitude', 'Latitude'],
#                     aggregation='MEAN',
#                     get_weight=1,
#                     radius_pixels=50,
#                 )
#             else:  # Point Distribution
#                 layer = pdk.Layer(
#                     "ScatterplotLayer",
#                     map_data,
#                     get_position=['Longitude', 'Latitude'],
#                     get_color=[255, 140, 0, 160],
#                     get_radius=1000,
#                     pickable=True,
#                 )
            
#             view_state = pdk.ViewState(
#                 latitude=12.5657,
#                 longitude=104.9910,
#                 zoom=6,
#                 pitch=45 if map_type == "Cluster View" else 0,
#                 bearing=0,
#             )
            
#             st.pydeck_chart(pdk.Deck(
#                 layers=[layer],
#                 initial_view_state=view_state,
#                 tooltip={
#                     "html": """
#                     <div style="background: white; padding: 12px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
#                         <b>{Province_English}</b>
#                         <div style="margin-top: 8px;">
#                             <div>📊 Records: {count}</div>
#                             <div>🏛️ Type: {group}</div>
#                             <div>📅 Year: {EFFDT_Year}</div>
#                         </div>
#                     </div>
#                     """,
#                     "style": {
#                         "color": "#2c3e50",
#                         "fontFamily": "'Inter', sans-serif"
#                     }
#                 },
#                 map_style='light'
#             ), use_container_width=True)
            
#             # Map statistics
#             col1, col2, col3 = st.columns(3)
#             with col1:
#                 st.metric("Total Points", len(map_data))
#             with col2:
#                 st.metric("Covered Provinces", map_data['Province_English'].nunique())
#             with col3:
#                 st.metric("Data Density", f"{(len(map_data) / len(df) * 100):.1f}%")

#     with tab3:
#         st.markdown('<div class="section-header">Advanced Data Exploration</div>', unsafe_allow_html=True)
        
#         # Advanced filters
#         col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
        
#         with col1:
#             search_query = st.text_input("🔍 Search across all fields", placeholder="Enter keywords...")
        
#         with col2:
#             data_year = st.selectbox("Filter Year", ["All", "2025", "2024", "2023"])
        
#         with col3:
#             data_status = st.selectbox("Filter Status", ["All", "Active", "Inactive"])
        
#         with col4:
#             data_group = st.selectbox("Filter Group", ["All", "District", "Communes", "School"])
        
#         # Apply filters
#         filtered_data = df.copy()
        
#         if data_year != "All":
#             year_val = int(data_year)
#             filtered_data = filtered_data[(filtered_data['Start_Year'] <= year_val) & (filtered_data['End_Year'] >= year_val)]
        
#         if data_status != "All":
#             filtered_data = filtered_data[filtered_data['EFF_STATUS'] == data_status]
        
#         if data_group != "All":
#             filtered_data = filtered_data[filtered_data['group'] == data_group]
        
#         if search_query:
#             mask = (
#                 filtered_data["DESCRLONG_KHM"].str.contains(search_query, case=False, na=False) |
#                 filtered_data["PRODUCT"].str.contains(search_query, case=False, na=False) |
#                 filtered_data["Province_English"].str.contains(search_query, case=False, na=False)
#             )
#             filtered_data = filtered_data[mask]
        
#         # Display results
#         st.markdown(f"""
#         <div style="background: var(--primary-gradient); color: white; padding: 1rem; border-radius: 12px; margin: 1rem 0;">
#             <div style="display: flex; justify-content: space-between; align-items: center;">
#                 <span>📈 Filtered Results: <strong>{len(filtered_data):,}</strong> records found</span>
#                 <span>🕐 Last updated: {datetime.now().strftime("%Y-%m-%d %H:%M")}</span>
#             </div>
#         </div>
#         """, unsafe_allow_html=True)
        
#         if not filtered_data.empty:
#             # Display data in an expandable format
#             for idx, row in filtered_data.head(50).iterrows():  # Limit to first 50 for performance
#                 with st.expander(f"📍 {row['PRODUCT']} - {row['Province_English']}", expanded=False):
#                     col1, col2 = st.columns([2, 1])
                    
#                     with col1:
#                         st.write(f"**Description:** {row['DESCRLONG_KHM']}")
#                         st.write(f"**Province:** {row['Province_English']}")
                        
#                     with col2:
#                         status_color = "🟢" if row['EFF_STATUS'] == 'Active' else "🔴"
#                         st.write(f"**Status:** {status_color} {row['EFF_STATUS']}")
#                         st.write(f"**Period:** {row['EFFDT_Year']}-2025")
#                         st.write(f"**Type:** {row['group']}")
            
#             # Show download option
#             csv = filtered_data.to_csv(index=False)
#             st.download_button(
#                 label="📥 Download Filtered Data",
#                 data=csv,
#                 file_name=f"cambodia_geographic_data_{datetime.now().strftime('%Y%m%d')}.csv",
#                 mime="text/csv",
#             )
#         else:
#             st.info("No records found matching your filters. Try adjusting your search criteria.")

# if __name__ == "__main__":


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
        file_path = "Excel files/Geographyfordatareader.xlsx"
        df = pd.read_excel(file_path, dtype=str).fillna("")
        df['EFFDT'] = pd.to_datetime(df['EFFDT'], errors='coerce')
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
        

        # Create 5 columns
        col1, col2, col3, col4, col5 = st.columns(5)

        # Prepare the metrics data
        metrics_data = [
            {"title": "Total Records", "value": len(current_data), "color": "#667eea"},
            {"title": "Provinces", "value": current_data['Province_English'].nunique(), "color": "#667eea"},
            {"title": "Districts", "value": len(current_data[current_data['group'] == 'District']),"color": "#667eea"},
            {"title": "Communes", "value": len(current_data[current_data['group'] == 'Communes']), "color": "#667eea"},
            {"title": "Schools", "value": len(current_data[current_data['group'] == 'School']), "color": "#667eea"}
        ]

        # Render the metrics in styled cards
        for i, metric in enumerate(metrics_data):
            with [col1, col2, col3, col4, col5][i]:
                st.markdown(f"""
                <div class="metric-card" style="padding: 1rem; border-radius: 0.5rem; background-color: #f9fafb; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
                    <h3 style="margin: 0; color: #6b7280; font-size: 0.9rem;">{metric['title']}</h3>
                    <p style="margin: 0; color: {metric['color']}; font-size: 1.8rem; font-weight: 700;">{metric['value']:,}</p>
                </div>
                """, unsafe_allow_html=True)
        
    
        

        # Charts Section
        st.markdown('<div class="section-header"></div>', unsafe_allow_html=True)
        
        # First Row: Distribution Charts
        st.markdown('<div class="subsection-header">Data Distribution</div>', unsafe_allow_html=True)
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Enhanced pie chart with more details
            group_data = current_data['group'].value_counts().reset_index()
            group_data.columns = ['Category', 'Count']
            group_data = group_data[group_data['Category'] != 3]
            
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
            selected_year_type = st.selectbox("ប្រភេទឆ្នាំ", year_type_options, index=0)

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
                            year_display = f"{row['EFFDT_Year']}-2025"
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

