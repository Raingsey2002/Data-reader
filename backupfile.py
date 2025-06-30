import streamlit as st
import pandas as pd

# Set page layout to wide mode (must be the first Streamlit command)
st.set_page_config(layout="wide")

st.markdown(
    """
    <h1 style="text-align: center; color: #1f2937; font-size: 40px; font-weight: bold; padding: 10px;">
        Data Reader
    </h1>
    """,
    unsafe_allow_html=True,
)

# Create three columns for layout
col1, col2, col3 = st.columns([30, 5, 2])  # Adjust column widths as needed

# Place the text input in the first column
with col1:
    text_search = st.text_input("និយមន័យពី ទិន្នន័យមេ ​​ស្វែងយល់បន្ថែម", value="")

# Place the selectbox in the second column
with col2:
    options = ("2000" ,"2023", "2024", "2025")  # Only show the specified years
    option = st.selectbox(
        "ឆ្នាំ",
        options,
        index=options.index("2025"),  # Set default to '2025'
        placeholder="Select year...",
    )

# File path for your Excel file
file_path = "OU_df_merged_test.xlsx"

# Read the Excel file into a dataframe
df = pd.read_excel(file_path, dtype=str).fillna("")
df = df[['OPERATING_UNIT', 'Len', 'EFFDT', 'EFFDT_Year', 'EFF_STATUS', 'DESCRLONG_KHM', 'នៅក្រោមក្រសួង', 'រដ្ឋបាលខេត្ត']]

# Convert 'EFFDT' to datetime and extract the year
df['EFFDT'] = pd.to_datetime(df['EFFDT'], errors='coerce')
df['Effective_date'] = df['EFFDT_Year'].astype(str) + '-2025'

# Ensure 'EFFDT_Year' is in 'YYYY-YYYY' format
df[['Start_Year', 'End_Year']] = df['Effective_date'].str.split('-', expand=True)
df['Start_Year'] = df['Start_Year'].astype(int)
df['End_Year'] = df['End_Year'].astype(int)

# Convert selected year to integer
selected_year = int(option)

# Step 1: Filter the dataframe based on the selected year range
filtered_df = df[(df['Start_Year'] <= selected_year) & (df['End_Year'] >= selected_year)]

# Step 2: Apply text search filter (only after filtering by year)
if text_search:
    mask1 = filtered_df["DESCRLONG_KHM"].str.contains(text_search, case=False, na=False)
    mask2 = filtered_df["OPERATING_UNIT"].str.contains(text_search, case=False, na=False)
    filtered_df = filtered_df[mask1 | mask2]

# Display results in a three-column layout
st.subheader("Filtered Results")
if not filtered_df.empty:
    num_cards = len(filtered_df)
    cards_per_col = (num_cards + 2) // 3  # Ensure balanced columns

    col1_df = filtered_df.iloc[:cards_per_col]
    col2_df = filtered_df.iloc[cards_per_col:2*cards_per_col]
    col3_df = filtered_df.iloc[2*cards_per_col:]

    cols = st.columns(3)
    
    # for i, col_df in enumerate([col1_df, col2_df, col3_df]):
    #     with cols[i]:
    #         for _, row in col_df.iterrows():
    #             # Ensure values are properly handled
    #             ministry = str(row['នៅក្រោមក្រសួង']).strip() if pd.notna(row['នៅក្រោមក្រសួង']) else ""
    #             province = str(row['រដ្ឋបាលខេត្ត']).strip() if pd.notna(row['រដ្ឋបាលខេត្ត']) else ""

    #             # Create HTML sections only if there's data to display
    #             ministry_text = (
    #                 f"<p style='font-size: 16px;'><b style='color:#28a745;'>🏛 ស្ថិតនៅក្រោមក្រសួង:</b> {ministry}</p>"
    #                 if ministry else ""
    #             )
    #             province_text = (
    #                 f"<p style='font-size: 16px;'><b style='color:#28a745;'>🌍 ស្ថិតនៅក្រោមរដ្ឋបាលខេត្ត:</b> {province}</p>"
    #                 if province else ""
    #             )

    #             # Wrap in div to prevent layout issues
    #             card_html = f"""
    #             <div style="border: 1px solid #ddd; border-radius: 10px; padding: 20px; margin-bottom: 20px; background-color: #f9f9f9; height: 260px; overflow-y: auto;">
    #                 <h4 style="color: #1f2937; font-size: 22px; height: 50px; overflow: hidden; text-overflow: ellipsis;">{row['OPERATING_UNIT']}</h4>
    #                 <p style="font-size: 18px;"><b style='color:#694a56;'>📅 កាលបរិច្ឆេទមានប្រសិទ្ធភាព:</b> <span style="color: #FF6347;">{row['EFFDT_Year']}-2025</span></p>
    #                 <p style="font-size: 18px;"><b style='color:#694a56;'>📖 បរិយាយ:</b> <span style="color: #858585;">{row['DESCRLONG_KHM']}</span></p>
    #                 {province_text}
    #                 {ministry_text}
    #             </div>
    #             """
                
    #             # Ensure HTML content is safe and rendered properly
    #             st.markdown(card_html, unsafe_allow_html=True)
    # Loop through the three columns and display results
for i, col_df in enumerate([col1_df, col2_df, col3_df]):
    with cols[i]:
        for _, row in col_df.iterrows():
            # Ensure values are properly handled, ensuring no NaN values or empty strings
            ministry = str(row['នៅក្រោមក្រសួង']).strip() if pd.notna(row['នៅក្រោមក្រសួង']) else None
            province = str(row['រដ្ឋបាលខេត្ត']).strip() if pd.notna(row['រដ្ឋបាលខេត្ត']) else None

            # Prepare HTML content, ensuring we don't include empty fields
            ministry_text = (
                f"<p style='font-size: 16px;'><b style='color:#28a745;'>🏛 ស្ថិតនៅក្រោមក្រសួង:</b> {ministry}</p>"
                if ministry else ""  # Only add if ministry is not empty or None
            )

            province_text = (
                f"<p style='font-size: 16px;'><b style='color:#28a745;'>🌍 ស្ថិតនៅក្រោមរដ្ឋបាលខេត្ត:</b> {province}</p>"
                if province else ""  # Only add if province is not empty or None
            )

            # Create the HTML card with all the dynamic content
            card_html = f"""
            <div style="border: 1px solid #ddd; border-radius: 10px; padding: 20px; margin-bottom: 20px; background-color: #f9f9f9; height: 260px; overflow-y: auto;">
                <h4 style="color: #1f2937; font-size: 22px; height: 50px; overflow: hidden; text-overflow: ellipsis;">{row['OPERATING_UNIT']}</h4>
                <p style="font-size: 18px;"><b style='color:#694a56;'>📅 កាលបរិច្ឆេទមានប្រសិទ្ធភាព:</b> <span style="color: #FF6347;">{row['EFFDT_Year']}-2025</span></p>
                <p style="font-size: 18px;"><b style='color:#694a56;'>📖 បរិយាយ:</b> <span style="color: #858585;">{row['DESCRLONG_KHM']}</span></p>
                {province_text}  <!-- Only if province is not None or empty -->
                {ministry_text}  <!-- Only if ministry is not None or empty -->
            </div>
            """

            # Make sure HTML content is safe to render
            st.markdown(card_html, unsafe_allow_html=True)

else:
    st.info("No data found for the selected year and search criteria.")
