"""
Naive Bayes implementation examples:
1) Gaussian Naive Bayes on numeric data
2) Multinomial Naive Bayes on simple text spam data
"""

from sklearn.datasets import load_iris
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, MultinomialNB


def gaussian_nb_demo() -> None:
    """Demonstrates Gaussian Naive Bayes on the Iris dataset."""
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42, stratify=iris.target
    )

    model = GaussianNB()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print("=" * 70)
    print("Gaussian Naive Bayes (Iris)")
    print("Accuracy:", round(accuracy_score(y_test, y_pred), 4))
    print(classification_report(y_test, y_pred, target_names=iris.target_names))


def multinomial_nb_demo() -> None:
    """Demonstrates Multinomial Naive Bayes on a tiny spam dataset."""
    messages = [
        "Win a free iPhone now",
        "Congratulations you won a lottery claim now",
        "Urgent claim your cash prize",
        "Hi are you coming to class today",
        "Let us meet for lunch tomorrow",
        "Can you call me when you are free",
        "Free reward waiting click now",
        "Project meeting is scheduled for tomorrow",
    ]
    labels = [1, 1, 1, 0, 0, 0, 1, 0]  # 1 = spam, 0 = not spam

    X_train, X_test, y_train, y_test = train_test_split(
        messages, labels, test_size=0.25, random_state=42, stratify=labels
    )

    vectorizer = CountVectorizer()
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    model = MultinomialNB(alpha=1.0)
    model.fit(X_train_vec, y_train)
    y_pred = model.predict(X_test_vec)

    print("=" * 70)
    print("Multinomial Naive Bayes (Simple Spam Dataset)")
    print("Accuracy:", round(accuracy_score(y_test, y_pred), 4))
    print(classification_report(y_test, y_pred, target_names=["not spam", "spam"]))

    sample_texts = [
        "Claim your free reward now",
        "Let us discuss the assignment tomorrow",
    ]
    sample_vec = vectorizer.transform(sample_texts)
    sample_pred = model.predict(sample_vec)

    print("Predictions on sample messages:")
    for text, pred in zip(sample_texts, sample_pred):
        label = "spam" if pred == 1 else "not spam"
        print(f"- {text!r} -> {label}")


if __name__ == "__main__":
    gaussian_nb_demo()
    multinomial_nb_demo()
