---
layout: page
title: Customize Line Charts in Python with Matplotlib
description: Learn how to customize a Matplotlib line chart by changing colors, markers, labels, gridlines, titles, and styling for more effective data visualization.
keywords: customize line chart Python, Matplotlib chart customization, line chart styling, Python plotting style, change line colors, add labels to plots, modify plot legend, Matplotlib customization
---

## 1. Modify and Customize

In this section, we will learn how to modify an existing line chart.

The objective is to understand how changing individual parameters affects the chart.

## 2. Complete Code

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


### A. Change the chart title

Use `plt.title()`.

```python
plt.title("University Enrollment Report")
```

You can replace the title with any meaningful description.

### B. Change line color

Use the `color` parameter.

```python
plt.plot(months, students, color="red")
```

Other options include:

```text
color="blue"
color="green
"color="orange
"color="purple"
```

### C. Change line width

Use `linewidth`.

```python
plt.plot(months, students, linewidth=3)
```

- `linewidth=1`: Thin line.
- `linewidth=2`: Medium line.
- `linewidth=3`: Thick line.

### D. Change line style

Use `linestyle`.

```python
plt.plot(months, students, linestyle="--")
```

Examples:

```python
plt.plot(months, students, linestyle="-")
plt.plot(months, students, linestyle="--")
plt.plot(months, students, linestyle=":")
plt.plot(months, students, linestyle="-.")
```

### E. Add markers

Use `marker`.

```python
plt.plot(months, students, marker="o")
```

This displays a circular marker at each data point.

### F. Change marker size

Use `markersize`.

```python
plt.plot(    months,    students,    marker="o",    markersize=10)
```

Larger values make the markers bigger.

### G. Change marker colors

Matplotlib allows us to customize the marker's face and border colors.

```python
plt.plot(months, students,    marker="o",    color="blue",    markerfacecolor="yellow",    markeredgecolor="red",    markersize=8)
plt.show()
```

| Parameter         | Purpose               |
| ----------------- | --------------------- |
| `color`           | Connecting line color |
| `markerfacecolor` | Inner marker color    |
| `markeredgecolor` | Marker border color   |
| `markersize`      | Marker size           |

### H. Change figure size

Use `plt.figure(figsize=(width, height))`.

```python
plt.figure(figsize=(12, 5))
plt.plot(months, students, marker="o")
plt.show()
```

Here:

- `12` represents the figure width in inches.
- `5` represents the figure height in inches.

A larger figure provides more space for the chart.

### I. Change font size

We can change the font size of the title and axis labels.

```python
plt.plot(months, students, marker="o")
plt.title("Monthly Enrollment", fontsize=18)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Students", fontsize=12)
plt.show()
```

### J. Add data labels or annotations

Use `plt.annotate()` to display values near data points.

```python

plt.plot(months, students, marker="o")

for i in range(len(months)):
    plt.annotate(
        students[i],
        (months[i], students[i]),
        xytext=(0, 8),
        textcoords="offset points",
        ha="center"
    )

plt.show()

```

The `xytext` parameter controls the position of the annotation relative to the point.

### K. Add gridlines

```python
plt.grid(True)
```

You can also customize gridline appearance.

```python
plt.grid(    True,    linestyle="--",    alpha=0.5)
```

Here:

- `linestyle="--"` displays dashed gridlines.
- `alpha=0.5` controls transparency.

### L. Customize X-axis and Y-axis ticks

Ticks are the values displayed along the axes.

**For example:**

```python
plt.plot(months, students, marker="o")
plt.yticks(range(0, 181, 20))
plt.show()
```

This displays Y-axis values at intervals of 20:

`0, 20, 40, 60, 80, ... 180`

We can also customize the X-axis ticks.

```python
plt.xticks(rotation=45)
```

### M. Rotate X-axis labels

Long category names may overlap.

Use:

```python
plt.xticks(rotation=45)
```

For example, month names will be displayed at a 45-degree angle.

### N. Add a legend

```python
plt.plot(    months,    students,    label="Enrollment")
plt.legend()
```

We can also change the legend position:

```python
plt.legend(loc="upper left")
```

### O. Set axis limits

Axis limits control the range displayed on the chart.

Use:

- `plt.xlim()` for the horizontal axis.
- `plt.ylim()` for the vertical axis.

Example:

```python
plt.plot(months, students, marker="o")
plt.ylim(0, 180)
plt.show()
```

This sets the Y-axis range from 0 to 180.

**Important:** Choose limits carefully. An inappropriate scale can make small changes appear much larger than they really are.

### P. Save the chart as a PNG image

Use `plt.savefig()`.

```python
plt.plot(months, students, marker="o")
plt.title("Monthly Student Enrollment")
plt.savefig("student_enrollment.png", dpi=300, bbox_inches="tight")
plt.show()
```

**Understand the parameters:**

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

**Complete Python code**

```python
import matplotlib.pyplot as plt

months = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

cs_students = [
    50, 55, 60, 65, 70, 75,
    80, 85, 90, 95, 100, 110
]

it_students = [
    40, 45, 50, 55, 60, 70,
    75, 80, 85, 90, 95, 100
]

plt.figure(figsize=(10, 5))

plt.plot(
    months,
    cs_students,
    color="blue",
    marker="o",
    label="Computer Science"
)

plt.plot(
    months,
    it_students,
    color="green",
    marker="s",
    label="Information Technology"
)

plt.title("Monthly Department Enrollment")
plt.xlabel("Month")
plt.ylabel("Number of Students")

plt.grid(True, alpha=0.3)
plt.legend()

plt.tight_layout()
plt.show()
```

![FIUDA](https://images.openai.com/static-rsc-4/qSCQU_5GCMJB58I9xIqtn72JEGNJHCP9xVtyBxdekGkx_3s6Oiy4VhaiTGr4dt6UTcFmc5PtMfUerASwc-GYCpLnBhBtPx_xsfkyDocMElri1s5uAG0vjV_ppAltrf-bvNW9q7tP8iezxpq58pBTX0CDyecLpy59thDgO5W9CqY?purpose=inline)

[fi.uda.cl](https://fi.uda.cl/FIUDAVISIBLE/estudiantes.html?utm_source=chatgpt.com)

What does this chart show?

- The blue line represents Computer Science.
- The green line represents Information Technology.
- Both departments show an overall increasing trend.
- Computer Science has higher enrollment throughout the year.

### B. Line Chart with Different Styles

We can display multiple line styles to understand how Matplotlib represents different patterns.

```python
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]

a = [20, 30, 40, 50, 60]
b = [25, 35, 45, 55, 65]
c = [30, 40, 50, 60, 70]
d = [35, 45, 55, 65, 75]

plt.plot(months, a, linestyle="-", label="Solid")
plt.plot(months, b, linestyle="--", label="Dashed")
plt.plot(months, c, linestyle=":", label="Dotted")
plt.plot(months, d, linestyle="-.", label="Dash-dot")

plt.title("Different Line Styles")
plt.xlabel("Month")
plt.ylabel("Values")

plt.legend()
plt.grid(True)

plt.show()
```

![请在同一张图中画出“实线、点线、虚线、双线”这四种线_python线的类型 有哪些对应代码-CSDN博客](https://images.openai.com/static-rsc-4/NXqAI2S47FoZJzCuto_DE4g8szad9Jol0Z84HzPNOTcvHKAZYai8cCbtTgL1lZNIj8SIZlrgQ2cYVV5sOMN9h2RRxGg71dKpew1PHpwx6_8d4FfkFyJtLo-XQVt9LCMmDRCkROBTE4_S9WxfcDy5Fb2ZoT7Dh26c1MvVrii-VC4?purpose=inline)

[blog.csdn.net](https://blog.csdn.net/qq_43585760/article/details/144008386?utm_source=chatgpt.com)

### C. Line Chart with Markers

Markers make individual data points easier to identify.

```python
import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]

attendance = [80, 85, 78, 90, 95]

plt.plot(
    days,
    attendance,
    marker="o",
    markersize=10,
    color="purple",
    linewidth=2
)

plt.title("Weekly Student Attendance")
plt.xlabel("Days")
plt.ylabel("Number of Students")

plt.grid(True)

plt.show()
```

![ANALYZING AND INTERPRETING GRAPHS OF PRIMARY DATA.pptx](https://images.openai.com/static-rsc-4/yuDDnPgvigf6_snRou5fys-V9--CL7aW-1vzJo877yO4ZfJ4Nisv7xPynvnl3MtSYchgaDBcgtu_qzgMj-1O1Rduw1kGxplZZWm5wYLkxxI0SR2IGD0jjEqaDwelhj1yeCyvq8D8zDuZGxkMc0JjuZrkLMvzV43S7jz82jq2iEo?purpose=inline)

[slideshare.net](https://www.slideshare.net/slideshow/analyzing-and-interpreting-graphs-of-primary-data-pptx/286211047?utm_source=chatgpt.com)

### D. Horizontal vs Vertical Concept

A standard line chart normally uses:

- A horizontal X-axis.
- A vertical Y-axis.

The X-axis represents the sequence, such as months or days.

The Y-axis represents numerical measurements, such as enrollment or temperature.

![Activities Activity 1.1 Construct a line graph using the data given from the table below. Online Class - Brainly.ph](https://images.openai.com/static-rsc-4/F7V4pKV_rsgNJ246mS30LAefhcPjaRFSn9kA430ClKc9PNYqtO6uH61avLi0So5DxkvZlp0CL0dFLSRzMBtpXhAZbOdTZOSNoBaq1LRknzWMc4rhvqRsP1b1elCgP5kEO0dCJ_sw8OHsRDGWbrEUxnMg5PnKkBBmDpePkeQqM6E?purpose=inline)

[brainly.ph](https://brainly.ph/question/29110529?utm_source=chatgpt.com)

Can we make a horizontal line chart?

Yes. We can swap the axes using `plt.plot()`.

```python
import matplotlib.pyplot as plt

months = [1, 2, 3, 4, 5]
students = [50, 65, 60, 80, 75]

plt.plot(
    students,
    months,
    marker="o"
)

plt.title("Horizontal Orientation Example")
plt.xlabel("Number of Students")
plt.ylabel("Month Number")

plt.grid(True)

plt.show()
```

However, this changes the meaning of the axes. It is not the usual way of displaying time-based line charts.

**Remember:** Use the horizontal axis for the ordered sequence and the vertical axis for the measured values in a standard time-series line chart.
