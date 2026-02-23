import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, classification_report
import joblib


SPLIT_DATE = "2018-01-01"
MODEL_PATH = "models/logistic_model.pkl"


def train_model(df):

    train = df[df["date"] < SPLIT_DATE]
    test = df[df["date"] >= SPLIT_DATE]

    X_train = train.drop(["date", "recession"], axis=1)
    y_train = train["recession"]

    X_test = test.drop(["date", "recession"], axis=1)
    y_test = test["recession"]

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = LogisticRegression(class_weight="balanced", max_iter=1000)
    model.fit(X_train_scaled, y_train)

    y_prob = model.predict_proba(X_test_scaled)[:, 1]

    print("ROC-AUC:", roc_auc_score(y_test, y_prob))

    threshold = 0.3
    y_pred = (y_prob > threshold).astype(int)

    print(classification_report(y_test, y_pred))

    joblib.dump((model, scaler), MODEL_PATH)

    print("Model saved to:", MODEL_PATH)

    return model, scaler, test, y_test, y_prob