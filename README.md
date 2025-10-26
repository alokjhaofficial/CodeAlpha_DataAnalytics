# CodeAlpha — Netflix EDA & Visualization

A beginner‑friendly data analytics project completing Task 2 (Exploratory Data Analysis) and Task 3 (Data Visualization) from the CodeAlpha internship.  

## Overview
This project explores Netflix Movies & TV Shows metadata to understand content mix, release trends, maturity ratings, and geographic distribution, with clear visual summaries suitable for a portfolio.  

## Tasks Covered
- Task 2: Exploratory Data Analysis (EDA) — data understanding, cleaning, trend/pattern discovery, anomaly checks, and statistical summaries.  
- Task 3: Data Visualization — multiple charts and a dashboard that communicate insights for non‑technical readers.  

## Dataset
- Source: Kaggle “Netflix Movies and TV Shows” dataset by Shivam Bansal (commonly used community dataset).  
- Typical fields: type, title, director, cast, country, date_added, release_year, rating, duration, listed_in (genres), description.  
- Download page: Search “Kaggle Netflix Movies and TV Shows (shivamb)” and download the CSV, then place it in this repository’s root as `netflix_titles.csv`.  

## Environment
- Python 3.8+  
- Libraries: pandas, numpy, matplotlib, seaborn (install with `pip install pandas numpy matplotlib seaborn`)  
- Optional: VS Code (Python & Jupyter extensions) or Jupyter Notebook  

## How to Run
1. Clone or download this repository.  
2. Place `netflix_titles.csv` in the project folder.  
3. Option A (Notebook): open `Task_2_EDA.ipynb` and run all cells.  
4. Option B (Script, VS Code): run `task2_eda.py` (Ctrl+F5) and then `task3_visualization.py`.  
5. Images will export automatically, for example:  
   - `eda_dashboard.png`  
   - `visualization_dashboard.png`  

## Key Findings (from EDA)
- Movies outnumber TV shows in the catalog.  
- Releases are heavily skewed toward post‑2010 titles, reflecting rapid growth in the 2010s.  
- TV‑MA and TV‑14 dominate maturity ratings.  
- The United States contributes the largest share of titles, with notable contributions from India and the UK.  
- Basic data cleaning is needed (missing values in director/country and multi‑value text fields like genres).  

## Visualizations
- Distribution of release years  
- Movie vs TV show counts (bar/pie)  
- Top producing countries (bar)  
- Ratings distribution (bar)  
- Optional: titles added per year using `date_added` (line)  
- Correlation heatmap for numeric columns (when available)  

## Project Structure
