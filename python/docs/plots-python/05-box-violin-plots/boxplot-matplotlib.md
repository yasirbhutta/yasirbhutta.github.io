---
layout: page
title: "Taylor Diagram in Python using Matplotlib and Pandas | Visualize Model Performance"
description: Learn how to create a Taylor Diagram in Python using Matplotlib and Pandas. This guide explains model evaluation through standard deviation, correlation, and performance visualization with clear code examples.
keywords: Taylor diagram Python, Taylor diagram matplotlib, Python Taylor plot, model evaluation Python, Taylor diagram tutorial, Taylor diagram with pandas, matplotlib Taylor diagram, visualize model accuracy Python, standard deviation correlation Python, Python model comparison chart
author: Muhammad Yasir Bhutta
course: python
topic: plots-python
show_toc: null
toc: toc/python.html
show_practice_progress: null
show_mini_project: null
breadcrumb:
  - title: Home
    url: /
  - title: Python
    url: /python/
  - title: Python Visualization 
    url: /python/lesson-plans/45-day-python-plotting-plan-matplotlib-seaborn-plotly.html
---

## Table of Contents

1. What is a Box Plot (Box-and-Whisker Plot)?
2. How Outliers Are Determined in a Box Plot

## 📦 What is a Box Plot (Box-and-Whisker Plot)?

A **box plot** is a graphical summary of data distribution. It helps visualize:

* **Median (middle value)**
* **Quartiles (25th and 75th percentiles)**
* **Minimum and Maximum (within limits)**
* **Outliers (data points that fall outside 1.5×IQR)**

It's great for comparing distributions across **multiple datasets**.([atlassian][1])

---

### 📊 Structure of a Box Plot

![box plot](https://wac-cdn.atlassian.com/dam/jcr:3ecc2cdd-2878-4b9f-a853-f0d1782ad285/box-plot-construction.png)
Image source: [www.atlassian.com](https://www.atlassian.com/data/charts/box-plot-complete-guide)

* **Q1**: 25th percentile
* **Q2 (Median)**: 50th percentile
* **Q3**: 75th percentile
* **IQR**: Q3 - Q1
* **Whiskers**: Extend to 1.5 × IQR or actual min/max
* **Dots**: Outliers
---

### 🐍 Simple Example in Matplotlib

```python
import matplotlib.pyplot as plt
import numpy as np

# Example datasets
np.random.seed(0)
model_A = np.random.normal(70, 10, 100)
model_B = np.random.normal(75, 15, 100)
model_C = np.random.normal(65, 20, 100)

data = [model_A, model_B, model_C]

# Updated box plot with tick_labels
plt.figure(figsize=(8, 5))
plt.boxplot(data, tick_labels=['Model A', 'Model B', 'Model C'], patch_artist=True)

plt.title('Box Plot Example: Model Score Distributions')
plt.ylabel('Scores')
plt.grid(True)
plt.show()
```
![box plot](https://res.cloudinary.com/da0pjikvw/image/upload/c_pad,w_512/v1749806015/box-plot_nzy0jw.png)

---

### ✅ Output Explanation:

* Each **box** shows the spread of scores.
* You can quickly compare:

  * Which model has higher median
  * Which model is more consistent (smaller IQR)
  * Presence of outliers

---

Great question! A **box plot** is specifically designed to help you **identify outliers** in your dataset.

---

## 📦 **How Outliers Are Determined in a Box Plot**

Box plots use the **Interquartile Range (IQR)** to find outliers.

#### ✅ Definitions:

* **Q1**: First quartile (25th percentile)
* **Q3**: Third quartile (75th percentile)
* **IQR**: Q3 − Q1

#### 🚨 **Outlier Rule:**

Any data point is considered an **outlier** if it is:

* **< Q1 − 1.5 × IQR**
* **> Q3 + 1.5 × IQR**

These points will show up as **individual dots** **outside the whiskers** in a box plot.

---

### 🐍 Python Example Using Matplotlib and NumPy

```python
import numpy as np
import matplotlib.pyplot as plt

# Sample data with outliers
data = np.array([12, 13, 14, 15, 16, 17, 18, 30])  # 40 is an outlier

# Box plot
plt.boxplot(data, vert=False, patch_artist=True)
plt.title("Box Plot with Outlier")
plt.xlabel("Value")
plt.grid(True)
plt.show()

# Calculate outlier thresholds
Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = data[(data < lower_bound) | (data > upper_bound)]

print("Outliers:", outliers)
```

---

### 📤 Output:

* Box plot showing a dot at **30**
* Console prints:

  ```
  Outliers: [30]
  ```

---

### ✅ Summary:

* **Box = middle 50% of data (Q1 to Q3)**
* **Whiskers = within 1.5×IQR**
* **Dots beyond whiskers = outliers**


## References and Bibliography

[1]: https://www.atlassian.com/data/charts/box-plot-complete-guide "A complete guide to box plots"
