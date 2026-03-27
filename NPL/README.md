# NPL

This folder contains notes and a full NLP text classification implementation.

## Contents
- `npl_notes.md`: Concept notes and key points.
- `npl_implementation.py`: End-to-end NLP implementation with training and evaluation.

## Features in implementation
- Text cleaning and normalization
- TF-IDF vectorization with unigram and bigram features
- Logistic Regression classifier
- Train/test split and evaluation report
- Optional custom text predictions
- Optional model saving (`joblib`)

## Run with default sample data
```bash
python npl_implementation.py
```

## Run with custom CSV data
```bash
python npl_implementation.py --data-path your_data.csv --text-column text --label-column label
```

## Predict custom text after training
```bash
python npl_implementation.py --predict "I love this service" "Worst experience ever"
```

## Save trained model
```bash
python npl_implementation.py --save-model --output-dir artifacts
```

## Required packages
```bash
pip install pandas scikit-learn joblib
```
