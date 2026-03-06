from src.data_pipeline import run_data_pipeline
from src.train_model import train_model


def main():

    for country in ["usa", "uk"]:

        df = run_data_pipeline(country)

        train_model(df, country)


if __name__ == "__main__":
    main()