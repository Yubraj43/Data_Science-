# Decision Tree Quick Notes

## Core Idea
A Decision Tree splits data using if-else rules until it reaches a prediction at a leaf node.

## Classifier vs Regressor
- Classifier: predicts class labels (0/1, A/B/C)
- Regressor: predicts continuous values (price, score)

## Splitting Criteria
Classifier:
- Gini
- Entropy

Regressor:
- Mean Squared Error reduction

## Important Parameters
- max_depth
- min_samples_split
- min_samples_leaf

## Overfitting Control
Use:
- Smaller max_depth
- Larger min_samples_leaf
- Pruning / validation tuning

## Common Evaluation Metrics
Classifier:
- Accuracy
- Precision, Recall, F1

Regressor:
- MAE
- MSE
- R2 score

## Interview One-Liner
Decision Tree is a rule-based supervised model that recursively splits data to maximize class purity (classification) or minimize prediction error (regression).
