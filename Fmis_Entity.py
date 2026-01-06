import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def FmisEntity():
    """Professional FMIS Entity Viewer with executive theme"""
    # Professional color palette
    PRIMARY_COLOR = "#1a202c"  # Navy dark slate
    SECONDARY_COLOR = "#2d3748"  # Dark gray
    ACCENT_COLOR = "#3182ce"  # Subtle blue
    BACKGROUND_COLOR = "#f7fafc"  # Light gray
    CARD_COLOR = "#ffffff"  # White
    TEXT_COLOR = "#2d3748"  # Slate gray
    LIGHT_TEXT = "#718096"  # Medium gray
    BORDER_COLOR = "#e2e8f0"  # Light border gray
    SUCCESS_COLOR = "#38a169"  # Green
    WARNING_COLOR = "#dd6b20"  # Orange
    CHART_GRID_COLOR = "#edf2f7"  # Grid light gray

    CHART_COLORS = ["#2b6cb0", "#3182ce", "#4299e1", "#63b3ed", "#90cdf4"]
    ALT_CHART_COLORS = ["#718096", "#a0aec0", "#cbd5e0", "#e2e8f0", "#edf2f7"]

    # Inject custom CSS
    st.markdown(f"""
    <style>
        .main {{
            background-color: {BACKGROUND_COLOR};
        }}
        
        .stSelectbox, .stTextInput, .stRadio > div {{
            background-color: {CARD_COLOR};
            border: 1px solid {BORDER_COLOR};
            border-radius: 6px;
            padding: 10px 12px;
            box-shadow: 0 1px 2px rgba(0,0,0,0.03);
        }}
        
        .stExpander {{
            background-color: {CARD_COLOR};
            border-radius: 6px;
            border-left: 4px solid {ACCENT_COLOR};
            box-shadow: 0 2px 6px rgba(0,0,0,0.03);
        }}

        .stTabs [data-baseweb="tab"] {{
            background-color: {CARD_COLOR};
            color: {LIGHT_TEXT};
            border: 1px solid {BORDER_COLOR};
            border-radius: 4px;
            padding: 6px 16px;
        }}

        .stTabs [aria-selected="true"] {{
            background-color: {ACCENT_COLOR};
            color: white !important;
            border-color: {ACCENT_COLOR};
        }}

        .stDataFrame {{
            border: 1px solid {BORDER_COLOR};
            border-radius: 6px;
        }}

        .stButton button {{
            background-color: {ACCENT_COLOR};
            color: white;
            border-radius: 6px;
            border: none;
        }}

        .stButton button:hover {{
            background-color: #2563eb;
        }}

        .stDownloadButton button {{
            background-color: {ACCENT_COLOR} !important;
            color: white !important;
        }}

        .stDownloadButton button:hover {{
            background-color: #2563eb !important;
        }}

        .stMarkdown h1, .stMarkdown h2 {{
            color: {PRIMARY_COLOR};
        }}

        div[data-testid="stExpander"] div[role="button"] p {{
            font-weight: 600 !important;
            color: {TEXT_COLOR} !important;
        }}

        /* Hide expander icon elements to prevent fallback text like
           "keyboard_arrow_right" appearing when icon fonts fail to load */
        div[data-testid="stExpander"] div[role="button"] > *:not(:last-child) {{
            display: none !important;
        }}
    </style>
    """, unsafe_allow_html=True)



    st.markdown("""
        <style>
            .block-container {
                padding-top: 1rem;
                padding-bottom: 3rem;
            }
        </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown(f"""
    <div style="margin-bottom: 2rem;">
        <h1 style="font-family: 'Segoe UI', Tahoma, Geneva, sans-serif;
                   color: {PRIMARY_COLOR};
                   font-weight: 700;
                   font-size: 2.2rem;
                   margin-bottom: 0.5rem;
                   display: inline-block;
                   border-bottom: 3px solid {ACCENT_COLOR};
                   padding-bottom: 0.5rem;">
            🏛️ FMIS Entity Explorer
        </h1>
        <p style="font-family: 'Segoe UI', Tahoma, Geneva, sans-serif;
                  color: {LIGHT_TEXT};
                  font-size: 1rem;">
            Discover entity hierarchy with clarity
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Load the Excel file
    try:
        df = pd.read_excel('Excel files/FMIS Entity all CMB01.xlsx')
    except FileNotFoundError:
        st.error("Error: The FMIS Entity data file could not be found.")
        return
    except Exception as e:
        st.error(f"An error occurred while loading the data: {str(e)}")
        return

    # Get unique values for the 'National Level' column
    national_levels = df['National Level'].dropna().unique()
    
    # Elegant filter panel
    with st.container():
        st.markdown(
            f"<h3 style='color:{TEXT_COLOR}; margin-bottom: 16px; font-size: 1.25rem;'>Filter Criteria</h3>", 
            unsafe_allow_html=True
        )
        col1, col2, col3 = st.columns(3)
    
    # with col1:
    #     selected_level = st.selectbox(
    #         "Level:", 
    #         sorted(national_levels),
    #         help="Select a national level to filter business units",
    #         key="national_level_select"
    #     )
    
    # if selected_level == "CMB02":
    #     with col2:
    #         sub_level = st.selectbox(
    #             "Sub Level:",
    #             ["All", "Line Ministry", "Line Department"],
    #             help="Filter by Line Ministry or Line Department",
    #             key="sub_level_select"
    #         )
    #     with col3:
    #         search_term = st.text_input(
    #             "Search Business Units:",
    #             "",
    #             help="Type to filter business units by name or code",
    #             key="business_unit_search"
    #         )
    # else:
    #     sub_level = None
    #     with col2:
    #         search_term = st.text_input(
    #             "Search Business Units:",
    #             "",
    #             help="Type to filter business units by name or code",
    #             key="business_unit_search"
    #         )
    with col1:
        selected_level = st.selectbox(
            "Level:", 
            sorted(national_levels),
            help="Select a national level to filter business units",
            key="national_level_select"
        )

    sub_level = None
    if selected_level == "CMB02":
        with col2:
            sub_level = st.selectbox(
                "National Level:",
                ["All", "Line Ministry", "Line Department"],
                help="Filter by Line Ministry or Line Department",
                key="sub_level_select_cmb02"
            )
        with col3:
            search_term = st.text_input(
                "Search Business Units:",
                "",
                help="Type to filter business units by name or code",
                key="business_unit_search_cmb02"
            )

    elif selected_level == "CMB03":
        with col2:
            sub_level = st.selectbox(
                "Sub-National Level:",
                ["All", "Provincial", "District", "Commune"],
                help="Filter by Provincial, District or Commune",
                key="sub_level_select_cmb03"
            )
        with col3:
            search_term = st.text_input(
                "Search Business Units:",
                "",
                help="Type to filter business units by name or code",
                key="business_unit_search_cmb03"
            )

    else:
        with col2:
            search_term = st.text_input(
                "Search Business Units:",
                "",
                help="Type to filter business units by name or code",
                key="business_unit_search_default"
            )
        # with col2:
        #     search_term = st.text_input(
        #         "Search Business Units:",
        #         "",
        #         help="Type to filter business units by name or code",
        #         key="business_unit_search"
        #     )

    # # Filter data based on selections
    # filtered_df = df[df['National Level'] == selected_level].copy()

    # # Apply second-level filter for CMB02
    # if selected_level == "CMB02" and sub_level != "All":
    #     if sub_level == "Line Ministry":
    #         filtered_df = filtered_df[filtered_df['BUSINESS_UNIT'].str.match(r'^\d|^NT')]
    #     elif sub_level == "Line Department":
    #         filtered_df = filtered_df[~filtered_df['BUSINESS_UNIT'].str.match(r'^\d|^NT')]
    # # Apply search filter if not CMB02
    # if selected_level != "CMB02" and search_term:
    #     search_mask = (filtered_df['BUSINESS_UNIT'].str.contains(search_term, case=False)) | \
    #                 (filtered_df['BU_Description'].str.contains(search_term, case=False))
    #     filtered_df = filtered_df[search_mask]

    # Filter data based on selections
    filtered_df = df[df['National Level'] == selected_level].copy()

    # Apply sub-level filters
    if selected_level == "CMB02" and sub_level != "All":
        if sub_level == "Line Ministry":
            filtered_df = filtered_df[filtered_df['BUSINESS_UNIT'].str.match(r'^\d|^NT')]
        elif sub_level == "Line Department":
            filtered_df = filtered_df[~filtered_df['BUSINESS_UNIT'].str.match(r'^\d|^NT')]

    elif selected_level == "CMB03" and sub_level != "All":
        if sub_level == "Provincial":
            filtered_df = filtered_df[filtered_df['BUSINESS_UNIT'].str.startswith("P")]
        elif sub_level == "District":
            filtered_df = filtered_df[filtered_df['BUSINESS_UNIT'].str.startswith("D")]
        elif sub_level == "Commune":
            filtered_df = filtered_df[filtered_df['BUSINESS_UNIT'].str.startswith("C")]

    # Apply search term (always works in all cases)
    if search_term:
        search_mask = (filtered_df['BUSINESS_UNIT'].str.contains(search_term, case=False)) | \
                    (filtered_df['BU_Description'].str.contains(search_term, case=False))
        filtered_df = filtered_df[search_mask]

    
    # if search_term:
    #     search_mask = (filtered_df['BUSINESS_UNIT'].str.contains(search_term, case=False)) | \
    #                  (filtered_df['BU_Description'].str.contains(search_term, case=False))
    #     filtered_df = filtered_df[search_mask]
    
    # Get unique business units
    business_units = filtered_df[['BUSINESS_UNIT', 'BU_Description']].drop_duplicates()
    
    # Elegant results count display
    st.markdown(f"""
    <div style="background-color: {CARD_COLOR}; padding: 16px; border-radius: 8px; 
                margin: 20px 0; border-left: 4px solid {ACCENT_COLOR}; 
                border: 1px solid {BORDER_COLOR}; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
        <div style="display: flex; align-items: center; gap: 8px;">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M9 12L11 14L15 10M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z" 
                      stroke="{PRIMARY_COLOR}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <span style="font-size: 16px; color: {TEXT_COLOR}; font-weight: 500;">
                Found <strong style="color: {PRIMARY_COLOR};">{len(business_units)}</strong> business units matching your criteria
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Elegant tabs with consistent styling
    tab1, tab2, tab3 = st.tabs(["Hierarchy", "Data Table", "Analytics"])
    
    with tab1:
        # Enhanced hierarchical tree view with elegant cards
        for _, bu_row in business_units.iterrows():
            bu_code = bu_row['BUSINESS_UNIT']
            bu_desc = bu_row['BU_Description']

            # Elegant expander card
            with st.expander(f"**{bu_code} - {bu_desc}**", expanded=False):
                # Get operating units for this business unit
                ou_df = filtered_df[filtered_df['BUSINESS_UNIT'] == bu_code][['OPERATING_UNIT', 'DESCRLONG_ENG']].drop_duplicates()

                if not ou_df.empty:
                    st.markdown(
                        f"<div style='color:{TEXT_COLOR}; font-weight:600; margin-bottom:12px; font-size: 15px;'>Operating Units</div>",
                        unsafe_allow_html=True
                    )

                    # Display operating units in elegant cards
                    cols = st.columns(2)
                    for i, (_, ou_row) in enumerate(ou_df.iterrows()):
                        with cols[i % 2]:
                            st.markdown(
                                f"""
                                <div style="padding: 16px; margin: 8px 0; background: {CARD_COLOR};
                                border-radius: 8px; border-left: 4px solid {ACCENT_COLOR};
                                border: 1px solid {BORDER_COLOR}; box-shadow: 0 2px 6px rgba(0,0,0,0.03);
                                transition: all 0.2s;">
                                    <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
                                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                            <path d="M19 21V5C19 3.89543 18.1046 3 17 3H7C5.89543 3 5 3.89543 5 5V21M19 21L21 21M19 21H14M5 21L3 21M5 21H10M9 6.99998H10M9 11H10M14 6.99998H15M14 11H15M10 21V16C10 15.4477 10.4477 15 11 15H13C13.5523 15 14 15.4477 14 16V21M10 21H14"
                                                  stroke="{ACCENT_COLOR}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                                        </svg>
                                        <div style="font-weight: 600; color: {PRIMARY_COLOR}; font-size: 15px;">
                                            {ou_row['OPERATING_UNIT']}
                                        </div>
                                    </div>
                                    <div style="color: {LIGHT_TEXT}; font-size: 14px; margin-top: 4px; padding-left: 26px;">
                                        {ou_row['DESCRLONG_ENG'] if pd.notna(ou_row['DESCRLONG_ENG']) else 'No description available'}
                                    </div>
                                </div>
                                """,
                                unsafe_allow_html=True
                            )
                else:
                    st.info("No operating units found for this business unit.", icon="ℹ️")
    
    with tab2:
        # Elegant table view with enhanced styling
        st.markdown(
            f"<h3 style='color:{TEXT_COLOR}; margin-bottom: 16px; font-size: 1.25rem;'>Business Units with Operating Units</h3>", 
            unsafe_allow_html=True
        )
        
        # Create a summary table
        summary_data = []
        for _, bu_row in business_units.iterrows():
            bu_code = bu_row['BUSINESS_UNIT']
            ou_count = len(filtered_df[filtered_df['BUSINESS_UNIT'] == bu_code]['OPERATING_UNIT'].unique())
            summary_data.append({
                "Business Unit": bu_code,
                "Description": bu_row['BU_Description'],
                "Operating Units Count": ou_count
            })
        
        summary_df = pd.DataFrame(summary_data)
        
        # Elegant conditional formatting
        def color_ou_count(val):
            if val > 10:
                color = '#e6fffa'  # Light teal
                text_color = SUCCESS_COLOR
            elif val > 5:
                color = '#fffaf0'  # Light orange
                text_color = WARNING_COLOR
            elif val > 0:
                color = '#fff5f5'  # Light coral
                text_color = '#f56565'  # Coral
            else:
                color = '#f5f5f5'  # Light gray
                text_color = LIGHT_TEXT
            return f'background-color: {color}; color: {text_color}; font-weight: 500; border-radius: 4px;'
        
        styled_df = summary_df.style.applymap(color_ou_count, subset=['Operating Units Count'])
        
        st.dataframe(
            styled_df,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Business Unit": st.column_config.TextColumn(width="small"),
                "Description": st.column_config.TextColumn(width="large"),
                "Operating Units Count": st.column_config.NumberColumn(width="small")
            }
        )
        
        # Elegant drill-down selector
        selected_bu = st.selectbox(
            "Select Business Unit to view details:",
            business_units['BUSINESS_UNIT'].unique(),
            key="bu_detail_select",
            help="Select a business unit to see its operating units"
        )
        
        if selected_bu:
            ou_details = filtered_df[filtered_df['BUSINESS_UNIT'] == selected_bu][['OPERATING_UNIT', 'DESCRLONG_ENG']].drop_duplicates()
            
            # Elegant heading with count
            st.markdown(f"""
            <div style="display: flex; align-items: center; gap: 8px; margin: 20px 0 12px 0;">
                <h3 style="color: {TEXT_COLOR}; margin: 0; font-size: 1.1rem;">Operating Units for {selected_bu}</h3>
                <span style="background: {PRIMARY_COLOR}; color: white; padding: 4px 10px; border-radius: 12px; 
                font-size: 12px; font-weight: 500;">{len(ou_details)} units</span>
            </div>
            """, unsafe_allow_html=True)
            
            # Elegant cards in columns
            cols = st.columns(2)
            for i, (_, row) in enumerate(ou_details.iterrows()):
                with cols[i % 2]:
                    st.markdown(
                        f"""
                        <div style="padding: 16px; margin-bottom: 12px; background-color: {CARD_COLOR}; 
                        border-radius: 8px; border-left: 4px solid {ACCENT_COLOR}; 
                        border: 1px solid {BORDER_COLOR}; box-shadow: 0 2px 6px rgba(0,0,0,0.03);
                        transition: all 0.2s;">
                            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M19 21V5C19 3.89543 18.1046 3 17 3H7C5.89543 3 5 3.89543 5 5V21M19 21L21 21M19 21H14M5 21L3 21M5 21H10M9 6.99998H10M9 11H10M14 6.99998H15M14 11H15M10 21V16C10 15.4477 10.4477 15 11 15H13C13.5523 15 14 15.4477 14 16V21M10 21H14" 
                                          stroke="{ACCENT_COLOR}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                                </svg>
                                <div style="font-weight: 600; color: {PRIMARY_COLOR}; font-size: 15px;">
                                    {row['OPERATING_UNIT']}
                                </div>
                            </div>
                            <div style="color: {LIGHT_TEXT}; font-size: 14px; margin-top: 4px; padding-left: 26px;">
                                {row['DESCRLONG_ENG'] if pd.notna(row['DESCRLONG_ENG']) else 'No description available'}
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
    
    with tab3:
        # Elegant visualization section
        st.markdown(
            f"<h3 style='color:{TEXT_COLOR}; margin-bottom: 16px; font-size: 1.25rem;'>Organizational Analytics</h3>", 
            unsafe_allow_html=True
        )
        
        # Prepare data for the charts
        graph_data = filtered_df[['National Level', 'BUSINESS_UNIT', 'OPERATING_UNIT']].drop_duplicates()
        graph_data = graph_data.rename(columns={
            'National Level': 'level1',
            'BUSINESS_UNIT': 'level2',
            'OPERATING_UNIT': 'level3'
        })
        
        # Check if we have more than 15 business units
        if len(graph_data['level2'].unique()) > 15:
            st.warning("Showing top 15 business units by operating unit count (out of {} total)".format(
                len(graph_data['level2'].unique())
            ))
            
            # Get top 15 business units by number of operating units
            top_business_units = (graph_data.groupby('level2')['level3']
                                     .count()
                                     .sort_values(ascending=False)
                                     .head(15)
                                     .index.tolist())
            
            # Filter the graph data to only include top 15
            graph_data = graph_data[graph_data['level2'].isin(top_business_units)]
        
        # Elegant visualization selector
        viz_option = st.radio(
            "Select Visualization Type:",
            ["Sunburst Chart", "Treemap", "Icicle Chart", "Bar Chart Summary"],
            horizontal=True,
            key="viz_type_selector",
            help="Choose how to visualize the organizational hierarchy"
        )
        
        if viz_option == "Sunburst Chart":
            # Elegant Sunburst chart with teal theme
            fig = px.sunburst(
                graph_data,
                path=['level1', 'level2', 'level3'],
                title=f"<b>Hierarchy for {selected_level}</b>" + (" (Top 15)" if len(graph_data['level2'].unique()) > 15 else ""),
                width=800,
                height=650,
                color_discrete_sequence=CHART_COLORS
            )
            
            # Professional layout
            fig.update_layout(
                margin=dict(t=60, l=0, r=0, b=0),
                hoverlabel=dict(
                    bgcolor="white",
                    font_size=12,
                    font_family="Arial",
                    bordercolor=PRIMARY_COLOR
                ),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                title_font=dict(size=18, color=TEXT_COLOR, family="Arial"),
                font=dict(family="Arial", size=12, color=TEXT_COLOR),
                uniformtext=dict(minsize=10, mode='hide'),
                showlegend=False
            )
            
            # Professional hover template
            fig.update_traces(
                hovertemplate="<b>%{label}</b><br>Level: %{id}<extra></extra>",
                textinfo="label+percent entry",
                textfont=dict(size=12),
                insidetextorientation='radial',
                marker=dict(line=dict(width=0.5, color='white'))
            )
            st.plotly_chart(fig, use_container_width=True)
            
        elif viz_option == "Treemap":
            # Elegant Treemap with teal/coral color scale
            fig = px.treemap(
                graph_data,
                path=['level1', 'level2', 'level3'],
                title=f"<b>Treemap View for {selected_level}</b>" + (" (Top 15)" if len(graph_data['level2'].unique()) > 15 else ""),
                color='level2',
                color_discrete_sequence=CHART_COLORS,
                width=800,
                height=600
            )
            
            fig.update_layout(
                margin=dict(t=60, l=0, r=0, b=0),
                paper_bgcolor='rgba(0,0,0,0)',
                title_font=dict(size=18, color=TEXT_COLOR, family="Arial"),
                font=dict(family="Arial", size=12, color=TEXT_COLOR),
                hoverlabel=dict(
                    bgcolor="white",
                    font_size=12,
                    font_family="Arial"
                ),
                uniformtext=dict(minsize=10, mode='hide'),
                showlegend=False
            )
            
            fig.update_traces(
                textfont=dict(size=12),
                marker=dict(line=dict(width=0.5, color='white')),
                textposition="middle center"
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
        elif viz_option == "Icicle Chart":
            # Elegant Icicle chart
            fig = px.icicle(
                graph_data,
                path=['level1', 'level2', 'level3'],
                title=f"<b>Icicle View for {selected_level}</b>" + (" (Top 15)" if len(graph_data['level2'].unique()) > 15 else ""),
                color='level2',
                color_discrete_sequence=ALT_CHART_COLORS,
                width=800,
                height=600
            )
            
            fig.update_layout(
                margin=dict(t=60, l=0, r=0, b=0),
                paper_bgcolor='rgba(0,0,0,0)',
                title_font=dict(size=18, color=TEXT_COLOR, family="Arial"),
                font=dict(family="Arial", size=12, color=TEXT_COLOR),
                hoverlabel=dict(
                    bgcolor="white",
                    font_size=12,
                    font_family="Arial"
                ),
                showlegend=False
            )
            
            fig.update_traces(
                textfont=dict(size=12),
                marker=dict(line=dict(width=0.5, color='white')),
                tiling=dict(orientation='h'),
                insidetextfont=dict(size=11)
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
        else:  # Bar Chart Summary
            # Elegant bar chart showing business units by operating unit count
            summary = graph_data.groupby('level2')['level3'].count().reset_index()
            summary = summary.sort_values('level3', ascending=False)
            
            fig = px.bar(
                summary,
                x='level3',
                y='level2',
                orientation='h',
                title=f"<b>Business Units by Operating Unit Count</b>",
                labels={'level3': 'Number of Operating Units', 'level2': 'Business Unit'},
                color='level3',
                color_continuous_scale=ALT_CHART_COLORS,
                text='level3',
                height=550
            )
            
            fig.update_layout(
                margin=dict(t=60, l=0, r=0, b=0),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor=CARD_COLOR,
                title_font=dict(size=18, color=TEXT_COLOR, family="Arial"),
                font=dict(family="Arial", size=12, color=TEXT_COLOR),
                yaxis=dict(
                    autorange="reversed",
                    showgrid=False,
                    title=None
                ),
                xaxis=dict(
                    showgrid=True, 
                    gridcolor=CHART_GRID_COLOR, 
                    gridwidth=1,
                    title=None
                ),
                coloraxis_showscale=False,
                hoverlabel=dict(
                    bgcolor="white",
                    font_size=12,
                    font_family="Arial"
                )
            )

            fig.update_traces(
                textposition='outside',
                marker_line_color='white',
                marker_line_width=0.5,
                opacity=0.9,
                textfont=dict(size=11, color=PRIMARY_COLOR),
                hovertemplate="<b>%{y}</b><br>Count: %{x}<extra></extra>"
            )
            
            st.plotly_chart(fig, use_container_width=True)
    
    # Elegant download section
    st.divider()
    with st.container():
        st.markdown(
            f"<h3 style='color:{TEXT_COLOR}; margin-bottom: 16px; font-size: 1.25rem;'>Data Export</h3>", 
            unsafe_allow_html=True
        )
        
        # Prepare data for download
        export_df = filtered_df[['BUSINESS_UNIT', 'BU_Description', 'OPERATING_UNIT', 'DESCRLONG_ENG']].drop_duplicates()
        
        col1, col2 = st.columns(2)
        with col1:
            csv = export_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download Full Data (CSV)",
                data=csv,
                file_name=f"fmis_entities_{selected_level.replace(' ', '_')}.csv",
                mime="text/csv",
                help="Download all business units and operating units as a CSV file",
                use_container_width=True
            )


if __name__ == "__main__":
    FmisEntity()






