---
layout: page
title: "confusion matrix"
description: confusion matrix
keywords: confusion matrix
author: Muhammad Yasir Bhutta
---

A **confusion matrix** is a matrix used to **evaluate the performance of a classification model** in machine learning, data analytics, and statistics.

It shows how many predictions the model got **right** and **wrong** by comparing **actual values** with **predicted values**.

---

## Confusion Table (Binary Classification)

| Actual \ Predicted | Positive                | Negative                |
| ------------------ | ----------------------- | ----------------------- |
| **Positive**       | **True Positive (TP)**  | **False Negative (FN)** |
| **Negative**       | **False Positive (FP)** | **True Negative (TN)**  |

---

## Meaning of Each Term

* **True Positive (TP)**
  Model correctly predicts **Positive**
  *(e.g., predicts “spam” and it is spam)*

* **True Negative (TN)**
  Model correctly predicts **Negative**
  *(predicts “not spam” and it is not spam)*

* **False Positive (FP)**
  Model predicts **Positive**, but actual is **Negative**
  *(also called Type-I error)*

* **False Negative (FN)**
  Model predicts **Negative**, but actual is **Positive**
  *(also called Type-II error)*

---

## Why Confusion Matrix Is Important

It helps us calculate key evaluation metrics:

* **Accuracy**
  [
  \frac{TP + TN}{TP + TN + FP + FN}
  ]

* **Precision**
  [
  \frac{TP}{TP + FP}
  ]

* **Recall (Sensitivity)**
  [
  \frac{TP}{TP + FN}
  ]

* **F1-Score**
  Harmonic mean of Precision and Recall

---

## Simple Example

Suppose we have **100 students** and predict whether they **passed or failed**:

* TP = 40 (correctly predicted pass)
* TN = 45 (correctly predicted fail)
* FP = 5 (predicted pass but actually failed)
* FN = 10 (predicted fail but actually passed)

This information forms the **confusion matrix**.

---

## Where It Is Used

* [Logistic Regression](logistic-regression.md)
* Decision Trees
* Random Forest
* Support Vector Machines (SVM)
* Deep Learning classification models

---

## Example 1: Confusion Matrix using `sklearn`

### Step 1: Import Libraries

```python
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
```

---

### Step 2: Actual and Predicted Values

```python
# Actual class labels
y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]

# Predicted class labels
y_pred = [1, 0, 0, 1, 0, 1, 1, 0, 1, 0]
```

---

### Step 3: Create Confusion Matrix

```python
cm = confusion_matrix(y_true, y_pred)
print(cm)
```

**Output**

```
[[4 1]
 [1 4]]
```

This means:

* TN = 4
* FP = 1
* FN = 1
* TP = 4

---

### Step 4: Visualize Confusion Matrix

```python
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.show()
```

---

## Example 2: Confusion Matrix with a Classification Model

### Using Logistic Regression

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
```

---

### Create Dataset

```python
X, y = make_classification(n_samples=100, random_state=42)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

---

### Train Model and Predict

```python
model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
```

---

### Generate Confusion Matrix

```python
cm = confusion_matrix(y_test, y_pred)
print(cm)
```

---

## Calculate Accuracy, Precision, Recall

```python
from sklearn.metrics import accuracy_score, precision_score, recall_score

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
```

---

## Key Takeaway

> **Confusion matrix** is used to evaluate classification models by showing
> True Positives, True Negatives, False Positives, and False Negatives.

---

