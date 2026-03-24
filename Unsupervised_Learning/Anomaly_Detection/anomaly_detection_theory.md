# Anomaly Detection Theory

## 1. What is Anomaly Detection?
Anomaly detection is the process of finding rare observations that are significantly different from most data points.

Anomalies are also called:
- outliers
- novelties
- exceptions

## 2. Why It Matters
Anomaly detection is useful when abnormal cases are important and often risky.

Examples:
- fraud detection in transactions
- network intrusion detection
- equipment failure prediction
- manufacturing quality control
- health monitoring

## 3. Types of Anomalies
- Point anomaly: A single data point is unusual.
- Contextual anomaly: A point is abnormal only in a specific context (time, location, season).
- Collective anomaly: A group of points together looks abnormal.

## 4. Main Approaches
### Statistical methods
Assume a probability distribution and flag low-probability points.

### Distance-based methods
Points far from neighbors are treated as anomalies.

### Density-based methods
Low-density regions indicate anomalies (for example, Local Outlier Factor).

### Model-based methods
Train a model that learns normal patterns and identifies deviations.
Examples: Isolation Forest, One-Class SVM, Autoencoders.

## 5. Isolation Forest (Intuition)
Isolation Forest isolates anomalies instead of profiling normal points.

Key idea:
- anomalies are few and different
- they are easier to isolate with random splits
- fewer splits imply higher anomaly score

## 6. Important Evaluation Notes
In real anomaly tasks, labels are often limited. Evaluation can use:
- precision, recall, F1 score (if labels are available)
- ROC-AUC or PR-AUC
- manual inspection in business-critical systems

## 7. Practical Tips
- Scale features when algorithms are distance-sensitive.
- Choose contamination carefully (expected anomaly fraction).
- Validate results with domain knowledge.
- Visualize outputs whenever possible.
