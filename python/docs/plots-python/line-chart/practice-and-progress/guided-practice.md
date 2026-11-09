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
