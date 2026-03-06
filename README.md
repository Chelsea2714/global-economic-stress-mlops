## 🌍 Global Economic Stress ML Pipeline

This project builds a machine learning pipeline to detect early signals of economic recession using macroeconomic indicators.

The system processes macroeconomic data, engineers time-series features, trains a classification model, and evaluates recession prediction performance.

The architecture is designed to be scalable across multiple countries, enabling global economic stress monitoring.

## 📊 Indicators Used

The model uses macroeconomic indicators commonly associated with economic cycles:
- GDP Growth
- Inflation
- Unemployment Rate
- Yield Spread (10Y bond − 3M treasury)
- Lagged macroeconomic features

These indicators are widely used in macroeconomic recession forecasting.

## ⚙️ Project Pipeline

The pipeline follows a modular ML engineering structure.

Raw Data → Data Cleaning → Feature Engineering → Model Training → Evaluation → Saved Model

Main components:

| **Module**             | **Purpose**               |
|------------------------|---------------------------|
| data_pipeline.py       | Data cleaning + merging   |
| feature_engineering.py | Lag feature creation      |
| train_model.py         | Model training            |
| evaluate.py            | Model performance metrics |
| main.py                | Runs full pipeline        |

## 🗂 Project Structure

global-economic-stress-mlops
│
├── data
│   ├── raw
│   │   ├── usa
│   │   ├── uk
│   │   ├── india
│   │   └── japan
│   │
│   └── processed
│
├── models
│
├── src
│   ├── data_pipeline.py
│   ├── feature_engineering.py
│   ├── train_model.py
│   └── evaluate.py
│
├── main.py
└── README.md

## 🇺🇸🇬🇧 Phase 2: Multi-Country Integration

The pipeline now supports multiple countries.

Currently supported:
- USA
- UK

Each country has:
- Separate raw datasets
- Independent feature engineering
- Country-specific trained models

Example output:

models/
├── logistic_model_usa.pkl
└── logistic_model_uk.pkl

## 📈 Model Performance
USA

ROC-AUC ≈ 0.96

| **Metric**         | **Value** |
|--------------------|-----------|
| Accuracy           | ~0.82     |
| Recall (Recession) | 1.0       |

UK

ROC-AUC ≈ 0.97

Metric	Value

| **Metric**         | **Value** |
|--------------------|-----------|
| Accuracy           | ~0.84     |
| Recall (Recession) | 1.0       |

## 🚀 Running the Pipeline

Run the full pipeline:

python3 main.py

This will:

1. Run the data pipeline
2. Generate features
3. Train recession models
4. Evaluate performance
5. Save models

## 🧠 Phase Roadmap

|                  **Phase**                  | **Status** |
|:-------------------------------------------:|:----------:|
| Phase 1 — USA recession model               | ✅ Complete |
| Phase 2 — Multi-country pipeline (USA + UK) | ✅ Complete |
| Phase 3 — Add India, Japan, Germany         | 🔜 Next     |
| Phase 4 — Global recession risk dashboard   | Planned    |
| Phase 5 — Real-time data pipeline           | Planned    |

## 📊 Data Source

Macroeconomic data sourced from:

Federal Reserve Economic Data (FRED)

https://fred.stlouisfed.org/

## 🎯 Goal

The long-term goal is to build a global economic stress monitoring system that can:
- detect early recession signals
- compare economic stress across countries
- support policy and investment insights