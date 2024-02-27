# MATLAB for Beginners - Constants, Variables and Expressions

Connect with me: [Youtube](https://www.youtube.com/yasirbhutta) \| [LinkedIn](https://www.linkedin.com/in/yasirbhutta/) \| [WhatsApp Channel](https://whatsapp.com/channel/0029VaC3BC160eBZZSs3CW0c) \| [Web](https://yasirbhutta.github.io/) \| [Facebook](https://www.facebook.com/yasirbhutta786) \| [Twitter](https://twitter.com/yasirbhutta)


## Data Types

## Data Types in MATLAB

In MATLAB, data types define the kind of information a variable can store and the operations allowed on them. Choosing the correct data type is crucial for optimizing memory usage, calculation accuracy, and code efficiency. Here's a breakdown of the various data types available:

**1. Numeric Data Types:**
    * **Double-precision floating-point (default):**
        - **Representation:** Uses 64 bits for storage, offering a balance between precision and memory usage.
        - **Type:** double
        - **Range:** Approximately `-1.7e+308` to `1.7e+308`.
        - **Precision:** Generally provides 15-16 decimal digits of precision.
        - **Applications:** Suitable for most general-purpose calculations due to its balanced characteristics.
    * **Single-precision floating-point:**
        - **Representation:** Uses 32 bits for storage, offering faster calculations and less memory usage compared to double-precision.
        - **Type:** single
        - **Range:** Approximately `-3.4e+38` to `3.4e+38`.
        - **Precision:** Provides 6-7 decimal digits of precision.
        - **Applications:** Suitable when memory efficiency is a concern, and required precision is not as high as double-precision.
    * **Integer data types:**
        - **Storage:** Use a specific number of bits to store whole numbers (integers) without decimal points, offering efficient memory usage and speed for integer operations.
        - **Types:**
            - `int8`: Signed, 8-bit integer (-128 to 127)
            - `uint8`: Unsigned, 8-bit integer (0 to 255)
            - `int16`: Signed, 16-bit integer (-32768 to 32767)
            - `uint16`: Unsigned, 16-bit integer (0 to 65535)
            - `int32`: Signed, 32-bit integer (-2147483648 to 2147483647)
            - `uint32`: Unsigned, 32-bit integer (0 to 4294967295)
        - **Applications:** For representing and manipulating whole numbers, particularly when memory or speed is critical.
    * **Complex numbers:**
        - **Representation:** Combine real and imaginary parts, using double-precision floating-point elements for storage.
        - **Applications:** Used in calculations involving complex mathematical concepts like electrical engineering, signal processing, and wave mechanics.

**2. Character and String Data Types:**
    * **Character:**
        - Stores a single character as a numeric code corresponding to its position in the Unicode character set.
        - Used for representing individual characters like letters, numbers, and symbols.
    * **String:**
        - An array of characters, allowing you to represent groups of characters as text.
        - Used for storing and manipulating textual data like words, sentences, or paragraphs.

**3. Logical Data Type:**
    * Represents logical values, either `true` or `false`.
    * Used for conditional statements and Boolean operations.
    * 
**Choosing the Right Data Type:**

Consider these factors when selecting a data type:

* **Range of values:** Choose a type that can accommodate the minimum and maximum values you need.
* **Required precision:** Select a type with sufficient precision to handle the level of accuracy needed.
* **Memory constraints:** If memory is limited, consider using efficient data types like integers when appropriate.
* **Functionality:** Choose the type that best suits the intended operations you'll perform on the data.

In MATLAB, there are several ways to check the data type of a variable:

**1. `class` function:**

This is the most common and recommended method. It returns a string indicating the data type of the variable.

```matlab
variable_name = "Hello";
data_type = class(variable_name);
disp(data_type); % Output: "string"
```

**2. `whos` command:**

This command provides a detailed list of all currently defined variables in your workspace, including their name, size, class (data type), and a few other attributes.

```matlab
whos
```

The output will show columns like "Name," "Size," and "Class," allowing you to check the data type for specific variables.

**3. `isa` function:**

This function allows you to check if a variable belongs to a specific data type. It returns `true` if the variable is of the specified type and `false` otherwise.

```matlab
number = 10;
is_integer = isa(number, 'int32');
disp(is_integer); % Output: true
```

**4. Built-in functions for specific types:**

Certain data types have dedicated functions that return information about them. For example, `ischar` checks for characters, `isfloat` checks for floating-point numbers, and `islogical` checks for logical values.

```matlab
text = "This is a string";
is_char = ischar(text);
disp(is_char); % Output: true
```

**Choosing the best method:**

* **`class` function** is the simplest and most versatile option for quickly determining the data type of a variable.
* **`whos` command** is useful when you need to see a complete list of variables and their attributes, not just the data type.
* **`isa` function** is beneficial for checking if a variable belongs to a specific type, often used in conditional statements.
* **Specific type functions** are helpful when working with particular data types and need additional information beyond just the basic class.

Remember, choosing the appropriate method depends on your specific needs and the context of your code.

## constants and Variables




## Operators

### Arithmetic Operators

#### Addition (+)

```matlab
x = 5;
y = 10;
z = x + y;
disp(z); % Output: 15
```

#### Subtraction (-)

```matlab
x = 10;
y = 5;
z = x - y;
disp(z); % Output: 5
```

#### Multiplication (*)

```matlab
x = 2;
y = 3;
z = x * y;
disp(z); % Output: 6
```

#### Division (/)

```matlab
x = 6;
y = 3;
z = x / y;
disp(z); % Output: 2
```

#### Exponentiation (^)

```matlab
x = 2;
y = 3;
z = x ^ y;
disp(z); % Output: 8
```

#### Modulo (%)

```matlab
x = 7;
y = 3;
z = mod(x,y);
disp(z); % Output: 1
```

### Example: ``` Calculates the area of a rectangle

```matlab
% Define the dimensions of the rectangle
width = 5;
height = 7;

% Calculate the area of the rectangle
area = width * height;

% Display the result
disp('The area of the rectangle is:');
disp(area);
```

### Example: Calculate the area of circle with a radius of 5 cm

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

### Example: Calculate the circumference of the rectangle

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

### Example: Calculate the area of the triangle

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

### Example: Calculate the semiperimeter of a spherical triangle

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

### Example: Calculate the area of a triangle using Heron's formula:

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

### Example: How to create a plot of a mathematical function

```matlab
% Define the x-values
x = linspace(-10, 10, 100);

% Define the function y = f(x)
y = sin(x);

% Create a plot of the function
plot(x, y);

% Add labels to the plot
xlabel('x');
ylabel('y');
title('Plot of sin(x)');
```

In this example, we first define a set of x-values using the `linspace` function, which creates an array of 100 equally spaced values between -10 and 10. Then, we define a mathematical function `y = sin(x)` that we want to plot. We use the `plot` function to create a line plot of the function, with the x-values on the horizontal axis and the y-values on the vertical axis. Finally, we add labels to the plot using the `xlabel`, `ylabel`, and `title` functions.

### Example: Generating a random number

```matlab
% Generate a random number between 0 and 1
r = rand();

% Print the random number
disp(r);
```

### Example: Finding the Roots of a Quadratic Equation

```matlab
% Define the coefficients a, b, and c of the quadratic equation ax^2 + bx + c = 0
a = 1;
b = 4;
c = 3;

% Calculate the roots of the quadratic equation using the quadratic formula
x1 = (-b + sqrt(b^2 - 4*a*c)) / (2*a);
x2 = (-b - sqrt(b^2 - 4*a*c)) / (2*a);

% Display the roots
disp(x1);
disp(x2);
```

## factorial

f = factorial(n) returns the product of all positive integers less than or equal to n, where n is a nonnegative integer value. If n is an array, then f contains the factorial of each value of n. The data type and size of f is the same as that of n.

The factorial of n is commonly written in math notation using the exclamation point character as n!. Note that n! is not a valid MATLAB® syntax for calculating the factorial of n. [^1]

## True/False (Mark T for True and F for False)

## Multiple Choice (Select the best answer)

## Exercises

## Review Questions

## References and Bibliography

- [^1]: [Factorial of input - MATLAB factorial - MathWorks](https://www.mathworks.com/help/matlab/ref/factorial.html)
