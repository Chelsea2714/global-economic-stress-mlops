import streamlit as st
import pandas as pd
import plotly.express as px
from fredapi import Fred

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Global Economic Stress Dashboard",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# Title
# --------------------------------------------------
st.title("🌍 Global Economic Stress Prediction Dashboard")

st.markdown(
"""
This dashboard monitors **global recession probability** using
macroeconomic indicators and machine learning predictions.
"""
)

# --------------------------------------------------
# Load Data
# --------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/macro_data.csv")
    df["date"] = pd.to_datetime(df["date"])
    return df

df = load_data()

countries = ["usa", "uk", "india", "japan", "germany"]

# --------------------------------------------------
# Sidebar Controls
# --------------------------------------------------
st.sidebar.title("Dashboard Controls")

country = st.sidebar.selectbox(
    "Select Country",
    countries,
    format_func=lambda x: x.upper()
)

# --------------------------------------------------
# KPI Metrics
# --------------------------------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Countries Modelled", len(countries))
col2.metric("Total Observations", len(df))
col3.metric("Model Used", "Logistic Regression")

st.markdown("---")

# --------------------------------------------------
# Global Risk Indicator
# --------------------------------------------------
latest = df.iloc[-1]
global_risk = latest[countries].mean()

st.subheader("🌐 Global Economic Stress Indicator")

if global_risk > 0.6:
    st.error(f"⚠️ Global Stress Level: HIGH ({global_risk:.2f})")
elif global_risk > 0.4:
    st.warning(f"⚠️ Global Stress Level: MODERATE ({global_risk:.2f})")
else:
    st.success(f"✅ Global Stress Level: LOW ({global_risk:.2f})")

# --------------------------------------------------
# Country Trend Chart
# --------------------------------------------------
st.subheader(f"📈 Recession Probability Trend — {country.upper()}")

fig = px.line(
    df,
    x="date",
    y=country,
    markers=True,
    title=f"{country.upper()} Economic Stress Probability"
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Probability",
    template="plotly_white"
)

st.plotly_chart(fig, use_container_width=True)

# --------------------------------------------------
# Latest Probabilities Table
# --------------------------------------------------
st.subheader("📊 Latest Country Risk Levels")

latest_df = pd.DataFrame({
    "Country": [c.upper() for c in countries],
    "Recession Probability": [latest[c] for c in countries]
})

latest_df = latest_df.sort_values(
    by="Recession Probability",
    ascending=False
)

st.dataframe(latest_df, use_container_width=True)

# --------------------------------------------------
# Global Risk Bar Chart
# --------------------------------------------------

fig3 = px.bar(
    latest_df,
    x="Country",
    y="Recession Probability",
    title="Latest Recession Risk by Country",
    color="Recession Probability",
)

st.plotly_chart(fig3, use_container_width=True)

# --------------------------------------------------
# Global Comparison Chart
# --------------------------------------------------
st.subheader("🌎 Global Recession Probability Comparison")

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
    title="Economic Stress Comparison Across Countries"
)

fig2.update_layout(
    template="plotly_white",
    xaxis_title="Date",
    yaxis_title="Probability"
)

st.plotly_chart(fig2, use_container_width=True)

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("---")

st.caption(
    "Global Economic Stress MLOps Pipeline | "
    "Machine Learning • Macroeconomic Indicators • Streamlit Dashboard"
)