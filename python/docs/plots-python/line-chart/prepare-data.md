---
layout: page
title: Prepare Data for Python Line Charts
description: Learn how to structure and understand data for line charts in Python, including x-axis and y-axis values, monthly trends, and beginner-friendly plotting examples.
keywords: prepare data for line chart, Python dataset for plotting, Matplotlib line chart data, x-axis y-axis data, line chart data preparation, Python chart data, data visualization basics
---

## 1. Understand the Dataset

Before creating a chart, we need to understand the data.

We will use a university student enrollment dataset.

### Sample Dataset: Monthly Student Enrollment

| Month     | Students Enrolled |
| --------- | ----------------- |
| January   | 50                |
| February  | 65                |
| March     | 60                |
| April     | 80                |
| May       | 75                |
| June      | 100               |
| July      | 110               |
| August    | 95                |
| September | 120               |
| October   | 130               |
| November  | 125               |
| December  | 150               |

### Understand the rows and columns

Consider the following example:

| Month    | Students Enrolled |
| -------- | ----------------- |
| January  | 50                |
| February | 65                |

- **Rows:** Each row represents one month's enrollment information.
- **Columns:** Each column represents a type of information.
- **Category:** Month is the category used to organize the records.
- **Numerical value:** Students Enrolled represents the number of students.

### Understand the X-axis and Y-axis

A line chart normally has two axes.

# X-axis

Horizontal axis

Month

January, February, March, and so on.

# Y-axis

Vertical axis

Number of Students

50, 65, 60, 80, and so on.

### How do values become points?

Each month has a corresponding enrollment value.

For example:

| Month    | Students | Chart point   |
| -------- | -------- | ------------- |
| January  | 50       | January → 50  |
| February | 65       | February → 65 |
| March    | 60       | March → 60    |
| April    | 80       | April → 80    |

The chart places each point according to its month and numerical value.

Then, the points are connected with lines.

![Khan Academy](https://images.openai.com/static-rsc-4/EHU5sCA2XegZe1LyPPRvfbpttnjH-2iEYpj6-z6VxllnQp44Gh3kZ6a_B_MTfCYekDkrRys3dYRqkeiib65AtHMeH5jPkuNFE2zeuIwng9yrLQZfA6RpotKi2lM-YMs1UoMmqhwBLnvXXBU8IjHeh15_xd-xvH532xHIzgaCGRo?purpose=inline)

[khanacademy.org](https://www.khanacademy.org/math/4th-grade-matatag/xb1aa4507e7ecda19%3A4th-quarter/xb1aa4507e7ecda19%3Acollecting-and-organizing-data/a/solving-problems-using-data-for-at-most-two-variables-in-a-single-line-graph)

Important: The X-axis shows the order or position of the data, while the Y-axis shows the corresponding numerical values.

## 6. When to Use This Chart

### When should we use a line chart?

Use a line chart when:

1. You want to show changes over time.
2. Your data has a meaningful order.
3. You want to identify trends.
4. You want to compare changes in multiple datasets.
5. You want to identify fluctuations or sudden changes.

### Suitable data for line charts

- Daily temperature.
- Monthly sales.
- Annual population.
- Weekly attendance.
- Quarterly revenue.
- Monthly student enrollment.

### Importance of ordered data

Line charts work best when the X-axis follows a meaningful sequence.

For example:

January → February → March → April

This order makes sense because months follow a natural sequence.

However, consider these unrelated categories:

Computer Science → English → Physics → Biology

Connecting these subjects with a line may suggest a continuous progression that does not actually exist.

A bar chart would usually be more appropriate for comparing unrelated subjects.

### When NOT to use a line chart

Avoid line charts when:

- You are comparing unrelated categories.
- The data has no meaningful order.
- Connecting the points would create a misleading relationship.
- You have too many lines and the chart becomes difficult to read.
- You only need to compare individual values.

### Line Chart vs Bar Chart vs Area Chart vs Scatter Plot

| Feature         | Line Chart      | Bar Chart             | Area Chart                  | Scatter Plot            |
| --------------- | --------------- | --------------------- | --------------------------- | ----------------------- |
| Purpose         | Show trends     | Compare values        | Show trends and magnitude   | Show relationships      |
| Suitable data   | Ordered data    | Categories            | Ordered data                | Paired numerical values |
| Best use case   | Monthly sales   | Sales by product      | Population growth over time | Height vs weight        |
| Main difference | Connects points | Uses rectangular bars | Fills area below line       | Uses unconnected points |

Practical examples:

- Line chart: Monthly sales from January to December.
- Bar chart: Sales of different products.
- Area chart: Total revenue growth over time with emphasis on magnitude.
- Scatter plot: Relationship between study hours and examination marks.

## 7. Chart Components

A line chart contains several important components.

### Visual illustration

![Matplotlib - Cheatsheet](https://images.openai.com/static-rsc-4/cPWK9jbPiS8lryHPrzowfUVAFn-mMRRhpw_bamgTB-YDjN8fYA0Ef-gCPSp_dc12z4dzxeok7P7zC2OF37Ng3oYaWw5xy_RWstDVpZnmU8Ym7Se37YpRuCD9STEWOIXDmBTWHr2SaxvWX3XzJvFWTU8TvpxlgbPnJ7iSwTVLTfA?purpose=inline)

[tutorialspoint.com](https://www.tutorialspoint.com/matplotlib/matplotlib_cheatsheet.htm)

### Explanation of each component

| Component        | Explanation                                                       |
| ---------------- | ----------------------------------------------------------------- |
| Chart Title      | Describes what the chart represents.                              |
| X-axis           | Horizontal axis, usually representing time or ordered categories. |
| Y-axis           | Vertical axis, representing numerical values.                     |
| X-axis Values    | Values displayed along the horizontal axis.                       |
| Y-axis Values    | Numerical scale displayed along the vertical axis.                |
| Data Points      | Individual points representing observations.                      |
| Connecting Lines | Lines joining data points.                                        |
| Axis Labels      | Names describing each axis.                                       |
| Tick Marks       | Small marks showing positions on an axis.                         |
| Gridlines        | Reference lines that help read values.                            |
| Legend           | Identifies different lines when multiple datasets are displayed.  |

### Understand different trends

![The Register | The HCPC](https://images.openai.com/static-rsc-4/rn6tJ4epi3uGjR5K5cWeQqkHWtFrzHHVye_Xy-STxKAPExejgZH9h9m0_AsvJAIwciHRGxy9_48kuoOBiKu-V8Mm_vkV26i94qSp632Yd70ZHLJyeVpMkfSeMxdfBwHd14mSLIEZ7bh3b6YIgkAG3UKTIfUUtcC1hL0bZCPmSKY?purpose=inline)

Increasing Trend

Values move upward.

![Decreasing graph](https://images.openai.com/static-rsc-4/l-uIhPUkMK7gHNuwBdXnNGCNCHB1gboctw_3dTB002HijSEv_fqbl5UcdQnpEDRFQQeWi5LCDsN-AWiQfJaf6_GuDt_R05edl-7WMKaBILgFKAuviV3xpAsF6YKK2wLxnlAjcxjyXv-YQJ3Or3WXlf9mwQMMNYjIvUYOjnrKiiVa3QlrTkIZ2tjvpkyMNdln?purpose=inline)

Decreasing Trend

Values move downward.

![Free Tools & Spare Parts STL Download - шильдик ладаby ugadaiugadaev](https://images.openai.com/static-rsc-4/ckTz4MPRSFH5o6Bq-t7zruif6jTpqtGJU5bXFL-vNFOr8DRSmCpy4KhiCUXFlNizA0XqAwiUf1iQLTf9oL8MdB6dh2p4xSV7HcvOn8pX8zjcO1qa3yaE0jpRNgW2dpzOLrqRhOqPEkyLTqTYFBMrrTTbB4J_7naR_p4NlRCQCxA?purpose=inline)

Constant Trend

Values remain unchanged.

![chart icon vector. Icon related to graph and seo . suitable for web site, app, user interfaces, printable etc. flat line icon style. simple vector design editable](https://images.openai.com/static-rsc-4/IFpuivYb3RvGhqTfj7LTxSdUfhqcn7OGkwdgfsM2c5eIGjAIAbiySsoX418lUaIhWZ0GtyOG-44u2qyCqJbDXGy6XVlaSmwg4_IYx2DEjDBhVD5ZMbNUOE6B4wv1ssmV1Du1uwzZxveSbxUI6CFdMa7cGAQxOwHNWKEpwg7en0ZM9onBCxiS-6XyWGRTdxO6?purpose=inline)

Fluctuating Trend

Values repeatedly rise and fall.

### Multiple lines on one chart

A multiple line chart displays two or more datasets on the same chart.

For example, we can compare monthly enrollment in:

- Computer Science.
- Information Technology.

Each department gets a separate line and a legend identifies each line.

![UC Berkeley Data: Freshman Admissions for the EECS and L&S CS Majors | Ronald Kwan](https://images.openai.com/static-rsc-4/YglpzMYhS17W1THrB_P2R9yklbgXSB6fqhhFakokmH1rfgMdBv4xE5d9j-Spr8XEnG9xw9eWMzwi1AgB3DUpXSGiih9MWrh8EHCOfUcBseq-VWBRriajov4cd7lodBX97rpqEtI9p6hKVGMfl3whTTiCu3gxt9DiEOFDMl70lOI?purpose=inline)

[rkwan.me](https://rkwan.me/blog/ucb-eecs-lscs-admissions?utm_source=chatgpt.com)

**Remember:** Use different colors or markers to make multiple lines easy to distinguish.
