from fredapi import Fred
import pandas as pd

fred = Fred(api_key="73442ee2bbd9434e30e16e0041129666")

# Core indicators
unemployment = fred.get_series("UNRATE")
gdp = fred.get_series("GDP")
inflation = fred.get_series("CPIAUCSL")

# Step 6 indicators
interest_rate = fred.get_series("FEDFUNDS")

# Combine everything
df = pd.concat([
    unemployment,
    gdp,
    inflation,
    interest_rate,
], axis=1)

df.columns = [
    "unemployment",
    "gdp",
    "inflation",
    "interest_rate"
]

df = df.dropna()

df.to_csv("data/macro_data.csv")