import pandas as pd


def create_features(df):

    for col in ["gdp_growth", "inflation", "unemployment",
                "interest_rate", "debt_to_gdp", "yield_spread"]:

        df[f"{col}_lag1"] = df[col].shift(1)

    df = df.dropna().reset_index(drop=True)

    return df