# Random Forest (ML): Theory and Implementation Guide

## 1) What is Random Forest?
Random Forest is an ensemble learning algorithm that combines many decision trees and aggregates their outputs.

- Classification: majority vote of all trees
- Regression: average prediction of all trees

It improves over a single decision tree by reducing overfitting and improving generalization.

## 2) Core Concepts
### 2.1 Bagging (Bootstrap Aggregation)
Each tree is trained on a random sample of training data (with replacement).

### 2.2 Feature Randomness
At each split, only a random subset of features is considered.
This reduces correlation between trees and improves ensemble performance.

### 2.3 Final Prediction
- Classifier: mode (most frequent class)
- Regressor: mean of tree outputs

## 3) Why Random Forest Works Well
- Single trees have high variance.
- Averaging many diverse trees lowers variance.
- Keeps good non-linear learning power with better stability.

## 4) Important Hyperparameters
- n_estimators: number of trees
- max_depth: max depth of each tree
- min_samples_split: min samples required to split
- min_samples_leaf: min samples in each leaf
- max_features: number of features considered at each split
- bootstrap: whether bootstrap sampling is used
- random_state: reproducibility

## 5) Advantages and Limitations
### Advantages
- Strong performance on many tabular datasets
- Handles non-linear relationships
- Less overfitting than one decision tree
- Built-in feature importance

### Limitations
- Larger models and slower inference than one tree
- Less interpretable than a single tree
- May still overfit if not tuned

## 6) Typical Workflow
1. Load dataset
2. Train-test split
3. Train RandomForestClassifier or RandomForestRegressor
4. Predict test set
5. Evaluate metrics
6. Tune hyperparameters

## 7) Evaluation Metrics
### Classification
- Accuracy
- Precision, Recall, F1-score

### Regression
- MAE
- MSE
- R2 score

## 8) Files in This Folder
- `README.md`: full theory + implementation guidance
- `random_forest_notes.md`: quick revision notes
- `random_forest_implementation.ipynb`: practical notebook implementation

## 9) Next Learning Path
After Random Forest, you can learn:
- Gradient Boosting
- XGBoost
- LightGBM
