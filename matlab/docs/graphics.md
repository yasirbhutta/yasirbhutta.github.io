# MATLAB

## MATLAB Graphics

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

## References

- [MATLAB Graphics](https://www.mathworks.com/help/matlab/graphics.html)
- [MATLAB: Plotting - tutorialspoint](https://www.tutorialspoint.com/matlab/matlab_plotting.htm)