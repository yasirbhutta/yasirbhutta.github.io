---
layout: page
title: "Logistic Regression in Python | Learn Logistic Regression with Examples"
description: Learn Logistic Regression in Python — what it is, how it works, and how to implement it with practical examples using sklearn.linear_model.LogisticRegression. Perfect for beginners in statistics and machine learning.
keywords: Logistic Regression Python, Logistic Regression tutorial, Python statistics,
LogisticRegression sklearn example, binary classification Python,
sigmoid function Python, logistic vs linear regression, machine learning
author: Muhammad Yasir Bhutta
---

## 1️⃣ What is Logistic Regression?

Logistic Regression predicts the **probability** that an input belongs to a **class**.

📌 **Output is always between 0 and 1**

* `1` → Yes / True / Positive
* `0` → No / False / Negative

---

## 2️⃣ Where Do We Use Logistic Regression?

| Problem                       | Output |
| ----------------------------- | ------ |
| Student Pass / Fail           | 1 or 0 |
| Email Spam / Not Spam         | 1 or 0 |
| Disease Present / Not Present | 1 or 0 |
| Loan Approved / Rejected      | 1 or 0 |

---

## 3️⃣ Why Not Linear Regression?

Linear regression can give values like:

```
-10, 1.5, 120
```

❌ Not suitable for classification.

Logistic Regression solves this by using the **Sigmoid Function**.

---

## 4️⃣ Sigmoid Function (Heart of Logistic Regression)

**Formula:**

```
σ(z) = 1 / (1 + e^(-z))
```

📈 It converts any value into **0 to 1**.

| z value | Output |
| ------- | ------ |
| -∞      | 0      |
| 0       | 0.5    |
| +∞      | 1      |

---

## 5️⃣ How Logistic Regression Works

1️⃣ Take input features
2️⃣ Multiply by weights
3️⃣ Add bias
4️⃣ Apply **sigmoid function**
5️⃣ Convert probability to class

📌 Decision rule:

```
If probability ≥ 0.5 → Class 1
Else → Class 0
```

---

## 6️⃣ Simple Example (Student Pass/Fail)

| Study Hours | Result   |
| ----------- | -------- |
| 1           | Fail (0) |
| 2           | Fail (0) |
| 3           | Pass (1) |
| 4           | Pass (1) |
| 5           | Pass (1) |

📌 The model learns:

> “More study hours → higher chance of passing”

---

## 7️⃣ Python Example

```python
from sklearn.linear_model import LogisticRegression

X = [[1], [2], [3], [4], [5]]
y = [0, 0, 1, 1, 1]

model = LogisticRegression()
model.fit(X, y)

# Predict pass/fail for 2.5 hours
print(model.predict([[2.5]]))

# Predict probability
print(model.predict_proba([[2.5]]))
```

---

## 8️⃣ Logistic vs Linear Regression (Exam Table)

| Feature  | Linear Regression | Logistic Regression |
| -------- | ----------------- | ------------------- |
| Output   | Continuous        | Binary (0/1)        |
| Used for | Prediction        | Classification      |
| Function | Straight line     | Sigmoid curve       |
| Range    | (-∞ to +∞)        | (0 to 1)            |

---

## 9️⃣ Advantages

✅ Simple and fast
✅ Easy to interpret
✅ Works well for binary classification
✅ Less computation

---

## 🔟 Limitations

❌ Only for binary classification
❌ Assumes linear relationship
❌ Not good for complex data

---

## 📌 Key Exam Points

* Logistic Regression uses **sigmoid function**
* Output is **probability**
* Used for **classification**
* Threshold usually **0.5**

---

## 📘 **Related Topics**


