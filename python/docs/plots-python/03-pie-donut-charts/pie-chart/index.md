---
layout: page
title: "Pie Chart in Python — Matplotlib Examples & Best Practices"
description: Learn how to create clear, publication-ready pie and donut charts in Python using Matplotlib, pandas and Plotly. Includes examples for labeling, percentages, exploded slices, donut charts, CSV input, and best practices for when to (and when not to) use pie charts.
keywords: pie chart, pie charts, donut chart, Python, Matplotlib, pandas, Plotly, data visualization, autopct, explode, labels, tutorial, example, CSV, charts
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

## 🥧 What Is a Pie Chart?

A **pie chart** is a circular chart divided into slices.
Each slice represents a **part of a whole**.
It helps you easily compare different categories by showing their **percentage share**.

Example:
If you surveyed 100 people about their favorite fruit:

* 40 like apples
* 30 like bananas
* 20 like mangoes
* 10 like grapes

A pie chart will show these proportions visually as slices of a circle.

---

# 🐍 How to Create a Pie Chart in Python (Beginner Guide)

To create a pie chart in Python, we use the **matplotlib** library.

## ✔️ Step 1: Install Matplotlib

If you don’t have it installed:

```bash
pip install matplotlib
```

## ✔️ Step 2: Import the Library

```python
import matplotlib.pyplot as plt
```

---

# 📘 Example 1: Basic Pie Chart

```python
import matplotlib.pyplot as plt

# Data
labels = ['Apples', 'Bananas', 'Mangoes', 'Grapes']
sizes = [40, 30, 20, 10]

# Plot
plt.pie(sizes, labels=labels)
plt.title("Favorite Fruits Pie Chart")

# Show chart
plt.show()
```

This will create a simple pie chart with labels.

---

# 📘 Example 2: Add Percentages (+ A Good-Looking Chart)

```python
import matplotlib.pyplot as plt

labels = ['Apples', 'Bananas', 'Mangoes', 'Grapes']
sizes = [40, 30, 20, 10]

plt.figure(figsize=(6,6))
plt.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',  # Show %, like 40.0%
    startangle=90       # Rotate chart for better look
)

plt.title("Favorite Fruits Distribution")
plt.show()
```

---

# 📘 Example 3: Explode (Pull Out) One Slice

```python
import matplotlib.pyplot as plt

labels = ['Apples', 'Bananas', 'Mangoes', 'Grapes']
sizes = [40, 30, 20, 10]
explode = [0.1, 0, 0, 0]  # Highlight 'Apples'

plt.pie(sizes, labels=labels, autopct='%1.1f%%', explode=explode, shadow=True)

plt.title("Pie Chart with Exploded Slice")
plt.show()
```

---

# 📘 Example 4: Pie Chart from a Dictionary

```python
import matplotlib.pyplot as plt

data = {
    'Chrome': 58,
    'Firefox': 20,
    'Edge': 12,
    'Safari': 10
}

plt.pie(data.values(), labels=data.keys(), autopct='%1.1f%%')
plt.title("Web Browser Usage")
plt.show()
```

---

# 🎯 Tips for Beginners

* Always make sure your data **adds up to a whole** (like total = 100 or sum of values).
* Use `autopct` to show percentages.
* Use `explode` to highlight important categories.
* Use `figsize=(6,6)` to control chart size.
* Pie charts are best for **3–6 categories**.

---

## 🌍 Real-World Example: CSV Data to Pie Chart in Python

---

# 📁 **Step 1: Example CSV File (traffic_data.csv)**

Create a CSV file named **`traffic_data.csv`** with the following content:

```
Source,Visitors
Search Engines,4500
Social Media,1800
Direct,2300
Referrals,900
Email,500
```

---

# 🐍 **Step 2: Python Code (Read CSV → Generate Pie Chart)**

This example uses **pandas** and **matplotlib**.

```python
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the CSV file
df = pd.read_csv("traffic_data.csv")

# Step 2: Extract data
labels = df["Source"]
sizes = df["Visitors"]

# Step 3: Plot the Pie Chart
plt.figure(figsize=(7,7))
plt.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90,
    shadow=True
)

plt.title("Website Traffic Sources - January 2025")
plt.show()
```

---

# 📊 What This Does

✔ Reads real data from a CSV file
✔ Extracts columns into lists
✔ Creates a clean pie chart
✔ Automatically calculates percentages
✔ Displays a real-world dataset from website analytics

---

# 🎯 Output

You will see a pie chart showing the distribution of visitor sources:

* Search Engines
* Social Media
* Direct
* Referral
* Email

---

