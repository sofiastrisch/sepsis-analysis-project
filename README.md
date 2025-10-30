# Sepsis Analysis Project

This project analyzes sepsis trends, patient risk factors, and outcomes using a de-identified hospital dataset. It includes Python scripts for data cleaning, prediction, and pathway analysis, as well as visualizations of key insights.

## Repository Structure

sepsis-analysis-project/
    data/
        sepsis_project_clean_aggregated.csv
        prediction_of_sepsis.csv
    scripts/
        interactive_sepsis.py
        sepsis_analysis_bar_graph.py
        sepsis_cleaning.py
        sepsis_pathway_analysis.py
    visualizations/
        sepsis_bar_graph.png
    .gitattributes
    README.md

## Overview

- Load and clean the aggregated sepsis dataset.
- Run predictive analyses to identify patients at risk of sepsis.
- Visualize trends and outcomes using bar graphs and pathway analysis.

## Scripts

| Script | Description | File |
|--------|-------------|------|
| Interactive Sepsis | Interactive script for exploring sepsis predictions | [scripts/interactive_sepsis.py](scripts/interactive_sepsis.py) |
| Data Cleaning | Cleans and aggregates the raw sepsis dataset | [scripts/sepsis_cleaning.py](scripts/sepsis_cleaning.py) |
| Pathway Analysis | Analyzes sepsis patient pathways and outcomes | [scripts/sepsis_pathway_analysis.py](scripts/sepsis_pathway_analysis.py) |
| Bar Graph Analysis | Generates bar graphs for key sepsis metrics | [scripts/sepsis_analysis_bar_graph.py](scripts/sepsis_analysis_bar_graph.py) |

## Data

| File | Description |
|------|-------------|
| sepsis_project_clean_aggregated.csv | Cleaned and aggregated sepsis dataset (large file tracked via Git LFS) |
| prediction_of_sepsis.csv | Prediction outputs from interactive analysis (tracked via Git LFS) |

## Visualizations

| Figure | Description | File |
|--------|-------------|------|
| Sepsis Bar Graph | Bar graph showing sepsis outcomes by patient group | [visualizations/sepsis_bar_graph.png](visualizations/sepsis_bar_graph.png) |

## How to Run

1. Install required Python packages (Python 3.6+ recommended).
2. Run scripts in the `scripts/` folder to reproduce cleaning, prediction, and analysis.
3. Visualizations are saved in `visualizations/` as PNG files.

## Key Insights

- Aggregated patient data allows for more accurate analysis of sepsis trends.
- Visualization highlights high-risk patient groups and critical time windows.
- Predictive modeling can help anticipate sepsis development in hospital settings.

## Skills Demonstrated

- Python scripting and data cleaning
- Data aggregation and exploratory data analysis
- Sepsis pathway and outcome analysis
- Data visualization (bar graphs)
- Working with large datasets using Git LFS

## Author

Sofia Strisch  
Toronto, Canada  
Registered Nurse | Data & Health Analytics Enthusiast
