# SVM Notes (Theory + Implementation)

## 1. What is SVM?
Support Vector Machine (SVM) is a supervised learning algorithm used for:
- Classification (most common)
- Regression (SVR)

Main idea:
- Find a decision boundary (hyperplane) that separates classes.
- Choose the boundary with the **maximum margin** (largest distance to the nearest points of each class).

The nearest points are called **support vectors**.

## 2. Geometric Intuition
For binary classification, SVM learns:
- Hyperplane: `w.x + b = 0`
- Class prediction: sign(`w.x + b`)

Margin size is `2 / ||w||`.
Maximizing margin improves generalization on unseen data.

## 3. Hard Margin vs Soft Margin
### Hard Margin SVM
- Assumes perfectly separable data.
- No classification errors allowed.
- Sensitive to noise/outliers.

### Soft Margin SVM
- Allows some misclassification using slack variables.
- Controlled by regularization parameter `C`.

`C` behavior:
- Large `C`: penalize errors heavily, narrower margin, possible overfitting.
- Small `C`: allow more errors, wider margin, better regularization.

## 4. Kernel Trick
When data is not linearly separable, SVM uses kernels to map data implicitly to higher dimensions.

Common kernels:
- `linear`
- `poly`
- `rbf` (Gaussian, most widely used)
- `sigmoid`

Important RBF parameter:
- `gamma`: controls influence range of each point.
  - High `gamma`: very local, complex boundary (risk of overfit).
  - Low `gamma`: smoother boundary (risk of underfit).

## 5. Why Feature Scaling is Important
SVM relies on distances and dot products.
If features are on different scales, one feature can dominate others.

Best practice:
- Standardize features (`StandardScaler`) before training SVM.
- Use a pipeline to avoid data leakage.

## 6. Typical Workflow
1. Load and inspect data.
2. Split into train/test.
3. Scale features.
4. Train SVM model.
5. Evaluate with accuracy, precision, recall, F1, confusion matrix.
6. Tune hyperparameters (`C`, `gamma`, `kernel`) using cross-validation.

## 7. Minimal Classification Example (scikit-learn)
```python
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix

# X: features, y: labels
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = Pipeline([
    ("scaler", StandardScaler()),
    ("svc", SVC(kernel="rbf", C=1.0, gamma="scale"))
])

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
```

## 8. Hyperparameter Tuning Example
```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    "svc__kernel": ["linear", "rbf"],
    "svc__C": [0.1, 1, 10, 100],
    "svc__gamma": ["scale", 0.01, 0.1, 1]
}

grid = GridSearchCV(
    model,
    param_grid=param_grid,
    cv=5,
    scoring="f1_macro",
    n_jobs=-1
)

grid.fit(X_train, y_train)
print("Best params:", grid.best_params_)
print("Best CV score:", grid.best_score_)
```

## 9. Common Mistakes
- Not scaling input features.
- Evaluating only accuracy on imbalanced data.
- Using very high `C` and `gamma` without validation.
- Tuning on test set (data leakage).

## 10. When to Use SVM
Use SVM when:
- Dataset size is small to medium.
- Feature space can be high-dimensional.
- You need a strong baseline classifier.

Avoid or be careful when:
- Dataset is extremely large (training can be slow).
- Model interpretability is a strict requirement.
