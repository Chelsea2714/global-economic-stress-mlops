import pandas as pd
import pickle


def predict_country(country):

    df = pd.read_csv(f"data/processed/{country}_macro_quarterly.csv")

    model_path = f"models/logistic_model_{country}.pkl"

    with open(model_path, "rb") as f:
        model = pickle.load(f)

    df = df.dropna()

    X = df.drop(columns=["recession", "date"])

    probs = model.predict_proba(X)[:, 1]

    result = pd.DataFrame({
        "date": df["date"],
        country: probs
    })

    return result


def global_recession_table():

    countries = ["usa", "uk", "india", "japan", "germany"]

    tables = []

    for c in countries:
        tables.append(predict_country(c))

    df = tables[0]

    for t in tables[1:]:
        df = df.merge(t, on="date", how="outer")

    df = df.sort_values("date")

    df.to_csv("data/global_recession_probabilities.csv", index=False)

    print("Global recession probability table created.")