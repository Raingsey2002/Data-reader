# import streamlit as st
# import plotly.graph_objects as go
# import plotly.express as px
# import pandas as pd
# import numpy as np
# from datetime import datetime, timedelta

# def Monitoring():
   

#     # Custom CSS to match original design
#     st.markdown("""
#     <style>
#         /* Import Inter font */
#         @import url('https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap');
        
#         /* Material Symbols */
#         @import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0,0');
        
#         * {
#             font-family: 'Inter', sans-serif;
#         }
        
#         .stApp {
#             background-color: #f7fafc;
#         }
        
#         /* Card styling */
#         .card-pro {
#             background-color: #ffffff;
#             border: 1px solid #e2e8f0;
#             border-radius: 1rem;
#             padding: 1.5rem;
#             box-shadow: 0 4px 12px -6px rgba(26,32,44,0.08), 0 2px 4px -2px rgba(0,0,0,0.02);
#             transition: all 0.15s ease;
#             margin-bottom: 1rem;
#         }
        
#         /* Stat values */
#         .stat-value-pro {
#             font-size: 1.875rem;
#             font-weight: 600;
#             letter-spacing: -0.025em;
#             color: #1a202c;
#         }
        
#         .stat-label-pro {
#             font-size: 0.75rem;
#             font-weight: 500;
#             text-transform: uppercase;
#             letter-spacing: 0.05em;
#             color: #718096;
#             margin-top: 0.25rem;
#         }
        
#         /* Section title */
#         .section-title-pro {
#             color: #718096;
#             font-size: 0.75rem;
#             font-weight: 600;
#             text-transform: uppercase;
#             letter-spacing: 0.05em;
#             margin-bottom: 1rem;
#             display: flex;
#             align-items: center;
#             gap: 0.25rem;
#         }
        
#         /* Badges */
#         .badge-success {
#             background-color: #e6f7e6;
#             color: #38a169;
#             font-size: 11px;
#             font-weight: 600;
#             padding: 0.125rem 0.5rem;
#             border-radius: 9999px;
#         }
        
#         .badge-warning {
#             background-color: #fff3e0;
#             color: #dd6b20;
#             font-size: 11px;
#             font-weight: 600;
#             padding: 0.125rem 0.5rem;
#             border-radius: 9999px;
#         }
        
#         .badge-blue {
#             background-color: #e6f0ff;
#             color: #3182ce;
#             font-size: 11px;
#             font-weight: 600;
#             padding: 0.125rem 0.5rem;
#             border-radius: 9999px;
#         }
        
#         /* Header styling */
#         .sticky-header {
#             background-color: rgba(255,255,255,0.95);
#             backdrop-filter: blur(5px);
#             border: 1px solid #e2e8f0;
#             border-radius: 1rem;
#             padding: 1rem 1.5rem;
#             margin-bottom: 2rem;
#             box-shadow: 0 4px 10px -6px rgba(26,32,44,0.1);
#             position: sticky;
#             top: 1rem;
#             z-index: 50;
#         }
        
#         /* Footer styling */
#         .footer-pro {
#             margin-top: 2rem;
#             font-size: 11px;
#             color: #a0aec0;
#             border-top: 1px solid #e2e8f0;
#             padding-top: 1rem;
#             display: flex;
#             justify-content: space-between;
#             align-items: center;
#         }
        
#         /* Progress bar styling */
#         .progress-track-pro {
#             background-color: #edf2f7;
#             height: 0.5rem;
#             border-radius: 9999px;
#             overflow: hidden;
#             flex: 1;
#         }
        
#         .progress-bar-primary {
#             background-color: #3182ce;
#             height: 100%;
#             border-radius: 9999px;
#         }
        
#         /* Hide Streamlit branding */
#         #MainMenu {visibility: hidden;}
#         footer {visibility: hidden;}
#         header {visibility: hidden;}
        
#         /* Custom spacing */
#         .block-container {
#             padding-top: 1rem;
#             padding-bottom: 1rem;
#             max-width: 1600px;
#         }
        
#         /* Material icons styling */
#         .material-symbols-outlined {
#             font-family: 'Material Symbols Outlined';
#             font-weight: normal;
#             font-style: normal;
#             font-size: 24px;
#             line-height: 1;
#             letter-spacing: normal;
#             text-transform: none;
#             display: inline-block;
#             white-space: nowrap;
#             word-wrap: normal;
#             direction: ltr;
#             -webkit-font-smoothing: antialiased;
#         }
#     </style>
#     """, unsafe_allow_html=True)

#     # Header
#     st.markdown("""
#     <div class="sticky-header">
#         <div style="display: flex; align-items: center; justify-content: space-between;">
#             <div style="display: flex; align-items: center; gap: 1.25rem;">
#                 <div style="display: flex; align-items: center; gap: 0.75rem;">
#                     <div style="width: 2.5rem; height: 2.5rem; border-radius: 0.75rem; border: 1px solid #e2e8f0; background: linear-gradient(145deg, #1a202c, #3182ce); display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; font-size: 0.875rem;">FM</div>
#                 </div>
#                 <div style="height: 1.25rem; width: 1px; background-color: #e2e8f0;"></div>
#                 <div style="font-size: 0.875rem; font-weight: 500; color: #718096;">User & report analytics</div>
#             </div>
#             <div style="display: flex; align-items: center; gap: 0.75rem;">
#                 <span style="display: flex; align-items: center; gap: 0.375rem; padding: 0.375rem 0.75rem; border-radius: 9999px; background-color: #edf2f7; color: #2d3748;">
#                     <span class="material-symbols-outlined" style="font-size: 18px; color: #3182ce;">schedule</span> Live
#                 </span>
#                 <span style="width: 0.5rem; height: 0.5rem; border-radius: 9999px; background-color: #38a169;"></span>
#             </div>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     # Generate sample data
#     @st.cache_data
#     def generate_data():
#         # Account status data
#         active_users = 2924
#         inactive_users_90d = 899
#         inactive_users_30d = 505
#         total_users = active_users + inactive_users_90d + inactive_users_30d
        
#         # Monthly new users data
#         months = ['S', 'O', 'N', 'D', 'J', 'F', 'M', 'A', 'M', 'J', 'J', 'A']
#         this_year = [52, 68, 45, 82, 55, 70, 65, 92, 63, 80, 72, 100]
#         last_year = [45, 58, 38, 70, 48, 60, 55, 78, 52, 68, 62, 85]
        
#         # Top entities data
#         entities = ['GDNT', 'PT006', 'PT018', 'PT002', 'PT004', 'PT008', 'LM10', 'GDPFMIT', 'PT020', 'PT012']
#         reports = [2145, 618, 458, 162, 385, 410, 258, 327, 174, 291]
#         queries = [1222, 151, 201, 410, 147, 119, 265, 166, 284, 117]
        
#         # Activity trends data
#         months_full = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#         reports_trend = [112, 120, 84, 110, 52, 69, 90, 44, 86, 16, 92, 48]
#         queries_trend = [33, 19, 39, 86, 37, 50, 25, 75, 30, 76, 33, 41]
        
#         return {
#             'active_users': active_users,
#             'inactive_users_90d': inactive_users_90d,
#             'inactive_users_30d': inactive_users_30d,
#             'total_users': total_users,
#             'account_locks': 1493,
#             'queries_reports': 74,
#             'failed_logins': 217,
#             'months': months,
#             'this_year': this_year,
#             'last_year': last_year,
#             'entities': entities,
#             'reports': reports,
#             'queries': queries,
#             'months_full': months_full,
#             'reports_trend': reports_trend,
#             'queries_trend': queries_trend
#         }

#     data = generate_data()

#     # Main content
#     col1, col2 = st.columns([5, 7])

#     with col1:
#         st.markdown('<div class="section-title-pro"><span class="material-symbols-outlined" style="font-size: 18px; color: #3182ce;">speed</span> Activity metrics</div>', unsafe_allow_html=True)
        
#         metrics_col1, metrics_col2 = st.columns(2)
        
#         with metrics_col1:
#             st.markdown("""
#             <div class="card-pro">
#                 <div style="display: flex; justify-content: space-between; align-items: center;">
#                     <span class="material-symbols-outlined" style="font-size: 2rem; color: #3182ce;">group</span>
#                 </div>
#                 <div style="margin-top: 1rem;">
#                     <div class="stat-value-pro">{:,}</div>
#                     <div class="stat-label-pro">Total users</div>
#                 </div>
#             </div>
#             """.format(data['total_users']), unsafe_allow_html=True)
            
#             st.markdown("""
#             <div class="card-pro">
#                 <div style="display: flex; justify-content: space-between; align-items: center;">
#                     <span class="material-symbols-outlined" style="font-size: 2rem; color: #2b6cb0;">search</span>
#                 </div>
#                 <div style="margin-top: 1rem;">
#                     <div class="stat-value-pro">{}</div>
#                     <div class="stat-label-pro">Queries & reports</div>
#                 </div>
#             </div>
#             """.format(data['queries_reports']), unsafe_allow_html=True)
        
#         with metrics_col2:
#             st.markdown("""
#             <div class="card-pro">
#                 <div style="display: flex; justify-content: space-between; align-items: center;">
#                     <span class="material-symbols-outlined" style="font-size: 2rem; color: #dd6b20;">lock</span>
#                 </div>
#                 <div style="margin-top: 1rem;">
#                     <div class="stat-value-pro">{:,}</div>
#                     <div class="stat-label-pro">Account locks</div>
#                 </div>
#             </div>
#             """.format(data['account_locks']), unsafe_allow_html=True)
            
#             st.markdown("""
#             <div class="card-pro">
#                 <div style="display: flex; justify-content: space-between; align-items: center;">
#                     <span class="material-symbols-outlined" style="font-size: 2rem; color: #dd6b20;">warning</span>
#                 </div>
#                 <div style="margin-top: 1rem;">
#                     <div class="stat-value-pro">{}</div>
#                     <div class="stat-label-pro">Failed logins</div>
#                 </div>
#             </div>
#             """.format(data['failed_logins']), unsafe_allow_html=True)

#     with col2:
#         st.markdown('<div class="section-title-pro"><span class="material-symbols-outlined" style="font-size: 18px; color: #3182ce;">person_play</span> User activity</div>', unsafe_allow_html=True)
        
#         user_col1, user_col2 = st.columns(2)
        
#         with user_col1:
#             # Donut chart for account status
#             fig_donut = go.Figure()
            
#             # Add active users
#             fig_donut.add_trace(go.Pie(
#                 labels=['Active', 'Inactive User (30d)', 'Inactive User (90d)'],
#                 values=[data['active_users'], data['inactive_users_30d'], data['inactive_users_90d']],
#                 hole=0.7,
#                 marker=dict(colors=['#3182ce', '#3182ce', '#dd6b20']),
#                 textinfo='none',
#                 hoverinfo='label+value+percent',
#                 showlegend=False
#             ))
            
#             fig_donut.update_layout(
#                 height=250,
#                 margin=dict(l=20, r=20, t=20, b=20),
#                 paper_bgcolor='rgba(0,0,0,0)',
#                 plot_bgcolor='rgba(0,0,0,0)',
#                 annotations=[dict(text='Account<br>Status', x=0.5, y=0.5, font_size=14, showarrow=False)]
#             )
            
#             st.plotly_chart(fig_donut, use_container_width=True)
            
#             st.markdown("""
#             <div style="display: flex; gap: 1rem; justify-content: center; margin-top: 0.5rem;">
#                 <div style="display: flex; align-items: center; gap: 0.375rem;">
#                     <div style="width: 0.625rem; height: 0.625rem; border-radius: 9999px; background: #3182ce;"></div>
#                     <span style="color: #2d3748; font-size: 0.75rem;">Active {:,}</span>
#                 </div>
#                 <div style="display: flex; align-items: center; gap: 0.375rem;">
#                     <div style="width: 0.625rem; height: 0.625rem; border-radius: 9999px; background: #3182ce;"></div>
#                     <span style="color: #2d3748; font-size: 0.75rem;">Inactive User {:,}</span>
#                 </div>
#                 <div style="display: flex; align-items: center; gap: 0.375rem;">
#                     <div style="width: 0.625rem; height: 0.625rem; border-radius: 9999px; background: #dd6b20;"></div>
#                     <span style="color: #2d3748; font-size: 0.75rem;">Inactive User (90days) {:,}</span>
#                 </div>
#             </div>
#             """.format(data['active_users'], data['inactive_users_30d'], data['inactive_users_90d']), unsafe_allow_html=True)
        
#         with user_col2:
#             # Bar chart for new users
#             fig_bars = go.Figure()
            
#             fig_bars.add_trace(go.Bar(
#                 x=data['months'],
#                 y=data['last_year'],
#                 name='Last year',
#                 marker_color='#a0aec0',
#                 text=data['last_year'],
#                 textposition='outside',
#                 textfont=dict(size=10)
#             ))
            
#             fig_bars.add_trace(go.Bar(
#                 x=data['months'],
#                 y=data['this_year'],
#                 name='This year',
#                 marker=dict(
#                     color=data['this_year'],
#                     colorscale=[[0, '#2b6cb0'], [1, '#4299e1']],
#                     showscale=False
#                 ),
#                 text=data['this_year'],
#                 textposition='outside',
#                 textfont=dict(size=10)
#             ))
            
#             fig_bars.update_layout(
#                 barmode='group',
#                 height=250,
#                 margin=dict(l=20, r=20, t=30, b=20),
#                 paper_bgcolor='rgba(0,0,0,0)',
#                 plot_bgcolor='rgba(0,0,0,0)',
#                 legend=dict(
#                     orientation="h",
#                     yanchor="bottom",
#                     y=1.02,
#                     xanchor="center",
#                     x=0.5,
#                     font=dict(size=11)
#                 ),
#                 xaxis=dict(
#                     showgrid=False,
#                     tickfont=dict(size=10, color='#718096')
#                 ),
#                 yaxis=dict(
#                     showgrid=True,
#                     gridcolor='#edf2f7',
#                     gridwidth=1,
#                     tickfont=dict(size=10, color='#718096')
#                 )
#             )
            
#             st.plotly_chart(fig_bars, use_container_width=True)

#     # Second row
#     col3, col4, col5 = st.columns([4, 3, 5])

#     with col3:
#         st.markdown('<div class="section-title-pro"><span class="material-symbols-outlined" style="font-size: 18px; color: #3182ce;">database</span> Report usage analytics</div>', unsafe_allow_html=True)
        
#         st.markdown("""
#         <div class="card-pro">
#             <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.25rem;">
#                 <h3 style="font-weight: 600; color: #1a202c; font-size: 0.875rem;">Top 10 Active Entities · Reports and Queries</h3>
#                 <span style="font-size: 10px; padding: 0.25rem 0.75rem; border-radius: 9999px; font-weight: 600; background-color: #edf2f7; color: #2d3748;">current_month</span>
#             </div>
#         """, unsafe_allow_html=True)
        
#         for i, entity in enumerate(data['entities']):
#             total = data['reports'][i] + data['queries'][i]
#             max_total = max([r+q for r,q in zip(data['reports'], data['queries'])])
#             width_percent = (total / max_total) * 100
            
#             st.markdown("""
#             <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 0.875rem;">
#                 <span style="font-size: 0.75rem; font-weight: 500; width: 5rem; color: #718096;">{}</span>
#                 <div class="progress-track-pro">
#                     <div class="progress-bar-primary" style="width: {:.0f}%;"></div>
#                 </div>
#                 <span style="font-size: 0.75rem; color: #718096;">report:{:,} query:{:,}</span>
#             </div>
#             """.format(entity, width_percent, data['reports'][i], data['queries'][i]), unsafe_allow_html=True)
        
#         st.markdown("""
#             <div style="display: flex; justify-content: space-between; margin-top: 1rem; font-size: 9px; font-weight: 500; color: #a0aec0; border-top: 1px solid #e2e8f0; padding-top: 0.75rem;">
#                 <span>0</span><span>40</span><span>80</span><span>120</span><span>160</span>
#             </div>
#         </div>
#         """, unsafe_allow_html=True)

#     with col4:
#         # Usage by type donut
#         fig_type = go.Figure()
        
#         fig_type.add_trace(go.Pie(
#             labels=['Reports', 'Queries'],
#             values=[53, 21],
#             hole=0.7,
#             marker=dict(colors=['#2b6cb0', '#4299e1']),
#             textinfo='none',
#             hoverinfo='label+value+percent',
#             showlegend=False
#         ))
        
#         fig_type.update_layout(
#             height=280,
#             margin=dict(l=20, r=20, t=40, b=20),
#             paper_bgcolor='rgba(0,0,0,0)',
#             plot_bgcolor='rgba(0,0,0,0)',
#             annotations=[dict(text='Usage<br>by type', x=0.5, y=0.5, font_size=14, showarrow=False)]
#         )
        
#         st.plotly_chart(fig_type, use_container_width=True)
        
#         st.markdown("""
#         <div style="display: flex; gap: 1rem; justify-content: center; margin-top: 0.5rem;">
#             <div style="display: flex; align-items: center; gap: 0.375rem;">
#                 <div style="width: 0.75rem; height: 0.75rem; border-radius: 9999px; background: #2b6cb0;"></div>
#                 <span style="color: #2d3748;">Reports 53</span>
#             </div>
#             <div style="display: flex; align-items: center; gap: 0.375rem;">
#                 <div style="width: 0.75rem; height: 0.75rem; border-radius: 9999px; background: #4299e1;"></div>
#                 <span style="color: #2d3748;">Queries 21</span>
#             </div>
#         </div>
#         <div style="text-align: center; margin-top: 0.75rem; font-size: 0.875rem; color: #718096;">
#             Total <span style="color: #1a202c; font-weight: 500;">74</span>
#         </div>
#         """, unsafe_allow_html=True)

#     with col5:
#         st.markdown("""
#         <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.75rem;">
#             <div class="section-title-pro"><span class="material-symbols-outlined" style="font-size: 18px; color: #3182ce;">trending_up</span> Activity trends</div>
#             <span style="font-size: 10px; padding: 0.25rem 0.5rem; border-radius: 9999px; font-weight: 600; background-color: #edf2f7; color: #2d3748;">monthly</span>
#         </div>
#         """, unsafe_allow_html=True)
        
#         # Line chart for activity trends
#         fig_trends = go.Figure()
        
#         fig_trends.add_trace(go.Scatter(
#             x=data['months_full'],
#             y=data['reports_trend'],
#             name='Reports',
#             line=dict(color='#2b6cb0', width=3),
#             mode='lines+markers',
#             marker=dict(size=6)
#         ))
        
#         fig_trends.add_trace(go.Scatter(
#             x=data['months_full'],
#             y=data['queries_trend'],
#             name='Queries',
#             line=dict(color='#4299e1', width=3),
#             mode='lines+markers',
#             marker=dict(size=6)
#         ))
        
#         fig_trends.update_layout(
#             height=280,
#             margin=dict(l=20, r=20, t=20, b=20),
#             paper_bgcolor='rgba(0,0,0,0)',
#             plot_bgcolor='rgba(0,0,0,0)',
#             legend=dict(
#                 orientation="h",
#                 yanchor="bottom",
#                 y=1.02,
#                 xanchor="center",
#                 x=0.5,
#                 font=dict(size=11)
#             ),
#             xaxis=dict(
#                 showgrid=False,
#                 tickfont=dict(size=10, color='#718096')
#             ),
#             yaxis=dict(
#                 showgrid=True,
#                 gridcolor='#edf2f7',
#                 gridwidth=1,
#                 tickfont=dict(size=10, color='#718096')
#             )
#         )
        
#         st.plotly_chart(fig_trends, use_container_width=True)

#     # Footer
#     st.markdown("""
#     <div class="footer-pro">
#         <span>© FMIS · Developed and prepared by OIM Team.</span>
#         <span style="display: flex; align-items: center; gap: 0.5rem;">
#             <span style="width: 0.375rem; height: 0.375rem; border-radius: 9999px; background-color: #38a169;"></span>
#             All systems operational
#         </span>
#     </div>
#     """, unsafe_allow_html=True)

# # Call the function to run the dashboard
# if __name__ == "__main__":
#     Monitoring()



# import streamlit as st
# import plotly.graph_objects as go
# import plotly.express as px
# import pandas as pd
# import numpy as np
# from datetime import datetime, timedelta

# def Monitoring():
#     # # Page configuration
#     # st.set_page_config(
#     #     page_title="Enterprise SOC Dashboard",
#     #     page_icon="🛡️",
#     #     layout="wide",
#     #     initial_sidebar_state="collapsed"
#     # )

#     # Custom CSS to match original design
#     st.markdown("""
#     <style>
#         /* Import Inter font */
#         @import url('https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap');
        
#         /* Material Symbols */
#         @import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0,0');
        
#         * {
#             font-family: 'Inter', sans-serif;
#         }
        
#         .stApp {
#             background-color: #f7fafc;
#         }
        
#         /* Card styling */
#         .card-pro {
#             background-color: #ffffff;
#             border: 1px solid #e2e8f0;
#             border-radius: 1rem;
#             padding: 1.5rem;
#             box-shadow: 0 4px 12px -6px rgba(26,32,44,0.08), 0 2px 4px -2px rgba(0,0,0,0.02);
#             transition: all 0.15s ease;
#             margin-bottom: 1rem;
#             height: 100%;
#         }
        
#         /* Stat values */
#         .stat-value-pro {
#             font-size: 1.875rem;
#             font-weight: 600;
#             letter-spacing: -0.025em;
#             color: #1a202c;
#         }
        
#         .stat-label-pro {
#             font-size: 0.75rem;
#             font-weight: 500;
#             text-transform: uppercase;
#             letter-spacing: 0.05em;
#             color: #718096;
#             margin-top: 0.25rem;
#         }
        
#         /* Section title */
#         .section-title-pro {
#             color: #718096;
#             font-size: 0.75rem;
#             font-weight: 600;
#             text-transform: uppercase;
#             letter-spacing: 0.05em;
#             margin-bottom: 1rem;
#             display: flex;
#             align-items: center;
#             gap: 0.25rem;
#         }
        
#         /* Badges */
#         .badge-success {
#             background-color: #e6f7e6;
#             color: #38a169;
#             font-size: 11px;
#             font-weight: 600;
#             padding: 0.125rem 0.5rem;
#             border-radius: 9999px;
#         }
        
#         .badge-warning {
#             background-color: #fff3e0;
#             color: #dd6b20;
#             font-size: 11px;
#             font-weight: 600;
#             padding: 0.125rem 0.5rem;
#             border-radius: 9999px;
#         }
        
#         .badge-blue {
#             background-color: #e6f0ff;
#             color: #3182ce;
#             font-size: 11px;
#             font-weight: 600;
#             padding: 0.125rem 0.5rem;
#             border-radius: 9999px;
#         }
        
#         /* Header styling */
#         .sticky-header {
#             background-color: rgba(255,255,255,0.95);
#             backdrop-filter: blur(5px);
#             border: 1px solid #e2e8f0;
#             border-radius: 1rem;
#             padding: 1rem 1.5rem;
#             margin-bottom: 2rem;
#             box-shadow: 0 4px 10px -6px rgba(26,32,44,0.1);
#             position: sticky;
#             top: 1rem;
#             z-index: 50;
#         }
        
#         /* Footer styling */
#         .footer-pro {
#             margin-top: 2rem;
#             font-size: 11px;
#             color: #a0aec0;
#             border-top: 1px solid #e2e8f0;
#             padding-top: 1rem;
#             display: flex;
#             justify-content: space-between;
#             align-items: center;
#         }
        
#         /* Hide Streamlit branding */
#         #MainMenu {visibility: hidden;}
#         footer {visibility: hidden;}
#         header {visibility: hidden;}
        
#         /* Custom spacing */
#         .block-container {
#             padding-top: 1rem;
#             padding-bottom: 1rem;
#             max-width: 1600px;
#         }
        
#         /* Material icons styling */
#         .material-symbols-outlined {
#             font-family: 'Material Symbols Outlined';
#             font-weight: normal;
#             font-style: normal;
#             font-size: 24px;
#             line-height: 1;
#             letter-spacing: normal;
#             text-transform: none;
#             display: inline-block;
#             white-space: nowrap;
#             word-wrap: normal;
#             direction: ltr;
#             -webkit-font-smoothing: antialiased;
#         }
        
#         /* Metric card hover effect */
#         .metric-card:hover {
#             transform: translateY(-2px);
#             box-shadow: 0 8px 24px -8px rgba(26,32,44,0.12);
#         }
        
#         /* Chart container */
#         .chart-container {
#             background-color: #ffffff;
#             border: 1px solid #e2e8f0;
#             border-radius: 1rem;
#             padding: 1rem;
#             margin-bottom: 1rem;
#         }
#     </style>
#     """, unsafe_allow_html=True)

#     # Header
#     st.markdown("""
#     <div class="sticky-header">
#         <div style="display: flex; align-items: center; justify-content: space-between;">
#             <div style="display: flex; align-items: center; gap: 1.25rem;">
#                 <div style="display: flex; align-items: center; gap: 0.75rem;">
#                     <div style="width: 2.5rem; height: 2.5rem; border-radius: 0.75rem; border: 1px solid #e2e8f0; background: linear-gradient(145deg, #1a202c, #3182ce); display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; font-size: 0.875rem;">FM</div>
#                     <div style="font-weight: 600; color: #1a202c;">FMIS</div>
#                 </div>
#                 <div style="height: 1.25rem; width: 1px; background-color: #e2e8f0;"></div>
#                 <div style="font-size: 0.875rem; font-weight: 500; color: #718096;">Security Operations Center · User & Report Analytics</div>
#             </div>
#             <div style="display: flex; align-items: center; gap: 1rem;">
#                 <span style="display: flex; align-items: center; gap: 0.375rem; padding: 0.375rem 0.75rem; border-radius: 9999px; background-color: #edf2f7; color: #2d3748;">
#                     <span class="material-symbols-outlined" style="font-size: 18px; color: #3182ce;">schedule</span> Live Dashboard
#                 </span>
#                 <span style="display: flex; align-items: center; gap: 0.375rem;">
#                     <span style="width: 0.5rem; height: 0.5rem; border-radius: 9999px; background-color: #38a169;"></span>
#                     <span style="font-size: 0.75rem; color: #718096;">All systems operational</span>
#                 </span>
#             </div>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     # Generate sample data
#     @st.cache_data
#     def generate_data():
#         # Account status data
#         active_users = 2924
#         inactive_users_90d = 899
#         inactive_users_30d = 505
#         total_users = active_users + inactive_users_90d + inactive_users_30d
        
#         # Monthly new users data
#         months = ['S', 'O', 'N', 'D', 'J', 'F', 'M', 'A', 'M', 'J', 'J', 'A']
#         this_year = [52, 68, 45, 82, 55, 70, 65, 92, 63, 80, 72, 100]
#         last_year = [45, 58, 38, 70, 48, 60, 55, 78, 52, 68, 62, 85]
        
#         # Top entities data
#         entities = ['GDNT', 'PT006', 'PT018', 'PT002', 'PT004', 'PT008', 'LM10', 'GDPFMIT', 'PT020', 'PT012']
#         reports = [2145, 618, 458, 162, 385, 410, 258, 327, 174, 291]
#         queries = [1222, 151, 201, 410, 147, 119, 265, 166, 284, 117]
        
#         # Activity trends data
#         months_full = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#         reports_trend = [112, 120, 84, 110, 52, 69, 90, 44, 86, 16, 92, 48]
#         queries_trend = [33, 19, 39, 86, 37, 50, 25, 75, 30, 76, 33, 41]
        
#         return {
#             'active_users': active_users,
#             'inactive_users_90d': inactive_users_90d,
#             'inactive_users_30d': inactive_users_30d,
#             'total_users': total_users,
#             'account_locks': 1493,
#             'queries_reports': 74,
#             'failed_logins': 217,
#             'months': months,
#             'this_year': this_year,
#             'last_year': last_year,
#             'entities': entities,
#             'reports': reports,
#             'queries': queries,
#             'months_full': months_full,
#             'reports_trend': reports_trend,
#             'queries_trend': queries_trend
#         }

#     data = generate_data()

#     # Create DataFrame for entity data
#     df_entities = pd.DataFrame({
#         'Entity': data['entities'],
#         'Reports': data['reports'],
#         'Queries': data['queries'],
#         'Total': [r + q for r, q in zip(data['reports'], data['queries'])]
#     }).sort_values('Total', ascending=True)

#     # Main content with better organization
#     st.markdown("## 📊 Security Analytics Dashboard")

#     # Row 1: Key Metrics
#     st.markdown("### 🔍 Key Metrics")
#     col1, col2, col3, col4 = st.columns(4)

#     with col1:
#         st.markdown("""
#         <div class="card-pro metric-card">
#             <div style="display: flex; justify-content: space-between; align-items: center;">
#                 <span class="material-symbols-outlined" style="font-size: 2rem; color: #3182ce;">group</span>
#                 <span class="badge-blue">+12%</span>
#             </div>
#             <div style="margin-top: 1rem;">
#                 <div class="stat-value-pro">{:,}</div>
#                 <div class="stat-label-pro">Total Users</div>
#                 <div style="font-size: 0.7rem; color: #38a169; margin-top: 0.25rem;">↑ 8.3% from last month</div>
#             </div>
#         </div>
#         """.format(data['total_users']), unsafe_allow_html=True)

#     with col2:
#         st.markdown("""
#         <div class="card-pro metric-card">
#             <div style="display: flex; justify-content: space-between; align-items: center;">
#                 <span class="material-symbols-outlined" style="font-size: 2rem; color: #2b6cb0;">search</span>
#                 <span class="badge-neutral">MTD</span>
#             </div>
#             <div style="margin-top: 1rem;">
#                 <div class="stat-value-pro">{}</div>
#                 <div class="stat-label-pro">Queries & Reports</div>
#                 <div style="font-size: 0.7rem; color: #718096; margin-top: 0.25rem;">24 reports, 50 queries</div>
#             </div>
#         </div>
#         """.format(data['queries_reports']), unsafe_allow_html=True)

#     with col3:
#         st.markdown("""
#         <div class="card-pro metric-card">
#             <div style="display: flex; justify-content: space-between; align-items: center;">
#                 <span class="material-symbols-outlined" style="font-size: 2rem; color: #dd6b20;">lock</span>
#                 <span class="badge-warning">+3</span>
#             </div>
#             <div style="margin-top: 1rem;">
#                 <div class="stat-value-pro">{:,}</div>
#                 <div class="stat-label-pro">Account Locks</div>
#                 <div style="font-size: 0.7rem; color: #dd6b20; margin-top: 0.25rem;">↑ 2.1% from yesterday</div>
#             </div>
#         </div>
#         """.format(data['account_locks']), unsafe_allow_html=True)

#     with col4:
#         st.markdown("""
#         <div class="card-pro metric-card">
#             <div style="display: flex; justify-content: space-between; align-items: center;">
#                 <span class="material-symbols-outlined" style="font-size: 2rem; color: #dd6b20;">warning</span>
#                 <span class="badge-warning">+8%</span>
#             </div>
#             <div style="margin-top: 1rem;">
#                 <div class="stat-value-pro">{}</div>
#                 <div class="stat-label-pro">Failed Logins</div>
#                 <div style="font-size: 0.7rem; color: #dd6b20; margin-top: 0.25rem;">↑ 5.7% from last week</div>
#             </div>
#         </div>
#         """.format(data['failed_logins']), unsafe_allow_html=True)

#     # Row 2: User Activity and Account Status
#     st.markdown("### 👥 User Activity Analysis")
#     col5, col6 = st.columns([5, 7])

#     with col5:
#         st.markdown('<div class="section-title-pro"><span class="material-symbols-outlined" style="font-size: 18px; color: #3182ce;">account_circle</span> Account Status Distribution</div>', unsafe_allow_html=True)
        
#         # Enhanced donut chart for account status
#         fig_donut = go.Figure()
        
#         fig_donut.add_trace(go.Pie(
#             labels=['Active Users', 'Inactive (30 days)', 'Inactive (90+ days)'],
#             values=[data['active_users'], data['inactive_users_30d'], data['inactive_users_90d']],
#             hole=0.6,
#             marker=dict(colors=['#3182ce', '#90cdf4', '#dd6b20']),
#             textinfo='percent',
#             textposition='inside',
#             hoverinfo='label+value+percent',
#             showlegend=False
#         ))
        
#         fig_donut.update_layout(
#             height=300,
#             margin=dict(l=20, r=20, t=20, b=20),
#             paper_bgcolor='rgba(0,0,0,0)',
#             plot_bgcolor='rgba(0,0,0,0)',
#             annotations=[dict(
#                 text=f"Total<br>{data['total_users']:,}",
#                 x=0.5, y=0.5, 
#                 font_size=16, 
#                 font_color='#1a202c',
#                 showarrow=False
#             )]
#         )
        
#         st.plotly_chart(fig_donut, use_container_width=True)

#     with col6:
#         st.markdown('<div class="section-title-pro"><span class="material-symbols-outlined" style="font-size: 18px; color: #3182ce;">bar_chart</span> New Users (Monthly Comparison)</div>', unsafe_allow_html=True)
        
#         # Enhanced bar chart for new users
#         fig_bars = go.Figure()
        
#         fig_bars.add_trace(go.Bar(
#             x=data['months'],
#             y=data['last_year'],
#             name='Last Year',
#             marker_color='#a0aec0',
#             text=data['last_year'],
#             textposition='outside',
#             textfont=dict(size=10, color='#718096'),
#             opacity=0.7
#         ))
        
#         fig_bars.add_trace(go.Bar(
#             x=data['months'],
#             y=data['this_year'],
#             name='This Year',
#             marker=dict(
#                 color=data['this_year'],
#                 colorscale=[[0, '#2b6cb0'], [1, '#4299e1']],
#                 showscale=False
#             ),
#             text=data['this_year'],
#             textposition='outside',
#             textfont=dict(size=10, color='#2b6cb0', weight='bold')
#         ))
        
#         fig_bars.update_layout(
#             barmode='group',
#             height=300,
#             margin=dict(l=20, r=20, t=30, b=20),
#             paper_bgcolor='rgba(0,0,0,0)',
#             plot_bgcolor='rgba(0,0,0,0)',
#             legend=dict(
#                 orientation="h",
#                 yanchor="bottom",
#                 y=1.02,
#                 xanchor="center",
#                 x=0.5,
#                 font=dict(size=11)
#             ),
#             xaxis=dict(
#                 showgrid=False,
#                 tickfont=dict(size=11, color='#718096')
#             ),
#             yaxis=dict(
#                 showgrid=True,
#                 gridcolor='#edf2f7',
#                 gridwidth=1,
#                 tickfont=dict(size=10, color='#718096'),
#                 title=dict(text="Number of Users", font=dict(size=10, color='#718096'))
#             )
#         )
        
#         st.plotly_chart(fig_bars, use_container_width=True)

#     # Row 3: Entity Analysis and Usage Trends
#     st.markdown("### 📈 Entity Performance & Usage Analytics")
#     col7, col8 = st.columns([6, 6])

#     with col7:
#         st.markdown('<div class="section-title-pro"><span class="material-symbols-outlined" style="font-size: 18px; color: #3182ce;">business</span> Top 10 Active Entities - Reports vs Queries</div>', unsafe_allow_html=True)
        
#         # Enhanced horizontal bar chart for entities
#         fig_entities = go.Figure()
        
#         fig_entities.add_trace(go.Bar(
#             y=df_entities['Entity'],
#             x=df_entities['Reports'],
#             name='Reports',
#             orientation='h',
#             marker=dict(color='#3182ce'),
#             text=df_entities['Reports'],
#             textposition='inside',
#             textfont=dict(color='white', size=10),
#             hovertemplate='<b>%{y}</b><br>Reports: %{x}<br>Queries: %{customdata}<extra></extra>',
#             customdata=df_entities['Queries']
#         ))
        
#         fig_entities.add_trace(go.Bar(
#             y=df_entities['Entity'],
#             x=df_entities['Queries'],
#             name='Queries',
#             orientation='h',
#             marker=dict(color='#90cdf4'),
#             text=df_entities['Queries'],
#             textposition='inside',
#             textfont=dict(color='#1a202c', size=10),
#             hovertemplate='<b>%{y}</b><br>Queries: %{x}<br>Reports: %{customdata}<extra></extra>',
#             customdata=df_entities['Reports']
#         ))
        
#         fig_entities.update_layout(
#             barmode='stack',
#             height=400,
#             margin=dict(l=100, r=20, t=30, b=20),
#             paper_bgcolor='rgba(0,0,0,0)',
#             plot_bgcolor='rgba(0,0,0,0)',
#             legend=dict(
#                 orientation="h",
#                 yanchor="bottom",
#                 y=1.02,
#                 xanchor="center",
#                 x=0.5,
#                 font=dict(size=11)
#             ),
#             xaxis=dict(
#                 showgrid=True,
#                 gridcolor='#edf2f7',
#                 gridwidth=1,
#                 tickfont=dict(size=10, color='#718096'),
#                 title=dict(text="Number of Activities", font=dict(size=10, color='#718096'))
#             ),
#             yaxis=dict(
#                 tickfont=dict(size=11, color='#2d3748', weight='bold'),
#                 autorange="reversed"
#             )
#         )
        
#         st.plotly_chart(fig_entities, use_container_width=True)

#     with col8:
#         # Create two sub-columns for the right side
#         subcol1, subcol2 = st.columns(2)
        
#         with subcol1:
#             st.markdown('<div class="section-title-pro"><span class="material-symbols-outlined" style="font-size: 18px; color: #3182ce;">pie_chart</span> Usage by Type</div>', unsafe_allow_html=True)
            
#             # Usage by type donut
#             fig_type = go.Figure()
            
#             fig_type.add_trace(go.Pie(
#                 labels=['Reports', 'Queries'],
#                 values=[53, 21],
#                 hole=0.6,
#                 marker=dict(colors=['#2b6cb0', '#4299e1']),
#                 textinfo='percent',
#                 textposition='inside',
#                 hoverinfo='label+value+percent',
#                 showlegend=False
#             ))
            
#             fig_type.update_layout(
#                 height=200,
#                 margin=dict(l=10, r=10, t=10, b=10),
#                 paper_bgcolor='rgba(0,0,0,0)',
#                 plot_bgcolor='rgba(0,0,0,0)',
#                 annotations=[dict(
#                     text=f"Total<br>74",
#                     x=0.5, y=0.5, 
#                     font_size=12, 
#                     font_color='#1a202c',
#                     showarrow=False
#                 )]
#             )
            
#             st.plotly_chart(fig_type, use_container_width=True)
            
#             # Quick stats
#             st.markdown("""
#             <div style="background-color: #f8fafc; padding: 1rem; border-radius: 0.75rem; margin-top: 0.5rem;">
#                 <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
#                     <span style="color: #718096;">Reports:</span>
#                     <span style="color: #1a202c; font-weight: 600;">53 (71.6%)</span>
#                 </div>
#                 <div style="display: flex; justify-content: space-between;">
#                     <span style="color: #718096;">Queries:</span>
#                     <span style="color: #1a202c; font-weight: 600;">21 (28.4%)</span>
#                 </div>
#             </div>
#             """, unsafe_allow_html=True)
        
#         with subcol2:
#             st.markdown('<div class="section-title-pro"><span class="material-symbols-outlined" style="font-size: 18px; color: #3182ce;">trending_up</span> Activity Trends</div>', unsafe_allow_html=True)
            
#             # Line chart for activity trends
#             fig_trends = go.Figure()
            
#             fig_trends.add_trace(go.Scatter(
#                 x=data['months_full'],
#                 y=data['reports_trend'],
#                 name='Reports',
#                 line=dict(color='#2b6cb0', width=3),
#                 mode='lines+markers',
#                 marker=dict(size=8, color='#2b6cb0'),
#                 fill='tonexty',
#                 fillcolor='rgba(43,108,176,0.1)'
#             ))
            
#             fig_trends.add_trace(go.Scatter(
#                 x=data['months_full'],
#                 y=data['queries_trend'],
#                 name='Queries',
#                 line=dict(color='#4299e1', width=3),
#                 mode='lines+markers',
#                 marker=dict(size=8, color='#4299e1'),
#                 fill='tonexty',
#                 fillcolor='rgba(66,153,225,0.1)'
#             ))
            
#             fig_trends.update_layout(
#                 height=250,
#                 margin=dict(l=10, r=10, t=10, b=20),
#                 paper_bgcolor='rgba(0,0,0,0)',
#                 plot_bgcolor='rgba(0,0,0,0)',
#                 legend=dict(
#                     orientation="h",
#                     yanchor="bottom",
#                     y=1.02,
#                     xanchor="center",
#                     x=0.5,
#                     font=dict(size=9)
#                 ),
#                 xaxis=dict(
#                     showgrid=False,
#                     tickfont=dict(size=8, color='#718096'),
#                     tickangle=45
#                 ),
#                 yaxis=dict(
#                     showgrid=True,
#                     gridcolor='#edf2f7',
#                     gridwidth=1,
#                     tickfont=dict(size=8, color='#718096'),
#                     showticklabels=False
#                 )
#             )
            
#             st.plotly_chart(fig_trends, use_container_width=True)
            
#             # Summary stats
#             st.markdown("""
#             <div style="display: flex; gap: 1rem; justify-content: space-between; margin-top: 0.5rem;">
#                 <div style="text-align: center; flex: 1; background-color: #f8fafc; padding: 0.5rem; border-radius: 0.5rem;">
#                     <div style="color: #718096; font-size: 0.6rem;">Avg Reports</div>
#                     <div style="color: #2b6cb0; font-weight: 600; font-size: 0.9rem;">76.8</div>
#                 </div>
#                 <div style="text-align: center; flex: 1; background-color: #f8fafc; padding: 0.5rem; border-radius: 0.5rem;">
#                     <div style="color: #718096; font-size: 0.6rem;">Avg Queries</div>
#                     <div style="color: #4299e1; font-weight: 600; font-size: 0.9rem;">45.4</div>
#                 </div>
#             </div>
#             """, unsafe_allow_html=True)

#     # Footer
#     st.markdown("""
#     <div class="footer-pro">
#         <span>© FMIS Security Operations Center · Developed and prepared by OIM Team</span>
#         <span style="display: flex; align-items: center; gap: 1rem;">
#             <span style="display: flex; align-items: center; gap: 0.25rem;">
#                 <span style="width: 0.375rem; height: 0.375rem; border-radius: 9999px; background-color: #38a169;"></span>
#                 Last updated: {}
#             </span>
#         </span>
#     </div>
#     """.format(datetime.now().strftime("%Y-%m-%d %H:%M UTC")), unsafe_allow_html=True)

# # Call the function to run the dashboard
# if __name__ == "__main__":
#     Monitoring()




# import streamlit as st
# import plotly.graph_objects as go
# import plotly.express as px
# import pandas as pd
# import numpy as np
# from datetime import datetime, timedelta

# def Monitoring():
#     # Page config for better TV display
#     # st.set_page_config(
#     #     page_title="FMIS Monitoring Dashboard",
#     #     layout="wide",
#     #     initial_sidebar_state="collapsed"
#     # )

#     # Custom CSS for TV-optimized professional dashboard
#     st.markdown("""
#     <style>
#         /* Import fonts */
#         @import url('https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap');
#         @import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0,0');
        
#         * {
#             font-family: 'Inter', sans-serif;
#             margin: 0;
#             padding: 0;
#             box-sizing: border-box;
#         }
        
#         /* Main container for TV */
#         .stApp {
#             background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
#             min-height: 100vh;
#             padding: 1rem;
#         }
        
#         /* Hide Streamlit branding for cleaner look */
#         #MainMenu {visibility: hidden;}
#         footer {visibility: hidden;}
#         header {visibility: hidden;}
        
#         /* Main container adjustments */
#         .block-container {
#             padding: 0.5rem 1rem;
#             max-width: 1920px;
#             margin: 0 auto;
#         }
        
#         /* Professional card design */
#         .tv-card {
#             background: rgba(255, 255, 255, 0.95);
#             backdrop-filter: blur(10px);
#             border: 1px solid rgba(226, 232, 240, 0.8);
#             border-radius: 1.5rem;
#             padding: 1.5rem;
#             box-shadow: 0 20px 40px -15px rgba(0,0,0,0.15), 
#                         0 0 0 1px rgba(0,0,0,0.02) inset;
#             transition: transform 0.2s ease, box-shadow 0.2s ease;
#             height: 100%;
#         }
        
#         .tv-card:hover {
#             transform: translateY(-2px);
#             box-shadow: 0 25px 50px -15px rgba(0,0,0,0.25);
#         }
        
#         /* Metric cards with gradients */
#         .metric-card {
#             background: linear-gradient(145deg, #ffffff, #f8fafc);
#             border-radius: 1.25rem;
#             padding: 1.75rem 1.5rem;
#             border: 1px solid rgba(226, 232, 240, 0.6);
#             box-shadow: 0 8px 20px -10px rgba(0,0,0,0.1);
#             transition: all 0.2s ease;
#         }
        
#         .metric-card:hover {
#             border-color: #3182ce;
#             box-shadow: 0 12px 25px -10px #3182ce40;
#         }
        
#         /* Large stat values for TV viewing */
#         .stat-value-tv {
#             font-size: 3rem;
#             font-weight: 700;
#             letter-spacing: -0.03em;
#             background: linear-gradient(135deg, #1a202c, #2d3748);
#             -webkit-background-clip: text;
#             -webkit-text-fill-color: transparent;
#             line-height: 1.2;
#         }
        
#         .stat-label-tv {
#             font-size: 1rem;
#             font-weight: 500;
#             color: #718096;
#             text-transform: uppercase;
#             letter-spacing: 0.05em;
#             margin-top: 0.5rem;
#         }
        
#         /* Section headers */
#         .section-header {
#             display: flex;
#             align-items: center;
#             gap: 0.75rem;
#             margin-bottom: 1.5rem;
#             padding-bottom: 0.75rem;
#             border-bottom: 2px solid #e2e8f0;
#         }
        
#         .section-header h2 {
#             font-size: 1.35rem;
#             font-weight: 600;
#             color: #1a202c;
#             margin: 0;
#         }
        
#         .section-header .material-symbols-outlined {
#             font-size: 2rem;
#             color: #3182ce;
#             background: rgba(49, 130, 206, 0.1);
#             padding: 0.5rem;
#             border-radius: 12px;
#         }
        
#         /* Status badges */
#         .status-badge {
#             display: inline-flex;
#             align-items: center;
#             gap: 0.5rem;
#             padding: 0.5rem 1rem;
#             border-radius: 100px;
#             font-weight: 600;
#             font-size: 0.9rem;
#             background: white;
#             border: 1px solid #e2e8f0;
#         }
        
#         .status-badge.live {
#             background: #f0f9ff;
#             border-color: #3182ce;
#             color: #3182ce;
#         }
        
#         .status-badge.success {
#             background: #f0fdf4;
#             border-color: #38a169;
#             color: #38a169;
#         }
        
#         /* Progress bar enhancements */
#         .progress-container {
#             background: #edf2f7;
#             height: 0.75rem;
#             border-radius: 100px;
#             overflow: hidden;
#             flex: 1;
#         }
        
#         .progress-fill {
#             height: 100%;
#             border-radius: 100px;
#             background: linear-gradient(90deg, #3182ce, #63b3ed);
#             transition: width 0.3s ease;
#         }
        
#         /* Footer styling */
#         .tv-footer {
#             margin-top: 2rem;
#             padding: 1.25rem 2rem;
#             background: rgba(255,255,255,0.9);
#             backdrop-filter: blur(10px);
#             border-radius: 1.25rem;
#             border: 1px solid #e2e8f0;
#             display: flex;
#             justify-content: space-between;
#             align-items: center;
#             font-size: 0.95rem;
#             color: #64748b;
#         }
        
#         /* KPI indicators */
#         .kpi-indicator {
#             display: flex;
#             align-items: center;
#             gap: 0.5rem;
#             font-size: 0.9rem;
#             padding: 0.35rem 1rem;
#             background: #f8fafc;
#             border-radius: 100px;
#             border: 1px solid #e2e8f0;
#         }
        
#         .trend-up { color: #38a169; }
#         .trend-down { color: #e53e3e; }
        
#         /* Responsive adjustments for TV */
#         @media (min-width: 1600px) {
#             .stat-value-tv { font-size: 3.5rem; }
#             .section-header h2 { font-size: 1.5rem; }
#         }
#     </style>
#     """, unsafe_allow_html=True)

#     # Top header with live status and timestamp
#     current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
#     st.markdown(f"""
#     <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem; background: white; padding: 1rem 2rem; border-radius: 100px; border: 1px solid #e2e8f0; box-shadow: 0 4px 12px -6px rgba(0,0,0,0.1);">
#         <div style="display: flex; align-items: center; gap: 2rem;">
#             <div style="display: flex; align-items: center; gap: 1rem;">
#                 <div style="width: 3rem; height: 3rem; background: linear-gradient(135deg, #1a202c, #3182ce); border-radius: 1rem; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; font-size: 1.2rem;">FM</div>
#                 <span style="font-weight: 600; color: #1a202c; font-size: 1.25rem;">FMIS Analytics</span>
#             </div>
#             <span class="status-badge live">
#                 <span class="material-symbols-outlined" style="font-size: 1.25rem;">fiber_manual_record</span>
#                 LIVE MONITORING
#             </span>
#         </div>
#         <div style="display: flex; align-items: center; gap: 2rem;">
#             <div class="kpi-indicator">
#                 <span class="material-symbols-outlined" style="color: #3182ce;">update</span>
#                 {current_time}
#             </div>
#             <div class="kpi-indicator">
#                 <span class="material-symbols-outlined" style="color: #38a169;">check_circle</span>
#                 System OK
#             </div>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     # Generate enhanced sample data
#     @st.cache_data(ttl=300)  # Cache for 5 minutes
#     def generate_enhanced_data():
#         # Enhanced metrics
#         active_users = 2924
#         inactive_users_90d = 899
#         inactive_users_30d = 505
#         total_users = active_users + inactive_users_90d + inactive_users_30d
        
#         # Monthly trends with growth indicators
#         months = ['Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug']
#         this_year = [52, 68, 45, 82, 55, 70, 65, 92, 63, 80, 72, 100]
#         last_year = [45, 58, 38, 70, 48, 60, 55, 78, 52, 68, 62, 85]
        
#         # Calculate growth percentages
#         growth_pct = [((ty - ly) / ly * 100) if ly > 0 else 0 for ty, ly in zip(this_year, last_year)]
        
#         # Top entities with enhanced data
#         entities = [
#             {'name': 'GDNT', 'reports': 2145, 'queries': 1222, 'change': '+12.5%'},
#             {'name': 'PT006', 'reports': 618, 'queries': 151, 'change': '+8.3%'},
#             {'name': 'PT018', 'reports': 458, 'queries': 201, 'change': '-2.1%'},
#             {'name': 'PT002', 'reports': 162, 'queries': 410, 'change': '+15.7%'},
#             {'name': 'PT004', 'reports': 385, 'queries': 147, 'change': '+5.2%'},
#             {'name': 'PT008', 'reports': 410, 'queries': 119, 'change': '+11.8%'},
#             {'name': 'LM10', 'reports': 258, 'queries': 265, 'change': '-1.5%'},
#             {'name': 'GDPFMIT', 'reports': 327, 'queries': 166, 'change': '+9.4%'},
#             {'name': 'PT020', 'reports': 174, 'queries': 284, 'change': '+3.7%'},
#             {'name': 'PT012', 'reports': 291, 'queries': 117, 'change': '+6.9%'}
#         ]
        
#         # Activity trends with forecasts
#         months_full = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#         reports_trend = [112, 120, 84, 110, 52, 69, 90, 44, 86, 16, 92, 48]
#         queries_trend = [33, 19, 39, 86, 37, 50, 25, 75, 30, 76, 33, 41]
        
#         # Add forecast for next 3 months
#         forecast_months = ['Jan (Forecast)', 'Feb (Forecast)', 'Mar (Forecast)']
#         forecast_reports = [52, 58, 63]
#         forecast_queries = [38, 42, 45]
        
#         return {
#             'active_users': active_users,
#             'inactive_users_90d': inactive_users_90d,
#             'inactive_users_30d': inactive_users_30d,
#             'total_users': total_users,
#             'account_locks': 1493,
#             'queries_reports': 74,
#             'failed_logins': 217,
#             'months': months,
#             'this_year': this_year,
#             'last_year': last_year,
#             'growth_pct': growth_pct,
#             'entities': entities,
#             'months_full': months_full + forecast_months,
#             'reports_trend': reports_trend + forecast_reports,
#             'queries_trend': queries_trend + forecast_queries,
#             'avg_response_time': 234,  # ms
#             'system_uptime': 99.97,  # percentage
#             'active_sessions': 847
#         }

#     data = generate_enhanced_data()

#     # Row 1: Key Metrics with enhanced visualization
#     st.markdown("""
#     <div class="section-header">
#         <span class="material-symbols-outlined">dashboard</span>
#         <h2>Key Performance Indicators</h2>
#     </div>
#     """, unsafe_allow_html=True)

#     # Create 4 columns for metrics
#     kpi_cols = st.columns(4)

#     metrics = [
#         {"icon": "group", "label": "Total Users", "value": f"{data['total_users']:,}", "trend": "+12.3%", "color": "#3182ce"},
#         # {"icon": "lock", "label": "Account Locks", "value": f"{data['account_locks']:,}", "trend": "-5.2%", "color": "#e53e3e"},
#         {"icon": "search", "label": "Queries & Reports", "value": str(data['queries_reports']), "trend": "+8.1%", "color": "#38a169"},
#         {"icon": "speed", "label": "Avg Response", "value": f"{data['avg_response_time']}ms", "trend": "-12ms", "color": "#805ad5"}
#     ]

#     for col, metric in zip(kpi_cols, metrics):
#         with col:
#             st.markdown(f"""
#             <div class="tv-card" style="padding: 1.5rem;">
#                 <div style="display: flex; justify-content: space-between; align-items: flex-start;">
#                     <span class="material-symbols-outlined" style="font-size: 2.5rem; color: {metric['color']}; background: {metric['color']}10; padding: 0.75rem; border-radius: 1rem;">{metric['icon']}</span>
#                     <span class="trend-up" style="font-weight: 600;">{metric['trend']}</span>
#                 </div>
#                 <div style="margin-top: 1rem;">
#                     <div class="stat-value-tv">{metric['value']}</div>
#                     <div class="stat-label-tv">{metric['label']}</div>
#                 </div>
#             </div>
#             """, unsafe_allow_html=True)

#     st.markdown("<br>", unsafe_allow_html=True)

#     # Row 2: Main analytics
#     col1, col2 = st.columns([6, 6])

#     with col1:
#         st.markdown("""
#         <div class="section-header">
#             <span class="material-symbols-outlined">monitoring</span>
#             <h2>User Account Status</h2>
#         </div>
#         """, unsafe_allow_html=True)
        
#         # Enhanced donut chart with better styling
#         fig_donut = go.Figure()
        
#         fig_donut.add_trace(go.Pie(
#             labels=['Active Users', 'Inactive (30d)', 'Inactive (90d)'],
#             values=[data['active_users'], data['inactive_users_30d'], data['inactive_users_90d']],
#             hole=0.6,
#             marker=dict(
#                 colors=['#3182ce', '#90cdf4', '#fbb6ce'],
#                 line=dict(color='white', width=2)
#             ),
#             textinfo='percent',
#             textposition='inside',
#             textfont=dict(size=14, color='white'),
#             hoverinfo='label+value+percent',
#             showlegend=False
#         ))
        
#         fig_donut.update_layout(
#             height=400,
#             margin=dict(l=20, r=20, t=30, b=20),
#             paper_bgcolor='rgba(0,0,0,0)',
#             plot_bgcolor='rgba(0,0,0,0)',
#             annotations=[dict(
#                 text=f"Total<br>{data['total_users']:,}",
#                 x=0.5, y=0.5,
#                 font_size=24,
#                 font_color='#1a202c',
#                 font_weight='bold',
#                 showarrow=False
#             )]
#         )
        
#         st.plotly_chart(fig_donut, use_container_width=True)

#     with col2:
#         st.markdown("""
#         <div class="section-header">
#             <span class="material-symbols-outlined">trending_up</span>
#             <h2>User Growth Trend</h2>
#         </div>
#         """, unsafe_allow_html=True)
        
#         # Enhanced bar chart with gradient
#         fig_growth = go.Figure()
        
#         fig_growth.add_trace(go.Bar(
#             name='This Year',
#             x=data['months'],
#             y=data['this_year'],
#             marker=dict(
#                 color=data['this_year'],
#                 colorscale='Blues',
#                 showscale=False
#             ),
#             text=data['this_year'],
#             textposition='outside',
#             textfont=dict(size=12),
#             hovertemplate='Month: %{x}<br>New Users: %{y}<extra></extra>'
#         ))
        
#         fig_growth.add_trace(go.Bar(
#             name='Last Year',
#             x=data['months'],
#             y=data['last_year'],
#             marker_color='#CBD5E0',
#             text=data['last_year'],
#             textposition='outside',
#             textfont=dict(size=12),
#             hovertemplate='Month: %{x}<br>New Users: %{y}<extra></extra>'
#         ))
        
#         fig_growth.update_layout(
#             barmode='group',
#             height=400,
#             margin=dict(l=40, r=20, t=20, b=40),
#             paper_bgcolor='rgba(0,0,0,0)',
#             plot_bgcolor='rgba(0,0,0,0)',
#             legend=dict(
#                 orientation="h",
#                 yanchor="bottom",
#                 y=1.02,
#                 xanchor="right",
#                 x=1,
#                 font=dict(size=12)
#             ),
#             xaxis=dict(
#                 showgrid=False,
#                 tickfont=dict(size=12, color='#4a5568')
#             ),
#             yaxis=dict(
#                 showgrid=True,
#                 gridcolor='#E2E8F0',
#                 gridwidth=1,
#                 tickfont=dict(size=12, color='#4a5568'),
#                 title=dict(text="New Users", font=dict(size=12))
#             )
#         )
        
#         st.plotly_chart(fig_growth, use_container_width=True)

#     st.markdown("<br>", unsafe_allow_html=True)

#     # Row 3: Detailed analytics
#     col3, col4, col5 = st.columns([4, 3, 5])

#     with col3:
#         st.markdown("""
#         <div class="section-header">
#             <span class="material-symbols-outlined">analytics</span>
#             <h2>Top Active Entities</h2>
#         </div>
#         """, unsafe_allow_html=True)
        
#         st.markdown('<div class="tv-card">', unsafe_allow_html=True)
        
#         # Create a DataFrame for better visualization
#         entities_df = pd.DataFrame(data['entities'])
#         max_total = max([e['reports'] + e['queries'] for e in data['entities']])
        
#         for entity in data['entities']:
#             total = entity['reports'] + entity['queries']
#             width_percent = (total / max_total) * 100
            
#             # Determine change indicator color
#             change_color = "#38a169" if entity['change'].startswith('+') else "#e53e3e"
            
#             st.markdown(f"""
#             <div style="margin-bottom: 1.25rem;">
#                 <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
#                     <div style="display: flex; align-items: center; gap: 0.5rem;">
#                         <span style="font-weight: 600; color: #1a202c;">{entity['name']}</span>
#                         <span style="color: {change_color}; font-size: 0.85rem;">{entity['change']}</span>
#                     </div>
#                     <span style="font-size: 0.9rem; color: #718096;">{total:,} total</span>
#                 </div>
#                 <div style="display: flex; align-items: center; gap: 0.75rem;">
#                     <div class="progress-container">
#                         <div class="progress-fill" style="width: {width_percent}%;"></div>
#                     </div>
#                 </div>
#                 <div style="display: flex; gap: 1rem; margin-top: 0.25rem; font-size: 0.85rem;">
#                     <span style="color: #3182ce;">Reports: {entity['reports']:,}</span>
#                     <span style="color: #718096;">Queries: {entity['queries']:,}</span>
#                 </div>
#             </div>
#             """, unsafe_allow_html=True)
        
#         st.markdown('</div>', unsafe_allow_html=True)

#     with col4:
#         st.markdown("""
#         <div class="section-header">
#             <span class="material-symbols-outlined">pie_chart</span>
#             <h2>Usage Distribution</h2>
#         </div>
#         """, unsafe_allow_html=True)
        
#         # Enhanced donut for usage by type
#         fig_usage = go.Figure()
        
#         fig_usage.add_trace(go.Pie(
#             labels=['Reports', 'Queries'],
#             values=[53, 21],
#             hole=0.6,
#             marker=dict(
#                 colors=['#3182ce', '#63b3ed'],
#                 line=dict(color='white', width=2)
#             ),
#             textinfo='percent',
#             textposition='inside',
#             textfont=dict(size=16, color='white'),
#             hoverinfo='label+value+percent',
#             showlegend=False
#         ))
        
#         fig_usage.update_layout(
#             height=350,
#             margin=dict(l=20, r=20, t=30, b=20),
#             paper_bgcolor='rgba(0,0,0,0)',
#             plot_bgcolor='rgba(0,0,0,0)',
#             annotations=[dict(
#                 text=f"Total<br>{data['queries_reports']}",
#                 x=0.5, y=0.5,
#                 font_size=20,
#                 font_color='#1a202c',
#                 font_weight='bold',
#                 showarrow=False
#             )]
#         )
        
#         st.plotly_chart(fig_usage, use_container_width=True)
        
#         # Additional system metrics
#         st.markdown(f"""
#         <div class="tv-card" style="margin-top: 1rem; padding: 1.25rem;">
#             <div style="display: flex; justify-content: space-around;">
#                 <div style="text-align: center;">
#                     <span class="material-symbols-outlined" style="color: #38a169; font-size: 2rem;">bolt</span>
#                     <div style="font-weight: 600; font-size: 1.5rem;">{data['system_uptime']}%</div>
#                     <div style="color: #718096; font-size: 0.9rem;">Uptime</div>
#                 </div>
#                 <div style="text-align: center;">
#                     <span class="material-symbols-outlined" style="color: #3182ce; font-size: 2rem;">group</span>
#                     <div style="font-weight: 600; font-size: 1.5rem;">{data['active_sessions']}</div>
#                     <div style="color: #718096; font-size: 0.9rem;">Active Sessions</div>
#                 </div>
#             </div>
#         </div>
#         """, unsafe_allow_html=True)

#     with col5:
#         st.markdown("""
#         <div class="section-header">
#             <span class="material-symbols-outlined">show_chart</span>
#             <h2>Activity Trends & Forecast</h2>
#         </div>
#         """, unsafe_allow_html=True)
        
#         # Enhanced line chart with forecast
#         fig_trends = go.Figure()
        
#         # Historical data
#         fig_trends.add_trace(go.Scatter(
#             x=data['months_full'][:12],
#             y=data['reports_trend'][:12],
#             name='Reports (Actual)',
#             line=dict(color='#3182ce', width=3),
#             mode='lines+markers',
#             marker=dict(size=8, symbol='circle'),
#             hovertemplate='Month: %{x}<br>Reports: %{y}<extra></extra>'
#         ))
        
#         fig_trends.add_trace(go.Scatter(
#             x=data['months_full'][:12],
#             y=data['queries_trend'][:12],
#             name='Queries (Actual)',
#             line=dict(color='#63b3ed', width=3),
#             mode='lines+markers',
#             marker=dict(size=8, symbol='circle'),
#             hovertemplate='Month: %{x}<br>Queries: %{y}<extra></extra>'
#         ))
        
#         # Forecast data (dashed lines)
#         fig_trends.add_trace(go.Scatter(
#             x=data['months_full'][11:],
#             y=data['reports_trend'][11:],
#             name='Reports (Forecast)',
#             line=dict(color='#3182ce', width=3, dash='dash'),
#             mode='lines+markers',
#             marker=dict(size=8, symbol='circle-open'),
#             hovertemplate='Month: %{x}<br>Forecast: %{y}<extra></extra>'
#         ))
        
#         fig_trends.add_trace(go.Scatter(
#             x=data['months_full'][11:],
#             y=data['queries_trend'][11:],
#             name='Queries (Forecast)',
#             line=dict(color='#63b3ed', width=3, dash='dash'),
#             mode='lines+markers',
#             marker=dict(size=8, symbol='circle-open'),
#             hovertemplate='Month: %{x}<br>Forecast: %{y}<extra></extra>'
#         ))
        
#         fig_trends.update_layout(
#             height=400,
#             margin=dict(l=40, r=20, t=20, b=40),
#             paper_bgcolor='rgba(0,0,0,0)',
#             plot_bgcolor='rgba(0,0,0,0)',
#             legend=dict(
#                 orientation="h",
#                 yanchor="bottom",
#                 y=1.02,
#                 xanchor="center",
#                 x=0.5,
#                 font=dict(size=12),
#                 bgcolor='rgba(255,255,255,0.8)',
#                 bordercolor='#E2E8F0',
#                 borderwidth=1
#             ),
#             xaxis=dict(
#                 showgrid=False,
#                 tickfont=dict(size=11, color='#4a5568'),
#                 tickangle=45
#             ),
#             yaxis=dict(
#                 showgrid=True,
#                 gridcolor='#E2E8F0',
#                 gridwidth=1,
#                 tickfont=dict(size=11, color='#4a5568'),
#                 title=dict(text="Activity Count", font=dict(size=12))
#             ),
#             hovermode='x unified'
#         )
        
#         st.plotly_chart(fig_trends, use_container_width=True)

#     # Footer with system status
#     st.markdown(f"""
#     <div class="tv-footer">
#         <div style="display: flex; align-items: center; gap: 2rem;">
#             <span>© FMIS · Developed by OIM Team</span>
#             <span style="display: flex; align-items: center; gap: 1rem;">
#                 <span style="display: flex; align-items: center; gap: 0.25rem;">
#                     <span style="width: 0.5rem; height: 0.5rem; border-radius: 50%; background-color: #38a169;"></span>
#                     API: 98ms
#                 </span>
#                 <span style="display: flex; align-items: center; gap: 0.25rem;">
#                     <span style="width: 0.5rem; height: 0.5rem; border-radius: 50%; background-color: #38a169;"></span>
#                     DB: 45ms
#                 </span>
#             </span>
#         </div>
#         <div style="display: flex; align-items: center; gap: 1rem;">
#             <span class="status-badge success">
#                 <span class="material-symbols-outlined" style="font-size: 1.25rem;">check_circle</span>
#                 All Systems Operational
#             </span>
#             <span>Last updated: {datetime.now().strftime("%H:%M:%S")}</span>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     # Auto-refresh every 30 seconds for TV display
#     st.markdown("""
#     <script>
#         setTimeout(function(){
#             window.location.reload();
#         }, 30000);
#     </script>
#     """, unsafe_allow_html=True)

# if __name__ == "__main__":
#     Monitoring()



# import streamlit as st
# import plotly.graph_objects as go

# def Monitoring():

#     st.markdown("""
#     <style>
#         @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700&family=DM+Mono:wght@400;500&display=swap');
#         @import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@24,400,1,0');

#         * { font-family: 'DM Sans', sans-serif; box-sizing: border-box; }

#         html, body, .stApp { background: #0b0f1a; color: #e2e8f0; }

#         .block-container {
#             padding: 1.5rem 2rem 1rem 2rem !important;
#             max-width: 100% !important;
#         }

#         #MainMenu, footer, header { visibility: hidden; }
#         .stDeployButton { display: none; }

#         /* HEADER */
#         .dash-header {
#             display: flex; align-items: center; justify-content: space-between;
#             background: linear-gradient(135deg, #111827 0%, #1a2235 100%);
#             border: 1px solid rgba(99,179,237,0.15);
#             border-radius: 1rem;
#             padding: 0.875rem 1.5rem;
#             margin-bottom: 1.5rem;
#             box-shadow: 0 0 40px rgba(49,130,206,0.06);
#         }
#         .dash-logo {
#             width: 2.75rem; height: 2.75rem;
#             border-radius: 0.65rem;
#             background: linear-gradient(135deg, #1e3a5f, #3182ce);
#             display: flex; align-items: center; justify-content: center;
#             font-weight: 700; font-size: 0.9rem; color: #fff;
#             letter-spacing: 0.05em;
#             border: 1px solid rgba(99,179,237,0.3);
#             box-shadow: 0 0 20px rgba(49,130,206,0.25);
#         }
#         .dash-title { font-size: 1rem; font-weight: 600; color: #e2e8f0; letter-spacing: -0.01em; }
#         .dash-subtitle { font-size: 0.75rem; color: #64748b; font-weight: 400; margin-top: 0.1rem; }
#         .live-pill {
#             display: flex; align-items: center; gap: 0.5rem;
#             background: rgba(56,161,105,0.12);
#             border: 1px solid rgba(56,161,105,0.25);
#             border-radius: 9999px;
#             padding: 0.35rem 0.875rem;
#             font-size: 0.75rem; font-weight: 600; color: #68d391;
#             letter-spacing: 0.05em;
#         }
#         .live-dot {
#             width: 0.45rem; height: 0.45rem;
#             border-radius: 9999px; background: #38a169;
#             box-shadow: 0 0 6px #38a169;
#             animation: pulse 2s ease-in-out infinite;
#         }
#         @keyframes pulse {
#             0%, 100% { opacity: 1; box-shadow: 0 0 6px #38a169; }
#             50%       { opacity: 0.6; box-shadow: 0 0 12px #38a169; }
#         }

#         /* SECTION LABEL */
#         .section-label {
#             font-size: 0.65rem; font-weight: 700;
#             text-transform: uppercase; letter-spacing: 0.1em;
#             color: #4a6fa5; margin-bottom: 0.75rem;
#             display: flex; align-items: center; gap: 0.4rem;
#         }
#         .section-label::before {
#             content: ''; display: inline-block;
#             width: 0.2rem; height: 0.8rem;
#             background: #3182ce; border-radius: 2px;
#         }

#         /* METRIC CARDS */
#         .metric-card {
#             background: linear-gradient(145deg, #111827, #1a2235);
#             border: 1px solid rgba(99,179,237,0.1);
#             border-radius: 0.875rem;
#             padding: 1.125rem 1.25rem;
#             margin-bottom: 0.75rem;
#             position: relative; overflow: hidden;
#         }
#         .metric-card::after {
#             content: ''; position: absolute;
#             top: 0; left: 0; right: 0; height: 2px;
#             border-radius: 0.875rem 0.875rem 0 0;
#         }
#         .metric-card.blue::after   { background: linear-gradient(90deg, #3182ce, #63b3ed); }
#         .metric-card.orange::after { background: linear-gradient(90deg, #dd6b20, #f6ad55); }
#         .metric-card.red::after    { background: linear-gradient(90deg, #c53030, #fc8181); }
#         .metric-card.teal::after   { background: linear-gradient(90deg, #2c7a7b, #81e6d9); }

#         .metric-icon { font-family: 'Material Symbols Rounded'; font-size: 1.5rem; line-height: 1; }
#         .metric-icon.blue   { color: #63b3ed; }
#         .metric-icon.orange { color: #f6ad55; }
#         .metric-icon.red    { color: #fc8181; }
#         .metric-icon.teal   { color: #81e6d9; }

#         .metric-value {
#             font-size: 2rem; font-weight: 700;
#             letter-spacing: -0.04em; color: #f7fafc;
#             line-height: 1.1; margin-top: 0.625rem;
#         }
#         .metric-label {
#             font-size: 0.7rem; font-weight: 500;
#             text-transform: uppercase; letter-spacing: 0.06em;
#             color: #4a5568; margin-top: 0.25rem;
#         }

#         /* CHART CARD */
#         .chart-card {
#             background: linear-gradient(145deg, #111827, #1a2235);
#             border: 1px solid rgba(99,179,237,0.1);
#             border-radius: 0.875rem;
#             padding: 1.125rem 1.25rem 0.75rem 1.25rem;
#             margin-bottom: 0.75rem;
#         }
#         .chart-title { font-size: 0.8rem; font-weight: 600; color: #cbd5e0; margin-bottom: 0.25rem; }
#         .chart-meta  { font-size: 0.65rem; color: #4a6fa5; margin-bottom: 0.75rem; }

#         /* LEGEND */
#         .legend-row  { display: flex; gap: 1.25rem; justify-content: center; margin-top: 0.5rem; }
#         .legend-item { display: flex; align-items: center; gap: 0.35rem; font-size: 0.72rem; color: #94a3b8; }
#         .legend-dot  { width: 0.55rem; height: 0.55rem; border-radius: 9999px; }

#         /* FOOTER */
#         .dash-footer {
#             display: flex; justify-content: space-between; align-items: center;
#             padding-top: 0.75rem;
#             border-top: 1px solid rgba(99,179,237,0.08);
#             font-size: 0.65rem; color: #334155; margin-top: 0.5rem;
#         }
#         .footer-status { display: flex; align-items: center; gap: 0.4rem; color: #48bb78; font-weight: 500; }
#     </style>
#     """, unsafe_allow_html=True)

#     # ── DATA ──────────────────────────────────────────────────────────────────
#     @st.cache_data
#     def generate_data():
#         entities      = ['GDNT','PT006','PT018','PT002','PT004','PT008','LM10','GDPFMIT','PT020','PT012']
#         reports       = [2145, 618, 458, 162, 385, 410, 258, 327, 174, 291]
#         queries       = [1222, 151, 201, 410, 147, 119, 265, 166, 284, 117]
#         months_short  = ['S','O','N','D','J','F','M','A','M','J','J','A']
#         this_year     = [52, 68, 45, 82, 55, 70, 65, 92, 63, 80, 72, 100]
#         last_year     = [45, 58, 38, 70, 48, 60, 55, 78, 52, 68, 62, 85]
#         months_full   = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
#         reports_trend = [112, 120, 84, 110, 52, 69, 90, 44, 86, 16, 92, 48]
#         queries_trend = [33,  19,  39,  86, 37, 50, 25, 75, 30, 76, 33, 41]
#         return dict(
#             active=2924, inactive_30=505, inactive_90=899,
#             total_users=4328, account_locks=1493, queries_reports=74, failed_logins=217,
#             entities=entities, reports=reports, queries=queries,
#             months_short=months_short, this_year=this_year, last_year=last_year,
#             months_full=months_full, reports_trend=reports_trend, queries_trend=queries_trend,
#         )

#     d = generate_data()

#     # ── SHARED CHART CONSTANTS ────────────────────────────────────────────────
#     PAPER  = 'rgba(0,0,0,0)'
#     GRID   = 'rgba(99,179,237,0.07)'
#     TICK   = dict(color='#4a6fa5', size=11, family='DM Sans')
#     FONT   = dict(family='DM Sans', color='#94a3b8')
#     LEGEND = dict(
#         orientation='h', yanchor='bottom', y=1.02,
#         xanchor='center', x=0.5,
#         font=dict(size=11, family='DM Sans'),
#         bgcolor='rgba(0,0,0,0)', borderwidth=0,
#     )

#     # ── HEADER ────────────────────────────────────────────────────────────────
#     st.markdown("""
#     <div class="dash-header">
#         <div style="display:flex;align-items:center;gap:1rem;">
#             <div class="dash-logo">FM</div>
#             <div style="height:1.5rem;width:1px;background:rgba(99,179,237,0.15);"></div>
#             <div>
#                 <div class="dash-title">FMIS Monitoring</div>
#                 <div class="dash-subtitle">User &amp; Report Analytics · OIM Team</div>
#             </div>
#         </div>
#         <div class="live-pill"><div class="live-dot"></div>LIVE</div>
#     </div>
#     """, unsafe_allow_html=True)

#     # ══════════════════════════════════════════════════════════════════════════
#     # ROW 1 — Metric cards | Account status donut | New users bar
#     # ══════════════════════════════════════════════════════════════════════════
#     col_m, col_charts = st.columns([2, 5])

#     with col_m:
#         st.markdown('<div class="section-label">Activity Metrics</div>', unsafe_allow_html=True)
#         for icon, color, val, label in [
#             ("group",   "blue",   f"{d['total_users']:,}",  "Total Users"),
#             # ("lock",    "orange", f"{d['account_locks']:,}", "Account Locks"),
#             ("search",  "teal",   str(d['queries_reports']), "Queries & Reports"),
#             ("warning", "red",    str(d['failed_logins']),   "Failed Logins"),
#         ]:
#             st.markdown(f"""
#             <div class="metric-card {color}">
#                 <span class="metric-icon {color}">{icon}</span>
#                 <div class="metric-value">{val}</div>
#                 <div class="metric-label">{label}</div>
#             </div>""", unsafe_allow_html=True)

#     with col_charts:
#         st.markdown('<div class="section-label">User Activity</div>', unsafe_allow_html=True)
#         cc1, cc2 = st.columns(2)

#         # Donut — Account Status
#         with cc1:
#             st.markdown("""
#             <div class="chart-card">
#                 <div class="chart-title">Account Status</div>
#                 <div class="chart-meta">Current period breakdown</div>
#             """, unsafe_allow_html=True)

#             fig_donut = go.Figure()
#             fig_donut.add_trace(go.Pie(
#                 labels=['Active', 'Inactive (30d)', 'Inactive (90d)'],
#                 values=[d['active'], d['inactive_30'], d['inactive_90']],
#                 hole=0.68,
#                 marker=dict(colors=['#3182ce','#63b3ed','#dd6b20'],
#                             line=dict(color='#0b0f1a', width=3)),
#                 textinfo='none', showlegend=False, sort=False,
#                 hovertemplate='<b>%{label}</b><br>%{value:,} users · %{percent}<extra></extra>',
#             ))
#             fig_donut.update_layout(
#                 height=240,
#                 paper_bgcolor=PAPER, plot_bgcolor=PAPER,
#                 margin=dict(l=10, r=10, t=10, b=10),
#                 font=FONT,
#                 annotations=[dict(
#                     text=f'<b>{d["total_users"]:,}</b><br>Users',
#                     x=0.5, y=0.5,
#                     font=dict(size=13, color='#e2e8f0'),
#                     showarrow=False,
#                 )],
#             )
#             st.plotly_chart(fig_donut, use_container_width=True, config={'displayModeBar': False})
#             st.markdown("""
#             <div class="legend-row">
#                 <div class="legend-item"><div class="legend-dot" style="background:#3182ce"></div>Active {:,}</div>
#                 <div class="legend-item"><div class="legend-dot" style="background:#63b3ed"></div>Inactive 30d {:,}</div>
#                 <div class="legend-item"><div class="legend-dot" style="background:#dd6b20"></div>Inactive 90d {:,}</div>
#             </div></div>
#             """.format(d['active'], d['inactive_30'], d['inactive_90']), unsafe_allow_html=True)

#         # Grouped Bar — New Users
#         with cc2:
#             st.markdown("""
#             <div class="chart-card">
#                 <div class="chart-title">New Users · Monthly</div>
#                 <div class="chart-meta">This year vs last year</div>
#             """, unsafe_allow_html=True)

#             fig_bar = go.Figure()
#             fig_bar.add_trace(go.Bar(
#                 x=d['months_short'], y=d['last_year'], name='Last Year',
#                 marker=dict(color='rgba(100,116,139,0.5)', line=dict(width=0)),
#             ))
#             fig_bar.add_trace(go.Bar(
#                 x=d['months_short'], y=d['this_year'], name='This Year',
#                 marker=dict(
#                     color=d['this_year'],
#                     colorscale=[[0,'#1e3a5f'],[1,'#63b3ed']],
#                     showscale=False, line=dict(width=0),
#                 ),
#             ))
#             fig_bar.update_layout(
#                 height=240,
#                 paper_bgcolor=PAPER, plot_bgcolor=PAPER,
#                 margin=dict(l=10, r=10, t=30, b=10),
#                 font=FONT, legend=LEGEND,
#                 barmode='group', bargap=0.25, bargroupgap=0.05,
#                 xaxis=dict(showgrid=False, tickfont=TICK,
#                            tickcolor='rgba(0,0,0,0)', linecolor='rgba(0,0,0,0)'),
#                 yaxis=dict(showgrid=True, gridcolor=GRID, gridwidth=1, tickfont=TICK,
#                            zeroline=False, linecolor='rgba(0,0,0,0)'),
#             )
#             st.plotly_chart(fig_bar, use_container_width=True, config={'displayModeBar': False})
#             st.markdown('</div>', unsafe_allow_html=True)

#     # ══════════════════════════════════════════════════════════════════════════
#     # ROW 2 — Top 10 Entities | Usage type donut | Activity trends
#     # ══════════════════════════════════════════════════════════════════════════
#     col_ent, col_usage, col_trend = st.columns([5, 2, 5])

#     # Horizontal Stacked Bar — Top 10 Entities
#     with col_ent:
#         st.markdown('<div class="section-label">Report Usage Analytics</div>', unsafe_allow_html=True)
#         st.markdown("""
#         <div class="chart-card">
#             <div class="chart-title">Top 10 Active Entities · Reports &amp; Queries</div>
#             <div class="chart-meta">Current month · Sorted by total volume</div>
#         """, unsafe_allow_html=True)

#         entities = d['entities']
#         reports  = d['reports']
#         queries  = d['queries']

#         order      = sorted(range(len(entities)), key=lambda i: reports[i] + queries[i])
#         ent_sorted = [entities[i] for i in order]
#         rep_sorted = [reports[i]  for i in order]
#         qry_sorted = [queries[i]  for i in order]

#         fig_hbar = go.Figure()
#         fig_hbar.add_trace(go.Bar(
#             y=ent_sorted, x=rep_sorted, name='Reports', orientation='h',
#             marker=dict(color='#2b6cb0', line=dict(width=0)),
#             text=[f'{v:,}' for v in rep_sorted],
#             textposition='inside', insidetextanchor='end',
#             textfont=dict(color='#e2e8f0', size=11, family='DM Mono'),
#             hovertemplate='<b>%{y}</b><br>Reports: %{x:,}<extra></extra>',
#         ))
#         fig_hbar.add_trace(go.Bar(
#             y=ent_sorted, x=qry_sorted, name='Queries', orientation='h',
#             marker=dict(color='#63b3ed', line=dict(width=0)),
#             text=[f'{v:,}' for v in qry_sorted],
#             textposition='inside', insidetextanchor='end',
#             textfont=dict(color='#1a2235', size=11, family='DM Mono'),
#             hovertemplate='<b>%{y}</b><br>Queries: %{x:,}<extra></extra>',
#         ))
#         fig_hbar.update_layout(
#             height=360,
#             paper_bgcolor=PAPER, plot_bgcolor=PAPER,
#             margin=dict(l=80, r=20, t=30, b=10),
#             font=FONT, legend=LEGEND,
#             barmode='stack', bargap=0.25,
#             xaxis=dict(showgrid=True, gridcolor=GRID, gridwidth=1,
#                        tickfont=TICK, zeroline=False,
#                        linecolor='rgba(0,0,0,0)', tickformat=','),
#             yaxis=dict(showgrid=False,
#                        tickfont=dict(color='#94a3b8', size=12, family='DM Mono'),
#                        linecolor='rgba(0,0,0,0)', categoryorder='total ascending'),
#         )
#         st.plotly_chart(fig_hbar, use_container_width=True, config={'displayModeBar': False})
#         st.markdown("""
#         <div class="legend-row" style="margin-bottom:0.25rem">
#             <div class="legend-item"><div class="legend-dot" style="background:#2b6cb0"></div>Reports</div>
#             <div class="legend-item"><div class="legend-dot" style="background:#63b3ed"></div>Queries</div>
#         </div></div>
#         """, unsafe_allow_html=True)

#     # Donut — Usage by Type
#     with col_usage:
#         st.markdown('<div class="section-label">Usage Type</div>', unsafe_allow_html=True)
#         st.markdown("""
#         <div class="chart-card">
#             <div class="chart-title">Usage by Type</div>
#             <div class="chart-meta">Reports vs Queries</div>
#         """, unsafe_allow_html=True)

#         fig_type = go.Figure()
#         fig_type.add_trace(go.Pie(
#             labels=['Reports', 'Queries'], values=[53, 21],
#             hole=0.68,
#             marker=dict(colors=['#2b6cb0','#63b3ed'],
#                         line=dict(color='#0b0f1a', width=3)),
#             textinfo='none', showlegend=False,
#             hovertemplate='<b>%{label}</b><br>%{value} · %{percent}<extra></extra>',
#         ))
#         fig_type.update_layout(
#             height=220,
#             paper_bgcolor=PAPER, plot_bgcolor=PAPER,
#             margin=dict(l=10, r=10, t=10, b=10),
#             font=FONT,
#             annotations=[dict(
#                 text='<b>74</b><br>Total',
#                 x=0.5, y=0.5,
#                 font=dict(size=13, color='#e2e8f0'),
#                 showarrow=False,
#             )],
#         )
#         st.plotly_chart(fig_type, use_container_width=True, config={'displayModeBar': False})
#         st.markdown("""
#         <div class="legend-row" style="flex-direction:column;align-items:center;gap:0.5rem;margin-bottom:0.5rem">
#             <div class="legend-item">
#                 <div class="legend-dot" style="background:#2b6cb0;width:0.75rem;height:0.75rem"></div>
#                 Reports &nbsp;<b style="color:#e2e8f0">53</b>
#             </div>
#             <div class="legend-item">
#                 <div class="legend-dot" style="background:#63b3ed;width:0.75rem;height:0.75rem"></div>
#                 Queries &nbsp;<b style="color:#e2e8f0">21</b>
#             </div>
#         </div></div>
#         """, unsafe_allow_html=True)

#     # Line chart — Activity Trends
#     with col_trend:
#         st.markdown('<div class="section-label">Activity Trends</div>', unsafe_allow_html=True)
#         st.markdown("""
#         <div class="chart-card">
#             <div class="chart-title">Monthly Activity Trends</div>
#             <div class="chart-meta">Reports &amp; Queries over the year</div>
#         """, unsafe_allow_html=True)

#         fig_trend = go.Figure()
#         fig_trend.add_trace(go.Scatter(
#             x=d['months_full'], y=d['reports_trend'], name='Reports',
#             line=dict(color='#3182ce', width=2.5, shape='spline', smoothing=0.8),
#             mode='lines+markers',
#             marker=dict(size=6, color='#3182ce', line=dict(width=2, color='#0b0f1a')),
#             fill='tozeroy', fillcolor='rgba(49,130,206,0.07)',
#             hovertemplate='%{x}<br>Reports: <b>%{y}</b><extra></extra>',
#         ))
#         fig_trend.add_trace(go.Scatter(
#             x=d['months_full'], y=d['queries_trend'], name='Queries',
#             line=dict(color='#63b3ed', width=2.5, shape='spline', smoothing=0.8, dash='dot'),
#             mode='lines+markers',
#             marker=dict(size=6, color='#63b3ed', line=dict(width=2, color='#0b0f1a')),
#             fill='tozeroy', fillcolor='rgba(99,179,237,0.05)',
#             hovertemplate='%{x}<br>Queries: <b>%{y}</b><extra></extra>',
#         ))
#         fig_trend.update_layout(
#             height=360,
#             paper_bgcolor=PAPER, plot_bgcolor=PAPER,
#             margin=dict(l=10, r=10, t=30, b=10),
#             font=FONT, legend=LEGEND,
#             hovermode='x unified',
#             xaxis=dict(showgrid=False, tickfont=TICK,
#                        linecolor='rgba(0,0,0,0)', tickcolor='rgba(0,0,0,0)'),
#             yaxis=dict(showgrid=True, gridcolor=GRID, gridwidth=1, tickfont=TICK,
#                        zeroline=False, linecolor='rgba(0,0,0,0)'),
#         )
#         st.plotly_chart(fig_trend, use_container_width=True, config={'displayModeBar': False})
#         st.markdown('</div>', unsafe_allow_html=True)

#     # ── FOOTER ────────────────────────────────────────────────────────────────
#     st.markdown("""
#     <div class="dash-footer">
#         <span>© FMIS · Developed and prepared by OIM Team</span>
#         <div class="footer-status">
#             <div class="live-dot" style="width:0.35rem;height:0.35rem"></div>
#             All systems operational
#         </div>
#     </div>
#     """, unsafe_allow_html=True)


# if __name__ == "__main__":
#     st.set_page_config(layout="wide", page_title="FMIS Monitoring", page_icon="📊")
#     Monitoring()










# import streamlit as st
# import plotly.graph_objects as go
# import plotly.express as px
# import pandas as pd
# import numpy as np
# from datetime import datetime, timedelta

# def Monitoring():
#     # Page config for better TV display
#     # st.set_page_config(
#     #     page_title="FMIS Monitoring Dashboard",
#     #     layout="wide",
#     #     initial_sidebar_state="collapsed"
#     # )

#     # Custom CSS for TV-optimized professional dashboard
#     st.markdown("""
#     <style>
#         /* Import fonts */
#         @import url('https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap');
#         @import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0,0');
        
#         * {
#             font-family: 'Inter', sans-serif;
#             margin: 0;
#             padding: 0;
#             box-sizing: border-box;
#         }
        
#         /* Main container for TV */
#         .stApp {
#             background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
#             min-height: 100vh;
#             padding: 1rem;
#         }
        
#         /* Hide Streamlit branding for cleaner look */
#         #MainMenu {visibility: hidden;}
#         footer {visibility: hidden;}
#         header {visibility: hidden;}
        
#         /* Main container adjustments */
#         .block-container {
#             padding: 0.5rem 1rem;
#             max-width: 1920px;
#             margin: 0 auto;
#         }
        
#         /* Professional card design */
#         .tv-card {
#             background: rgba(255, 255, 255, 0.95);
#             backdrop-filter: blur(10px);
#             border: 1px solid rgba(226, 232, 240, 0.8);
#             border-radius: 1.5rem;
#             padding: 1.5rem;
#             box-shadow: 0 20px 40px -15px rgba(0,0,0,0.15), 
#                         0 0 0 1px rgba(0,0,0,0.02) inset;
#             transition: transform 0.2s ease, box-shadow 0.2s ease;
#             height: 100%;
#         }
        
#         .tv-card:hover {
#             transform: translateY(-2px);
#             box-shadow: 0 25px 50px -15px rgba(0,0,0,0.25);
#         }
        
#         /* Metric cards with gradients */
#         .metric-card {
#             background: linear-gradient(145deg, #ffffff, #f8fafc);
#             border-radius: 1.25rem;
#             padding: 1.75rem 1.5rem;
#             border: 1px solid rgba(226, 232, 240, 0.6);
#             box-shadow: 0 8px 20px -10px rgba(0,0,0,0.1);
#             transition: all 0.2s ease;
#         }
        
#         .metric-card:hover {
#             border-color: #3182ce;
#             box-shadow: 0 12px 25px -10px #3182ce40;
#         }
        
#         /* Large stat values for TV viewing */
#         .stat-value-tv {
#             font-size: 3rem;
#             font-weight: 700;
#             letter-spacing: -0.03em;
#             background: linear-gradient(135deg, #1a202c, #2d3748);
#             -webkit-background-clip: text;
#             -webkit-text-fill-color: transparent;
#             line-height: 1.2;
#         }
        
#         .stat-label-tv {
#             font-size: 1rem;
#             font-weight: 500;
#             color: #718096;
#             text-transform: uppercase;
#             letter-spacing: 0.05em;
#             margin-top: 0.5rem;
#         }
        
#         /* Section headers */
#         .section-header {
#             display: flex;
#             align-items: center;
#             gap: 0.75rem;
#             margin-bottom: 1.5rem;
#             padding-bottom: 0.75rem;
#             border-bottom: 2px solid #e2e8f0;
#         }
        
#         .section-header h2 {
#             font-size: 1.35rem;
#             font-weight: 600;
#             color: #1a202c;
#             margin: 0;
#         }
        
#         .section-header .material-symbols-outlined {
#             font-size: 2rem;
#             color: #3182ce;
#             background: rgba(49, 130, 206, 0.1);
#             padding: 0.5rem;
#             border-radius: 12px;
#         }
        
#         /* Status badges */
#         .status-badge {
#             display: inline-flex;
#             align-items: center;
#             gap: 0.5rem;
#             padding: 0.5rem 1rem;
#             border-radius: 100px;
#             font-weight: 600;
#             font-size: 0.9rem;
#             background: white;
#             border: 1px solid #e2e8f0;
#         }
        
#         .status-badge.live {
#             background: #f0f9ff;
#             border-color: #3182ce;
#             color: #3182ce;
#         }
        
#         .status-badge.success {
#             background: #f0fdf4;
#             border-color: #38a169;
#             color: #38a169;
#         }
        
#         /* Progress bar enhancements */
#         .progress-container {
#             background: #edf2f7;
#             height: 0.75rem;
#             border-radius: 100px;
#             overflow: hidden;
#             flex: 1;
#         }
        
#         .progress-fill {
#             height: 100%;
#             border-radius: 100px;
#             background: linear-gradient(90deg, #3182ce, #63b3ed);
#             transition: width 0.3s ease;
#         }
        
#         /* Footer styling */
#         .tv-footer {
#             margin-top: 2rem;
#             padding: 1.25rem 2rem;
#             background: rgba(255,255,255,0.9);
#             backdrop-filter: blur(10px);
#             border-radius: 1.25rem;
#             border: 1px solid #e2e8f0;
#             display: flex;
#             justify-content: space-between;
#             align-items: center;
#             font-size: 0.95rem;
#             color: #64748b;
#         }
        
#         /* KPI indicators */
#         .kpi-indicator {
#             display: flex;
#             align-items: center;
#             gap: 0.5rem;
#             font-size: 0.9rem;
#             padding: 0.35rem 1rem;
#             background: #f8fafc;
#             border-radius: 100px;
#             border: 1px solid #e2e8f0;
#         }
        
#         .trend-up { color: #38a169; }
#         .trend-down { color: #e53e3e; }
        
#         /* Responsive adjustments for TV */
#         @media (min-width: 1600px) {
#             .stat-value-tv { font-size: 3.5rem; }
#             .section-header h2 { font-size: 1.5rem; }
#         }
#     </style>
#     """, unsafe_allow_html=True)

#     # Top header with live status and timestamp
#     current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
#     st.markdown(f"""
#     <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem; background: white; padding: 1rem 2rem; border-radius: 100px; border: 1px solid #e2e8f0; box-shadow: 0 4px 12px -6px rgba(0,0,0,0.1);">
#         <div style="display: flex; align-items: center; gap: 2rem;">
#             <div style="display: flex; align-items: center; gap: 1rem;">
#                 <div style="width: 3rem; height: 3rem; background: linear-gradient(135deg, #1a202c, #3182ce); border-radius: 1rem; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; font-size: 1.2rem;">FM</div>
#                 <span style="font-weight: 600; color: #1a202c; font-size: 1.25rem;">FMIS Analytics</span>
#             </div>
#             <span class="status-badge live">
#                 <span class="material-symbols-outlined" style="font-size: 1.25rem;">fiber_manual_record</span>
#                 LIVE MONITORING
#             </span>
#         </div>
#         <div style="display: flex; align-items: center; gap: 2rem;">
#             <div class="kpi-indicator">
#                 <span class="material-symbols-outlined" style="color: #3182ce;">update</span>
#                 {current_time}
#             </div>
#             <div class="kpi-indicator">
#                 <span class="material-symbols-outlined" style="color: #38a169;">check_circle</span>
#                 System OK
#             </div>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     # Generate enhanced sample data
#     @st.cache_data(ttl=300)  # Cache for 5 minutes
#     def generate_enhanced_data():
#         # Enhanced metrics
#         active_users = 2924
#         inactive_users_90d = 899
#         inactive_users_30d = 505
#         total_users = active_users + inactive_users_90d + inactive_users_30d
        
#         # Monthly trends with growth indicators
#         months = ['Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug']
#         this_year = [52, 68, 45, 82, 55, 70, 65, 92, 63, 80, 72, 100]
#         last_year = [45, 58, 38, 70, 48, 60, 55, 78, 52, 68, 62, 85]
        
#         # Calculate growth percentages
#         growth_pct = [((ty - ly) / ly * 100) if ly > 0 else 0 for ty, ly in zip(this_year, last_year)]
        
#         # Top entities with enhanced data
#         entities = [
#             {'name': 'GDNT', 'reports': 2145, 'queries': 1222, 'change': '+12.5%'},
#             {'name': 'PT006', 'reports': 618, 'queries': 151, 'change': '+8.3%'},
#             {'name': 'PT018', 'reports': 458, 'queries': 201, 'change': '-2.1%'},
#             {'name': 'PT002', 'reports': 162, 'queries': 410, 'change': '+15.7%'},
#             {'name': 'PT004', 'reports': 385, 'queries': 147, 'change': '+5.2%'},
#             {'name': 'PT008', 'reports': 410, 'queries': 119, 'change': '+11.8%'},
#             {'name': 'LM10', 'reports': 258, 'queries': 265, 'change': '-1.5%'},
#             {'name': 'GDPFMIT', 'reports': 327, 'queries': 166, 'change': '+9.4%'},
#             {'name': 'PT020', 'reports': 174, 'queries': 284, 'change': '+3.7%'},
#             {'name': 'PT012', 'reports': 291, 'queries': 117, 'change': '+6.9%'}
#         ]
        
#         # Activity trends with forecasts
#         months_full = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#         reports_trend = [112, 120, 84, 110, 52, 69, 90, 44, 86, 16, 92, 48]
#         queries_trend = [33, 19, 39, 86, 37, 50, 25, 75, 30, 76, 33, 41]
        
#         # Add forecast for next 3 months
#         forecast_months = ['Jan (Forecast)', 'Feb (Forecast)', 'Mar (Forecast)']
#         forecast_reports = [52, 58, 63]
#         forecast_queries = [38, 42, 45]
        
#         return {
#             'active_users': active_users,
#             'inactive_users_90d': inactive_users_90d,
#             'inactive_users_30d': inactive_users_30d,
#             'total_users': total_users,
#             'account_locks': 1493,
#             'queries_reports': 74,
#             'failed_logins': 217,
#             'months': months,
#             'this_year': this_year,
#             'last_year': last_year,
#             'growth_pct': growth_pct,
#             'entities': entities,
#             'months_full': months_full + forecast_months,
#             'reports_trend': reports_trend + forecast_reports,
#             'queries_trend': queries_trend + forecast_queries,
#             'avg_response_time': 234,  # ms
#             'system_uptime': 99.97,  # percentage
#             'active_sessions': 847
#         }

#     data = generate_enhanced_data()

#     # Row 1: Key Metrics with enhanced visualization
#     st.markdown("""
#     <div class="section-header">
#         <span class="material-symbols-outlined">dashboard</span>
#         <h2>Key Performance Indicators</h2>
#     </div>
#     """, unsafe_allow_html=True)

#     # Create 4 columns for metrics
#     kpi_cols = st.columns(4)

#     metrics = [
#         {"icon": "group", "label": "Total Users", "value": f"{data['total_users']:,}", "trend": "+12.3%", "color": "#3182ce"},
#         # {"icon": "lock", "label": "Account Locks", "value": f"{data['account_locks']:,}", "trend": "-5.2%", "color": "#e53e3e"},
#         {"icon": "search", "label": "Queries & Reports", "value": str(data['queries_reports']), "trend": "+8.1%", "color": "#38a169"},
#         {"icon": "speed", "label": "Avg Response", "value": f"{data['avg_response_time']}ms", "trend": "-12ms", "color": "#805ad5"}
#     ]

#     for col, metric in zip(kpi_cols, metrics):
#         with col:
#             st.markdown(f"""
#             <div class="tv-card" style="padding: 1.5rem;">
#                 <div style="display: flex; justify-content: space-between; align-items: flex-start;">
#                     <span class="material-symbols-outlined" style="font-size: 2.5rem; color: {metric['color']}; background: {metric['color']}10; padding: 0.75rem; border-radius: 1rem;">{metric['icon']}</span>
#                     <span class="trend-up" style="font-weight: 600;">{metric['trend']}</span>
#                 </div>
#                 <div style="margin-top: 1rem;">
#                     <div class="stat-value-tv">{metric['value']}</div>
#                     <div class="stat-label-tv">{metric['label']}</div>
#                 </div>
#             </div>
#             """, unsafe_allow_html=True)

#     st.markdown("<br>", unsafe_allow_html=True)

#     # Row 2: Main analytics
#     col1, col2 = st.columns([6, 6])

#     with col1:
#         st.markdown("""
#         <div class="section-header">
#             <span class="material-symbols-outlined">monitoring</span>
#             <h2>User Account Status</h2>
#         </div>
#         """, unsafe_allow_html=True)
        
#         # Enhanced donut chart with better styling
#         fig_donut = go.Figure()
        
#         fig_donut.add_trace(go.Pie(
#             labels=['Active Users', 'Inactive (30d)', 'Inactive (90d)'],
#             values=[data['active_users'], data['inactive_users_30d'], data['inactive_users_90d']],
#             hole=0.6,
#             marker=dict(
#                 colors=['#3182ce', '#90cdf4', '#fbb6ce'],
#                 line=dict(color='white', width=2)
#             ),
#             textinfo='percent',
#             textposition='inside',
#             textfont=dict(size=14, color='white'),
#             hoverinfo='label+value+percent',
#             showlegend=False
#         ))
        
#         fig_donut.update_layout(
#             height=400,
#             margin=dict(l=20, r=20, t=30, b=20),
#             paper_bgcolor='rgba(0,0,0,0)',
#             plot_bgcolor='rgba(0,0,0,0)',
#             annotations=[dict(
#                 text=f"Total<br>{data['total_users']:,}",
#                 x=0.5, y=0.5,
#                 font_size=24,
#                 font_color='#1a202c',
#                 font_weight='bold',
#                 showarrow=False
#             )]
#         )
        
#         st.plotly_chart(fig_donut, use_container_width=True)

#     with col2:
#         st.markdown("""
#         <div class="section-header">
#             <span class="material-symbols-outlined">trending_up</span>
#             <h2>User Growth Trend</h2>
#         </div>
#         """, unsafe_allow_html=True)
        
#         # Enhanced bar chart with gradient
#         fig_growth = go.Figure()
        
#         fig_growth.add_trace(go.Bar(
#             name='This Year',
#             x=data['months'],
#             y=data['this_year'],
#             marker=dict(
#                 color=data['this_year'],
#                 colorscale='Blues',
#                 showscale=False
#             ),
#             text=data['this_year'],
#             textposition='outside',
#             textfont=dict(size=12),
#             hovertemplate='Month: %{x}<br>New Users: %{y}<extra></extra>'
#         ))
        
#         fig_growth.add_trace(go.Bar(
#             name='Last Year',
#             x=data['months'],
#             y=data['last_year'],
#             marker_color='#CBD5E0',
#             text=data['last_year'],
#             textposition='outside',
#             textfont=dict(size=12),
#             hovertemplate='Month: %{x}<br>New Users: %{y}<extra></extra>'
#         ))
        
#         fig_growth.update_layout(
#             barmode='group',
#             height=400,
#             margin=dict(l=40, r=20, t=20, b=40),
#             paper_bgcolor='rgba(0,0,0,0)',
#             plot_bgcolor='rgba(0,0,0,0)',
#             legend=dict(
#                 orientation="h",
#                 yanchor="bottom",
#                 y=1.02,
#                 xanchor="right",
#                 x=1,
#                 font=dict(size=12)
#             ),
#             xaxis=dict(
#                 showgrid=False,
#                 tickfont=dict(size=12, color='#4a5568')
#             ),
#             yaxis=dict(
#                 showgrid=True,
#                 gridcolor='#E2E8F0',
#                 gridwidth=1,
#                 tickfont=dict(size=12, color='#4a5568'),
#                 title=dict(text="New Users", font=dict(size=12))
#             )
#         )
        
#         st.plotly_chart(fig_growth, use_container_width=True)

#     st.markdown("<br>", unsafe_allow_html=True)

#     # Row 3: Detailed analytics
#     col3, col4, col5 = st.columns([4, 3, 5])

#     with col3:
#         st.markdown("""
#         <div class="section-header">
#             <span class="material-symbols-outlined">analytics</span>
#             <h2>Top Active Entities</h2>
#         </div>
#         """, unsafe_allow_html=True)
        
#         st.markdown('<div class="tv-card">', unsafe_allow_html=True)
        
#         # Create a DataFrame for better visualization
#         entities_df = pd.DataFrame(data['entities'])
#         max_total = max([e['reports'] + e['queries'] for e in data['entities']])
        
#         for entity in data['entities']:
#             total = entity['reports'] + entity['queries']
#             width_percent = (total / max_total) * 100
            
#             # Determine change indicator color
#             change_color = "#38a169" if entity['change'].startswith('+') else "#e53e3e"
            
#             st.markdown(f"""
#             <div style="margin-bottom: 1.25rem;">
#                 <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
#                     <div style="display: flex; align-items: center; gap: 0.5rem;">
#                         <span style="font-weight: 600; color: #1a202c;">{entity['name']}</span>
#                         <span style="color: {change_color}; font-size: 0.85rem;">{entity['change']}</span>
#                     </div>
#                     <span style="font-size: 0.9rem; color: #718096;">{total:,} total</span>
#                 </div>
#                 <div style="display: flex; align-items: center; gap: 0.75rem;">
#                     <div class="progress-container">
#                         <div class="progress-fill" style="width: {width_percent}%;"></div>
#                     </div>
#                 </div>
#                 <div style="display: flex; gap: 1rem; margin-top: 0.25rem; font-size: 0.85rem;">
#                     <span style="color: #3182ce;">Reports: {entity['reports']:,}</span>
#                     <span style="color: #718096;">Queries: {entity['queries']:,}</span>
#                 </div>
#             </div>
#             """, unsafe_allow_html=True)
        
#         st.markdown('</div>', unsafe_allow_html=True)

#     with col4:
#         st.markdown("""
#         <div class="section-header">
#             <span class="material-symbols-outlined">pie_chart</span>
#             <h2>Usage Distribution</h2>
#         </div>
#         """, unsafe_allow_html=True)
        
#         # Enhanced donut for usage by type
#         fig_usage = go.Figure()
        
#         fig_usage.add_trace(go.Pie(
#             labels=['Reports', 'Queries'],
#             values=[53, 21],
#             hole=0.6,
#             marker=dict(
#                 colors=['#3182ce', '#63b3ed'],
#                 line=dict(color='white', width=2)
#             ),
#             textinfo='percent',
#             textposition='inside',
#             textfont=dict(size=16, color='white'),
#             hoverinfo='label+value+percent',
#             showlegend=False
#         ))
        
#         fig_usage.update_layout(
#             height=350,
#             margin=dict(l=20, r=20, t=30, b=20),
#             paper_bgcolor='rgba(0,0,0,0)',
#             plot_bgcolor='rgba(0,0,0,0)',
#             annotations=[dict(
#                 text=f"Total<br>{data['queries_reports']}",
#                 x=0.5, y=0.5,
#                 font_size=20,
#                 font_color='#1a202c',
#                 font_weight='bold',
#                 showarrow=False
#             )]
#         )
        
#         st.plotly_chart(fig_usage, use_container_width=True)
        
#         # Additional system metrics
#         st.markdown(f"""
#         <div class="tv-card" style="margin-top: 1rem; padding: 1.25rem;">
#             <div style="display: flex; justify-content: space-around;">
#                 <div style="text-align: center;">
#                     <span class="material-symbols-outlined" style="color: #38a169; font-size: 2rem;">bolt</span>
#                     <div style="font-weight: 600; font-size: 1.5rem;">{data['system_uptime']}%</div>
#                     <div style="color: #718096; font-size: 0.9rem;">Uptime</div>
#                 </div>
#                 <div style="text-align: center;">
#                     <span class="material-symbols-outlined" style="color: #3182ce; font-size: 2rem;">group</span>
#                     <div style="font-weight: 600; font-size: 1.5rem;">{data['active_sessions']}</div>
#                     <div style="color: #718096; font-size: 0.9rem;">Active Sessions</div>
#                 </div>
#             </div>
#         </div>
#         """, unsafe_allow_html=True)

#     with col5:
#         st.markdown("""
#         <div class="section-header">
#             <span class="material-symbols-outlined">show_chart</span>
#             <h2>Activity Trends & Forecast</h2>
#         </div>
#         """, unsafe_allow_html=True)
        
#         # Enhanced line chart with forecast
#         fig_trends = go.Figure()
        
#         # Historical data
#         fig_trends.add_trace(go.Scatter(
#             x=data['months_full'][:12],
#             y=data['reports_trend'][:12],
#             name='Reports (Actual)',
#             line=dict(color='#3182ce', width=3),
#             mode='lines+markers',
#             marker=dict(size=8, symbol='circle'),
#             hovertemplate='Month: %{x}<br>Reports: %{y}<extra></extra>'
#         ))
        
#         fig_trends.add_trace(go.Scatter(
#             x=data['months_full'][:12],
#             y=data['queries_trend'][:12],
#             name='Queries (Actual)',
#             line=dict(color='#63b3ed', width=3),
#             mode='lines+markers',
#             marker=dict(size=8, symbol='circle'),
#             hovertemplate='Month: %{x}<br>Queries: %{y}<extra></extra>'
#         ))
        
#         # Forecast data (dashed lines)
#         fig_trends.add_trace(go.Scatter(
#             x=data['months_full'][11:],
#             y=data['reports_trend'][11:],
#             name='Reports (Forecast)',
#             line=dict(color='#3182ce', width=3, dash='dash'),
#             mode='lines+markers',
#             marker=dict(size=8, symbol='circle-open'),
#             hovertemplate='Month: %{x}<br>Forecast: %{y}<extra></extra>'
#         ))
        
#         fig_trends.add_trace(go.Scatter(
#             x=data['months_full'][11:],
#             y=data['queries_trend'][11:],
#             name='Queries (Forecast)',
#             line=dict(color='#63b3ed', width=3, dash='dash'),
#             mode='lines+markers',
#             marker=dict(size=8, symbol='circle-open'),
#             hovertemplate='Month: %{x}<br>Forecast: %{y}<extra></extra>'
#         ))
        
#         fig_trends.update_layout(
#             height=400,
#             margin=dict(l=40, r=20, t=20, b=40),
#             paper_bgcolor='rgba(0,0,0,0)',
#             plot_bgcolor='rgba(0,0,0,0)',
#             legend=dict(
#                 orientation="h",
#                 yanchor="bottom",
#                 y=1.02,
#                 xanchor="center",
#                 x=0.5,
#                 font=dict(size=12),
#                 bgcolor='rgba(255,255,255,0.8)',
#                 bordercolor='#E2E8F0',
#                 borderwidth=1
#             ),
#             xaxis=dict(
#                 showgrid=False,
#                 tickfont=dict(size=11, color='#4a5568'),
#                 tickangle=45
#             ),
#             yaxis=dict(
#                 showgrid=True,
#                 gridcolor='#E2E8F0',
#                 gridwidth=1,
#                 tickfont=dict(size=11, color='#4a5568'),
#                 title=dict(text="Activity Count", font=dict(size=12))
#             ),
#             hovermode='x unified'
#         )
        
#         st.plotly_chart(fig_trends, use_container_width=True)

#     # Footer with system status
#     st.markdown(f"""
#     <div class="tv-footer">
#         <div style="display: flex; align-items: center; gap: 2rem;">
#             <span>© FMIS · Developed by OIM Team</span>
#             <span style="display: flex; align-items: center; gap: 1rem;">
#                 <span style="display: flex; align-items: center; gap: 0.25rem;">
#                     <span style="width: 0.5rem; height: 0.5rem; border-radius: 50%; background-color: #38a169;"></span>
#                     API: 98ms
#                 </span>
#                 <span style="display: flex; align-items: center; gap: 0.25rem;">
#                     <span style="width: 0.5rem; height: 0.5rem; border-radius: 50%; background-color: #38a169;"></span>
#                     DB: 45ms
#                 </span>
#             </span>
#         </div>
#         <div style="display: flex; align-items: center; gap: 1rem;">
#             <span class="status-badge success">
#                 <span class="material-symbols-outlined" style="font-size: 1.25rem;">check_circle</span>
#                 All Systems Operational
#             </span>
#             <span>Last updated: {datetime.now().strftime("%H:%M:%S")}</span>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     # Auto-refresh every 30 seconds for TV display
#     st.markdown("""
#     <script>
#         setTimeout(function(){
#             window.location.reload();
#         }, 30000);
#     </script>
#     """, unsafe_allow_html=True)

# if __name__ == "__main__":
#     Monitoring()



# import streamlit as st
# import plotly.graph_objects as go

# def Monitoring():

#     st.markdown("""
#     <style>
#         @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700&family=DM+Mono:wght@400;500&display=swap');
#         @import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@24,400,1,0');

#         * { font-family: 'DM Sans', sans-serif; box-sizing: border-box; }

#         html, body, .stApp { background: #0b0f1a; color: #e2e8f0; }

#         .block-container {
#             padding: 1.5rem 2rem 1rem 2rem !important;
#             max-width: 100% !important;
#         }

#         #MainMenu, footer, header { visibility: hidden; }
#         .stDeployButton { display: none; }

#         /* HEADER */
#         .dash-header {
#             display: flex; align-items: center; justify-content: space-between;
#             background: linear-gradient(135deg, #111827 0%, #1a2235 100%);
#             border: 1px solid rgba(99,179,237,0.15);
#             border-radius: 1rem;
#             padding: 0.875rem 1.5rem;
#             margin-bottom: 1.5rem;
#             box-shadow: 0 0 40px rgba(49,130,206,0.06);
#         }
#         .dash-logo {
#             width: 2.75rem; height: 2.75rem;
#             border-radius: 0.65rem;
#             background: linear-gradient(135deg, #1e3a5f, #3182ce);
#             display: flex; align-items: center; justify-content: center;
#             font-weight: 700; font-size: 0.9rem; color: #fff;
#             letter-spacing: 0.05em;
#             border: 1px solid rgba(99,179,237,0.3);
#             box-shadow: 0 0 20px rgba(49,130,206,0.25);
#         }
#         .dash-title { font-size: 1rem; font-weight: 600; color: #e2e8f0; letter-spacing: -0.01em; }
#         .dash-subtitle { font-size: 0.75rem; color: #64748b; font-weight: 400; margin-top: 0.1rem; }
#         .live-pill {
#             display: flex; align-items: center; gap: 0.5rem;
#             background: rgba(56,161,105,0.12);
#             border: 1px solid rgba(56,161,105,0.25);
#             border-radius: 9999px;
#             padding: 0.35rem 0.875rem;
#             font-size: 0.75rem; font-weight: 600; color: #68d391;
#             letter-spacing: 0.05em;
#         }
#         .live-dot {
#             width: 0.45rem; height: 0.45rem;
#             border-radius: 9999px; background: #38a169;
#             box-shadow: 0 0 6px #38a169;
#             animation: pulse 2s ease-in-out infinite;
#         }
#         @keyframes pulse {
#             0%, 100% { opacity: 1; box-shadow: 0 0 6px #38a169; }
#             50%       { opacity: 0.6; box-shadow: 0 0 12px #38a169; }
#         }

#         /* SECTION LABEL */
#         .section-label {
#             font-size: 0.65rem; font-weight: 700;
#             text-transform: uppercase; letter-spacing: 0.1em;
#             color: #4a6fa5; margin-bottom: 0.75rem;
#             display: flex; align-items: center; gap: 0.4rem;
#         }
#         .section-label::before {
#             content: ''; display: inline-block;
#             width: 0.2rem; height: 0.8rem;
#             background: #3182ce; border-radius: 2px;
#         }

#         /* METRIC CARDS */
#         .metric-card {
#             background: linear-gradient(145deg, #111827, #1a2235);
#             border: 1px solid rgba(99,179,237,0.1);
#             border-radius: 0.875rem;
#             padding: 1.125rem 1.25rem;
#             margin-bottom: 0.75rem;
#             position: relative; overflow: hidden;
#         }
#         .metric-card::after {
#             content: ''; position: absolute;
#             top: 0; left: 0; right: 0; height: 2px;
#             border-radius: 0.875rem 0.875rem 0 0;
#         }
#         .metric-card.blue::after   { background: linear-gradient(90deg, #3182ce, #63b3ed); }
#         .metric-card.orange::after { background: linear-gradient(90deg, #dd6b20, #f6ad55); }
#         .metric-card.red::after    { background: linear-gradient(90deg, #c53030, #fc8181); }
#         .metric-card.teal::after   { background: linear-gradient(90deg, #2c7a7b, #81e6d9); }

#         .metric-icon { font-family: 'Material Symbols Rounded'; font-size: 1.5rem; line-height: 1; }
#         .metric-icon.blue   { color: #63b3ed; }
#         .metric-icon.orange { color: #f6ad55; }
#         .metric-icon.red    { color: #fc8181; }
#         .metric-icon.teal   { color: #81e6d9; }

#         .metric-value {
#             font-size: 2rem; font-weight: 700;
#             letter-spacing: -0.04em; color: #f7fafc;
#             line-height: 1.1; margin-top: 0.625rem;
#         }
#         .metric-label {
#             font-size: 0.7rem; font-weight: 500;
#             text-transform: uppercase; letter-spacing: 0.06em;
#             color: #4a5568; margin-top: 0.25rem;
#         }

#         /* CHART CARD */
#         .chart-card {
#             background: linear-gradient(145deg, #111827, #1a2235);
#             border: 1px solid rgba(99,179,237,0.1);
#             border-radius: 0.875rem;
#             padding: 1.125rem 1.25rem 0.75rem 1.25rem;
#             margin-bottom: 0.75rem;
#         }
#         .chart-title { font-size: 0.8rem; font-weight: 600; color: #cbd5e0; margin-bottom: 0.25rem; }
#         .chart-meta  { font-size: 0.65rem; color: #4a6fa5; margin-bottom: 0.75rem; }

#         /* LEGEND */
#         .legend-row  { display: flex; gap: 1.25rem; justify-content: center; margin-top: 0.5rem; }
#         .legend-item { display: flex; align-items: center; gap: 0.35rem; font-size: 0.72rem; color: #94a3b8; }
#         .legend-dot  { width: 0.55rem; height: 0.55rem; border-radius: 9999px; }

#         /* FOOTER */
#         .dash-footer {
#             display: flex; justify-content: space-between; align-items: center;
#             padding-top: 0.75rem;
#             border-top: 1px solid rgba(99,179,237,0.08);
#             font-size: 0.65rem; color: #334155; margin-top: 0.5rem;
#         }
#         .footer-status { display: flex; align-items: center; gap: 0.4rem; color: #48bb78; font-weight: 500; }
#     </style>
#     """, unsafe_allow_html=True)

#     # ── DATA ──────────────────────────────────────────────────────────────────
#     @st.cache_data
#     def generate_data():
#         entities      = ['GDNT','PT006','PT018','PT002','PT004','PT008','LM10','GDPFMIT','PT020','PT012']
#         reports       = [2145, 618, 458, 162, 385, 410, 258, 327, 174, 291]
#         queries       = [1222, 151, 201, 410, 147, 119, 265, 166, 284, 117]
#         months_short  = ['S','O','N','D','J','F','M','A','M','J','J','A']
#         this_year     = [52, 68, 45, 82, 55, 70, 65, 92, 63, 80, 72, 100]
#         last_year     = [45, 58, 38, 70, 48, 60, 55, 78, 52, 68, 62, 85]
#         months_full   = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
#         reports_trend = [112, 120, 84, 110, 52, 69, 90, 44, 86, 16, 92, 48]
#         queries_trend = [33,  19,  39,  86, 37, 50, 25, 75, 30, 76, 33, 41]
#         return dict(
#             active=2924, inactive_30=505, inactive_90=899,
#             total_users=4328, account_locks=1493, queries_reports=74, failed_logins=217,
#             entities=entities, reports=reports, queries=queries,
#             months_short=months_short, this_year=this_year, last_year=last_year,
#             months_full=months_full, reports_trend=reports_trend, queries_trend=queries_trend,
#         )

#     d = generate_data()

#     # ── SHARED CHART CONSTANTS ────────────────────────────────────────────────
#     PAPER  = 'rgba(0,0,0,0)'
#     GRID   = 'rgba(99,179,237,0.07)'
#     TICK   = dict(color='#4a6fa5', size=11, family='DM Sans')
#     FONT   = dict(family='DM Sans', color='#94a3b8')
#     LEGEND = dict(
#         orientation='h', yanchor='bottom', y=1.02,
#         xanchor='center', x=0.5,
#         font=dict(size=11, family='DM Sans'),
#         bgcolor='rgba(0,0,0,0)', borderwidth=0,
#     )

#     # ── HEADER ────────────────────────────────────────────────────────────────
#     st.markdown("""
#     <div class="dash-header">
#         <div style="display:flex;align-items:center;gap:1rem;">
#             <div class="dash-logo">FM</div>
#             <div style="height:1.5rem;width:1px;background:rgba(99,179,237,0.15);"></div>
#             <div>
#                 <div class="dash-title">FMIS Monitoring</div>
#                 <div class="dash-subtitle">User &amp; Report Analytics · OIM Team</div>
#             </div>
#         </div>
#         <div class="live-pill"><div class="live-dot"></div>LIVE</div>
#     </div>
#     """, unsafe_allow_html=True)

#     # ══════════════════════════════════════════════════════════════════════════
#     # ROW 1 — Metric cards | Account status donut | New users bar
#     # ══════════════════════════════════════════════════════════════════════════
#     col_m, col_charts = st.columns([2, 5])

#     with col_m:
#         st.markdown('<div class="section-label">Activity Metrics</div>', unsafe_allow_html=True)
#         for icon, color, val, label in [
#             ("group",   "blue",   f"{d['total_users']:,}",  "Total Users"),
#             # ("lock",    "orange", f"{d['account_locks']:,}", "Account Locks"),
#             ("search",  "teal",   str(d['queries_reports']), "Queries & Reports"),
#             ("warning", "red",    str(d['failed_logins']),   "Failed Logins"),
#         ]:
#             st.markdown(f"""
#             <div class="metric-card {color}">
#                 <span class="metric-icon {color}">{icon}</span>
#                 <div class="metric-value">{val}</div>
#                 <div class="metric-label">{label}</div>
#             </div>""", unsafe_allow_html=True)

#     with col_charts:
#         st.markdown('<div class="section-label">User Activity</div>', unsafe_allow_html=True)
#         cc1, cc2 = st.columns(2)

#         # Donut — Account Status
#         with cc1:
#             st.markdown("""
#             <div class="chart-card">
#                 <div class="chart-title">Account Status</div>
#                 <div class="chart-meta">Current period breakdown</div>
#             """, unsafe_allow_html=True)

#             fig_donut = go.Figure()
#             fig_donut.add_trace(go.Pie(
#                 labels=['Active', 'Inactive (30d)', 'Inactive (90d)'],
#                 values=[d['active'], d['inactive_30'], d['inactive_90']],
#                 hole=0.68,
#                 marker=dict(colors=['#3182ce','#63b3ed','#dd6b20'],
#                             line=dict(color='#0b0f1a', width=3)),
#                 textinfo='none', showlegend=False, sort=False,
#                 hovertemplate='<b>%{label}</b><br>%{value:,} users · %{percent}<extra></extra>',
#             ))
#             fig_donut.update_layout(
#                 height=240,
#                 paper_bgcolor=PAPER, plot_bgcolor=PAPER,
#                 margin=dict(l=10, r=10, t=10, b=10),
#                 font=FONT,
#                 annotations=[dict(
#                     text=f'<b>{d["total_users"]:,}</b><br>Users',
#                     x=0.5, y=0.5,
#                     font=dict(size=13, color='#e2e8f0'),
#                     showarrow=False,
#                 )],
#             )
#             st.plotly_chart(fig_donut, use_container_width=True, config={'displayModeBar': False})
#             st.markdown("""
#             <div class="legend-row">
#                 <div class="legend-item"><div class="legend-dot" style="background:#3182ce"></div>Active {:,}</div>
#                 <div class="legend-item"><div class="legend-dot" style="background:#63b3ed"></div>Inactive 30d {:,}</div>
#                 <div class="legend-item"><div class="legend-dot" style="background:#dd6b20"></div>Inactive 90d {:,}</div>
#             </div></div>
#             """.format(d['active'], d['inactive_30'], d['inactive_90']), unsafe_allow_html=True)

#         # Grouped Bar — New Users
#         with cc2:
#             st.markdown("""
#             <div class="chart-card">
#                 <div class="chart-title">New Users · Monthly</div>
#                 <div class="chart-meta">This year vs last year</div>
#             """, unsafe_allow_html=True)

#             fig_bar = go.Figure()
#             fig_bar.add_trace(go.Bar(
#                 x=d['months_short'], y=d['last_year'], name='Last Year',
#                 marker=dict(color='rgba(100,116,139,0.5)', line=dict(width=0)),
#             ))
#             fig_bar.add_trace(go.Bar(
#                 x=d['months_short'], y=d['this_year'], name='This Year',
#                 marker=dict(
#                     color=d['this_year'],
#                     colorscale=[[0,'#1e3a5f'],[1,'#63b3ed']],
#                     showscale=False, line=dict(width=0),
#                 ),
#             ))
#             fig_bar.update_layout(
#                 height=240,
#                 paper_bgcolor=PAPER, plot_bgcolor=PAPER,
#                 margin=dict(l=10, r=10, t=30, b=10),
#                 font=FONT, legend=LEGEND,
#                 barmode='group', bargap=0.25, bargroupgap=0.05,
#                 xaxis=dict(showgrid=False, tickfont=TICK,
#                            tickcolor='rgba(0,0,0,0)', linecolor='rgba(0,0,0,0)'),
#                 yaxis=dict(showgrid=True, gridcolor=GRID, gridwidth=1, tickfont=TICK,
#                            zeroline=False, linecolor='rgba(0,0,0,0)'),
#             )
#             st.plotly_chart(fig_bar, use_container_width=True, config={'displayModeBar': False})
#             st.markdown('</div>', unsafe_allow_html=True)

#     # ══════════════════════════════════════════════════════════════════════════
#     # ROW 2 — Top 10 Entities | Usage type donut | Activity trends
#     # ══════════════════════════════════════════════════════════════════════════
#     col_ent, col_usage, col_trend = st.columns([5, 2, 5])

#     # Horizontal Stacked Bar — Top 10 Entities
#     with col_ent:
#         st.markdown('<div class="section-label">Report Usage Analytics</div>', unsafe_allow_html=True)
#         st.markdown("""
#         <div class="chart-card">
#             <div class="chart-title">Top 10 Active Entities · Reports &amp; Queries</div>
#             <div class="chart-meta">Current month · Sorted by total volume</div>
#         """, unsafe_allow_html=True)

#         entities = d['entities']
#         reports  = d['reports']
#         queries  = d['queries']

#         order      = sorted(range(len(entities)), key=lambda i: reports[i] + queries[i])
#         ent_sorted = [entities[i] for i in order]
#         rep_sorted = [reports[i]  for i in order]
#         qry_sorted = [queries[i]  for i in order]

#         fig_hbar = go.Figure()
#         fig_hbar.add_trace(go.Bar(
#             y=ent_sorted, x=rep_sorted, name='Reports', orientation='h',
#             marker=dict(color='#2b6cb0', line=dict(width=0)),
#             text=[f'{v:,}' for v in rep_sorted],
#             textposition='inside', insidetextanchor='end',
#             textfont=dict(color='#e2e8f0', size=11, family='DM Mono'),
#             hovertemplate='<b>%{y}</b><br>Reports: %{x:,}<extra></extra>',
#         ))
#         fig_hbar.add_trace(go.Bar(
#             y=ent_sorted, x=qry_sorted, name='Queries', orientation='h',
#             marker=dict(color='#63b3ed', line=dict(width=0)),
#             text=[f'{v:,}' for v in qry_sorted],
#             textposition='inside', insidetextanchor='end',
#             textfont=dict(color='#1a2235', size=11, family='DM Mono'),
#             hovertemplate='<b>%{y}</b><br>Queries: %{x:,}<extra></extra>',
#         ))
#         fig_hbar.update_layout(
#             height=360,
#             paper_bgcolor=PAPER, plot_bgcolor=PAPER,
#             margin=dict(l=80, r=20, t=30, b=10),
#             font=FONT, legend=LEGEND,
#             barmode='stack', bargap=0.25,
#             xaxis=dict(showgrid=True, gridcolor=GRID, gridwidth=1,
#                        tickfont=TICK, zeroline=False,
#                        linecolor='rgba(0,0,0,0)', tickformat=','),
#             yaxis=dict(showgrid=False,
#                        tickfont=dict(color='#94a3b8', size=12, family='DM Mono'),
#                        linecolor='rgba(0,0,0,0)', categoryorder='total ascending'),
#         )
#         st.plotly_chart(fig_hbar, use_container_width=True, config={'displayModeBar': False})
#         st.markdown("""
#         <div class="legend-row" style="margin-bottom:0.25rem">
#             <div class="legend-item"><div class="legend-dot" style="background:#2b6cb0"></div>Reports</div>
#             <div class="legend-item"><div class="legend-dot" style="background:#63b3ed"></div>Queries</div>
#         </div></div>
#         """, unsafe_allow_html=True)

#     # Donut — Usage by Type
#     with col_usage:
#         st.markdown('<div class="section-label">Usage Type</div>', unsafe_allow_html=True)
#         st.markdown("""
#         <div class="chart-card">
#             <div class="chart-title">Usage by Type</div>
#             <div class="chart-meta">Reports vs Queries</div>
#         """, unsafe_allow_html=True)

#         fig_type = go.Figure()
#         fig_type.add_trace(go.Pie(
#             labels=['Reports', 'Queries'], values=[53, 21],
#             hole=0.68,
#             marker=dict(colors=['#2b6cb0','#63b3ed'],
#                         line=dict(color='#0b0f1a', width=3)),
#             textinfo='none', showlegend=False,
#             hovertemplate='<b>%{label}</b><br>%{value} · %{percent}<extra></extra>',
#         ))
#         fig_type.update_layout(
#             height=220,
#             paper_bgcolor=PAPER, plot_bgcolor=PAPER,
#             margin=dict(l=10, r=10, t=10, b=10),
#             font=FONT,
#             annotations=[dict(
#                 text='<b>74</b><br>Total',
#                 x=0.5, y=0.5,
#                 font=dict(size=13, color='#e2e8f0'),
#                 showarrow=False,
#             )],
#         )
#         st.plotly_chart(fig_type, use_container_width=True, config={'displayModeBar': False})
#         st.markdown("""
#         <div class="legend-row" style="flex-direction:column;align-items:center;gap:0.5rem;margin-bottom:0.5rem">
#             <div class="legend-item">
#                 <div class="legend-dot" style="background:#2b6cb0;width:0.75rem;height:0.75rem"></div>
#                 Reports &nbsp;<b style="color:#e2e8f0">53</b>
#             </div>
#             <div class="legend-item">
#                 <div class="legend-dot" style="background:#63b3ed;width:0.75rem;height:0.75rem"></div>
#                 Queries &nbsp;<b style="color:#e2e8f0">21</b>
#             </div>
#         </div></div>
#         """, unsafe_allow_html=True)

#     # Line chart — Activity Trends
#     with col_trend:
#         st.markdown('<div class="section-label">Activity Trends</div>', unsafe_allow_html=True)
#         st.markdown("""
#         <div class="chart-card">
#             <div class="chart-title">Monthly Activity Trends</div>
#             <div class="chart-meta">Reports &amp; Queries over the year</div>
#         """, unsafe_allow_html=True)

#         fig_trend = go.Figure()
#         fig_trend.add_trace(go.Scatter(
#             x=d['months_full'], y=d['reports_trend'], name='Reports',
#             line=dict(color='#3182ce', width=2.5, shape='spline', smoothing=0.8),
#             mode='lines+markers',
#             marker=dict(size=6, color='#3182ce', line=dict(width=2, color='#0b0f1a')),
#             fill='tozeroy', fillcolor='rgba(49,130,206,0.07)',
#             hovertemplate='%{x}<br>Reports: <b>%{y}</b><extra></extra>',
#         ))
#         fig_trend.add_trace(go.Scatter(
#             x=d['months_full'], y=d['queries_trend'], name='Queries',
#             line=dict(color='#63b3ed', width=2.5, shape='spline', smoothing=0.8, dash='dot'),
#             mode='lines+markers',
#             marker=dict(size=6, color='#63b3ed', line=dict(width=2, color='#0b0f1a')),
#             fill='tozeroy', fillcolor='rgba(99,179,237,0.05)',
#             hovertemplate='%{x}<br>Queries: <b>%{y}</b><extra></extra>',
#         ))
#         fig_trend.update_layout(
#             height=360,
#             paper_bgcolor=PAPER, plot_bgcolor=PAPER,
#             margin=dict(l=10, r=10, t=30, b=10),
#             font=FONT, legend=LEGEND,
#             hovermode='x unified',
#             xaxis=dict(showgrid=False, tickfont=TICK,
#                        linecolor='rgba(0,0,0,0)', tickcolor='rgba(0,0,0,0)'),
#             yaxis=dict(showgrid=True, gridcolor=GRID, gridwidth=1, tickfont=TICK,
#                        zeroline=False, linecolor='rgba(0,0,0,0)'),
#         )
#         st.plotly_chart(fig_trend, use_container_width=True, config={'displayModeBar': False})
#         st.markdown('</div>', unsafe_allow_html=True)

#     # ── FOOTER ────────────────────────────────────────────────────────────────
#     st.markdown("""
#     <div class="dash-footer">
#         <span>© FMIS · Developed and prepared by OIM Team</span>
#         <div class="footer-status">
#             <div class="live-dot" style="width:0.35rem;height:0.35rem"></div>
#             All systems operational
#         </div>
#     </div>
#     """, unsafe_allow_html=True)


# if __name__ == "__main__":
#     st.set_page_config(layout="wide", page_title="FMIS Monitoring", page_icon="📊")
#     Monitoring()


import base64
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def Monitoring():
    # Custom CSS for professional dashboard with #3498dc theme
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@24,400,1,0');

        * { 
            font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            box-sizing: border-box; 
        }

        html, body, .stApp { 
            # background: linear-gradient(135deg, #f5f9ff 0%, #ecf3fa 100%);
            # color: #1e293b; 
        }

        .block-container {
            padding: 1.5rem 2rem 1rem 2rem !important;
            max-width: 100% !important;
        }

        #MainMenu, footer, header { visibility: hidden; }
        .stDeployButton { display: none; }

        /* HEADER - Enhanced with #3498dc */
        .dash-header {
            display: flex; align-items: center; justify-content: space-between;
            #background: linear-gradient(135deg, #ffffff 0%, #f8fcff 100%);
            border: 1px solid rgba(52, 152, 220, 0.15);
            #border-radius: 1rem;
            padding: 0.875rem 1.5rem;
            margin-bottom: 1.5rem;
            #box-shadow: 0 8px 20px -8px rgba(52, 152, 220, 0.15);
            
            background: white;
            border-radius: 8px;
            
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
            border: 1px solid #e0e0e0;
           
        }
        .dash-logo {
            width: 2.75rem; height: 2.75rem;
            border-radius: 0.65rem;
            background: linear-gradient(135deg, #2c3e50, #3498dc);
            display: flex; align-items: center; justify-content: center;
            font-weight: 700; font-size: 0.9rem; color: #fff;
            letter-spacing: 0.05em;
            border: 1px solid rgba(52, 152, 220, 0.3);
            box-shadow: 0 4px 10px -2px rgba(52, 152, 220, 0.3);
        }
        .dash-title { font-size: 1rem; font-weight: 600; color: #1e293b; letter-spacing: -0.01em; }
        .dash-subtitle { font-size: 0.75rem; color: #64748b; font-weight: 400; margin-top: 0.1rem; }
        .live-pill {
            display: flex; align-items: center; gap: 0.5rem;
            background: rgba(52, 152, 220, 0.08);
            border: 1px solid rgba(52, 152, 220, 0.2);
            border-radius: 9999px;
            padding: 0.35rem 0.875rem;
            font-size: 0.75rem; font-weight: 600; color: #3498dc;
            letter-spacing: 0.05em;
        }
        .live-dot {
            width: 0.45rem; height: 0.45rem;
            border-radius: 9999px; background: #3498dc;
            box-shadow: 0 0 8px #3498dc;
            animation: pulse 2s ease-in-out infinite;
        }
        @keyframes pulse {
            0%, 100% { opacity: 1; box-shadow: 0 0 8px #3498dc; }
            50%       { opacity: 0.6; box-shadow: 0 0 16px #3498dc; }
        }

        /* SECTION LABEL - Enhanced with #3498dc */
        .section-label {
            # font-size: 0.65rem; font-weight: 700;
            # text-transform: uppercase; letter-spacing: 0.1em;
            # color: #3498dc; margin-bottom: 0.75rem;
             display: flex; align-items: center; gap: 0.4rem;
            font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: #2c3e50;
            font-weight: 600;
            font-size: 1rem;
            margin: 2rem 0 1rem 0;
            padding-bottom: 0.5rem;
            border-bottom: 1px solid #ecf0f1;
        }
        .section-label::before {
            content: ''; display: inline-block;
            width: 0.25rem; height: 1.2rem;
            background: #3498dc; border-radius: 2px;
        }

        /* METRIC CARDS - Enhanced with #3498dc accents */
        .metric-card {
            #background: linear-gradient(145deg, #ffffff, #f8fcff);
            #border: 1px solid rgba(52, 152, 220, 0.1);
            #border-radius: 0.875rem;
            #padding: 1.125rem 1.25rem;
            margin-bottom: 0.75rem;
            position: relative; overflow: hidden;
            #box-shadow: 0 4px 12px -4px rgba(52, 152, 220, 0.1);
            transition: all 0.2s ease;
                
            background: white;
            border-radius: 8px;
            padding: 1.5rem;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
            border: 1px solid #e0e0e0;
     

        }
        .metric-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 24px -8px rgba(52, 152, 220, 0.2);
            border-color: rgba(52, 152, 220, 0.2);
        }
        .metric-card::after {
            content: ''; position: absolute;
            top: 0; left: 0; right: 0; height: 2px;
            border-radius: 0.875rem 0.875rem 0 0;
        }
        .metric-card.blue::after   { background: linear-gradient(90deg, #3498dc, #5faee3); }
        .metric-card.orange::after { background: linear-gradient(90deg, #e67e22, #f39c12); }
        .metric-card.red::after    { background: linear-gradient(90deg, #e74c3c, #f1948a); }
        .metric-card.teal::after   { background: linear-gradient(90deg, #1abc9c, #48c9b0); }

        .metric-icon { font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 1.5rem; line-height: 1; }
        .metric-icon.blue   { color: #3498dc; }
        .metric-icon.orange { color: #e67e22; }
        .metric-icon.red    { color: #e74c3c; }
        .metric-icon.teal   { color: #1abc9c; }

                





        .metric-value {
            font-size: 2rem; font-weight: 700;
            letter-spacing: -0.04em; color: #1e293b;
            line-height: 1.1; margin-top: 0.625rem;
        }
        .metric-label {
            font-size: 0.7rem; font-weight: 500;
            text-transform: uppercase; letter-spacing: 0.06em;
            color: #64748b; margin-top: 0.25rem;
        }

        /* CHART CARD - Enhanced with #3498dc theme */
        .chart-card {
            background: linear-gradient(145deg, #ffffff, #f8fcff);
            #border: 1px solid rgba(52, 152, 220, 0.1);
            #border-radius: 0.875rem;
            #padding: 1.125rem 1.25rem 0.75rem 1.25rem;
            margin-bottom: 0.75rem;
            #box-shadow: 0 4px 12px -4px rgba(52, 152, 220, 0.08);
            transition: all 0.2s ease;
            
            background: white;
           
            border-radius: 8px;
            padding: 1.5rem;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
            border: 1px solid #e0e0e0;
            
                

            
        }
        .chart-card:hover {
            box-shadow: 0 8px 24px -8px rgba(52, 152, 220, 0.15);
            border-color: rgba(52, 152, 220, 0.15);
        }
        .chart-title { font-size: 0.8rem; font-weight: 600; color: #1e293b; margin-bottom: 0.25rem; }
        .chart-meta  { font-size: 0.65rem; color: #3498dc; margin-bottom: 0.75rem; }

        /* LEGEND - Enhanced */
        .legend-row  { display: flex; gap: 1.25rem; justify-content: center; margin-top: 0.5rem; }
        .legend-item { display: flex; align-items: center; gap: 0.35rem; font-size: 0.72rem; color: #475569; }
        .legend-dot  { width: 0.55rem; height: 0.55rem; border-radius: 9999px; }

        /* FOOTER - Enhanced */
        .dash-footer {
            display: flex; justify-content: space-between; align-items: center;
            #padding: 1rem 1.5rem;
            #background: #ffffff;
            #border: 1px solid rgba(52, 152, 220, 0.1);
            #border-radius: 0.875rem;
            font-size: 0.75rem; color: #64748b; margin-top: 1rem;
            #box-shadow: 0 4px 12px -4px rgba(52, 152, 220, 0.05);
                
            background: white;
            border-radius: 8px;
            padding: 1.5rem;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
            border: 1px solid #e0e0e0;
         

        }
        .footer-status { 
            display: flex; align-items: center; gap: 0.4rem; 
            color: #3498dc; font-weight: 500;
            background: rgba(52, 152, 220, 0.08);
            padding: 0.35rem 1rem;
            border-radius: 9999px;
            border: 1px solid rgba(52, 152, 220, 0.1);
        }
        
        /* Custom scrollbar */
        ::-webkit-scrollbar {
            width: 6px;
            height: 6px;
        }
        ::-webkit-scrollbar-track {
            background: #f1f5f9;
        }
        ::-webkit-scrollbar-thumb {
            background: #3498dc;
            border-radius: 3px;
        }
    </style>
    """, unsafe_allow_html=True)

    # ── DATA ──────────────────────────────────────────────────────────────────
    @st.cache_data
    def generate_data():
        entities      = ['GDNT','PT006','PT018','PT002','PT004','PT008','LM10','GDPFMIT','PT020','PT012']
        reports       = [2145, 618, 458, 162, 385, 410, 258, 327, 174, 291]
        queries       = [1222, 151, 201, 410, 147, 119, 265, 166, 284, 117]
        months_short  = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        this_2025     = [3525,3533,3551,3569,3602,3619,3673,3798,3810,3840,3852,3852]
        last_2024   = [2959,2970,3016,3021,3043,3203,3223,3243,3324,3388,3426,3572]
        months_full   = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        reports_trend = [11203, 12084,  11052, 6907, 9044, 8616, 9248, 7799, 6627,10517,7266,9271]
        queries_trend = [3319,   3986,  3750,  2575, 3076, 3341,  4435, 4011, 3393,3815,2876,3678]
        return dict(
            active=2924, inactive=505, inactive_90=899,
            total_users=4328, account_locks=1493, queries_reports=74, failed_logins=217,
            entities=entities, reports=reports, queries=queries,
            months_short=months_short, this_year=this_2025, last_year=last_2024,
            months_full=months_full, reports_trend=reports_trend, queries_trend=queries_trend,
        )

    d = generate_data()



    # ── SHARED CHART CONSTANTS ────────────────────────────────────────────────
    PAPER  = 'rgba(0,0,0,0)'
    GRID   = 'rgba(52, 152, 220, 0.1)'  # #3498dc tinted grid
    TICK   = dict(color='#475569', size=11, family='Inter')
    FONT   = dict(family='Inter', color='#475569')
    LEGEND = dict(
        orientation='h', yanchor='bottom', y=1.02,
        xanchor='center', x=0.5,
        font=dict(size=11, family='Inter'),
        bgcolor='rgba(0,0,0,0)', borderwidth=0,
    )


    def get_base64_image(path):
        with open(path, "rb") as img:
            return base64.b64encode(img.read()).decode()

    img_base64 = get_base64_image("FMIS_Logo.png")

    # ── HEADER ────────────────────────────────────────────────────────────────
    # st.markdown("""
    # <div class="dash-header">
    #     <div style="display:flex;align-items:center;gap:1rem;">
    #         -- <div class="dash-logo">FM</div>
    #         <img src="data:image/png;base64,{img_base64}" width="40">
    #         <div style="height:1.5rem;width:1px;background:rgba(52,152,220,0.15);"></div>
    #         <div>
    #             <div class="dash-title">FMIS Monitoring</div>
    
    #             <div class="dash-subtitle">User &amp; Report Analytics · OIM Team</div>
    #         </div>
    #     </div>
    #     <div class="live-pill"><div class="live-dot"></div>LIVE</div>
    # </div>
    # """, unsafe_allow_html=True)
    # st.markdown(f"""
    #     <div class="dash-header">
    #         <div style="display:flex;align-items:center;gap:1rem;">
    #             <img src="data:image/png;base64,{img_base64}" width="40">
    #             <div style="height:1.5rem;width:1px;background:rgba(52,152,220,0.15);"></div>
    #             <div>
    #                 <div class="dash-title">FMIS Monitoring</div>
    #                 <div class="dash-subtitle">User & Report Analytics · OIM Team</div>
    #             </div>
    #         </div>
    #         <div class="live-pill"><div class="live-dot"></div>LIVE</div>
    #     </div>
    #     """, unsafe_allow_html=True)
    st.markdown(f"""
    <div class="dash-header">
        <div style="display:flex;align-items:center;gap:1rem;">
            <img src="data:image/png;base64,{img_base64}" width="40">
            <div style="height:1.5rem;width:1px;background:rgba(52,152,220,0.15);"></div>
            <div>
                <div class="dash-title">FMIS Monitoring</div>
                <div class="dash-subtitle">User & Report Analytics · OIM Team</div>
            </div>
        </div>
        <div style="display:flex;align-items:center;gap:1rem;">
            <div style="background:rgba(52,152,220,0.1); padding:0.25rem 0.75rem; border-radius:20px; font-size:0.8rem; color:#2c3e50; border:1px solid rgba(52,152,220,0.2);">
                📅 Date Range Last 30days
            </div>
            <div class="live-pill">
                <div class="live-dot"></div>LIVE
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ══════════════════════════════════════════════════════════════════════════
    # ROW 1 — Metric cards | Account status donut | New users bar
    # ══════════════════════════════════════════════════════════════════════════
    col_m, col_charts = st.columns([2, 5])

    with col_m:
        st.markdown('<div class="section-label">Activity Metrics</div>', unsafe_allow_html=True)
        for icon, color, val, label in [
            ("👥",   "blue",   f"{d['total_users']:,}",  "Total Users"),
            ("📘",  "teal",   str(d['queries_reports']), "Queries & Reports"),
            ("⚠️", "red",    str(d['failed_logins']),   "Failed Logins"),
        ]:
            st.markdown(f"""
            <div class="metric-card {color}">
                <span class="metric-icon {color}">{icon}</span>
                <div class="metric-value">{val}</div>
                <div class="metric-label">{label}</div>
            </div>""", unsafe_allow_html=True)

    with col_charts:
        st.markdown('<div class="section-label">User Activity</div>', unsafe_allow_html=True)
        cc1, cc2 = st.columns(2)

        # Donut — Account Status
        with cc1:
            st.markdown("""
            <div class="chart-card">
                <div class="chart-title">User Status</div>
                <div class="chart-meta">User Status Distribution</div>
            """, unsafe_allow_html=True)

            # fig_donut = go.Figure()
            # fig_donut.add_trace(go.Pie(
            #     labels=['Active', 'Inactive (30d)', 'Inactive (90d)'],
            #     values=[d['active'], d['inactive'], d['inactive_90']],
            #     hole=0.68,
            #     marker=dict(colors=['#3498dc', '#7bb9e8', '#f39c12'],
            #                 line=dict(color='#ffffff', width=3)),
            #     textinfo='none', showlegend=False, sort=False,
            #     hovertemplate='<b>%{label}</b><br>%{value:,} users · %{percent}<extra></extra>',
            # ))
            # fig_donut.update_layout(
            #     height=240,
            #     paper_bgcolor=PAPER, plot_bgcolor=PAPER,
            #     margin=dict(l=10, r=10, t=10, b=10),
            #     font=FONT,
            #     annotations=[dict(
            #         text=f'<b>{d["total_users"]:,}</b><br>Users',
            #         x=0.5, y=0.5,
            #         font=dict(size=13, color='#1e293b'),
            #         showarrow=False,
            #     )],
            # )
            # st.plotly_chart(fig_donut, use_container_width=True, config={'displayModeBar': False})
            # st.markdown("""
            # <div class="legend-row">
            #     <div class="legend-item"><div class="legend-dot" style="background:#3498dc"></div>Active {:,}</div>
            #     <div class="legend-item"><div class="legend-dot" style="background:#7bb9e8"></div>Inactive {:,}</div>
            #     <div class="legend-item"><div class="legend-dot" style="background:#f39c12"></div>Inactive 90d {:,}</div>
            # </div></div>
            # """.format(d['active'], d['inactive'], d['inactive_90']), unsafe_allow_html=True)
            # Prepare data for donut chart
            status_counts = pd.DataFrame({
                'Status': ['Active', 'Inactive', 'Inactive (90d)'],
                'Count': [d['active'], d['inactive'], d['inactive_90']]
            })

            # Create donut chart
            fig = px.pie(
                status_counts,
                values='Count',
                names='Status',
                hole=0.6,  # Slightly smaller hole to show labels better
                height=350,  # Taller to accommodate labels
                color_discrete_sequence=['#3498dc', '#7bb9e8', '#f39c12'],  # Original colors
            )

            fig.update_traces(
                textposition='inside',
                textinfo='percent+label',  # Show both percent and label on chart
                marker=dict(
                    line=dict(color='white', width=2)
                ),
                pull=[0.05, 0.05, 0.05],  # Slight pull on all segments for explosion effect
                textfont=dict(family="Inter", size=11),
                hovertemplate='<b>%{label}</b><br>%{value:,} users · %{percent}<extra></extra>',
                sort=False  # Keep original order
            )

            fig.update_layout(
                showlegend=False,  # Hide legend since labels are on chart
                margin=dict(t=30, b=30, l=30, r=30),  # More margin for labels
                paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(family="Inter", size=12),
                annotations=[dict(
                    text=f"Total<br>{d['total_users']:,}",
                    x=0.5, y=0.5,
                    font_size=16,
                    font_family="Inter",
                    font_color="#1e293b",
                    showarrow=False,
                    align='center'
                )]
            )

            st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

           

        # Grouped Bar — New Users
        with cc2:
            st.markdown("""
            <div class="chart-card">
                <div class="chart-title">New Users · Monthly</div>
                <div class="chart-meta">2024 vs 2025 comparison</div>
            """, unsafe_allow_html=True)

            fig_bar = go.Figure()
            fig_bar.add_trace(go.Bar(
                x=d['months_short'], 
                y=d['last_year'], 
                name='2024',
                marker=dict(color='rgba(52, 152, 220, 0.2)', line=dict(width=0)),
                text=[f'{v:,}' for v in d['last_year']],
                textposition='outside',
                textfont=dict(size=9, color='#64748b'),
            ))
            fig_bar.add_trace(go.Bar(
                x=d['months_short'], 
                y=d['this_year'], 
                name='2025',
                marker=dict(
                    color='#3498dc',
                    line=dict(width=0),
                ),
                text=[f'{v:,}' for v in d['this_year']],
                textposition='outside',
                textfont=dict(size=9, color='#3498dc', weight='bold'),
            ))
            fig_bar.update_layout(
                height=260,
                paper_bgcolor=PAPER, 
                plot_bgcolor=PAPER,
                margin=dict(l=10, r=10, t=30, b=10),
                font=FONT, 
                legend=LEGEND,
                barmode='group', 
                bargap=0.2, 
                bargroupgap=0.1,
                xaxis=dict(
                    showgrid=False, 
                    tickfont=TICK,
                    tickcolor='rgba(0,0,0,0)', 
                    linecolor='rgba(0,0,0,0)'
                ),
                yaxis=dict(
                    showgrid=True, 
                    gridcolor=GRID, 
                    gridwidth=1, 
                    tickfont=TICK,
                    zeroline=False, 
                    linecolor='rgba(0,0,0,0)'
                ),
            )
            st.plotly_chart(fig_bar, use_container_width=True, config={'displayModeBar': False})
            st.markdown('</div>', unsafe_allow_html=True)
        # Grouped Bar — New Users
        
        # with cc2:
        #     st.markdown("""
        #     <div class="chart-card">
        #         <div class="chart-title">New Users · Monthly</div>
        #         <div class="chart-meta">2024 vs 2025</div>
        #     """, unsafe_allow_html=True)

        #     fig_bar = go.Figure()
        #     fig_bar.add_trace(go.Bar(
        #         x=d['months_short'], y=d['last_year'], name='2024',
        #         marker=dict(color='rgba(52, 152, 220, 0.15)', line=dict(width=0)),
        #     ))
        #     fig_bar.add_trace(go.Bar(
        #         x=d['months_short'], y=d['this_year'], name='2025',
        #         marker=dict(
        #             color=d['this_year'],
        #             colorscale=[[0,'#2c3e50'],[1,'#3498dc']],
        #             showscale=False, line=dict(width=0),
        #         ),
        #     ))
        #     fig_bar.update_layout(
        #         height=240,
        #         paper_bgcolor=PAPER, plot_bgcolor=PAPER,
        #         margin=dict(l=10, r=10, t=30, b=10),
        #         font=FONT, legend=LEGEND,
        #         barmode='group', bargap=0.25, bargroupgap=0.05,
        #         xaxis=dict(showgrid=False, tickfont=TICK,
        #                    tickcolor='rgba(0,0,0,0)', linecolor='rgba(0,0,0,0)'),
        #         yaxis=dict(showgrid=True, gridcolor=GRID, gridwidth=1, tickfont=TICK,
        #                    zeroline=False, linecolor='rgba(0,0,0,0)'),
        #     )
        #     st.plotly_chart(fig_bar, use_container_width=True, config={'displayModeBar': False})
        #     st.markdown('</div>', unsafe_allow_html=True)

    # ══════════════════════════════════════════════════════════════════════════
    # ROW 2 — Top 10 Entities | Usage type donut | Activity trends
    # ══════════════════════════════════════════════════════════════════════════
    col_ent, col_usage, col_trend = st.columns([5, 2, 5])

    # Horizontal Stacked Bar — Top 10 Entities
    with col_ent:
        st.markdown('<div class="section-label">Report Usage Analytics</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="chart-card">
            <div class="chart-title">Top 10 Active Entities · Reports &amp; Queries</div>
            <div class="chart-meta">Current month · Sorted by total volume</div>
        """, unsafe_allow_html=True)

        entities = d['entities']
        reports  = d['reports']
        queries  = d['queries']

        order      = sorted(range(len(entities)), key=lambda i: reports[i] + queries[i])
        ent_sorted = [entities[i] for i in order]
        rep_sorted = [reports[i]  for i in order]
        qry_sorted = [queries[i]  for i in order]

        fig_hbar = go.Figure()
        fig_hbar.add_trace(go.Bar(
            y=ent_sorted, x=rep_sorted, name='Reports', orientation='h',
            marker=dict(color='#2c3e50', line=dict(width=0)),
            text=[f'{v:,}' for v in rep_sorted],
            textposition='inside', insidetextanchor='end',
            textfont=dict(color='#ffffff', size=11, family='DM Mono'),
            hovertemplate='<b>%{y}</b><br>Reports: %{x:,}<extra></extra>',
        ))
        fig_hbar.add_trace(go.Bar(
            y=ent_sorted, x=qry_sorted, name='Queries', orientation='h',
            marker=dict(color='#3498dc', line=dict(width=0)),
            text=[f'{v:,}' for v in qry_sorted],
            textposition='inside', insidetextanchor='end',
            textfont=dict(color='#ffffff', size=11, family='DM Mono'),
            hovertemplate='<b>%{y}</b><br>Queries: %{x:,}<extra></extra>',
        ))
        fig_hbar.update_layout(
            height=360,
            paper_bgcolor=PAPER, plot_bgcolor=PAPER,
            margin=dict(l=80, r=20, t=30, b=10),
            font=FONT, legend=LEGEND,
            barmode='stack', bargap=0.25,
            xaxis=dict(showgrid=True, gridcolor=GRID, gridwidth=1,
                       tickfont=TICK, zeroline=False,
                       linecolor='rgba(0,0,0,0)', tickformat=','),
            yaxis=dict(showgrid=False,
                       tickfont=dict(color='#1e293b', size=12, family='Inter'),
                       linecolor='rgba(0,0,0,0)', categoryorder='total ascending'),
        )
        st.plotly_chart(fig_hbar, use_container_width=True, config={'displayModeBar': False})
        st.markdown("""
        <div class="legend-row" style="margin-bottom:0.25rem">
            <div class="legend-item"><div class="legend-dot" style="background:#2c3e50"></div>Reports</div>
            <div class="legend-item"><div class="legend-dot" style="background:#3498dc"></div>Queries</div>
        </div></div>
        """, unsafe_allow_html=True)

    # Donut — Usage by Type
    with col_usage:
        st.markdown('<div class="section-label">Usage Type</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="chart-card">
            <div class="chart-title">Usage by Type</div>
            <div class="chart-meta">Reports vs Queries</div>
        """, unsafe_allow_html=True)

        fig_type = go.Figure()
        fig_type.add_trace(go.Pie(
            labels=['Reports', 'Queries'], values=[53, 21],
            hole=0.68,
            marker=dict(colors=['#2c3e50','#3498dc'],
                        line=dict(color='#ffffff', width=3)),
            textinfo='none', showlegend=False,
            hovertemplate='<b>%{label}</b><br>%{value} · %{percent}<extra></extra>',
        ))
        fig_type.update_layout(
            height=220,
            paper_bgcolor=PAPER, plot_bgcolor=PAPER,
            margin=dict(l=10, r=10, t=10, b=10),
            font=FONT,
            annotations=[dict(
                text='<b>74</b><br>Total',
                x=0.5, y=0.5,
                font=dict(size=13, color='#1e293b'),
                showarrow=False,
            )],
        )
        st.plotly_chart(fig_type, use_container_width=True, config={'displayModeBar': False})
        st.markdown("""
        <div class="legend-row" style="flex-direction:column;align-items:center;gap:0.5rem;margin-bottom:0.5rem">
            <div class="legend-item">
                <div class="legend-dot" style="background:#2c3e50;width:0.75rem;height:0.75rem"></div>
                Reports &nbsp;<b style="color:#1e293b">53</b>
            </div>
            <div class="legend-item">
                <div class="legend-dot" style="background:#3498dc;width:0.75rem;height:0.75rem"></div>
                Queries &nbsp;<b style="color:#1e293b">21</b>
            </div>
        </div></div>
        """, unsafe_allow_html=True)

    # Line chart — Activity Trends
    with col_trend:
        st.markdown('<div class="section-label">Activity Trends</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="chart-card">
            <div class="chart-title">Monthly Activity Trends</div>
            <div class="chart-meta">Reports &amp; Queries over the year</div>
        """, unsafe_allow_html=True)

        fig_trend = go.Figure()
        fig_trend.add_trace(go.Scatter(
            x=d['months_full'], y=d['reports_trend'], name='Reports',
            line=dict(color='#2c3e50', width=2.5, shape='spline', smoothing=0.8),
            mode='lines+markers',
            marker=dict(size=6, color='#2c3e50', line=dict(width=2, color='#ffffff')),
            fill='tozeroy', fillcolor='rgba(44, 62, 80, 0.05)',
            hovertemplate='%{x}<br>Reports: <b>%{y}</b><extra></extra>',
        ))
        fig_trend.add_trace(go.Scatter(
            x=d['months_full'], y=d['queries_trend'], name='Queries',
            line=dict(color='#3498dc', width=2.5, shape='spline', smoothing=0.8, dash='dot'),
            mode='lines+markers',
            marker=dict(size=6, color='#3498dc', line=dict(width=2, color='#ffffff')),
            fill='tozeroy', fillcolor='rgba(52, 152, 220, 0.05)',
            hovertemplate='%{x}<br>Queries: <b>%{y}</b><extra></extra>',
        ))
        fig_trend.update_layout(
            height=360,
            paper_bgcolor=PAPER, plot_bgcolor=PAPER,
            margin=dict(l=10, r=10, t=30, b=10),
            font=FONT, legend=LEGEND,
            hovermode='x unified',
            xaxis=dict(showgrid=False, tickfont=TICK,
                       linecolor='rgba(0,0,0,0)', tickcolor='rgba(0,0,0,0)'),
            yaxis=dict(showgrid=True, gridcolor=GRID, gridwidth=1, tickfont=TICK,
                       zeroline=False, linecolor='rgba(0,0,0,0)'),
        )
        st.plotly_chart(fig_trend, use_container_width=True, config={'displayModeBar': False})
        st.markdown('</div>', unsafe_allow_html=True)

    # ── FOOTER ────────────────────────────────────────────────────────────────
    st.markdown("""
    <div class="dash-footer">
        <span>© FMIS · Developed and prepared by OIM Team</span>
        <div class="footer-status">
            <div class="live-dot" style="width:0.35rem;height:0.35rem;background:#3498dc;"></div>
            All systems operational
        </div>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="FMIS Monitoring", page_icon="📊")
    Monitoring()




#kimiAI 

# import streamlit as st
# import plotly.graph_objects as go
# import plotly.express as px
# import pandas as pd
# import numpy as np
# from datetime import datetime, timedelta

# def Monitoring():
   
#     # Custom CSS - Clean, TV-optimized dark theme
#     st.markdown("""
#     <style>
#         @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
#         @import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24..48,100..700,0..1,0');
        
#         * {
#             font-family: 'Inter', sans-serif;
#         }
        
#         .stApp {
#             background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%);
#             color: #e2e8f0;
#         }
        
#         /* Glassmorphism Cards */
#         .glass-card {
#             background: rgba(30, 41, 59, 0.7);
#             backdrop-filter: blur(20px);
#             border: 1px solid rgba(255, 255, 255, 0.1);
#             border-radius: 1.5rem;
#             padding: 1.5rem;
#             box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5), 
#                         0 0 0 1px rgba(255, 255, 255, 0.05) inset;
#             transition: all 0.3s ease;
#         }
        
#         .glass-card:hover {
#             transform: translateY(-2px);
#             box-shadow: 0 30px 60px -12px rgba(0, 0, 0, 0.6), 
#                         0 0 0 1px rgba(255, 255, 255, 0.1) inset;
#             border-color: rgba(255, 255, 255, 0.15);
#         }
        
#         /* Stat Cards with Glow */
#         .stat-card {
#             background: linear-gradient(145deg, rgba(30, 41, 59, 0.9), rgba(15, 23, 42, 0.9));
#             border: 1px solid rgba(56, 189, 248, 0.2);
#             border-radius: 1.25rem;
#             padding: 1.5rem;
#             position: relative;
#             overflow: hidden;
#         }
        
#         .stat-card::before {
#             content: '';
#             position: absolute;
#             top: 0;
#             left: 0;
#             right: 0;
#             height: 3px;
#             background: linear-gradient(90deg, #38bdf8, #818cf8, #c084fc);
#         }
        
#         .stat-value-tv {
#             font-size: 2.5rem;
#             font-weight: 800;
#             background: linear-gradient(135deg, #fff 0%, #94a3b8 100%);
#             -webkit-background-clip: text;
#             -webkit-text-fill-color: transparent;
#             background-clip: text;
#             letter-spacing: -0.02em;
#         }
        
#         .stat-label-tv {
#             font-size: 0.875rem;
#             font-weight: 500;
#             color: #64748b;
#             text-transform: uppercase;
#             letter-spacing: 0.1em;
#             margin-top: 0.5rem;
#         }
        
#         /* Section Headers */
#         .section-header {
#             display: flex;
#             align-items: center;
#             gap: 0.75rem;
#             margin-bottom: 1.5rem;
#             padding-bottom: 0.75rem;
#             border-bottom: 1px solid rgba(255, 255, 255, 0.1);
#         }
        
#         .section-icon {
#             width: 2.5rem;
#             height: 2.5rem;
#             background: linear-gradient(135deg, #38bdf8, #818cf8);
#             border-radius: 0.75rem;
#             display: flex;
#             align-items: center;
#             justify-content: center;
#             color: white;
#             box-shadow: 0 10px 25px -5px rgba(56, 189, 248, 0.4);
#         }
        
#         .section-title {
#             font-size: 1.125rem;
#             font-weight: 700;
#             color: #f1f5f9;
#             letter-spacing: -0.01em;
#         }
        
#         /* TV Header */
#         .tv-header {
#             background: linear-gradient(145deg, rgba(15, 23, 42, 0.95), rgba(30, 41, 59, 0.95));
#             backdrop-filter: blur(20px);
#             border: 1px solid rgba(56, 189, 248, 0.2);
#             border-radius: 1.5rem;
#             padding: 1.5rem 2rem;
#             margin-bottom: 2rem;
#             box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
#             display: flex;
#             align-items: center;
#             justify-content: space-between;
#         }
        
#         .logo-badge {
#             width: 3.5rem;
#             height: 3.5rem;
#             background: linear-gradient(135deg, #38bdf8, #818cf8, #c084fc);
#             border-radius: 1rem;
#             display: flex;
#             align-items: center;
#             justify-content: center;
#             color: white;
#             font-weight: 800;
#             font-size: 1.25rem;
#             box-shadow: 0 10px 30px -5px rgba(56, 189, 248, 0.5);
#         }
        
#         .live-indicator {
#             display: flex;
#             align-items: center;
#             gap: 0.75rem;
#             background: rgba(56, 189, 248, 0.1);
#             border: 1px solid rgba(56, 189, 248, 0.3);
#             border-radius: 9999px;
#             padding: 0.5rem 1rem;
#         }
        
#         .pulse-dot {
#             width: 0.75rem;
#             height: 0.75rem;
#             background: #22c55e;
#             border-radius: 50%;
#             animation: pulse 2s infinite;
#             box-shadow: 0 0 20px rgba(34, 197, 94, 0.6);
#         }
        
#         @keyframes pulse {
#             0%, 100% { opacity: 1; transform: scale(1); }
#             50% { opacity: 0.5; transform: scale(1.2); }
#         }
        
#         /* Hide Streamlit elements */
#         #MainMenu, footer, header {visibility: hidden;}
#         .block-container {padding: 2rem; max-width: 100%;}
        
#         /* Footer */
#         .tv-footer {
#             margin-top: 3rem;
#             padding: 1.5rem 0;
#             border-top: 1px solid rgba(255, 255, 255, 0.1);
#             display: flex;
#             justify-content: space-between;
#             align-items: center;
#             color: #64748b;
#             font-size: 0.875rem;
#         }
        
#         .status-badge {
#             display: flex;
#             align-items: center;
#             gap: 0.5rem;
#             background: rgba(34, 197, 94, 0.1);
#             border: 1px solid rgba(34, 197, 94, 0.3);
#             border-radius: 9999px;
#             padding: 0.375rem 1rem;
#             color: #22c55e;
#             font-weight: 600;
#         }
#     </style>
#     """, unsafe_allow_html=True)

#     # TV Header
#     st.markdown("""
#     <div class="tv-header">
#         <div style="display: flex; align-items: center; gap: 1.25rem;">
#             <div class="logo-badge">FM</div>
#             <div>
#                 <div style="font-size: 1.5rem; font-weight: 800; color: #f1f5f9; letter-spacing: -0.02em;">FMIS Monitoring</div>
#                 <div style="font-size: 0.875rem; color: #64748b; margin-top: 0.25rem;">User & Report Analytics Dashboard</div>
#             </div>
#         </div>
#         <div class="live-indicator">
#             <span class="material-symbols-outlined" style="color: #38bdf8;">schedule</span>
#             <span style="color: #94a3b8; font-weight: 500;">LIVE</span>
#             <div class="pulse-dot"></div>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     # Generate sample data
#     @st.cache_data
#     def generate_data():
#         active_users = 2924
#         inactive_users_90d = 899
#         inactive_users_30d = 505
#         total_users = active_users + inactive_users_90d + inactive_users_30d
        
#         months = ['S', 'O', 'N', 'D', 'J', 'F', 'M', 'A', 'M', 'J', 'J', 'A']
#         this_year = [52, 68, 45, 82, 55, 70, 65, 92, 63, 80, 72, 100]
#         last_year = [45, 58, 38, 70, 48, 60, 55, 78, 52, 68, 62, 85]
        
#         entities = ['GDNT', 'PT006', 'PT018', 'PT002', 'PT004', 'PT008', 'LM10', 'GDPFMIT', 'PT020', 'PT012']
#         reports = [2145, 618, 458, 162, 385, 410, 258, 327, 174, 291]
#         queries = [1222, 151, 201, 410, 147, 119, 265, 166, 284, 117]
        
#         months_full = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#         reports_trend = [112, 120, 84, 110, 52, 69, 90, 44, 86, 16, 92, 48]
#         queries_trend = [33, 19, 39, 86, 37, 50, 25, 75, 30, 76, 33, 41]
        
#         return {
#             'active_users': active_users, 'inactive_users_90d': inactive_users_90d,
#             'inactive_users_30d': inactive_users_30d, 'total_users': total_users,
#             'account_locks': 1493, 'queries_reports': 74, 'failed_logins': 217,
#             'months': months, 'this_year': this_year, 'last_year': last_year,
#             'entities': entities, 'reports': reports, 'queries': queries,
#             'months_full': months_full, 'reports_trend': reports_trend, 'queries_trend': queries_trend
#         }

#     data = generate_data()

#     # Row 1: Metrics & Activity
#     col1, col2 = st.columns([5, 7])

#     with col1:
#         st.markdown("""
#         <div class="section-header">
#             <div class="section-icon">
#                 <span class="material-symbols-outlined">speed</span>
#             </div>
#             <div class="section-title">Activity Metrics</div>
#         </div>
#         """, unsafe_allow_html=True)
        
#         m1, m2 = st.columns(2)
        
#         with m1:
#             st.markdown(f"""
#             <div class="stat-card">
#                 <div style="display: flex; justify-content: space-between; align-items: flex-start;">
#                     <span class="material-symbols-outlined" style="font-size: 2.5rem; color: #38bdf8; opacity: 0.8;">group</span>
#                 </div>
#                 <div class="stat-value-tv">{data['total_users']:,}</div>
#                 <div class="stat-label-tv">Total Users</div>
#             </div>
#             """, unsafe_allow_html=True)
            
#             st.markdown(f"""
#             <div class="stat-card" style="margin-top: 1rem;">
#                 <div style="display: flex; justify-content: space-between; align-items: flex-start;">
#                     <span class="material-symbols-outlined" style="font-size: 2.5rem; color: #818cf8; opacity: 0.8;">search</span>
#                 </div>
#                 <div class="stat-value-tv">{data['queries_reports']}</div>
#                 <div class="stat-label-tv">Queries & Reports</div>
#             </div>
#             """, unsafe_allow_html=True)
        
#         with m2:
#             st.markdown(f"""
#             <div class="stat-card">
#                 <div style="display: flex; justify-content: space-between; align-items: flex-start;">
#                     <span class="material-symbols-outlined" style="font-size: 2.5rem; color: #fbbf24; opacity: 0.8;">lock</span>
#                 </div>
#                 <div class="stat-value-tv">{data['account_locks']:,}</div>
#                 <div class="stat-label-tv">Account Locks</div>
#             </div>
#             """, unsafe_allow_html=True)
            
#             st.markdown(f"""
#             <div class="stat-card" style="margin-top: 1rem;">
#                 <div style="display: flex; justify-content: space-between; align-items: flex-start;">
#                     <span class="material-symbols-outlined" style="font-size: 2.5rem; color: #f87171; opacity: 0.8;">warning</span>
#                 </div>
#                 <div class="stat-value-tv">{data['failed_logins']}</div>
#                 <div class="stat-label-tv">Failed Logins</div>
#             </div>
#             """, unsafe_allow_html=True)

#     with col2:
#         st.markdown("""
#         <div class="section-header">
#             <div class="section-icon">
#                 <span class="material-symbols-outlined">person_play</span>
#             </div>
#             <div class="section-title">User Activity</div>
#         </div>
#         """, unsafe_allow_html=True)
        
#         u1, u2 = st.columns(2)
        
#         with u1:
#             fig_donut = go.Figure()
#             fig_donut.add_trace(go.Pie(
#                 labels=['Active', 'Inactive (30d)', 'Inactive (90d)'],
#                 values=[data['active_users'], data['inactive_users_30d'], data['inactive_users_90d']],
#                 hole=0.75,
#                 marker=dict(colors=['#38bdf8', '#818cf8', '#fbbf24'], 
#                            line=dict(color='rgba(0,0,0,0.2)', width=2)),
#                 textinfo='none',
#                 hovertemplate='<b>%{label}</b><br>%{value:,} users<br>%{percent}<extra></extra>'
#             ))
            
#             fig_donut.update_layout(
#                 height=280,
#                 margin=dict(l=10, r=10, t=10, b=10),
#                 paper_bgcolor='rgba(0,0,0,0)',
#                 plot_bgcolor='rgba(0,0,0,0)',
#                 showlegend=False,
#                 annotations=[dict(
#                     text=f'<b>{data["total_users"]:,}</b><br>Total Users',
#                     x=0.5, y=0.5,
#                     font=dict(size=16, color='#f1f5f9', family='Inter'),
#                     showarrow=False
#                 )]
#             )
            
#             st.plotly_chart(fig_donut, use_container_width=True, config={'displayModeBar': False})
            
#             st.markdown(f"""
#             <div style="display: flex; justify-content: center; gap: 1.5rem; margin-top: 0.5rem;">
#                 <div style="display: flex; align-items: center; gap: 0.5rem;">
#                     <div style="width: 0.75rem; height: 0.75rem; border-radius: 50%; background: #38bdf8; box-shadow: 0 0 10px #38bdf8;"></div>
#                     <span style="color: #94a3b8; font-size: 0.875rem;">Active <b style="color: #f1f5f9;">{data['active_users']:,}</b></span>
#                 </div>
#                 <div style="display: flex; align-items: center; gap: 0.5rem;">
#                     <div style="width: 0.75rem; height: 0.75rem; border-radius: 50%; background: #818cf8;"></div>
#                     <span style="color: #94a3b8; font-size: 0.875rem;">30d <b style="color: #f1f5f9;">{data['inactive_users_30d']:,}</b></span>
#                 </div>
#                 <div style="display: flex; align-items: center; gap: 0.5rem;">
#                     <div style="width: 0.75rem; height: 0.75rem; border-radius: 50%; background: #fbbf24;"></div>
#                     <span style="color: #94a3b8; font-size: 0.875rem;">90d <b style="color: #f1f5f9;">{data['inactive_users_90d']:,}</b></span>
#                 </div>
#             </div>
#             """, unsafe_allow_html=True)
        
#         with u2:
#             fig_bars = go.Figure()
            
#             fig_bars.add_trace(go.Bar(
#                 x=data['months'],
#                 y=data['last_year'],
#                 name='Last Year',
#                 marker=dict(color='rgba(148, 163, 184, 0.3)', line=dict(color='rgba(148, 163, 184, 0.5)', width=1)),
#                 text=data['last_year'],
#                 textposition='outside',
#                 textfont=dict(size=10, color='#64748b')
#             ))
            
#             fig_bars.add_trace(go.Bar(
#                 x=data['months'],
#                 y=data['this_year'],
#                 name='This Year',
#                 marker=dict(
#                     color=data['this_year'],
#                     colorscale=[[0, '#38bdf8'], [0.5, '#818cf8'], [1, '#c084fc']],
#                     line=dict(color='rgba(255,255,255,0.2)', width=1)
#                 ),
#                 text=data['this_year'],
#                 textposition='outside',
#                 textfont=dict(size=10, color='#f1f5f9')
#             ))
            
#             fig_bars.update_layout(
#                 barmode='group',
#                 height=280,
#                 margin=dict(l=10, r=10, t=40, b=10),
#                 paper_bgcolor='rgba(0,0,0,0)',
#                 plot_bgcolor='rgba(0,0,0,0)',
#                 legend=dict(
#                     orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5,
#                     font=dict(size=11, color='#94a3b8'),
#                     bgcolor='rgba(0,0,0,0)'
#                 ),
#                 xaxis=dict(showgrid=False, tickfont=dict(size=11, color='#94a3b8')),
#                 yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.05)', tickfont=dict(size=10, color='#64748b'))
#             )
            
#             st.plotly_chart(fig_bars, use_container_width=True, config={'displayModeBar': False})

#     # Row 2: Analytics
#     col3, col4, col5 = st.columns([5, 3, 4])

#     with col3:
#         st.markdown("""
#         <div class="section-header">
#             <div class="section-icon">
#                 <span class="material-symbols-outlined">database</span>
#             </div>
#             <div class="section-title">Top 10 Active Entities</div>
#         </div>
#         """, unsafe_allow_html=True)
        
#         st.markdown("""
#         <div class="glass-card">
#             <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
#                 <span style="font-size: 0.875rem; color: #64748b;">Reports vs Queries Comparison</span>
#                 <span style="font-size: 0.75rem; padding: 0.375rem 0.75rem; background: rgba(56, 189, 248, 0.1); border: 1px solid rgba(56, 189, 248, 0.2); border-radius: 9999px; color: #38bdf8; font-weight: 600;">CURRENT MONTH</span>
#             </div>
#         """, unsafe_allow_html=True)
        
#         # Horizontal grouped bar chart for entities
#         entities_df = pd.DataFrame({
#             'Entity': data['entities'],
#             'Reports': data['reports'],
#             'Queries': data['queries']
#         })
        
#         fig_entities = go.Figure()
        
#         fig_entities.add_trace(go.Bar(
#             y=data['entities'][::-1],
#             x=data['reports'][::-1],
#             name='Reports',
#             orientation='h',
#             marker=dict(color='#38bdf8', line=dict(color='rgba(255,255,255,0.2)', width=1)),
#             text=data['reports'][::-1],
#             textposition='outside',
#             textfont=dict(size=10, color='#f1f5f9')
#         ))
        
#         fig_entities.add_trace(go.Bar(
#             y=data['entities'][::-1],
#             x=data['queries'][::-1],
#             name='Queries',
#             orientation='h',
#             marker=dict(color='#818cf8', line=dict(color='rgba(255,255,255,0.2)', width=1)),
#             text=data['queries'][::-1],
#             textposition='outside',
#             textfont=dict(size=10, color='#f1f5f9')
#         ))
        
#         fig_entities.update_layout(
#             barmode='group',
#             height=400,
#             margin=dict(l=80, r=80, t=20, b=20),
#             paper_bgcolor='rgba(0,0,0,0)',
#             plot_bgcolor='rgba(0,0,0,0)',
#             legend=dict(
#                 orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5,
#                 font=dict(size=12, color='#94a3b8'),
#                 bgcolor='rgba(0,0,0,0)'
#             ),
#             xaxis=dict(
#                 showgrid=True, 
#                 gridcolor='rgba(255,255,255,0.05)',
#                 tickfont=dict(size=10, color='#64748b'),
#                 title=dict(text='Count', font=dict(size=11, color='#64748b'))
#             ),
#             yaxis=dict(
#                 showgrid=False,
#                 tickfont=dict(size=11, color='#f1f5f9'),
#                 autorange='reversed'
#             ),
#             bargap=0.3,
#             bargroupgap=0.1
#         )
        
#         st.plotly_chart(fig_entities, use_container_width=True, config={'displayModeBar': False})
#         st.markdown("</div>", unsafe_allow_html=True)

#     with col4:
#         st.markdown("""
#         <div class="section-header">
#             <div class="section-icon">
#                 <span class="material-symbols-outlined">donut_large</span>
#             </div>
#             <div class="section-title">Usage Type</div>
#         </div>
#         """, unsafe_allow_html=True)
        
#         fig_type = go.Figure()
#         fig_type.add_trace(go.Pie(
#             labels=['Reports', 'Queries'],
#             values=[53, 21],
#             hole=0.7,
#             marker=dict(colors=['#38bdf8', '#818cf8'], line=dict(color='rgba(0,0,0,0.3)', width=2)),
#             textinfo='none',
#             hovertemplate='<b>%{label}</b><br>%{value}<extra></extra>'
#         ))
        
#         fig_type.update_layout(
#             height=300,
#             margin=dict(l=10, r=10, t=10, b=10),
#             paper_bgcolor='rgba(0,0,0,0)',
#             plot_bgcolor='rgba(0,0,0,0)',
#             showlegend=False,
#             annotations=[dict(
#                 text='<b>74</b><br>Total',
#                 x=0.5, y=0.5,
#                 font=dict(size=18, color='#f1f5f9', family='Inter'),
#                 showarrow=False
#             )]
#         )
        
#         st.plotly_chart(fig_type, use_container_width=True, config={'displayModeBar': False})
        
#         st.markdown("""
#         <div style="display: flex; justify-content: center; gap: 2rem; margin-top: 1rem;">
#             <div style="text-align: center;">
#                 <div style="font-size: 2rem; font-weight: 800; color: #38bdf8;">53</div>
#                 <div style="font-size: 0.875rem; color: #64748b;">Reports</div>
#                 <div style="font-size: 0.75rem; color: #22c55e; margin-top: 0.25rem;">▲ 12%</div>
#             </div>
#             <div style="width: 1px; background: rgba(255,255,255,0.1);"></div>
#             <div style="text-align: center;">
#                 <div style="font-size: 2rem; font-weight: 800; color: #818cf8;">21</div>
#                 <div style="font-size: 0.875rem; color: #64748b;">Queries</div>
#                 <div style="font-size: 0.75rem; color: #22c55e; margin-top: 0.25rem;">▲ 8%</div>
#             </div>
#         </div>
#         """, unsafe_allow_html=True)

#     with col5:
#         st.markdown("""
#         <div class="section-header">
#             <div class="section-icon">
#                 <span class="material-symbols-outlined">trending_up</span>
#             </div>
#             <div class="section-title">Activity Trends</div>
#         </div>
#         """, unsafe_allow_html=True)
        
#         fig_trends = go.Figure()
        
#         fig_trends.add_trace(go.Scatter(
#             x=data['months_full'],
#             y=data['reports_trend'],
#             name='Reports',
#             line=dict(color='#38bdf8', width=4),
#             mode='lines+markers',
#             marker=dict(size=8, color='#38bdf8', line=dict(color='#0f172a', width=2)),
#             fill='tozeroy',
#             fillcolor='rgba(56, 189, 248, 0.1)'
#         ))
        
#         fig_trends.add_trace(go.Scatter(
#             x=data['months_full'],
#             y=data['queries_trend'],
#             name='Queries',
#             line=dict(color='#818cf8', width=4),
#             mode='lines+markers',
#             marker=dict(size=8, color='#818cf8', line=dict(color='#0f172a', width=2)),
#             fill='tozeroy',
#             fillcolor='rgba(129, 140, 248, 0.1)'
#         ))
        
#         fig_trends.update_layout(
#             height=350,
#             margin=dict(l=10, r=10, t=40, b=10),
#             paper_bgcolor='rgba(0,0,0,0)',
#             plot_bgcolor='rgba(0,0,0,0)',
#             legend=dict(
#                 orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5,
#                 font=dict(size=12, color='#94a3b8'),
#                 bgcolor='rgba(0,0,0,0)'
#             ),
#             xaxis=dict(showgrid=False, tickfont=dict(size=11, color='#94a3b8')),
#             yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.05)', tickfont=dict(size=10, color='#64748b'))
#         )
        
#         st.plotly_chart(fig_trends, use_container_width=True, config={'displayModeBar': False})

#     # Footer
#     st.markdown("""
#     <div class="tv-footer">
#         <div style="display: flex; align-items: center; gap: 1rem;">
#             <span style="font-weight: 600; color: #f1f5f9;">FMIS</span>
#             <span style="color: #475569;">|</span>
#             <span>Developed by OIM Team</span>
#         </div>
#         <div class="status-badge">
#             <span class="material-symbols-outlined" style="font-size: 1rem;">check_circle</span>
#             All Systems Operational
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

# if __name__ == "__main__":
#     Monitoring()




# import streamlit as st
# import plotly.graph_objects as go

# def Monitoring():

#     st.markdown("""
#     <style>
#         @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700&family=DM+Mono:wght@400;500&display=swap');
#         @import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@24,400,1,0');

#         * { font-family: 'DM Sans', sans-serif; box-sizing: border-box; }

#         html, body, .stApp { background: #0b0f1a; color: #e2e8f0; }

#         .block-container {
#             padding: 1.5rem 2rem 1rem 2rem !important;
#             max-width: 100% !important;
#         }

#         #MainMenu, footer, header { visibility: hidden; }
#         .stDeployButton { display: none; }

#         /* HEADER */
#         .dash-header {
#             display: flex; align-items: center; justify-content: space-between;
#             background: linear-gradient(135deg, #111827 0%, #1a2235 100%);
#             border: 1px solid rgba(99,179,237,0.15);
#             border-radius: 1rem;
#             padding: 0.875rem 1.5rem;
#             margin-bottom: 1.5rem;
#             box-shadow: 0 0 40px rgba(49,130,206,0.06);
#         }
#         .dash-logo {
#             width: 2.75rem; height: 2.75rem;
#             border-radius: 0.65rem;
#             background: linear-gradient(135deg, #1e3a5f, #3182ce);
#             display: flex; align-items: center; justify-content: center;
#             font-weight: 700; font-size: 0.9rem; color: #fff;
#             letter-spacing: 0.05em;
#             border: 1px solid rgba(99,179,237,0.3);
#             box-shadow: 0 0 20px rgba(49,130,206,0.25);
#         }
#         .dash-title { font-size: 1rem; font-weight: 600; color: #e2e8f0; letter-spacing: -0.01em; }
#         .dash-subtitle { font-size: 0.75rem; color: #64748b; font-weight: 400; margin-top: 0.1rem; }
#         .live-pill {
#             display: flex; align-items: center; gap: 0.5rem;
#             background: rgba(56,161,105,0.12);
#             border: 1px solid rgba(56,161,105,0.25);
#             border-radius: 9999px;
#             padding: 0.35rem 0.875rem;
#             font-size: 0.75rem; font-weight: 600; color: #68d391;
#             letter-spacing: 0.05em;
#         }
#         .live-dot {
#             width: 0.45rem; height: 0.45rem;
#             border-radius: 9999px; background: #38a169;
#             box-shadow: 0 0 6px #38a169;
#             animation: pulse 2s ease-in-out infinite;
#         }
#         @keyframes pulse {
#             0%, 100% { opacity: 1; box-shadow: 0 0 6px #38a169; }
#             50%       { opacity: 0.6; box-shadow: 0 0 12px #38a169; }
#         }

#         /* SECTION LABEL */
#         .section-label {
#             font-size: 0.65rem; font-weight: 700;
#             text-transform: uppercase; letter-spacing: 0.1em;
#             color: #4a6fa5; margin-bottom: 0.75rem;
#             display: flex; align-items: center; gap: 0.4rem;
#         }
#         .section-label::before {
#             content: ''; display: inline-block;
#             width: 0.2rem; height: 0.8rem;
#             background: #3182ce; border-radius: 2px;
#         }

#         /* METRIC CARDS */
#         .metric-card {
#             background: linear-gradient(145deg, #111827, #1a2235);
#             border: 1px solid rgba(99,179,237,0.1);
#             border-radius: 0.875rem;
#             padding: 1.125rem 1.25rem;
#             margin-bottom: 0.75rem;
#             position: relative; overflow: hidden;
#         }
#         .metric-card::after {
#             content: ''; position: absolute;
#             top: 0; left: 0; right: 0; height: 2px;
#             border-radius: 0.875rem 0.875rem 0 0;
#         }
#         .metric-card.blue::after   { background: linear-gradient(90deg, #3182ce, #63b3ed); }
#         .metric-card.orange::after { background: linear-gradient(90deg, #dd6b20, #f6ad55); }
#         .metric-card.red::after    { background: linear-gradient(90deg, #c53030, #fc8181); }
#         .metric-card.teal::after   { background: linear-gradient(90deg, #2c7a7b, #81e6d9); }

#         .metric-icon { font-family: 'Material Symbols Rounded'; font-size: 1.5rem; line-height: 1; }
#         .metric-icon.blue   { color: #63b3ed; }
#         .metric-icon.orange { color: #f6ad55; }
#         .metric-icon.red    { color: #fc8181; }
#         .metric-icon.teal   { color: #81e6d9; }

#         .metric-value {
#             font-size: 2rem; font-weight: 700;
#             letter-spacing: -0.04em; color: #f7fafc;
#             line-height: 1.1; margin-top: 0.625rem;
#         }
#         .metric-label {
#             font-size: 0.7rem; font-weight: 500;
#             text-transform: uppercase; letter-spacing: 0.06em;
#             color: #4a5568; margin-top: 0.25rem;
#         }

#         /* CHART CARD */
#         .chart-card {
#             background: linear-gradient(145deg, #111827, #1a2235);
#             border: 1px solid rgba(99,179,237,0.1);
#             border-radius: 0.875rem;
#             padding: 1.125rem 1.25rem 0.75rem 1.25rem;
#             margin-bottom: 0.75rem;
#         }
#         .chart-title { font-size: 0.8rem; font-weight: 600; color: #cbd5e0; margin-bottom: 0.25rem; }
#         .chart-meta  { font-size: 0.65rem; color: #4a6fa5; margin-bottom: 0.75rem; }

#         /* LEGEND */
#         .legend-row  { display: flex; gap: 1.25rem; justify-content: center; margin-top: 0.5rem; }
#         .legend-item { display: flex; align-items: center; gap: 0.35rem; font-size: 0.72rem; color: #94a3b8; }
#         .legend-dot  { width: 0.55rem; height: 0.55rem; border-radius: 9999px; }

#         /* FOOTER */
#         .dash-footer {
#             display: flex; justify-content: space-between; align-items: center;
#             padding-top: 0.75rem;
#             border-top: 1px solid rgba(99,179,237,0.08);
#             font-size: 0.65rem; color: #334155; margin-top: 0.5rem;
#         }
#         .footer-status { display: flex; align-items: center; gap: 0.4rem; color: #48bb78; font-weight: 500; }
#     </style>
#     """, unsafe_allow_html=True)

#     # ── DATA ──────────────────────────────────────────────────────────────────
#     @st.cache_data
#     def generate_data():
#         entities      = ['GDNT','PT006','PT018','PT002','PT004','PT008','LM10','GDPFMIT','PT020','PT012']
#         reports       = [2145, 618, 458, 162, 385, 410, 258, 327, 174, 291]
#         queries       = [1222, 151, 201, 410, 147, 119, 265, 166, 284, 117]
#         months_short  = ['S','O','N','D','J','F','M','A','M','J','J','A']
#         this_year     = [52, 68, 45, 82, 55, 70, 65, 92, 63, 80, 72, 100]
#         last_year     = [45, 58, 38, 70, 48, 60, 55, 78, 52, 68, 62, 85]
#         months_full   = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
#         reports_trend = [112, 120, 84, 110, 52, 69, 90, 44, 86, 16, 92, 48]
#         queries_trend = [33,  19,  39,  86, 37, 50, 25, 75, 30, 76, 33, 41]
#         return dict(
#             active=2924, inactive_30=505, inactive_90=899,
#             total_users=4328, account_locks=1493, queries_reports=74, failed_logins=217,
#             entities=entities, reports=reports, queries=queries,
#             months_short=months_short, this_year=this_year, last_year=last_year,
#             months_full=months_full, reports_trend=reports_trend, queries_trend=queries_trend,
#         )

#     d = generate_data()

#     # ── SHARED CHART CONSTANTS ────────────────────────────────────────────────
#     PAPER  = 'rgba(0,0,0,0)'
#     GRID   = 'rgba(99,179,237,0.07)'
#     TICK   = dict(color='#4a6fa5', size=11, family='DM Sans')
#     FONT   = dict(family='DM Sans', color='#94a3b8')
#     LEGEND = dict(
#         orientation='h', yanchor='bottom', y=1.02,
#         xanchor='center', x=0.5,
#         font=dict(size=11, family='DM Sans'),
#         bgcolor='rgba(0,0,0,0)', borderwidth=0,
#     )

#     # ── HEADER ────────────────────────────────────────────────────────────────
#     st.markdown("""
#     <div class="dash-header">
#         <div style="display:flex;align-items:center;gap:1rem;">
#             <div class="dash-logo">FM</div>
#             <div style="height:1.5rem;width:1px;background:rgba(99,179,237,0.15);"></div>
#             <div>
#                 <div class="dash-title">FMIS Monitoring</div>
#                 <div class="dash-subtitle">User &amp; Report Analytics · OIM Team</div>
#             </div>
#         </div>
#         <div class="live-pill"><div class="live-dot"></div>LIVE</div>
#     </div>
#     """, unsafe_allow_html=True)

#     # ══════════════════════════════════════════════════════════════════════════
#     # ROW 1 — Metric cards | Account status donut | New users bar
#     # ══════════════════════════════════════════════════════════════════════════
#     col_m, col_charts = st.columns([2, 5])

#     with col_m:
#         st.markdown('<div class="section-label">Activity Metrics</div>', unsafe_allow_html=True)
#         for icon, color, val, label in [
#             ("group",   "blue",   f"{d['total_users']:,}",  "Total Users"),
#             ("lock",    "orange", f"{d['account_locks']:,}", "Account Locks"),
#             ("search",  "teal",   str(d['queries_reports']), "Queries & Reports"),
#             ("warning", "red",    str(d['failed_logins']),   "Failed Logins"),
#         ]:
#             st.markdown(f"""
#             <div class="metric-card {color}">
#                 <span class="metric-icon {color}">{icon}</span>
#                 <div class="metric-value">{val}</div>
#                 <div class="metric-label">{label}</div>
#             </div>""", unsafe_allow_html=True)

#     with col_charts:
#         st.markdown('<div class="section-label">User Activity</div>', unsafe_allow_html=True)
#         cc1, cc2 = st.columns(2)

#         # Donut — Account Status
#         with cc1:
#             st.markdown("""
#             <div class="chart-card">
#                 <div class="chart-title">Account Status</div>
#                 <div class="chart-meta">Current period breakdown</div>
#             """, unsafe_allow_html=True)

#             fig_donut = go.Figure()
#             fig_donut.add_trace(go.Pie(
#                 labels=['Active', 'Inactive (30d)', 'Inactive (90d)'],
#                 values=[d['active'], d['inactive_30'], d['inactive_90']],
#                 hole=0.68,
#                 marker=dict(colors=['#3182ce','#63b3ed','#dd6b20'],
#                             line=dict(color='#0b0f1a', width=3)),
#                 textinfo='none', showlegend=False, sort=False,
#                 hovertemplate='<b>%{label}</b><br>%{value:,} users · %{percent}<extra></extra>',
#             ))
#             fig_donut.update_layout(
#                 height=240,
#                 paper_bgcolor=PAPER, plot_bgcolor=PAPER,
#                 margin=dict(l=10, r=10, t=10, b=10),
#                 font=FONT,
#                 annotations=[dict(
#                     text=f'<b>{d["total_users"]:,}</b><br>Users',
#                     x=0.5, y=0.5,
#                     font=dict(size=13, color='#e2e8f0'),
#                     showarrow=False,
#                 )],
#             )
#             st.plotly_chart(fig_donut, use_container_width=True, config={'displayModeBar': False})
#             st.markdown("""
#             <div class="legend-row">
#                 <div class="legend-item"><div class="legend-dot" style="background:#3182ce"></div>Active {:,}</div>
#                 <div class="legend-item"><div class="legend-dot" style="background:#63b3ed"></div>Inactive 30d {:,}</div>
#                 <div class="legend-item"><div class="legend-dot" style="background:#dd6b20"></div>Inactive 90d {:,}</div>
#             </div></div>
#             """.format(d['active'], d['inactive_30'], d['inactive_90']), unsafe_allow_html=True)

#         # Grouped Bar — New Users
#         with cc2:
#             st.markdown("""
#             <div class="chart-card">
#                 <div class="chart-title">New Users · Monthly</div>
#                 <div class="chart-meta">This year vs last year</div>
#             """, unsafe_allow_html=True)

#             fig_bar = go.Figure()
#             fig_bar.add_trace(go.Bar(
#                 x=d['months_short'], y=d['last_year'], name='Last Year',
#                 marker=dict(color='rgba(100,116,139,0.5)', line=dict(width=0)),
#             ))
#             fig_bar.add_trace(go.Bar(
#                 x=d['months_short'], y=d['this_year'], name='This Year',
#                 marker=dict(
#                     color=d['this_year'],
#                     colorscale=[[0,'#1e3a5f'],[1,'#63b3ed']],
#                     showscale=False, line=dict(width=0),
#                 ),
#             ))
#             fig_bar.update_layout(
#                 height=240,
#                 paper_bgcolor=PAPER, plot_bgcolor=PAPER,
#                 margin=dict(l=10, r=10, t=30, b=10),
#                 font=FONT, legend=LEGEND,
#                 barmode='group', bargap=0.25, bargroupgap=0.05,
#                 xaxis=dict(showgrid=False, tickfont=TICK,
#                            tickcolor='rgba(0,0,0,0)', linecolor='rgba(0,0,0,0)'),
#                 yaxis=dict(showgrid=True, gridcolor=GRID, gridwidth=1, tickfont=TICK,
#                            zeroline=False, linecolor='rgba(0,0,0,0)'),
#             )
#             st.plotly_chart(fig_bar, use_container_width=True, config={'displayModeBar': False})
#             st.markdown('</div>', unsafe_allow_html=True)

#     # ══════════════════════════════════════════════════════════════════════════
#     # ROW 2 — Top 10 Entities | Usage type donut | Activity trends
#     # ══════════════════════════════════════════════════════════════════════════
#     col_ent, col_usage, col_trend = st.columns([5, 2, 5])

#     # Horizontal Stacked Bar — Top 10 Entities
#     with col_ent:
#         st.markdown('<div class="section-label">Report Usage Analytics</div>', unsafe_allow_html=True)
#         st.markdown("""
#         <div class="chart-card">
#             <div class="chart-title">Top 10 Active Entities · Reports &amp; Queries</div>
#             <div class="chart-meta">Current month · Sorted by total volume</div>
#         """, unsafe_allow_html=True)

#         entities = d['entities']
#         reports  = d['reports']
#         queries  = d['queries']

#         order      = sorted(range(len(entities)), key=lambda i: reports[i] + queries[i])
#         ent_sorted = [entities[i] for i in order]
#         rep_sorted = [reports[i]  for i in order]
#         qry_sorted = [queries[i]  for i in order]

#         fig_hbar = go.Figure()
#         fig_hbar.add_trace(go.Bar(
#             y=ent_sorted, x=rep_sorted, name='Reports', orientation='h',
#             marker=dict(color='#2b6cb0', line=dict(width=0)),
#             text=[f'{v:,}' for v in rep_sorted],
#             textposition='inside', insidetextanchor='end',
#             textfont=dict(color='#e2e8f0', size=11, family='DM Mono'),
#             hovertemplate='<b>%{y}</b><br>Reports: %{x:,}<extra></extra>',
#         ))
#         fig_hbar.add_trace(go.Bar(
#             y=ent_sorted, x=qry_sorted, name='Queries', orientation='h',
#             marker=dict(color='#63b3ed', line=dict(width=0)),
#             text=[f'{v:,}' for v in qry_sorted],
#             textposition='inside', insidetextanchor='end',
#             textfont=dict(color='#1a2235', size=11, family='DM Mono'),
#             hovertemplate='<b>%{y}</b><br>Queries: %{x:,}<extra></extra>',
#         ))
#         fig_hbar.update_layout(
#             height=360,
#             paper_bgcolor=PAPER, plot_bgcolor=PAPER,
#             margin=dict(l=80, r=20, t=30, b=10),
#             font=FONT, legend=LEGEND,
#             barmode='stack', bargap=0.25,
#             xaxis=dict(showgrid=True, gridcolor=GRID, gridwidth=1,
#                        tickfont=TICK, zeroline=False,
#                        linecolor='rgba(0,0,0,0)', tickformat=','),
#             yaxis=dict(showgrid=False,
#                        tickfont=dict(color='#94a3b8', size=12, family='DM Mono'),
#                        linecolor='rgba(0,0,0,0)', categoryorder='total ascending'),
#         )
#         st.plotly_chart(fig_hbar, use_container_width=True, config={'displayModeBar': False})
#         st.markdown("""
#         <div class="legend-row" style="margin-bottom:0.25rem">
#             <div class="legend-item"><div class="legend-dot" style="background:#2b6cb0"></div>Reports</div>
#             <div class="legend-item"><div class="legend-dot" style="background:#63b3ed"></div>Queries</div>
#         </div></div>
#         """, unsafe_allow_html=True)

#     # Donut — Usage by Type
#     with col_usage:
#         st.markdown('<div class="section-label">Usage Type</div>', unsafe_allow_html=True)
#         st.markdown("""
#         <div class="chart-card">
#             <div class="chart-title">Usage by Type</div>
#             <div class="chart-meta">Reports vs Queries</div>
#         """, unsafe_allow_html=True)

#         fig_type = go.Figure()
#         fig_type.add_trace(go.Pie(
#             labels=['Reports', 'Queries'], values=[53, 21],
#             hole=0.68,
#             marker=dict(colors=['#2b6cb0','#63b3ed'],
#                         line=dict(color='#0b0f1a', width=3)),
#             textinfo='none', showlegend=False,
#             hovertemplate='<b>%{label}</b><br>%{value} · %{percent}<extra></extra>',
#         ))
#         fig_type.update_layout(
#             height=220,
#             paper_bgcolor=PAPER, plot_bgcolor=PAPER,
#             margin=dict(l=10, r=10, t=10, b=10),
#             font=FONT,
#             annotations=[dict(
#                 text='<b>74</b><br>Total',
#                 x=0.5, y=0.5,
#                 font=dict(size=13, color='#e2e8f0'),
#                 showarrow=False,
#             )],
#         )
#         st.plotly_chart(fig_type, use_container_width=True, config={'displayModeBar': False})
#         st.markdown("""
#         <div class="legend-row" style="flex-direction:column;align-items:center;gap:0.5rem;margin-bottom:0.5rem">
#             <div class="legend-item">
#                 <div class="legend-dot" style="background:#2b6cb0;width:0.75rem;height:0.75rem"></div>
#                 Reports &nbsp;<b style="color:#e2e8f0">53</b>
#             </div>
#             <div class="legend-item">
#                 <div class="legend-dot" style="background:#63b3ed;width:0.75rem;height:0.75rem"></div>
#                 Queries &nbsp;<b style="color:#e2e8f0">21</b>
#             </div>
#         </div></div>
#         """, unsafe_allow_html=True)

#     # Line chart — Activity Trends
#     with col_trend:
#         st.markdown('<div class="section-label">Activity Trends</div>', unsafe_allow_html=True)
#         st.markdown("""
#         <div class="chart-card">
#             <div class="chart-title">Monthly Activity Trends</div>
#             <div class="chart-meta">Reports &amp; Queries over the year</div>
#         """, unsafe_allow_html=True)

#         fig_trend = go.Figure()
#         fig_trend.add_trace(go.Scatter(
#             x=d['months_full'], y=d['reports_trend'], name='Reports',
#             line=dict(color='#3182ce', width=2.5, shape='spline', smoothing=0.8),
#             mode='lines+markers',
#             marker=dict(size=6, color='#3182ce', line=dict(width=2, color='#0b0f1a')),
#             fill='tozeroy', fillcolor='rgba(49,130,206,0.07)',
#             hovertemplate='%{x}<br>Reports: <b>%{y}</b><extra></extra>',
#         ))
#         fig_trend.add_trace(go.Scatter(
#             x=d['months_full'], y=d['queries_trend'], name='Queries',
#             line=dict(color='#63b3ed', width=2.5, shape='spline', smoothing=0.8, dash='dot'),
#             mode='lines+markers',
#             marker=dict(size=6, color='#63b3ed', line=dict(width=2, color='#0b0f1a')),
#             fill='tozeroy', fillcolor='rgba(99,179,237,0.05)',
#             hovertemplate='%{x}<br>Queries: <b>%{y}</b><extra></extra>',
#         ))
#         fig_trend.update_layout(
#             height=360,
#             paper_bgcolor=PAPER, plot_bgcolor=PAPER,
#             margin=dict(l=10, r=10, t=30, b=10),
#             font=FONT, legend=LEGEND,
#             hovermode='x unified',
#             xaxis=dict(showgrid=False, tickfont=TICK,
#                        linecolor='rgba(0,0,0,0)', tickcolor='rgba(0,0,0,0)'),
#             yaxis=dict(showgrid=True, gridcolor=GRID, gridwidth=1, tickfont=TICK,
#                        zeroline=False, linecolor='rgba(0,0,0,0)'),
#         )
#         st.plotly_chart(fig_trend, use_container_width=True, config={'displayModeBar': False})
#         st.markdown('</div>', unsafe_allow_html=True)

#     # ── FOOTER ────────────────────────────────────────────────────────────────
#     st.markdown("""
#     <div class="dash-footer">
#         <span>© FMIS · Developed and prepared by OIM Team</span>
#         <div class="footer-status">
#             <div class="live-dot" style="width:0.35rem;height:0.35rem"></div>
#             All systems operational
#         </div>
#     </div>
#     """, unsafe_allow_html=True)


# if __name__ == "__main__":
#     st.set_page_config(layout="wide", page_title="FMIS Monitoring", page_icon="📊")
#     Monitoring()


# import streamlit as st
# import plotly.graph_objects as go
# import plotly.express as px
# import pandas as pd
# import numpy as np
# from datetime import datetime, timedelta

# def Monitoring():
   
#     # Custom CSS - Clean, light mode theme
#     st.markdown("""
#     <style>
#         @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
#         @import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24..48,100..700,0..1,0');
        
#         * {
#             font-family: 'Inter', sans-serif;
#         }
        
#         .stApp {
#             background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 50%, #e2e8f0 100%);
#             color: #0f172a;
#         }
        
#         /* Glassmorphism Cards - Light mode */
#         .glass-card {
#             background: rgba(255, 255, 255, 0.7);
#             backdrop-filter: blur(20px);
#             border: 1px solid rgba(0, 0, 0, 0.05);
#             border-radius: 1.5rem;
#             padding: 1.5rem;
#             box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.15), 
#                         0 0 0 1px rgba(255, 255, 255, 0.5) inset;
#             transition: all 0.3s ease;
#         }
        
#         .glass-card:hover {
#             transform: translateY(-2px);
#             box-shadow: 0 30px 60px -12px rgba(0, 0, 0, 0.2), 
#                         0 0 0 1px rgba(255, 255, 255, 0.8) inset;
#             border-color: rgba(0, 0, 0, 0.1);
#         }
        
#         /* Stat Cards with Glow - Light mode */
#         .stat-card {
#             background: linear-gradient(145deg, #ffffff, #f8fafc);
#             border: 1px solid rgba(37, 99, 235, 0.1);
#             border-radius: 1.25rem;
#             padding: 1.5rem;
#             position: relative;
#             overflow: hidden;
#             box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
#         }
        
#         .stat-card::before {
#             content: '';
#             position: absolute;
#             top: 0;
#             left: 0;
#             right: 0;
#             height: 3px;
#             background: linear-gradient(90deg, #2563eb, #7c3aed, #db2777);
#         }
        
#         .stat-value-tv {
#             font-size: 2.5rem;
#             font-weight: 800;
#             background: linear-gradient(135deg, #0f172a 0%, #334155 100%);
#             -webkit-background-clip: text;
#             -webkit-text-fill-color: transparent;
#             background-clip: text;
#             letter-spacing: -0.02em;
#         }
        
#         .stat-label-tv {
#             font-size: 0.875rem;
#             font-weight: 600;
#             color: #64748b;
#             text-transform: uppercase;
#             letter-spacing: 0.1em;
#             margin-top: 0.5rem;
#         }
        
#         /* Section Headers - Light mode */
#         .section-header {
#             display: flex;
#             align-items: center;
#             gap: 0.75rem;
#             margin-bottom: 1.5rem;
#             padding-bottom: 0.75rem;
#             border-bottom: 1px solid rgba(0, 0, 0, 0.1);
#         }
        
#         .section-icon {
#             width: 2.5rem;
#             height: 2.5rem;
#             background: linear-gradient(135deg, #2563eb, #7c3aed);
#             border-radius: 0.75rem;
#             display: flex;
#             align-items: center;
#             justify-content: center;
#             color: white;
#             box-shadow: 0 10px 25px -5px rgba(37, 99, 235, 0.3);
#         }
        
#         .section-title {
#             font-size: 1.125rem;
#             font-weight: 700;
#             color: #0f172a;
#             letter-spacing: -0.01em;
#         }
        
#         /* TV Header - Light mode */
#         .tv-header {
#             background: linear-gradient(145deg, #ffffff, #f8fafc);
#             backdrop-filter: blur(20px);
#             border: 1px solid rgba(0, 0, 0, 0.1);
#             border-radius: 1.5rem;
#             padding: 1.5rem 2rem;
#             margin-bottom: 2rem;
#             box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.15);
#             display: flex;
#             align-items: center;
#             justify-content: space-between;
#         }
        
#         .logo-badge {
#             width: 3.5rem;
#             height: 3.5rem;
#             background: linear-gradient(135deg, #2563eb, #7c3aed, #db2777);
#             border-radius: 1rem;
#             display: flex;
#             align-items: center;
#             justify-content: center;
#             color: white;
#             font-weight: 800;
#             font-size: 1.25rem;
#             box-shadow: 0 10px 30px -5px rgba(37, 99, 235, 0.4);
#         }
        
#         .live-indicator {
#             display: flex;
#             align-items: center;
#             gap: 0.75rem;
#             background: rgba(37, 99, 235, 0.1);
#             border: 1px solid rgba(37, 99, 235, 0.2);
#             border-radius: 9999px;
#             padding: 0.5rem 1rem;
#         }
        
#         .pulse-dot {
#             width: 0.75rem;
#             height: 0.75rem;
#             background: #16a34a;
#             border-radius: 50%;
#             animation: pulse 2s infinite;
#             box-shadow: 0 0 20px rgba(22, 163, 74, 0.4);
#         }
        
#         @keyframes pulse {
#             0%, 100% { opacity: 1; transform: scale(1); }
#             50% { opacity: 0.5; transform: scale(1.2); }
#         }
        
#         /* Hide Streamlit elements */
#         #MainMenu, footer, header {visibility: hidden;}
#         .block-container {padding: 2rem; max-width: 100%;}
        
#         /* Footer - Light mode */
#         .tv-footer {
#             margin-top: 3rem;
#             padding: 1.5rem 0;
#             border-top: 1px solid rgba(0, 0, 0, 0.1);
#             display: flex;
#             justify-content: space-between;
#             align-items: center;
#             color: #64748b;
#             font-size: 0.875rem;
#         }
        
#         .status-badge {
#             display: flex;
#             align-items: center;
#             gap: 0.5rem;
#             background: rgba(22, 163, 74, 0.1);
#             border: 1px solid rgba(22, 163, 74, 0.2);
#             border-radius: 9999px;
#             padding: 0.375rem 1rem;
#             color: #16a34a;
#             font-weight: 600;
#         }
        
#         /* Light mode text adjustments */
#         .material-symbols-outlined {
#             color: #0f172a;
#         }
        
#         .stPlotlyChart {
#             background: transparent;
#         }
#     </style>
#     """, unsafe_allow_html=True)

#     # TV Header with updated label
#     st.markdown("""
#     <div class="tv-header">
#         <div style="display: flex; align-items: center; gap: 1.25rem;">
#             <div class="logo-badge">DA</div>
#             <div>
#                 <div style="font-size: 1.5rem; font-weight: 800; color: #0f172a; letter-spacing: -0.02em;">Dashboard Analytics</div>
#                 <div style="font-size: 0.875rem; color: #64748b; margin-top: 0.25rem;">User & Report Performance Metrics</div>
#             </div>
#         </div>
#         <div class="live-indicator">
#             <span class="material-symbols-outlined" style="color: #2563eb;">schedule</span>
#             <span style="color: #475569; font-weight: 500;">LIVE</span>
#             <div class="pulse-dot"></div>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     # Generate sample data
#     @st.cache_data
#     def generate_data():
#         active_users = 2924
#         inactive_users_90d = 899
#         inactive_users_30d = 505
#         total_users = active_users + inactive_users_90d + inactive_users_30d
        
#         months = ['S', 'O', 'N', 'D', 'J', 'F', 'M', 'A', 'M', 'J', 'J', 'A']
#         this_year = [52, 68, 45, 82, 55, 70, 65, 92, 63, 80, 72, 100]
#         last_year = [45, 58, 38, 70, 48, 60, 55, 78, 52, 68, 62, 85]
        
#         entities = ['GDNT', 'PT006', 'PT018', 'PT002', 'PT004', 'PT008', 'LM10', 'GDPFMIT', 'PT020', 'PT012']
#         reports = [2145, 618, 458, 162, 385, 410, 258, 327, 174, 291]
#         queries = [1222, 151, 201, 410, 147, 119, 265, 166, 284, 117]
        
#         months_full = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#         reports_trend = [112, 120, 84, 110, 52, 69, 90, 44, 86, 16, 92, 48]
#         queries_trend = [33, 19, 39, 86, 37, 50, 25, 75, 30, 76, 33, 41]
        
#         return {
#             'active_users': active_users, 'inactive_users_90d': inactive_users_90d,
#             'inactive_users_30d': inactive_users_30d, 'total_users': total_users,
#             'account_locks': 1493, 'queries_reports': 74, 'failed_logins': 217,
#             'months': months, 'this_year': this_year, 'last_year': last_year,
#             'entities': entities, 'reports': reports, 'queries': queries,
#             'months_full': months_full, 'reports_trend': reports_trend, 'queries_trend': queries_trend
#         }

#     data = generate_data()

#     # Row 1: Metrics & Activity
#     col1, col2 = st.columns([5, 7])

#     with col1:
#         st.markdown("""
#         <div class="section-header">
#             <div class="section-icon">
#                 <span class="material-symbols-outlined">speed</span>
#             </div>
#             <div class="section-title">Performance Metrics</div>
#         </div>
#         """, unsafe_allow_html=True)
        
#         m1, m2 = st.columns(2)
        
#         with m1:
#             st.markdown(f"""
#             <div class="stat-card">
#                 <div style="display: flex; justify-content: space-between; align-items: flex-start;">
#                     <span class="material-symbols-outlined" style="font-size: 2.5rem; color: #2563eb; opacity: 0.8;">group</span>
#                 </div>
#                 <div class="stat-value-tv">{data['total_users']:,}</div>
#                 <div class="stat-label-tv">Total Users</div>
#             </div>
#             """, unsafe_allow_html=True)
            
#             st.markdown(f"""
#             <div class="stat-card" style="margin-top: 1rem;">
#                 <div style="display: flex; justify-content: space-between; align-items: flex-start;">
#                     <span class="material-symbols-outlined" style="font-size: 2.5rem; color: #7c3aed; opacity: 0.8;">analytics</span>
#                 </div>
#                 <div class="stat-value-tv">{data['queries_reports']}</div>
#                 <div class="stat-label-tv">Total Activities</div>
#             </div>
#             """, unsafe_allow_html=True)
        
#         with m2:
#             st.markdown(f"""
#             <div class="stat-card">
#                 <div style="display: flex; justify-content: space-between; align-items: flex-start;">
#                     <span class="material-symbols-outlined" style="font-size: 2.5rem; color: #eab308; opacity: 0.8;">lock</span>
#                 </div>
#                 <div class="stat-value-tv">{data['account_locks']:,}</div>
#                 <div class="stat-label-tv">Account Locks</div>
#             </div>
#             """, unsafe_allow_html=True)
            
#             st.markdown(f"""
#             <div class="stat-card" style="margin-top: 1rem;">
#                 <div style="display: flex; justify-content: space-between; align-items: flex-start;">
#                     <span class="material-symbols-outlined" style="font-size: 2.5rem; color: #dc2626; opacity: 0.8;">warning</span>
#                 </div>
#                 <div class="stat-value-tv">{data['failed_logins']}</div>
#                 <div class="stat-label-tv">Failed Attempts</div>
#             </div>
#             """, unsafe_allow_html=True)

#     with col2:
#         st.markdown("""
#         <div class="section-header">
#             <div class="section-icon">
#                 <span class="material-symbols-outlined">insights</span>
#             </div>
#             <div class="section-title">User Engagement</div>
#         </div>
#         """, unsafe_allow_html=True)
        
#         u1, u2 = st.columns(2)
        
#         with u1:
#             fig_donut = go.Figure()
#             fig_donut.add_trace(go.Pie(
#                 labels=['Active', 'Inactive (30d)', 'Inactive (90d)'],
#                 values=[data['active_users'], data['inactive_users_30d'], data['inactive_users_90d']],
#                 hole=0.75,
#                 marker=dict(colors=['#2563eb', '#7c3aed', '#eab308'], 
#                            line=dict(color='white', width=2)),
#                 textinfo='none',
#                 hovertemplate='<b>%{label}</b><br>%{value:,} users<br>%{percent}<extra></extra>'
#             ))
            
#             fig_donut.update_layout(
#                 height=280,
#                 margin=dict(l=10, r=10, t=10, b=10),
#                 paper_bgcolor='rgba(0,0,0,0)',
#                 plot_bgcolor='rgba(0,0,0,0)',
#                 showlegend=False,
#                 annotations=[dict(
#                     text=f'<b>{data["total_users"]:,}</b><br>Total Users',
#                     x=0.5, y=0.5,
#                     font=dict(size=16, color='#0f172a', family='Inter'),
#                     showarrow=False
#                 )]
#             )
            
#             st.plotly_chart(fig_donut, use_container_width=True, config={'displayModeBar': False})
            
#             st.markdown(f"""
#             <div style="display: flex; justify-content: center; gap: 1.5rem; margin-top: 0.5rem;">
#                 <div style="display: flex; align-items: center; gap: 0.5rem;">
#                     <div style="width: 0.75rem; height: 0.75rem; border-radius: 50%; background: #2563eb; box-shadow: 0 0 10px #2563eb;"></div>
#                     <span style="color: #475569; font-size: 0.875rem;">Active <b style="color: #0f172a;">{data['active_users']:,}</b></span>
#                 </div>
#                 <div style="display: flex; align-items: center; gap: 0.5rem;">
#                     <div style="width: 0.75rem; height: 0.75rem; border-radius: 50%; background: #7c3aed;"></div>
#                     <span style="color: #475569; font-size: 0.875rem;">30d <b style="color: #0f172a;">{data['inactive_users_30d']:,}</b></span>
#                 </div>
#                 <div style="display: flex; align-items: center; gap: 0.5rem;">
#                     <div style="width: 0.75rem; height: 0.75rem; border-radius: 50%; background: #eab308;"></div>
#                     <span style="color: #475569; font-size: 0.875rem;">90d <b style="color: #0f172a;">{data['inactive_users_90d']:,}</b></span>
#                 </div>
#             </div>
#             """, unsafe_allow_html=True)
        
#         with u2:
#             fig_bars = go.Figure()
            
#             fig_bars.add_trace(go.Bar(
#                 x=data['months'],
#                 y=data['last_year'],
#                 name='Previous Period',
#                 marker=dict(color='rgba(100, 116, 139, 0.3)', line=dict(color='rgba(100, 116, 139, 0.5)', width=1)),
#                 text=data['last_year'],
#                 textposition='outside',
#                 textfont=dict(size=10, color='#475569')
#             ))
            
#             fig_bars.add_trace(go.Bar(
#                 x=data['months'],
#                 y=data['this_year'],
#                 name='Current Period',
#                 marker=dict(
#                     color=data['this_year'],
#                     colorscale=[[0, '#2563eb'], [0.5, '#7c3aed'], [1, '#db2777']],
#                     line=dict(color='rgba(255,255,255,0.5)', width=1)
#                 ),
#                 text=data['this_year'],
#                 textposition='outside',
#                 textfont=dict(size=10, color='#0f172a')
#             ))
            
#             fig_bars.update_layout(
#                 barmode='group',
#                 height=280,
#                 margin=dict(l=10, r=10, t=40, b=10),
#                 paper_bgcolor='rgba(0,0,0,0)',
#                 plot_bgcolor='rgba(0,0,0,0)',
#                 legend=dict(
#                     orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5,
#                     font=dict(size=11, color='#475569'),
#                     bgcolor='rgba(0,0,0,0)'
#                 ),
#                 xaxis=dict(showgrid=False, tickfont=dict(size=11, color='#475569')),
#                 yaxis=dict(showgrid=True, gridcolor='rgba(0,0,0,0.05)', tickfont=dict(size=10, color='#64748b'))
#             )
            
#             st.plotly_chart(fig_bars, use_container_width=True, config={'displayModeBar': False})

#     # Row 2: Analytics
#     col3, col4, col5 = st.columns([5, 3, 4])

#     with col3:
#         st.markdown("""
#         <div class="section-header">
#             <div class="section-icon">
#                 <span class="material-symbols-outlined">top</span>
#             </div>
#             <div class="section-title">Top Performing Entities</div>
#         </div>
#         """, unsafe_allow_html=True)
        
#         st.markdown("""
#         <div class="glass-card">
#             <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
#                 <span style="font-size: 0.875rem; color: #475569;">Reports vs Queries by Entity</span>
#                 <span style="font-size: 0.75rem; padding: 0.375rem 0.75rem; background: rgba(37, 99, 235, 0.1); border: 1px solid rgba(37, 99, 235, 0.2); border-radius: 9999px; color: #2563eb; font-weight: 600;">MTD</span>
#             </div>
#         """, unsafe_allow_html=True)
        
#         # Horizontal grouped bar chart for entities
#         entities_df = pd.DataFrame({
#             'Entity': data['entities'],
#             'Reports': data['reports'],
#             'Queries': data['queries']
#         })
        
#         fig_entities = go.Figure()
        
#         fig_entities.add_trace(go.Bar(
#             y=data['entities'][::-1],
#             x=data['reports'][::-1],
#             name='Reports',
#             orientation='h',
#             marker=dict(color='#2563eb', line=dict(color='white', width=1)),
#             text=data['reports'][::-1],
#             textposition='outside',
#             textfont=dict(size=10, color='#0f172a')
#         ))
        
#         fig_entities.add_trace(go.Bar(
#             y=data['entities'][::-1],
#             x=data['queries'][::-1],
#             name='Queries',
#             orientation='h',
#             marker=dict(color='#7c3aed', line=dict(color='white', width=1)),
#             text=data['queries'][::-1],
#             textposition='outside',
#             textfont=dict(size=10, color='#0f172a')
#         ))
        
#         fig_entities.update_layout(
#             barmode='group',
#             height=400,
#             margin=dict(l=80, r=80, t=20, b=20),
#             paper_bgcolor='rgba(0,0,0,0)',
#             plot_bgcolor='rgba(0,0,0,0)',
#             legend=dict(
#                 orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5,
#                 font=dict(size=12, color='#475569'),
#                 bgcolor='rgba(0,0,0,0)'
#             ),
#             xaxis=dict(
#                 showgrid=True, 
#                 gridcolor='rgba(0,0,0,0.05)',
#                 tickfont=dict(size=10, color='#64748b'),
#                 title=dict(text='Count', font=dict(size=11, color='#475569'))
#             ),
#             yaxis=dict(
#                 showgrid=False,
#                 tickfont=dict(size=11, color='#0f172a'),
#                 autorange='reversed'
#             ),
#             bargap=0.3,
#             bargroupgap=0.1
#         )
        
#         st.plotly_chart(fig_entities, use_container_width=True, config={'displayModeBar': False})
#         st.markdown("</div>", unsafe_allow_html=True)

#     with col4:
#         st.markdown("""
#         <div class="section-header">
#             <div class="section-icon">
#                 <span class="material-symbols-outlined">pie_chart</span>
#             </div>
#             <div class="section-title">Activity Distribution</div>
#         </div>
#         """, unsafe_allow_html=True)
        
#         fig_type = go.Figure()
#         fig_type.add_trace(go.Pie(
#             labels=['Reports', 'Queries'],
#             values=[53, 21],
#             hole=0.7,
#             marker=dict(colors=['#2563eb', '#7c3aed'], line=dict(color='white', width=2)),
#             textinfo='none',
#             hovertemplate='<b>%{label}</b><br>%{value}<extra></extra>'
#         ))
        
#         fig_type.update_layout(
#             height=300,
#             margin=dict(l=10, r=10, t=10, b=10),
#             paper_bgcolor='rgba(0,0,0,0)',
#             plot_bgcolor='rgba(0,0,0,0)',
#             showlegend=False,
#             annotations=[dict(
#                 text='<b>74</b><br>Total',
#                 x=0.5, y=0.5,
#                 font=dict(size=18, color='#0f172a', family='Inter'),
#                 showarrow=False
#             )]
#         )
        
#         st.plotly_chart(fig_type, use_container_width=True, config={'displayModeBar': False})
        
#         st.markdown("""
#         <div style="display: flex; justify-content: center; gap: 2rem; margin-top: 1rem;">
#             <div style="text-align: center;">
#                 <div style="font-size: 2rem; font-weight: 800; color: #2563eb;">53</div>
#                 <div style="font-size: 0.875rem; color: #475569;">Reports</div>
#                 <div style="font-size: 0.75rem; color: #16a34a; margin-top: 0.25rem;">▲ 12%</div>
#             </div>
#             <div style="width: 1px; background: rgba(0,0,0,0.1);"></div>
#             <div style="text-align: center;">
#                 <div style="font-size: 2rem; font-weight: 800; color: #7c3aed;">21</div>
#                 <div style="font-size: 0.875rem; color: #475569;">Queries</div>
#                 <div style="font-size: 0.75rem; color: #16a34a; margin-top: 0.25rem;">▲ 8%</div>
#             </div>
#         </div>
#         """, unsafe_allow_html=True)

#     with col5:
#         st.markdown("""
#         <div class="section-header">
#             <div class="section-icon">
#                 <span class="material-symbols-outlined">show_chart</span>
#             </div>
#             <div class="section-title">Performance Trends</div>
#         </div>
#         """, unsafe_allow_html=True)
        
#         fig_trends = go.Figure()
        
#         fig_trends.add_trace(go.Scatter(
#             x=data['months_full'],
#             y=data['reports_trend'],
#             name='Reports',
#             line=dict(color='#2563eb', width=4),
#             mode='lines+markers',
#             marker=dict(size=8, color='#2563eb', line=dict(color='white', width=2)),
#             fill='tozeroy',
#             fillcolor='rgba(37, 99, 235, 0.1)'
#         ))
        
#         fig_trends.add_trace(go.Scatter(
#             x=data['months_full'],
#             y=data['queries_trend'],
#             name='Queries',
#             line=dict(color='#7c3aed', width=4),
#             mode='lines+markers',
#             marker=dict(size=8, color='#7c3aed', line=dict(color='white', width=2)),
#             fill='tozeroy',
#             fillcolor='rgba(124, 58, 237, 0.1)'
#         ))
        
#         fig_trends.update_layout(
#             height=350,
#             margin=dict(l=10, r=10, t=40, b=10),
#             paper_bgcolor='rgba(0,0,0,0)',
#             plot_bgcolor='rgba(0,0,0,0)',
#             legend=dict(
#                 orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5,
#                 font=dict(size=12, color='#475569'),
#                 bgcolor='rgba(0,0,0,0)'
#             ),
#             xaxis=dict(showgrid=False, tickfont=dict(size=11, color='#475569')),
#             yaxis=dict(showgrid=True, gridcolor='rgba(0,0,0,0.05)', tickfont=dict(size=10, color='#64748b'))
#         )
        
#         st.plotly_chart(fig_trends, use_container_width=True, config={'displayModeBar': False})

#     # Footer with updated label
#     st.markdown("""
#     <div class="tv-footer">
#         <div style="display: flex; align-items: center; gap: 1rem;">
#             <span style="font-weight: 600; color: #0f172a;">Dashboard Analytics</span>
#             <span style="color: #94a3b8;">|</span>
#             <span>Powered by Analytics Team</span>
#         </div>
#         <div class="status-badge">
#             <span class="material-symbols-outlined" style="font-size: 1rem;">check_circle</span>
#             System Status: Healthy
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

# if __name__ == "__main__":
#     Monitoring()












# import base64
# import streamlit as st
# import plotly.graph_objects as go
# import plotly.express as px
# import pandas as pd
# import numpy as np
# from datetime import datetime, timedelta

# def Monitoring():
#     # Enhanced Professional CSS with refined #3498dc theme - keeping your layout structure
#     st.markdown("""
#     <style>
#         @import url('https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap');
#         @import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@24,400,1,0');

#         * { 
#             font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
#             box-sizing: border-box; 
#         }

#         html, body, .stApp { 
#             background: linear-gradient(135deg, #f5f9ff 0%, #ecf3fa 100%);
#             color: #1e293b; 
#         }

#         .block-container {
#             padding: 1.5rem 2rem 1rem 2rem !important;
#             max-width: 100% !important;
#         }

#         #MainMenu, footer, header { visibility: hidden; }
#         .stDeployButton { display: none; }

#         /* HEADER - Enhanced with premium styling */
#         .dash-header {
#             display: flex; 
#             align-items: center; 
#             justify-content: space-between;
#             background: linear-gradient(135deg, #ffffff 0%, #f8fcff 100%);
#             border: 1px solid rgba(52, 152, 220, 0.2);
#             border-radius: 16px;
#             padding: 0.875rem 1.5rem;
#             margin-bottom: 1.5rem;
#             box-shadow: 0 8px 25px -8px rgba(52, 152, 220, 0.2);
#             backdrop-filter: blur(10px);
#         }
        
#         .dash-logo {
#             width: 2.75rem; 
#             height: 2.75rem;
#             border-radius: 12px;
#             background: linear-gradient(135deg, #2c3e50, #3498dc);
#             display: flex; 
#             align-items: center; 
#             justify-content: center;
#             font-weight: 700; 
#             font-size: 0.9rem; 
#             color: #fff;
#             letter-spacing: 0.05em;
#             border: 2px solid rgba(255, 255, 255, 0.3);
#             box-shadow: 0 6px 15px -3px rgba(52, 152, 220, 0.4);
#         }
        
#         .dash-title { 
#             font-size: 1.1rem; 
#             font-weight: 700; 
#             color: #1e293b; 
#             letter-spacing: -0.02em; 
#         }
        
#         .dash-subtitle { 
#             font-size: 0.75rem; 
#             color: #64748b; 
#             font-weight: 500; 
#             margin-top: 0.1rem; 
#         }
        
#         .live-pill {
#             display: flex; 
#             align-items: center; 
#             gap: 0.5rem;
#             background: linear-gradient(135deg, rgba(52, 152, 220, 0.1), rgba(52, 152, 220, 0.15));
#             border: 1px solid rgba(52, 152, 220, 0.3);
#             border-radius: 40px;
#             padding: 0.45rem 1.2rem;
#             font-size: 0.8rem; 
#             font-weight: 600; 
#             color: #3498dc;
#             letter-spacing: 0.03em;
#             box-shadow: 0 2px 8px rgba(52, 152, 220, 0.1);
#         }
        
#         .live-dot {
#             width: 0.5rem; 
#             height: 0.5rem;
#             border-radius: 50%; 
#             background: #3498dc;
#             box-shadow: 0 0 12px #3498dc;
#             animation: pulse 2s ease-in-out infinite;
#         }
        
#         @keyframes pulse {
#             0%, 100% { opacity: 1; transform: scale(1); }
#             50% { opacity: 0.6; transform: scale(1.2); }
#         }

#         /* SECTION LABEL - Enhanced with gradient accent */
#         .section-label {
#             display: flex; 
#             align-items: center; 
#             gap: 0.4rem;
#             font-family: 'Inter', sans-serif;
#             color: #2c3e50;
#             font-weight: 700;
#             font-size: 1.1rem;
#             margin: 2rem 0 1rem 0;
#             padding-bottom: 0.5rem;
#             border-bottom: 2px solid rgba(52, 152, 220, 0.2);
#         }
        
#         .section-label::before {
#             content: ''; 
#             display: inline-block;
#             width: 0.3rem; 
#             height: 1.3rem;
#             background: linear-gradient(135deg, #3498dc, #2c3e50);
#             border-radius: 4px;
#             box-shadow: 0 2px 8px rgba(52, 152, 220, 0.3);
#         }

#         /* METRIC CARDS - Premium design with depth */
#         .metric-card {
#             background: white;
#             border-radius: 16px;
#             padding: 1.125rem 1.25rem;
#             margin-bottom: 0.75rem;
#             position: relative; 
#             overflow: hidden;
#             box-shadow: 0 4px 15px -4px rgba(0, 0, 0, 0.05);
#             border: 1px solid rgba(52, 152, 220, 0.15);
#             transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
#         }
        
#         .metric-card:hover {
#             transform: translateY(-3px);
#             box-shadow: 0 12px 30px -8px rgba(52, 152, 220, 0.25);
#             border-color: rgba(52, 152, 220, 0.3);
#         }
        
#         .metric-card::before {
#             content: ''; 
#             position: absolute;
#             top: 0; 
#             left: 0; 
#             right: 0; 
#             height: 4px;
#             border-radius: 16px 16px 0 0;
#         }
        
#         .metric-card.blue::before   { background: linear-gradient(90deg, #3498dc, #5faee3); }
#         .metric-card.orange::before { background: linear-gradient(90deg, #e67e22, #f39c12); }
#         .metric-card.red::before    { background: linear-gradient(90deg, #e74c3c, #f1948a); }
#         .metric-card.teal::before   { background: linear-gradient(90deg, #1abc9c, #48c9b0); }

#         .metric-icon { 
#             font-family: 'Material Symbols Rounded';
#             font-size: 2rem; 
#             line-height: 1; 
#             margin-bottom: 0.5rem;
#         }
        
#         .metric-icon.blue   { color: #3498dc; }
#         .metric-icon.orange { color: #e67e22; }
#         .metric-icon.red    { color: #e74c3c; }
#         .metric-icon.teal   { color: #1abc9c; }

#         .metric-value {
#             font-size: 2.2rem; 
#             font-weight: 800;
#             letter-spacing: -0.03em; 
#             color: #1e293b;
#             line-height: 1.1; 
#         }
        
#         .metric-label {
#             font-size: 0.75rem; 
#             font-weight: 600;
#             text-transform: uppercase; 
#             letter-spacing: 0.04em;
#             color: #64748b; 
#             margin-top: 0.25rem;
#         }

#         /* CHART CARDS - Premium glass-morphism effect */
#         .chart-card {
#             background: white;
#             border-radius: 16px;
#             padding: 1.125rem 1.25rem 0.75rem 1.25rem;
#             margin-bottom: 0.75rem;
#             box-shadow: 0 4px 15px -4px rgba(0, 0, 0, 0.05);
#             border: 1px solid rgba(52, 152, 220, 0.15);
#             transition: all 0.3s ease;
#             backdrop-filter: blur(10px);
#         }
        
#         .chart-card:hover {
#             box-shadow: 0 12px 30px -10px rgba(52, 152, 220, 0.2);
#             border-color: rgba(52, 152, 220, 0.3);
#         }
        
#         .chart-title { 
#             font-size: 0.9rem; 
#             font-weight: 700; 
#             color: #1e293b; 
#             margin-bottom: 0.1rem; 
#         }
        
#         .chart-meta {  
#             font-size: 0.7rem; 
#             color: #3498dc; 
#             font-weight: 500;
#             margin-bottom: 0.75rem; 
#             text-transform: uppercase;
#             letter-spacing: 0.03em;
#         }

#         /* LEGEND - Refined */
#         .legend-row {  
#             display: flex; 
#             gap: 1.5rem; 
#             justify-content: center; 
#             margin-top: 0.5rem; 
#             padding: 0.5rem 0;
#         }
        
#         .legend-item { 
#             display: flex; 
#             align-items: center; 
#             gap: 0.5rem; 
#             font-size: 0.75rem; 
#             color: #475569; 
#             font-weight: 500;
#         }
        
#         .legend-dot {  
#             width: 0.6rem; 
#             height: 0.6rem; 
#             border-radius: 4px; 
#         }

#         /* FOOTER - Premium */
#         .dash-footer {
#             display: flex; 
#             justify-content: space-between; 
#             align-items: center;
#             background: white;
#             border-radius: 16px;
#             padding: 1rem 1.5rem;
#             box-shadow: 0 4px 15px -4px rgba(0, 0, 0, 0.05);
#             border: 1px solid rgba(52, 152, 220, 0.15);
#             font-size: 0.8rem; 
#             color: #64748b; 
#             margin-top: 1rem;
#             font-weight: 500;
#         }
        
#         .footer-status { 
#             display: flex; 
#             align-items: center; 
#             gap: 0.5rem; 
#             color: #27ae60; 
#             font-weight: 600;
#             background: rgba(39, 174, 96, 0.1);
#             padding: 0.4rem 1.2rem;
#             border-radius: 40px;
#             border: 1px solid rgba(39, 174, 96, 0.2);
#         }
        
#         .footer-status .live-dot {
#             background: #27ae60;
#             box-shadow: 0 0 12px #27ae60;
#             width: 0.4rem;
#             height: 0.4rem;
#         }
        
#         /* Custom scrollbar */
#         ::-webkit-scrollbar {
#             width: 6px;
#             height: 6px;
#         }
#         ::-webkit-scrollbar-track {
#             background: #f1f5f9;
#         }
#         ::-webkit-scrollbar-thumb {
#             background: #3498dc;
#             border-radius: 3px;
#         }
        
#         /* Date badge styling */
#         .date-badge {
#             background: linear-gradient(135deg, rgba(52, 152, 220, 0.1), rgba(52, 152, 220, 0.15));
#             padding: 0.4rem 1rem;
#             border-radius: 40px;
#             font-size: 0.8rem;
#             font-weight: 500;
#             color: #2c3e50;
#             border: 1px solid rgba(52, 152, 220, 0.2);
#             display: flex;
#             align-items: center;
#             gap: 0.5rem;
#         }
#     </style>
#     """, unsafe_allow_html=True)

#     # ── DATA ──────────────────────────────────────────────────────────────────
#     @st.cache_data
#     def generate_data():
#         entities      = ['GDNT','PT006','PT018','PT002','PT004','PT008','LM10','GDPFMIT','PT020','PT012']
#         reports       = [2145, 618, 458, 162, 385, 410, 258, 327, 174, 291]
#         queries       = [1222, 151, 201, 410, 147, 119, 265, 166, 284, 117]
#         months_short  = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
#         this_2025     = [3525,3533,3551,3569,3602,3619,3673,3798,3810,3840,3852,3852]
#         last_2024   = [2959,2970,3016,3021,3043,3203,3223,3243,3324,3388,3426,3572]
#         months_full   = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
#         reports_trend = [11203, 12084,  11052, 6907, 9044, 8616, 9248, 7799, 6627,10517,7266,9271]
#         queries_trend = [3319,   3986,  3750,  2575, 3076, 3341,  4435, 4011, 3393,3815,2876,3678]
#         return dict(
#             active=2924, inactive=505, inactive_90=899,
#             total_users=4328, account_locks=1493, queries_reports=74, failed_logins=217,
#             entities=entities, reports=reports, queries=queries,
#             months_short=months_short, this_year=this_2025, last_year=last_2024,
#             months_full=months_full, reports_trend=reports_trend, queries_trend=queries_trend,
#         )

#     d = generate_data()

#     # ── SHARED CHART CONSTANTS ────────────────────────────────────────────────
#     PAPER  = 'rgba(0,0,0,0)'
#     GRID   = 'rgba(52, 152, 220, 0.1)'
#     TICK   = dict(color='#475569', size=11, family='Inter')
#     FONT   = dict(family='Inter', color='#475569')
#     LEGEND = dict(
#         orientation='h', yanchor='bottom', y=1.02,
#         xanchor='center', x=0.5,
#         font=dict(size=11, family='Inter', color='#475569'),
#         bgcolor='rgba(0,0,0,0)', borderwidth=0,
#     )

#     def get_base64_image(path):
#         with open(path, "rb") as img:
#             return base64.b64encode(img.read()).decode()

#     img_base64 = get_base64_image("FMIS_Logo.png")

#     # ── HEADER ────────────────────────────────────────────────────────────────
#     st.markdown(f"""
#     <div class="dash-header">
#         <div style="display:flex;align-items:center;gap:1rem;">
#             <div class="dash-logo">FM</div>
#             <img src="data:image/png;base64,{img_base64}" width="40" style="border-radius:8px;">
#             <div style="height:1.5rem;width:1px;background:rgba(52,152,220,0.2);"></div>
#             <div>
#                 <div class="dash-title">FMIS Monitoring</div>
#                 <div class="dash-subtitle">User & Report Analytics · OIM Team</div>
#             </div>
#         </div>
#         <div style="display:flex;align-items:center;gap:1rem;">
#             <div class="date-badge">
#                 <span>📅</span> Last 30 Days
#             </div>
#             <div class="live-pill">
#                 <div class="live-dot"></div>
#                 LIVE
#             </div>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     # ══════════════════════════════════════════════════════════════════════════
#     # ROW 1 — Metric cards | Account status donut | New users bar
#     # ══════════════════════════════════════════════════════════════════════════
#     col_m, col_charts = st.columns([2, 5])

#     with col_m:
#         st.markdown('<div class="section-label">Activity Metrics</div>', unsafe_allow_html=True)
#         for icon, color, val, label in [
#             ("👥",   "blue",   f"{d['total_users']:,}",  "Total Users"),
#             ("📊",  "teal",   str(d['queries_reports']), "Queries & Reports"),
#             ("⚠️", "red",    str(d['failed_logins']),   "Failed Logins"),
#         ]:
#             st.markdown(f"""
#             <div class="metric-card {color}">
#                 <div style="display:flex; align-items:center; justify-content:space-between;">
#                     <span class="metric-icon {color}" style="font-size:1.8rem;">{icon}</span>
#                 </div>
#                 <div class="metric-value">{val}</div>
#                 <div class="metric-label">{label}</div>
#             </div>""", unsafe_allow_html=True)

#     with col_charts:
#         st.markdown('<div class="section-label">User Activity</div>', unsafe_allow_html=True)
#         cc1, cc2 = st.columns(2)

#         # Donut — Account Status
#         with cc1:
#             st.markdown("""
#             <div class="chart-card">
#                 <div class="chart-title">Account Status</div>
#                 <div class="chart-meta">Current period breakdown</div>
#             """, unsafe_allow_html=True)

#             fig_donut = go.Figure()
#             fig_donut.add_trace(go.Pie(
#                 labels=['Active', 'Inactive (30d)', 'Inactive (90d)'],
#                 values=[d['active'], d['inactive'], d['inactive_90']],
#                 hole=0.7,
#                 marker=dict(
#                     colors=['#3498dc', '#94a3b8', '#f39c12'],
#                     line=dict(color='#ffffff', width=3)
#                 ),
#                 textinfo='none', 
#                 showlegend=False, 
#                 sort=False,
#                 hovertemplate='<b>%{label}</b><br>%{value:,} users · %{percent}<extra></extra>',
#             ))
#             fig_donut.update_layout(
#                 height=240,
#                 paper_bgcolor=PAPER, 
#                 plot_bgcolor=PAPER,
#                 margin=dict(l=10, r=10, t=10, b=10),
#                 font=FONT,
#                 annotations=[dict(
#                     text=f'<b>{d["total_users"]:,}</b><br>Total',
#                     x=0.5, y=0.5,
#                     font=dict(size=14, color='#1e293b', family='Inter', weight='bold'),
#                     showarrow=False,
#                 )],
#             )
#             st.plotly_chart(fig_donut, use_container_width=True, config={'displayModeBar': False})
#             st.markdown(f"""
#             <div class="legend-row">
#                 <div class="legend-item"><div class="legend-dot" style="background:#3498dc"></div>Active {d['active']:,}</div>
#                 <div class="legend-item"><div class="legend-dot" style="background:#94a3b8"></div>Inactive {d['inactive']:,}</div>
#                 <div class="legend-item"><div class="legend-dot" style="background:#f39c12"></div>90d+ {d['inactive_90']:,}</div>
#             </div></div>
#             """, unsafe_allow_html=True)

#         # Grouped Bar — New Users
#         with cc2:
#             st.markdown("""
#             <div class="chart-card">
#                 <div class="chart-title">New Users · Monthly</div>
#                 <div class="chart-meta">2024 vs 2025 comparison</div>
#             """, unsafe_allow_html=True)

#             fig_bar = go.Figure()
#             fig_bar.add_trace(go.Bar(
#                 x=d['months_short'], 
#                 y=d['last_year'], 
#                 name='2024',
#                 marker=dict(color='rgba(52, 152, 220, 0.2)', line=dict(width=0)),
#                 text=[f'{v:,}' for v in d['last_year']],
#                 textposition='outside',
#                 textfont=dict(size=9, color='#64748b'),
#             ))
#             fig_bar.add_trace(go.Bar(
#                 x=d['months_short'], 
#                 y=d['this_year'], 
#                 name='2025',
#                 marker=dict(
#                     color='#3498dc',
#                     line=dict(width=0),
#                 ),
#                 text=[f'{v:,}' for v in d['this_year']],
#                 textposition='outside',
#                 textfont=dict(size=9, color='#3498dc', weight='bold'),
#             ))
#             fig_bar.update_layout(
#                 height=240,
#                 paper_bgcolor=PAPER, 
#                 plot_bgcolor=PAPER,
#                 margin=dict(l=10, r=10, t=30, b=10),
#                 font=FONT, 
#                 legend=LEGEND,
#                 barmode='group', 
#                 bargap=0.2, 
#                 bargroupgap=0.1,
#                 xaxis=dict(
#                     showgrid=False, 
#                     tickfont=TICK,
#                     tickcolor='rgba(0,0,0,0)', 
#                     linecolor='rgba(0,0,0,0)'
#                 ),
#                 yaxis=dict(
#                     showgrid=True, 
#                     gridcolor=GRID, 
#                     gridwidth=1, 
#                     tickfont=TICK,
#                     zeroline=False, 
#                     linecolor='rgba(0,0,0,0)'
#                 ),
#             )
#             st.plotly_chart(fig_bar, use_container_width=True, config={'displayModeBar': False})
#             st.markdown('</div>', unsafe_allow_html=True)

#     # ══════════════════════════════════════════════════════════════════════════
#     # ROW 2 — Top 10 Entities | Usage type donut | Activity trends
#     # ══════════════════════════════════════════════════════════════════════════
#     col_ent, col_usage, col_trend = st.columns([5, 2, 5])

#     # Horizontal Stacked Bar — Top 10 Entities
#     with col_ent:
#         st.markdown('<div class="section-label">Report Usage Analytics</div>', unsafe_allow_html=True)
#         st.markdown("""
#         <div class="chart-card">
#             <div class="chart-title">Top 10 Active Entities</div>
#             <div class="chart-meta">Reports & Queries · Current month</div>
#         """, unsafe_allow_html=True)

#         entities = d['entities']
#         reports  = d['reports']
#         queries  = d['queries']

#         order      = sorted(range(len(entities)), key=lambda i: reports[i] + queries[i])
#         ent_sorted = [entities[i] for i in order]
#         rep_sorted = [reports[i]  for i in order]
#         qry_sorted = [queries[i]  for i in order]

#         fig_hbar = go.Figure()
#         fig_hbar.add_trace(go.Bar(
#             y=ent_sorted, 
#             x=rep_sorted, 
#             name='Reports', 
#             orientation='h',
#             marker=dict(color='#2c3e50', line=dict(width=0)),
#             text=[f'{v:,}' for v in rep_sorted],
#             textposition='inside', 
#             insidetextanchor='end',
#             textfont=dict(color='#ffffff', size=10, family='Inter'),
#             hovertemplate='<b>%{y}</b><br>Reports: %{x:,}<extra></extra>',
#         ))
#         fig_hbar.add_trace(go.Bar(
#             y=ent_sorted, 
#             x=qry_sorted, 
#             name='Queries', 
#             orientation='h',
#             marker=dict(color='#3498dc', line=dict(width=0)),
#             text=[f'{v:,}' for v in qry_sorted],
#             textposition='inside', 
#             insidetextanchor='end',
#             textfont=dict(color='#ffffff', size=10, family='Inter'),
#             hovertemplate='<b>%{y}</b><br>Queries: %{x:,}<extra></extra>',
#         ))
#         fig_hbar.update_layout(
#             height=360,
#             paper_bgcolor=PAPER, 
#             plot_bgcolor=PAPER,
#             margin=dict(l=80, r=20, t=30, b=10),
#             font=FONT, 
#             legend=LEGEND,
#             barmode='stack', 
#             bargap=0.2,
#             xaxis=dict(
#                 showgrid=True, 
#                 gridcolor=GRID, 
#                 gridwidth=1,
#                 tickfont=TICK, 
#                 zeroline=False,
#                 linecolor='rgba(0,0,0,0)', 
#                 tickformat=','
#             ),
#             yaxis=dict(
#                 showgrid=False,
#                 tickfont=dict(color='#1e293b', size=11, family='Inter', weight='500'),
#                 linecolor='rgba(0,0,0,0)', 
#                 categoryorder='total ascending'
#             ),
#         )
#         st.plotly_chart(fig_hbar, use_container_width=True, config={'displayModeBar': False})
#         st.markdown("""
#         <div class="legend-row" style="margin-bottom:0.25rem">
#             <div class="legend-item"><div class="legend-dot" style="background:#2c3e50"></div>Reports</div>
#             <div class="legend-item"><div class="legend-dot" style="background:#3498dc"></div>Queries</div>
#         </div></div>
#         """, unsafe_allow_html=True)

#     # Donut — Usage by Type
#     with col_usage:
#         st.markdown('<div class="section-label">Usage Type</div>', unsafe_allow_html=True)
#         st.markdown("""
#         <div class="chart-card">
#             <div class="chart-title">Usage Distribution</div>
#             <div class="chart-meta">Reports vs Queries</div>
#         """, unsafe_allow_html=True)

#         fig_type = go.Figure()
#         fig_type.add_trace(go.Pie(
#             labels=['Reports', 'Queries'], 
#             values=[53, 21],
#             hole=0.7,
#             marker=dict(
#                 colors=['#2c3e50','#3498dc'],
#                 line=dict(color='#ffffff', width=3)
#             ),
#             textinfo='none', 
#             showlegend=False,
#             hovertemplate='<b>%{label}</b><br>%{value} · %{percent}<extra></extra>',
#         ))
#         fig_type.update_layout(
#             height=220,
#             paper_bgcolor=PAPER, 
#             plot_bgcolor=PAPER,
#             margin=dict(l=10, r=10, t=10, b=10),
#             font=FONT,
#             annotations=[dict(
#                 text='<b>74</b><br>Total',
#                 x=0.5, y=0.5,
#                 font=dict(size=13, color='#1e293b', family='Inter', weight='bold'),
#                 showarrow=False,
#             )],
#         )
#         st.plotly_chart(fig_type, use_container_width=True, config={'displayModeBar': False})
#         st.markdown("""
#         <div class="legend-row" style="flex-direction:column;align-items:center;gap:0.5rem;margin-bottom:0.5rem">
#             <div class="legend-item">
#                 <div class="legend-dot" style="background:#2c3e50;width:0.75rem;height:0.75rem;border-radius:4px;"></div>
#                 Reports <b style="color:#1e293b; margin-left:0.25rem;">53</b>
#             </div>
#             <div class="legend-item">
#                 <div class="legend-dot" style="background:#3498dc;width:0.75rem;height:0.75rem;border-radius:4px;"></div>
#                 Queries <b style="color:#1e293b; margin-left:0.25rem;">21</b>
#             </div>
#         </div></div>
#         """, unsafe_allow_html=True)

#     # Line chart — Activity Trends
#     with col_trend:
#         st.markdown('<div class="section-label">Activity Trends</div>', unsafe_allow_html=True)
#         st.markdown("""
#         <div class="chart-card">
#             <div class="chart-title">Monthly Activity Trends</div>
#             <div class="chart-meta">12-month overview</div>
#         """, unsafe_allow_html=True)

#         fig_trend = go.Figure()
#         fig_trend.add_trace(go.Scatter(
#             x=d['months_full'], 
#             y=d['reports_trend'], 
#             name='Reports',
#             line=dict(color='#2c3e50', width=3, shape='spline', smoothing=0.8),
#             mode='lines+markers',
#             marker=dict(size=7, color='#2c3e50', line=dict(width=2, color='#ffffff')),
#             fill='tozeroy', 
#             fillcolor='rgba(44, 62, 80, 0.05)',
#             hovertemplate='%{x}<br>Reports: <b>%{y:,}</b><extra></extra>',
#         ))
#         fig_trend.add_trace(go.Scatter(
#             x=d['months_full'], 
#             y=d['queries_trend'], 
#             name='Queries',
#             line=dict(color='#3498dc', width=3, shape='spline', smoothing=0.8),
#             mode='lines+markers',
#             marker=dict(size=7, color='#3498dc', line=dict(width=2, color='#ffffff')),
#             fill='tozeroy', 
#             fillcolor='rgba(52, 152, 220, 0.05)',
#             hovertemplate='%{x}<br>Queries: <b>%{y:,}</b><extra></extra>',
#         ))
#         fig_trend.update_layout(
#             height=360,
#             paper_bgcolor=PAPER, 
#             plot_bgcolor=PAPER,
#             margin=dict(l=10, r=10, t=30, b=10),
#             font=FONT, 
#             legend=LEGEND,
#             hovermode='x unified',
#             xaxis=dict(
#                 showgrid=False, 
#                 tickfont=TICK,
#                 linecolor='rgba(0,0,0,0)', 
#                 tickcolor='rgba(0,0,0,0)'
#             ),
#             yaxis=dict(
#                 showgrid=True, 
#                 gridcolor=GRID, 
#                 gridwidth=1, 
#                 tickfont=TICK,
#                 zeroline=False, 
#                 linecolor='rgba(0,0,0,0)',
#                 tickformat=','
#             ),
#         )
#         st.plotly_chart(fig_trend, use_container_width=True, config={'displayModeBar': False})
#         st.markdown("""
#         <div class="legend-row">
#             <div class="legend-item"><div class="legend-dot" style="background:#2c3e50"></div>Reports</div>
#             <div class="legend-item"><div class="legend-dot" style="background:#3498dc"></div>Queries</div>
#         </div></div>
#         """, unsafe_allow_html=True)

#     # ── FOOTER ────────────────────────────────────────────────────────────────
#     st.markdown("""
#     <div class="dash-footer">
#         <span>© 2025 FMIS · Developed and prepared by OIM Team</span>
#         <div class="footer-status">
#             <div class="live-dot"></div>
#             All systems operational
#         </div>
#     </div>
#     """, unsafe_allow_html=True)


# if __name__ == "__main__":
#     st.set_page_config(
#         layout="wide", 
#         page_title="FMIS Monitoring", 
#         page_icon="📊",
#         initial_sidebar_state="collapsed"
#     )
#     Monitoring()