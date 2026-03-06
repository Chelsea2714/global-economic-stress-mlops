import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, classification_report
import pickle


def train_model(df, country):

    X = df.drop(columns=["recession", "date"])
    y = df["recession"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, shuffle=False
    )

    model = LogisticRegression()
    model.fit(X_train, y_train)

    probs = model.predict_proba(X_test)[:, 1]

    roc = roc_auc_score(y_test, probs)
    print("ROC-AUC:", roc)

    preds = (probs >= 0.3).astype(int)

    print(classification_report(y_test, preds))

    model_path = f"models/logistic_model_{country}.pkl"

    with open(model_path, "wb") as f:
        pickle.dump(model, f)

    print(f"Model saved for {country.upper()} to:", model_path)