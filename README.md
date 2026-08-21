# Week 2 – Advanced Data Visualization and Storytelling with Python


## Overview
This project builds a data-driven visual narrative using the World 
Happiness Report dataset, moving beyond simple charts to tell a coherent 
story about what drives national happiness — designed to communicate 
complex, multi-dimensional data to a non-technical audience.

## Dataset
World Happiness Report — 153 countries, ranked by Happiness Score with six 
contributing factors: GDP per capita, social support, health, freedom, 
generosity, and perceived corruption.

## What Was Done
- **Ranking**: Identified the happiest and least happy countries.
- **Regional comparison**: Compared happiness distributions across world regions.
- **Relationship analysis**: Explored GDP vs. happiness, with life expectancy as a third dimension.
- **Correlation analysis**: Quantified which factors most strongly predict happiness.
- **Decomposition**: Broke down the top 10 countries' scores into individual factor contributions.

Six visualizations were built using Python (Matplotlib, Seaborn), each 
chosen deliberately for the specific part of the story it needed to tell, 
with written justification for every chart type.

## Key Insights
- GDP, Job Satisfaction, and Health are the strongest predictors of 
  happiness (all r > 0.75).
- Generosity is only weakly correlated with happiness (r = 0.16) — a 
  genuinely counter-intuitive finding.
- The gap between the happiest and least happy regions is roughly 3 points 
  on a 10-point scale.
- No single factor fully explains happiness — top countries reach high 
  scores through different combinations of drivers.

## Business & Scientific Implications
Findings are connected to real-world relevance across public policy 
(social support investment), corporate HR (employee wellbeing), and market 
research (using regional happiness as a proxy for market stability).

## Files
| File | Description |
|---|---|
| `Week2_Data_Storytelling_Report.docx` | Full report with methodology, code, and visualizations |
| `week2_analysis.py` | Python script for analysis and chart generation |
| `happiness.csv` | Raw dataset used for analysis |

## Tools Used
Python, Pandas, NumPy, Matplotlib, Seaborn
