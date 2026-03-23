"""
K-Nearest Neighbors (KNN) implementation demo.
Includes:
1) Basic KNN classification on Iris dataset
2) Simple K tuning loop to compare accuracy for multiple K values
"""

from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler


def knn_basic_demo() -> None:
    """Train and evaluate a basic KNN classifier."""
    iris = load_iris()
    X = iris.data
    y = iris.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Scale features because KNN is distance-based.
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = KNeighborsClassifier(n_neighbors=5, metric="euclidean")
    model.fit(X_train_scaled, y_train)

    y_pred = model.predict(X_test_scaled)

    print("=" * 70)
    print("KNN Basic Demo (K=5)")
    print("Accuracy:", round(accuracy_score(y_test, y_pred), 4))
    print(classification_report(y_test, y_pred, target_names=iris.target_names))


def knn_k_tuning_demo() -> None:
    """Try different K values and print their test accuracies."""
    iris = load_iris()
    X = iris.data
    y = iris.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    print("=" * 70)
    print("K Tuning Demo")

    best_k = None
    best_acc = 0.0

    for k in range(1, 16):
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)
        acc = accuracy_score(y_test, y_pred)

        print(f"K={k:2d} -> Accuracy={acc:.4f}")

        if acc > best_acc:
            best_acc = acc
            best_k = k

    print(f"Best K on this split: {best_k} (Accuracy={best_acc:.4f})")


if __name__ == "__main__":
    knn_basic_demo()
    knn_k_tuning_demo()
