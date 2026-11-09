
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
