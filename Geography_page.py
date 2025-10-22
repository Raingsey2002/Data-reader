# import streamlit as st
# import pandas as pd 

# def Geography():
#     st.markdown(
#         """
#         <h1 style="text-align: center; color: #1f2937; font-size: 40px; font-weight: bold; padding: 10px;">
#             ភូមិសាស្រ្ត
#         </h1>
#         """,
#         unsafe_allow_html=True,
#     )

#     # Create layout columns
#     col1, col2, col3, col4 = st.columns([30, 5, 5, 2])

#     # Text search
#     with col1:
#         text_search = st.text_input("និយមន័យពី ទិន្នន័យមេ ​​ស្វែងយល់បន្ថែម", value="")

#     # Year selection
#     with col2:
#         options = ("2000", "2023", "2024", "2025")
#         option = st.selectbox("ឆ្នាំ", options, index=options.index("2025"))

#     # Status selection
#     with col3:
#         status_options = ("Active", "Inactive")
#         selected_status = st.selectbox("ស្ថានភាព", status_options, index=0)

#     # Load Excel file
#     file_path = "Geographyfordatareader.xlsx"
#     df = pd.read_excel(file_path, dtype=str).fillna("")
#     df = df[['PRODUCT', 'Len', 'EFFDT', 'EFFDT_Year', 'EFF_STATUS', 'DESCRLONG_KHM', 'នៅក្រោមខេត្ត']]

#     # Convert date fields
#     df['EFFDT'] = pd.to_datetime(df['EFFDT'], errors='coerce')
#     df['Effective_date'] = df['EFFDT_Year'].astype(str) + '-2025'

#     df['EFF_STATUS'] = df['EFF_STATUS'].map({'A': 'Active', 'I': 'Inactive'})

#     df[['Start_Year', 'End_Year']] = df['Effective_date'].str.split('-', expand=True)
#     df['Start_Year'] = df['Start_Year'].astype(int)
#     df['End_Year'] = df['End_Year'].astype(int)

#     selected_year = int(option)

#     # Filter by year and status
#     filtered_df = df[(df['Start_Year'] <= selected_year) & (df['End_Year'] >= selected_year)]
#     filtered_df = filtered_df[filtered_df['EFF_STATUS'] == selected_status]

#     # Filter by search text
#     if text_search:
#         mask1 = filtered_df["DESCRLONG_KHM"].str.contains(text_search, case=False, na=False)
#         mask2 = filtered_df["PRODUCT"].str.contains(text_search, case=False, na=False)
#         filtered_df = filtered_df[mask1 | mask2]

#     # Display filtered results
#     st.subheader("Filtered Results")
#     filtered_df = filtered_df.head(12)

#     if not filtered_df.empty:
#         num_cards = len(filtered_df)
#         cards_per_col = (num_cards + 2) // 3

#         col1_df = filtered_df.iloc[:cards_per_col]
#         col2_df = filtered_df.iloc[cards_per_col:2*cards_per_col]
#         col3_df = filtered_df.iloc[2*cards_per_col:]

#         cols = st.columns(3)

#         for i, col_df in enumerate([col1_df, col2_df, col3_df]):
#             with cols[i]:
#                 for _, row in col_df.iterrows():
#                     province = str(row['នៅក្រោមខេត្ត']).strip() if pd.notna(row['នៅក្រោមខេត្ត']) else None
#                     province_text = (
#                         f"<p style='font-size: 16px;'><b style='color:#28a745;'>🏛 ស្ថិតនៅក្រោមខេត្ត:</b> {province}</p>"
#                         if province else ""
#                     )

#                     card_html = f"""
#                     <div style="border: 1px solid #ddd; border-radius: 10px; padding: 20px; margin-bottom: 20px; background-color: #f9f9f9; height: 280px; overflow-y: auto;">
#                         <h4 style="color: #1f2937; font-size: 22px; height: 50px; overflow: hidden; text-overflow: ellipsis;">{row['PRODUCT']}</h4>
#                         <p style="font-size: 18px;"><b style='color:#694a56;'>📅 កាលបរិច្ឆេទមានប្រសិទ្ធភាព:</b> <span style="color: #FF6347;">{row['EFFDT_Year']}-2025</span></p>
#                         <p style="font-size: 18px;"><b style='color:#694a56;'>📖 បរិយាយ:</b> <span style="color: #858585;">{row['DESCRLONG_KHM']}</span></p>
#                         <p style="font-size: 18px;"><b style='color:#694a56;'>ស្ថានភាព:</b> <span style="color:#694a56;">{row['EFF_STATUS']}</span></p>
#                         {province_text}
#                     </div>
#                     """

#                     st.markdown(card_html, unsafe_allow_html=True)
#     else:
#         st.info("No data found for the selected year and search criteria.")


# import streamlit as st
# import pandas as pd
# import pydeck as pdk
# from datetime import datetime

# def Geography():
#     st.markdown(
#         """
#         <h1 style="text-align: center; color: #1f2937; font-size: 40px; font-weight: bold; padding: 10px;">
#             ភូមិសាស្រ្ត
#         </h1>
#         """,
#         unsafe_allow_html=True,
#     )

#     # Create layout columns
#     col1, col2, col3, col4 = st.columns([30, 5, 5, 2])

#     # Text search
#     with col1:
#         text_search = st.text_input("និយមន័យពី ទិន្នន័យមេ ​​ស្វែងយល់បន្ថែម", value="")

#     # Year selection
#     with col2:
#         current_year = datetime.now().year
#         options = [str(year) for year in range(2000, current_year + 1)]
#         option = st.selectbox("ឆ្នាំ", options, index=len(options)-1)

#     # Status selection
#     with col3:
#         status_options = ("Active", "Inactive")
#         selected_status = st.selectbox("ស្ថានភាព", status_options, index=0)

#     # Load Excel file
#     try:
#         file_path = "Geographyfordatareader.xlsx"
#         df = pd.read_excel(file_path, dtype=str).fillna("")
        
#         # Ensure required columns exist
#         required_columns = ['PRODUCT', 'Len', 'EFFDT', 'EFFDT_Year', 'EFF_STATUS', 
#                           'DESCRLONG_KHM', 'នៅក្រោមខេត្ត', 'Type']
        
#         for col in required_columns:
#             if col not in df.columns:
#                 st.error(f"Required column '{col}' not found in the Excel file")
#                 return

#         # Add mock coordinates (replace with your actual coordinates)
#         # This is a simplified approach - you should have real coordinates in your data
#         df['latitude'] = 12.5 + (pd.to_numeric(df['PRODUCT'].str[:2], errors='coerce') / 100)
#         df['longitude'] = 104.5 + (pd.to_numeric(df['PRODUCT'].str[2:4], errors='coerce') / 100)
        
#         # Convert date fields
#         df['EFFDT'] = pd.to_datetime(df['EFFDT'], errors='coerce')
#         df['Effective_date'] = df['EFFDT_Year'].astype(str) + '-' + df['EFFDT_Year'].astype(str)

#         df['EFF_STATUS'] = df['EFF_STATUS'].map({'A': 'Active', 'I': 'Inactive'})

#         # Handle Effective_date (assuming format like "2000-2025")
#         df[['Start_Year', 'End_Year']] = df['Effective_date'].str.split('-', expand=True)
#         df['Start_Year'] = pd.to_numeric(df['Start_Year'], errors='coerce').fillna(0).astype(int)
#         df['End_Year'] = pd.to_numeric(df['End_Year'], errors='coerce').fillna(0).astype(int)

#         selected_year = int(option)

#         # Filter by year and status
#         filtered_df = df[(df['Start_Year'] <= selected_year) & (df['End_Year'] >= selected_year)]
#         filtered_df = filtered_df[filtered_df['EFF_STATUS'] == selected_status]

#         # Filter by search text
#         if text_search:
#             mask1 = filtered_df["DESCRLONG_KHM"].str.contains(text_search, case=False, na=False)
#             mask2 = filtered_df["PRODUCT"].str.contains(text_search, case=False, na=False)
#             filtered_df = filtered_df[mask1 | mask2]

#         # Create map section
#         st.markdown("## ផែនទីកម្ពុជា")
        
#         if not filtered_df.empty:
#             # Create a map layer
#             layer = pdk.Layer(
#                 "ScatterplotLayer",
#                 filtered_df,
#                 get_position=['longitude', 'latitude'],
#                 get_color=[200, 30, 0, 160],
#                 get_radius=10000,
#                 pickable=True
#             )
            
#             # Set the viewport for Cambodia
#             view_state = pdk.ViewState(
#                 longitude=104.990963,  # Approximate center of Cambodia
#                 latitude=12.565679,
#                 zoom=6,
#                 pitch=0
#             )
            
#             # Render the map
#             r = pdk.Deck(
#                 layers=[layer],
#                 initial_view_state=view_state,
#                 tooltip={
#                     "html": "<b>Location:</b> {DESCRLONG_KHM}<br><b>Code:</b> {PRODUCT}<br><b>Province:</b> {នៅក្រោមខេត្ត}",
#                     "style": {
#                         "backgroundColor": "white",
#                         "color": "black"
#                     }
#                 }
#             )
            
#             st.pydeck_chart(r)
#         else:
#             st.warning("No locations found to display on the map.")

#         # Display filtered results in cards
#         st.subheader("Filtered Results")
#         filtered_df = filtered_df.head(12)

#         if not filtered_df.empty:
#             num_cards = len(filtered_df)
#             cards_per_col = (num_cards + 2) // 3

#             col1_df = filtered_df.iloc[:cards_per_col]
#             col2_df = filtered_df.iloc[cards_per_col:2*cards_per_col]
#             col3_df = filtered_df.iloc[2*cards_per_col:]

#             cols = st.columns(3)

#             for i, col_df in enumerate([col1_df, col2_df, col3_df]):
#                 with cols[i]:
#                     for _, row in col_df.iterrows():
#                         province = str(row['នៅក្រោមខេត្ត']).strip() if pd.notna(row['នៅក្រោមខេត្ត']) else None
#                         province_text = (
#                             f"<p style='font-size: 16px;'><b style='color:#28a745;'>🏛 ស្ថិតនៅក្រោមខេត្ត:</b> {province}</p>"
#                             if province else ""
#                         )

#                         card_html = f"""
#                         <div style="border: 1px solid #ddd; border-radius: 10px; padding: 20px; margin-bottom: 20px; background-color: #f9f9f9; height: 280px; overflow-y: auto;">
#                             <h4 style="color: #1f2937; font-size: 22px; height: 50px; overflow: hidden; text-overflow: ellipsis;">{row['PRODUCT']}</h4>
#                             <p style="font-size: 18px;"><b style='color:#694a56;'>📅 កាលបរិច្ឆេទមានប្រសិទ្ធភាព:</b> <span style="color: #FF6347;">{row['EFFDT_Year']}-{row['End_Year']}</span></p>
#                             <p style="font-size: 18px;"><b style='color:#694a56;'>📖 បរិយាយ:</b> <span style="color: #858585;">{row['DESCRLONG_KHM']}</span></p>
#                             <p style="font-size: 18px;"><b style='color:#694a56;'>ស្ថានភាព:</b> <span style="color:#694a56;">{row['EFF_STATUS']}</span></p>
#                             {province_text}
#                         </div>
#                         """

#                         st.markdown(card_html, unsafe_allow_html=True)
#         else:
#             st.info("No data found for the selected year and search criteria.")

#     except FileNotFoundError:
#         st.error("Error: The file 'Geographyfordatareader.xlsx' was not found. Please ensure it's in the correct directory.")
#     except Exception as e:
#         st.error(f"An error occurred while processing the data: {str(e)}")



# import streamlit as st
# import pandas as pd
# import pydeck as pdk

# def Geography():
#     st.markdown(
#         """
#         <h1 style="text-align: center; color: #1f2937; font-size: 40px; font-weight: bold; padding: 10px;">
#             ភូមិសាស្រ្ត
#         </h1>
#         """,
#         unsafe_allow_html=True,
#     )

#     # Create layout columns
#     col1, col2, col3, col4 = st.columns([30, 5, 5, 2])

#     # Text search
#     with col1:
#         text_search = st.text_input("និយមន័យពី ទិន្នន័យមេ ​​ស្វែងយល់បន្ថែម", value="")

#     # Year selection
#     with col2:
#         options = ("2000", "2023", "2024", "2025")
#         option = st.selectbox("ឆ្នាំ", options, index=options.index("2025"))

#     # Status selection
#     with col3:
#         status_options = ("Active", "Inactive")
#         selected_status = st.selectbox("ស្ថានភាព", status_options, index=0)

#     # Load Excel file
#     file_path = "Geographyfordatareader.xlsx"
#     df = pd.read_excel(file_path, dtype=str).fillna("")
#     #df = df[['PRODUCT', 'Len', 'EFFDT', 'EFFDT_Year', 'EFF_STATUS', 'DESCRLONG_KHM', 'នៅក្រោមខេត្ត']]

#     # Convert date fields
#     df['EFFDT'] = pd.to_datetime(df['EFFDT'], errors='coerce')
#     df['Effective_date'] = df['EFFDT_Year'].astype(str) + '-2025'

#     df['EFF_STATUS'] = df['EFF_STATUS'].map({'A': 'Active', 'I': 'Inactive'})

#     df[['Start_Year', 'End_Year']] = df['Effective_date'].str.split('-', expand=True)
#     df['Start_Year'] = df['Start_Year'].astype(int)
#     df['End_Year'] = df['End_Year'].astype(int)

#     selected_year = int(option)

#     # Filter by year and status
#     filtered_df = df[(df['Start_Year'] <= selected_year) & (df['End_Year'] >= selected_year)]
#     filtered_df = filtered_df[filtered_df['EFF_STATUS'] == selected_status]

#     # Filter by search text
#     if text_search:
#         mask1 = filtered_df["DESCRLONG_KHM"].str.contains(text_search, case=False, na=False)
#         mask2 = filtered_df["PRODUCT"].str.contains(text_search, case=False, na=False)
#         filtered_df = filtered_df[mask1 | mask2]

#     # ====================== MAP VISUALIZATION ======================
#     st.markdown("---")
#     st.markdown(
#         """
#         <h2 style="text-align: center; color: #1f2937; font-size: 30px; font-weight: bold; padding: 10px;">
#             ផែនទីខេត្តនៃព្រះរាជាណាចក្រកម្ពុជា
#         </h2>
#         """,
#         unsafe_allow_html=True,
#     )
    
#     # Create a simplified representation of Cambodia provinces
#     # Note: In a real implementation, you would use actual geojson data for Cambodia
#     cambodia_provinces = {
#         'PRODUCT': ['Phnom Penh', 'Siem Reap', 'Battambang', 'Sihanoukville', 'Kampong Cham'],
#         'នៅក្រោមខេត្ត': ['Central', 'Northwest', 'Northwest', 'Southwest', 'Central'],
#         'lat': [11.5564, 13.3622, 13.0957, 10.6275, 11.9934],
#         'lon': [104.9282, 103.8596, 103.2022, 103.5296, 105.4635],
#         'size': [100, 80, 70, 60, 50]
#     }
    
#     map_df = pd.DataFrame(cambodia_provinces)
    
#     # Merge with filtered data
#     if not filtered_df.empty:
#         map_df = pd.merge(
#             map_df,
#             filtered_df[['PRODUCT', 'DESCRLONG_KHM', 'EFF_STATUS']],
#             on='PRODUCT',
#             how='left'
#         ).fillna('No description available')
    
#     # Define a layer to display on the map
#     layer = pdk.Layer(
#         "ScatterplotLayer",
#         map_df,
#         pickable=True,
#         opacity=0.8,
#         stroked=True,
#         filled=True,
#         radius_scale=6,
#         radius_min_pixels=10,
#         radius_max_pixels=100,
#         line_width_min_pixels=1,
#         get_position=["lon", "lat"],
#         get_radius="size",
#         get_fill_color=[255, 140, 0],
#         get_line_color=[0, 0, 0],
#     )
    
#     # Set the viewport location for Cambodia
#     view_state = pdk.ViewState(
#         latitude=12.5657,
#         longitude=104.9910,
#         zoom=6,
#         pitch=40,
#     )
    
#     # Render
#     r = pdk.Deck(
#         layers=[layer],
#         initial_view_state=view_state,
#         tooltip={
#             "html": "<b>Province:</b> {PRODUCT}<br/>"
#                     "<b>Region:</b> {នៅក្រោមខេត្ត}<br/>"
#                     "<b>Description:</b> {DESCRLONG_KHM}<br/>"
#                     "<b>Status:</b> {EFF_STATUS}",
#             "style": {
#                 "backgroundColor": "white",
#                 "color": "black",
#                 "fontFamily": '"Khmer OS System", Arial',
#                 "zIndex": "10000",
#             },
#         },
#         map_style="light",  # or "dark", "satellite", etc.
#     )
    
#     st.pydeck_chart(r)
    
#     # ====================== END MAP VISUALIZATION ======================

#     # Display filtered results
#     st.markdown("---")
#     st.subheader("Filtered Results")
#     filtered_df = filtered_df.head(12)

#     if not filtered_df.empty:
#         num_cards = len(filtered_df)
#         cards_per_col = (num_cards + 2) // 3

#         col1_df = filtered_df.iloc[:cards_per_col]
#         col2_df = filtered_df.iloc[cards_per_col:2*cards_per_col]
#         col3_df = filtered_df.iloc[2*cards_per_col:]

#         cols = st.columns(3)

#         for i, col_df in enumerate([col1_df, col2_df, col3_df]):
#             with cols[i]:
#                 for _, row in col_df.iterrows():
#                     province = str(row['នៅក្រោមខេត្ត']).strip() if pd.notna(row['នៅក្រោមខេត្ត']) else None
#                     province_text = (
#                         f"<p style='font-size: 16px;'><b style='color:#28a745;'>🏛 ស្ថិតនៅក្រោមខេត្ត:</b> {province}</p>"
#                         if province else ""
#                     )

#                     card_html = f"""
#                     <div style="border: 1px solid #ddd; border-radius: 10px; padding: 20px; margin-bottom: 20px; background-color: #f9f9f9; height: 280px; overflow-y: auto;">
#                         <h4 style="color: #1f2937; font-size: 22px; height: 50px; overflow: hidden; text-overflow: ellipsis;">{row['PRODUCT']}</h4>
#                         <p style="font-size: 18px;"><b style='color:#694a56;'>📅 កាលបរិច្ឆេទមានប្រសិទ្ធភាព:</b> <span style="color: #FF6347;">{row['EFFDT_Year']}-2025</span></p>
#                         <p style="font-size: 18px;"><b style='color:#694a56;'>📖 បរិយាយ:</b> <span style="color: #858585;">{row['DESCRLONG_KHM']}</span></p>
#                         <p style="font-size: 18px;"><b style='color:#694a56;'>ស្ថានភាព:</b> <span style="color:#694a56;">{row['EFF_STATUS']}</span></p>
#                         {province_text}
#                     </div>
#                     """

#                     st.markdown(card_html, unsafe_allow_html=True)
#     else:
#         st.info("No data found for the selected year and search criteria.")



# import streamlit as st
# import pandas as pd
# import pydeck as pdk

# def Geography():
#     st.markdown(
#         """
#         <h1 style="text-align: center; color: #1f2937; font-size: 40px; font-weight: bold; padding: 10px;">
#             ភូមិសាស្រ្ត
#         </h1>
#         """,
#         unsafe_allow_html=True,
#     )

#     # Create layout columns
#     col1, col2, col3, col4 = st.columns([30, 5, 5, 2])

#     # Text search
#     with col1:
#         text_search = st.text_input("និយមន័យពី ទិន្នន័យមេ ​​ស្វែងយល់បន្ថែម", value="")

#     # Year selection
#     with col2:
#         options = ("2000", "2023", "2024", "2025")
#         option = st.selectbox("ឆ្នាំ", options, index=options.index("2025"))

#     # Status selection
#     with col3:
#         status_options = ("Active", "Inactive")
#         selected_status = st.selectbox("ស្ថានភាព", status_options, index=0)

#     # Load Excel file
#     file_path = "Geographyfordatareader.xlsx"
#     df = pd.read_excel(file_path, dtype=str).fillna("")
    
#     # Convert date fields
#     df['EFFDT'] = pd.to_datetime(df['EFFDT'], errors='coerce')
#     df['Effective_date'] = df['EFFDT_Year'].astype(str) + '-2025'

#     df['EFF_STATUS'] = df['EFF_STATUS'].map({'A': 'Active', 'I': 'Inactive'})

#     df[['Start_Year', 'End_Year']] = df['Effective_date'].str.split('-', expand=True)
#     df['Start_Year'] = df['Start_Year'].astype(int)
#     df['End_Year'] = df['End_Year'].astype(int)

#     selected_year = int(option)

#     # Filter by year and status
#     filtered_df = df[(df['Start_Year'] <= selected_year) & (df['End_Year'] >= selected_year)]
#     filtered_df = filtered_df[filtered_df['EFF_STATUS'] == selected_status]

#     # Filter by search text
#     if text_search:
#         mask1 = filtered_df["DESCRLONG_KHM"].str.contains(text_search, case=False, na=False)
#         mask2 = filtered_df["PRODUCT"].str.contains(text_search, case=False, na=False)
#         filtered_df = filtered_df[mask1 | mask2]

# # ====================== MAP VISUALIZATION ======================
#     st.markdown("---")
#     st.markdown(
#         """
#         <h2 style="text-align: center; color: #1f2937; font-size: 30px; font-weight: bold; padding: 10px;">
#             ផែនទីខេត្តនៃព្រះរាជាណាចក្រកម្ពុជា
#         </h2>
#         """,
#         unsafe_allow_html=True,
#     )

#     # Prepare the data for mapping
#     province_df = filtered_df.copy()

#     # Convert coordinates
#     province_df['Latitude'] = pd.to_numeric(province_df['Latitude'], errors='coerce')
#     province_df['Longitude'] = pd.to_numeric(province_df['Longitude'], errors='coerce')

#     # Drop missing coordinates
#     province_df = province_df.dropna(subset=['Latitude', 'Longitude'])

#     # If empty, show warning
#     if province_df.empty:
#         st.warning("No geographic data available for the selected criteria.")
#         return

#     # ====================== NEW: COUNT VALUES ======================
#     # Count how many times each province appears
#     province_counts = province_df['Province_English'].value_counts().reset_index()
#     province_counts.columns = ['Province_English', 'count']

#     # Merge count into main DataFrame
#     province_df = province_df.merge(province_counts, on='Province_English', how='left')

#     # Normalize the count for visualization size (optional scale)
#     province_df['size'] = province_df['count'] * 20  # Adjust multiplier for visibility

#     # ====================== MAP LAYERS ======================
#     layer = pdk.Layer(
#         "ScatterplotLayer",
#         province_df,
#         pickable=True,
#         opacity=0.8,
#         stroked=True,
#         filled=True,
#         radius_scale=1,
#         radius_min_pixels=5,
#         radius_max_pixels=100,
#         line_width_min_pixels=1,
#         get_position=["Longitude", "Latitude"],
#         get_radius="size",
#         get_fill_color=[255, 140, 0, 200],  # Orange
#         get_line_color=[0, 0, 0],
#     )

#     text_layer = pdk.Layer(
#         "TextLayer",
#         province_df,
#         pickable=False,
#         get_position=["Longitude", "Latitude"],
#         get_text="Province_Khmer",
#         get_size=16,
#         get_color=[0, 0, 0, 200],
#         get_angle=0,
#         get_text_anchor="'middle'",
#         get_alignment_baseline="'center'",
#     )

#     view_state = pdk.ViewState(
#         latitude=12.5657,
#         longitude=104.9910,
#         zoom=6,
#         pitch=0,
#     )

#     # ====================== RENDER MAP ======================
#     r = pdk.Deck(
#         layers=[layer, text_layer],
#         initial_view_state=view_state,
#         tooltip={
#             "html": "<b>ខេត្ត:</b> {Province_Khmer}<br/>"
#                     "<b>ភូមិសាស្រ្តដែលស្ថិតក្រោម{Province_Khmer}:</b> {count}<br/>",
#             "style": {
#                 "backgroundColor": "white",
#                 "color": "black",
#                 "fontFamily": '"Khmer OS System", Arial',
#                 "zIndex": "10000",
#             },
#         },
#         map_style="light",
#     )

#     st.pydeck_chart(r)

    

#     # Display filtered results
#     st.markdown("---")
#     st.subheader("Filtered Results")
#     filtered_df = filtered_df.head(12)

#     if not filtered_df.empty:
#         num_cards = len(filtered_df)
#         cards_per_col = (num_cards + 2) // 3

#         col1_df = filtered_df.iloc[:cards_per_col]
#         col2_df = filtered_df.iloc[cards_per_col:2*cards_per_col]
#         col3_df = filtered_df.iloc[2*cards_per_col:]

#         cols = st.columns(3)

#         for i, col_df in enumerate([col1_df, col2_df, col3_df]):
#             with cols[i]:
#                 for _, row in col_df.iterrows():
#                     province = str(row['នៅក្រោមខេត្ត']).strip() if pd.notna(row['នៅក្រោមខេត្ត']) else None
#                     province_text = (
#                         f"<p style='font-size: 16px;'><b style='color:#28a745;'>🏛 ស្ថិតនៅក្រោមខេត្ត:</b> {province}</p>"
#                         if province else ""
#                     )

#                     card_html = f"""
#                     <div style="border: 1px solid #ddd; border-radius: 10px; padding: 20px; margin-bottom: 20px; background-color: #f9f9f9; height: 280px; overflow-y: auto;">
#                         <h4 style="color: #1f2937; font-size: 22px; height: 50px; overflow: hidden; text-overflow: ellipsis;">{row['PRODUCT']}</h4>
#                         <p style="font-size: 18px;"><b style='color:#694a56;'>📅 កាលបរិច្ឆេទមានប្រសិទ្ធភាព:</b> <span style="color: #FF6347;">{row['EFFDT_Year']}-2025</span></p>
#                         <p style="font-size: 18px;"><b style='color:#694a56;'>📖 បរិយាយ:</b> <span style="color: #858585;">{row['DESCRLONG_KHM']}</span></p>
#                         <p style="font-size: 18px;"><b style='color:#694a56;'>ស្ថានភាព:</b> <span style="color:#694a56;">{row['EFF_STATUS']}</span></p>
#                         {province_text}
#                     </div>
#                     """

#                     st.markdown(card_html, unsafe_allow_html=True)
#     else:
#         st.info("No data found for the selected year and search criteria.")





# import streamlit as st
# import pandas as pd
# import pydeck as pdk

# def Geography():
#     # Set page config (if this is your main page)
#     # st.set_page_config(layout="wide", page_title="ភូមិសាស្រ្ត - Geography Dashboard")

#     # Custom CSS for better styling
#     st.markdown("""
#     <style>
#         .main {background-color: #f8f9fa;}
#         .stSelectbox, .stTextInput {background-color: white;}
#         .tab-container {background-color: white; border-radius: 10px; padding: 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);}
#         .card {border: none !important; box-shadow: 0 4px 8px rgba(0,0,0,0.1); transition: transform 0.3s;}
#         .card:hover {transform: translateY(-5px);}
#         .map-container {border-radius: 10px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.15);}
#         .header {color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px;}
#         .metric-card {background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);}
#         .config-box {background-color: white; border-radius: 10px; padding: 20px; margin-bottom: 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);}
#         @font-face {font-family: 'Khmer OS'; src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts@master/phaseIII_only/unhinted/NotoSansKhmer/NotoSansKhmer-Regular.ttf') format('truetype');}
#         body {font-family: 'Khmer OS', Arial, sans-serif;}
#     </style>
#     """, unsafe_allow_html=True)

#     # Main title with better styling
#     st.markdown(
#         """
#         <div style='text-align: center; margin-bottom: 30px;'>
#             <h1 style='color: #2c3e50; font-size: 2.5rem; font-weight: 700; margin-bottom: 10px;'>
#                 ភូមិសាស្ត្រកម្ពុជា
#             </h1>
#             <p style='color: #7f8c8d; font-size: 1.1rem;'>
#                 ប្រព័ន្ធព័ត៌មានភូមិសាស្ត្រនៃព្រះរាជាណាចក្រកម្ពុជា
#             </p>
#         </div>
#         """,
#         unsafe_allow_html=True
#     )

#     # Create tabs for different views (now only 2 tabs)
#     tab1, tab2 = st.tabs(["🗺 ផែនទីខេត្ត & ស្ថិតិ", "📋 ទិន្នន័យលម្អិត"])

#     # Load data once (cached for better performance)
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
#         return df

#     df = load_data()

#     # Tab 1: Combined Map and Statistics
#     with tab1:
#         # Create columns for filters at the top
#         col1, col2, col3 = st.columns([2, 1, 1])
        
#         with col1:
#             text_search = st.text_input("ស្វែងរកពាក្យ", value="")
        
#         with col2:
#             options = ("2000", "2023", "2024", "2025")
#             option = st.selectbox("ឆ្នាំ", options, index=options.index("2025"))
#             selected_year = int(option)
        
#         with col3:
#             status_options = ("Active", "Inactive")
#             selected_status = st.selectbox("ស្ថានភាព", status_options, index=0)

#         # Filter data based on selections
#         filtered_df = df[(df['Start_Year'] <= selected_year) & (df['End_Year'] >= selected_year)]
#         filtered_df = filtered_df[filtered_df['EFF_STATUS'] == selected_status]
        
#         if text_search:
#             mask1 = filtered_df["DESCRLONG_KHM"].str.contains(text_search, case=False, na=False)
#             mask2 = filtered_df["PRODUCT"].str.contains(text_search, case=False, na=False)
#             filtered_df = filtered_df[mask1 | mask2]

#         # First row - Metrics
#         st.markdown("---")
#         st.markdown(
#             """
#             <div class='header'>
#                 <h2 style='color: #2c3e50;'>ស្ថិតិភូមិសាស្ត្រ</h2>
#             </div>
#             """,
#             unsafe_allow_html=True
#         )
        
#         if not filtered_df.empty:
#             col1, col2, col3, col4 = st.columns(4)
            
#             with col1:
#                 st.markdown(
#                     """
#                     <div class='metric-card' style='padding: 20px; border-radius: 10px;'>
#                         <h3 style='color: #2c3e50; margin-top: 0;'>ចំនួនសរុប</h3>
#                         <p style='font-size: 2rem; color: #3498db; font-weight: bold;'>{}</p>
#                     </div>
#                     """.format(len(filtered_df)),
#                     unsafe_allow_html=True
#                 )
            
#             with col2:
#                 st.markdown(
#                     """
#                     <div class='metric-card' style='padding: 20px; border-radius: 10px;'>
#                         <h3 style='color: #2c3e50; margin-top: 0;'>ខេត្តដែលមានទិន្នន័យ</h3>
#                         <p style='font-size: 2rem; color: #e74c3c; font-weight: bold;'>{}</p>
#                     </div>
#                     """.format(filtered_df['Province_English'].nunique()),
#                     unsafe_allow_html=True
#                 )
            
#             with col3:
#                 st.markdown(
#                     """
#                     <div class='metric-card' style='padding: 20px; border-radius: 10px;'>
#                         <h3 style='color: #2c3e50; margin-top: 0;'>ឆ្នាំដែលបានជ្រើសរើស</h3>
#                         <p style='font-size: 2rem; color: #2ecc71; font-weight: bold;'>{}</p>
#                     </div>
#                     """.format(selected_year),
#                     unsafe_allow_html=True
#                 )
            
#             with col4:
#                 active_count = len(filtered_df[filtered_df['EFF_STATUS'] == 'Active'])
#                 st.markdown(
#                     """
#                     <div class='metric-card' style='padding: 20px; border-radius: 10px;'>
#                         <h3 style='color: #2c3e50; margin-top: 0;'>សកម្ម</h3>
#                         <p style='font-size: 2rem; color: #9b59b6; font-weight: bold;'>{}</p>
#                     </div>
#                     """.format(active_count),
#                     unsafe_allow_html=True
#                 )
            
#             # Top provinces chart
#             st.markdown("---")
#             st.markdown("#### ខេត្តដែលមានទិន្នន័យច្រើនបំផុត")
#             top_provinces = filtered_df['Province_English'].value_counts().head(10).reset_index()
#             top_provinces.columns = ['Province', 'Count']
#             st.bar_chart(top_provinces.set_index('Province'))
            
#             # Map Visualization
#             st.markdown("---")
#             st.markdown(
#                 """
#                 <div class='header'>
#                     <h2 style='color: #2c3e50;'>ផែនទីខេត្តនៃព្រះរាជាណាចក្រកម្ពុជា</h2>
#                 </div>
#                 """,
#                 unsafe_allow_html=True
#             )
            
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
#                     radius_max_pixels=120,
#                     line_width_min_pixels=1,
#                     get_position=["Longitude", "Latitude"],
#                     get_radius="size",
#                     get_fill_color=[52, 152, 219, 200],  # Blue color
#                     get_line_color=[0, 0, 0],
#                 )

#                 text_layer = pdk.Layer(
#                     "TextLayer",
#                     province_df,
#                     pickable=False,
#                     get_position=["Longitude", "Latitude"],
#                     get_text="Province_Khmer",
#                     get_size=16,
#                     get_color=[0, 0, 0, 200],
#                     get_angle=0,
#                     get_text_anchor="'middle'",
#                     get_alignment_baseline="'center'",
#                 )

#                 view_state = pdk.ViewState(
#                     latitude=12.5657,
#                     longitude=104.9910,
#                     zoom=6,
#                     pitch=0,
#                 )

#                 # Render the map in a container
#                 with st.container():
#                     st.pydeck_chart(
#                         pdk.Deck(
#                             layers=[layer, text_layer],
#                             initial_view_state=view_state,
#                             tooltip={
#                                 "html": """
#                                 <div style="padding: 10px; font-family: 'Khmer OS', Arial;">
#                                     <b>ខេត្ត:</b> {Province_Khmer}<br/>
#                                     <b>ចំនួនទិន្នន័យ:</b> {count}<br/>
#                                     <b>ស្ថានភាព:</b> {EFF_STATUS}<br/>
#                                 </div>
#                                 """,
#                                 "style": {
#                                     "backgroundColor": "white",
#                                     "color": "#2c3e50",
#                                     "fontFamily": "'Khmer OS', Arial",
#                                     "borderRadius": "5px",
#                                     "boxShadow": "0 2px 10px rgba(0,0,0,0.1)"
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

#     # Tab 2: Detailed Data with Configuration
#     with tab2:
#         # Configuration box at the top
#         with st.container():
#             st.markdown(
#                 """
#                 <div class='config-box'>
#                     <h3 style='color: #2c3e50; margin-top: 0;'>ការកំណត់រចនាសម្ព័ន្ធ</h3>
#                 """,
#                 unsafe_allow_html=True
#             )
            
#             col1, col2, col3 = st.columns([2, 1, 1])
            
#             with col1:
#                 tab2_text_search = st.text_input("ស្វែងរកពាក្យ (ទិន្នន័យលម្អិត)", value=text_search if 'text_search' in locals() else "")
            
#             with col2:
#                 options = ("2000", "2023", "2024", "2025")
#                 tab2_option = st.selectbox("ឆ្នាំ (ទិន្នន័យលម្អិត)", options, index=options.index(option) if 'option' in locals() else options.index("2025"))
#                 tab2_selected_year = int(tab2_option)
            
#             with col3:
#                 status_options = ("Active", "Inactive")
#                 tab2_selected_status = st.selectbox("ស្ថានភាព (ទិន្នន័យលម្អិត)", status_options, index=status_options.index(selected_status) if 'selected_status' in locals() else 0)
            
#             st.markdown("</div>", unsafe_allow_html=True)
        
#         # Filter data based on selections
#         tab2_filtered_df = df[(df['Start_Year'] <= tab2_selected_year) & (df['End_Year'] >= tab2_selected_year)]
#         tab2_filtered_df = tab2_filtered_df[tab2_filtered_df['EFF_STATUS'] == tab2_selected_status]
        
#         if tab2_text_search:
#             mask1 = tab2_filtered_df["DESCRLONG_KHM"].str.contains(tab2_text_search, case=False, na=False)
#             mask2 = tab2_filtered_df["PRODUCT"].str.contains(tab2_text_search, case=False, na=False)
#             tab2_filtered_df = tab2_filtered_df[mask1 | mask2]

#         # Data display
#         st.markdown(
#             """
#             <div class='header'>
#                 <h2 style='color: #2c3e50;'>ទិន្នន័យលម្អិត</h2>
#             </div>
#             """,
#             unsafe_allow_html=True
#         )
        
#         if not tab2_filtered_df.empty:
#             # Display filtered results in a nice grid
#             num_cards = len(tab2_filtered_df)
#             cards_per_col = (num_cards + 2) // 3

#             col1_df = tab2_filtered_df.iloc[:cards_per_col]
#             col2_df = tab2_filtered_df.iloc[cards_per_col:2*cards_per_col]
#             col3_df = tab2_filtered_df.iloc[2*cards_per_col:]

#             cols = st.columns(3)

#             for i, col_df in enumerate([col1_df, col2_df, col3_df]):
#                 with cols[i]:
#                     for _, row in col_df.iterrows():
#                         province = str(row['នៅក្រោមខេត្ត']).strip() if pd.notna(row['នៅក្រោមខេត្ត']) else None
#                         province_text = (
#                             f"<p style='font-size: 16px;'><b style='color:#28a745;'>🏛 ស្ថិតនៅក្រោមខេត្ត:</b> {province}</p>"
#                             if province else ""
#                         )

#                         card_html = f"""
#                         <div class='card' style='border-radius: 10px; padding: 20px; margin-bottom: 20px; background-color: white; height: 280px; overflow-y: auto;'>
#                             <h4 style='color: #2c3e50; font-size: 20px; height: 50px; overflow: hidden; text-overflow: ellipsis;'>{row['PRODUCT']}</h4>
#                             <p style='font-size: 16px;'><b style='color:#7f8c8d;'>📅 កាលបរិច្ឆេទ:</b> <span style='color: #e74c3c;'>{row['EFFDT_Year']}-2025</span></p>
#                             <p style='font-size: 16px;'><b style='color:#7f8c8d;'>📖 បរិយាយ:</b> <span style='color: #95a5a6;'>{row['DESCRLONG_KHM']}</span></p>
#                             <p style='font-size: 16px;'><b style='color:#7f8c8d;'>ស្ថានភាព:</b> <span style='color: {'#2ecc71' if row['EFF_STATUS'] == 'Active' else '#e74c3c'};'>{row['EFF_STATUS']}</span></p>
#                             {province_text}
#                         </div>
#                         """
#                         st.markdown(card_html, unsafe_allow_html=True)
#         else:
#             st.info("No data found for the selected filters.")

# if __name__ == "__main__":
#     Geography()

# import streamlit as st
# import pandas as pd
# import pydeck as pdk
# from datetime import datetime

# def Geography():
#     # Set page config with wider layout and custom title
#     # st.set_page_config(
#     #     layout="wide",
#     #     page_title="ភូមិសាស្រ្ត - Cambodia Geography Dashboard",
#     #     page_icon="🇰🇭"
#     # )

#     # Custom CSS for professional styling
#     st.markdown("""
#     <style>
#         :root {
#             --primary-color: #3498db;
#             --secondary-color: #2c3e50;
#             --accent-color: #e74c3c;
#             --light-bg: #f8f9fa;
#             --card-shadow: 0 4px 6px rgba(0,0,0,0.1);
#             --transition: all 0.3s ease;
#         }
        
#         .main {
#             background-color: var(--light-bg);
#             font-family: 'Khmer OS', 'Arial', sans-serif;
#         }
        
#         .stSelectbox, .stTextInput, .stSlider {
#             background-color: white;
#             border-radius: 8px;
#             box-shadow: var(--card-shadow);
#         }
        
#         .header-card {
#             background: linear-gradient(135deg, #2c3e50 0%, #3498db 100%);
#             color: white;
#             border-radius: 12px;
#             padding: 2rem;
#             margin-bottom: 2rem;
#             box-shadow: var(--card-shadow);
#         }
        
#         .metric-card {
#             background: white;
#             border-radius: 10px;
#             padding: 1.5rem;
#             box-shadow: var(--card-shadow);
#             transition: var(--transition);
#             border-left: 4px solid var(--primary-color);
#         }
        
#         .metric-card:hover {
#             transform: translateY(-5px);
#             box-shadow: 0 10px 20px rgba(0,0,0,0.1);
#         }
        
#         .metric-title {
#             font-size: 1rem;
#             color: #7f8c8d;
#             margin-bottom: 0.5rem;
#         }
        
#         .metric-value {
#             font-size: 2rem;
#             font-weight: 700;
#             color: var(--secondary-color);
#         }
        
#         .data-card {
#             background: white;
#             border-radius: 10px;
#             padding: 1.5rem;
#             margin-bottom: 1.5rem;
#             box-shadow: var(--card-shadow);
#             border-left: 4px solid var(--primary-color);
#             height: 280px;
#             overflow-y: auto;
#         }
        
#         .data-card h4 {
#             color: var(--secondary-color);
#             font-size: 1.2rem;
#             margin-bottom: 1rem;
#             border-bottom: 1px solid #eee;
#             padding-bottom: 0.5rem;
#         }
        
#         .data-card p {
#             margin-bottom: 0.8rem;
#             font-size: 0.95rem;
#         }
        
#         .map-container {
#             border-radius: 12px;
#             overflow: hidden;
#             box-shadow: 0 8px 24px rgba(0,0,0,0.15);
#             margin-top: 1.5rem;
#         }
        
#         .tab-content {
#             padding: 1.5rem 0;
#         }
        
#         .stTabs [data-baseweb="tab-list"] {
#             gap: 10px;
#         }
        
#         .stTabs [data-baseweb="tab"] {
#             background: white;
#             border-radius: 8px 8px 0 0 !important;
#             padding: 10px 20px;
#             transition: var(--transition);
#         }
        
#         .stTabs [aria-selected="true"] {
#             background-color: var(--primary-color) !important;
#             color: white !important;
#         }
        
#         @font-face {
#             font-family: 'Khmer OS';
#             src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts@master/phaseIII_only/unhinted/NotoSansKhmer/NotoSansKhmer-Regular.ttf') format('truetype');
#         }
        
#         body {
#             font-family: 'Khmer OS', 'Arial', sans-serif;
#         }
        
#         /* Custom scrollbar */
#         ::-webkit-scrollbar {
#             width: 8px;
#         }
        
#         ::-webkit-scrollbar-track {
#             background: #f1f1f1;
#             border-radius: 10px;
#         }
        
#         ::-webkit-scrollbar-thumb {
#             background: #888;
#             border-radius: 10px;
#         }
        
#         ::-webkit-scrollbar-thumb:hover {
#             background: #555;
#         }
#     </style>
#     """, unsafe_allow_html=True)

#     # Header with gradient background
#     st.markdown("""
#     <div class="header-card">
#         <div style="text-align: center;">
#             <h1 style="color: white; font-size: 2.5rem; margin-bottom: 0.5rem;">ភូមិសាស្ត្រកម្ពុជា</h1>
#             <p style="color: rgba(255,255,255,0.9); font-size: 1.1rem; margin-bottom: 0;">
#                 ប្រព័ន្ធព័ត៌មានភូមិសាស្ត្រនៃព្រះរាជាណាចក្រកម្ពុជា
#             </p>
#             <p style="color: rgba(255,255,255,0.7); font-size: 0.9rem; margin-top: 0.5rem;">
#                 បច្ចុប្បន្នភាព: {current_date}
#             </p>
#         </div>
#     </div>
#     """.format(current_date=datetime.now().strftime("%d %B %Y")), unsafe_allow_html=True)

#     # Create tabs for different views
#     tab1, tab2 = st.tabs(["🗺 ផែនទីខេត្ត & ស្ថិតិ", "📋 ទិន្នន័យលម្អិត"])

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
#         st.markdown("""
#         <div style="margin-bottom: 2rem;">
#             <h2 style="color: var(--secondary-color); border-bottom: 2px solid var(--primary-color); padding-bottom: 0.5rem;">
#                 ព័ត៌មានទូទៅ
#             </h2>
#         </div>
#         """, unsafe_allow_html=True)
        
#         # Filter controls in a clean layout
#         with st.container():
#             col1, col2, col3 = st.columns([2, 1, 1])
            
#             with col1:
#                 text_search = st.text_input(
#                     "ស្វែងរកពាក្យ",
#                     value="",
#                     placeholder="វាយបញ្ចូលឈ្មោះខេត្ត ឬពាក្យគន្លឹះ...",
#                     help="ស្វែងរកតាមឈ្មោះខេត្ត ឬពាក្យពីការពិពណ៌នា"
#                 )
            
#             with col2:
#                 year_options = ("2000", "2023", "2024", "2025")
#                 selected_year = st.selectbox(
#                     "ឆ្នាំ",
#                     year_options,
#                     index=year_options.index("2025"),
#                     help="ជ្រើសរើសឆ្នាំដើម្បីមើលទិន្នន័យ"
#                 )
#                 selected_year = int(selected_year)
            
#             with col3:
#                 status_options = ("Active", "Inactive")
#                 selected_status = st.selectbox(
#                     "ស្ថានភាព",
#                     status_options,
#                     index=0,
#                     help="ជ្រើសរើសស្ថានភាពនៃទិន្នន័យ"
#                 )
        
#         # Filter data based on selections
#         filtered_df = df[(df['Start_Year'] <= selected_year) & (df['End_Year'] >= selected_year)]
#         filtered_df = filtered_df[filtered_df['EFF_STATUS'] == selected_status]
        
#         if text_search:
#             mask1 = filtered_df["DESCRLONG_KHM"].str.contains(text_search, case=False, na=False)
#             mask2 = filtered_df["PRODUCT"].str.contains(text_search, case=False, na=False)
#             filtered_df = filtered_df[mask1 | mask2]

#         # Key Metrics Section
#         if not filtered_df.empty:
#             st.markdown("""
#             <div style="margin: 2rem 0;">
#                 <h3 style="color: var(--secondary-color); margin-bottom: 1rem;">ស្ថិតិសំខាន់ៗ</h3>
#             </div>
#             """, unsafe_allow_html=True)
            
#             col1, col2, col3, col4 = st.columns(4)
            
#             with col1:
#                 st.markdown(f"""
#                 <div class="metric-card">
#                     <div class="metric-title">ចំនួនសរុប</div>
#                     <div class="metric-value">{len(filtered_df):,}</div>
#                 </div>
#                 """, unsafe_allow_html=True)
            
#             with col2:
#                 st.markdown(f"""
#                 <div class="metric-card">
#                     <div class="metric-title">ចំនួនខេត្ត</div>
#                     <div class="metric-value" style="color: var(--accent-color);">
#                         {filtered_df['Province_English'].nunique():,}
#                     </div>
#                 </div>
#                 """, unsafe_allow_html=True)
            
#             with col3:
#                 st.markdown(f"""
#                 <div class="metric-card">
#                     <div class="metric-title">ឆ្នាំដែលបានជ្រើសរើស</div>
#                     <div class="metric-value" style="color: #2ecc71;">
#                         {selected_year}
#                     </div>
#                 </div>
#                 """, unsafe_allow_html=True)
            
#             with col4:
#                 active_count = len(filtered_df[filtered_df['EFF_STATUS'] == 'Active'])
#                 st.markdown(f"""
#                 <div class="metric-card">
#                     <div class="metric-title">ស្ថានភាពសកម្ម</div>
#                     <div class="metric-value" style="color: #9b59b6;">
#                         {active_count:,}
#                     </div>
#                 </div>
#                 """, unsafe_allow_html=True)
            
#             # Province Distribution Chart
#             st.markdown("---")
#             st.markdown("""
#             <div style="margin-bottom: 1.5rem;">
#                 <h3 style="color: var(--secondary-color);">ការចែកចាយទិន្នន័យតាមខេត្ត</h3>
#                 <p style="color: #7f8c8d;">ខេត្តដែលមានទិន្នន័យច្រើនបំផុត</p>
#             </div>
#             """, unsafe_allow_html=True)
            
#             top_provinces = filtered_df['Province_English'].value_counts().head(10).reset_index()
#             top_provinces.columns = ['Province', 'Count']
            
#             # Use columns to make the chart responsive
#             col1, col2 = st.columns([3, 1])
            
#             with col1:
#                 st.bar_chart(
#                     top_provinces.set_index('Province'),
#                     height=400,
#                     use_container_width=True,
#                     color='#3498db'
#                 )
            
#             with col2:
#                 st.markdown("""
#                 <div style="background: white; border-radius: 10px; padding: 1rem; box-shadow: var(--card-shadow);">
#                     <h4 style="color: var(--secondary-color); margin-top: 0;">ខេត្តកំពូល</h4>
#                     <ol style="padding-left: 1.2rem;">
#                 """, unsafe_allow_html=True)
                
#                 for i, row in top_provinces.iterrows():
#                     st.markdown(f"""
#                     <li style="margin-bottom: 0.5rem;">
#                         <span style="font-weight: 500;">{row['Province']}</span>
#                         <span style="float: right; color: var(--accent-color);">{row['Count']:,}</span>
#                     </li>
#                     """, unsafe_allow_html=True)
                
#                 st.markdown("</ol></div>", unsafe_allow_html=True)
            
#             # Interactive Map Visualization
#             st.markdown("---")
#             st.markdown("""
#             <div style="margin-bottom: 1.5rem;">
#                 <h2 style="color: var(--secondary-color); border-bottom: 2px solid var(--primary-color); padding-bottom: 0.5rem;">
#                     ផែនទីខេត្តនៃព្រះរាជាណាចក្រកម្ពុជា
#                 </h2>
#                 <p style="color: #7f8c8d;">ចុចលើចំណុចនីមួយៗដើម្បីមើលព័ត៌មានលម្អិត</p>
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
#                     radius_max_pixels=120,
#                     line_width_min_pixels=1,
#                     get_position=["Longitude", "Latitude"],
#                     get_radius="size",
#                     get_fill_color=[52, 152, 219, 200],  # Blue color
#                     get_line_color=[0, 0, 0],
#                 )

#                 text_layer = pdk.Layer(
#                     "TextLayer",
#                     province_df,
#                     pickable=False,
#                     get_position=["Longitude", "Latitude"],
#                     get_text="Province_Khmer",
#                     get_size=16,
#                     get_color=[0, 0, 0, 200],
#                     get_angle=0,
#                     get_text_anchor="'middle'",
#                     get_alignment_baseline="'center'",
#                 )

#                 view_state = pdk.ViewState(
#                     latitude=12.5657,
#                     longitude=104.9910,
#                     zoom=6,
#                     pitch=0,
#                 )

#                 # Render the map in a container
#                 with st.container():
#                     st.pydeck_chart(
#                         pdk.Deck(
#                             layers=[layer, text_layer],
#                             initial_view_state=view_state,
#                             tooltip={
#                                 "html": """
#                                 <div style="padding: 10px; font-family: 'Khmer OS', Arial; background: white; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
#                                     <h3 style="margin: 0; color: #2c3e50; border-bottom: 1px solid #eee; padding-bottom: 8px;">{Province_Khmer}</h3>
#                                     <p style="margin: 8px 0;"><b>ចំនួនទិន្នន័យ:</b> <span style="color: #e74c3c;">{count}</span></p>
#                                     <p style="margin: 8px 0;"><b>ស្ថានភាព:</b> <span style="color: {color};">{EFF_STATUS}</span></p>
#                                 </div>
#                                 """.replace("{color}", "'#2ecc71'" if selected_status == "Active" else "'#e74c3c'"),
#                                 "style": {
#                                     "fontFamily": "'Khmer OS', Arial"
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
#         <div style="margin-bottom: 2rem;">
#             <h2 style="color: var(--secondary-color); border-bottom: 2px solid var(--primary-color); padding-bottom: 0.5rem;">
#                 ទិន្នន័យលម្អិត
#             </h2>
#             <p style="color: #7f8c8d;">ព័ត៌មានលម្អិតអំពីភូមិសាស្ត្រកម្ពុជា</p>
#         </div>
#         """, unsafe_allow_html=True)
        
#         # Filter controls
#         with st.container():
#             col1, col2, col3 = st.columns([2, 1, 1])
            
#             with col1:
#                 tab2_text_search = st.text_input(
#                     "ស្វែងរកពាក្យ (ទិន្នន័យលម្អិត)",
#                     value=text_search if 'text_search' in locals() else "",
#                     placeholder="ស្វែងរកពាក្យគន្លឹះ...",
#                     key="tab2_search"
#                 )
            
#             # with col2:
#             #     year_options = ("2000", "2023", "2024", "2025")
#             #     tab2_selected_year = st.selectbox(
#             #         "ឆ្នាំ (ទិន្នន័យលម្អិត)",
#             #         year_options,
#             #         index=year_options.index(selected_year) if 'selected_year' in locals() else year_options.index("2025"),
#             #         key="tab2_year"
#             #     )
#             #     tab2_selected_year = int(tab2_selected_year)
#             with col2:
#                 year_options = ("2000", "2023", "2024", "2025")
#                 # Set default index safely
#                 default_index = 3  # Default to "2025" (index 3)
#                 if 'selected_year' in locals():
#                     try:
#                         default_index = year_options.index(str(selected_year))
#                     except ValueError:
#                         pass  # Use default if not found
                
#                 tab2_selected_year = st.selectbox(
#                     "ឆ្នាំ (ទិន្នន័យលម្អិត)",
#                     year_options,
#                     index=default_index,
#                     key="tab2_year"
#                 )
#                 tab2_selected_year = int(tab2_selected_year)
            
#             with col3:
#                 status_options = ("Active", "Inactive")
#                 tab2_selected_status = st.selectbox(
#                     "ស្ថានភាព (ទិន្នន័យលម្អិត)",
#                     status_options,
#                     index=status_options.index(selected_status) if 'selected_status' in locals() else 0,
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
#             <div style="background: white; border-radius: 10px; padding: 1rem; margin-bottom: 1.5rem; box-shadow: var(--card-shadow);">
#                 <p style="margin: 0; color: var(--secondary-color);">
#                     បានរកឃើញ: <strong>{len(tab2_filtered_df):,}</strong> ធាតុទិន្នន័យ
#                 </p>
#             </div>
#             """, unsafe_allow_html=True)
            
#             # Display filtered results in a responsive grid
#             cols = st.columns(3)
            
#             for idx, row in tab2_filtered_df.iterrows():
#                 with cols[idx % 3]:
#                     province = str(row['នៅក្រោមខេត្ត']).strip() if pd.notna(row['នៅក្រោមខេត្ត']) else None
#                     province_text = (
#                         f"""<p style="margin: 0.5rem 0; font-size: 0.9rem;">
#                             <span style="color: #7f8c8d;">🏛 ខេត្ត:</span> 
#                             <span style="color: #28a745;">{province}</span>
#                         </p>"""
#                         if province else ""
#                     )

#                     st.markdown(f"""
#                     <div class="data-card">
#                         <h4>{row['PRODUCT']}</h4>
#                         <p style="margin: 0.5rem 0;">
#                             <span style="color: #7f8c8d;">📅 ឆ្នាំ:</span> 
#                             <span style="color: var(--accent-color);">{row['EFFDT_Year']}-2025</span>
#                         </p>
#                         <p style="margin: 0.5rem 0;">
#                             <span style="color: #7f8c8d;">📖 ពណ៌នា:</span> 
#                             <span style="color: #95a5a6;">{row['DESCRLONG_KHM'][:100]}{'...' if len(row['DESCRLONG_KHM']) > 100 else ''}</span>
#                         </p>
#                         <p style="margin: 0.5rem 0;">
#                             <span style="color: #7f8c8d;">ស្ថានភាព:</span> 
#                             <span style="color: {'#2ecc71' if row['EFF_STATUS'] == 'Active' else '#e74c3c'};">
#                                 {row['EFF_STATUS']}
#                             </span>
#                         </p>
#                         {province_text}
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

# def Geography():
#     # Custom CSS for professional styling with improved visual hierarchy
#     st.markdown("""
#     <style>
#         :root {
#             --primary-color: #3498db;
#             --primary-dark: #2980b9;
#             --secondary-color: #2c3e50;
#             --accent-color: #e74c3c;
#             --success-color: #27ae60;
#             --light-bg: #f8f9fa;
#             --card-shadow: 0 4px 6px rgba(0,0,0,0.1);
#             --transition: all 0.3s ease;
#             --border-radius: 12px;
#         }
        
#         .main {
#             background-color: var(--light-bg);
#             font-family: 'Khmer OS', 'Arial', sans-serif;
#         }
        
#         .stSelectbox, .stTextInput, .stSlider {
#             background-color: white;
#             border-radius: var(--border-radius);
#             box-shadow: var(--card-shadow);
#             border: 1px solid #e0e0e0;
#         }
        
#         .stTextInput input {
#             padding: 10px 12px !important;
#         }
        
#         .header-card {
#             background: linear-gradient(135deg, var(--secondary-color) 0%, var(--primary-dark) 100%);
#             color: white;
#             border-radius: var(--border-radius);
#             padding: 2.5rem 2rem;
#             margin-bottom: 2rem;
#             box-shadow: var(--card-shadow);
#             border: none;
#         }
        
#         .metric-card {
#             background: white;
#             border-radius: var(--border-radius);
#             padding: 1.5rem;
#             box-shadow: var(--card-shadow);
#             transition: var(--transition);
#             border-left: 4px solid var(--primary-color);
#             height: 100%;
#             display: flex;
#             flex-direction: column;
#         }
        
#         .metric-card:hover {
#             transform: translateY(-5px);
#             box-shadow: 0 10px 20px rgba(0,0,0,0.15);
#         }
        
#         .metric-title {
#             font-size: 0.95rem;
#             color: #7f8c8d;
#             margin-bottom: 0.5rem;
#             font-weight: 500;
#         }
        
#         .metric-value {
#             font-size: 2rem;
#             font-weight: 700;
#             color: var(--secondary-color);
#             line-height: 1.2;
#         }
        
#         .metric-description {
#             font-size: 0.85rem;
#             color: #95a5a6;
#             margin-top: auto;
#             padding-top: 0.5rem;
#         }
        
#         .data-card {
#             background: white;
#             border-radius: var(--border-radius);
#             padding: 1.5rem;
#             margin-bottom: 1.5rem;
#             box-shadow: var(--card-shadow);
#             border-left: 4px solid var(--primary-color);
#             height: 280px;
#             overflow-y: auto;
#             transition: var(--transition);
#         }
        
#         .data-card:hover {
#             box-shadow: 0 8px 16px rgba(0,0,0,0.1);
#         }
        
#         .data-card h4 {
#             color: var(--secondary-color);
#             font-size: 1.2rem;
#             margin-bottom: 1rem;
#             border-bottom: 1px solid #eee;
#             padding-bottom: 0.5rem;
#             font-weight: 600;
#         }
        
#         .data-card p {
#             margin-bottom: 0.8rem;
#             font-size: 0.95rem;
#             line-height: 1.5;
#         }
        
#         .map-container {
#             border-radius: var(--border-radius);
#             overflow: hidden;
#             box-shadow: 0 8px 24px rgba(0,0,0,0.15);
#             margin-top: 1.5rem;
#             border: 1px solid #e0e0e0;
#         }
        
#         .tab-content {
#             padding: 1.5rem 0;
#         }
        
#         .stTabs [data-baseweb="tab-list"] {
#             gap: 8px;
#             padding: 0 4px;
#         }
        
#         .stTabs [data-baseweb="tab"] {
#             background: white;
#             border-radius: 8px 8px 0 0 !important;
#             padding: 10px 20px;
#             transition: var(--transition);
#             border: 1px solid #e0e0e0;
#             margin-right: 0 !important;
#             font-weight: 500;
#         }
        
#         .stTabs [aria-selected="true"] {
#             background-color: var(--primary-color) !important;
#             color: white !important;
#             border-color: var(--primary-dark) !important;
#         }
        
#         .stTabs [aria-selected="false"]:hover {
#             background-color: #f8f9fa !important;
#         }
        
#         @font-face {
#             font-family: 'Khmer OS';
#             src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts@master/phaseIII_only/unhinted/NotoSansKhmer/NotoSansKhmer-Regular.ttf') format('truetype');
#         }
        
#         body {
#             font-family: 'Khmer OS', 'Arial', sans-serif;
#         }
        
#         /* Section headers */
#         .section-header {
#             color: var(--secondary-color);
#             border-bottom: 2px solid var(--primary-color);
#             padding-bottom: 0.5rem;
#             margin-bottom: 1.5rem;
#             font-weight: 600;
#         }
        
#         .section-subheader {
#             color: #7f8c8d;
#             font-size: 1rem;
#             margin-top: -1.25rem;
#             margin-bottom: 1.5rem;
#         }
        
#         /* Custom scrollbar */
#         ::-webkit-scrollbar {
#             width: 8px;
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
#             font-family: 'Khmer OS', Arial !important;
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
#                 padding: 1.5rem 1rem;
#             }
#         }
        
#         /* Loading spinner color */
#         .stSpinner > div > div {
#             border-color: var(--primary-color) transparent transparent transparent !important;
#         }
#     </style>
#     """, unsafe_allow_html=True)

#     # Header with gradient background and improved typography
#     st.markdown("""
#     <div class="header-card">
#         <div style="text-align: center;">
#             <h1 style="color: white; font-size: 2.5rem; margin-bottom: 0.5rem; font-weight: 700;">ភូមិសាស្ត្រកម្ពុជា</h1>
#             <p style="color: rgba(255,255,255,0.9); font-size: 1.1rem; margin-bottom: 0.5rem;">
#                 ប្រព័ន្ធព័ត៌មានភូមិសាស្ត្រនៃព្រះរាជាណាចក្រកម្ពុជា
#             </p>
#             <div style="background: rgba(255,255,255,0.15); border-radius: 20px; padding: 0.25rem 1rem; display: inline-block;">
#                 <p style="color: rgba(255,255,255,0.9); font-size: 0.9rem; margin: 0;">
#                     បច្ចុប្បន្នភាព: {current_date}
#                 </p>
#             </div>
#         </div>
#     </div>
#     """.format(current_date=datetime.now().strftime("%d %B %Y")), unsafe_allow_html=True)

#     # Create tabs for different views with better spacing
#     tab1, tab2 = st.tabs(["🗺 ផែនទីខេត្ត & ស្ថិតិ", "📋 ទិន្នន័យលម្អិត"])

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
#         st.markdown("""
#         <div style="margin-bottom: 1.5rem;">
#             <h2 class="section-header">ព័ត៌មានទូទៅ</h2>
#             <p class="section-subheader">ទិន្នន័យសង្ខេបនៃភូមិសាស្ត្រកម្ពុជា</p>
#         </div>
#         """, unsafe_allow_html=True)
        
#         # Filter controls in a clean layout with better spacing
#         with st.container():
#             col1, col2, col3 = st.columns([2, 1, 1])
            
#             with col1:
#                 text_search = st.text_input(
#                     "ស្វែងរកពាក្យ",
#                     value="",
#                     placeholder="វាយបញ្ចូលឈ្មោះខេត្ត ឬពាក្យគន្លឹះ...",
#                     help="ស្វែងរកតាមឈ្មោះខេត្ត ឬពាក្យពីការពិពណ៌នា",
#                     key="tab1_search"
#                 )
            
#             with col2:
#                 year_options = ("2000", "2023", "2024", "2025")
#                 selected_year = st.selectbox(
#                     "ឆ្នាំ",
#                     year_options,
#                     index=year_options.index("2025"),
#                     help="ជ្រើសរើសឆ្នាំដើម្បីមើលទិន្នន័យ",
#                     key="tab1_year"
#                 )
#                 selected_year = int(selected_year)
            
#             with col3:
#                 status_options = ("Active", "Inactive")
#                 selected_status = st.selectbox(
#                     "ស្ថានភាព",
#                     status_options,
#                     index=0,
#                     help="ជ្រើសរើសស្ថានភាពនៃទិន្នន័យ",
#                     key="tab1_status"
#                 )
        
#         # Filter data based on selections
#         filtered_df = df[(df['Start_Year'] <= selected_year) & (df['End_Year'] >= selected_year)]
#         filtered_df = filtered_df[filtered_df['EFF_STATUS'] == selected_status]
        
#         if text_search:
#             mask1 = filtered_df["DESCRLONG_KHM"].str.contains(text_search, case=False, na=False)
#             mask2 = filtered_df["PRODUCT"].str.contains(text_search, case=False, na=False)
#             filtered_df = filtered_df[mask1 | mask2]

#         # Key Metrics Section with improved cards
#         if not filtered_df.empty:
#             st.markdown("""
#             <div style="margin: 2rem 0 1.5rem 0;">
#                 <h3 class="section-header">ស្ថិតិសំខាន់ៗ</h3>
#                 <p class="section-subheader">សូចនាករសំខាន់ៗនៃទិន្នន័យភូមិសាស្ត្រ</p>
#             </div>
#             """, unsafe_allow_html=True)
            
#             col1, col2, col3, col4 = st.columns(4)
            
#             with col1:
#                 st.markdown(f"""
#                 <div class="metric-card">
#                     <div class="metric-title">ចំនួនសរុប</div>
#                     <div class="metric-value">{len(filtered_df):,}</div>
#                     <div class="metric-description">ធាតុទិន្នន័យសរុប</div>
#                 </div>
#                 """, unsafe_allow_html=True)
            
#             with col2:
#                 st.markdown(f"""
#                 <div class="metric-card">
#                     <div class="metric-title">ចំនួនខេត្ត</div>
#                     <div class="metric-value" style="color: var(--accent-color);">
#                         {filtered_df['Province_English'].nunique():,}
#                     </div>
#                     <div class="metric-description">ខេត្តដែលមានទិន្នន័យ</div>
#                 </div>
#                 """, unsafe_allow_html=True)
            
#             with col3:
#                 st.markdown(f"""
#                 <div class="metric-card">
#                     <div class="metric-title">ឆ្នាំដែលបានជ្រើសរើស</div>
#                     <div class="metric-value" style="color: var(--success-color);">
#                         {selected_year}
#                     </div>
#                     <div class="metric-description">ឆ្នាំដែលបានជ្រើសរើស</div>
#                 </div>
#                 """, unsafe_allow_html=True)
            
#             with col4:
#                 active_count = len(filtered_df[filtered_df['EFF_STATUS'] == 'Active'])
#                 st.markdown(f"""
#                 <div class="metric-card">
#                     <div class="metric-title">ស្ថានភាពសកម្ម</div>
#                     <div class="metric-value" style="color: #9b59b6;">
#                         {active_count:,}
#                     </div>
#                     <div class="metric-description">ធាតុទិន្នន័យសកម្ម</div>
#                 </div>
#                 """, unsafe_allow_html=True)
            
#             # Province Distribution Chart with improved layout
#             st.markdown("---")
#             st.markdown("""
#             <div style="margin-bottom: 1.5rem;">
#                 <h3 class="section-header">ការចែកចាយទិន្នន័យតាមខេត្ត</h3>
#                 <p class="section-subheader">ខេត្តដែលមានទិន្នន័យច្រើនបំផុត</p>
#             </div>
#             """, unsafe_allow_html=True)
            
#             top_provinces = filtered_df['Province_English'].value_counts().head(10).reset_index()
#             top_provinces.columns = ['Province', 'Count']
            
#             # Use columns to make the chart responsive
#             col1, col2 = st.columns([3, 1])
            
#             with col1:
#                 st.bar_chart(
#                     top_provinces.set_index('Province'),
#                     height=400,
#                     use_container_width=True,
#                     color='#3498db'
#                 )
            
#             with col2:
#                 st.markdown("""
#                 <div style="background: white; border-radius: var(--border-radius); padding: 1.25rem; box-shadow: var(--card-shadow); height: 100%;">
#                     <h4 style="color: var(--secondary-color); margin-top: 0; font-weight: 600;">ខេត្តកំពូល</h4>
#                     <ol style="padding-left: 1.2rem; margin-top: 1rem;">
#                 """, unsafe_allow_html=True)
                
#                 for i, row in top_provinces.iterrows():
#                     st.markdown(f"""
#                     <li style="margin-bottom: 0.75rem; padding-bottom: 0.5rem; border-bottom: 1px dashed #eee;">
#                         <span style="font-weight: 500;">{row['Province']}</span>
#                         <span style="float: right; color: var(--accent-color); font-weight: 600;">{row['Count']:,}</span>
#                     </li>
#                     """, unsafe_allow_html=True)
                
#                 st.markdown("</ol></div>", unsafe_allow_html=True)
            
#             # Interactive Map Visualization with improved styling
#             st.markdown("---")
#             st.markdown("""
#             <div style="margin-bottom: 1.5rem;">
#                 <h2 class="section-header">ផែនទីខេត្តនៃព្រះរាជាណាចក្រកម្ពុជា</h2>
#                 <p class="section-subheader">ចុចលើចំណុចនីមួយៗដើម្បីមើលព័ត៌មានលម្អិត</p>
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
                
#                 # Create map layers with improved styling
#                 layer = pdk.Layer(
#                     "ScatterplotLayer",
#                     province_df,
#                     pickable=True,
#                     opacity=0.9,
#                     stroked=True,
#                     filled=True,
#                     radius_scale=1,
#                     radius_min_pixels=10,
#                     radius_max_pixels=120,
#                     line_width_min_pixels=1,
#                     get_position=["Longitude", "Latitude"],
#                     get_radius="size",
#                     get_fill_color=[52, 152, 219, 220],  # More opaque blue
#                     get_line_color=[0, 0, 0, 200],
#                 )

#                 text_layer = pdk.Layer(
#                     "TextLayer",
#                     province_df,
#                     pickable=False,
#                     get_position=["Longitude", "Latitude"],
#                     get_text="Province_Khmer",
#                     get_size=16,
#                     get_color=[0, 0, 0, 220],
#                     get_angle=0,
#                     get_text_anchor="'middle'",
#                     get_alignment_baseline="'center'",
#                 )

#                 view_state = pdk.ViewState(
#                     latitude=12.5657,
#                     longitude=104.9910,
#                     zoom=6.2,
#                     pitch=0,
#                 )

#                 # Render the map in a container with improved tooltip
#                 with st.container():
#                     st.pydeck_chart(
#                         pdk.Deck(
#                             layers=[layer, text_layer],
#                             initial_view_state=view_state,
#                             tooltip={
#                                 "html": """
#                                 <div class="map-tooltip" style="padding: 12px; font-family: 'Khmer OS', Arial; background: white; border-radius: 8px; max-width: 300px;">
#                                     <h3 style="margin: 0 0 8px 0; color: #2c3e50; border-bottom: 1px solid #eee; padding-bottom: 8px; font-size: 1.1rem;">{Province_Khmer}</h3>
#                                     <p style="margin: 6px 0; font-size: 0.9rem;"><b>ចំនួនទិន្នន័យ:</b> <span style="color: var(--accent-color); font-weight: 600;">{count}</span></p>
#                                     <p style="margin: 6px 0; font-size: 0.9rem;"><b>ស្ថានភាព:</b> <span style="color: {color}; font-weight: 500;">{EFF_STATUS}</span></p>
#                                     <p style="margin: 6px 0 0 0; font-size: 0.85rem; color: #7f8c8d;">ចុចដើម្បីមើលព័ត៌មានលម្អិត</p>
#                                 </div>
#                                 """.replace("{color}", "'#27ae60'" if selected_status == "Active" else "'#e74c3c'"),
#                                 "style": {
#                                     "fontFamily": "'Khmer OS', Arial",
#                                     "boxShadow": "0 4px 12px rgba(0,0,0,0.15)"
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

#     # Tab 2: Detailed Data with improved layout
#     with tab2:
#         st.markdown("""
#         <div style="margin-bottom: 2rem;">
#             <h2 class="section-header">ទិន្នន័យលម្អិត</h2>
#             <p class="section-subheader">ព័ត៌មានលម្អិតអំពីភូមិសាស្ត្រកម្ពុជា</p>
#         </div>
#         """, unsafe_allow_html=True)
        
#         # Filter controls with consistent styling
#         with st.container():
#             col1, col2, col3 = st.columns([2, 1, 1])
            
#             with col1:
#                 tab2_text_search = st.text_input(
#                     "ស្វែងរកពាក្យ (ទិន្នន័យលម្អិត)",
#                     value=text_search if 'text_search' in locals() else "",
#                     placeholder="ស្វែងរកពាក្យគន្លឹះ...",
#                     key="tab2_search"
#                 )
            
#             with col2:
#                 year_options = ("2000", "2023", "2024", "2025")
#                 # Set default index safely
#                 default_index = 3  # Default to "2025" (index 3)
#                 if 'selected_year' in locals():
#                     try:
#                         default_index = year_options.index(str(selected_year))
#                     except ValueError:
#                         pass  # Use default if not found
                
#                 tab2_selected_year = st.selectbox(
#                     "ឆ្នាំ (ទិន្នន័យលម្អិត)",
#                     year_options,
#                     index=default_index,
#                     key="tab2_year"
#                 )
#                 tab2_selected_year = int(tab2_selected_year)
            
#             with col3:
#                 status_options = ("Active", "Inactive")
#                 tab2_selected_status = st.selectbox(
#                     "ស្ថានភាព (ទិន្នន័យលម្អិត)",
#                     status_options,
#                     index=status_options.index(selected_status) if 'selected_status' in locals() else 0,
#                     key="tab2_status"
#                 )
        
#         # Filter data based on selections
#         tab2_filtered_df = df[(df['Start_Year'] <= tab2_selected_year) & (df['End_Year'] >= tab2_selected_year)]
#         tab2_filtered_df = tab2_filtered_df[tab2_filtered_df['EFF_STATUS'] == tab2_selected_status]
        
#         if tab2_text_search:
#             mask1 = tab2_filtered_df["DESCRLONG_KHM"].str.contains(tab2_text_search, case=False, na=False)
#             mask2 = tab2_filtered_df["PRODUCT"].str.contains(tab2_text_search, case=False, na=False)
#             tab2_filtered_df = tab2_filtered_df[mask1 | mask2]

#         # Data display with improved cards
#         if not tab2_filtered_df.empty:
#             st.markdown(f"""
#             <div style="background: white; border-radius: var(--border-radius); padding: 1rem 1.5rem; margin-bottom: 1.5rem; box-shadow: var(--card-shadow);">
#                 <div style="display: flex; justify-content: space-between; align-items: center;">
#                     <p style="margin: 0; color: var(--secondary-color); font-weight: 500;">
#                         បានរកឃើញ: <strong style="color: var(--primary-color);">{len(tab2_filtered_df):,}</strong> ធាតុទិន្នន័យ
#                     </p>
#                     <p style="margin: 0; color: #7f8c8d; font-size: 0.9rem;">
#                         កាលបរិច្ឆេទ: {datetime.now().strftime("%d %B %Y")}
#                     </p>
#                 </div>
#             </div>
#             """, unsafe_allow_html=True)
            
#             # Display filtered results in a responsive grid with improved cards
#             cols = st.columns(3)
            
#             for idx, row in tab2_filtered_df.iterrows():
#                 with cols[idx % 3]:
#                     province = str(row['នៅក្រោមខេត្ត']).strip() if pd.notna(row['នៅក្រោមខេត្ត']) else None
#                     province_text = (
#                         f"""<p style="margin: 0.5rem 0; font-size: 0.9rem;">
#                             <span style="color: #7f8c8d;">🏛 ខេត្ត:</span> 
#                             <span style="color: var(--success-color); font-weight: 500;">{province}</span>
#                         </p>"""
#                         if province else ""
#                     )

#                     status_color = "#27ae60" if row['EFF_STATUS'] == 'Active' else "#e74c3c"
#                     status_icon = "🟢" if row['EFF_STATUS'] == 'Active' else "🔴"
                    
#                     st.markdown(f"""
#                     <div class="data-card">
#                         <h4>{row['PRODUCT']}</h4>
#                         <p style="margin: 0.5rem 0;">
#                             <span style="color: #7f8c8d;">📅 ឆ្នាំ:</span> 
#                             <span style="color: var(--primary-color); font-weight: 500;">{row['EFFDT_Year']}-2025</span>
#                         </p>
#                         <p style="margin: 0.5rem 0;">
#                             <span style="color: #7f8c8d;">{status_icon} ស្ថានភាព:</span> 
#                             <span style="color: {status_color}; font-weight: 500;">
#                                 {row['EFF_STATUS']}
#                             </span>
#                         </p>
#                         <p style="margin: 0.5rem 0;">
#                             <span style="color: #7f8c8d;">📖 ពណ៌នា:</span> 
#                             <span style="color: var(--secondary-color);">
#                                 {row['DESCRLONG_KHM'][:100]}{'...' if len(row['DESCRLONG_KHM']) > 100 else ''}
#                             </span>
#                         </p>
#                         {province_text}
#                         <div style="margin-top: 0.5rem; text-align: right;">
#                             <span style="font-size: 0.8rem; color: #7f8c8d; font-style: italic;">ធាតុទិន្នន័យ #{idx + 1}</span>
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

# def Geography():
#     # Custom CSS for professional styling with improved visual hierarchy
#     st.markdown("""
#     <style>
#         :root {
#             --primary-color: #3498db;
#             --primary-dark: #2980b9;
#             --secondary-color: #2c3e50;
#             --accent-color: #e74c3c;
#             --success-color: #27ae60;
#             --light-bg: #f8f9fa;
#             --card-shadow: 0 4px 6px rgba(0,0,0,0.1);
#             --transition: all 0.3s ease;
#             --border-radius: 12px;
#         }
        
#         .main {
#             background-color: var(--light-bg);
#             font-family: 'Khmer OS', 'Arial', sans-serif;
#         }
        
#         .stSelectbox, .stTextInput, .stSlider {
#             background-color: white;
#             border-radius: var(--border-radius);
#             box-shadow: var(--card-shadow);
#             border: 1px solid #e0e0e0;
#         }
        
#         .stTextInput input {
#             padding: 10px 12px !important;
#         }
        
#         .header-card {
#             background: linear-gradient(135deg, var(--secondary-color) 0%, var(--primary-dark) 100%);
#             color: white;
#             border-radius: var(--border-radius);
#             padding: 2.5rem 2rem;
#             margin-bottom: 2rem;
#             box-shadow: var(--card-shadow);
#             border: none;
#         }
        
#         .metric-card {
#             background: white;
#             border-radius: var(--border-radius);
#             padding: 1.5rem;
#             box-shadow: var(--card-shadow);
#             transition: var(--transition);
#             border-left: 4px solid var(--primary-color);
#             height: 100%;
#             display: flex;
#             flex-direction: column;
#         }
        
#         .metric-card:hover {
#             transform: translateY(-5px);
#             box-shadow: 0 10px 20px rgba(0,0,0,0.15);
#         }
        
#         .metric-title {
#             font-size: 0.95rem;
#             color: #7f8c8d;
#             margin-bottom: 0.5rem;
#             font-weight: 500;
#         }
        
#         .metric-value {
#             font-size: 2rem;
#             font-weight: 700;
#             color: var(--secondary-color);
#             line-height: 1.2;
#         }
        
#         .metric-description {
#             font-size: 0.85rem;
#             color: #95a5a6;
#             margin-top: auto;
#             padding-top: 0.5rem;
#         }
        
#         .data-card {
#             background: white;
#             border-radius: var(--border-radius);
#             padding: 1.5rem;
#             margin-bottom: 1.5rem;
#             box-shadow: var(--card-shadow);
#             border-left: 4px solid var(--primary-color);
#             height: 280px;
#             overflow-y: auto;
#             transition: var(--transition);
#         }
        
#         .data-card:hover {
#             box-shadow: 0 8px 16px rgba(0,0,0,0.1);
#         }
        
#         .data-card h4 {
#             color: var(--secondary-color);
#             font-size: 1.2rem;
#             margin-bottom: 1rem;
#             border-bottom: 1px solid #eee;
#             padding-bottom: 0.5rem;
#             font-weight: 600;
#         }
        
#         .data-card p {
#             margin-bottom: 0.8rem;
#             font-size: 0.95rem;
#             line-height: 1.5;
#         }
        
#         .map-container {
#             border-radius: var(--border-radius);
#             overflow: hidden;
#             box-shadow: 0 8px 24px rgba(0,0,0,0.15);
#             margin-top: 1.5rem;
#             border: 1px solid #e0e0e0;
#         }
        
#         .tab-content {
#             padding: 1.5rem 0;
#         }
        
#         .stTabs [data-baseweb="tab-list"] {
#             gap: 8px;
#             padding: 0 4px;
#         }
        
#         .stTabs [data-baseweb="tab"] {
#             background: white;
#             border-radius: 8px 8px 0 0 !important;
#             padding: 10px 20px;
#             transition: var(--transition);
#             border: 1px solid #e0e0e0;
#             margin-right: 0 !important;
#             font-weight: 500;
#         }
        
#         .stTabs [aria-selected="true"] {
#             background-color: var(--primary-color) !important;
#             color: white !important;
#             border-color: var(--primary-dark) !important;
#         }
        
#         .stTabs [aria-selected="false"]:hover {
#             background-color: #f8f9fa !important;
#         }
        
#         @font-face {
#             font-family: 'Khmer OS';
#             src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts@master/phaseIII_only/unhinted/NotoSansKhmer/NotoSansKhmer-Regular.ttf') format('truetype');
#         }
        
#         body {
#             font-family: 'Khmer OS', 'Arial', sans-serif;
#         }
        
#         /* Section headers */
#         .section-header {
#             color: var(--secondary-color);
#             border-bottom: 2px solid var(--primary-color);
#             padding-bottom: 0.5rem;
#             margin-bottom: 1.5rem;
#             font-weight: 600;
#         }
        
#         .section-subheader {
#             color: #7f8c8d;
#             font-size: 1rem;
#             margin-top: -1.25rem;
#             margin-bottom: 1.5rem;
#         }
        
#         /* Custom scrollbar */
#         ::-webkit-scrollbar {
#             width: 8px;
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
#             font-family: 'Khmer OS', Arial !important;
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
#                 padding: 1.5rem 1rem;
#             }
#         }
        
#         /* Loading spinner color */
#         .stSpinner > div > div {
#             border-color: var(--primary-color) transparent transparent transparent !important;
#         }
#     </style>
#     """, unsafe_allow_html=True)

#     # Header with gradient background and improved typography
#     st.markdown("""
#     <div class="header-card">
#         <div style="text-align: center;">
#             <h1 style="color: white; font-size: 2.5rem; margin-bottom: 0.5rem; font-weight: 700;">ភូមិសាស្ត្រកម្ពុជា</h1>
#             <p style="color: rgba(255,255,255,0.9); font-size: 1.1rem; margin-bottom: 0.5rem;">
#                 ប្រព័ន្ធព័ត៌មានភូមិសាស្ត្រនៃព្រះរាជាណាចក្រកម្ពុជា
#             </p>
#             <div style="background: rgba(255,255,255,0.15); border-radius: 20px; padding: 0.25rem 1rem; display: inline-block;">
#                 <p style="color: rgba(255,255,255,0.9); font-size: 0.9rem; margin: 0;">
#                     បច្ចុប្បន្នភាព: {current_date}
#                 </p>
#             </div>
#         </div>
#     </div>
#     """.format(current_date=datetime.now().strftime("%d %B %Y")), unsafe_allow_html=True)

#     # Create tabs for different views with better spacing
#     tab1, tab2 = st.tabs(["🗺 ផែនទីខេត្ត & ស្ថិតិ", "📋 ទិន្នន័យលម្អិត"])

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
#         # Filter controls in a clean layout with better spacing
#         with st.container():
#             col1, col2, col3 = st.columns([2, 1, 1])
            
#             with col1:
#                 text_search = st.text_input(
#                     "ស្វែងរកពាក្យ",
#                     value="",
#                     placeholder="វាយបញ្ចូលឈ្មោះខេត្ត ឬពាក្យគន្លឹះ...",
#                     help="ស្វែងរកតាមឈ្មោះខេត្ត ឬពាក្យពីការពិពណ៌នា",
#                     key="tab1_search"
#                 )
            
#             with col2:
#                 year_options = ("2000", "2023", "2024", "2025")
#                 selected_year = st.selectbox(
#                     "ឆ្នាំ",
#                     year_options,
#                     index=year_options.index("2025"),
#                     help="ជ្រើសរើសឆ្នាំដើម្បីមើលទិន្នន័យ",
#                     key="tab1_year"
#                 )
#                 selected_year = int(selected_year)
            
#             with col3:
#                 status_options = ("Active", "Inactive")
#                 selected_status = st.selectbox(
#                     "ស្ថានភាព",
#                     status_options,
#                     index=0,
#                     help="ជ្រើសរើសស្ថានភាពនៃទិន្នន័យ",
#                     key="tab1_status"
#                 )
        
#         # Filter data based on selections
#         filtered_df = df[(df['Start_Year'] <= selected_year) & (df['End_Year'] >= selected_year)]
#         filtered_df = filtered_df[filtered_df['EFF_STATUS'] == selected_status]
        
#         if text_search:
#             mask1 = filtered_df["DESCRLONG_KHM"].str.contains(text_search, case=False, na=False)
#             mask2 = filtered_df["PRODUCT"].str.contains(text_search, case=False, na=False)
#             filtered_df = filtered_df[mask1 | mask2]

#         # Key Metrics Section with improved cards
#         if not filtered_df.empty:
#             st.markdown("""
#             <div style="margin: 2rem 0 1.5rem 0;">
#                 <h3 class="section-header">ស្ថិតិសំខាន់ៗ</h3>
#                 <p class="section-subheader">សូចនាករសំខាន់ៗនៃទិន្នន័យភូមិសាស្ត្រ</p>
#             </div>
#             """, unsafe_allow_html=True)
            
#             col1, col2, col3, col4 = st.columns(4)
            
#             with col1:
#                 st.markdown(f"""
#                 <div class="metric-card">
#                     <div class="metric-title">ចំនួនសរុប</div>
#                     <div class="metric-value">{len(filtered_df):,}</div>
#                     <div class="metric-description">ធាតុទិន្នន័យសរុប</div>
#                 </div>
#                 """, unsafe_allow_html=True)
            
#             with col2:
#                 st.markdown(f"""
#                 <div class="metric-card">
#                     <div class="metric-title">ចំនួនខេត្ត</div>
#                     <div class="metric-value" style="color: var(--accent-color);">
#                         {filtered_df['Province_English'].nunique():,}
#                     </div>
#                     <div class="metric-description">ខេត្តដែលមានទិន្នន័យ</div>
#                 </div>
#                 """, unsafe_allow_html=True)
            
#             with col3:
#                 st.markdown(f"""
#                 <div class="metric-card">
#                     <div class="metric-title">ឆ្នាំដែលបានជ្រើសរើស</div>
#                     <div class="metric-value" style="color: var(--success-color);">
#                         {selected_year}
#                     </div>
#                     <div class="metric-description">ឆ្នាំដែលបានជ្រើសរើស</div>
#                 </div>
#                 """, unsafe_allow_html=True)
            
#             with col4:
#                 active_count = len(filtered_df[filtered_df['EFF_STATUS'] == 'Active'])
#                 st.markdown(f"""
#                 <div class="metric-card">
#                     <div class="metric-title">ស្ថានភាពសកម្ម</div>
#                     <div class="metric-value" style="color: #9b59b6;">
#                         {active_count:,}
#                     </div>
#                     <div class="metric-description">ធាតុទិន្នន័យសកម្ម</div>
#                 </div>
#                 """, unsafe_allow_html=True)
            
#             # Province Distribution Chart with improved layout
#             st.markdown("---")
#             st.markdown("""
#             <div style="margin-bottom: 1.5rem;">
#                 <h3 class="section-header">ការចែកចាយទិន្នន័យតាមខេត្ត</h3>
#                 <p class="section-subheader">ខេត្តដែលមានទិន្នន័យច្រើនបំផុត</p>
#             </div>
#             """, unsafe_allow_html=True)
            
#             top_provinces = filtered_df['Province_English'].value_counts().head(10).reset_index()
#             top_provinces.columns = ['Province', 'Count']
            
#             # Use columns to make the chart responsive
#             col1, col2 = st.columns([3, 1])
            
#             with col1:
#                 st.bar_chart(
#                     top_provinces.set_index('Province'),
#                     height=400,
#                     use_container_width=True,
#                     color='#3498db'
#                 )
            
#             with col2:
#                 st.markdown("""
#                 <div style="background: white; border-radius: var(--border-radius); padding: 1.25rem; box-shadow: var(--card-shadow); height: 100%;">
#                     <h4 style="color: var(--secondary-color); margin-top: 0; font-weight: 600;">ខេត្តកំពូល</h4>
#                     <ol style="padding-left: 1.2rem; margin-top: 1rem;">
#                 """, unsafe_allow_html=True)
                
#                 for i, row in top_provinces.iterrows():
#                     st.markdown(f"""
#                     <li style="margin-bottom: 0.75rem; padding-bottom: 0.5rem; border-bottom: 1px dashed #eee;">
#                         <span style="font-weight: 500;">{row['Province']}</span>
#                         <span style="float: right; color: var(--accent-color); font-weight: 600;">{row['Count']:,}</span>
#                     </li>
#                     """, unsafe_allow_html=True)
                
#                 st.markdown("</ol></div>", unsafe_allow_html=True)
            
#             # Interactive Map Visualization with improved styling
#             st.markdown("---")
#             st.markdown("""
#             <div style="margin-bottom: 1.5rem;">
#                 <h2 class="section-header">ផែនទីខេត្តនៃព្រះរាជាណាចក្រកម្ពុជា</h2>
#                 <p class="section-subheader">ចុចលើចំណុចនីមួយៗដើម្បីមើលព័ត៌មានលម្អិត</p>
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
                
#                 # Create map layers with improved styling
#                 layer = pdk.Layer(
#                     "ScatterplotLayer",
#                     province_df,
#                     pickable=True,
#                     opacity=0.9,
#                     stroked=True,
#                     filled=True,
#                     radius_scale=1,
#                     radius_min_pixels=10,
#                     radius_max_pixels=120,
#                     line_width_min_pixels=1,
#                     get_position=["Longitude", "Latitude"],
#                     get_radius="size",
#                     get_fill_color=[52, 152, 219, 220],  # More opaque blue
#                     get_line_color=[0, 0, 0, 200],
#                 )

#                 text_layer = pdk.Layer(
#                     "TextLayer",
#                     province_df,
#                     pickable=False,
#                     get_position=["Longitude", "Latitude"],
#                     get_text="Province_Khmer",
#                     get_size=16,
#                     get_color=[0, 0, 0, 220],
#                     get_angle=0,
#                     get_text_anchor="'middle'",
#                     get_alignment_baseline="'center'",
#                 )

#                 view_state = pdk.ViewState(
#                     latitude=12.5657,
#                     longitude=104.9910,
#                     zoom=6.2,
#                     pitch=0,
#                 )

#                 # Render the map in a container with improved tooltip
#                 with st.container():
#                     st.pydeck_chart(
#                         pdk.Deck(
#                             layers=[layer, text_layer],
#                             initial_view_state=view_state,
#                             tooltip={
#                                 "html": """
#                                 <div class="map-tooltip" style="padding: 12px; font-family: 'Khmer OS', Arial; background: white; border-radius: 8px; max-width: 300px;">
#                                     <h3 style="margin: 0 0 8px 0; color: #2c3e50; border-bottom: 1px solid #eee; padding-bottom: 8px; font-size: 1.1rem;">{Province_Khmer}</h3>
#                                     <p style="margin: 6px 0; font-size: 0.9rem;"><b>ចំនួនទិន្នន័យ:</b> <span style="color: var(--accent-color); font-weight: 600;">{count}</span></p>
#                                     <p style="margin: 6px 0; font-size: 0.9rem;"><b>ស្ថានភាព:</b> <span style="color: {color}; font-weight: 500;">{EFF_STATUS}</span></p>
#                                     <p style="margin: 6px 0 0 0; font-size: 0.85rem; color: #7f8c8d;">ចុចដើម្បីមើលព័ត៌មានលម្អិត</p>
#                                 </div>
#                                 """.replace("{color}", "'#27ae60'" if selected_status == "Active" else "'#e74c3c'"),
#                                 "style": {
#                                     "fontFamily": "'Khmer OS', Arial",
#                                     "boxShadow": "0 4px 12px rgba(0,0,0,0.15)"
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

#     # Tab 2: Detailed Data with improved layout
#     with tab2:
#         st.markdown("""
#         <div style="margin-bottom: 2rem;">
#             <h2 class="section-header">ទិន្នន័យលម្អិត</h2>
#             <p class="section-subheader">ព័ត៌មានលម្អិតអំពីភូមិសាស្ត្រកម្ពុជា</p>
#         </div>
#         """, unsafe_allow_html=True)
        
#         # Filter controls with consistent styling
#         with st.container():
#             col1, col2, col3 = st.columns([2, 1, 1])
            
#             with col1:
#                 tab2_text_search = st.text_input(
#                     "ស្វែងរកពាក្យ (ទិន្នន័យលម្អិត)",
#                     value=text_search if 'text_search' in locals() else "",
#                     placeholder="ស្វែងរកពាក្យគន្លឹះ...",
#                     key="tab2_search"
#                 )
            
#             with col2:
#                 year_options = ("2000", "2023", "2024", "2025")
#                 # Set default index safely
#                 default_index = 3  # Default to "2025" (index 3)
#                 if 'selected_year' in locals():
#                     try:
#                         default_index = year_options.index(str(selected_year))
#                     except ValueError:
#                         pass  # Use default if not found
                
#                 tab2_selected_year = st.selectbox(
#                     "ឆ្នាំ (ទិន្នន័យលម្អិត)",
#                     year_options,
#                     index=default_index,
#                     key="tab2_year"
#                 )
#                 tab2_selected_year = int(tab2_selected_year)
            
#             with col3:
#                 status_options = ("Active", "Inactive")
#                 tab2_selected_status = st.selectbox(
#                     "ស្ថានភាព (ទិន្នន័យលម្អិត)",
#                     status_options,
#                     index=status_options.index(selected_status) if 'selected_status' in locals() else 0,
#                     key="tab2_status"
#                 )
        
#         # Filter data based on selections
#         tab2_filtered_df = df[(df['Start_Year'] <= tab2_selected_year) & (df['End_Year'] >= tab2_selected_year)]
#         tab2_filtered_df = tab2_filtered_df[tab2_filtered_df['EFF_STATUS'] == tab2_selected_status]
        
#         if tab2_text_search:
#             mask1 = tab2_filtered_df["DESCRLONG_KHM"].str.contains(tab2_text_search, case=False, na=False)
#             mask2 = tab2_filtered_df["PRODUCT"].str.contains(tab2_text_search, case=False, na=False)
#             tab2_filtered_df = tab2_filtered_df[mask1 | mask2]

#         # Data display with improved cards
#         if not tab2_filtered_df.empty:
#             st.markdown(f"""
#             <div style="background: white; border-radius: var(--border-radius); padding: 1rem 1.5rem; margin-bottom: 1.5rem; box-shadow: var(--card-shadow);">
#                 <div style="display: flex; justify-content: space-between; align-items: center;">
#                     <p style="margin: 0; color: var(--secondary-color); font-weight: 500;">
#                         បានរកឃើញ: <strong style="color: var(--primary-color);">{len(tab2_filtered_df):,}</strong> ធាតុទិន្នន័យ
#                     </p>
#                     <p style="margin: 0; color: #7f8c8d; font-size: 0.9rem;">
#                         កាលបរិច្ឆេទ: {datetime.now().strftime("%d %B %Y")}
#                     </p>
#                 </div>
#             </div>
#             """, unsafe_allow_html=True)
            
#             # Display filtered results in a responsive grid with improved cards
#             cols = st.columns(3)
            
#             for idx, row in tab2_filtered_df.iterrows():
#                 with cols[idx % 3]:
#                     province = str(row['នៅក្រោមខេត្ត']).strip() if pd.notna(row['នៅក្រោមខេត្ត']) else None
#                     province_text = (
#                         f"""<p style="margin: 0.5rem 0; font-size: 0.9rem;">
#                             <span style="color: #7f8c8d;">🏛 ខេត្ត:</span> 
#                             <span style="color: var(--success-color); font-weight: 500;">{province}</span>
#                         </p>"""
#                         if province else ""
#                     )

#                     status_color = "#27ae60" if row['EFF_STATUS'] == 'Active' else "#e74c3c"
#                     status_icon = "🟢" if row['EFF_STATUS'] == 'Active' else "🔴"
                    
#                     st.markdown(f"""
#                     <div class="data-card">
#                         <h4>{row['PRODUCT']}</h4>
#                         <p style="margin: 0.5rem 0;">
#                             <span style="color: #7f8c8d;">📅 ឆ្នាំ:</span> 
#                             <span style="color: var(--primary-color); font-weight: 500;">{row['EFFDT_Year']}-2025</span>
#                         </p>
#                         <p style="margin: 0.5rem 0;">
#                             <span style="color: #7f8c8d;">{status_icon} ស្ថានភាព:</span> 
#                             <span style="color: {status_color}; font-weight: 500;">
#                                 {row['EFF_STATUS']}
#                             </span>
#                         </p>
#                         <p style="margin: 0.5rem 0;">
#                             <span style="color: #7f8c8d;">📖 ពណ៌នា:</span> 
#                             <span style="color: var(--secondary-color);">
#                                 {row['DESCRLONG_KHM'][:100]}{'...' if len(row['DESCRLONG_KHM']) > 100 else ''}
#                             </span>
#                         </p>
#                         {province_text}
#                         <div style="margin-top: 0.5rem; text-align: right;">
#                             <span style="font-size: 0.8rem; color: #7f8c8d; font-style: italic;">ធាតុទិន្នន័យ #{idx + 1}</span>
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

# def Geography():
#     # Custom CSS for professional styling with improved visual hierarchy
#     st.markdown("""
#     <style>
#         :root {
#             --primary-color: #3498db;
#             --primary-dark: #2980b9;
#             --secondary-color: #2c3e50;
#             --accent-color: #e74c3c;
#             --success-color: #27ae60;
#             --light-bg: #f8f9fa;
#             --card-shadow: 0 4px 6px rgba(0,0,0,0.1);
#             --transition: all 0.3s ease;
#             --border-radius: 12px;
#         }
        
#         .main {
#             background-color: var(--light-bg);
#             font-family: 'Noto Sans Khmer', Arial, sans-serif !important;
#         }
        
#         .stSelectbox, .stTextInput, .stSlider {
#             background-color: white;
#             border-radius: var(--border-radius);
#             box-shadow: var(--card-shadow);
#             border: 1px solid #e0e0e0;
#         }
        
#         .stTextInput input {
#             padding: 10px 12px !important;
#         }
        
#         .header-card {
#             background: linear-gradient(135deg, var(--secondary-color) 0%, var(--primary-dark) 100%);
#             color: white;
#             border-radius: var(--border-radius);
#             padding: 2.5rem 2rem;
#             margin-bottom: 2rem;
#             box-shadow: var(--card-shadow);
#             border: none;
#         }
        
#         .metric-card {
#             background: white;
#             border-radius: var(--border-radius);
#             padding: 1.5rem;
#             box-shadow: var(--card-shadow);
#             transition: var(--transition);
#             border-left: 4px solid var(--primary-color);
#             height: 100%;
#             display: flex;
#             flex-direction: column;
#         }
        
#         .metric-card:hover {
#             transform: translateY(-5px);
#             box-shadow: 0 10px 20px rgba(0,0,0,0.15);
#         }
        
#         .metric-title {
#             font-size: 0.95rem;
#             color: #7f8c8d;
#             margin-bottom: 0.5rem;
#             font-weight: 500;
#         }
        
#         .metric-value {
#             font-size: 2rem;
#             font-weight: 700;
#             color: var(--secondary-color);
#             line-height: 1.2;
#         }
        
#         .metric-description {
#             font-size: 0.85rem;
#             color: #95a5a6;
#             margin-top: auto;
#             padding-top: 0.5rem;
#         }
        
#         .data-card {
#             background: white;
#             border-radius: var(--border-radius);
#             padding: 1.5rem;
#             margin-bottom: 1.5rem;
#             box-shadow: var(--card-shadow);
#             border-left: 4px solid var(--primary-color);
#             height: 280px;
#             overflow-y: auto;
#             transition: var(--transition);
#         }
        
#         .data-card:hover {
#             box-shadow: 0 8px 16px rgba(0,0,0,0.1);
#         }
        
#         .data-card h4 {
#             color: var(--secondary-color);
#             font-size: 1.2rem;
#             margin-bottom: 1rem;
#             border-bottom: 1px solid #eee;
#             padding-bottom: 0.5rem;
#             font-weight: 600;
#         }
        
#         .data-card p {
#             margin-bottom: 0.8rem;
#             font-size: 0.95rem;
#             line-height: 1.5;
#         }
        
#         .map-container {
#             border-radius: var(--border-radius);
#             overflow: hidden;
#             box-shadow: 0 8px 24px rgba(0,0,0,0.15);
#             margin-top: 1.5rem;
#             border: 1px solid #e0e0e0;
#         }
        
#         .tab-content {
#             padding: 1.5rem 0;
#         }
        
#         .stTabs [data-baseweb="tab-list"] {
#             gap: 8px;
#             padding: 0 4px;
#         }
        
#         .stTabs [data-baseweb="tab"] {
#             background: white;
#             border-radius: 8px 8px 0 0 !important;
#             padding: 10px 20px;
#             transition: var(--transition);
#             border: 1px solid #e0e0e0;
#             margin-right: 0 !important;
#             font-weight: 500;
#         }
        
#         .stTabs [aria-selected="true"] {
#             background-color: var(--primary-color) !important;
#             color: white !important;
#             border-color: var(--primary-dark) !important;
#         }
        
#         .stTabs [aria-selected="false"]:hover {
#             background-color: #f8f9fa !important;
#         }
        
#         @font-face {
#             font-family: 'Noto Sans Khmer',;
#             src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts@master/phaseIII_only/unhinted/NotoSansKhmer/NotoSansKhmer-Regular.ttf') format('truetype');
#         }
        
#         body {
#             font-family: 'Noto Sans Khmer', Arial, sans-serif !important;
#         }
        
#         /* Section headers */
#         .section-header {
#             color: var(--secondary-color);
#             border-bottom: 2px solid var(--primary-color);
#             padding-bottom: 0.5rem;
#             margin-bottom: 1.5rem;
#             font-weight: 600;
#         }
        
#         .section-subheader {
#             color: #7f8c8d;
#             font-size: 1rem;
#             margin-top: -1.25rem;
#             margin-bottom: 1.5rem;
#         }
        
#         /* Custom scrollbar */
#         ::-webkit-scrollbar {
#             width: 8px;
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
#             font-family: 'Noto Sans Khmer', Arial, sans-serif !important;
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
#                 padding: 1.5rem 1rem;
#             }
#         }
        
#         /* Loading spinner color */
#         .stSpinner > div > div {
#             border-color: var(--primary-color) transparent transparent transparent !important;
#         }
#     </style>
#     """, unsafe_allow_html=True)
 
#      # 🔹 Remove Streamlit default top padding
#     st.markdown("""
#         <style>
#             .block-container {
#                 padding-top: 1rem;
#                 padding-bottom: 3rem;
#             }
#         </style>
#     """, unsafe_allow_html=True)

#     # Header with gradient background and improved typography
#     st.markdown("""
#      <div style="margin-bottom: 2rem;">
#        <h1 style="font-family: 'Segoe UI', Tahoma, Geneva, sans-serif;
#                 color: {PRIMARY_COLOR};
#                 font-weight: 700;
#                 font-size: 2.2rem;
#                 margin-bottom: 0.5rem;
#                 display: inline-block;
#                 border-bottom: 3px solid {ACCENT_COLOR};
#                 padding-bottom: 0.5rem;">
#         🏛️ ភូមិសាស្ត្រ
#        </h1>
#         <p style="font-family: 'Segoe UI', Tahoma, Geneva, sans-serif;
#                     color: {LIGHT_TEXT};
#                     font-size: 1rem;">
#             ភូមិសាស្ត្រនៃព្រះរាជាណាចក្រកម្ពុជា
#         </p>
#     </div>
#     """, unsafe_allow_html=True)

#     # Create tabs for different views with better spacing
#     tab1, tab2 = st.tabs(["🗺 ផែនទីខេត្ត & ស្ថិតិ", "📋 ទិន្នន័យលម្អិត"])

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
#         text_search = ""
#         selected_year = 2025
#         selected_status = "Active"
        
#         # Filter data based on default selections
#         filtered_df = df[(df['Start_Year'] <= selected_year) & (df['End_Year'] >= selected_year)]
#         filtered_df = filtered_df[filtered_df['EFF_STATUS'] == selected_status]
        
#         # Key Metrics Section with improved cards
#         if not filtered_df.empty:
#             st.markdown("""
#             <div style="margin: 2rem 0 1.5rem 0;">
#                 <h3 class="section-header">ស្ថិតិសំខាន់ៗ</h3>
#                 <p class="section-subheader">សូចនាករសំខាន់ៗនៃទិន្នន័យភូមិសាស្ត្រ</p>
#             </div>
#             """, unsafe_allow_html=True)
            
#             col1, col2, col3 = st.columns(3)
            
#             with col1:
#                 st.markdown(f"""
#                 <div class="metric-card">
#                     <div class="metric-title">ចំនួនសរុប</div>
#                     <div class="metric-value">{len(filtered_df):,}</div>
#                     <div class="metric-description">ធាតុទិន្នន័យសរុប</div>
#                 </div>
#                 """, unsafe_allow_html=True)
            
#             with col2:
#                 st.markdown(f"""
#                 <div class="metric-card">
#                     <div class="metric-title">ចំនួនខេត្ត</div>
#                     <div class="metric-value" style="color: var(--accent-color);">
#                         {filtered_df['Province_English'].nunique():,}
#                     </div>
#                     <div class="metric-description">ខេត្តដែលមានទិន្នន័យ</div>
#                 </div>
#                 """, unsafe_allow_html=True)
            
#             with col3:
#                 st.markdown(f"""
#                 <div class="metric-card">
#                     <div class="metric-title">ឆ្នាំដែលបានជ្រើសរើស</div>
#                     <div class="metric-value" style="color: var(--success-color);">
#                         {selected_year}
#                     </div>
#                     <div class="metric-description">ឆ្នាំដែលបានជ្រើសរើស</div>
#                 </div>
#                 """, unsafe_allow_html=True)
            
        
            
#             # Province Distribution Chart with improved layout
#             st.markdown("---")
#             st.markdown("""
#             <div style="margin-bottom: 1.5rem;">
#                 <h3 class="section-header">ការចែកចាយទិន្នន័យតាមខេត្ត</h3>
#                 <p class="section-subheader">ខេត្តដែលមានទិន្នន័យច្រើនបំផុត</p>
#             </div>
#             """, unsafe_allow_html=True)
            
#             top_provinces = filtered_df['Province_English'].value_counts().head(10).reset_index()
#             top_provinces.columns = ['Province', 'Count']
            
#             # Use columns to make the chart responsive
#             col1, col2 = st.columns([3, 1])
            
#             with col1:
#                 st.bar_chart(
#                     top_provinces.set_index('Province'),
#                     height=400,
#                     use_container_width=True,
#                     color='#3498db'
#                 )
            
#             with col2:
#                 st.markdown("""
#                 <div style="background: white; border-radius: var(--border-radius); padding: 1.25rem; box-shadow: var(--card-shadow); height: 100%;">
#                     <h4 style="color: var(--secondary-color); margin-top: 0; font-weight: 600;">ខេត្តកំពូល</h4>
#                     <ol style="padding-left: 1.2rem; margin-top: 1rem;">
#                 """, unsafe_allow_html=True)
                
#                 for i, row in top_provinces.iterrows():
#                     st.markdown(f"""
#                     <li style="margin-bottom: 0.75rem; padding-bottom: 0.5rem; border-bottom: 1px dashed #eee;">
#                         <span style="font-weight: 500;">{row['Province']}</span>
#                         <span style="float: right; color: var(--accent-color); font-weight: 600;">{row['Count']:,}</span>
#                     </li>
#                     """, unsafe_allow_html=True)
                
#                 st.markdown("</ol></div>", unsafe_allow_html=True)
            
#             # Interactive Map Visualization with improved styling
#             st.markdown("---")
#             st.markdown("""
#             <div style="margin-bottom: 1.5rem;">
#                 <h2 class="section-header">ផែនទីខេត្តនៃព្រះរាជាណាចក្រកម្ពុជា</h2>
#                 <p class="section-subheader">ចុចលើចំណុចនីមួយៗដើម្បីមើលព័ត៌មានលម្អិត</p>
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
                
#                 # Create map layers with improved styling
#                 layer = pdk.Layer(
#                     "ScatterplotLayer",
#                     province_df,
#                     pickable=True,
#                     opacity=0.9,
#                     stroked=True,
#                     filled=True,
#                     radius_scale=1,
#                     radius_min_pixels=10,
#                     radius_max_pixels=120,
#                     line_width_min_pixels=1,
#                     get_position=["Longitude", "Latitude"],
#                     get_radius="size",
#                     get_fill_color=[52, 152, 219, 220],  # More opaque blue
#                     get_line_color=[0, 0, 0, 200],
#                 )

#                 text_layer = pdk.Layer(
#                     "TextLayer",
#                     province_df,
#                     pickable=False,
#                     get_position=["Longitude", "Latitude"],
#                     get_text="Province_Khmer",
#                     get_size=16,
#                     get_color=[0, 0, 0, 220],
#                     get_angle=0,
#                     get_text_anchor="'middle'",
#                     get_alignment_baseline="'center'",
#                 )

#                 view_state = pdk.ViewState(
#                     latitude=12.5657,
#                     longitude=104.9910,
#                     zoom=6.2,
#                     pitch=0,
#                 )

#                 # Render the map in a container with improved tooltip
#                 with st.container():
#                     st.pydeck_chart(
#                         pdk.Deck(
#                             layers=[layer, text_layer],
#                             initial_view_state=view_state,
#                             tooltip={
#                                 "html": """
#                                 <div class="map-tooltip" style="padding: 12px; font-family: 'Noto Sans Khmer', Arial, sans-serif !important; background: white; border-radius: 8px; max-width: 300px;">
#                                     <h3 style="margin: 0 0 8px 0; color: #2c3e50; border-bottom: 1px solid #eee; padding-bottom: 8px; font-size: 1.1rem;">{Province_Khmer}</h3>
#                                     <p style="margin: 6px 0; font-size: 0.9rem;"><b>ចំនួនទិន្នន័យ:</b> <span style="color: var(--accent-color); font-weight: 600;">{count}</span></p>
#                                     <p style="margin: 6px 0; font-size: 0.9rem;"><b>ស្ថានភាព:</b> <span style="color: {color}; font-weight: 500;">{EFF_STATUS}</span></p>
#                                     <p style="margin: 6px 0 0 0; font-size: 0.85rem; color: #7f8c8d;">ចុចដើម្បីមើលព័ត៌មានលម្អិត</p>
#                                 </div>
#                                 """.replace("{color}", "'#27ae60'" if selected_status == "Active" else "'#e74c3c'"),
#                                 "style": {
#                                     "fontFamily": "'Noto Sans Khmer', Arial, sans-serif !important",
#                                     "boxShadow": "0 4px 12px rgba(0,0,0,0.15)"
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

#     # Tab 2: Detailed Data with improved layout
#     with tab2:
#         st.markdown("""
#         <div style="margin-bottom: 2rem;">
#             <h2 class="section-header">ទិន្នន័យលម្អិត</h2>
#             <p class="section-subheader">ព័ត៌មានលម្អិតអំពីភូមិសាស្ត្រកម្ពុជា</p>
#         </div>
#         """, unsafe_allow_html=True)
        
#         # Filter controls with consistent styling
#         with st.container():
#             col1, col2, col3 = st.columns([2, 1, 1])
            
#             with col1:
#                 tab2_text_search = st.text_input(
#                     "ស្វែងរកពាក្យ (ទិន្នន័យលម្អិត)",
#                     value="",
#                     placeholder="ស្វែងរកពាក្យគន្លឹះ...",
#                     key="tab2_search"
#                 )
            
#             with col2:
#                 year_options = ("2000", "2023", "2024", "2025")
#                 tab2_selected_year = st.selectbox(
#                     "ឆ្នាំ (ទិន្នន័យលម្អិត)",
#                     year_options,
#                     index=3,
#                     key="tab2_year"
#                 )
#                 tab2_selected_year = int(tab2_selected_year)
            
#             with col3:
#                 status_options = ("Active", "Inactive")
#                 tab2_selected_status = st.selectbox(
#                     "ស្ថានភាព (ទិន្នន័យលម្អិត)",
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

#         # Data display with improved cards
#         if not tab2_filtered_df.empty:
#             st.markdown(f"""
#             <div style="background: white; border-radius: var(--border-radius); padding: 1rem 1.5rem; margin-bottom: 1.5rem; box-shadow: var(--card-shadow);">
#                 <div style="display: flex; justify-content: space-between; align-items: center;">
#                     <p style="margin: 0; color: var(--secondary-color); font-weight: 500;">
#                         បានរកឃើញ: <strong style="color: var(--primary-color);">{len(tab2_filtered_df):,}</strong> ធាតុទិន្នន័យ
#                     </p>
#                     <p style="margin: 0; color: #7f8c8d; font-size: 0.9rem;">
#                         កាលបរិច្ឆេទ: {datetime.now().strftime("%d %B %Y")}
#                     </p>
#                 </div>
#             </div>
#             """, unsafe_allow_html=True)
            
#             # Display filtered results in a responsive grid with improved cards
#             cols = st.columns(3)
            
#             for idx, row in tab2_filtered_df.iterrows():
#                 with cols[idx % 3]:
#                     province = str(row['នៅក្រោមខេត្ត']).strip() if pd.notna(row['នៅក្រោមខេត្ត']) else None
#                     province_text = (
#                         f"""<p style="margin: 0.5rem 0; font-size: 0.9rem;">
#                             <span style="color: #7f8c8d;">🏛 ខេត្ត:</span> 
#                             <span style="color: var(--success-color); font-weight: 500;">{province}</span>
#                         </p>"""
#                         if province else ""
#                     )

#                     status_color = "#27ae60" if row['EFF_STATUS'] == 'Active' else "#e74c3c"
#                     status_icon = "🟢" if row['EFF_STATUS'] == 'Active' else "🔴"
                    
#                     st.markdown(f"""
#                     <div class="data-card">
#                         <h4>{row['PRODUCT']}</h4>
#                         <p style="margin: 0.5rem 0;">
#                             <span style="color: #7f8c8d;">📅 ឆ្នាំ:</span> 
#                             <span style="color: var(--primary-color); font-weight: 500;">{row['EFFDT_Year']}-2025</span>
#                         </p>
#                         <p style="margin: 0.5rem 0;">
#                             <span style="color: #7f8c8d;">{status_icon} ស្ថានភាព:</span> 
#                             <span style="color: {status_color}; font-weight: 500;">
#                                 {row['EFF_STATUS']}
#                             </span>
#                         </p>
#                         <p style="margin: 0.5rem 0;">
#                             <span style="color: #7f8c8d;">📖 ពណ៌នា:</span> 
#                             <span style="color: var(--secondary-color);">
#                                 {row['DESCRLONG_KHM'][:100]}{'...' if len(row['DESCRLONG_KHM']) > 100 else ''}
#                             </span>
#                         </p>
#                         {province_text}
#                         <div style="margin-top: 0.5rem; text-align: right;">
#                             <span style="font-size: 0.8rem; color: #7f8c8d; font-style: italic;">ធាតុទិន្នន័យ #{idx + 1}</span>
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

# def Geography():
#     # Custom CSS for professional styling with improved visual hierarchy
#     st.markdown("""
#     <style>
#         :root {
#             --primary-color: #1a365d;
#             --primary-light: #2a4a7f;
#             --secondary-color: #e53e3e;
#             --accent-color: #38a169;
#             --light-bg: #f7fafc;
#             --card-shadow: 0 4px 6px rgba(0,0,0,0.05);
#             --transition: all 0.3s ease;
#             --border-radius: 8px;
#         }
        
#         .main {
#             background-color: var(--light-bg);
#             font-family: 'Noto Sans Khmer', 'Inter', Arial, sans-serif;
#         }
        
#         .stSelectbox, .stTextInput, .stSlider {
#             background-color: white;
#             border-radius: var(--border-radius);
#             box-shadow: var(--card-shadow);
#             border: 1px solid #e2e8f0;
#         }
        
#         .header-card {
#             background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-light) 100%);
#             color: white;
#             border-radius: var(--border-radius);
#             padding: 2rem;
#             margin-bottom: 1.5rem;
#             box-shadow: var(--card-shadow);
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
#             color: #718096;
#             margin-bottom: 0.5rem;
#             font-weight: 500;
#             text-transform: uppercase;
#             letter-spacing: 0.5px;
#         }
        
#         .metric-value {
#             font-size: 1.75rem;
#             font-weight: 700;
#             color: var(--primary-color);
#             line-height: 1.2;
#         }
        
#         .metric-description {
#             font-size: 0.8rem;
#             color: #a0aec0;
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
#             height: 280px;
#             overflow-y: auto;
#             transition: var(--transition);
#         }
        
#         .data-card:hover {
#             box-shadow: 0 6px 12px rgba(0,0,0,0.1);
#         }
        
#         .data-card h4 {
#             color: var(--primary-color);
#             font-size: 1.1rem;
#             margin-bottom: 0.75rem;
#             border-bottom: 1px solid #e2e8f0;
#             padding-bottom: 0.5rem;
#             font-weight: 600;
#         }
        
#         .data-card p {
#             margin-bottom: 0.6rem;
#             font-size: 0.9rem;
#             line-height: 1.5;
#         }
        
#         .map-container {
#             border-radius: var(--border-radius);
#             overflow: hidden;
#             box-shadow: 0 6px 12px rgba(0,0,0,0.1);
#             margin-top: 1.5rem;
#             border: 1px solid #e2e8f0;
#         }
        
#         .tab-content {
#             padding: 1rem 0;
#         }
        
#         .stTabs [data-baseweb="tab-list"] {
#             gap: 4px;
#             padding: 0 2px;
#         }
        
#         .stTabs [data-baseweb="tab"] {
#             background: white;
#             border-radius: 6px 6px 0 0;
#             padding: 8px 16px;
#             transition: var(--transition);
#             border: 1px solid #e2e8f0;
#             margin-right: 0;
#             font-weight: 500;
#             font-size: 0.9rem;
#         }
        
#         .stTabs [aria-selected="true"] {
#             background-color: var(--primary-color);
#             color: white;
#             border-color: var(--primary-color);
#         }
        
#         .stTabs [aria-selected="false"]:hover {
#             background-color: #edf2f7;
#         }
        
#         @font-face {
#             font-family: 'Noto Sans Khmer';
#             src: url('https://fonts.googleapis.com/css2?family=Noto+Sans+Khmer:wght@400;500;600;700&display=swap');
#         }
        
#         body {
#             font-family: 'Noto Sans Khmer', 'Inter', Arial, sans-serif;
#         }
        
#         /* Section headers */
#         .section-header {
#             color: var(--primary-color);
#             font-size: 1.35rem;
#             font-weight: 600;
#             margin-bottom: 0.75rem;
#         }
        
#         .section-subheader {
#             color: #718096;
#             font-size: 0.95rem;
#             margin-bottom: 1.5rem;
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
#             background: #cbd5e0;
#             border-radius: 10px;
#         }
        
#         ::-webkit-scrollbar-thumb:hover {
#             background: #a0aec0;
#         }
        
#         /* Tooltip styling */
#         .map-tooltip {
#             font-family: 'Noto Sans Khmer', 'Inter', Arial, sans-serif;
#             border-radius: var(--border-radius);
#             box-shadow: 0 4px 12px rgba(0,0,0,0.1);
#             border: none;
#         }
        
#         /* Remove Streamlit default top padding */
#         .block-container {
#             padding-top: 1rem;
#             padding-bottom: 2rem;
#         }
        
#         /* Responsive adjustments */
#         @media (max-width: 768px) {
#             .metric-value {
#                 font-size: 1.5rem;
#             }
            
#             .header-card {
#                 padding: 1.5rem 1rem;
#             }
#         }
        
#         /* Loading spinner color */
#         .stSpinner > div > div {
#             border-color: var(--primary-color) transparent transparent transparent;
#         }
#     </style>
#     """, unsafe_allow_html=True)

#     # Header with gradient background and improved typography
#     st.markdown("""
#     <div class="header-card">
#         <h1 style="font-size: 2rem; margin-bottom: 0.5rem; font-weight: 700;">🏛️ ភូមិសាស្ត្រ</h1>
#         <p style="font-size: 1rem; margin: 0; opacity: 0.9;">ភូមិសាស្ត្រនៃព្រះរាជាណាចក្រកម្ពុជា</p>
#     </div>
#     """, unsafe_allow_html=True)

#     # Create tabs for different views with better spacing
#     tab1, tab2 = st.tabs(["🗺 ផែនទីខេត្ត & ស្ថិតិ", "📋 ទិន្នន័យលម្អិត"])

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
#         text_search = ""
#         selected_year = 2025
#         selected_status = "Active"
        
#         # Filter data based on default selections
#         filtered_df = df[(df['Start_Year'] <= selected_year) & (df['End_Year'] >= selected_year)]
#         filtered_df = filtered_df[filtered_df['EFF_STATUS'] == selected_status]
        
#         # Key Metrics Section with improved cards
#         if not filtered_df.empty:
#             st.markdown("""
#             <div style="margin: 1.5rem 0 1rem 0;">
#                 <h3 class="section-header">ស្ថិតិសំខាន់ៗ</h3>
#                 <p class="section-subheader">សូចនាករសំខាន់ៗនៃទិន្នន័យភូមិសាស្ត្រ</p>
#             </div>
#             """, unsafe_allow_html=True)
            
#             col1, col2, col3 = st.columns(3)
            
#             with col1:
#                 st.markdown(f"""
#                 <div class="metric-card">
#                     <div class="metric-title">ចំនួនសរុប</div>
#                     <div class="metric-value">{len(filtered_df):,}</div>
#                     <div class="metric-description">ធាតុទិន្នន័យសរុប</div>
#                 </div>
#                 """, unsafe_allow_html=True)
            
#             with col2:
#                 st.markdown(f"""
#                 <div class="metric-card">
#                     <div class="metric-title">ចំនួនខេត្ត</div>
#                     <div class="metric-value" style="color: var(--accent-color);">
#                         {filtered_df['Province_English'].nunique():,}
#                     </div>
#                     <div class="metric-description">ខេត្តដែលមានទិន្នន័យ</div>
#                 </div>
#                 """, unsafe_allow_html=True)
            
#             with col3:
#                 st.markdown(f"""
#                 <div class="metric-card">
#                     <div class="metric-title">ឆ្នាំដែលបានជ្រើសរើស</div>
#                     <div class="metric-value" style="color: var(--secondary-color);">
#                         {selected_year}
#                     </div>
#                     <div class="metric-description">ឆ្នាំដែលបានជ្រើសរើស</div>
#                 </div>
#                 """, unsafe_allow_html=True)
            
#             # Province Distribution Chart with improved layout
#             st.markdown("---")
#             st.markdown("""
#             <div style="margin-bottom: 1rem;">
#                 <h3 class="section-header">ការចែកចាយទិន្នន័យតាមខេត្ត</h3>
#                 <p class="section-subheader">ខេត្តដែលមានទិន្នន័យច្រើនបំផុត</p>
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
#                     color='#2a4a7f'
#                 )
            
#             with col2:
#                 st.markdown("""
#                 <div style="background: white; border-radius: var(--border-radius); padding: 1rem; box-shadow: var(--card-shadow); height: 100%;">
#                     <h4 style="color: var(--primary-color); margin-top: 0; margin-bottom: 1rem; font-weight: 600; font-size: 1rem;">ខេត្តកំពូល</h4>
#                     <ol style="padding-left: 1.2rem; margin: 0;">
#                 """, unsafe_allow_html=True)
                
#                 for i, row in top_provinces.iterrows():
#                     st.markdown(f"""
#                     <li style="margin-bottom: 0.75rem; padding-bottom: 0.5rem; border-bottom: 1px dashed #e2e8f0;">
#                         <span style="font-weight: 500; font-size: 0.9rem;">{row['Province']}</span>
#                         <span style="float: right; color: var(--accent-color); font-weight: 600;">{row['Count']:,}</span>
#                     </li>
#                     """, unsafe_allow_html=True)
                
#                 st.markdown("</ol></div>", unsafe_allow_html=True)
            
#             # Interactive Map Visualization with improved styling
#             st.markdown("---")
#             st.markdown("""
#             <div style="margin-bottom: 1rem;">
#                 <h2 class="section-header">ផែនទីខេត្តនៃព្រះរាជាណាចក្រកម្ពុជា</h2>
#                 <p class="section-subheader">ចុចលើចំណុចនីមួយៗដើម្បីមើលព័ត៌មានលម្អិត</p>
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
                
#                 # Create map layers with improved styling
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
#                     get_fill_color=[42, 74, 127, 200],
#                     get_line_color=[0, 0, 0, 150],
#                 )

#                 text_layer = pdk.Layer(
#                     "TextLayer",
#                     province_df,
#                     pickable=False,
#                     get_position=["Longitude", "Latitude"],
#                     get_text="Province_Khmer",
#                     get_size=14,
#                     get_color=[0, 0, 0, 200],
#                     get_angle=0,
#                     get_text_anchor="'middle'",
#                     get_alignment_baseline="'center'",
#                 )

#                 view_state = pdk.ViewState(
#                     latitude=12.5657,
#                     longitude=104.9910,
#                     zoom=6.2,
#                     pitch=0,
#                 )

#                 # Render the map in a container with improved tooltip
#                 with st.container():
#                     st.pydeck_chart(
#                         pdk.Deck(
#                             layers=[layer, text_layer],
#                             initial_view_state=view_state,
#                             tooltip={
#                                 "html": """
#                                 <div class="map-tooltip" style="padding: 10px; background: white; max-width: 280px;">
#                                     <h3 style="margin: 0 0 6px 0; color: #1a365d; border-bottom: 1px solid #e2e8f0; padding-bottom: 6px; font-size: 1rem;">{Province_Khmer}</h3>
#                                     <p style="margin: 4px 0; font-size: 0.85rem;"><b>ចំនួនទិន្នន័យ:</b> <span style="color: #38a169; font-weight: 600;">{count}</span></p>
#                                     <p style="margin: 4px 0; font-size: 0.85rem;"><b>ស្ថានភាព:</b> <span style="color: {color}; font-weight: 500;">{EFF_STATUS}</span></p>
#                                     <p style="margin: 4px 0 0 0; font-size: 0.8rem; color: #718096;">ចុចដើម្បីមើលព័ត៌មានលម្អិត</p>
#                                 </div>
#                                 """.replace("{color}", "'#38a169'" if selected_status == "Active" else "'#e53e3e'"),
#                                 "style": {
#                                     "fontFamily": "'Noto Sans Khmer', 'Inter', Arial, sans-serif",
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

#     # Tab 2: Detailed Data with improved layout
#     with tab2:
#         st.markdown("""
#         <div style="margin-bottom: 1.5rem;">
#             <h2 class="section-header">ទិន្នន័យលម្អិត</h2>
#             <p class="section-subheader">ព័ត៌មានលម្អិតអំពីភូមិសាស្ត្រកម្ពុជា</p>
#         </div>
#         """, unsafe_allow_html=True)
        
#         # Filter controls with consistent styling
#         with st.container():
#             col1, col2, col3 = st.columns([2, 1, 1])
            
#             with col1:
#                 tab2_text_search = st.text_input(
#                     "ស្វែងរកពាក្យ (ទិន្នន័យលម្អិត)",
#                     value="",
#                     placeholder="ស្វែងរកពាក្យគន្លឹះ...",
#                     key="tab2_search"
#                 )
            
#             with col2:
#                 year_options = ("2000", "2023", "2024", "2025")
#                 tab2_selected_year = st.selectbox(
#                     "ឆ្នាំ (ទិន្នន័យលម្អិត)",
#                     year_options,
#                     index=3,
#                     key="tab2_year"
#                 )
#                 tab2_selected_year = int(tab2_selected_year)
            
#             with col3:
#                 status_options = ("Active", "Inactive")
#                 tab2_selected_status = st.selectbox(
#                     "ស្ថានភាព (ទិន្នន័យលម្អិត)",
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

#         # Data display with improved cards
#         if not tab2_filtered_df.empty:
#             st.markdown(f"""
#             <div style="background: white; border-radius: var(--border-radius); padding: 1rem; margin-bottom: 1rem; box-shadow: var(--card-shadow);">
#                 <div style="display: flex; justify-content: space-between; align-items: center;">
#                     <p style="margin: 0; color: var(--primary-color); font-weight: 500; font-size: 0.95rem;">
#                         បានរកឃើញ: <strong style="color: var(--accent-color);">{len(tab2_filtered_df):,}</strong> ធាតុទិន្នន័យ
#                     </p>
#                     <p style="margin: 0; color: #718096; font-size: 0.85rem;">
#                         កាលបរិច្ឆេទ: {datetime.now().strftime("%d %B %Y")}
#                     </p>
#                 </div>
#             </div>
#             """, unsafe_allow_html=True)
            
#             # Display filtered results in a responsive grid with improved cards
#             cols = st.columns(3)
            
#             for idx, row in tab2_filtered_df.iterrows():
#                 with cols[idx % 3]:
#                     province = str(row['នៅក្រោមខេត្ត']).strip() if pd.notna(row['នៅក្រោមខេត្ត']) else None
#                     province_text = (
#                         f"""<p style="margin: 0.4rem 0; font-size: 0.85rem;">
#                             <span style="color: #718096;">🏛 ខេត្ត:</span> 
#                             <span style="color: var(--accent-color); font-weight: 500;">{province}</span>
#                         </p>"""
#                         if province else ""
#                     )

#                     status_color = "#38a169" if row['EFF_STATUS'] == 'Active' else "#e53e3c"
#                     status_icon = "🟢" if row['EFF_STATUS'] == 'Active' else "🔴"
                    
#                     st.markdown(f"""
#                     <div class="data-card">
#                         <h4>{row['PRODUCT']}</h4>
#                         <p style="margin: 0.4rem 0;">
#                             <span style="color: #718096;">📅 ឆ្នាំ:</span> 
#                             <span style="color: var(--primary-light); font-weight: 500;">{row['EFFDT_Year']}-2025</span>
#                         </p>
#                         <p style="margin: 0.4rem 0;">
#                             <span style="color: #718096;">{status_icon} ស្ថានភាព:</span> 
#                             <span style="color: {status_color}; font-weight: 500;">
#                                 {row['EFF_STATUS']}
#                             </span>
#                         </p>
#                         <p style="margin: 0.4rem 0;">
#                             <span style="color: #718096;">📖 ពណ៌នា:</span> 
#                             <span style="color: var(--primary-color);">
#                                 {row['DESCRLONG_KHM'][:100]}{'...' if len(row['DESCRLONG_KHM']) > 100 else ''}
#                             </span>
#                         </p>
#                         {province_text}
#                         <div style="margin-top: 0.5rem; text-align: right;">
#                             <span style="font-size: 0.75rem; color: #a0aec0; font-style: italic;">ធាតុទិន្នន័យ #{idx + 1}</span>
#                         </div>
#                     </div>
#                     """, unsafe_allow_html=True)
#         else:
#             st.info("No data found for the selected filters.")

# if __name__ == "__main__":
#     Geography()



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
        file_path = "Geographyfordatareader.xlsx"
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
        st.subheader("Filtered Results")
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
        
#         .subsection-header {
#             font-size: 1.3rem;
#             font-weight: 600;
#             margin: 1.5rem 0 1rem 0;
#             color: #2c3e50;
#             padding-left: 0.5rem;
#             border-left: 4px solid #667eea;
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

#         # First Row: Distribution Charts
#         st.markdown('<div class="subsection-header">Data Distribution Analysis</div>', unsafe_allow_html=True)
#         col1, col2 = st.columns([2, 1])
        
#         with col1:
#             # Enhanced pie chart with more details
#             group_data = current_data['group'].value_counts().reset_index()
#             group_data.columns = ['Category', 'Count']
            
#             fig_pie = px.pie(
#                 group_data, 
#                 values='Count', 
#                 names='Category',
#                 hole=0.5,
#                 color_discrete_sequence=px.colors.sequential.Blues_r,
#                 template='plotly_white'
#             )
            
#             fig_pie.update_layout(
#                 height=400,
#                 showlegend=True,
#                 plot_bgcolor='rgba(0,0,0,0)',
#                 paper_bgcolor='rgba(0,0,0,0)',
#                 font=dict(size=12, family='Arial'),
#                 margin=dict(t=40, b=20, l=20, r=20),
#                 title=dict(
#                     text='Data Distribution by Category',
#                     x=0.5,
#                     font=dict(size=16, color='#2c3e50')
#                 )
#             )
            
#             fig_pie.update_traces(
#                 textposition='inside',
#                 textinfo='percent+label',
#                 marker=dict(line=dict(color='white', width=2)),
#                 hovertemplate='<b>%{label}</b><br>Count: %{value}<br>Percentage: %{percent}'
#             )
            
#             st.plotly_chart(fig_pie, use_container_width=True)

#         with col2:
#             # Enhanced gauge chart
#             active_count = len(current_data)
#             total_count = len(df)
#             inactive_count = total_count - active_count
            
#             fig_gauge = go.Figure(go.Indicator(
#                 mode = "gauge+number+delta",
#                 value = active_count,
#                 domain = {'x': [0, 1], 'y': [0, 1]},
#                 title = {'text': "Active Records", 'font': {'size': 16, 'color': '#2c3e50'}},
#                 delta = {'reference': total_count, 'relative': True, 'position': "top"},
#                 gauge = {
#                     'axis': {'range': [None, total_count], 'tickwidth': 1, 'tickcolor': "darkblue"},
#                     'bar': {'color': "#667eea"},
#                     'bgcolor': "white",
#                     'borderwidth': 2,
#                     'bordercolor': "gray",
#                     'steps': [
#                         {'range': [0, inactive_count], 'color': '#f8f9fa'},
#                         {'range': [inactive_count, total_count], 'color': '#e3f2fd'}],
#                     'threshold': {
#                         'line': {'color': "red", 'width': 4},
#                         'thickness': 0.75,
#                         'value': total_count}}
#             ))
            
#             fig_gauge.update_layout(
#                 height=300, 
#                 font={'color': "#2c3e50", 'family': "Arial"},
#                 paper_bgcolor='rgba(0,0,0,0)',
#                 plot_bgcolor='rgba(0,0,0,0)'
#             )
#             st.plotly_chart(fig_gauge, use_container_width=True)

#         # Second Row: Temporal Analysis and Province Distribution
#         st.markdown('<div class="subsection-header">Temporal & Geographic Analysis</div>', unsafe_allow_html=True)
#         col1, col2 = st.columns([1, 1])
        
#         with col1:
#             # Temporal distribution - Records by Year
#             yearly_data = df.groupby('Start_Year').size().reset_index(name='Count')
#             yearly_data = yearly_data.sort_values('Start_Year')
            
#             fig_line = px.line(
#                 yearly_data,
#                 x='Start_Year',
#                 y='Count',
#                 title='Records Distribution Over Time',
#                 markers=True,
#                 line_shape='spline',
#                 color_discrete_sequence=['#667eea']
#             )
            
#             fig_line.update_layout(
#                 height=350,
#                 xaxis_title='Year',
#                 yaxis_title='Number of Records',
#                 template='plotly_white',
#                 showlegend=False,
#                 plot_bgcolor='rgba(0,0,0,0)',
#                 paper_bgcolor='rgba(0,0,0,0)'
#             )
            
#             fig_line.update_traces(
#                 line=dict(width=4),
#                 marker=dict(size=8, color='#764ba2')
#             )
            
#             st.plotly_chart(fig_line, use_container_width=True)

#         with col2:
#             # Province-wise distribution (Top 10)
#             province_data = current_data['Province_English'].value_counts().head(10).reset_index()
#             province_data.columns = ['Province', 'Count']
            
#             fig_bar = px.bar(
#                 province_data,
#                 x='Count',
#                 y='Province',
#                 orientation='h',
#                 title='Top 10 Provinces by Record Count',
#                 color='Count',
#                 color_continuous_scale='Blues'
#             )
            
#             fig_bar.update_layout(
#                 height=350,
#                 xaxis_title='Number of Records',
#                 yaxis_title='Province',
#                 template='plotly_white',
#                 showlegend=False,
#                 plot_bgcolor='rgba(0,0,0,0)',
#                 paper_bgcolor='rgba(0,0,0,0)'
#             )
            
#             fig_bar.update_traces(
#                 marker=dict(line=dict(width=0))
#             )
            
#             st.plotly_chart(fig_bar, use_container_width=True)

#     with tab2:
#         st.markdown('<div class="section-header">Spatial Distribution Map</div>', unsafe_allow_html=True)
        
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
#         # Your Data Explorer tab design
#         st.markdown(
#             """
#             <h1 style="text-align: center; color: #1f2937; font-size: 40px; font-weight: bold; padding: 10px;">
#                 ភូមិសាស្រ្ត
#             </h1>
#             """,
#             unsafe_allow_html=True,
#         )

#         # Create layout columns
#         col1, col2, col3, col4 = st.columns([30, 5, 5, 2])

#         # Text search
#         with col1:
#             text_search = st.text_input("និយមន័យពី ទិន្នន័យមេ ​​ស្វែងយល់បន្ថែម", value="")

#         # Year selection
#         with col2:
#             options = ("2000", "2023", "2024", "2025")
#             option = st.selectbox("ឆ្នាំ", options, index=options.index("2025"))

#         # Status selection
#         with col3:
#             status_options = ("Active", "Inactive")
#             selected_status = st.selectbox("ស្ថានភាព", status_options, index=0)

#         # Use the already loaded df from cache
#         # Filter by year and status
#         selected_year = int(option)

#         filtered_df = df[(df['Start_Year'] <= selected_year) & (df['End_Year'] >= selected_year)]
#         filtered_df = filtered_df[filtered_df['EFF_STATUS'] == selected_status]

#         # Filter by search text
#         if text_search:
#             mask1 = filtered_df["DESCRLONG_KHM"].str.contains(text_search, case=False, na=False)
#             mask2 = filtered_df["PRODUCT"].str.contains(text_search, case=False, na=False)
#             mask3 = filtered_df["Province_English"].str.contains(text_search, case=False, na=False)
#             filtered_df = filtered_df[mask1 | mask2 | mask3]

#         # Display filtered results
#         st.subheader("Filtered Results")
        
#         # Show results count
#         st.markdown(f"""
#         <div style="background: var(--primary-gradient); color: white; padding: 1rem; border-radius: 12px; margin: 1rem 0;">
#             <div style="display: flex; justify-content: space-between; align-items: center;">
#                 <span>📈 លទ្ធផលដែលបានចម្រាញ់: <strong>{len(filtered_df):,}</strong> កំណត់ត្រាត្រូវបានរកឃើញ</span>
#                 <span>🕐 បានធ្វើបច្ចុប្បន្នភាពចុងក្រោយ: {datetime.now().strftime("%Y-%m-%d %H:%M")}</span>
#             </div>
#         </div>
#         """, unsafe_allow_html=True)

#         if not filtered_df.empty:
#             # Limit to first 12 records for better display
#             filtered_df = filtered_df.head(12)

#             num_cards = len(filtered_df)
#             cards_per_col = (num_cards + 2) // 3

#             col1_df = filtered_df.iloc[:cards_per_col]
#             col2_df = filtered_df.iloc[cards_per_col:2*cards_per_col]
#             col3_df = filtered_df.iloc[2*cards_per_col:]

#             cols = st.columns(3)

#             for i, col_df in enumerate([col1_df, col2_df, col3_df]):
#                 with cols[i]:
#                     for _, row in col_df.iterrows():
#                         # Get province information - adjust column name as needed
#                         province_column = 'Province_English' if 'Province_English' in row else 'នៅក្រោមខេត្ត'
#                         province = str(row[province_column]).strip() if pd.notna(row[province_column]) and str(row[province_column]).strip() != '' else None
                        
#                         province_text = (
#                             f"<p style='font-size: 16px;'><b style='color:#28a745;'>🏛 ស្ថិតនៅក្រោមខេត្ត:</b> {province}</p>"
#                             if province else ""
#                         )

#                         card_html = f"""
#                         <div style="border: 1px solid #ddd; border-radius: 10px; padding: 20px; margin-bottom: 20px; background-color: #f9f9f9; height: 280px; overflow-y: auto; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
#                             <h4 style="color: #1f2937; font-size: 22px; height: 50px; overflow: hidden; text-overflow: ellipsis;">{row['PRODUCT']}</h4>
#                             <p style="font-size: 18px;"><b style='color:#694a56;'>📅 កាលបរិច្ឆេទមានប្រសិទ្ធភាព:</b> <span style="color: #FF6347;">{row['EFFDT_Year']}-2025</span></p>
#                             <p style="font-size: 18px;"><b style='color:#694a56;'>📖 បរិយាយ:</b> <span style="color: #858585;">{row['DESCRLONG_KHM']}</span></p>
#                             <p style="font-size: 18px;"><b style='color:#694a56;'>ស្ថានភាព:</b> <span style="color:#694a56;">{row['EFF_STATUS']}</span></p>
#                             {province_text}
#                         </div>
#                         """

#                         st.markdown(card_html, unsafe_allow_html=True)
            
#             # Download button
#             if len(filtered_df) > 0:
#                 csv = filtered_df.to_csv(index=False)
#                 st.download_button(
#                     label="📥 ទាញយកទិន្នន័យដែលបានចម្រាញ់",
#                     data=csv,
#                     file_name=f"cambodia_geographic_data_{datetime.now().strftime('%Y%m%d')}.csv",
#                     mime="text/csv",
#                 )
#         else:
#             st.info("គ្មានទិន្នន័យ被发现សម្រាប់ឆ្នាំនិងលក្ខណៈវិនិច្ឆ័យស្វែងរកដែលបានជ្រើសរើស។")

# if __name__ == "__main__":
#     Geography()

# # IMPORTS AT THE VERY TOP
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
        
#         .subsection-header {
#             font-size: 1.3rem;
#             font-weight: 600;
#             margin: 1.5rem 0 1rem 0;
#             color: #2c3e50;
#             padding-left: 0.5rem;
#             border-left: 4px solid #667eea;
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

#         # First Row: Distribution Charts
#         st.markdown('<div class="subsection-header">Data Distribution Analysis</div>', unsafe_allow_html=True)
#         col1, col2 = st.columns([2, 1])
        
#         with col1:
#             # Enhanced pie chart with more details
#             group_data = current_data['group'].value_counts().reset_index()
#             group_data.columns = ['Category', 'Count']
            
#             fig_pie = px.pie(
#                 group_data, 
#                 values='Count', 
#                 names='Category',
#                 hole=0.5,
#                 color_discrete_sequence=px.colors.sequential.Blues_r,
#                 template='plotly_white'
#             )
            
#             fig_pie.update_layout(
#                 height=400,
#                 showlegend=True,
#                 plot_bgcolor='rgba(0,0,0,0)',
#                 paper_bgcolor='rgba(0,0,0,0)',
#                 font=dict(size=12, family='Arial'),
#                 margin=dict(t=40, b=20, l=20, r=20),
#                 title=dict(
#                     text='Data Distribution by Category',
#                     x=0.5,
#                     font=dict(size=16, color='#2c3e50')
#                 )
#             )
            
#             fig_pie.update_traces(
#                 textposition='inside',
#                 textinfo='percent+label',
#                 marker=dict(line=dict(color='white', width=2)),
#                 hovertemplate='<b>%{label}</b><br>Count: %{value}<br>Percentage: %{percent}'
#             )
            
#             st.plotly_chart(fig_pie, use_container_width=True)

#         # with col2:
#             # # Enhanced gauge chart
#             # active_count = len(current_data)
#             # total_count = len(df)
#             # inactive_count = total_count - active_count
            
#             # fig_gauge = go.Figure(go.Indicator(
#             #     mode = "gauge+number+delta",
#             #     value = active_count,
#             #     domain = {'x': [0, 1], 'y': [0, 1]},
#             #     title = {'text': "Active Records", 'font': {'size': 16, 'color': '#2c3e50'}},
#             #     delta = {'reference': total_count, 'relative': True, 'position': "top"},
#             #     gauge = {
#             #         'axis': {'range': [None, total_count], 'tickwidth': 1, 'tickcolor': "darkblue"},
#             #         'bar': {'color': "#667eea"},
#             #         'bgcolor': "white",
#             #         'borderwidth': 2,
#             #         'bordercolor': "gray",
#             #         'steps': [
#             #             {'range': [0, inactive_count], 'color': '#f8f9fa'},
#             #             {'range': [inactive_count, total_count], 'color': '#e3f2fd'}],
#             #         'threshold': {
#             #             'line': {'color': "red", 'width': 4},
#             #             'thickness': 0.75,
#             #             'value': total_count}}
#             # ))
            
#             # fig_gauge.update_layout(
#             #     height=300, 
#             #     font={'color': "#2c3e50", 'family': "Arial"},
#             #     paper_bgcolor='rgba(0,0,0,0)',
#             #     plot_bgcolor='rgba(0,0,0,0)'
#             # )
#             # st.plotly_chart(fig_gauge, use_container_width=True)

#         # Second Row: Temporal Analysis and Province Distribution
#         st.markdown('<div class="subsection-header">Temporal & Geographic Analysis</div>', unsafe_allow_html=True)
#         col1, col2 = st.columns([1, 1])
        
#         with col1:
#             # Temporal distribution - Records by Year
#             yearly_data = df.groupby('Start_Year').size().reset_index(name='Count')
#             yearly_data = yearly_data.sort_values('Start_Year')
            
#             fig_line = px.line(
#                 yearly_data,
#                 x='Start_Year',
#                 y='Count',
#                 title='Records Distribution Over Time',
#                 markers=True,
#                 line_shape='spline',
#                 color_discrete_sequence=['#667eea']
#             )
            
#             fig_line.update_layout(
#                 height=350,
#                 xaxis_title='Year',
#                 yaxis_title='Number of Records',
#                 template='plotly_white',
#                 showlegend=False,
#                 plot_bgcolor='rgba(0,0,0,0)',
#                 paper_bgcolor='rgba(0,0,0,0)'
#             )
            
#             fig_line.update_traces(
#                 line=dict(width=4),
#                 marker=dict(size=8, color='#764ba2')
#             )
            
#             st.plotly_chart(fig_line, use_container_width=True)

#         with col2:
#             # Province-wise distribution (Top 10)
#             province_data = current_data['Province_English'].value_counts().head(10).reset_index()
#             province_data.columns = ['Province', 'Count']
            
#             fig_bar = px.bar(
#                 province_data,
#                 x='Count',
#                 y='Province',
#                 orientation='h',
#                 title='Top 10 Provinces by Record Count',
#                 color='Count',
#                 color_continuous_scale='Blues'
#             )
            
#             fig_bar.update_layout(
#                 height=350,
#                 xaxis_title='Number of Records',
#                 yaxis_title='Province',
#                 template='plotly_white',
#                 showlegend=False,
#                 plot_bgcolor='rgba(0,0,0,0)',
#                 paper_bgcolor='rgba(0,0,0,0)'
#             )
            
#             fig_bar.update_traces(
#                 marker=dict(line=dict(width=0))
#             )
            
#             st.plotly_chart(fig_bar, use_container_width=True)

#         # Third Row: Status Analysis and Additional Metrics
#         st.markdown('<div class="subsection-header">Status & Performance Metrics</div>', unsafe_allow_html=True)
#         col1, col2, col3 = st.columns([2, 1, 1])
        
#         with col1:
#             # Status comparison over years
#             status_yearly = df.groupby(['Start_Year', 'EFF_STATUS']).size().reset_index(name='Count')
            
#             fig_area = px.area(
#                 status_yearly,
#                 x='Start_Year',
#                 y='Count',
#                 color='EFF_STATUS',
#                 title='Status Distribution Over Time',
#                 color_discrete_map={'Active': '#43e97b', 'Inactive': '#ff9a9e'}
#             )
            
#             fig_area.update_layout(
#                 height=300,
#                 xaxis_title='Year',
#                 yaxis_title='Number of Records',
#                 template='plotly_white',
#                 plot_bgcolor='rgba(0,0,0,0)',
#                 paper_bgcolor='rgba(0,0,0,0)'
#             )
            
#             st.plotly_chart(fig_area, use_container_width=True)

#         with col2:
#             # Donut chart for status distribution
#             status_data = current_data['EFF_STATUS'].value_counts().reset_index()
#             status_data.columns = ['Status', 'Count']
            
#             fig_donut = px.pie(
#                 status_data,
#                 values='Count',
#                 names='Status',
#                 hole=0.7,
#                 color_discrete_map={'Active': '#43e97b', 'Inactive': '#ff9a9e'}
#             )
            
#             fig_donut.update_layout(
#                 height=300,
#                 showlegend=True,
#                 margin=dict(t=40, b=20, l=20, r=20),
#                 annotations=[dict(text='Status', x=0.5, y=0.5, font_size=14, showarrow=False)]
#             )
            
#             fig_donut.update_traces(
#                 textposition='inside',
#                 textinfo='percent+label'
#             )
            
#             st.plotly_chart(fig_donut, use_container_width=True)

#         with col3:
#             # Quick metrics card
#             st.markdown("""
#             <div class="glass-card" style="text-align: center; height: 300px; display: flex; flex-direction: column; justify-content: center;">
#                 <div style="font-size: 3rem; margin-bottom: 1rem;">📈</div>
#                 <div style="font-size: 1.2rem; font-weight: 600; color: #2c3e50; margin-bottom: 0.5rem;">Performance Insights</div>
#                 <div style="font-size: 0.9rem; color: #64748b; line-height: 1.5;">
#                     • <strong>{(len(current_data)/len(df)*100):.1f}%</strong> Active Rate<br>
#                     • <strong>{current_data['Province_English'].nunique()}</strong> Provinces Covered<br>
#                     • Data spans <strong>{df['Start_Year'].min()}-{df['Start_Year'].max()}</strong>
#                 </div>
#             </div>
#             """, unsafe_allow_html=True)

#         # Fourth Row: Advanced Analytics
#         st.markdown('<div class="subsection-header">Advanced Analytics</div>', unsafe_allow_html=True)
#         col1, col2 = st.columns([1, 1])
        
#         with col1:
#             # Monthly/Quarterly distribution (if date data is available)
#             if 'EFFDT' in df.columns and df['EFFDT'].notna().any():
#                 monthly_data = df[df['EFFDT'].notna()].copy()
#                 monthly_data['Month'] = monthly_data['EFFDT'].dt.month
#                 monthly_counts = monthly_data['Month'].value_counts().sort_index().reset_index()
#                 monthly_counts.columns = ['Month', 'Count']
                
#                 fig_monthly = px.bar(
#                     monthly_counts,
#                     x='Month',
#                     y='Count',
#                     title='Monthly Distribution (All Years)',
#                     color='Count',
#                     color_continuous_scale='Viridis'
#                 )
                
#                 fig_monthly.update_layout(
#                     height=300,
#                     xaxis_title='Month',
#                     yaxis_title='Number of Records',
#                     template='plotly_white'
#                 )
                
#                 st.plotly_chart(fig_monthly, use_container_width=True)
#             else:
#                 # Alternative: Group distribution by type
#                 group_comparison = df.groupby(['group', 'EFF_STATUS']).size().reset_index(name='Count')
                
#                 fig_group = px.bar(
#                     group_comparison,
#                     x='group',
#                     y='Count',
#                     color='EFF_STATUS',
#                     title='Distribution by Group and Status',
#                     barmode='group',
#                     color_discrete_map={'Active': '#43e97b', 'Inactive': '#ff9a9e'}
#                 )
                
#                 fig_group.update_layout(
#                     height=300,
#                     xaxis_title='Group Type',
#                     yaxis_title='Number of Records',
#                     template='plotly_white'
#                 )
                
#                 st.plotly_chart(fig_group, use_container_width=True)

#         with col2:
#             # Trend analysis - Cumulative records over time
#             yearly_cumulative = df.groupby('Start_Year').size().cumsum().reset_index(name='Cumulative')
#             yearly_cumulative.columns = ['Year', 'Cumulative Records']
            
#             fig_trend = px.area(
#                 yearly_cumulative,
#                 x='Year',
#                 y='Cumulative Records',
#                 title='Cumulative Records Over Time',
#                 color_discrete_sequence=['#4facfe']
#             )
            
#             fig_trend.update_layout(
#                 height=300,
#                 xaxis_title='Year',
#                 yaxis_title='Cumulative Records',
#                 template='plotly_white',
#                 showlegend=False
#             )
            
#             st.plotly_chart(fig_trend, use_container_width=True)

#     with tab2:
#         st.markdown('<div class="section-header">Spatial Distribution Map</div>', unsafe_allow_html=True)
        
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
            
#             col1, col2, col3, col4 = st.columns(4)
            
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
            
#             with col3:
#                 #🤣 Count districts from group column where group == 'District'
#                 district_count = len(filtered_df[filtered_df['group'] == 'District'])
#                 st.markdown(f"""
#                 <div class="metric-card">
#                     <div class="metric-title">Districts</div>
#                     <div class="metric-value" style="color: var(--success-color);">
#                         {district_count:,}
#                     </div>
#                     <div class="metric-description">District records in dataset</div>
#                 </div>
#                 """, unsafe_allow_html=True)
                
#             with col4:
#                 active_percentage = (len(filtered_df[filtered_df['EFF_STATUS'] == 'Active']) / len(df)) * 100
#                 st.markdown(f"""
#                 <div class="metric-card">
#                     <div class="metric-title">Active Data</div>
#                     <div class="metric-value" style="color: var(--warning-color);">
#                         {active_percentage:.1f}%
#                     </div>
#                     <div class="metric-description">Active records from total</div>
#                 </div>
#                 """, unsafe_allow_html=True)
            
#             # District Distribution Chart
#             st.markdown("---")
#             st.markdown("""
#             <div style="margin-bottom: 1.25rem;">
#                 <h3 class="section-header">District Distribution</h3>
#                 <p class="section-subheader">Data concentration across districts</p>
#             </div>
#             """, unsafe_allow_html=True)
            
#             # Get district data where group == 'District'
#             district_data = filtered_df[filtered_df['group'] == 'District']
            
#             if not district_data.empty:
#                 # Get top districts by record count (using the appropriate district name column)
#                 # Assuming district names are in 'នៅក្រោមខេត្ត' or similar column
#                 district_col = 'នៅក្រោមខេត្ត' if 'នៅក្រោមខេត្ត' in district_data.columns else 'Province_English'
#                 top_districts = district_data[district_col].value_counts().head(10).reset_index()
#                 top_districts.columns = ['District', 'Count']
                
#                 # Use columns to make the chart responsive
#                 col1, col2 = st.columns([3, 1])
                
#                 with col1:
#                     st.bar_chart(
#                         top_districts.set_index('District'),
#                         height=350,
#                         use_container_width=True,
#                         color='#1a73e8'
#                     )
                
#                 with col2:
#                     st.markdown("""
#                     <div style="background: white; border-radius: var(--border-radius); padding: 1rem; box-shadow: var(--card-shadow); height: 100%;">
#                         <h4 style="color: var(--secondary-color); margin-top: 0; font-weight: 600; font-size: 1rem;">Top Districts</h4>
#                         <ol style="padding-left: 1.2rem; margin-top: 0.75rem;">
#                     """, unsafe_allow_html=True)
                    
#                     for i, row in top_districts.iterrows():
#                         st.markdown(f"""
#                         <li style="margin-bottom: 0.6rem; padding-bottom: 0.4rem; border-bottom: 1px dashed #eee; font-size: 0.9rem;">
#                             <span style="font-weight: 500;">{row['District']}</span>
#                             <span style="float: right; color: var(--accent-color); font-weight: 600;">{row['Count']:,}</span>
#                         </li>
#                         """, unsafe_allow_html=True)
                    
#                     st.markdown("</ol></div>", unsafe_allow_html=True)
#             else:
#                 st.info("No district data available for the selected filters.")
            
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
#                                     <p style="margin: 4px 0; font-size: 0.85rem;"><b>Group:</b> <span style="color: #e91e63; font-weight: 600;">{group}</span></p>
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
#                 # Filter by group type
#                 group_options = sorted(df['group'].unique())
#                 tab2_selected_group = st.selectbox(
#                     "Group Type",
#                     group_options,
#                     index=0,
#                     key="tab2_group"
#                 )
            
#             with col3:
#                 status_options = ("Active", "Inactive")
#                 tab2_selected_status = st.selectbox(
#                     "Status",
#                     status_options,
#                     index=0,
#                     key="tab2_status"
#                 )
        
#         # Filter data based on selections
#         tab2_filtered_df = df[df['group'] == tab2_selected_group]
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
#                         Found: <strong style="color: var(--primary-color);">{len(tab2_filtered_df):,}</strong> records in <strong style="color: var(--accent-color);">{tab2_selected_group}</strong> group
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
#                     province = str(row['Province_English']).strip() if pd.notna(row['Province_English']) else None
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
#                             <span style="color: #7f8c8d;">🏷️ Group:</span> 
#                             <span style="color: var(--primary-color); font-weight: 500;">{row['group']}</span>
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