---
layout: page
title: Data Visualization in Python
description: Learn Python variables with this beginner-friendly guide. Understand variable naming rules, assignments, and operations with examples and exercises. Perfect for students and professionals starting their Python journey.
keywords: Python variables, Python variable examples, Python variable exercises, Python variable naming rules, Python variable assignment, Python beginner tutorials, Python programming basics, learn Python variables, Python coding exercises
toc: toc/python.html
---

Data visualization in Python is typically done with libraries like `Matplotlib` and `Seaborn`, which provide tools for creating a variety of plots, charts, and other visualizations. Below is a breakdown of key plotting and data visualization techniques.

## 1. **Basic Plotting with Matplotlib**

   `Matplotlib` is one of the foundational libraries for data visualization in Python. It offers a range of functions for creating static, animated, and interactive visualizations.

   ```python
   import matplotlib.pyplot as plt

   # Simple line plot
   x = [1, 2, 3, 4, 5]
   y = [1, 4, 9, 16, 25]
   plt.plot(x, y, marker='o', color='b', linestyle='-')
   plt.title("Simple Line Plot")
   plt.xlabel("X-axis")
   plt.ylabel("Y-axis")
   plt.show()
   ```

**See also:**

- “matplotlib.markers — Matplotlib 3.4.2 documentation,” matplotlib.org. <https://matplotlib.org/stable/api/markers_api.html>
- [Markers in Matplotlib](https://e2eml.school/matplotlib_points.html)
‌

## . **Bar Plots**
   Bar plots display data using rectangular bars. They are commonly used for categorical data comparison.

   ```python
   categories = ['A', 'B', 'C', 'D']
   values = [4, 7, 1, 8]

   plt.bar(categories, values, color='teal')
   plt.title("Bar Plot")
   plt.xlabel("Categories")
   plt.ylabel("Values")
   plt.show()
   ```
### Task 
https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_colors.html


## 4. **Histograms**
   Histograms display the distribution of data by grouping it into bins. They are helpful for identifying patterns and distributions in data.

   ```python
   data = np.random.randn(1000)

   plt.hist(data, bins=30, color='purple', edgecolor='black')
   plt.title("Histogram")
   plt.xlabel("Data Values")
   plt.ylabel("Frequency")
   plt.show()
   ```

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1602443888929206"
     crossorigin="anonymous"></script>
<ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-1602443888929206"
     data-ad-slot="6296238623"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

## 5. **Pie Charts**
   Pie charts show proportions of a whole and are best used for data with a limited number of categories.

   ```python
   labels = ['Category 1', 'Category 2', 'Category 3', 'Category 4']
   sizes = [15, 30, 45, 10]
   explode = (0, 0.1, 0, 0)  # "explode" Category 2 for emphasis

   plt.pie(sizes, labels=labels, explode=explode, autopct='%1.1f%%', startangle=140)
   plt.title("Pie Chart")
   plt.show()
   ```

   In the context of `matplotlib.pyplot.pie()`:

1. **`autopct`**:
   - This parameter specifies the format in which the percentage of each pie slice should be displayed on the chart.
   - It accepts a format string or a callable function.
   - Example: 
     - `'%1.1f%%'` displays the percentage with one decimal place followed by the `%` sign.
     - `'%1.0f%%'` displays the percentage as a whole number (no decimal places).
     - A callable function can be used to define custom formatting.
   - If you don't specify `autopct`, no percentages will be displayed on the pie slices.

2. **`startangle`**:
   - This parameter specifies the starting angle of the pie chart, measured counterclockwise from the positive x-axis.
   - The value is in degrees.
   - Example: 
     - `startangle=180` rotates the pie chart so that the first slice starts from the bottom (180 degrees from the positive x-axis).
     - `startangle=90` positions the first slice at the top (90 degrees counterclockwise from the positive x-axis).
   - By default, `startangle=0`, so the first slice starts on the positive x-axis.

### Output:
- **`autopct='%1.1f%%'`**: Displays percentages with one decimal place on the slices.
- **`startangle=180`**: Rotates the pie chart so that the first slice starts at the bottom.

## 2. **Scatter Plots**
   Scatter plots are useful for displaying the relationship between two continuous variables. They can reveal correlations, clusters, and trends.

   ```python
   import numpy as np

   # Generating random data
   x = np.random.rand(50)
   y = np.random.rand(50)
   colors = np.random.rand(50)
   sizes = 1000 * np.random.rand(50)

   # Scatter plot with color and size variation
   plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='viridis')
   plt.colorbar()
   plt.title("Scatter Plot")
   plt.xlabel("X-axis")
   plt.ylabel("Y-axis")
   plt.show()
   ```

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1602443888929206"
     crossorigin="anonymous"></script>
<ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-1602443888929206"
     data-ad-slot="6296238623"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

## 6. **Box Plots**
   Box plots show the distribution of data and outliers within a dataset. They display the minimum, first quartile, median, third quartile, and maximum of a data set.

   ```python
   data = [np.random.normal(0, std, 100) for std in range(1, 4)]
   plt.boxplot(data, patch_artist=True)
   plt.title("Box Plot")
   plt.xlabel("Category")
   plt.ylabel("Values")
   plt.show()
   ```

## 7. **Heatmaps**
   Heatmaps represent data in a matrix format, with color intensity representing values. They're often used in data analysis for displaying correlation matrices.

   ```python
   import seaborn as sns

   # Generating random data for a heatmap
   data = np.random.rand(10, 12)
   sns.heatmap(data, annot=True, cmap='coolwarm')
   plt.title("Heatmap")
   plt.show()
   ```

## 8. **Line Plots**
   Line plots are effective for time series data or continuous data. They can help identify trends over time.

   ```python
   time = np.arange(0., 5., 0.2)
   plt.plot(time, time**2, 'r--', label='y = x^2')
   plt.plot(time, time**3, 'bs', label='y = x^3')
   plt.title("Line Plot")
   plt.xlabel("Time")
   plt.ylabel("Values")
   plt.legend()
   plt.show()
   ```

## 9. **Pair Plots**
   Pair plots (also called scatterplot matrices) are a great way to visualize the relationships between multiple variables. They’re commonly used in exploratory data analysis.

   ```python
   # Loading a sample dataset
   data = sns.load_dataset("iris")
   sns.pairplot(data, hue="species")
   plt.show()
   ```

## 10. **Violin Plots**
   Violin plots combine aspects of box plots and KDEs (Kernel Density Estimation). They show the distribution of the data, including peaks and valleys.

   ```python
   data = sns.load_dataset("tips")
   sns.violinplot(x="day", y="total_bill", data=data, palette="muted")
   plt.title("Violin Plot")
   plt.show()
   ```

## 11. **Subplots**
   Subplots allow for multiple plots in a single figure, useful for comparing different datasets or visualizations side by side.

   ```python
   # Creating a 2x2 grid of subplots
   fig, axs = plt.subplots(2, 2)

   axs[0, 0].plot(x, y)
   axs[0, 0].set_title("Line Plot")

   axs[0, 1].scatter(x, y, color='orange')
   axs[0, 1].set_title("Scatter Plot")

   axs[1, 0].hist(data, color='purple')
   axs[1, 0].set_title("Histogram")

   axs[1, 1].bar(categories, values, color='teal')
   axs[1, 1].set_title("Bar Plot")

   plt.tight_layout()
   plt.show()
   ```

### Summary Table of Visualization Techniques

| Visualization Type | Library Function       | Description                                     |
|--------------------|------------------------|-------------------------------------------------|
| Line Plot          | `plt.plot()`           | Displays trends over continuous data or time    |
| Scatter Plot       | `plt.scatter()`        | Shows relationship between two variables        |
| Bar Plot           | `plt.bar()`            | Compares categories                             |
| Histogram          | `plt.hist()`           | Shows data distribution                         |
| Pie Chart          | `plt.pie()`            | Displays proportions of a whole                 |
| Box Plot           | `plt.boxplot()`        | Shows distribution and outliers                 |
| Heatmap            | `sns.heatmap()`        | Shows intensity matrix, ideal for correlations  |
| Pair Plot          | `sns.pairplot()`       | Relationship matrix for multiple variables      |
| Violin Plot        | `sns.violinplot()`     | Shows data distribution and density             |
| Subplots           | `plt.subplots()`       | Multiple plots within a single figure           |

Both `Matplotlib` and `Seaborn` offer extensive customization options, including color palettes, labeling, legends, and layout adjustments. This combination of plotting libraries makes Python highly versatile for data visualization. Let me know if you'd like more details on any specific plotting technique!

## Key Terms

## True/False (Mark T for True and F for False)

**Answer Key (True/False):**

## Multiple Choice (Select the best answer)

1. **Which function would you use to determine the type of a variable in Python?**
   - A) id()
   - B) type()
   - C) str()
   - D) isinstance()
  
**Watch this video for the answer:**

**Answer key (Mutiple Choice):**

## Fill in the Blanks

**Answer Key (Fill in the Blanks):**

## Exercises

### Beginner: Basic concepts and syntax.

### Intermediate: More complex problems involving data structures and algorithms.

### Advanced: Challenging problems that require in-depth understanding and optimization.

## Review Questions

## References and Bibliography

- [1] Y. Holtz, “Python Graph Gallery,” The Python Graph Gallery. <https://python-graph-gallery.com/>
‌

For more details, see Appendix A.

## **Appendices**

### **Appendix A: Data Tables**

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1602443888929206"
     crossorigin="anonymous"></script>
<!-- display square -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-1602443888929206"
     data-ad-slot="9845543342"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
