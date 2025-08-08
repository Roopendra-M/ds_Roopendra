# Market Sentiment and Trading Performance Report

## Overview
This project analyzes trading performance in relation to market sentiment.
It uses Python for data cleaning and visualization, and LaTeX for report generation.

## Folder Structure

.
├── data/ # Raw and processed data files
├── outputs/ # Generated plots
│ ├── rolling_pnl_vs_sentiment.png
│ ├── pnl_vs_sentiment.png
│ └── sentiment_trading_heatmap.png
├── scripts/ # Python scripts for analysis
│ └── analysis.py
├── report.tex # LaTeX report file
└── README.md # This file


## Setup Instructions

### 1. Install Dependencies
```bash
pip install pandas matplotlib seaborn
```

##How to Run
1. Open `assignment.ipynb` in **Jupyter Notebook** or **JupyterLab**.
2. Run all cells from top to bottom.
3. Plots will be saved automatically in the `outputs/` folder.