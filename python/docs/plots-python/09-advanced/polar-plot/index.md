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

### 🧭 What is a **Polar Plot**?

A **polar plot** is a type of plot where data is displayed using **angles and radial distances** instead of Cartesian x-y coordinates.

---

### 📌 Key Features:

| Element        | Description                                                       |
| -------------- | ----------------------------------------------------------------- |
| **Angle (θ)**  | Represents the direction or **correlation** (in Taylor diagrams). |
| **Radius (r)** | Represents the **magnitude**, often standard deviation.           |
| **Center**     | Called the **origin**, where `r = 0`.                             |

---

### 🌀 How It Works:

In a polar plot:

* A point is located by how **far it is from the center** (radial distance)
  and the **angle** it makes with a reference direction (often 0° or 90°).
* Think of a radar screen or compass.

---

### 📊 Used In:

* **Taylor diagrams**
* **Wind direction and speed plots**
* **Circular statistics**
* **Phase angle plots**

---

## 🎯 Goal: Plot angles and magnitudes (like points on a compass)

```python
import matplotlib.pyplot as plt
import numpy as np

# Example angles (in degrees) and magnitudes
angles_deg = [0, 45, 90, 135, 180, 225, 270, 315]
magnitudes = [1, 2, 1.5, 3, 2.5, 2, 1, 1.8]

# Convert degrees to radians for polar plot
angles_rad = np.deg2rad(angles_deg)

# Create polar plot
plt.figure(figsize=(6, 6))
ax = plt.subplot(111, polar=True)  # 111 means 1x1 grid, 1st plot

# Plot the data
ax.plot(angles_rad, magnitudes, marker='o')

# Add title
ax.set_title("Simple Polar Plot", va='bottom')

# Show the plot
plt.show()
```

---

### 🔍 Explanation:

* `angles_deg`: Compass directions like North (0°), East (90°), South (180°), etc.
* `magnitudes`: Distance from the center for each direction.
* `np.deg2rad()`: Converts degrees to radians since `matplotlib` uses radians.
* `polar=True`: Tells matplotlib to use polar coordinates.

---

### **customized polar plot example** with:

* ✅ **Filled area**
* 🎨 Custom **colors**
* 🏷️ Labeled angles (like a compass)

---

### 🌈 Polar Plot with Area Fill

```python
import matplotlib.pyplot as plt
import numpy as np

# Compass directions in degrees
angles_deg = [0, 45, 90, 135, 180, 225, 270, 315]
magnitudes = [1, 2, 1.5, 3, 2.5, 2, 1, 1.8]

# Convert degrees to radians
angles_rad = np.deg2rad(angles_deg)

# Repeat first point to close the circular shape
angles_rad = np.append(angles_rad, angles_rad[0])
magnitudes.append(magnitudes[0])

# Create plot
plt.figure(figsize=(7, 7))
ax = plt.subplot(111, polar=True)

# Plot line and fill area
ax.plot(angles_rad, magnitudes, color='teal', linewidth=2, label='Measurements')
ax.fill(angles_rad, magnitudes, color='skyblue', alpha=0.4)

# Set title and labels
ax.set_title("🌍 Compass Polar Plot", va='bottom')
ax.set_xticks(np.deg2rad(angles_deg))
ax.set_xticklabels(['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'])

# Add legend
ax.legend(loc='upper right')

# Show plot
plt.show()
```

---

### 📌 What This Shows:

* The shape connects all points and fills the area.
* Labels around the circle match compass directions (North, East, etc.).
* `fill()` makes the plot visually intuitive and engaging.

---

### 📊 Polar Plot Example: Sales by Region

```python
import matplotlib.pyplot as plt
import numpy as np

# Define sales regions and sales figures
regions = ['North', 'North-East', 'East', 'South-East', 'South', 'South-West', 'West', 'North-West']
sales = [120, 150, 130, 180, 160, 140, 110, 170]

# Convert region positions to angles (in radians)
angles = np.linspace(0, 2 * np.pi, len(regions), endpoint=False).tolist()

# Close the circular plot by repeating the first point
sales += [sales[0]]
angles += [angles[0]]

# Create polar plot
plt.figure(figsize=(8, 6))
ax = plt.subplot(111, polar=True)

# Plot the line and fill the area
ax.plot(angles, sales, color='navy', linewidth=2, label='Sales')
ax.fill(angles, sales, color='skyblue', alpha=0.4)

# Set region names around the circle
ax.set_xticks(angles[:-1])  # exclude last repeated angle
ax.set_xticklabels(regions)

# Title and legend
ax.set_title("📈 Sales Distribution by Region", pad=30)
ax.legend(loc='upper right')

# Show plot
plt.show()
```

---

### 🧠 What's Happening Here:

* Each region is mapped to a direction around the circle.
* The **distance from the center (radial distance)** shows the **sales amount**.
* The filled area makes it easier to **compare sales visually** across regions.



