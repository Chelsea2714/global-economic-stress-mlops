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