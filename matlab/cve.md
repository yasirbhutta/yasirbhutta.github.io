# Matlab - Constants, Variables and Expressions

## Operators

### Arithmetic Operators

#### Addition (+):

```matlab
x = 5;
y = 10;
z = x + y;
disp(z); % Output: 15
```

#### Subtraction (-):

```matlab
x = 10;
y = 5;
z = x - y;
disp(z); % Output: 5
```

#### Multiplication (*):

```matlab
x = 2;
y = 3;
z = x * y;
disp(z); % Output: 6
```

#### Division (/):

```matlab
x = 6;
y = 3;
z = x / y;
disp(z); % Output: 2
```

#### Exponentiation (^):

```matlab
x = 2;
y = 3;
z = x ^ y;
disp(z); % Output: 8
```

#### Modulo (%):

```matlab
x = 7;
y = 3;
z = mod(x,y);
disp(z); % Output: 1
```

## Example: Calculate the area of circle with a radius of 5 cm

```matlab
% Define the radius of the circle
r = 5;

% Calculate the area of the circle
area = pi * r^2;

% Display the result
fprintf('The area of the circle with radius %.2f is %.2f.\n', r, area);
```

In this example, we define the radius of the circle as `r=5`. Then, we use the formula for the area of a circle, which is `pi * r^2`, to calculate the area. The `pi` function is a built-in MATLAB function that returns the value of pi (approximately 3.1416). Finally, we use the `fprintf` function to display the result, which is the area of the circle with two decimal places.

You can adjust the value of `r` to calculate the area of a circle with a different radius.

## Example: Calculate the circumference of the rectangle

```matlab
% Define the width and height of the rectangle
w = 5;
h = 10;

% Calculate the circumference of the rectangle
circumference = 2 * (w + h);

% Display the result
fprintf('The circumference of the rectangle with width %.2f and height %.2f is %.2f.\n', w, h, circumference);
```

In this example, we define the width and height of the rectangle as `w=5` and `h=10`, respectively. Then, we use the formula for the circumference of a rectangle, which is `2 * (width + height)`, to calculate the circumference. Finally, we use the `fprintf` function to display the result, which is the circumference of the rectangle with two decimal places. 

You can adjust the values of `w` and `h` to calculate the circumference of a rectangle with different dimensions.

## Example: Calculate the area of the triangle

```matlab
% Define the base and height of the triangle
b = 6;
h = 4;

% Calculate the area of the triangle
area = 0.5 * b * h;

% Display the result
fprintf('The area of the triangle with base %.2f and height %.2f is %.2f.\n', b, h, area);
```

In this example, we define the base and height of the triangle as `b=6` and `h=4`, respectively. Then, we use the formula for the area of a triangle, which is `0.5 * base * height`, to calculate the area. Finally, we use the `fprintf` function to display the result, which is the area of the triangle with two decimal places.

You can adjust the values of `b` and `h` to calculate the area of a triangle with different dimensions.

## Example: Calculate the semiperimeter of a spherical triangle

```matlab
% Define the three sides of the spherical triangle
a = pi/6;  % in radians
b = pi/4;  % in radians
c = pi/3;  % in radians

% Calculate the semiperimeter of the spherical triangle
s = (a + b + c)/2;

% Display the result
fprintf('The semiperimeter of the spherical triangle with sides %.2f, %.2f, and %.2f is %.2f.\n', a, b, c, s);
```

In this example, we define the three sides of the spherical triangle as `a=pi/6`, `b=pi/4`, and `c=pi/3`, which are angles measured in radians. Then, we use the semiperimeter formula, which is `s = (a + b + c)/2`, to calculate the semiperimeter of the spherical triangle.

Finally, we use the `fprintf` function to display the result, which is the semiperimeter of the spherical triangle with two decimal places.

You can adjust the values of `a`, `b`, and `c` to calculate the semiperimeter of a different spherical triangle.

## Example: Calculate the area of a triangle using Heron's formula:

```matlab
% Define the lengths of the sides of the triangle
a = 5;
b = 6;
c = 7;

% Calculate the semiperimeter of the triangle
s = (a + b + c)/2;

% Calculate the area of the triangle using Heron's formula
A = sqrt(s * (s - a) * (s - b) * (s - c));

% Display the result
fprintf('The area of the triangle with sides %.2f, %.2f, and %.2f is %.2f.\n', a, b, c, A);
```

In this example, we define the lengths of the sides of the triangle as `a=5`, `b=6`, and `c=7`. Then, we use the semiperimeter formula, which is `s = (a + b + c)/2`, to calculate the semiperimeter of the triangle. Finally, we use Heron's formula, which is `A = sqrt(s * (s - a) * (s - b) * (s - c))`, to calculate the area of the triangle.

The `sqrt` function is the square root function in MATLAB. The `fprintf` function is used to display the result, which is the area of the triangle with two decimal places.

You can adjust the values of `a`, `b`, and `c` to calculate the area of a different triangle using Heron's formula.

## factorial

f = factorial(n) returns the product of all positive integers less than or equal to n, where n is a nonnegative integer value. If n is an array, then f contains the factorial of each value of n. The data type and size of f is the same as that of n.

The factorial of n is commonly written in math notation using the exclamation point character as n!. Note that n! is not a valid MATLAB® syntax for calculating the factorial of n. [^1]

## References

- [^1]: [Factorial of input - MATLAB factorial - MathWorks](https://www.mathworks.com/help/matlab/ref/factorial.html)


