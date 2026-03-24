# Gradient Boosting Notes

## What It Is
Gradient Boosting is an ensemble technique that builds weak learners sequentially, where each new learner reduces the errors made by the previous ensemble.

## Core Idea
- Start with a simple model.
- Compute residual errors.
- Fit a new weak learner to those residuals.
- Add the new learner to the ensemble with a learning rate.
- Repeat for many iterations.

## Important Hyperparameters
- n_estimators: number of boosting stages.
- learning_rate: contribution of each tree.
- max_depth: depth of individual trees.
- subsample: fraction of samples used per stage.
- min_samples_split and min_samples_leaf: regularization controls.

## Pros
- High predictive performance on tabular data.
- Handles nonlinear relationships.
- Works for regression and classification.

## Cons
- Can overfit if not tuned.
- Training can be slower than simpler models.
- Sensitive to noisy data and outliers.

## Common Workflow
1. Prepare and clean data.
2. Split into train and test sets.
3. Train baseline model.
4. Tune hyperparameters with cross-validation.
5. Evaluate and interpret feature importance.
