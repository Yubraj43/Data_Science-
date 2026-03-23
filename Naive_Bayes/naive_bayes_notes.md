# Naive Bayes Quick Notes

## Core Idea
Naive Bayes is a classifier that uses probability and Bayes' Theorem.

It predicts class C for input X by maximizing:

P(C | X) proportional to P(X | C) * P(C)

## Key Assumption
Features are conditionally independent given class:

P(X1, X2, ..., Xn | C) = product of P(Xi | C)

## Formula Breakdown
- Prior: P(C)
- Likelihood: P(X | C)
- Posterior: P(C | X)
- Evidence: P(X) (same across classes during argmax comparison)

## Variants
- Gaussian NB: continuous numeric features
- Multinomial NB: count-based features (often text)
- Bernoulli NB: binary features (presence/absence)

## Common Use Cases
- Spam filtering
- Sentiment analysis
- Text categorization

## Important Concept: Smoothing
Use Laplace smoothing to avoid zero probabilities.

## Why Log Probability?
To avoid floating-point underflow when multiplying many small probabilities:

log(P(C | X)) = log(P(C)) + sum of log(P(Xi | C)) + constant

## Pros
- Fast training and prediction
- Works well with high-dimensional sparse text data
- Good baseline model

## Cons
- Independence assumption often unrealistic
- Can underperform on strongly correlated features

## Interview-Style One-Liner
Naive Bayes is a probabilistic classifier that uses Bayes' Theorem with conditional independence assumptions to classify data efficiently.
