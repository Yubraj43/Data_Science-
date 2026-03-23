# Naive Bayes: Theory and Implementation Guide

## 1. What is Naive Bayes?
Naive Bayes is a probabilistic machine learning algorithm used mainly for classification tasks.

It is based on Bayes' Theorem and a strong assumption:
- Features are conditionally independent given the class.

Even though this assumption is often not perfectly true, Naive Bayes performs very well in many real-world tasks such as:
- Spam detection
- Sentiment analysis
- Document classification
- Basic medical diagnosis support

## 2. Bayes' Theorem
Bayes' Theorem:

P(C | X) = (P(X | C) * P(C)) / P(X)

Where:
- C = class label (for example, Spam or Not Spam)
- X = feature vector
- P(C | X) = posterior probability (probability of class C given features X)
- P(X | C) = likelihood
- P(C) = prior probability of class C
- P(X) = evidence

For classification, P(X) is the same for all classes, so we compare:

P(C | X) proportional to P(X | C) * P(C)

## 3. Why it is called "Naive"
The algorithm assumes:

P(X1, X2, ..., Xn | C) = P(X1 | C) * P(X2 | C) * ... * P(Xn | C)

This means each feature contributes independently to the class decision.

## 4. Types of Naive Bayes
### 4.1 Gaussian Naive Bayes
- Used when features are continuous and approximately normally distributed.
- Example: height, weight, blood pressure.

### 4.2 Multinomial Naive Bayes
- Used for count data.
- Common in text classification with word counts or TF-IDF.

### 4.3 Bernoulli Naive Bayes
- Used for binary feature vectors (0/1).
- Example: whether a word is present or absent.

## 5. Training and Prediction Workflow
### Training
1. Calculate prior probabilities P(C).
2. Calculate feature likelihoods P(Xi | C) for each class.
3. Store these probabilities.

### Prediction
1. For a new sample X, compute posterior score for each class:
   score(C) = P(C) * product of P(Xi | C)
2. Choose class with highest score.

In practice, log probabilities are used to avoid numerical underflow:

log(score(C)) = log(P(C)) + sum(log(P(Xi | C)))

## 6. Advantages and Limitations
### Advantages
- Fast and simple
- Works well with high-dimensional data
- Performs strongly on text tasks
- Requires less training data than many models

### Limitations
- Independence assumption may be unrealistic
- Zero-frequency problem (handled with smoothing)
- Probabilities can be poorly calibrated

## 7. Smoothing (Important)
If a feature value never appears in a class during training, its probability becomes 0 and can zero-out the whole posterior.

Solution: Laplace smoothing.

For counts:

P(word | class) = (count(word, class) + alpha) / (total_words_in_class + alpha * vocabulary_size)

Usually alpha = 1.

## 8. Practical Implementation
This folder includes:
- `naive_bayes_notes.md`: concise theory notes
- `naive_bayes_implementation.py`: implementation examples

### Run the implementation file
From this folder:

```bash
python naive_bayes_implementation.py
```

What it demonstrates:
1. Gaussian Naive Bayes on a numeric dataset
2. Multinomial Naive Bayes for spam text classification

## 9. Where Naive Bayes is commonly used
- Email spam filtering
- Message category classification
- Review sentiment tagging
- Topic detection in documents

## 10. Summary
Naive Bayes is one of the best first algorithms to learn for classification because:
- It is mathematically elegant
- Easy to implement
- Very effective in many practical tasks

It is a strong baseline model before trying more complex algorithms.
