import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.sidebar.title("Dashboard Controls")

country = st.sidebar.selectbox(
    "Select Country",
    countries
    format_func=lambda x: x.upper()
)

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
page_title="Global Economic Stress Dashboard",
page_icon="📊",
layout="wide"
)

# --------------------------------------------------
# Title & Description
# --------------------------------------------------
st.title("🌍 Global Economic Stress Prediction Dashboard")

st.info("Interactive dashboard for monitoring global recession risk using macroeconomic indicators.")

st.markdown("""
This dashboard predicts **economic stress / recession probability**
across major economies using machine learning models trained on
macroeconomic indicators.
""")

# --------------------------------------------------
# Load Data
# --------------------------------------------------
@st.cache_data
def load_data():
df = pd.read_csv("data/global_recession_probabilities.csv")
df["date"] = pd.to_datetime(df["date"])
return df

df = load_data()

countries = ["usa", "uk", "india", "japan", "germany"]

# --------------------------------------------------
# KPI Metrics
# --------------------------------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Countries Modelled", len(countries))
col2.metric("Total Data Points", len(df))
col3.metric("Model Type", "Logistic Regression")

st.markdown("---")

st.subheader("Global Economic Stress Indicator")

latest = df.iloc[-1]

global_risk = latest[countries].mean()

if global_risk > 0.6:
    st.error(f"⚠️ Global Stress Level: HIGH ({global_risk:.2f})")

elif global_risk > 0.4:
    st.warning(f"⚠️ Global Stress Level: MODERATE ({global_risk:.2f})")

else:
    st.success(f"✅ Global Stress Level: LOW ({global_risk:.2f})")

# --------------------------------------------------
# Country Selector
# --------------------------------------------------
country = st.selectbox(
"Select Country",
countries,
format_func=lambda x: x.upper()
)

# --------------------------------------------------
# Country Recession Probability
# --------------------------------------------------
st.subheader(f"Recession Probability Trend: {country.upper()}")

fig = px.line(
    df,
    x="date",
    y=country,
    title=f"{country.upper()} Economic Stress Probability",
)

st.plotly_chart(fig, use_container_width=True)

# --------------------------------------------------
# Latest Probabilities Table
# --------------------------------------------------
st.subheader("Latest Recession Probabilities")

latest = df.iloc[-1]

latest_df = pd.DataFrame({
"Country": [c.upper() for c in countries],
"Probability": [latest[c] for c in countries]
})

st.dataframe(latest_df, use_container_width=True)

# --------------------------------------------------
# Global Comparison Chart
# --------------------------------------------------
st.subheader("Global Recession Probability Comparison")

df_long = df.melt(
    id_vars="date",
    value_vars=countries,
    var_name="Country",
    value_name="Probability"
)

fig2 = px.line(
    df_long,
    x="date",
    y="Probability",
    color="Country",
    title="Global Recession Probability Comparison"
)

st.plotly_chart(fig2, use_container_width=True)

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("---")
st.caption(
"Global Economic Stress MLOps Pipeline | "
"Machine Learning + Macroeconomic Data + Interactive Dashboard"
)
