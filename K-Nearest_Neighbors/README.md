# K-Nearest Neighbors (KNN): Theory and Implementation Guide

## 1. What is KNN?
K-Nearest Neighbors (KNN) is a supervised machine learning algorithm used for:
- Classification
- Regression

KNN is a non-parametric, instance-based learning method:
- Non-parametric: it does not assume a fixed mathematical form.
- Instance-based: it stores training data and predicts by comparing new points with stored examples.

## 2. Core Idea
To predict a new data point:
1. Choose a value for K (number of neighbors).
2. Compute distance from the new point to all training points.
3. Select the K nearest points.
4. Classification: choose the majority class among neighbors.
5. Regression: take average (or weighted average) of neighbor values.

## 3. Distance Metrics
Common metrics:
- Euclidean distance (most common):
  d = sqrt(sum((xi - yi)^2))
- Manhattan distance
- Minkowski distance

Distance choice can affect results.

## 4. Choosing K
- Small K (e.g., 1): sensitive to noise, high variance.
- Large K: smoother decision boundary, can underfit.

Typical approach:
- Try multiple K values (grid search or manual loop).
- Select best K using validation/test accuracy.

## 5. Why Feature Scaling Matters
KNN depends on distance.
If one feature has a much larger scale, it dominates the distance.

Always scale features for KNN:
- StandardScaler
- MinMaxScaler

## 6. Advantages and Limitations
### Advantages
- Easy to understand and implement.
- No explicit training phase.
- Works well for small to medium datasets.

### Limitations
- Prediction can be slow on large datasets.
- Sensitive to irrelevant features and feature scales.
- Memory heavy (stores training set).

## 7. Practical Implementation Steps
1. Load data
2. Split train/test
3. Scale features
4. Train KNN model
5. Predict on test set
6. Evaluate with accuracy and classification report
7. Tune K by trying multiple values

## 8. Files in This Folder
- `README.md`: full KNN explanation
- `knn_notes.md`: quick revision notes
- `knn_implementation.py`: runnable implementation example

## 9. Run the Example
From this folder:

```bash
python knn_implementation.py
```

## 10. Summary
KNN is one of the best beginner algorithms to learn classification fundamentals.
It teaches:
- distance-based learning
- importance of scaling
- model selection through K tuning
