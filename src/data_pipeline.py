import pandas as pd

RAW_PATH = "data/raw/"
PROCESSED_PATH = "data/processed/usa_macro_quarterly.csv"


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


def run_data_pipeline():

    # Load
    gdp = pd.read_csv(RAW_PATH + "GDP USA.csv")
    inflation = pd.read_csv(RAW_PATH + "Inflation USA.csv")
    debt = pd.read_csv(RAW_PATH + "Govt debt USA.csv")
    interest = pd.read_csv(RAW_PATH + "Int rate USA.csv")
    unemployment = pd.read_csv(RAW_PATH + "Unemp USA.csv")
    dgs10 = pd.read_csv(RAW_PATH + "DGS10.csv")
    tb3ms = pd.read_csv(RAW_PATH + "TB3MS.csv")
    recession = pd.read_csv(RAW_PATH + "Recession USA.csv")

    # Clean
    gdp = clean_macro(gdp, "gdp_growth")
    inflation = clean_macro(inflation, "inflation")
    debt = clean_macro(debt, "debt_to_gdp")
    interest = clean_macro(interest, "interest_rate")
    unemployment = clean_macro(unemployment, "unemployment")
    dgs10 = clean_macro(dgs10, "dgs10")
    tb3ms = clean_macro(tb3ms, "tb3ms")
    recession = clean_macro(recession, "recession")

    # Quarterly
    gdp = to_quarterly(gdp)
    inflation = to_quarterly(inflation)
    debt = to_quarterly(debt)
    interest = to_quarterly(interest)
    unemployment = to_quarterly(unemployment)
    dgs10 = to_quarterly(dgs10)
    tb3ms = to_quarterly(tb3ms)
    recession = to_quarterly(recession)

    # Yield Spread
    yield_data = dgs10.merge(tb3ms, on="date")
    yield_data["yield_spread"] = yield_data["dgs10"] - yield_data["tb3ms"]
    yield_data = yield_data[["date", "yield_spread"]]

    # Merge all
    df = gdp.merge(inflation, on="date") \
            .merge(debt, on="date") \
            .merge(interest, on="date") \
            .merge(unemployment, on="date") \
            .merge(yield_data, on="date") \
            .merge(recession, on="date")

    df = df.sort_values("date").dropna().reset_index(drop=True)

    df.to_csv(PROCESSED_PATH, index=False)

    print("Data pipeline complete. Saved to:", PROCESSED_PATH)

    return df