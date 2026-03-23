# Random Forest Quick Notes

## Definition
Random Forest is an ensemble of decision trees trained with bagging + random feature selection.

## For Classification
- Each tree predicts a class
- Final output = majority vote

## For Regression
- Each tree predicts a numeric value
- Final output = average

## Key Ideas
- Bootstrap sampling for each tree
- Random subset of features at each split
- Reduces variance and overfitting

## Important Hyperparameters
- n_estimators
- max_depth
- max_features
- min_samples_split
- min_samples_leaf

## Pros
- Accurate and robust
- Handles non-linear patterns
- Less tuning than many advanced models

## Cons
- Less interpretable than one decision tree
- Larger model size
- Slower prediction than a single tree

## Metrics
Classifier: Accuracy, Precision, Recall, F1
Regressor: MAE, MSE, R2

## Interview One-Liner
Random Forest is a bagging-based ensemble method that combines many randomized decision trees to improve prediction accuracy and reduce overfitting.
