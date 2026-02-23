import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve


def plot_roc(y_test, y_prob):

    fpr, tpr, _ = roc_curve(y_test, y_prob)

    plt.figure()
    plt.plot(fpr, tpr)
    plt.plot([0, 1], [0, 1])
    plt.title("ROC Curve")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.show()


def plot_recession_probability(test_df, y_prob):

    test_df = test_df.copy()
    test_df["probability"] = y_prob

    plt.figure()
    plt.plot(test_df["date"], test_df["probability"])
    plt.title("Predicted Recession Probability Over Time")
    plt.xticks(rotation=45)
    plt.show()