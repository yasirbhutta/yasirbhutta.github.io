# MATLAB

## MATLAB Graphics

### 2D Plots

#### Printing Labels

The xlabel() and ylabel() functions are used to label the x and y axes in a figure in MATLAB. The labels should describe the data that is being plotted on each axis.

The title() function is used to add a title to a figure in MATLAB. The title should provide a brief description of the plot.

#### Grid and Axex Box

The grid() function is used to add grid lines to a figure in MATLAB. Grid lines can help to make it easier to interpret the data in a plot.

#### Entering Text in a Plot

#### Axis Control

he axis() function is used to set the limits of the axes in a figure in MATLAB. The axes are the horizontal and vertical lines that extend across the figure window.

#### Axi Aspect Ration

### Multiple Plots

#### Using plot Command

The plot() function is used to create a line plot in MATLAB. A line plot is a graphical representation of a set of data points connected by a line.

#### Using hold Command

The hold function is used to prevent MATLAB from overwriting existing plots when creating new ones. By default, MATLAB overwrites existing plots when creating new ones. However, if you use the hold function before creating a new plot, MATLAB will add the new plot to the existing plot instead of overwriting it.

#### Using line Command

### Style Options

#### Example

```matlab
x = 1:1:10;

y1 = sqrt(x.^2+1);
y2 = 2 * x + 20;
y3 = 3 * x + 3;

plot(x,y1,'r*:');
line(x,y2);
line(x,y3);
```

#### Example: Plotting Two Functions on the Same Graph in MATLAB

```matlab
x = 1:1:10;

y1 = sqrt(x.^2+1);
y2 = 2 * x + 20;


plot(x, y1, 'r', x, y2, 'bo');
axis([0 12 0 45]);
```

### LEGEND

The legend() function is used to create a legend for a figure in MATLAB. A legend is a key that explains which line or curve corresponds to which data set.

### Example

```matlab
% Real world data example
% Global average temperature data from NASA
% https://data.giss.nasa.gov/gistemp/graphs/

% Load the data
data = load('global_average_temperature.csv');

% Extract the years and temperatures
years = data(:, 1);
temperatures = data(:, 2);

% Create a line plot of the data
figure;
plot(years, temperatures);

% Add a legend
legend('Global average temperature');

% Set the axis labels and title
xlabel('Year');
ylabel('Temperature (°C)');
title('Global Average Temperature from 1880 to 2022');
```

### SUBPLOTS

```matlab```

### Specialized 2D plots

#### Logarithmic Plot Functions

#### polar

#### area

#### bar

#### barh

#### hist

#### rose

#### pie

#### stairs

#### stem

#### compass

### 3D Plots

#### plot3

#### bar3

#### bar3h

#### pie3

#### stem3

#### meshgrid

#### mesh

#### surf

#### contour and contour3

## True/False (Mark T for True and F for False)

## Multiple Choice (Select the best answer)

Which of the following functions is used to create a plot of a line?
A. plot()
B. stem()
C. bar()
D. pie()

Which of the following functions is used to create a plot of a bar graph?
A. plot()
B. stem()
C. bar()
D. pie()

Which of the following functions is used to create a plot of a pie chart?
A. plot()
B. stem()
C. bar()
D. pie()

Which of the following is NOT a valid MATLAB graphics command?

(a) plot()
(b) subplot()
(c) log1p()
(d) title()

What is the purpose of the title() function?

(a) To label the axes of a plot
(b) To create a new figure window
(c) To add a title to a plot
(d) To change the color of a plot

How can you create a subplot in MATLAB?

(a) Use the subplot() function.
(b) Use the figure() function.
(c) Use the plot() function.
(d) Use the title() function.

What is the difference between a bar plot and a histogram?

(a) A bar plot is used to compare categorical data, while a histogram is used to visualize continuous data.
(b) A bar plot is used to represent frequencies, while a histogram is used to represent probabilities.
(c) A bar plot is used to show the distribution of data, while a histogram is used to compare means.
(d) A bar plot is used to show the relationship between two variables, while a histogram is used to show the distribution of a single variable.

Which of the following is NOT a valid MATLAB graphics function?

(a) plot()
(b) bar()
(c) pie()
(d) histogram()
(e) stem()

Which of the following is the correct syntax for plotting a line graph of the function y = x^2?

(a) plot(x, y^2)
(b) plot(x, x^2)
(c) plot(y, x^2)
(d) plot(x^2, y)
(e) plot(y^2, x)

What is the purpose of the legend() function?

(a) To label the x-axis of a graph
(b) To label the y-axis of a graph
(c) To add a title to a graph
(d) To add a legend to a graph
(e) To change the color of a line on a graph

> What is the purpose of the xlabel() and ylabel() functions?

1. [x] To label the x-axis of a graph
2. [x] To label the y-axis of a graph
3. [ ] To add a title to a graph
4. [ ] To add a legend to a graph
5. [ ] To change the color of a line on a graph

Which of the following commands would you use to create a scatter plot of the data points (x, y)?

(a) plot(x, y)
(b) scatter(x, y)
(c) plotxy(x, y)
(d) scatterxy(x, y)

Which of the following commands would you use to change the title of the current figure to 'My Figure'?

1. [x] title('My Figure')
2. [x] set(gcf, 'Title', 'My Figure')
3. [ ] title(figure, 'My Figure')
4. [ ] set(figure, 'Title', 'My Figure')

Explanation: The title() function can be used to change the title of the current figure. The set() function can also be used to change the title of the current figure, but it requires more verbose syntax.

What is the command to add a title to a chart in MATLAB? A) title(‘text’) B) xlabel(‘text’) C) ylabel(‘text’) D) legend(‘text’)

What is the command to create a 2-D line plot of x and y vectors in MATLAB? A) plot(x,y) B) line(x,y) C) graph(x,y) D) draw(x,y)

What is the command to create a pie chart of a vector x in MATLAB? 

1. [ ] pie(x)
2. [ ] pie3(x)
3. [ ] piechart(x)
4. [x] pie(x) and pie3(x)

Which MATLAB function is used to label the axes of a figure?

(a) xlabel()
(b) ylabel()
(c) title()
(d) legend()

What is the command to show the box outline around the axes in MATLAB? A) box on B) box off C) box show D) box hide

What is the command to show the grid in a MATLAB figure?

A) box on
B) grid on
C) grid off
D) box show
E) box hide

Which MATLAB function is used to add text to a plot?

(a) text()
(b) label()
(c) title()
(d) legend()

How can you change the font color of the text in a plot?

1 [x] Use the color property of the text() function.
(b) Use the Color property of the current axes.
(c) Use the Color property of the figure window.
(d) Use the Color property of the current figure.

**Code snippet:**

```matlab
text(x, y, 'string', 'color', 'red');
```

How can you position text relative to a specific data point in a plot?

1. [x] Use the x and y coordinates of the data point.
(b) Use the DataPoints property of the text() function.
(c) Use the handle property of the data point object.
(d) Use the Position property of the text object.

What is the primary purpose of the hold function in MATLAB plotting?

(a) To clear the current plot window
(b) To temporarily pause the execution of a plot command
[x] To prevent subsequent plot commands from overwriting existing plots
(d) To adjust the scaling of the plot axes

Which of the following statements correctly describes the behavior of the hold function when used in conjunction with the plot function?

(a) The hold function must be called before the plot function for it to have any effect.
(b) The hold function must be called after the plot function for it to have any effect.
[x] The hold function remains active until it is explicitly turned off using the hold off command.
(d) The hold function only affects the current plot window and has no effect on subsequent plot windows.

Which of the following scenarios would require the use of the hold function?

(a) Plotting two different line graphs of separate data sets on the same axes
(b) Plotting multiple curves representing different functions in the same plot window
(c) Creating a scatter plot of data points along with a trend line
[x] All of the above

What are the two basic arguments required for the plot() function?

[] x-coordinates and y-coordinates
(b) x-axis label and y-axis label
(c) figure window and axes labels
(d) title and legend

What is the default line style used by the plot() function?

[x] Solid line (-)
(b) Dashed line (--)
(c) Dotted line (:)
(d) Dot-dash line (- -)

What is the default line color used by the plot() function?

(a) Blue
(b) Red
(c) Green
[x] Black

Which line style is represented by the string '-.'?

(a) Solid line
(b) Dashed line
(c) Dotted line
[x] Dash-dotted line

What is the purpose of using different line styles in a plot?

(a) To make the plot more visually appealing
(b) To distinguish between different data sets in a plot
(c) To increase the readability of the plot
[x] All of the above

How would you set the line style of a plot to be dashed?

[x] plot(x, y, '--')
(b) line(x, y, '--')
(c) get(plot(x, y), 'LineStyle', '--')
(d) style(plot(x, y), '--')

How would you create a plot with two lines, one solid and one dashed?

(a) plot(x1, y1, '-', x2, y2, '--')
(b) line(x1, y1, '-', x2, y2, '--')
(c) figure(plot(x1, y1), 'LineStyle', '-'), plot(x2, y2), 'LineStyle', '--')
(d) style(plot(x1, y1), '-'), plot(x2, y2), 'LineStyle', '--')

What is the default marker style for a line plot in MATLAB?
[x] No marker
(b) Circle (o)
(c) Plus sign (+)
(d) Asterisk (*)

## Exercises

## Review Questions

- What is the syntax for adding text to a plot using the text() function?
- What is the purpose of the plot() function in MATLAB?
- What is the purpose of the grid() function in MATLAB?
- What is the purpose of the axis() function in MATLAB?
- What is the purpose of the xlabel() and ylabel() functions in MATLAB?
- What is the purpose of the title() function in MATLAB?
- What is the purpose of the legend() function in MATLAB?
- What are some of the different line styles that can be used in MATLAB?
- What are some of the different marker styles that can be used in MATLAB?
- What is the difference between the hold on and hold off functions in MATLAB?
- How do you use the line function in MATLAB?

Answer:

The line function is used to create a line plot in MATLAB. The syntax for the line function is as follows:

```matlab
line(x, y)
```

where x is a vector of x-coordinates and y is a vector of y-coordinates.

- How do you plot a line in MATLAB using plot function?

**Answer:**

To plot a line in MATLAB, you can use the plot() function. The plot() function takes two vectors as arguments: the x-values and the y-values. For example, the following command will plot a line with x-values from 1 to 10 and y-values from 1 to 10:

```matlab
x = 1:10;
y = 1:10;
plot(x, y);
```

- How do you change the color of a line in MATLAB?

**Answer:**

To change the color of a line in MATLAB, you can use the Color property. For example, the following command will change the color of the line to red:

```matlab
x = 1:10;
y = 1:10;
plot(x, y, 'Color', 'red');
```

- How do you add a title to a figure in MATLAB?

Answer:

To add a title to a figure in MATLAB, you can use the title() function. For example, the following command will add the title "My Line Plot" to the figure:

```matlab
x = 1:10;
y = 1:10;
plot(x, y);
title('My Line Plot');
```

- How do you add labels to the axes in a figure in MATLAB?

**Answer:**

To add labels to the axes in a figure in MATLAB, you can use the xlabel() and ylabel() functions. For example, the following commands will add the labels "X-Axis" and "Y-Axis" to the x-axis and y-axis, respectively:

```matlab
x = 1:10;
y = 1:10;
plot(x, y);
xlabel('X-Axis');
ylabel('Y-Axis');
```

- How do you add a grid to a figure in MATLAB

**Answer:**

To add a grid to a figure in MATLAB, you can use the grid() function. For example, the following command will add a grid to the figure:

```matlab
x = 1:10;
y = 1:10;
plot(x, y);
grid on;
```

- What is the difference between a 2D and 3D plot in MATLAB?

**Answer:**

A 2D plot is used to visualize data that has two dimensions, such as height and weight. A 3D plot is used to visualize data that has three dimensions, such as height, weight, and depth.

- What does the hold function do in MATLAB? 

## References

- [MATLAB Graphics](https://www.mathworks.com/help/matlab/graphics.html)
- [MATLAB: Plotting - tutorialspoint](https://www.tutorialspoint.com/matlab/matlab_plotting.htm)

## Social Links

- [WhatsApp Channel](https://whatsapp.com/channel/0029VaC3BC160eBZZSs3CW0c)
- [Web](https://yasirbhutta.github.io/)
- [Youtube](https://www.youtube.com/yasirbhutta)
- [Facebook](https://www.facebook.com/yasirbhutta786)
- [Twitter](https://twitter.com/yasirbhutta)
