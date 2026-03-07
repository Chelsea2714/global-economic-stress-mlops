from src.data_pipeline import run_data_pipeline
from src.train_model import train_model


def main():

    countries = ["usa", "uk", "india", "japan", "germany"]

    for country in countries:

        print("\nRunning pipeline for:", country.upper())

        df = run_data_pipeline("india")

        train_model(df, country)


if __name__ == "__main__":
    main()