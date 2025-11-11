import streamlit as st
import pandas as pd 

def Fund():
    st.markdown(
        """
        <h1 style="text-align: center; color: #1f2937; font-size: 40px; font-weight: bold; padding: 10px;">
           មូលនិធិ
        </h1>
        """,
        unsafe_allow_html=True,
    )

    # Create layout columns
    col1, col2, col3, col4 = st.columns([30, 5, 5, 2])

    # Text search
    with col1:
        text_search = st.text_input("និយមន័យពី ទិន្នន័យមេ ​​ស្វែងយល់បន្ថែម", value="")

    # # Year selection
    # with col2:
    #     options = ("2000", "2023", "2024", "2025")
    #     option = st.selectbox("ឆ្នាំ", options, index=options.index("2025"))

    # Status selection
    with col2:
        status_options = ("Active", "Inactive")
        selected_status = st.selectbox("ស្ថានភាព", status_options, index=0)

    # Load Excel file
    file_path = "Excel files/fund_df_merged.xlsx"
    df = pd.read_excel(file_path, dtype=str).fillna("")
    #df = df[['FUND_CODE', 'Len', 'EFFDT', 'EFFDT_Year', 'EFF_STATUS', 'DESCRLONG_ENG', 'នៅក្រោមខេត្ត']]

    # Convert date fields
    # df['EFFDT'] = pd.to_datetime(df['EFFDT'], errors='coerce')
    # df['Effective_date'] = df['EFFDT_Year'].astype(str) + '-2025'

    df['EFF_STATUS'] = df['EFF_STATUS'].map({'A': 'Active', 'I': 'Inactive'})

    # df[['Start_Year', 'End_Year']] = df['Effective_date'].str.split('-', expand=True)
    # df['Start_Year'] = df['Start_Year'].astype(int)
    # df['End_Year'] = df['End_Year'].astype(int)

    # selected_year = int(option)

    # Filter by year and status
    # filtered_df = df[(df['Start_Year'] <= selected_year) & (df['End_Year'] >= selected_year)]
    filtered_df = df[df['EFF_STATUS'] == selected_status]

    # Filter by search text
    if text_search:
        mask1 = filtered_df["DESCRLONG_ENG"].str.contains(text_search, case=False, na=False)
        mask2 = filtered_df["FUND_CODE"].str.contains(text_search, case=False, na=False)
        filtered_df = filtered_df[mask1 | mask2]

    # Display filtered results
    st.subheader("Filtered Results")
    filtered_df = filtered_df.head(12)

    if not filtered_df.empty:
        num_cards = len(filtered_df)
        cards_per_col = (num_cards + 2) // 3

        col1_df = filtered_df.iloc[:cards_per_col]
        col2_df = filtered_df.iloc[cards_per_col:2*cards_per_col]
        col3_df = filtered_df.iloc[2*cards_per_col:]

        cols = st.columns(3)

        for i, col_df in enumerate([col1_df, col2_df, col3_df]):
            with cols[i]:
                for _, row in col_df.iterrows():
                    province = str(row['នៅក្រោមខេត្ត']).strip() if pd.notna(row['នៅក្រោមខេត្ត']) else None
                    province_text = (
                        f"<p style='font-size: 16px;'><b style='color:#28a745;'>🏛 ស្ថិតនៅក្រោមមូលនិធិ:</b> {province}</p>"
                        if province else ""
                    )

                    card_html = f"""
                    <div style="border: 1px solid #ddd; border-radius: 10px; padding: 20px; margin-bottom: 20px; background-color: #f9f9f9; height: 280px; overflow-y: auto;">
                        <h4 style="color: #1f2937; font-size: 22px; height: 50px; overflow: hidden; text-overflow: ellipsis;">{row['FUND_CODE']}</h4>
                        <p style="font-size: 18px;"><b style='color:#694a56;'>📖 បរិយាយ:</b> <span style="color: #858585;">{row['DESCRLONG_ENG']}</span></p>
                        <p style="font-size: 18px;"><b style='color:#694a56;'>ស្ថានភាព:</b> <span style="color:#694a56;">{row['EFF_STATUS']}</span></p>
                        {province_text}
                    </div>
                    """

                    st.markdown(card_html, unsafe_allow_html=True)
    else:
        st.info("No data found for the selected year and search criteria.")
