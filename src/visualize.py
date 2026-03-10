import pandas as pd
import matplotlib.pyplot as plt


def plot_recession_probabilities():

    df = pd.read_csv("data/global_recession_probabilities.csv")

    plt.figure(figsize=(12,6))

    for col in df.columns[1:]:
        plt.plot(df["date"], df[col], label=col.upper())

    plt.xticks(rotation=45)
    plt.ylabel("Recession Probability")
    plt.title("Global Recession Probabilities")
    plt.legend()

    plt.tight_layout()

    from src.config import REPORT_PATH

    plt.savefig(f"{REPORT_PATH}recession_probabilities.png")

    print("Figure saved to reports/figures/")

def plot_feature_importance(model, X, country):
    
    importance = model.feature_importances_

    df = pd.DataFrame({
        "feature": X.columns,
        "importance": importance
    })

    df = df.sort_values("importance", ascending=True)

    plt.figure(figsize=(8,5))

    plt.barh(df["feature"], df["importance"])

    plt.title(f"Feature Importance ({country.upper()})")

    plt.xlabel("Importance")

    plt.tight_layout()

    plt.savefig(f"reports/figures/feature_importance_{country}.png")

    print(f"Feature importance saved for {country.upper()}")
