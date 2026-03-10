from src.data_pipeline import run_data_pipeline
from src.train_model import train_model
from src.predict_global import global_recession_table
from src.visualize import plot_recession_probabilities


def main():

    countries = ["usa", "uk", "india", "japan", "germany"]

    for country in countries:

        print("\nRunning pipeline for:", country.upper())

        df = run_data_pipeline(country)

        train_model(df, country)

        global_recession_table()

        plot_recession_probabilities()

if __name__ == "__main__":
    main()