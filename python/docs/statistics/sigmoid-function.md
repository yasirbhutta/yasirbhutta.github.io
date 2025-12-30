---
layout: page
title: "Python Sigmoid Function | Definition & Code Examples"
description: Learn what the sigmoid function is in Python, how it works in machine learning and statistics, and see easy code examples using Python. Perfect for beginners.
keywords: Python sigmoid function, sigmoid function Python examples, sigmoid activation function, Python statistics sigmoid, machine learning sigmoid, logistic function in Python
author: Muhammad Yasir Bhutta
---

## 📌 What is the **Sigmoid Function**?

The **sigmoid function** is a mathematical function that **converts any number into a value between 0 and 1**.

👉 That value can be understood as a **probability**.

---

## 2️⃣ Why Do We Need the Sigmoid Function?

In Machine Learning, many problems require answers like:

* Yes / No
* True / False
* Pass / Fail
* Spam / Not Spam

Numbers like `-5`, `10`, or `100` are **not useful** for these decisions.

📌 The sigmoid function **fixes this problem** by converting numbers into probabilities.

---

## 3️⃣ Sigmoid Function Formula

[
\text{Sigmoid}(z) = \frac{1}{1 + e^{-z}}
]

Where:

* `z` = input value (can be any number)
* `e` ≈ 2.718 (a mathematical constant)

---

## 4️⃣ What Does the Sigmoid Function Do?

| Input (z) | Output |
| --------- | ------ |
| -10       | 0.000  |
| -2        | 0.12   |
| 0         | 0.50   |
| 2         | 0.88   |
| 10        | 0.999  |

📌 Key idea:

* Large negative → **close to 0**
* Zero → **0.5**
* Large positive → **close to 1**

---

## 5️⃣ Shape of Sigmoid Function

* Looks like a **smooth S-shaped curve**
* Left side → flat near **0**
* Middle → steep rise
* Right side → flat near **1**

This makes it perfect for **classification problems**.

---

## 6️⃣ Real-Life Example

### 🎓 Student Pass / Fail

Suppose a model calculates:

```
z = study_hours × weight + bias
```

| z value | Probability | Decision   |
| ------- | ----------- | ---------- |
| -1.5    | 0.18        | Fail       |
| 0.0     | 0.50        | Borderline |
| 2.0     | 0.88        | Pass       |

📌 Rule:

```
If probability ≥ 0.5 → Pass
Else → Fail
```

---

## 7️⃣ Where Is Sigmoid Used?

✔ Logistic Regression
✔ Binary Classification
✔ Neural Networks (activation function)
✔ Data Science decision models

---

## 8️⃣ Simple Python Example

```python
import math

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

print(sigmoid(-2))
print(sigmoid(0))
print(sigmoid(2))
```

---

## 9️⃣ Advantages of Sigmoid Function

✅ Output between 0 and 1
✅ Easy to understand
✅ Works well for probabilities
✅ Smooth and continuous

---

## 🔟 Limitations (Beginner Note)

❌ Can be slow for deep neural networks
❌ Suffers from vanishing gradient problem
❌ Mostly used for **binary outputs**

---

## ⭐ Key Points

* Sigmoid converts numbers into **probabilities**
* Output range is **0 to 1**
* Used mainly in **Logistic Regression**
* Decision boundary is **0.5**
* Shape is **S-curve**

---

## 📈 Sigmoid Curve (Logistic Function)

The **sigmoid curve** is an **S-shaped curve** used in **Logistic Regression** to convert values into **probabilities between 0 and 1**.

---

## 1️⃣ What is a Sigmoid Curve?

The sigmoid function maps **any real number** into a value **between 0 and 1**.

### 📌 Formula

[
\sigma(z) = \frac{1}{1 + e^{-z}}
]

Where:

* `z` = weighted sum of inputs
* `e` = Euler’s number (≈ 2.718)

---

## 2️⃣ Why Do We Use the Sigmoid Curve?

Because classification problems need:

* ✔ Probabilities
* ✔ Clear decision boundary (Yes/No)

📌 Output interpretation:

* Close to **0** → Class 0 (No)
* Close to **1** → Class 1 (Yes)

---

## 3️⃣ Shape of Sigmoid Curve (Easy Explanation)

| z value | Sigmoid Output |
| ------- | -------------- |
| -∞      | 0              |
| -2      | 0.12           |
| 0       | 0.5            |
| +2      | 0.88           |
| +∞      | 1              |

📈 **Key features**

* Smooth **S-shape**
* Center point at **0.5**
* Never touches exactly **0 or 1**

---

## 4️⃣ Classroom Example (Pass / Fail)

| Study Hours (z) | Probability of Pass |
| --------------- | ------------------- |
| 1               | 0.20                |
| 2               | 0.35                |
| 3               | 0.50                |
| 4               | 0.75                |
| 5               | 0.90                |

📌 Decision rule:

```
Probability ≥ 0.5 → Pass
Else → Fail
```

---

## 5️⃣ Visual Description (For Notes)

Imagine:

* Left side → flat near **0**
* Middle → steep increase
* Right side → flat near **1**

This makes classification **stable and reliable**.

---

## 6️⃣ Simple Python Code to Plot Sigmoid Curve

```python
import numpy as np
import matplotlib.pyplot as plt

z = np.linspace(-10, 10, 100)
sigmoid = 1 / (1 + np.exp(-z))

plt.plot(z, sigmoid)
plt.xlabel("z")
plt.ylabel("Sigmoid(z)")
plt.title("Sigmoid Curve")
plt.show()
```

---

## 7️⃣ Key Exam Points ⭐

* Sigmoid converts values to **probability**
* Output range: **0 to 1**
* Used in **Logistic Regression**
* Decision boundary at **0.5**
* Shape is **S-curve**

---

## 8️⃣ One-Line Definition

**“The sigmoid curve is an S-shaped function that converts input values into probabilities between 0 and 1.”**

---

## 📘 **Related Topics**

