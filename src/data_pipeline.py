import pandas as pd
import os


def clean_macro(df, value_name):
    df.columns = [col.strip() for col in df.columns]

    if "observation_date" in df.columns:
        df = df.rename(columns={"observation_date": "date"})
    else:
        df = df.rename(columns={df.columns[0]: "date"})

    df["date"] = pd.to_datetime(df["date"])
    value_col = df.columns[1]
    df = df.rename(columns={value_col: value_name})

    return df


def to_quarterly(df):
    df["date"] = df["date"].dt.to_period("Q").dt.start_time
    return df.groupby("date").mean().reset_index()


def annual_to_quarterly(df):
    df["date"] = pd.to_datetime(df["date"])
    df = df.set_index("date")

    df = df.resample("QE").ffill()

    df = df.reset_index()
    return df


def run_data_pipeline(country="usa"):

    from src.config import RAW_DATA_PATH

    base_path = f"{RAW_DATA_PATH}{country}"

    if country == "usa":
        gdp_file = "GDP USA.csv"
        inflation_file = "Inflation USA.csv"
        unemployment_file = "Unemp USA.csv"
        short_rate = "USA3MS.csv"
        long_rate = "USAS10.csv"
        recession_file = "Recession USA.csv"

    elif country == "uk":
        gdp_file = "GDP UK.csv"
        inflation_file = "Inflation UK.csv"
        unemployment_file = "Unemp UK.csv"
        short_rate = "UK3MS.csv"
        long_rate = "UKS10.csv"
        recession_file = "Recession UK.csv"

    elif country == "india":
        gdp_file = "GDP India.csv"
        inflation_file = "Inflation India.csv"
        unemployment_file = "Unemp India.csv"
        short_rate = "IND3MS.csv"
        long_rate = "INDS10.csv"
        recession_file = "Recession India.csv"

    elif country == "japan":
        gdp_file = "GDP Japan.csv"
        inflation_file = "Inflation Japan.csv"
        unemployment_file = "Unemp Japan.csv"
        short_rate = "JP3MS.csv"
        long_rate = "JPS10.csv"
        recession_file = "Recession Japan.csv"

    elif country == "germany":
        gdp_file = "GDP Germany.csv"
        inflation_file = "Inflation Germany.csv"
        unemployment_file = "Unemp Germany.csv"
        short_rate = "DE3MS.csv"
        long_rate = "DES10.csv"
        recession_file = "Recession Germany.csv"

    else:
        raise ValueError("Country not supported")

    # Load data
    gdp = pd.read_csv(os.path.join(base_path, gdp_file))
    inflation = pd.read_csv(os.path.join(base_path, inflation_file))
    unemployment = pd.read_csv(os.path.join(base_path, unemployment_file))
    short = pd.read_csv(os.path.join(base_path, short_rate))
    long = pd.read_csv(os.path.join(base_path, long_rate))
    recession = pd.read_csv(os.path.join(base_path, recession_file))

    # Clean columns
    gdp = clean_macro(gdp, "gdp_growth")
    inflation = clean_macro(inflation, "inflation")
    unemployment = clean_macro(unemployment, "unemployment")
    short = clean_macro(short, "short_rate")
    long = clean_macro(long, "long_rate")
    recession = clean_macro(recession, "recession")

    # Handle unemployment frequency
    if country == "india":
        unemployment = annual_to_quarterly(unemployment)
    else:
        unemployment = to_quarterly(unemployment)

    # Convert other indicators to quarterly
    gdp = to_quarterly(gdp)
    inflation = to_quarterly(inflation)
    short = to_quarterly(short)
    long = to_quarterly(long)
    recession = to_quarterly(recession)

    # Create yield spread
    yield_data = long.merge(short, on="date")
    yield_data["yield_spread"] = yield_data["long_rate"] - yield_data["short_rate"]
    yield_data = yield_data[["date", "yield_spread"]]

    # Merge all macro indicators
    df = (
        gdp.merge(inflation, on="date", how="outer")
        .merge(unemployment, on="date", how="outer")
        .merge(yield_data, on="date", how="outer")
        .merge(recession, on="date", how="outer")
    )

    df = df.sort_values("date")

    # Forward fill macro indicators
    df = df.ffill()

    # Keep rows where recession label exists
    df = df.dropna(subset=["recession"])

    print(country.upper(), "rows:", len(df))

    df = df.reset_index(drop=True)

    # Ensure processed folder exists
    os.makedirs("data/processed", exist_ok=True)

    output_path = f"data/processed/{country}_macro_quarterly.csv"
    df.to_csv(output_path, index=False)

    print(f"Data pipeline complete for {country.upper()}. Saved to: {output_path}")

    return df