---
layout: page
title: "Taylor Diagram in Python: Compare Multiple Models with Matplotlib & SkillMetrics"
description: Learn how to create a Taylor Diagram in Python using Matplotlib and SkillMetrics. This guide helps you visualize and compare five models against observed data using correlation, standard deviation, and RMS
keywords: taylor diagram python, matplotlib taylor diagram, python model comparison, skillmetrics python, data visualization python, standard deviation correlation python, taylor diagram example, evaluate model accuracy python, visualize model performance, python statistics plot
author: Muhammad Yasir Bhutta
course: python
topic: matplotlib
show_toc: null
toc: toc/python.html
show_practice_progress: null
show_mini_project: null
breadcrumb:
  - title: Home
    url: /
  - title: Python
    url: /python/
---

To create a **Taylor diagram** in Python for comparing **five models** against observations, you can use the `skill_metrics` or `taylorDiagram` implementations from various libraries. Here’s a step-by-step using **Matplotlib** and **SkillMetrics**, which is commonly used in the geoscience community.

---

### ✅ **What You Need**

1. **Observed data**: The reference dataset.
2. **Model outputs**: Five different model outputs to compare.
3. **Python libraries**: `numpy`, `matplotlib`, and optionally, `skill_metrics`.

---

### 🔧 **Step-by-Step Code (Without External Library)**

Below is a **custom implementation** using only `matplotlib`.

```python
import matplotlib.pyplot as plt
import numpy as np

# Example data
obs = np.array([3.0, 3.5, 4.0, 4.5, 5.0])  # observed values

models = {
    'Model A': np.array([2.8, 3.4, 4.2, 4.7, 4.9]),
    'Model B': np.array([3.2, 3.6, 4.1, 4.4, 5.1]),
    'Model C': np.array([2.9, 3.2, 4.0, 4.3, 4.8]),
    'Model D': np.array([3.0, 3.7, 3.9, 4.6, 5.0]),
    'Model E': np.array([3.1, 3.5, 4.3, 4.5, 5.2]),
}

# Compute statistics
def compute_stats(model, obs):
    std_model = np.std(model)
    std_obs = np.std(obs)
    corr_coeff = np.corrcoef(model, obs)[0, 1]
    return std_model, corr_coeff

# Setup Taylor diagram
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, polar=True)
ax.set_theta_direction(-1)
ax.set_theta_offset(np.pi / 2)

# Reference STD
std_ref = np.std(obs)
ax.plot([0], [std_ref], 'ko', label='Observation')

# Grid and labels
rs = np.linspace(0, 1.5 * std_ref, 100)
ts = np.arccos(np.linspace(0, 1, 100))
for r in rs[::20]:
    ax.plot(ts, np.full_like(ts, r), color='gray', alpha=0.3)

# Plot each model
colors = ['r', 'g', 'b', 'm', 'c']
for i, (name, model_data) in enumerate(models.items()):
    std_model, corr = compute_stats(model_data, obs)
    theta = np.arccos(corr)
    ax.plot(theta, std_model, 'o', label=name, color=colors[i])

ax.set_title('Taylor Diagram')
ax.set_rlim(0, 1.5 * std_ref)
ax.set_rlabel_position(135)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
plt.tight_layout()
plt.show()
```

---

### 📌 Taylor Diagram Shows:

* **Radial distance**: Standard deviation
* **Angle**: Correlation coefficient
* **Distance from reference point**: Root mean square error (implicitly)

---

## 📘 **Related Topics**

* **Taylor Diagram in Python | Matplotlib Guide with Examples** – Learn what a Taylor Diagram is and how to create one using Python's Matplotlib. This beginner-friendly guide explains standard deviation, correlation, and variability with clear examples.
  👉 [Learn more](what-taylor-diagram.md)
* **Understanding Variability in Taylor Diagram | Python Matplotlib Tutorial** – Explore the concept of variability in a Taylor Diagram using Python and Matplotlib. Learn how variability helps interpret model performance with practical visualization examples.
  👉 [Learn more](variability-taylor-diagram.md)