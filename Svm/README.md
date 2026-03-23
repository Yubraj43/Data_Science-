# Support Vector Machine (SVM)

This folder contains learning material and implementation practice for Support Vector Machine.

## Files in this Folder
- `support_vector.ipynb`: Notebook for SVM practice and experiments.
- `NOTE.md`: Quick theory and implementation notes.

## What You Will Learn
- SVM core concept: maximum-margin classifier
- Support vectors and decision boundary
- Hard margin vs soft margin SVM
- Kernel-based classification (`linear`, `rbf`, `poly`, `sigmoid`)
- Hyperparameter tuning (`C`, `gamma`, `kernel`)
- Model evaluation with confusion matrix and classification metrics

## SVM Theory (Short)
SVM finds a hyperplane that separates classes while maximizing margin.
Only a subset of points (support vectors) determines the final boundary.

For linearly separable data:
- Hyperplane: `w.x + b = 0`
- Prediction: `sign(w.x + b)`

For non-linear data, SVM uses kernels (especially RBF) to model complex boundaries.

## Implementation Steps (scikit-learn)
1. Prepare `X` (features) and `y` (target).
2. Split data using `train_test_split`.
3. Scale features using `StandardScaler`.
4. Train `SVC` model.
5. Evaluate with:
   - `confusion_matrix`
   - `classification_report`
6. Tune model with `GridSearchCV`.

## Quick Start Code
```python
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report

# X, y should already be defined
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("svc", SVC())
])

param_grid = {
    "svc__kernel": ["linear", "rbf"],
    "svc__C": [0.1, 1, 10],
    "svc__gamma": ["scale", 0.01, 0.1]
}

search = GridSearchCV(pipeline, param_grid, cv=5, scoring="f1_macro", n_jobs=-1)
search.fit(X_train, y_train)

pred = search.predict(X_test)
print("Best Parameters:", search.best_params_)
print(classification_report(y_test, pred))
```

## Best Practices
- Always scale numeric features before SVM.
- Use cross-validation for tuning.
- For imbalanced data, track precision/recall/F1, not only accuracy.
- Start simple (`linear` kernel), then try `rbf` if needed.

## Suggested Next Improvements
- Add decision boundary visualization for 2D datasets.
- Add class imbalance handling (`class_weight='balanced'`).
- Save the trained model using `joblib`.
