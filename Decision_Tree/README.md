# Decision Tree: Classifier and Regressor Guide

## 1) What is a Decision Tree?
A Decision Tree is a supervised machine learning algorithm that predicts output by splitting data step-by-step using feature-based rules.

- For classification: predicts categories/classes.
- For regression: predicts continuous numbers.

It looks like a flowchart:
- Root node: first split
- Internal nodes: conditions
- Leaf nodes: final prediction

## 2) Decision Tree Classifier
A classifier tree chooses splits that make class groups as pure as possible.

Common impurity measures:
- Gini impurity
- Entropy (information gain)

Goal:
Create branches where each leaf mostly contains one class.

## 3) Decision Tree Regressor
A regressor tree chooses splits that reduce prediction error.

Common split criterion:
- Squared error reduction (MSE reduction)

Goal:
Create leaves where target values are similar, then predict mean value of each leaf.

## 4) Key Hyperparameters
- max_depth: maximum depth of tree
- min_samples_split: minimum samples required to split
- min_samples_leaf: minimum samples per leaf
- criterion:
  - classifier: gini, entropy
  - regressor: squared_error

## 5) Why Trees Are Popular
Advantages:
- Easy to understand and explain
- Handles non-linear patterns
- No feature scaling required in most cases

Limitations:
- Can overfit easily
- Unstable to small data changes
- Single trees are weaker than ensemble methods (Random Forest, XGBoost)

## 6) Typical Workflow
1. Load dataset
2. Split train/test
3. Train model (classifier or regressor)
4. Predict test set
5. Evaluate metrics
6. Tune hyperparameters

## 7) Files in This Folder
- decision_tree_notes.md: quick revision notes
- decision_tree_implementation.ipynb: practical implementation notebook
- README.md: complete concept + implementation guide

## 8) Suggested Next Step
After understanding a single decision tree, learn:
- Random Forest
- Gradient Boosting
- XGBoost
