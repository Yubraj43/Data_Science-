# AdaBoost (Adaptive Boosting): Theory and Implementation Guide

## 1) What is AdaBoost?
AdaBoost is an ensemble machine learning algorithm that combines many weak learners to create a strong learner.

- Most commonly uses decision stumps (very small decision trees, usually depth=1)
- Works for both classification and regression variants
- Most popular in practice: AdaBoostClassifier

## 2) Core Idea
AdaBoost trains weak models sequentially.
Each new model focuses more on samples that previous models got wrong.

High-level process:
1. Start with equal sample weights
2. Train weak learner
3. Increase weights for misclassified samples
4. Decrease weights for correctly classified samples
5. Repeat for many estimators
6. Combine learners with weighted voting

## 3) Why it is called Adaptive
It "adapts" by changing sample weights after each iteration.
Hard examples gradually receive more attention.

## 4) AdaBoost for Classification
Final prediction is a weighted vote of weak classifiers.
Classifiers with better performance get higher influence.

## 5) Important Hyperparameters
- n_estimators: number of weak learners
- learning_rate: contribution of each learner
- estimator: base learner (default often DecisionTreeClassifier with depth=1)

## 6) Advantages and Limitations
### Advantages
- Often better than a single weak model
- Good performance on structured/tabular datasets
- Simple concept with strong practical results

### Limitations
- Sensitive to noisy labels and outliers
- Sequential nature can be slower than bagging methods
- Needs hyperparameter tuning for best results

## 7) Typical Workflow
1. Load dataset
2. Train-test split
3. Build AdaBoost model
4. Train model
5. Predict
6. Evaluate metrics
7. Tune n_estimators and learning_rate

## 8) Files in This Folder
- README.md: full explanation
- adaboost_notes.md: quick revision notes
- adaboost_implementation.ipynb: runnable notebook implementation

## 9) Next Learning Path
After AdaBoost, learn:
- Gradient Boosting
- XGBoost
- LightGBM
