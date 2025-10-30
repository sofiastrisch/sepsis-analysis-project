# Sepsis Analysis Project

This project analyzes sepsis patterns and patient outcomes using a de-identified hospital dataset.  
It includes Python scripts for data cleaning, sepsis prediction, pathway analysis, and visualization.

## Overview
The goal of this project is to explore sepsis patient data, clean and aggregate it, analyze outcomes, and visualize trends such as sepsis incidence, severity, and prediction performance.

## Folder Structure
sepsis-analysis-project/
├── data/
├── scripts/
├── visualizations/
└── README.md

## Data Files
All CSV files are **de-identified**. Large files are tracked with **Git LFS**.

| File | Description | GitHub Link |
|------|------------|-------------|
| `sepsis_project_clean_aggregated.csv` | Cleaned and aggregated sepsis patient data | [View CSV](https://github.com/sofiastrisch/sepsis-analysis-project/blob/main/data/sepsis_project_clean_aggregated.csv) |
| `prediction_of_sepsis.csv` | Output predictions of sepsis from interactive model | [View CSV](https://github.com/sofiastrisch/sepsis-analysis-project/blob/main/data/prediction_of_sepsis.csv) |

## Scripts
| Script | Description | GitHub Link |
|--------|------------|-------------|
| `sepsis_cleaning.py` | Cleans and processes raw sepsis data | [View Script](https://github.com/sofiastrisch/sepsis-analysis-project/blob/main/scripts/sepsis_cleaning.py) |
| `interactive_sepsis.py` | Runs interactive sepsis detection on patient data | [View Script](https://github.com/sofiastrisch/sepsis-analysis-project/blob/main/scripts/interactive_sepsis.py) |
| `sepsis_pathway_analysis.py` | Analyzes patient pathways and outcomes | [View Script](https://github.com/sofiastrisch/sepsis-analysis-project/blob/main/scripts/sepsis_pathway_analysis.py) |
| `sepsis_analysis_bar_graph.py` | Generates bar graph visualizations for sepsis outcomes | [View Script](https://github.com/sofiastrisch/sepsis-analysis-project/blob/main/scripts/sepsis_analysis_bar_graph.py) |

## Visualizations
| Figure | Description | GitHub Link |
|--------|------------|-------------|
| `Figure_1.png` | Visualizes patient outcomes, incidence, or severity | [View PNG](https://github.com/sofiastrisch/sepsis-analysis-project/blob/main/visualizations/Figure_1.png) |

## How to Reproduce
1. Clone the repository:
git clone https://github.com/sofiastrisch/sepsis-analysis-project.git
cd sepsis-analysis-project

2. Install required Python packages (Python 3.6+ recommended).  
3. Run scripts in the `scripts/` folder to reproduce cleaning, prediction, and analysis.  
4. Visualizations are saved in `visualizations/` as PNG files.  

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
**Sofia Strisch**  
Toronto, Canada  
Registered Nurse | Data & Health Analytics Enthusiast
