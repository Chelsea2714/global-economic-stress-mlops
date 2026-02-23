## Global Economic Stress — USA Recession Prediction

## Overview
This project builds a forward-tested macroeconomic recession prediction model using U.S. quarterly data.
The model predicts recession probability using:
- GDP Growth
- Inflation
- Debt-to-GDP
- Interest Rate
- Unemployment
- Yield Curve Spread (10Y − 3M)
Data sourced from the Federal Reserve Economic Data (FRED).

## Methodology
1. Monthly macro data converted to quarterly frequency
2. Yield spread engineered from 10-year and 3-month Treasury rates
3. 1-quarter lag features added
4. Time-aware split (Train: pre-2018, Test: 2018+)
5. Logistic Regression with class balancing
6. Custom probability threshold (0.3) for recession detection

## Results (Forward Test 2018+)
- ROC-AUC: ~0.96
- Recession Recall: 1.00
- Accuracy: ~0.93

## Project Structure
- data_pipeline.py — Data cleaning and merging
- feature_engineering.py — Lag feature creation
- train_model.py — Model training and evaluation
- evaluate.py — Visualization
- main.py — End-to-end pipeline

## Future Work
- Extend to global economies
- Compare yield curve effectiveness across countries
- Rolling window backtesting
- Country-specific macro sensitivity analysis