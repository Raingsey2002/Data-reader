import pandas as pd
import os

base_dir = "Excel files"
files_to_check = [
    "Function_df_merged.xlsx",
    "fund_df_merged.xlsx",
    "Program_df_merged.parquet",
    "Economic_df_merged.parquet"
]

for file_name in files_to_check:
    file_path = os.path.join(base_dir, file_name)
    print(f"\n--- Checking {file_name} ---")
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        continue
        
    try:
        if file_name.endswith(".parquet"):
            df = pd.read_parquet(file_path)
        else:
            df = pd.read_excel(file_path)
            
        print("Columns:", df.columns.tolist())
        print("First 2 rows:")
        print(df.head(2).to_string())
    except Exception as e:
        print(f"Error reading {file_name}: {e}")
