import os

# Folder structure
folders = [
    "ds_Roopendra/csv_files",
    "ds_Roopendra/outputs"
]

files = [
    "ds_Roopendra/notebook_1.ipynb",
    "ds_Roopendra/notebook_2.ipynb",
    "ds_Roopendra/csv_files/raw_trader_data.csv",
    "ds_Roopendra/csv_files/fear_greed.csv",
    "ds_Roopendra/csv_files/processed_data.csv",
    "ds_Roopendra/outputs/sentiment_trends.png",
    "ds_Roopendra/outputs/pnl_vs_sentiment.png",
    "ds_Roopendra/outputs/leverage_heatmap.png",
    "ds_Roopendra/ds_report.pdf",
    "ds_Roopendra/README.md"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create empty files
for file in files:
    open(file, 'a').close()

