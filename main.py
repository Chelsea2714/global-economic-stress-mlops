from src.data_pipeline import run_data_pipeline
from src.feature_engineering import create_features
from src.train_model import train_model
from src.evaluate import plot_roc, plot_recession_probability


def main():

    df = run_data_pipeline()
    df = create_features(df)

    model, scaler, test, y_test, y_prob = train_model(df)

    plot_roc(y_test, y_prob)
    plot_recession_probability(test, y_prob)


if __name__ == "__main__":
    main()