import pandas as pd
import os
import glob

data_dir = r"d:\my-tech-project\fmis-report-query-dashboard\fmis-report\Data-reader\Excel files\report-data"
files = glob.glob(os.path.join(data_dir, "main_data_*.xlsx"))

if files:
    f = files[0]
    try:
        df = pd.read_excel(f, dtype=str)
        cols = df.columns.tolist()
        # Find column that looks like Report/Query
        target_col = next((c for c in cols if "Report" in c and "Query" in c), None)
        
        if target_col:
            uniques = df[target_col].dropna().unique().tolist()
            print(f"--- SAMPLE VALUES from '{target_col}' ---")
            for u in uniques[:20]:
                print(u)
        else:
            print("Target column not found")
            
    except Exception as e:
        print(f"Error: {e}")
