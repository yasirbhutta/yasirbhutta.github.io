---
layout: page
title: "Regression model"
description: regression model
keywords: regression model, yasir, bhutta
author: Muhammad Yasir Bhutta
---

A **regression model** is a **machine learning / statistical model** used to **predict a continuous numerical value** based on one or more input variables.

---

## 1️⃣ What is a Regression Model?

A regression model finds the **relationship between variables**.

📌 **Example**

* Predict **house price** based on:

  * size (sq ft)
  * number of rooms
  * location

Here:

* **Input (X)** → size, rooms, location
* **Output (Y)** → price (a number)

---

## 2️⃣ Why Do We Use Regression?

We use regression to:
✔ Predict values
✔ Understand relationships
✔ Analyze trends

📌 **Common predictions**

* Student marks
* Salary
* Sales
* Temperature
* House prices

---

## 3️⃣ Simple Example (Classroom Friendly)

### Predict marks based on study hours

| Study Hours | Marks |
| ----------- | ----- |
| 1           | 35    |
| 2           | 45    |
| 3           | 55    |
| 4           | 65    |
| 5           | 75    |

📈 The model learns:

> “As study hours increase, marks increase.”

---

## 4️⃣ Types of Regression Models

### 🔹 1. Linear Regression

Most basic and commonly used.

**Formula:**

```
y = mx + b
```

* `x` → input
* `y` → output
* `m` → slope
* `b` → intercept

📌 Example:

```
Marks = 10 × StudyHours + 25
```

---

### 🔹 2. Multiple Linear Regression

Uses **more than one input**

📌 Example:

```
Salary = Experience + Education + Skills
```

---

### 🔹 3. Polynomial Regression

Used when data is **curved**, not straight.

📌 Example:

* Speed vs fuel consumption

---

### 🔹 4. Logistic Regression (Special Case)

Used for **Yes/No** outcomes (classification).

📌 Example:

* Pass / Fail
* Spam / Not Spam

⚠ Although named “regression”, it’s used for **classification**.

---

## 5️⃣ Python Example

```python
from sklearn.linear_model import LinearRegression

# Input data (study hours)
X = [[1], [2], [3], [4], [5]]
y = [35, 45, 55, 65, 75]

model = LinearRegression()
model.fit(X, y)

# Predict marks for 6 hours
print(model.predict([[6]]))
```

---

## 6️⃣ Real-Life Activities for Students 👨‍🏫

✔ Measure **height vs weight**
✔ Predict **electricity bill** from units
✔ Predict **sales** from advertising cost
✔ Predict **marks** from attendance

---

## 7️⃣ Key Points to Remember

✅ Regression predicts **numbers**
✅ Shows **relationship between variables**
✅ Linear regression draws a **best-fit line**
✅ Widely used in **ML, data science, economics**

---


