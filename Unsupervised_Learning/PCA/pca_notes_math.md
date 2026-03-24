# PCA Notes (Math)

## Goal
PCA projects high-dimensional data into a lower-dimensional space while preserving as much variance as possible.

## Data Matrix
Let the centered dataset be:

\[
X \in \mathbb{R}^{n \times d}
\]

where:
- \(n\) = number of samples
- \(d\) = number of features

Centering means each feature has mean 0.

## Covariance Matrix
\[
\Sigma = \frac{1}{n-1} X^T X
\]

\(\Sigma\) captures how features vary together.

## Eigenvalue Decomposition
PCA solves:

\[
\Sigma v_i = \lambda_i v_i
\]

where:
- \(v_i\): eigenvector (principal direction)
- \(\lambda_i\): eigenvalue (variance along \(v_i\))

Sort eigenvalues in descending order:

\[
\lambda_1 \ge \lambda_2 \ge \cdots \ge \lambda_d
\]

The first \(k\) eigenvectors form projection matrix:

\[
W_k = [v_1, v_2, \dots, v_k]
\]

## Projection
Reduced representation:

\[
Z = X W_k
\]

where \(Z \in \mathbb{R}^{n \times k}\).

## Explained Variance Ratio
For component \(i\):

\[
\text{EVR}_i = \frac{\lambda_i}{\sum_{j=1}^{d} \lambda_j}
\]

Cumulative explained variance for first \(k\) components:

\[
\text{CEV}_k = \sum_{i=1}^{k} \text{EVR}_i
\]

Choose \(k\) such that CEV is high (for example, 0.90 to 0.99).

## Important Notes
- PCA is sensitive to feature scaling, so standardization is usually required.
- PCA is linear and may not capture complex nonlinear structure.
- PCA is unsupervised: it does not use target labels.
