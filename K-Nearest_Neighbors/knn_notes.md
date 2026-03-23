# KNN Quick Notes

## Definition
KNN (K-Nearest Neighbors) is a supervised learning algorithm that predicts using the K closest training points.

## Steps
1. Choose K
2. Compute distances
3. Pick K nearest neighbors
4. Classification: majority vote
5. Regression: average value

## Common Distance Formula
Euclidean:

d = sqrt(sum((xi - yi)^2))

## Important Concepts
- Feature scaling is required for KNN.
- Small K -> overfitting risk.
- Large K -> underfitting risk.

## Hyperparameters
- `n_neighbors` (K)
- `metric` (euclidean, manhattan, etc.)
- `weights` (`uniform` or `distance`)

## Pros
- Simple
- No training complexity
- Good baseline

## Cons
- Slow for large data at prediction time
- Sensitive to noisy features
- Needs scaling

## Typical Use Cases
- Basic pattern recognition
- Recommendation prototypes
- Introductory classification tasks
