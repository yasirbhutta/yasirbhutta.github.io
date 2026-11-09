---
layout: page
title: Python Line Chart Tutorial - Matplotlib Basics
description: Learn how to create, customize, and interpret line charts in Python using Matplotlib with practical examples, exercises, and beginner-friendly guidance.
keywords: Python line chart, Matplotlib line plot, Python data visualization, plotting in Python, line graph tutorial, beginner Python charts, Matplotlib tutorial, Python chart examples
---

## Lesson Overview

A line chart is one of the most useful charts for understanding how values change over time. In this lesson, students will learn to prepare data, create line charts using Python's Matplotlib library, customize charts, and interpret trends.

**Teaching sequence:**

Example → Understand the Data → Create the Chart → Interpret the Results → Modify the Chart → Practice

**Main library**: Matplotlib

**Required knowledge:** Basic Python variables, lists, and the `print()` function.

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

![Blended Learning](https://images.openai.com/static-rsc-4/I0XvXML3uac3W-IUPhXl-vXqMR4iHj55Quz8wc59K-a_m8koxBe9p0cGCux0SKZ-47gqsLlhcDQQdZE_N_FHrQbWUOsyUJpTJLogFI7q3FYij6a04LYeWPS0_3cvlKOvTmG8YUU_yN2NMvqD_XrxExvnXYY86MHhqozsV_9t8zQ?purpose=inline)

![blended-learning.resources.wjec.co.uk](https://blended-learning.resources.wjec.co.uk/en/mfw24-25_1-2/0/6?utm_source=chatgpt.com)

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

**Remember:** A line chart helps answer the question: How has something changed over time?

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

![Academics](https://images.openai.com/static-rsc-4/AImB8bm0VL_2zKmJibuq6Tc9R9x4OBqxhaNozx-MnuE1bpDBGJ-ZaKVAw9aRxN5XZasuwSasyDA8Gc1Vk0NbHts7Vbj7aWumMytDUwMxqQP5L4nEORCxFOoX-WcBIZO7iGki7lYl6iShv8QLxcVj0G9JGKfIDCGDg7Fk6c4eBfg?purpose=inline)

Education

Universities can monitor monthly enrollment, daily attendance, and annual examination performance.

![Home](https://images.openai.com/static-rsc-4/WNCkeA9GMym7ICAyYHdbRHogOp8yulrV_ps6rryrqwgpEIwLi8DiUjjeeePXdXfnL56o6jbk9zqsfaKn2eox3w5j4FblimWWO1AQ92-nGyshNrb06NZFK9sCXuuKe_TCZ5T1sqzJ3TBfcSrd0_GRBJCm4_8vqt2TVUpVZ6RHUsU?purpose=inline)

Business

Companies can analyze monthly sales, revenue, expenses, and customer growth.

![Innovating Biopharmaceutical Manufacturing: Timegate’s Real-Time Solutions Transform Process Control](https://images.openai.com/static-rsc-4/JPUMse0rkaaTwdPZ-qT08x0zqgIYNdKJXl-N5Y1H_MsmNdHcIhbdBdXic9Yi3dMTKKqrWESQuYA6dciMtlpbYVFIc7kJTHSkunaoZswsA7idkoL8BVawfr-DThG_2qN5C5owT2gDOADlwlKDqjrv-2MJVZeJ-ORj37XAYlogozU?purpose=inline)

Science

Scientists can monitor experimental measurements and changes in research data over time.

![NETHERLANDS-WEATHER-CLIMATE-HEAT](https://images.openai.com/static-rsc-4/aJBwhnUj4znkgjhnFn5DuHnC-WhsgvwjnSogFTfd5fFclI1fvgeWh0Dyp16zqBDV10l9aO45izY2t_AKCvxGhM3OwsjJVlgATWPBBGNsGc91EMk18N6UuclYH6bYoF-d-cwetVKm6_QmOGPK0-y4_ynNyICJyqUChj14zi5Q-VgJ5dClatADFTYComd2C1Xm?purpose=inline)

Weather

Meteorologists can study daily temperatures, rainfall, and changes in weather conditions.

![\[100+\] Smartwatch Backgrounds | Wallpapers.com](https://images.openai.com/static-rsc-4/GkFWqprbG7hVzJLaJRAvMCnVqVUtseVv2K20h3wUug0fMPxzTDcm89qE-qrbA6gYxj_B_ZsniG6E5muxbVTKNWqNJVC9XW94m8vF5dceWqkzLHcom-630RSobzi4W0-l61CAVzCE-IEsb1g-cWyhj-MWTu59QNoa9hSXGTdCv_I?purpose=inline)

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

![Statistics | Mechanical Engineering](https://images.openai.com/static-rsc-4/e9ziPJzDlgUZc6Iym-5cpsNtoHU-A2-wtXcxnqM9OTojURIj7fTgqCDZ_oLo-TEXplfoJeB9tkhMH8Qww1KWbl0swC4WLW-lKHcY4bgWTklxGUjs2tp_v3e2TFdGeo17RllxWDw-28-1g65pqpGJ0ZG9wiaguwML-ztrAE8AgzE?purpose=inline)

![www2.sjsu.edu](https://www2.sjsu.edu/me/about-us/program-outcomes/statistics.php?utm_source=chatgpt.com)

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

