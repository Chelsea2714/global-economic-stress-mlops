import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Global Economic Stress Dashboard")

st.write(
"""
This dashboard visualizes recession probabilities across major global economies
predicted using macroeconomic indicators such as GDP growth, inflation,
unemployment, and yield curve spread.
"""
)

# Load probability data
df = pd.read_csv("data/global_recession_probabilities.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

countries = ["usa", "uk", "india", "japan", "germany"]

country = st.selectbox("Select Country", countries)

st.subheader(f"Recession Probability: {country.upper()}")

fig, ax = plt.subplots()

ax.plot(df["date"], df[country])
ax.set_ylabel("Recession Probability")
ax.set_xlabel("Date")

st.pyplot(fig)

st.subheader("Latest Probabilities")

latest = df.iloc[-1]

latest_df = pd.DataFrame({
    "Country": countries,
    "Probability": [latest[c] for c in countries]
})

st.dataframe(latest_df)

st.subheader("Global Recession Probability Comparison")

fig2, ax2 = plt.subplots()

for c in countries:
    ax2.plot(df["date"], df[c], label=c.upper())

ax2.legend()

st.pyplot(fig2)