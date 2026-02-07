---
layout: page
title: "Introduction to Regression & Regression Models in Python | Tutorial & Examples"
description: Learn the introduction to regression and regression models in Python. Understand regression concepts, build regression models, and see practical Python examples using scikit-learn and statsmodels.
keywords: Introduction to Regression, Regression Model Python, Python regression tutorial, Regression modeling in Python, Linear regression Python, Multiple regression Python, Regression analysis Python examples, Scikit-learn regression
author: Muhammad Yasir Bhutta
---

## Introduction to Regression

Regression is a **statistical and machine learning technique** used to understand the relationship between a **dependent variable (output)** and one or more **independent variables (inputs)**. The main goal of regression is to **predict continuous values** and **analyze how changes in inputs affect the output**.

In simple words, regression helps us answer questions like:

* How does house price change with area?
* How does salary increase with years of experience?
* How does temperature affect electricity consumption?

Regression models find the **best-fit line or curve** that represents the relationship between variables based on historical data.

---

## Why Regression Is Important

Regression is widely used because it:

* Helps in **prediction and forecasting**
* Shows **cause-and-effect relationships**
* Is easy to interpret and explain
* Forms the foundation of many **machine learning algorithms**

---

## Types of Regression

Some common types of regression include:

* **Linear Regression** – Used when the relationship is linear
* **Multiple Linear Regression** – Uses more than one independent variable
* **Polynomial Regression** – Fits curved relationships
* **Logistic Regression** – Used for classification problems
* **Ridge & Lasso Regression** – Used to reduce overfitting

---

## Basic Regression Equation

A simple linear regression model is represented as:

[
y = mx + c
]

Where:

* ( y ) = dependent variable
* ( x ) = independent variable
* ( m ) = slope (effect of x on y)
* ( c ) = intercept

---


A **regression model** is a **machine learning / statistical model** used to **predict a continuous numerical value** based on one or more input variables.

---

## 1️⃣ What is a Regression Model?

- A regression model finds the **relationship between variables**.
- Regression is the technique; a regression model is the mathematical model created using that technique.
  
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

## 3️⃣ Simple Example

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

## 📘 **Related Topics**

- [Logistic Regression in Python /| Learn Logistic Regression with Examples](logistic-regression.md)
- [Introduction to Confusion Matrix in Python /| Classification Evaluation](confusion-matrix.md)
  