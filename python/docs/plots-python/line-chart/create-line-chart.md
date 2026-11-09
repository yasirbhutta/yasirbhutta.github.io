---
layout: page
title: Create Line Charts in Python with Matplotlib
description: Learn how to build a line chart in Python using Matplotlib, from preparing data to plotting values, labeling axes, and visualizing trends step by step.
keywords: create line chart in Python, Matplotlib line chart, Python plotting tutorial, line graph example, Python data visualization, chart creation in Python, Matplotlib tutorial for beginners
---

## 1. Step-by-Step Demonstration

Now we will create our first line chart using Python and Matplotlib.

We will use the university enrollment dataset introduced earlier.

### Step 1: Install Matplotlib

Matplotlib is a Python library used to create charts and graphs.

Open your terminal or command prompt and execute:

```python
pip install matplotlib
```

Wait until the installation is completed.

Note: If you are using Jupyter Notebook, you can run `!pip install matplotlib` in a notebook cell.

### Step 2: Import the required library

Before using Matplotlib, we need to import it.

```python
import matplotlib.pyplot as plt
```

Understand the code:

- `import` loads a Python library.
- `matplotlib` is the library name.
- `pyplot` provides functions for creating charts.
- `as plt` gives us a short name to use instead of writing `matplotlib.pyplot` every time.

For example, we can write:

```python
plt.show()
```

Instead of writing the full library name.

### Step 3: Prepare the dataset

We will store the months and enrollment values in two Python lists.

```python
months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

students = [
    50, 65, 60, 80, 75, 100,
    110, 95, 120, 130, 125, 150
]
```

**Understand the code:**

- `months` stores the names of the months.
- `students` stores the number of enrolled students.
- Each position in the first list corresponds to the same position in the second list.

**For example:**

| Position | Month    | Students |
| -------- | -------- | -------- |
| 0        | January  | 50       |
| 1        | February | 65       |
| 2        | March    | 60       |
| 3        | April    | 80       |

Important: Both lists must contain the same number of items.

### Step 4: Create a basic line chart

We will use `plt.plot()` to create our first line chart.

```python
import matplotlib.pyplot as plt

months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

students = [
    50, 65, 60, 80, 75, 100,
    110, 95, 120, 130, 125, 150
]

plt.plot(months, students)

plt.show()
```

![The Complete Guide to Line Charts with Matplotlib: Unleash the Power of Visual Storytelling | by Datasans | Medium](https://images.openai.com/static-rsc-4/nuuOsKEiPJglSDkszoUFoxJs2Qjt_xBpB_mgtC5p8Cmppo6K-_MMjprr3xoi5aIpORrTe3YI7spgj8qnMmc4Bu9fx8rK5kG9eb0pXboOVwkTl3imt2qclM3zcnpr-SqEZnBtI8gBjrtZhPGR_D-vENlkS5XP97T1lmF2eCi3_VM?purpose=inline)

[datasans.medium.com](https://datasans.medium.com/the-complete-guide-to-line-charts-with-matplotlib-unleash-the-power-of-visual-storytelling-e456b71a06ff?utm_source=chatgpt.com)

**Understand `plt.plot()`:**

```python
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

```python
plt.plot(months, students)
plt.title("Monthly Student Enrollment")plt.show()
```

![Student enrolment and result detail | COLLEGE OF BUSINESS](https://images.openai.com/static-rsc-4/F3kbnvG4gONCF394eEVWBLpgM7vFZbV1X-6aFQVhmqCuW6ik1rOjB0X4VBRoWpI_Q3A1mNsf9R4sHx4saYMC-VD1poUml5A-Rm6cRvO00R4BQruax8kqVrIK0xFqyzarM0Ef4-XDt3MAxSYf5tPNPxnlZ4xSjcvniyYaZWvhngc?purpose=inline)

[cb.kku.edu.sa](https://cb.kku.edu.sa/en/node/294?utm_source=chatgpt.com)

### Step 6: Add X-axis and Y-axis labels

We should describe what each axis represents.

Use:

- `plt.xlabel()` for the horizontal axis.
- `plt.ylabel()` for the vertical axis.

```python

plt.plot(months, students)
plt.title("Monthly Student Enrollment")
plt.xlabel("Months")
plt.ylabel("Number of Students")
plt.show()

```

Expected chart information:

- Title: Monthly Student Enrollment
- X-axis: Months
- Y-axis: Number of Students

### Step 7: Display the chart

The function `plt.show()` displays the completed chart.

It is normally placed at the end of the chart code.

```python
plt.show()
```

Without this command, a chart may not appear in some Python environments.

### Step 8: Add markers to show individual data points

A line connects data points, but we may also want to display the individual points clearly.

We can use the `marker` parameter.

```python
plt.plot(months, students, marker="o")
plt.title("Monthly Student Enrollment")
plt.xlabel("Months")
plt.ylabel("Number of Students")
plt.show()
```

![\[Excel\] 꺾은선 차트가 삐죽삐죽하다면? 부드러운 곡선으로 차트 꾸미기](https://images.openai.com/static-rsc-4/5-ltkDmngnQI3KwKQ_uV8ghZSUeNx8COrSOeBycIgBPp7Ja3ruDv8GeRER_7eYimCsuZ9ez7ODcgLjPT6MVjttdbKD5i0AFFmNSfIV05hdrDfYzCs10g6hnp8uvk98rX5nTkJAdu6nhZbBLfRZe8X8VejHE_p27PLTDuOctqNIQ?purpose=inline)

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

```python
plt.plot(    months,    students,    color="green",    linestyle="--",    marker="o")
plt.title("Monthly Student Enrollment")
plt.xlabel("Months")
plt.ylabel("Number of Students")plt.show()
```

**Important parameters:**

| Parameter   | Purpose                  |
| ----------- | ------------------------ |
| `color`     | Changes line color.      |
| `linestyle` | Changes line appearance. |
| `marker`    | Displays data points.    |

**Common line styles:**

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

```python
plt.plot(months, students, marker="o")
plt.title("Monthly Student Enrollment")
plt.xlabel("Months")
plt.ylabel("Number of Students")
plt.grid(True)plt.show()
```

![Python Charts - Saving High-Resolution Figures in Seaborn](https://images.openai.com/static-rsc-4/Ci2zrsO7ZYRP1vGa8uivC9Txgjy5Rzc0p4NRmBLSiQk92No6A5GElJUJ9qtJKbt3Nu0ZEiYPDjPAE5nam0mAG_eFXJm3BHPzFl4Npv6gmu8bkuYlKGSjt4NV5WSC0zIx6x0tvywRpiEe-namXRT_ip5xQ1NahdpHnGhPBjaeCm0?purpose=inline)

[pythoncharts.com](https://www.pythoncharts.com/seaborn/seaborn-save-high-resolution-figures/?utm_source=chatgpt.com)

Here:

- `plt.grid(True)` displays gridlines.
- Gridlines help us compare the position of each point with the axis values.

### Step 11: Add a legend

A legend identifies the data shown by a line.

We can use `label` inside `plt.plot()` and `plt.legend()` to display it.

```python
plt.plot(    months,    students,    marker="o",    color="blue",    label="University Enrollment")
plt.title("Monthly Student Enrollment")
plt.xlabel("Months")
plt.ylabel("Number of Students")
plt.legend()plt.grid(True)plt.show()
```

Understand:

- `label` gives a name to the line.
- `plt.legend()` displays that name on the chart.

A legend becomes especially important when a chart contains multiple lines.

### Step 12: Display values using annotations

Sometimes we want to show the exact numerical value beside each point.

We can use `plt.annotate()`.

```python
plt.plot(months, students, marker="o")

for i in range(len(months)):
    plt.annotate(
        students[i],
        (months[i], students[i])
    )

plt.title("Monthly Student Enrollment")
plt.xlabel("Months")
plt.ylabel("Number of Students")
plt.grid(True)

plt.show()
```

**Understand the new code:**

- `len(months)` returns the number of months.
- `range()` generates positions from zero to eleven.
- `for` repeats the annotation operation for every month.
- `students[i]` gets the enrollment value at position `i`.
- `(months[i], students[i])` identifies the location of the point.

Result: Every data point displays its corresponding enrollment value.

### Complete example: Your first professional line chart

Now combine the concepts learned in this section.

```python
import matplotlib.pyplot as plt

# Step 1: Prepare data
months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

students = [
    50, 65, 60, 80, 75, 100,
    110, 95, 120, 130, 125, 150
]

# Step 2: Create line chart
plt.plot(
    months,
    students,
    color="blue",
    linestyle="-",
    linewidth=2,
    marker="o",
    markersize=7,
    label="Student Enrollment"
)

# Step 3: Add chart information
plt.title("Monthly Student Enrollment")
plt.xlabel("Month")
plt.ylabel("Number of Students")

# Step 4: Add data labels
for i in range(len(months)):
    plt.annotate(
        students[i],
        (months[i], students[i]),
        textcoords="offset points",
        xytext=(0, 8),
        ha="center"
    )

# Step 5: Add gridlines and legend
plt.grid(True)
plt.legend()

# Step 6: Display chart
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

![Yearly Overview: Previous Overviews: Office of Enrollment Management: Indiana University Bloomington](https://images.openai.com/static-rsc-4/V4BqnNPZdIPBa7nwgpn4bTdmwjaWfwZy_FuPcxYjoeEyqBGaiL5Wjvi_jX754E1dGsfZwQjTomuslpVKXSYOw0knDPTqOxEogVRDoRQsqzrCRP8pC31bosgVaWobiQros0Qu4RnK_lTXqviGsNUHPJ5eqFi_D69ndh2ZN_Q9psU?purpose=inline)

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

