# AdaBoost Quick Notes

## Definition
AdaBoost (Adaptive Boosting) is an ensemble method that combines weak learners sequentially.

## Core Mechanism
- Start with equal sample weights
- Train weak learner
- Increase weights of misclassified points
- Train next learner on updated weighted data
- Final output is weighted combination of learners

## Typical Base Learner
Decision stump (decision tree with max_depth=1)

## Key Hyperparameters
- n_estimators
- learning_rate
- estimator (base model)

## Use Cases
- Binary classification
- Multi-class classification
- Tabular data tasks

## Pros
- Improves weak learners significantly
- Good benchmark boosting algorithm

## Cons
- Sensitive to noise/outliers
- Can overfit noisy data

## Interview One-Liner
AdaBoost builds a strong classifier by sequentially training weak learners and adaptively reweighting training samples to focus on previous errors.
