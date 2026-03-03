import streamlit as st

# Set page layout to wide mode (must be the first Streamlit command)
st.set_page_config(
       page_title="My Dashboard",
    page_icon="📊",
    layout="wide"
    )
import base64

# Read and encode image
file_path = "Screenshot_2025-09-02_at_3.58.31_in_the_afternoon-removebg-preview.png"
with open(file_path, "rb") as f:
    data = f.read()
encoded = base64.b64encode(data).decode()

import pandas as pd

from user_Alias import show as UserAlias
from Fmis_Entity  import FmisEntity 
from Geography_page import Geography
from Project_Page  import Project
from Function_page import Functionpage
from Fund_page import Fund
from Economic_page import Economic
from program_page import Program
from Report_page import Report
from Supplier_page import Supplier
from  Monitoring_dashboard_page import Monitoring
from Overview import Overview_page

#st.sidebar.image("Screenshot 2025-09-02 at 3.58.31 in the afternoon.png",)



# Inject Google Fonts (Noto Sans Khmer) and apply global font styles
st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Khmer&display=swap" rel="stylesheet">
    <style>
    html, body, [class*="css"] {
        font-family: 'Noto Sans Khmer', Arial, sans-serif !important;
        color: #1f2937;
    }
    h1, h4, p, span, b {
        font-family: 'Noto Sans Khmer', Arial, sans-serif !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# Define your pages
def data_reader_page():
    
    st.markdown("""
        <style>
            .block-container {
                padding-top: 1rem;
                padding-bottom: 3rem;
            }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown(
        """
        <h1 style="text-align: center; color: #1f2937; font-size: 40px; font-weight: bold; padding: 10px font-family: 'Noto Sans Khmer', Arial, sans-serif;">
            អង្គភាពប្រតិបត្តិ និងរដ្ឋបាល
        </h1>
        """,
        unsafe_allow_html=True,
    )

     # File path for your Parquet file
    file_path = "Excel files/OU_df_merged.parquet"

    # Read the Parquet file into a dataframe
    df = pd.read_parquet(file_path).astype(str).fillna("")
    # df = pd.read_parquet(file_path)
    df = df[['OPERATING_UNIT', 'Len', 'EFFDT', 'EFFDT_Year', 'EFF_STATUS', 'DESCRLONG_KHM', 'នៅក្រោមក្រសួង', 'រដ្ឋបាលខេត្ត','DESCRSHORT_ENG']]


    # Create three columns for layout
    col1, col2, col3, col4 = st.columns([20, 5, 5, 5])


    # Place the text input in the first column
    with col1:
        text_search = st.text_input("និយមន័យពី ទិន្នន័យមេ ​​ស្វែងយល់បន្ថែម", value="")

    # Place the selectbox in the second column
    # with col3:
    #     options = ("2000" ,"2023", "2024", "2025")  # Only show the specified years
    #     option = st.selectbox(
    #         "ឆ្នាំ",
    #         options,
    #         index=options.index("2025"),  # Set default to '2025'
    #         placeholder="Select year...",
    #     )
    # with col3:
    # # Extract unique years from dataframe and sort them
    #     options = sorted(df['EFFDT_Year'].astype(str).unique())

    #     option = st.selectbox(
    #         "ឆ្នាំ",
    #         options,
    #         index=options.index("2025") if "2025" in options else 0,  # Default to 2025 if available
    #         placeholder="Select year...",
    #     )

    # ✅ Modified: Year selectbox with "All" option
    with col3:
        year_options = sorted(df['EFFDT_Year'].astype(str).unique())
        options = ["All"] + year_options  

        option = st.selectbox(
            "ឆ្នាំ",
            options,
            index= 0,  # Default to 2025 if available
            placeholder="Select year...",
        )

    # Place the selectbox for status in the third column
    with col4:
        status_options = ("Active", "Inactive")
        selected_status = st.selectbox("ស្ថានភាព", status_options, index=0)  # Default to 'Active'
    
    # New selectbox for choosing year type
    with col2:
        year_type_options = ("ឆ្នាំបង្កើត​​", "ឆ្នាំប្រសិទ្ធភាព")
        selected_year_type = st.selectbox("ប្រភេទឆ្នាំ", year_type_options, index=1)



   
    # Convert 'EFFDT' to datetime and extract the year
    df['EFFDT'] = pd.to_datetime(df['EFFDT'], errors='coerce')
    df['Effective_date'] = df['EFFDT_Year'].astype(str) + '-2025'

    # Convert 'EFF_STATUS' to Active and Inactive
    df['EFF_STATUS'] = df['EFF_STATUS'].map({'A': 'Active', 'I': 'Inactive'})

    # Ensure 'EFFDT_Year' is in 'YYYY-YYYY' format
    df[['Start_Year', 'End_Year']] = df['Effective_date'].str.split('-', expand=True)
    df['Start_Year'] = df['Start_Year'].astype(int)
    df['End_Year'] = df['End_Year'].astype(int)

    # # Convert selected year to integer
    # selected_year = int(option)

    # # # Step 1: Filter the dataframe based on the selected year range
    # # filtered_df = df[(df['Start_Year'] <= selected_year) & (df['End_Year'] >= selected_year)]
    # filtered_df = df[df['EFFDT_Year'].astype(int) == selected_year]
    # ✅ Handle filtering with "All"
    if option != "All":
        selected_year = int(option)
        filtered_df = df[df['EFFDT_Year'].astype(int) == selected_year]
    else:
        filtered_df = df.copy()


    # Filter by status
    filtered_df = filtered_df[filtered_df['EFF_STATUS'] == selected_status]

    # Step 2: Apply text search filter (only after filtering by year)
    if text_search:
        pattern = f"^{text_search}"
        mask1 = filtered_df["DESCRLONG_KHM"].str.contains(text_search, case=False, na=False)
        mask2 = filtered_df["OPERATING_UNIT"].str.match(pattern, case=False, na=False)
        mask3 = filtered_df["DESCRSHORT_ENG"].str.contains(text_search, case=False, na=False)
        filtered_df = filtered_df[mask1 | mask2 | mask3]



    # Display results in a three-column layout
    st.subheader("លទ្ធផល")

    filtered_df = filtered_df.head(12)
    
    if not filtered_df.empty:
        num_cards = len(filtered_df)
        cards_per_col = (num_cards + 2) // 3  # Ensure balanced columns

        col1_df = filtered_df.iloc[:cards_per_col]
        col2_df = filtered_df.iloc[cards_per_col:2*cards_per_col]
        col3_df = filtered_df.iloc[2*cards_per_col:]

        cols = st.columns(3)
        
        # Loop through the three columns and display results
        for i, col_df in enumerate([col1_df, col2_df, col3_df]):
            with cols[i]:
                for _, row in col_df.iterrows():
                    # Ensure values are properly handled, ensuring no NaN values or empty strings
                    ministry = str(row['នៅក្រោមក្រសួង']).strip() if pd.notna(row['នៅក្រោមក្រសួង']) else None
                    province = str(row['រដ្ឋបាលខេត្ត']).strip() if pd.notna(row['រដ្ឋបាលខេត្ត']) else None

                    # Dynamic year display
                    if selected_year_type == "ឆ្នាំបង្កើត​​":
                        year_display = f"{row['EFFDT_Year']}"
                        year_label = "📅 ឆ្នាំបង្កើត"
                    else:  # ឆ្នាំប្រសិទ្ធភាព
                        year_display = f"{row['EFFDT_Year']}-បច្ចុប្បន្ន"
                        year_label = "📅 កាលបរិច្ឆេទមានប្រសិទ្ធភាព"


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
                    <div style="border: 1px solid #ddd; border-radius: 10px; padding: 20px; margin-bottom: 20px; background-color: #f9f9f9; height: 260px; overflow-y: auto; font-family: 'Noto Sans Khmer', Arial, sans-serif;">
                        <h4 style="color: #1f2937; font-size: 22px; height: 50px; overflow: hidden; text-overflow: ellipsis;">{row['OPERATING_UNIT']}</h4>
                        <p style="font-size: 18px;"><b style='color:#694a56;'>{year_label}</b> <span style="color: #FF6347;">{year_display}</span></p>
                         <p style="font-size: 18px;"><b style='color:#694a56;'>📖 បរិយាយ:</b> <span style="color: #858585;">{row['DESCRLONG_KHM']}</span></p>
                        <p style="font-size: 18px;"><b style='color:#694a56;'> អក្សរកាត់:</b> <span style="color: #858585;">{row['DESCRSHORT_ENG']}</span></p>
                        <p style="font-size: 18px;"><b style='color:#694a56;'> ស្ថានភាព:</b> <span style="color:#694a56;">{row['EFF_STATUS']}</span></p>
                        {province_text}  <!-- Only if province is not None or empty -->
                        {ministry_text}  <!-- Only if ministry is not None or empty -->
                    </div>
                    """

                    # Make sure HTML content is safe to render
                    st.markdown(card_html, unsafe_allow_html=True)

    else:
        st.info("No data found for the selected year and search criteria.")

# pages = {
#     "App navigation": [
#         st.Page(FmisEntity, title="អង្គភាពការងារ"),
#         st.Page(data_reader_page, title="អង្គភាពប្រតិបត្តិ"),
#         st.Page(Economic,title="មាតិកាគណនី"),
#         st.Page(Program, title="កម្មវិធី"),
#         st.Page(Geography, title="ភូមិសាស្រ្ត"),
#         st.Page(UserAlias, title="អ្នកប្រើប្រាស់"),
#         st.Page(Report, title="របាយការណ៍"),


# Inject into CSS
st.markdown(
    f"""
    <style>
    section[data-testid="stSidebar"] > div:before {{
        content: "";
        display: block;
        background-image: url("data:image/png;base64,{encoded}");
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
        height: 100px;
        margin-top: 30px;
        margin-bottom: 15px;
    }}

    /* Move sidebar content slightly up */
    section[data-testid="stSidebar"] div.block-container {{
        margin-top: 100px;   /* adjust negative value to move content higher */
    }}

    </style>
    """,
    unsafe_allow_html=True,
)






# pages = [
#     st.Page(FmisEntity, title="🏛️  អង្គភាពការងារ"),
#     st.Page(data_reader_page, title="🏢  អង្គភាពប្រតិបត្តិ"),
#     st.Page(Economic, title="📊  មាតិកាគណនី"),
#     st.Page(Program, title="📋  កម្មវិធី"),
#     st.Page(Geography, title="🌍  ភូមិសាស្រ្ត"),
#     st.Page(UserAlias, title="👤  អ្នកប្រើប្រាស់"),
#     st.Page(Report, title="📘  របាយការណ៍"),
#         #st.Page(Project, title="គម្រោង"),
#         #st.Page(Functionpage, title="មុខងារ"),
#         #st.Page(Fund, title="មូលនិធិ"),
#      ]    



# pages = {
#         "ទិដ្ឋភាពទូទៅ": [ st.Page(Overview_page, title="ទិដ្ឋភាពទូទៅ")],    
        
#     "Monitoring": [
#         st.Page(Monitoring, title="📈  Monitoring Dashboard"),
#     ],
#     "មាតិកាគណនីនៃប្លង់គណនេយ្យ": [
#         st.Page(data_reader_page, title="🏢  អង្គភាពប្រតិបត្តិ និងរដ្ឋបាល"),
#         st.Page(Economic, title="📊  មាតិកាគណនី"),
#         st.Page(Program, title="📋  កម្មវិធី"),
#         st.Page(Geography, title="🌍  ភូមិសាស្រ្ត"),
#         st.Page(Project, title="📂  គម្រោង"),
#         st.Page(Functionpage, title="⚙️  មុខងារ"),
#         st.Page(Fund, title="💰  មូលនិធិ"),
        
#     ],
#     "ទិន្នន័យមេ": [
#          st.Page(FmisEntity, title="🏛️  អង្គភាពការងារ"),
#          st.Page(UserAlias, title="👤  អ្នកប្រើប្រាស់"),
#          st.Page(Report, title="📘  របាយការណ៍"),
#          st.Page(Supplier, title="🚚 អ្នកផ្គត់ផ្គង់"),

#     ],
# }   
        




# pg = st.navigation(pages)

# # Add sidebar content
# with st.sidebar:

#     st.markdown("**អំពី**")
#     st.markdown("រៀបចំ​ និងអភិវឌ្ឍដោយក្រុមការងារការិយាល័យគ្រប់គ្រងព័ត៌មាន")
#     st.markdown("ត្រូវការជំនួយ, សូមទាក់ទងមកកាន់មជ្ឈមណ្ឌលផ្ដល់ព័ត៌មានFMISតាមរយ:(+855)23 430 063 និងតាមបណ្ដាញផ្សេងៗ។")



# pg.run()




pages = {

    "Monitoring": [
        st.Page(Monitoring, title="📈 Monitoring Dashboard"),
    ],

    # "ទិដ្ឋភាពទូទៅ": [
    #     st.Page(Overview_page, title="ទិដ្ឋភាពទូទៅ", default=True)
    # ],

    "មាតិកាគណនីនៃប្លង់គណនេយ្យ": [
        st.Page(data_reader_page, title="🏢 អង្គភាពប្រតិបត្តិ និងរដ្ឋបាល"),
        st.Page(Economic, title="📊 មាតិកាគណនី"),
        st.Page(Program, title="📋 កម្មវិធី"),
        st.Page(Geography, title="🌍 ភូមិសាស្រ្ត"),
        st.Page(Project, title="📂 គម្រោង"),
        st.Page(Functionpage, title="⚙️ មុខងារ"),
        st.Page(Fund, title="💰 មូលនិធិ"),
    ],

    "ទិន្នន័យមេ": [
        st.Page(FmisEntity, title="🏛️ អង្គភាពការងារ"),
        st.Page(UserAlias, title="👤 អ្នកប្រើប្រាស់"),
        st.Page(Report, title="📘 របាយការណ៍"),
        st.Page(Supplier, title="🚚 អ្នកផ្គត់ផ្គង់"),
    ],
}

pg = st.navigation(pages)

with st.sidebar:
    st.markdown("**អំពី**")
    st.markdown("រៀបចំ និងអភិវឌ្ឍដោយក្រុមការងារការិយាល័យគ្រប់គ្រងព័ត៌មាន")
    st.markdown("ត្រូវការជំនួយ, សូមទាក់ទង FMIS (+855)23 430 063")

pg.run()
