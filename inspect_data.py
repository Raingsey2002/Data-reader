import pandas as pd
import glob
import os
import json

DATA_DIR = r"d:\my-tech-project\fmis-report-query-dashboard\fmis-report\Data-reader\Excel files\report-data"
MASTERS_FILE = os.path.join(DATA_DIR, "masters.json")

# Load Masters
with open(MASTERS_FILE, 'r', encoding='utf-8') as f:
    masters = json.load(f)

print("Masters Report Types Sample:", masters['reportTypes'][:5])
print("Masters Query Types Sample:", masters['queryTypes'][:5])

# Load Excel
excel_files = glob.glob(os.path.join(DATA_DIR, "main_data_*.xlsx"))
if excel_files:
    df = pd.read_excel(excel_files[0], dtype=str)
    print("\nColumns:", df.columns.tolist())
    
    if "Report/Query" in df.columns:
        print("\n'Report/Query' Sample (mapped to code):")
        print(df["Report/Query"].head(5).tolist())

    if "Name of Report and Query" in df.columns:
        print("\n'Name of Report and Query' Sample (mapped to name):")
        print(df["Name of Report and Query"].head(5).tolist())
else:
    print("No excel files found")
