---
layout: page
title: "Boxplot in Matplotlib: Create Box and Whisker Plots in Python"
description: Learn how to create boxplots in Python using Matplotlib. Visualize distributions, identify outliers, and compare data groups with clear examples and code.
keywords: boxplot matplotlib, boxplot python, box and whisker plot matplotlib, matplotlib boxplot example, python data visualization, compare distributions python, matplotlib tutorial, outliers in boxplot, data visualization with matplotlib, boxplot guide
author: Muhammad Yasir Bhutta
course: python
topic: matplotlib
show_toc: null
toc: toc/python.html
show_practice_progress: null
show_mini_project: null
- title: Python Visualization
url: /python/lesson-plans/45-day-python-plotting-plan-matplotlib-seaborn-plotly.html
---


```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data
df = pd.read_excel("MODEL1Test.xlsx")

# Separate observed and model data
obs = df['Actual FS']
models = df.drop(columns='Actual FS')

# Compute statistics
def compute_stats(model, obs):
    std_model = np.std(model)
    corr_coeff = np.corrcoef(model, obs)[0, 1]
    return std_model, corr_coeff

# Setup Taylor diagram - 1/4 circle
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, polar=True)
ax.set_theta_direction(-1)
ax.set_theta_offset(np.pi / 2)
ax.set_thetamin(0)      # 0 degrees
ax.set_thetamax(90)     # 90 degrees

# Reference STD
std_ref = np.std(obs)
ax.plot([0], [std_ref], 'ko', label='Obs')

# Grid circles
rs = np.linspace(0, 1.5 * std_ref, 100)
ts = np.arccos(np.linspace(0, 1, 100))
for r in rs[::20]:
    ax.plot(ts, np.full_like(ts, r), color='gray', alpha=0.3)

# Plot models
colors = ['r', 'g', 'b', 'm', 'c']
for i, column in enumerate(models.columns):
    model_data = models[column].values
    std_model, corr = compute_stats(model_data, obs)
    theta = np.arccos(corr)
    ax.plot(theta, std_model, 'o', label=column, color=colors[i % len(colors)])

# Replace angle labels with correlation values
corr_ticks = [1.0, 0.95, 0.9, 0.8, 0.7, 0.6,0.5,0.4,0.3,0.2,0.1,0]
theta_labels = [np.arccos(c) for c in corr_ticks]
ax.set_xticks(theta_labels)
ax.set_xticklabels([str(c) for c in corr_ticks])

# Axis settings
ax.set_title('Taylor Diagram', pad=30)
ax.set_rlim(0, 1.5 * std_ref)
ax.set_rlabel_position(135)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1), fontsize='5')
plt.tight_layout()
plt.show()
```
