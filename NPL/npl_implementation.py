"""Full NLP text classification implementation.

This script supports two modes:
1. Train and evaluate on a default sample dataset.
2. Train and evaluate on a custom CSV dataset.

CSV requirements:
- A text column (default: `text`)
- A label column (default: `label`)
"""

from __future__ import annotations

import argparse
import re
import string
from pathlib import Path
from typing import Iterable, cast

import pandas as pd
from joblib import dump
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline


def clean_text(text: str) -> str:
    """Normalize input text for vectorization."""
    text = text.lower()
    text = re.sub(r"https?://\S+|www\.\S+", " ", text)
    text = re.sub(r"\d+", " ", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\s+", " ", text).strip()
    return text


def build_default_dataset() -> pd.DataFrame:
    """Create a small, balanced sentiment dataset for quick experimentation."""
    data = {
        "text": [
            "I loved this movie, the acting was fantastic",
            "Absolutely wonderful experience and great service",
            "The product quality is excellent and worth every penny",
            "Very happy with the fast delivery and packaging",
            "This app is intuitive and easy to use",
            "The support team solved my issue quickly",
            "I am disappointed, the item broke in two days",
            "Terrible service, nobody responded to my complaint",
            "The food was cold and tasted awful",
            "Waste of money, not recommended at all",
            "The update made the application very unstable",
            "I regret buying this because performance is poor",
            "Great value for money and excellent customer care",
            "User interface is clean and performance is smooth",
            "Bad packaging and delayed shipping experience",
            "The instructions were clear and setup was simple",
            "Horrible battery life after just one week",
            "Fantastic build quality and premium finish",
            "Customer support was rude and unhelpful",
            "I am extremely satisfied with this purchase",
        ],
        "label": [
            "positive",
            "positive",
            "positive",
            "positive",
            "positive",
            "positive",
            "negative",
            "negative",
            "negative",
            "negative",
            "negative",
            "negative",
            "positive",
            "positive",
            "negative",
            "positive",
            "negative",
            "positive",
            "negative",
            "positive",
        ],
    }
    return pd.DataFrame(data)


def load_dataset(data_path: str | None, text_column: str, label_column: str) -> pd.DataFrame:
    """Load dataset from CSV or fallback to default sample dataset."""
    if data_path is None:
        dataset = build_default_dataset()
        print("Using built-in sample dataset.")
        return dataset

    csv_path = Path(data_path)
    if not csv_path.exists():
        raise FileNotFoundError(f"Dataset file not found: {csv_path}")

    dataset = pd.read_csv(csv_path)
    required = {text_column, label_column}
    missing = required.difference(dataset.columns)
    if missing:
        raise ValueError(
            f"Missing required columns: {sorted(missing)}. "
            f"Available columns: {list(dataset.columns)}"
        )

    dataset = dataset[[text_column, label_column]].dropna()
    if dataset.empty:
        raise ValueError("Dataset is empty after dropping null values.")

    print(f"Loaded dataset from: {csv_path}")
    return dataset


def build_pipeline() -> Pipeline:
    """Create a TF-IDF + Logistic Regression text classifier pipeline."""
    return Pipeline(
        steps=[
            (
                "tfidf",
                TfidfVectorizer(
                    preprocessor=clean_text,
                    stop_words=list(ENGLISH_STOP_WORDS),
                    ngram_range=(1, 2),
                    min_df=1,
                ),
            ),
            (
                "classifier",
                LogisticRegression(
                    max_iter=1000,
                    class_weight="balanced",
                ),
            ),
        ]
    )


def train_and_evaluate(
    dataset: pd.DataFrame,
    text_column: str,
    label_column: str,
    test_size: float = 0.25,
    random_state: int = 42,
) -> tuple[Pipeline, float, str]:
    """Train model and return model, accuracy, and classification report."""
    class_counts = dataset[label_column].value_counts()
    if class_counts.nunique() == 1:
        raise ValueError("Only one class is present. At least two classes are required.")

    can_stratify = bool((class_counts >= 2).all())
    stratify = dataset[label_column] if can_stratify else None

    x_train, x_test, y_train, y_test = train_test_split(
        dataset[text_column].astype(str),
        dataset[label_column].astype(str),
        test_size=test_size,
        random_state=random_state,
        stratify=stratify,
    )

    model = build_pipeline()
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)
    accuracy = float(accuracy_score(y_test, y_pred))
    report = cast(
        str,
        classification_report(
            y_test,
            y_pred,
            zero_division=0,
            output_dict=False,
        ),
    )

    return model, accuracy, report


def predict_samples(model: Pipeline, texts: Iterable[str]) -> None:
    """Print predictions for user-provided samples."""
    text_list = [item for item in texts if item.strip()]
    if not text_list:
        print("No valid prediction text provided.")
        return

    predictions = model.predict(text_list)
    print("\nPredictions:")
    for text, label in zip(text_list, predictions):
        print(f"- Text: {text}")
        print(f"  Predicted label: {label}")


def save_model(model: Pipeline, output_dir: str) -> Path:
    """Persist trained model pipeline to disk."""
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    model_path = out_dir / "npl_text_classifier.joblib"
    dump(model, model_path)
    return model_path


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments."""
    parser = argparse.ArgumentParser(description="NPL full text classification implementation")
    parser.add_argument("--data-path", type=str, default=None, help="Path to CSV dataset")
    parser.add_argument("--text-column", type=str, default="text", help="Text column name")
    parser.add_argument("--label-column", type=str, default="label", help="Label column name")
    parser.add_argument(
        "--predict",
        nargs="*",
        default=None,
        help="One or more texts for prediction after training",
    )
    parser.add_argument(
        "--save-model",
        action="store_true",
        help="Save trained model to disk",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="artifacts",
        help="Output directory for saved model",
    )
    return parser.parse_args()


def main() -> None:
    """Run training, evaluation, optional prediction, and model saving."""
    args = parse_args()

    dataset = load_dataset(args.data_path, args.text_column, args.label_column)
    model, accuracy, report = train_and_evaluate(
        dataset=dataset,
        text_column=args.text_column,
        label_column=args.label_column,
    )

    print(f"\nModel accuracy: {accuracy:.4f}")
    print("\nClassification report:")
    print(report)

    if args.predict:
        predict_samples(model, args.predict)

    if args.save_model:
        model_path = save_model(model, args.output_dir)
        print(f"\nModel saved to: {model_path}")


if __name__ == "__main__":
    main()
