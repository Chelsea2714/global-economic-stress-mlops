import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, classification_report
import pickle


def train_model(df, country):

    # Remove remaining NaN rows
    df = df.dropna()

    X = df.drop(columns=["recession", "date"])
    y = df["recession"]

    if len(df) < 20:
        print(f"Not enough data for {country.upper()}, skipping.")
        return

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, shuffle=False
    )

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    probs = model.predict_proba(X_test)[:, 1]

    if len(y_test.unique()) > 1:
        roc = roc_auc_score(y_test, probs)
        print("ROC-AUC:", roc)
    else:
        print("ROC-AUC: not defined (only one class in test set)")

    preds = (probs >= 0.3).astype(int)

    print(classification_report(y_test, preds))

    from src.config import MODEL_PATH

    model_path = f"{MODEL_PATH}logistic_model_{country}.pkl"

    with open(model_path, "wb") as f:
        pickle.dump(model, f)

    print(f"Model saved for {country.upper()} to:", model_path)