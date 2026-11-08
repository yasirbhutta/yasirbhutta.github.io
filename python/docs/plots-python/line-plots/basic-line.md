---
layout: page
title: Basic Line
description: Documentation and resources for Basic Line.
keywords: basic, line, 01-line-plots, plots-python, docs
---

# Line Charts in Python Using Matplotlib

Complete Beginner-Friendly Lesson · Data Visualization · Python



Beginner Level

15 Sections



## Lesson Overview

A line chart is one of the most useful charts for understanding how values change over time. In this lesson, students will learn to prepare data, create line charts using Python's Matplotlib library, customize charts, and interpret trends.

Teaching sequence:

Example → Understand the Data → Create the Chart → Interpret the Results → Modify the Chart → Practice

Main library: Matplotlib

Required knowledge: Basic Python variables, lists, and the `print()` function.

# Part A – Understand

## 1. Learning Objectives

After completing this lesson, students will be able to:

1. Define a line chart and explain its purpose.
2. Identify situations where a line chart is appropriate.
3. Understand the X-axis, Y-axis, data points, and connecting lines.
4. Prepare a dataset for line chart visualization.
5. Create basic line charts using Python and Matplotlib.
6. Add titles, labels, markers, gridlines, and legends.
7. Customize line colors, styles, sizes, and axis limits.
8. Create multiple line charts to compare different datasets.
9. Identify increasing, decreasing, constant, and fluctuating trends.
10. Interpret information presented in a line chart.
11. Save a line chart as an image.
12. Select an appropriate chart for a given dataset.

## 2. Introduction

### What is a Line Chart?

A Line Chart is a type of graph that displays information using points connected by straight lines.

It helps us understand how something changes over a period of time.

### Real-life example: Daily temperature

Imagine that you record the temperature of your city at different times during the day.

| Time  | Temperature |
| ----- | ----------- |
| 8 AM  | 20°C        |
| 10 AM | 24°C        |
| 12 PM | 30°C        |
| 2 PM  | 34°C        |
| 4 PM  | 31°C        |
| 6 PM  | 27°C        |

We can represent this information using a line chart.

[Blended Learning](https://images.openai.com/static-rsc-4/I0XvXML3uac3W-IUPhXl-vXqMR4iHj55Quz8wc59K-a_m8koxBe9p0cGCux0SKZ-47gqsLlhcDQQdZE_N_FHrQbWUOsyUJpTJLogFI7q3FYij6a04LYeWPS0_3cvlKOvTmG8YUU_yN2NMvqD_XrxExvnXYY86MHhqozsV_9t8zQ?purpose=inline)

[blended-learning.resources.wjec.co.uk](https://blended-learning.resources.wjec.co.uk/en/mfw24-25_1-2/0/6?utm_source=chatgpt.com)

### How does it work?

A line chart works in three simple steps:

1. Select data: Collect values, such as daily temperatures.
2. Plot points: Represent each value as a point on the chart.
3. Connect points: Join the points using straight lines.

The connected line helps us see whether temperature is increasing, decreasing, or changing.

### Why do we use line charts?

Line charts are particularly useful for showing changes over time, such as:

- Monthly student enrollment.
- Daily attendance.
- Monthly business sales.
- Annual examination results.
- Daily weather conditions.

Remember: A line chart helps answer the question: How has something changed over time?

## 3. Purpose and Applications

The main purpose of a line chart is to display changes and patterns in numerical data.

### What information does it communicate?

| Information      | Explanation                                    |
| ---------------- | ---------------------------------------------- |
| Increasing trend | Values are going up.                           |
| Decreasing trend | Values are going down.                         |
| Constant trend   | Values remain almost the same.                 |
| Fluctuation      | Values repeatedly increase and decrease.       |
| Pattern          | A repeated or recognizable change in values.   |
| Comparison       | Different lines can compare multiple datasets. |

### Applications in different fields

[Academics](https://images.openai.com/static-rsc-4/AImB8bm0VL_2zKmJibuq6Tc9R9x4OBqxhaNozx-MnuE1bpDBGJ-ZaKVAw9aRxN5XZasuwSasyDA8Gc1Vk0NbHts7Vbj7aWumMytDUwMxqQP5L4nEORCxFOoX-WcBIZO7iGki7lYl6iShv8QLxcVj0G9JGKfIDCGDg7Fk6c4eBfg?purpose=inline)

Education

Universities can monitor monthly enrollment, daily attendance, and annual examination performance.

[Home](https://images.openai.com/static-rsc-4/WNCkeA9GMym7ICAyYHdbRHogOp8yulrV_ps6rryrqwgpEIwLi8DiUjjeeePXdXfnL56o6jbk9zqsfaKn2eox3w5j4FblimWWO1AQ92-nGyshNrb06NZFK9sCXuuKe_TCZ5T1sqzJ3TBfcSrd0_GRBJCm4_8vqt2TVUpVZ6RHUsU?purpose=inline)

Business

Companies can analyze monthly sales, revenue, expenses, and customer growth.

[Innovating Biopharmaceutical Manufacturing: Timegate’s Real-Time Solutions Transform Process Control](https://images.openai.com/static-rsc-4/JPUMse0rkaaTwdPZ-qT08x0zqgIYNdKJXl-N5Y1H_MsmNdHcIhbdBdXic9Yi3dMTKKqrWESQuYA6dciMtlpbYVFIc7kJTHSkunaoZswsA7idkoL8BVawfr-DThG_2qN5C5owT2gDOADlwlKDqjrv-2MJVZeJ-ORj37XAYlogozU?purpose=inline)

Science

Scientists can monitor experimental measurements and changes in research data over time.

[NETHERLANDS-WEATHER-CLIMATE-HEAT](https://images.openai.com/static-rsc-4/aJBwhnUj4znkgjhnFn5DuHnC-WhsgvwjnSogFTfd5fFclI1fvgeWh0Dyp16zqBDV10l9aO45izY2t_AKCvxGhM3OwsjJVlgATWPBBGNsGc91EMk18N6UuclYH6bYoF-d-cwetVKm6_QmOGPK0-y4_ynNyICJyqUChj14zi5Q-VgJ5dClatADFTYComd2C1Xm?purpose=inline)

Weather

Meteorologists can study daily temperatures, rainfall, and changes in weather conditions.

[\[100+\] Smartwatch Backgrounds | Wallpapers.com](https://images.openai.com/static-rsc-4/GkFWqprbG7hVzJLaJRAvMCnVqVUtseVv2K20h3wUug0fMPxzTDcm89qE-qrbA6gYxj_B_ZsniG6E5muxbVTKNWqNJVC9XW94m8vF5dceWqkzLHcom-630RSobzi4W0-l61CAVzCE-IEsb1g-cWyhj-MWTu59QNoa9hSXGTdCv_I?purpose=inline)

Everyday Life

People can track daily walking steps, monthly savings, weight changes, and electricity consumption.

## 4. Real-life Examples

Let's understand five practical applications.

### Example 1: Monthly University Student Enrollment

A university records the number of students enrolled every month.

- X-axis: Months (January to December).
- Y-axis: Number of enrolled students.
- Purpose: Monitor enrollment growth throughout the year.
- Why a line chart? It shows how enrollment changes from one month to another.

[Statistics | Mechanical Engineering](https://images.openai.com/static-rsc-4/e9ziPJzDlgUZc6Iym-5cpsNtoHU-A2-wtXcxnqM9OTojURIj7fTgqCDZ_oLo-TEXplfoJeB9tkhMH8Qww1KWbl0swC4WLW-lKHcY4bgWTklxGUjs2tp_v3e2TFdGeo17RllxWDw-28-1g65pqpGJ0ZG9wiaguwML-ztrAE8AgzE?purpose=inline)

[www2.sjsu.edu](https://www2.sjsu.edu/me/about-us/program-outcomes/statistics.php?utm_source=chatgpt.com)

### Example 2: Daily Student Attendance

A university records the number of students attending classes each day.

- X-axis: Days.
- Y-axis: Number of students present.
- Purpose: Monitor attendance patterns.
- Why a line chart? It identifies days with high or low attendance.

### Example 3: Monthly Business Sales

A shop records its monthly sales.

- X-axis: Months.
- Y-axis: Sales amount.
- Purpose: Monitor business performance.
- Why a line chart? It makes increases and decreases in sales easy to identify.

### Example 4: Daily Temperature Changes

A weather station records daily temperatures.

- X-axis: Days.
- Y-axis: Temperature in Celsius.
- Purpose: Monitor weather changes.
- Why a line chart? It shows temperature fluctuations over time.

### Example 5: Annual University Examination Results

A university records the pass percentage for each year.

- X-axis: Years.
- Y-axis: Pass percentage.
- Purpose: Monitor academic performance.
- Why a line chart? It helps identify long-term improvement or decline.

# Part B – Prepare

## 5. Understand the Dataset

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

- Rows: Each row represents one month's enrollment information.
- Columns: Each column represents a type of information.
- Category: Month is the category used to organize the records.
- Numerical value: Students Enrolled represents the number of students.

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

[Khan Academy](https://images.openai.com/static-rsc-4/EHU5sCA2XegZe1LyPPRvfbpttnjH-2iEYpj6-z6VxllnQp44Gh3kZ6a_B_MTfCYekDkrRys3dYRqkeiib65AtHMeH5jPkuNFE2zeuIwng9yrLQZfA6RpotKi2lM-YMs1UoMmqhwBLnvXXBU8IjHeh15_xd-xvH532xHIzgaCGRo?purpose=inline)

[khanacademy.org](https://www.khanacademy.org/math/4th-grade-matatag/xb1aa4507e7ecda19%3A4th-quarter/xb1aa4507e7ecda19%3Acollecting-and-organizing-data/a/solving-problems-using-data-for-at-most-two-variables-in-a-single-line-graph?utm_source=chatgpt.com)

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

[Matplotlib - Cheatsheet](https://images.openai.com/static-rsc-4/cPWK9jbPiS8lryHPrzowfUVAFn-mMRRhpw_bamgTB-YDjN8fYA0Ef-gCPSp_dc12z4dzxeok7P7zC2OF37Ng3oYaWw5xy_RWstDVpZnmU8Ym7Se37YpRuCD9STEWOIXDmBTWHr2SaxvWX3XzJvFWTU8TvpxlgbPnJ7iSwTVLTfA?purpose=inline)

[tutorialspoint.com](https://www.tutorialspoint.com/matplotlib/matplotlib_cheatsheet.htm?utm_source=chatgpt.com)

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

[The Register | The HCPC](https://images.openai.com/static-rsc-4/rn6tJ4epi3uGjR5K5cWeQqkHWtFrzHHVye_Xy-STxKAPExejgZH9h9m0_AsvJAIwciHRGxy9_48kuoOBiKu-V8Mm_vkV26i94qSp632Yd70ZHLJyeVpMkfSeMxdfBwHd14mSLIEZ7bh3b6YIgkAG3UKTIfUUtcC1hL0bZCPmSKY?purpose=inline)

Increasing Trend

Values move upward.

[Decreasing graph](https://images.openai.com/static-rsc-4/l-uIhPUkMK7gHNuwBdXnNGCNCHB1gboctw_3dTB002HijSEv_fqbl5UcdQnpEDRFQQeWi5LCDsN-AWiQfJaf6_GuDt_R05edl-7WMKaBILgFKAuviV3xpAsF6YKK2wLxnlAjcxjyXv-YQJ3Or3WXlf9mwQMMNYjIvUYOjnrKiiVa3QlrTkIZ2tjvpkyMNdln?purpose=inline)

Decreasing Trend

Values move downward.

[Free Tools & Spare Parts STL Download - шильдик ладаby ugadaiugadaev](https://images.openai.com/static-rsc-4/ckTz4MPRSFH5o6Bq-t7zruif6jTpqtGJU5bXFL-vNFOr8DRSmCpy4KhiCUXFlNizA0XqAwiUf1iQLTf9oL8MdB6dh2p4xSV7HcvOn8pX8zjcO1qa3yaE0jpRNgW2dpzOLrqRhOqPEkyLTqTYFBMrrTTbB4J_7naR_p4NlRCQCxA?purpose=inline)

Constant Trend

Values remain unchanged.

[chart icon vector. Icon related to graph and seo . suitable for web site, app, user interfaces, printable etc. flat line icon style. simple vector design editable](https://images.openai.com/static-rsc-4/IFpuivYb3RvGhqTfj7LTxSdUfhqcn7OGkwdgfsM2c5eIGjAIAbiySsoX418lUaIhWZ0GtyOG-44u2qyCqJbDXGy6XVlaSmwg4_IYx2DEjDBhVD5ZMbNUOE6B4wv1ssmV1Du1uwzZxveSbxUI6CFdMa7cGAQxOwHNWKEpwg7en0ZM9onBCxiS-6XyWGRTdxO6?purpose=inline)

Fluctuating Trend

Values repeatedly rise and fall.

### Multiple lines on one chart

A multiple line chart displays two or more datasets on the same chart.

For example, we can compare monthly enrollment in:

- Computer Science.
- Information Technology.

Each department gets a separate line and a legend identifies each line.

[UC Berkeley Data: Freshman Admissions for the EECS and L&S CS Majors | Ronald Kwan](https://images.openai.com/static-rsc-4/YglpzMYhS17W1THrB_P2R9yklbgXSB6fqhhFakokmH1rfgMdBv4xE5d9j-Spr8XEnG9xw9eWMzwi1AgB3DUpXSGiih9MWrh8EHCOfUcBseq-VWBRriajov4cd7lodBX97rpqEtI9p6hKVGMfl3whTTiCu3gxt9DiEOFDMl70lOI?purpose=inline)

[rkwan.me](https://rkwan.me/blog/ucb-eecs-lscs-admissions?utm_source=chatgpt.com)

Remember: Use different colors or markers to make multiple lines easy to distinguish.

# Part C – Create

## 8. Step-by-Step Demonstration

Now we will create our first line chart using Python and Matplotlib.

We will use the university enrollment dataset introduced earlier.

### Step 1: Install Matplotlib

Matplotlib is a Python library used to create charts and graphs.

Open your terminal or command prompt and execute:

```
pip install matplotlib
```

Wait until the installation is completed.

Note: If you are using Jupyter Notebook, you can run `!pip install matplotlib` in a notebook cell.

### Step 2: Import the required library

Before using Matplotlib, we need to import it.

```
import matplotlib.pyplot as plt
```

Understand the code:

- `import` loads a Python library.
- `matplotlib` is the library name.
- `pyplot` provides functions for creating charts.
- `as plt` gives us a short name to use instead of writing `matplotlib.pyplot` every time.

For example, we can write:

```
plt.show()
```

Instead of writing the full library name.

### Step 3: Prepare the dataset

We will store the months and enrollment values in two Python lists.

```
months = [    "January", "February", "March", "April",    "May", "June", "July", "August",    "September", "October", "November", "December"]students = [50, 65, 60, 80, 75, 100,            110, 95, 120, 130, 125, 150]
```

Understand the code:

- `months` stores the names of the months.
- `students` stores the number of enrolled students.
- Each position in the first list corresponds to the same position in the second list.

For example:

| Position | Month    | Students |
| -------- | -------- | -------- |
| 0        | January  | 50       |
| 1        | February | 65       |
| 2        | March    | 60       |
| 3        | April    | 80       |

Important: Both lists must contain the same number of items.

### Step 4: Create a basic line chart

We will use `plt.plot()` to create our first line chart.

```
import matplotlib.pyplot as pltmonths = ["January", "February", "March", "April",          "May", "June", "July", "August",          "September", "October", "November", "December"]students = [50, 65, 60, 80, 75, 100,            110, 95, 120, 130, 125, 150]plt.plot(months, students)plt.show()
```

[The Complete Guide to Line Charts with Matplotlib: Unleash the Power of Visual Storytelling | by Datasans | Medium](https://images.openai.com/static-rsc-4/nuuOsKEiPJglSDkszoUFoxJs2Qjt_xBpB_mgtC5p8Cmppo6K-_MMjprr3xoi5aIpORrTe3YI7spgj8qnMmc4Bu9fx8rK5kG9eb0pXboOVwkTl3imt2qclM3zcnpr-SqEZnBtI8gBjrtZhPGR_D-vENlkS5XP97T1lmF2eCi3_VM?purpose=inline)

[datasans.medium.com](https://datasans.medium.com/the-complete-guide-to-line-charts-with-matplotlib-unleash-the-power-of-visual-storytelling-e456b71a06ff?utm_source=chatgpt.com)

Understand `plt.plot()`:

```
plt.plot(months, students)
```

| Part       | Meaning              |
| ---------- | -------------------- |
| `plt`      | Matplotlib pyplot    |
| `plot()`   | Creates a line chart |
| `months`   | X-axis data          |
| `students` | Y-axis data          |

What happens?

1. Python reads the month names.
2. It reads the corresponding enrollment values.
3. Matplotlib places the values on the chart.
4. It connects the points with lines.
5. `plt.show()` displays the chart.

### Step 5: Add a chart title

A chart title tells viewers what the chart represents.

Use `plt.title()`.

```
plt.plot(months, students)plt.title("Monthly Student Enrollment")plt.show()
```

[Student enrolment and result detail | COLLEGE OF BUSINESS](https://images.openai.com/static-rsc-4/F3kbnvG4gONCF394eEVWBLpgM7vFZbV1X-6aFQVhmqCuW6ik1rOjB0X4VBRoWpI_Q3A1mNsf9R4sHx4saYMC-VD1poUml5A-Rm6cRvO00R4BQruax8kqVrIK0xFqyzarM0Ef4-XDt3MAxSYf5tPNPxnlZ4xSjcvniyYaZWvhngc?purpose=inline)

[cb.kku.edu.sa](https://cb.kku.edu.sa/en/node/294?utm_source=chatgpt.com)

### Step 6: Add X-axis and Y-axis labels

We should describe what each axis represents.

Use:

- `plt.xlabel()` for the horizontal axis.
- `plt.ylabel()` for the vertical axis.

```
plt.plot(months, students)plt.title("Monthly Student Enrollment")plt.xlabel("Months")plt.ylabel("Number of Students")plt.show()
```

Expected chart information:

- Title: Monthly Student Enrollment
- X-axis: Months
- Y-axis: Number of Students

### Step 7: Display the chart

The function `plt.show()` displays the completed chart.

It is normally placed at the end of the chart code.

```
plt.show()
```

Without this command, a chart may not appear in some Python environments.

### Step 8: Add markers to show individual data points

A line connects data points, but we may also want to display the individual points clearly.

We can use the `marker` parameter.

```
plt.plot(months, students, marker="o")plt.title("Monthly Student Enrollment")plt.xlabel("Months")plt.ylabel("Number of Students")plt.show()
```

[\[Excel\] 꺾은선 차트가 삐죽삐죽하다면? 부드러운 곡선으로 차트 꾸미기](https://images.openai.com/static-rsc-4/5-ltkDmngnQI3KwKQ_uV8ghZSUeNx8COrSOeBycIgBPp7Ja3ruDv8GeRER_7eYimCsuZ9ez7ODcgLjPT6MVjttdbKD5i0AFFmNSfIV05hdrDfYzCs10g6hnp8uvk98rX5nTkJAdu6nhZbBLfRZe8X8VejHE_p27PLTDuOctqNIQ?purpose=inline)

[luvbong.tistory.com](https://luvbong.tistory.com/629?utm_source=chatgpt.com)

Here:

- `marker="o"` displays circular markers.
- Each circle represents one month's enrollment.

Other marker examples:

| Marker | Appearance |
| ------ | ---------- |
| `"o"`  | Circle     |
| `"s"`  | Square     |
| `"^"`  | Triangle   |
| `"D"`  | Diamond    |
| `"*"`  | Star       |
| `"x"`  | Cross      |

### Step 9: Change line colors and styles

We can customize the appearance of the line.

```
plt.plot(    months,    students,    color="green",    linestyle="--",    marker="o")plt.title("Monthly Student Enrollment")plt.xlabel("Months")plt.ylabel("Number of Students")plt.show()
```

Important parameters:

| Parameter   | Purpose                  |
| ----------- | ------------------------ |
| `color`     | Changes line color.      |
| `linestyle` | Changes line appearance. |
| `marker`    | Displays data points.    |

Common line styles:

| Style  | Appearance    |
| ------ | ------------- |
| `"-"`  | Solid line    |
| `"--"` | Dashed line   |
| `":"`  | Dotted line   |
| `"-."` | Dash-dot line |

Common colors include:

`"red"`, `"blue"`, `"green"`, `"orange"`, `"black"` and `"purple"`.

### Step 10: Add gridlines

Gridlines make it easier to read numerical values.

Use `plt.grid()`.

```
plt.plot(months, students, marker="o")plt.title("Monthly Student Enrollment")plt.xlabel("Months")plt.ylabel("Number of Students")plt.grid(True)plt.show()
```

[Python Charts - Saving High-Resolution Figures in Seaborn](https://images.openai.com/static-rsc-4/Ci2zrsO7ZYRP1vGa8uivC9Txgjy5Rzc0p4NRmBLSiQk92No6A5GElJUJ9qtJKbt3Nu0ZEiYPDjPAE5nam0mAG_eFXJm3BHPzFl4Npv6gmu8bkuYlKGSjt4NV5WSC0zIx6x0tvywRpiEe-namXRT_ip5xQ1NahdpHnGhPBjaeCm0?purpose=inline)

[pythoncharts.com](https://www.pythoncharts.com/seaborn/seaborn-save-high-resolution-figures/?utm_source=chatgpt.com)

Here:

- `plt.grid(True)` displays gridlines.
- Gridlines help us compare the position of each point with the axis values.

### Step 11: Add a legend

A legend identifies the data shown by a line.

We can use `label` inside `plt.plot()` and `plt.legend()` to display it.

```
plt.plot(    months,    students,    marker="o",    color="blue",    label="University Enrollment")plt.title("Monthly Student Enrollment")plt.xlabel("Months")plt.ylabel("Number of Students")plt.legend()plt.grid(True)plt.show()
```

Understand:

- `label` gives a name to the line.
- `plt.legend()` displays that name on the chart.

A legend becomes especially important when a chart contains multiple lines.

### Step 12: Display values using annotations

Sometimes we want to show the exact numerical value beside each point.

We can use `plt.annotate()`.

```
plt.plot(months, students, marker="o")for i in range(len(months)):    plt.annotate(        students[i],        (months[i], students[i])    )plt.title("Monthly Student Enrollment")plt.xlabel("Months")plt.ylabel("Number of Students")plt.grid(True)plt.show()
```

Understand the new code:

- `len(months)` returns the number of months.
- `range()` generates positions from zero to eleven.
- `for` repeats the annotation operation for every month.
- `students[i]` gets the enrollment value at position `i`.
- `(months[i], students[i])` identifies the location of the point.

Result: Every data point displays its corresponding enrollment value.

### Complete example: Your first professional line chart

Now combine the concepts learned in this section.

```
import matplotlib.pyplot as plt# Step 1: Prepare datamonths = [    "January", "February", "March", "April",    "May", "June", "July", "August",    "September", "October", "November", "December"]students = [50, 65, 60, 80, 75, 100,            110, 95, 120, 130, 125, 150]# Step 2: Create line chartplt.plot(    months,    students,    color="blue",    linestyle="-",    linewidth=2,    marker="o",    markersize=7,    label="Student Enrollment")# Step 3: Add chart informationplt.title("Monthly Student Enrollment")plt.xlabel("Month")plt.ylabel("Number of Students")# Step 4: Add data labelsfor i in range(len(months)):    plt.annotate(        students[i],        (months[i], students[i]),        textcoords="offset points",        xytext=(0, 8),
```

[Yearly Overview: Previous Overviews: Office of Enrollment Management: Indiana University Bloomington](https://images.openai.com/static-rsc-4/V4BqnNPZdIPBa7nwgpn4bTdmwjaWfwZy_FuPcxYjoeEyqBGaiL5Wjvi_jX754E1dGsfZwQjTomuslpVKXSYOw0knDPTqOxEogVRDoRQsqzrCRP8pC31bosgVaWobiQros0Qu4RnK_lTXqviGsNUHPJ5eqFi_D69ndh2ZN_Q9psU?purpose=inline)

[oem.indiana.edu](https://oem.indiana.edu/archives/2023/index.html?utm_source=chatgpt.com)

What have we learned?

We have created a line chart with:

- A title.
- X-axis and Y-axis labels.
- A blue connecting line.
- Circular markers.
- Data labels.
- Gridlines.
- A legend.
- Rotated month names.

## 9. Modify and Customize

In this section, we will learn how to modify an existing line chart.

The objective is to understand how changing individual parameters affects the chart.

### A. Change the chart title

Use `plt.title()`.

```
plt.title("University Enrollment Report")
```

You can replace the title with any meaningful description.

### B. Change line color

Use the `color` parameter.

```
plt.plot(months, students, color="red")
```

Other options include:

```
color="blue"color="green"color="orange"color="purple"
```

### C. Change line width

Use `linewidth`.

```
plt.plot(months, students, linewidth=3)
```

- `linewidth=1`: Thin line.
- `linewidth=2`: Medium line.
- `linewidth=3`: Thick line.

### D. Change line style

Use `linestyle`.

```
plt.plot(months, students, linestyle="--")
```

Examples:

```
plt.plot(months, students, linestyle="-")plt.plot(months, students, linestyle="--")plt.plot(months, students, linestyle=":")plt.plot(months, students, linestyle="-.")
```

### E. Add markers

Use `marker`.

```
plt.plot(months, students, marker="o")
```

This displays a circular marker at each data point.

### F. Change marker size

Use `markersize`.

```
plt.plot(    months,    students,    marker="o",    markersize=10)
```

Larger values make the markers bigger.

### G. Change marker colors

Matplotlib allows us to customize the marker's face and border colors.

```
plt.plot(    months,    students,    marker="o",    color="blue",    markerfacecolor="yellow",    markeredgecolor="red",    markersize=8)plt.show()
```

| Parameter         | Purpose               |
| ----------------- | --------------------- |
| `color`           | Connecting line color |
| `markerfacecolor` | Inner marker color    |
| `markeredgecolor` | Marker border color   |
| `markersize`      | Marker size           |

### H. Change figure size

Use `plt.figure(figsize=(width, height))`.

```
plt.figure(figsize=(12, 5))plt.plot(months, students, marker="o")plt.show()
```

Here:

- `12` represents the figure width in inches.
- `5` represents the figure height in inches.

A larger figure provides more space for the chart.

### I. Change font size

We can change the font size of the title and axis labels.

```
plt.plot(months, students, marker="o")plt.title("Monthly Enrollment", fontsize=18)plt.xlabel("Month", fontsize=12)plt.ylabel("Students", fontsize=12)plt.show()
```

### J. Add data labels or annotations

Use `plt.annotate()` to display values near data points.

```
plt.plot(months, students, marker="o")for i in range(len(months)):    plt.annotate(        students[i],        (months[i], students[i]),        xytext=(0, 8),        textcoords="offset points",        ha="center"    )plt.show()
```

The `xytext` parameter controls the position of the annotation relative to the point.

### K. Add gridlines

```
plt.grid(True)
```

You can also customize gridline appearance.

```
plt.grid(    True,    linestyle="--",    alpha=0.5)
```

Here:

- `linestyle="--"` displays dashed gridlines.
- `alpha=0.5` controls transparency.

### L. Customize X-axis and Y-axis ticks

Ticks are the values displayed along the axes.

For example:

```
plt.plot(months, students, marker="o")plt.yticks(range(0, 181, 20))plt.show()
```

This displays Y-axis values at intervals of 20:

`0, 20, 40, 60, 80, ... 180`

We can also customize the X-axis ticks.

```
plt.xticks(rotation=45)
```

### M. Rotate X-axis labels

Long category names may overlap.

Use:

```
plt.xticks(rotation=45)
```

For example, month names will be displayed at a 45-degree angle.

### N. Add a legend

```
plt.plot(    months,    students,    label="Enrollment")plt.legend()
```

We can also change the legend position:

```
plt.legend(loc="upper left")
```

### O. Set axis limits

Axis limits control the range displayed on the chart.

Use:

- `plt.xlim()` for the horizontal axis.
- `plt.ylim()` for the vertical axis.

Example:

```
plt.plot(months, students, marker="o")plt.ylim(0, 180)plt.show()
```

This sets the Y-axis range from 0 to 180.

Important: Choose limits carefully. An inappropriate scale can make small changes appear much larger than they really are.

### P. Save the chart as a PNG image

Use `plt.savefig()`.

```
plt.plot(months, students, marker="o")plt.title("Monthly Student Enrollment")plt.savefig(    "student_enrollment.png",    dpi=300,    bbox_inches="tight")plt.show()
```

Understand the parameters:

- `"student_enrollment.png"` is the image filename.
- `dpi=300` controls image resolution.
- `bbox_inches="tight"` reduces unnecessary empty space around the chart.

The image is saved in the current working directory.

### A. Multiple Line Chart

Now we will compare enrollment in two university departments.

Dataset

| Month | Computer Science | Information Technology |
| ----- | ---------------- | ---------------------- |
| Jan   | 50               | 40                     |
| Feb   | 55               | 45                     |
| Mar   | 60               | 50                     |
| Apr   | 65               | 55                     |
| May   | 70               | 60                     |
| Jun   | 75               | 70                     |
| Jul   | 80               | 75                     |
| Aug   | 85               | 80                     |
| Sep   | 90               | 85                     |
| Oct   | 95               | 90                     |
| Nov   | 100              | 95                     |
| Dec   | 110              | 100                    |

Complete Python code

```
import matplotlib.pyplot as pltmonths = [    "Jan", "Feb", "Mar", "Apr", "May", "Jun",    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]cs_students = [50, 55, 60, 65, 70, 75,               80, 85, 90, 95, 100, 110]it_students = [40, 45, 50, 55, 60, 70,               75, 80, 85, 90, 95, 100]plt.figure(figsize=(10, 5))plt.plot(    months,    cs_students,    color="blue",    marker="o",    label="Computer Science")plt.plot(    months,    it_students,    color="green",    marker="s",    label="Information Technology")plt.title("Monthly Department Enrollment")plt.xlabel("Month")plt.ylabel("Number of Students")plt.grid(True, alpha=0.3)plt.legend()plt.tight_layout()plt.show()
```

[FIUDA](https://images.openai.com/static-rsc-4/qSCQU_5GCMJB58I9xIqtn72JEGNJHCP9xVtyBxdekGkx_3s6Oiy4VhaiTGr4dt6UTcFmc5PtMfUerASwc-GYCpLnBhBtPx_xsfkyDocMElri1s5uAG0vjV_ppAltrf-bvNW9q7tP8iezxpq58pBTX0CDyecLpy59thDgO5W9CqY?purpose=inline)

[fi.uda.cl](https://fi.uda.cl/FIUDAVISIBLE/estudiantes.html?utm_source=chatgpt.com)

What does this chart show?

- The blue line represents Computer Science.
- The green line represents Information Technology.
- Both departments show an overall increasing trend.
- Computer Science has higher enrollment throughout the year.

### B. Line Chart with Different Styles

We can display multiple line styles to understand how Matplotlib represents different patterns.

```
import matplotlib.pyplot as pltmonths = ["Jan", "Feb", "Mar", "Apr", "May"]a = [20, 30, 40, 50, 60]b = [25, 35, 45, 55, 65]c = [30, 40, 50, 60, 70]d = [35, 45, 55, 65, 75]plt.plot(months, a, linestyle="-", label="Solid")plt.plot(months, b, linestyle="--", label="Dashed")plt.plot(months, c, linestyle=":", label="Dotted")plt.plot(months, d, linestyle="-.", label="Dash-dot")plt.title("Different Line Styles")plt.xlabel("Month")plt.ylabel("Values")plt.legend()plt.grid(True)plt.show()
```

[请在同一张图中画出“实线、点线、虚线、双线”这四种线_python线的类型 有哪些对应代码-CSDN博客](https://images.openai.com/static-rsc-4/NXqAI2S47FoZJzCuto_DE4g8szad9Jol0Z84HzPNOTcvHKAZYai8cCbtTgL1lZNIj8SIZlrgQ2cYVV5sOMN9h2RRxGg71dKpew1PHpwx6_8d4FfkFyJtLo-XQVt9LCMmDRCkROBTE4_S9WxfcDy5Fb2ZoT7Dh26c1MvVrii-VC4?purpose=inline)

[blog.csdn.net](https://blog.csdn.net/qq_43585760/article/details/144008386?utm_source=chatgpt.com)

### C. Line Chart with Markers

Markers make individual data points easier to identify.

```
import matplotlib.pyplot as pltdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]attendance = [80, 85, 78, 90, 95]plt.plot(    days,    attendance,    marker="o",    markersize=10,    color="purple",    linewidth=2)plt.title("Weekly Student Attendance")plt.xlabel("Days")plt.ylabel("Number of Students")plt.grid(True)plt.show()
```

[ANALYZING AND INTERPRETING GRAPHS OF PRIMARY DATA.pptx](https://images.openai.com/static-rsc-4/yuDDnPgvigf6_snRou5fys-V9--CL7aW-1vzJo877yO4ZfJ4Nisv7xPynvnl3MtSYchgaDBcgtu_qzgMj-1O1Rduw1kGxplZZWm5wYLkxxI0SR2IGD0jjEqaDwelhj1yeCyvq8D8zDuZGxkMc0JjuZrkLMvzV43S7jz82jq2iEo?purpose=inline)

[slideshare.net](https://www.slideshare.net/slideshow/analyzing-and-interpreting-graphs-of-primary-data-pptx/286211047?utm_source=chatgpt.com)

### D. Horizontal vs Vertical Concept

A standard line chart normally uses:

- A horizontal X-axis.
- A vertical Y-axis.

The X-axis represents the sequence, such as months or days.

The Y-axis represents numerical measurements, such as enrollment or temperature.

[Activities Activity 1.1 Construct a line graph using the data given from the table below. Online Class - Brainly.ph](https://images.openai.com/static-rsc-4/F7V4pKV_rsgNJ246mS30LAefhcPjaRFSn9kA430ClKc9PNYqtO6uH61avLi0So5DxkvZlp0CL0dFLSRzMBtpXhAZbOdTZOSNoBaq1LRknzWMc4rhvqRsP1b1elCgP5kEO0dCJ_sw8OHsRDGWbrEUxnMg5PnKkBBmDpePkeQqM6E?purpose=inline)

[brainly.ph](https://brainly.ph/question/29110529?utm_source=chatgpt.com)

Can we make a horizontal line chart?

Yes. We can swap the axes using `plt.plot()`.

```
import matplotlib.pyplot as pltmonths = [1, 2, 3, 4, 5]students = [50, 65, 60, 80, 75]plt.plot(students, months, marker="o")plt.title("Horizontal Orientation Example")plt.xlabel("Number of Students")plt.ylabel("Month Number")plt.grid(True)plt.show()
```

However, this changes the meaning of the axes. It is not the usual way of displaying time-based line charts.

Remember: Use the horizontal axis for the ordered sequence and the vertical axis for the measured values in a standard time-series line chart.

# Part D – Analyze

## 10. Read and Interpret

Creating a chart is only one part of data visualization.

We must also understand what the chart tells us.

Let's examine our original student enrollment dataset.

| Month     | Students |
| --------- | -------- |
| January   | 50       |
| February  | 65       |
| March     | 60       |
| April     | 80       |
| May       | 75       |
| June      | 100      |
| July      | 110      |
| August    | 95       |
| September | 120      |
| October   | 130      |
| November  | 125      |
| December  | 150      |

### Read the chart

[Figure 1 - from Beliefs and Attitudes toward the English](https://images.openai.com/static-rsc-4/V3QxV6DH_SE-DzlEnKZ7qiFrl79MN_IZExRC3SkOqTZxQNsZW7ytudqew-C0QoKVqdqXQmAzy_rNQyvOqp4TVkyWYFQ6bPBEmAFUO6zH_lOXH7mE7K62mUx5pc3vHDzO2GjU_eAP9PYwejSkAmCYDbZlCq_Upx28qQM_aikj5sc?purpose=inline)

[academia.edu](https://www.academia.edu/figures/1294270/figure-1-the-enrolment-trend-in-the-ab-english-program-from?utm_source=chatgpt.com)

### Question 1: Which month has the highest enrollment?

Answer: December

December has 150 enrolled students, which is the highest value in the dataset.

### Question 2: Which month has the lowest enrollment?

Answer: January

January has 50 enrolled students.

### Question 3: During which months did enrollment increase?

Enrollment increased during these transitions:

- January to February: 50 → 65
- March to April: 60 → 80
- May to June: 75 → 100
- June to July: 100 → 110
- August to September: 95 → 120
- September to October: 120 → 130
- November to December: 125 → 150

### Question 4: During which months did enrollment decrease?

Enrollment decreased during:

- February to March: 65 → 60
- April to May: 80 → 75
- July to August: 110 → 95
- October to November: 130 → 125

### Question 5: What is the difference between the highest and lowest enrollment?

Highest enrollment = 150

Lowest enrollment = 50

Difference:

\\[ 150-50=100 \\]

Answer: 100 students.

### Question 6: In which month did enrollment show the greatest increase?

Let's calculate the changes between consecutive months.

| Period  | Change |
| ------- | ------ |
| Jan–Feb | +15    |
| Feb–Mar | -5     |
| Mar–Apr | +20    |
| Apr–May | -5     |
| May–Jun | +25    |
| Jun–Jul | +10    |
| Jul–Aug | -15    |
| Aug–Sep | +25    |
| Sep–Oct | +10    |
| Oct–Nov | -5     |
| Nov–Dec | +25    |

Answer: May–June, August–September, and November–December share the greatest increase of 25 students.

### Question 7: What overall trend can we observe?

The overall trend is increasing.

Enrollment starts at 50 students in January and reaches 150 students in December.

Although there are some decreases during the year, the general direction is upward.

### How to identify patterns in a line chart

| Pattern        | How to identify it              | Example                      |
| -------------- | ------------------------------- | ---------------------------- |
| Upward trend   | Line moves upward               | Sales increase               |
| Downward trend | Line moves downward             | Temperature decreases        |
| Stable period  | Line remains nearly horizontal  | Attendance stays similar     |
| Sudden change  | Line moves sharply              | Enrollment increases quickly |
| Peak           | Highest point                   | Highest monthly sales        |
| Lowest point   | Lowest point                    | Lowest daily attendance      |
| Fluctuation    | Line repeatedly rises and falls | Daily temperature changes    |

Practice reading charts: Always look at the overall direction first, then examine individual increases and decreases.

## 11. Common Mistakes and Limitations

Students should understand common mistakes before using line charts in real projects.

### Common mistakes

| Mistake                                    | Why it is a problem                        | How to avoid it                               |
| ------------------------------------------ | ------------------------------------------ | --------------------------------------------- |
| Using line charts for unrelated categories | Suggests a relationship between categories | Use a bar chart instead.                      |
| Incorrect data sequence                    | Creates misleading trends                  | Arrange data in the correct order.            |
| Missing chart title                        | Viewers cannot easily understand the chart | Add a meaningful title.                       |
| Missing axis labels                        | Axis meanings are unclear                  | Label both axes.                              |
| Too many lines                             | Makes the chart difficult to read          | Show fewer relevant datasets.                 |
| Too many colors                            | Creates visual confusion                   | Use a limited color palette.                  |
| Misleading axis scales                     | Exaggerates or hides changes               | Choose appropriate axis limits.               |
| Inappropriate markers                      | Makes the chart crowded                    | Use simple markers.                           |
| Unnecessary connecting lines               | Suggests a continuous relationship         | Use scatter plots for unrelated observations. |
| Too many data labels                       | Makes the chart overcrowded                | Label only important points when necessary.   |

### Practical limitations of line charts

1. Not suitable for every dataset: Unrelated categories are usually better represented by bar charts.
2. Difficult with many lines: Too many datasets can make comparisons confusing.
3. Can hide individual values: Without markers or annotations, exact values may be difficult to identify.
4. Sensitive to axis scales: Different scales can change how trends appear.
5. Requires meaningful order: Connecting unrelated data points can produce misleading interpretations.
6. May not show total magnitude clearly: An area chart may be better when the amount or cumulative size is important.

Important lesson: A chart should make information easier to understand, not create confusion.

## 12. Comparison with Other Charts

Let's compare line charts with three other common visualization types.

[Creating Matplotlib Bar Charts: A Step-by-Step Guide | LabEx](https://images.openai.com/static-rsc-4/ZmOycWA3jmfQJO0DHE37hZ95eXPblo_mClc8A1z1iMmP_YNQx-uHUszTN3DcQ51iEbidpC-Ef3I3rnqOx1UKaykXUIMxW-5vYMPLJZDg7MaPefu7srhkujTI3rkEgoAU3lvpgUYE502jgfARhEr-_QT7BCtGAmoiOwq12kxVEz8?purpose=inline)

1\. Bar Chart

Used to compare numerical values across different categories.

Example: Comparing the number of students in Computer Science, IT, Mathematics, and Physics.

[Area Graph | Create Area Charts with Python - Plotivy](https://images.openai.com/static-rsc-4/2eKMR96AMQBkovVAMRiBB7VVPpZJpOLllDnaRYERicLdmhFIjNYbv6WewpeDjHCuV-qAg9KXlEeMpJkPuKDP17dWtAoUmrIJCmywyHz_6pH0ic_LCNVpEYFdXhbqe-InpkTwQebf9tsc4HTzkUBhbYY-SziD8EjJdTywgUBxF8M?purpose=inline)

2\. Area Chart

Used to show changes over time while emphasizing the magnitude of values through a filled area.

Example: Showing monthly electricity consumption.

[Regression Analysis - DEV Community](https://images.openai.com/static-rsc-4/QprIe_-cNHzm-5Sl8kqj07weqqRMsXpjvxktSvZiGxwh7X11eAPwNDGmgYd3O3lakO7o70GXPo8Mj9EYovRXUvIceh186wHtPQ8aTLY3hxjkusdyRVX6cCMuTa_-9xM_tq4U3XqIYzlOqNeeq0EQ00vlLvkaG8ZHPt-Gx8ykKwk?purpose=inline)

3\. Scatter Plot

Used to examine relationships between two numerical variables.

Example: Studying the relationship between study hours and examination marks.

### Detailed comparison

| Feature         | Line Chart              | Bar Chart              | Area Chart               | Scatter Plot             |
| --------------- | ----------------------- | ---------------------- | ------------------------ | ------------------------ |
| Purpose         | Show changes and trends | Compare categories     | Show magnitude over time | Show relationships       |
| Suitable data   | Ordered values          | Categorical values     | Ordered numerical values | Two numerical variables  |
| Best use case   | Monthly enrollment      | Students by department | Monthly revenue          | Study hours vs marks     |
| Main difference | Connects data points    | Uses bars              | Fills area under line    | Displays separate points |

### Which chart should you select?

| Your requirement                          | Recommended chart |
| ----------------------------------------- | ----------------- |
| Compare monthly sales                     | Line Chart        |
| Compare sales of products                 | Bar Chart         |
| Show revenue growth and magnitude         | Area Chart        |
| Compare study hours and marks             | Scatter Plot      |
| Track daily attendance                    | Line Chart        |
| Compare students in different departments | Bar Chart         |
| Show temperature changes                  | Line Chart        |

Remember these simple rules:

- Line Chart = Change over time.
- Bar Chart = Compare categories.
- Area Chart = Change over time with emphasis on magnitude.
- Scatter Plot = Relationship between numerical variables.

# Part E – Practice

## 13. Guided Exercise

Your turn to practice

### Exercise: Monthly Average Temperature

A weather station records the average monthly temperature of a city.

Use the following dataset.

| Month     | Average Temperature (°C) |
| --------- | ------------------------ |
| January   | 12                       |
| February  | 15                       |
| March     | 20                       |
| April     | 26                       |
| May       | 32                       |
| June      | 36                       |
| July      | 35                       |
| August    | 33                       |
| September | 30                       |
| October   | 25                       |
| November  | 19                       |
| December  | 14                       |

### Step 1: Understand the dataset

Identify:

- What does each row represent?
- What information is stored in the Month column?
- What information is stored in the Temperature column?
- Which column should be used for the X-axis?
- Which column should be used for the Y-axis?

### Step 2: Prepare the Python lists

Create two lists:

```python
months = [...]temperature = [...]
```

Fill these lists using the dataset.

### Step 3: Create a basic line chart

Use:

```python
plt.plot(months, temperature)
```

Display the chart.

### Step 4: Add title and axis labels

Your chart should contain:

- Title: Monthly Average Temperature
- X-axis: Month
- Y-axis: Temperature (°C)

### Step 5: Add markers

Use circular markers to show individual temperature values.

Hint:

```
marker="o"
```

### Step 6: Customize the line

Change the line color to red.

Hint:

```
color="red"
```

### Step 7: Add gridlines

Display gridlines to make temperature values easier to read.

Hint:

```
plt.grid(True)
```

### Step 8: Interpret the chart

Answer these questions:

1. Which month has the highest temperature?
2. Which month has the lowest temperature?
3. During which months does temperature increase?
4. During which months does temperature decrease?
5. What happens to temperature after June?
6. What overall pattern can you observe?

Your learning challenge

Complete the Python program yourself before looking for a solution.

Prepare the two Python lists.

Create the basic line chart.

Add title and axis labels.

Add markers, color, and gridlines.

Interpret the temperature trend.

0 of 5 tasks completed

## 14. Independent Practical Task

Now complete the following exercises independently.

The exercises are arranged from beginner to advanced level.

### Exercise 1: Beginner – Monthly Shop Sales

Scenario

A shop owner wants to monitor monthly sales.

Use the following dataset:

| Month     | Sales (PKR) |
| --------- | ----------- |
| January   | 20,000      |
| February  | 25,000      |
| March     | 22,000      |
| April     | 30,000      |
| May       | 35,000      |
| June      | 40,000      |
| July      | 38,000      |
| August    | 45,000      |
| September | 50,000      |
| October   | 48,000      |
| November  | 55,000      |
| December  | 65,000      |

Requirements

1. Prepare two Python lists.
2. Create a line chart using `plt.plot()`.
3. Add an appropriate chart title.
4. Label both axes.
5. Change the line color to green.
6. Add circular markers.
7. Display gridlines.
8. Display the chart.

Questions

- Which month has the highest sales?
- Which month has the lowest sales?
- During which month did sales decrease?
- What is the overall sales trend?

### Exercise 2: Intermediate – Daily Student Attendance

Scenario

A teacher records the attendance of students over 15 working days.

Use the following dataset:

| Day    | Students Present |
| ------ | ---------------- |
| Day 1  | 35               |
| Day 2  | 38               |
| Day 3  | 36               |
| Day 4  | 40               |
| Day 5  | 42               |
| Day 6  | 39               |
| Day 7  | 43               |
| Day 8  | 45               |
| Day 9  | 41               |
| Day 10 | 44               |
| Day 11 | 46               |
| Day 12 | 48               |
| Day 13 | 45               |
| Day 14 | 47               |
| Day 15 | 50               |

Requirements

1. Prepare the attendance dataset.
2. Create a line chart.
3. Add a suitable title.
4. Label the X-axis and Y-axis.
5. Add circular markers.
6. Change the line color.
7. Add gridlines.
8. Display data labels for each point.
9. Rotate the X-axis labels if necessary.

Questions

- Which day has the highest attendance?
- Which day has the lowest attendance?
- How many students were present on Day 10?
- Did attendance generally increase or decrease?

### Exercise 3: Advanced – Department-wise Student Enrollment

Scenario

A university wants to compare enrollment in three departments over 12 months.

Use the following dataset:

| Month | Computer Science | IT  | Mathematics |
| ----- | ---------------- | --- | ----------- |
| Jan   | 50               | 40  | 30          |
| Feb   | 55               | 45  | 32          |
| Mar   | 60               | 48  | 35          |
| Apr   | 65               | 55  | 38          |
| May   | 70               | 60  | 40          |
| Jun   | 75               | 65  | 45          |
| Jul   | 80               | 70  | 48          |
| Aug   | 85               | 75  | 50          |
| Sep   | 90               | 80  | 55          |
| Oct   | 95               | 85  | 58          |
| Nov   | 100              | 90  | 60          |
| Dec   | 110              | 100 | 65          |

Requirements

1. Prepare four Python lists.
2. Create a multiple line chart.
3. Display all three departments on the same chart.
4. Use different colors for each department.
5. Use different markers.
6. Use different line styles.
7. Add a chart title.
8. Label both axes.
9. Add a legend.
10. Add gridlines.
11. Display the chart using `plt.show()`.

Questions

- Which department has the highest enrollment?
- Which department has the lowest enrollment?
- Which department shows the greatest overall growth?
- Do all three departments show an increasing trend?
- Why is a multiple line chart suitable for this comparison?

## 15. Assessment and Recap

This section checks your understanding of line charts and Python Matplotlib.

### A. Multiple-Choice Questions (5)

Select the correct answer for each question.

Question 1. What is the main purpose of a line chart?

A. To display text information.

B. To show changes and trends over time.

C. To display images.

D. To store numerical values.

Question 2. Which Matplotlib function is used to create a line chart?

A. `plt.bar()`

B. `plt.scatter()`

C. `plt.plot()`

D. `plt.pie()`

Question 3. Which parameter is used to display circular markers?

A. `color="o"`

B. `marker="o"`

C. `linestyle="o"`

D. `markersize="o"`

Question 4. Which function is used to display gridlines?

A. `plt.grid()`

B. `plt.title()`

C. `plt.legend()`

D. `plt.xlabel()`

Question 5. Which chart is generally more suitable for comparing sales of different products?

A. Line Chart

B. Area Chart

C. Bar Chart

D. Scatter Plot

### B. Output-Prediction Questions (3)

Predict the output of each Python program.

Question 6. Understanding a basic line chart

```
import matplotlib.pyplot as pltmonths = ["Jan", "Feb", "Mar"]sales = [20, 40, 30]plt.plot(months, sales)plt.show()
```

Answer:

1. Which values appear on the X-axis?
2. Which values appear on the Y-axis?
3. Does the line increase throughout the chart?

Question 7. Understanding markers and gridlines

```
import matplotlib.pyplot as pltdays = [1, 2, 3, 4]attendance = [30, 35, 40, 45]plt.plot(days, attendance, marker="o")plt.grid(True)plt.show()
```

Answer:

1. How many data points are displayed?
2. What does `marker="o"` do?
3. What does `plt.grid(True)` do?

Question 8. Understanding multiple lines

```
import matplotlib.pyplot as pltmonths = ["Jan", "Feb", "Mar"]a = [10, 20, 30]b = [30, 20, 10]plt.plot(months, a, label="Department A")plt.plot(months, b, label="Department B")plt.legend()plt.show()
```

Answer:

1. How many lines are displayed?
2. Which department shows an increasing trend?
3. Which department shows a decreasing trend?
4. What is the purpose of `plt.legend()`?

### C. Code Modification Questions (3)

Modify the given programs according to the requirements.

Question 9. Change line appearance

Given code:

```
plt.plot(months, students)
```

Modify it to:

- Change the line color to red.
- Add circular markers.
- Set line width to 3.

Question 10. Add chart information

Given code:

```
plt.plot(months, sales)plt.show()
```

Modify it to:

- Add title: Monthly Sales Report.
- Add X-axis label: Month.
- Add Y-axis label: Sales.
- Add gridlines.

Question 11. Add a legend and save the chart

Given code:

```
plt.plot(months, cs_students, label="Computer Science")plt.plot(months, it_students, label="Information Technology")
```

Modify it to:

- Display a legend.
- Display gridlines.
- Save the chart as `department_enrollment.png`.

### D. Practical Programming Tasks (2)

Question 12. Monthly Electricity Consumption

A household records electricity consumption over six months.

| Month    | Units Consumed |
| -------- | -------------- |
| January  | 250            |
| February | 280            |
| March    | 260            |
| April    | 300            |
| May      | 320            |
| June     | 350            |

Create a line chart that:

1. Displays monthly electricity consumption.
2. Includes a title and axis labels.
3. Uses a blue line with circular markers.
4. Displays gridlines.
5. Shows the numerical values beside each point.
6. Explains the overall trend.

Question 13. Compare Two Departments

A university wants to compare student enrollment in two departments.

| Month    | Computer Science | Mathematics |
| -------- | ---------------- | ----------- |
| January  | 40               | 30          |
| February | 45               | 35          |
| March    | 50               | 38          |
| April    | 55               | 42          |
| May      | 65               | 45          |
| June     | 70               | 50          |

Create a multiple line chart that:

1. Displays both departments.
2. Uses different colors and markers.
3. Uses different line styles.
4. Includes a title and axis labels.
5. Displays a legend.
6. Displays gridlines.
7. Identifies which department has higher enrollment.

### E. Short Lesson Summary

A line chart is a graph that displays numerical information using data points connected by lines.

In this lesson, we learned:

1. Line charts are useful for showing changes over time.
2. The X-axis normally represents time or an ordered sequence.
3. The Y-axis represents numerical values.
4. `plt.plot()` creates a line chart.
5. `plt.title()` adds a chart title.
6. `plt.xlabel()` and `plt.ylabel()` add axis labels.
7. `marker` displays individual data points.
8. `color`, `linewidth`, and `linestyle` customize the line.
9. `plt.grid()` displays gridlines.
10. `plt.legend()` identifies different lines.
11. `plt.annotate()` displays values near data points.
12. `plt.savefig()` saves the chart as an image.
13. Multiple line charts help compare different datasets.
14. Line charts help identify increasing, decreasing, stable, and fluctuating trends.

### F. Key Terms to Remember

| Term                | Meaning                                                |
| ------------------- | ------------------------------------------------------ |
| Line Chart          | A chart that connects data points using lines.         |
| Matplotlib          | A Python library for creating charts.                  |
| Pyplot              | Matplotlib's plotting interface.                       |
| X-axis              | Horizontal axis.                                       |
| Y-axis              | Vertical axis.                                         |
| Data Point          | A point representing a numerical observation.          |
| Marker              | A symbol showing a data point.                         |
| Gridlines           | Reference lines that help read chart values.           |
| Legend              | Identifies different datasets.                         |
| Trend               | General direction of data changes.                     |
| Fluctuation         | Repeated increases and decreases.                      |
| Annotation          | Additional information displayed near a chart element. |
| Multiple Line Chart | A chart containing two or more lines.                  |

### G. Answer Key

For instructors and self-assessment. Students should attempt all questions before checking these answers.

Assessment answer key

13 questions

Reveal answer key

## Final Learning Outcome

## What students should be able to do

By completing this lesson and its exercises, students should be able to:

1. Understand line charts and their real-world applications.
2. Prepare datasets using Python lists.
3. Create basic and multiple line charts using Matplotlib.
4. Customize charts using colors, markers, labels, and gridlines.
5. Interpret trends, fluctuations, and changes in data.
6. Choose the appropriate chart for different datasets.
7. Complete independent data visualization exercises.

Lesson completed

Teaching recommendation: Teach Sections 1–7 before starting Python coding. Demonstrate Sections 8–9 live in class, discuss Sections 10–12 using actual charts, and assign Sections 13–15 as guided and independent practice.

This keeps the learning progression consistent: Understand → Prepare → Create → Analyze → Practice.