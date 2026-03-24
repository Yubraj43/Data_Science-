# XGBoost Notes

## What Is XGBoost?
XGBoost (Extreme Gradient Boosting) is an efficient and scalable implementation of gradient boosted decision trees.

## Why It Is Popular
- Strong performance on tabular datasets.
- Built-in regularization helps reduce overfitting.
- Handles missing values internally.
- Supports feature importance analysis.
- Fast training with parallelized tree construction.

## Key Hyperparameters
- n_estimators: number of boosting rounds.
- learning_rate: step size shrinkage.
- max_depth: tree complexity control.
- min_child_weight: minimum sum of instance weight in a child.
- subsample: fraction of samples used per tree.
- colsample_bytree: fraction of features used per tree.
- reg_alpha: L1 regularization.
- reg_lambda: L2 regularization.

## Basic Workflow
1. Clean and prepare data.
2. Split data into train and test.
3. Train baseline XGBoost model.
4. Evaluate using metrics such as accuracy, precision, recall, F1, or RMSE.
5. Tune parameters with cross-validation.

## Tips
- Use smaller learning_rate and larger n_estimators for stable learning.
- Use early stopping with a validation set.
- Standardization is usually not required for tree-based models.
