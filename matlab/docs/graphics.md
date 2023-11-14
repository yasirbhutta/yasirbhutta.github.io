# [MATLAB for Beginners](https://yasirbhutta.github.io/matlab/)

## MATLAB Graphics

- [Download PDF](https://yasirbhutta.github.io/matlab/docs/graphics.pdf)
  
- To access the updated lecture notes, please click on the following link:
[https://yasirbhutta.github.io/matlab/docs/graphics.html](https://yasirbhutta.github.io/matlab/docs/graphics.html)

### 2D Plots

#### Printing Labels

The xlabel() and ylabel() functions are used to label the x and y axes in a figure in MATLAB. The labels should describe the data that is being plotted on each axis.

The title() function is used to add a title to a figure in MATLAB. The title should provide a brief description of the plot.

Example 3: Label the axes and add a title

```matlab
x = linspace(0, 10, 100);
y = sin(x);

plot(x, y);
xlabel('X-axis');
ylabel('Y-axis');
title('Sine Wave');
```

#### Grid and Axex Box

The grid() function is used to add grid lines to a figure in MATLAB. Grid lines can help to make it easier to interpret the data in a plot.

#### Entering Text in a Plot

#### Axis Control

he axis() function is used to set the limits of the axes in a figure in MATLAB. The axes are the horizontal and vertical lines that extend across the figure window.

#### Axis Aspect Ration

### Multiple Plots

#### Using plot Command

The plot() function is used to create a line plot in MATLAB. A line plot is a graphical representation of a set of data points connected by a line.

#### Using hold Command

The hold function is used to prevent MATLAB from overwriting existing plots when creating new ones. By default, MATLAB overwrites existing plots when creating new ones. However, if you use the hold function before creating a new plot, MATLAB will add the new plot to the existing plot instead of overwriting it.

Example 2: Plotting multiple lines on the same graph

```matlab
x = linspace(0, 10, 100);
y1 = sin(x);
y2 = cos(x);

plot(x, y1, 'b');
hold on;
plot(x, y2, 'r');
hold off;
```

This will plot two lines on the same graph, one blue and one red. The hold on and hold off functions are used to prevent the second line from overwriting the first line.

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

#### Example: Visualizing Daily Temperature Data with Subplots in MATLAB

Download dataset `Daily Temperature (Dataset #2)` from [Datasets](../../datasets/index.md).

```matlab
% Specify the name of the CSV file
filename = 'ds2.csv';

% Read the data from the CSV file into a table variable
data = readtable(filename,'VariableNamingRule','preserve'); 

% Create the first subplot
subplot(1, 2, 1);
plot(data.dated, data.temperature);
title('Daily Temperatures');
xlabel('Date');
ylabel('Temperature (C)');

% Create the second subplot
subplot(1, 2, 2);
histogram(data.temperature);
title('Temperature Distribution');
xlabel('Temperature (C)');
ylabel('Frequency');

% Save the figure
saveas(gcf, 'daily_temperatures.png');
```

### Specialized 2D plots

#### Logarithmic Plot Functions

#### polar

#### area

#### bar

Example 3: Plotting a bar graph

```matlab
x = categorical({'A', 'B', 'C'});
y = [10, 20, 30];

bar(x, y);
```

**Categorical Arrary:** categorical is a data type to store data with values from a finite set of discrete categories. For example, the syntax C = categorical({'R','G','B','B','G','B'}) creates a categorical array with six elements that belong to the categories R, G, or B.[^1]

Download dataset `Population by Country` from [Datasets](../../datasets/index.md).

##### Example: Population Distribution by Country using bar charts

```matlab
% Specify the name of the CSV file
filename = 'ds1.csv';

% Read the data from the CSV file into a table variable
data = readtable(filename,'VariableNamingRule','preserve'); 

% Convert the Country column to a categorical variable
x = categorical(data.Country);

% Generate a bar plot of the population data
bar(x,data.Population);

% Add a title and axis labels to the plot
title('Population by Country');
xlabel('Country');
ylabel('Population');

```

**See also:**

- [bar - MathWorks Help Center](https://www.mathworks.com/help/matlab/ref/bar.html)

#### barh

**See also:**

#### histogram

Example 4: Plotting a histogram

```matlab
x = randn(1000, 1);
histogram(x);
```

**See also:**

- [histogram - MathWorks Help Center](https://www.mathworks.com/help/matlab/ref/matlab.graphics.chart.primitive.histogram.html)
- [Replace Discouraged Instances of hist and histc](https://www.mathworks.com/help/matlab/creating_plots/replace-discouraged-instances-of-hist-and-histc.html)

#### rose

#### pie

Example 5: Plotting a pie chart

```matlab
X = [10 20 30];

pie(X);
```

This will plot a pie chart with three slices, one for each value in the vector X. The size of each slice represents the proportion of that value to the total.

#### Example: Visualizing Fruit Sales Distribution with Exploded Pie Chart

```matlab
% Define the fruit names and sales figures
fruit_names = ["Apples", "Oranges", "Bananas", "Grapes", "Strawberries"];
sales_figures = [120, 90, 150, 80, 60];

% Define the explode vector to offset the "Bananas" slice
explode = [0 0 1 0 0];

% Create the pie chart and label the slices
pie(sales_figures, explode, fruit_names);

% Set the title of the pie chart
title('Fruit Sales Pie Chart');
```

**See also:**

- [MATLAB Tutorial: Visualizing Fruit Sales Distribution with Exploded Pie Chart](https://youtu.be/5X5gelyCgr4?si=mLjZtwFRrdv7pEhG)

#### stairs

#### stem

#### compass

### 3D Plots

#### plot3

##### Example: Create 3-D Bar Graph from Vector Data

```matlab
% Create a vector of values to plot.
z = [50 40 30 20 10];

% Plot the 3-D bar graph.
bar3(z);

% Set the axes labels.
xlabel('X Axis');
ylabel('Y Axis');
zlabel('Z Axis');

% Set the title.
title('My 3-D Bar Graph');
```

**See also:**

- [bar3 - MathWorks Help Center](https://www.mathworks.com/help/matlab/ref/bar3.html)

#### bar3

#### bar3h

#### pie3

**See also:**

- [pie3 - MathWorks Help Center](https://www.mathworks.com/help/matlab/ref/pie3.html)

#### stem3

#### meshgrid

#### mesh

#### surf

#### contour and contour3

## True/False (Mark T for True and F for False)

- The MATLAB plot function plots data points as connected line segments. **True**
- The MATLAB bar function plots the relationship between two variables.  **False**
- The xlabel() and ylabel() functions are used to label the X-axis and Y-axis of the current plot, respectively. **True**.
- The clf() function clears the current plot. **True**
- The xlabel, ylabel, and title functions in MATLAB are used to add labels to a plot. **True**
- You can customize the appearance of a plot in MATLAB by specifying various properties like line color, line style, and marker type. **True**

## Multiple Choice (Select the best answer)

> Which of the following functions is used to create a plot of a line?

1. [x] plot()
2. [ ] stem()
3. [ ] bar()
4. [ ] pie()

> Which of the following functions is used to create a plot of a bar graph?

1. [ ] plot()
2. [ ] stem()
3. [x] bar()
4. [ ] pie()

> Which of the following functions is used to create a plot of a pie chart?

1. [ ] plot()
2. [ ] stem()
3. [ ] bar()
4. [x] pie()

> Which of the following is NOT a valid MATLAB graphics command?

1. [ ] plot()
2. [ ] subplot()
3. [x] log1pp()
4. [ ] title()

> What is the purpose of the title() function?

1. [ ] To label the axes of a plot
2. [ ] To create a new figure window
3. [x] To add a title to a plot
4. [ ] To change the color of a plot

> How can you create a subplot in MATLAB?

1. [x] Use the subplot() function.
2. [ ] Use the figure() function.
3. [ ] Use the plot() function.
4. [ ] Use the title() function.

> What is the difference between a bar plot and a histogram?

1. [x] A bar plot is used to compare categorical data, while a histogram is used to visualize continuous data.
2. [ ] A bar plot is used to represent frequencies, while a histogram is used to represent probabilities.
3. [ ] A bar plot is used to show the distribution of data, while a histogram is used to compare means.
4. [ ] A bar histogram is used to show the relationship between two variables, while a plot is used to show the distribution of a single variable.

> Which of the following is NOT a valid MATLAB graphics function?

1. [ ] plot()
2. [ ] bar()
3. [ ] pie()
4. [x] histrogram()
5. [ ] stem()

> Which of the following is the correct syntax for plotting a line graph of the function y = x^2?

1. [ ] plot(x, y=x^2)
2. [x] plot(x, x.^2)
3. [ ] plot(y, x^2)
4. [ ] plot(x^2, y)
5. [ ] plot(y^2, x)

> What is the purpose of the legend() function?

1. [ ] To label the x-axis of a graph
2. [ ] To label the y-axis of a graph
3. [ ] To add a title to a graph
4. [x] To add a legend to a graph
5. [ ] To change the color of a line on a graph

> What is the purpose of the xlabel() and ylabel() functions?

1. [x] To label the x-axis of a graph
2. [x] To label the y-axis of a graph
3. [ ] To add a title to a graph
4. [ ] To add a legend to a graph
5. [ ] To change the color of a line on a graph

> Which of the following commands would you use to change the title of the current figure to 'My Figure'?

1. [x] title('My Figure')
2. [ ] sets(gcf, 'Title', 'My Figure')
3. [ ] title(figure, 'My Figure')
4. [ ] sets(figure, 'Title', 'My Figure')

> What is the command to create a 2-D line plot of x and y vectors in MATLAB?

1. [x] plot(x,y)
2. [ ] line(x,y)
3. [ ] graph(x,y)
4. [ ] draw(x,y)

> What is the command to create a pie chart of a vector x in MATLAB? 

1. [ ] pie(x)
2. [ ] pie3(x)
3. [ ] piechart(x)
4. [x] pie(x) and pie3(x)

> Which MATLAB function is used to label the axes of a figure?

1. [ ] title()
2. [ ] legend()
3. [x] xlabel()
4. [x] ylabel()

> What is the command to show the box outline around the axes in MATLAB?

1. [ ] box off
2. [ ] box show
3. [x] box on
4. [ ] box hide

> What is the command to show the grid in a MATLAB figure?

1. [ ] box on
2. [x] grid on
3. [ ] grid off
4. [ ] box show
5. [ ] box hide

> Which MATLAB function is used to add text to a plot?

1. [x] text()
2. [ ] label()
3. [ ] title()
4. [ ] legend()

> How can you change the font color of the text in a plot?

1. [x] Use the color property of the text() function.
2. [ ] Use the Color property of the current axes.
3. [ ] Use the Color property of the figure window.
4. [ ] Use the Color property of the current figure.

**Code snippet:**

```matlab
x = 1:10;
y = 1:10;
plot(x, y);
text(6, 5, 'string', 'color', 'red');
```

> How can you position text relative to a specific data point in a plot?

1. [x] Use the x and y coordinates of the data point.
2. [ ] Use the DataPoints property of the text() function.
3. [ ] Use the handle property of the data point object.
4. [ ] Use the Position property of the text object.

> What is the primary purpose of the `hold` function in MATLAB plotting?

1. [ ] To clear the current plot window
2. [ ] To temporarily pause the execution of a plot command
3. [x] To prevent subsequent plot commands from overwriting existing plots
4. [ ] To adjust the scaling of the plot axes

> Which of the following statements correctly describes the behavior of the `hold` function when used in conjunction with the plot function?

1. [ ] The hold function must be called before the plot function for it to have any effect.
2. [ ] The hold function must be called after the plot function for it to have any effect.
3. [x] The hold function remains active until it is explicitly turned off using the hold off command.
4. [ ] The hold function only affects the current plot window and has no effect on subsequent plot windows.

> Which of the following scenarios would require the use of the `hold` function?

1. [ ] Plotting two different line graphs of separate data sets on the same axes
2. [ ] Plotting multiple curves representing different functions in the same plot window
3. [ ] Creating a scatter plot of data points along with a trend line
4. [x] All of the above

> What are the two basic arguments required for the `plot()` function?

1. [x] x-coordinates and y-coordinates
2. [ ] x-axis label and y-axis label
3. [ ] figure window and axes labels
4. [ ] title and legend

> What is the default line style used by the `plot()` function?

1. [x] Solid line (-)
2. [ ] Dashed line (--)
3. [ ] Dotted line (:)
4. [ ] Dot-dash line (- -)

> What is the default line color used by the `plot()` function?

1. [ ] Blue
2. [ ] Red
3. [ ] Green
4. [x] Black

> Which line style is represented by the string '-.'?

1. [ ] Solid line
2. [ ] Dashed line
3. [ ] Dotted line
4. [ ] [x] Dash-dotted line

> What is the purpose of using different line styles in a plot?

1. [ ] To make the plot more visually appealing
2. [ ] To distinguish between different data sets in a plot
3. [ ] To increase the readability of the plot
4. [x] All of the above

> How would you set the line style of a plot to be dashed?

1. [x] plot(x, y, '--')
2. [ ] line(x, y, '--')
3. [ ] get(plot(x, y), 'LineStyle', '--')
4. [ ] style(plot(x, y), '--')

> How would you create a plot with two lines, one solid and one dashed?

1. [ ] plot(x1, y1, '-', x2, y2, '--')
2. [ ] line(x1, y1, '-', x2, y2, '--')
3. [ ] figure(plot(x1, y1), 'LineStyle', '-'), plot(x2, y2), 'LineStyle', '--')
4. [ ] style(plot(x1, y1), '-'), plot(x2, y2), 'LineStyle', '--')

> What is the default marker style for a line plot in MATLAB?

1. [x] No marker
2. [ ] Circle (o)
3. [ ] Plus sign (+)
4. [ ] Asterisk (*)

## Exercises

## Review Questions

- What is the syntax for adding text to a plot using the text() function?
- What is the purpose of the `plot()` function in MATLAB?
- What is the purpose of the `grid()` function in MATLAB?
- What is the purpose of the `axis()` function in MATLAB?
- What is the purpose of the `xlabel()` and `ylabel()` functions in MATLAB?
- What is the purpose of the `title()` function in MATLAB?
- What is the purpose of the `legend()` function in MATLAB?
- What are some of the different line styles that can be used in MATLAB?
- What are some of the different marker styles that can be used in MATLAB?
- What is the difference between the hold on and hold off functions in MATLAB?
- How do you use the line function in MATLAB?

**Answer:**

The line function is used to create a line plot in MATLAB. The syntax for the line function is as follows:

```matlab
line(x, y)
```

where x is a vector of x-coordinates and y is a vector of y-coordinates.

- How do you plot a line in MATLAB using `plot` function?

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

- How do you add a `title` to a figure in MATLAB?

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

- [^1:] [Categorical Arrays - MathWorks Help Center](https://www.mathworks.com/help/matlab/categorical-arrays.html)
- [MATLAB Graphics](https://www.mathworks.com/help/matlab/graphics.html)
- [MATLAB: Plotting - tutorialspoint](https://www.tutorialspoint.com/matlab/matlab_plotting.htm)

## Social Links

- [WhatsApp Channel](https://whatsapp.com/channel/0029VaC3BC160eBZZSs3CW0c)
- [Web](https://yasirbhutta.github.io/)
- [Youtube](https://www.youtube.com/yasirbhutta)
- [Facebook](https://www.facebook.com/yasirbhutta786)
- [Twitter](https://twitter.com/yasirbhutta)
