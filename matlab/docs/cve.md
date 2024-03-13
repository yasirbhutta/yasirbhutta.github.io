# MATLAB for Beginners - Constants, Variables and Expressions

Connect with me: [Youtube](https://www.youtube.com/yasirbhutta) \| [LinkedIn](https://www.linkedin.com/in/yasirbhutta/) \| [WhatsApp Channel](https://whatsapp.com/channel/0029VaC3BC160eBZZSs3CW0c) \| [Web](https://yasirbhutta.github.io/) \| [Facebook](https://www.facebook.com/yasirbhutta786) \| [Twitter](https://twitter.com/yasirbhutta)

## Data Types in MATLAB

In MATLAB, data types define the kind of information a variable can store and the operations allowed on them. Choosing the correct data type is crucial for optimizing memory usage, calculation accuracy, and code efficiency. Here's a breakdown of the various data types available:

**1. Numeric Data Types:**
- **Double-precision floating-point (default):**
  - **Representation:** Uses 64 bits for storage, offering a balance between precision and memory usage.
  - **Type:** double
  - **Range:** Approximately `-1.7e+308` to `1.7e+308`.
  - **Precision:** Generally provides 15-16 decimal digits of precision.
  - **Applications:** Suitable for most general-purpose calculations due to its balanced characteristics.
- **Single-precision floating-point:**
  - **Representation:** Uses 32 bits for storage, offering faster calculations and less memory usage compared to double-precision.
  - **Type:** single
  - **Range:** Approximately `-3.4e+38` to `3.4e+38`.
    - **Precision:** Provides 6-7 decimal digits of precision.
    - **Applications:** Suitable when memory efficiency is a concern, and required precision is not as high as double-precision.
- **Integer data types:**
  - **Storage:** Use a specific number of bits to store whole numbers (integers) without decimal points, offering efficient memory usage and speed for integer operations.
    - **Types:**
      - `int8`: Signed, 8-bit integer (-128 to 127)
      - `uint8`: Unsigned, 8-bit integer (0 to 255)
      - `int16`: Signed, 16-bit integer (-32768 to 32767)
      - `uint16`: Unsigned, 16-bit integer (0 to 65535)
      - `int32`: Signed, 32-bit integer (-2147483648 to 2147483647)
      - `uint32`: Unsigned, 32-bit integer (0 to 4294967295)
  - **Applications:** For representing and manipulating whole numbers, particularly when memory or speed is critical.
- **Complex numbers:**
  - **Representation:** Combine real and imaginary parts, using double-precision floating-point elements for storage.
  - **Applications:** Used in calculations involving complex mathematical concepts like electrical engineering, signal processing, and wave mechanics.

**2. Character and String Data Types:**
- **Character:**
  - Type: char
  - A character array is a sequence of individual characters stored one after another in memory. Each character takes 2 bytes of storage, typically representing a single letter, number, or symbol.
  - **Use Cases:**
    - Used for storing short pieces of text where individual characters matter, such as filenames, captions, or labels.
    - Useful for manipulating individual characters within the array using indexing and string functions.
  - **String:**
    - Type: string
    - A string array is a container that holds text data with additional features and functionalities. Internally, it uses a more complex structure than char arrays, leading to a slightly larger memory footprint.
    - Used for storing and manipulating textual data like words, sentences, or paragraphs. 
    - **Use Cases:**
      - Used for storing text data in a more versatile way.
      - Offers built-in functions for various string operations like concatenation, searching, and comparison.
      - Can hold text of any length without requiring padding or pre-allocation.

**Example #:** Creating char and string

```matlab
% char array
myChar = 'Hello';

% string
myString = "Hello World!";
```

**Example #:** Accessing elements

```matlab
% Accessing first character of char array (individual character)
firstChar = myChar(1);
```
**3. Logical Data Type:**
- Represents logical values, either `true` or `false`.
- Used for conditional statements and Boolean operations.

**Choosing the Right Data Type:**

Consider these factors when selecting a data type:

- **Range of values:** Choose a type that can accommodate the minimum and maximum values you need.
- **Required precision:** Select a type with sufficient precision to handle the level of accuracy needed.
- **Memory constraints:** If memory is limited, consider using efficient data types like integers when appropriate.
- **Functionality:** Choose the type that best suits the intended operations you'll perform on the data.

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

This function allows you to check if a variable belongs to a specific data type. It returns `1` if the variable is of the specified type and `0` otherwise.

```matlab
number = 10;
is_integer = isa(number, 'double');
disp(is_integer); % Output: 1
```

**4. Built-in functions for specific types:**

Certain data types have dedicated functions that return information about them. For example, `ischar` checks for characters, `isfloat` checks for floating-point numbers, and `islogical` checks for logical values.

```matlab
myChar = 'This is a string';
is_char = ischar(myChar);
disp(is_char); % Output: 1
```

**Choosing the best method:**

- **`class` function** is the simplest and most versatile option for quickly determining the data type of a variable.
- **`whos` command** is useful when you need to see a complete list of variables and their attributes, not just the data type.
- **`isa` function** is beneficial for checking if a variable belongs to a specific type, often used in conditional statements.
- **Specific type functions** are helpful when working with particular data types and need additional information beyond just the basic class.

Remember, choosing the appropriate method depends on your specific needs and the context of your code.

## Type Conversion

Some common MATLAB functions used to change data types:

**1. `cast`:** This is the most versatile function for converting data between various numeric types. It takes two arguments:

- **The data to be converted:** This can be any variable or expression that evaluates to a numerical value.
- **The desired data type:** Specify the new data type using a string like 'double', 'int32', 'single', etc.

```matlab
% Convert a double to an integer
convertedInt = cast(12.34, 'int32');

% Convert a string to a double
convertedDouble = cast('3.14', 'double');
```

**Additional points:**

- These functions might not always be successful, especially when converting between incompatible data types. 
- Always check the documentation for each function to understand its limitations and potential errors.
- Consider using `is*` functions like `isnumeric` or `ischar` to check the data type before conversion to avoid errors.

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

**Example #2.1 from book** [2]
**Example #2.2 from book** [2]
**Example #2.3 from book** [2]

### Relational Operators in MATLAB

In MATLAB, relational operators help you compare values and create logical expressions that evaluate to either `true` (1) or `false` (0). These logical expressions are crucial for making decisions and controlling program flow in your code.

Here's a table summarizing the most common relational operators:

| Operator | Description | Example |
|---|---|---|
| `==` | Equal to | `a == 5` checks if `a` is equal to 5 |
| `~=` | Not equal to | `b ~= 3` checks if `b` is not equal to 3 |
| `<` | Less than | `c < 10` checks if `c` is less than 10 |
| `>` | Greater than | `d > 2` checks if `d` is greater than 2 |
| `<=` | Less than or equal to | `e <= 0` checks if `e` is less than or equal to 0 |
| `>=` | Greater than or equal to | `f >= 7.5` checks if `f` is greater than or equal to 7.5 |

**Using Relational Operators in Expressions**

You can combine relational operators with numerical values and variables to create logical expressions. Here are some examples:

```matlab
age = 20;
isAdult = age >= 18;  % Checks if age is 18 or older (true)

grade = 85;
passedExam = grade > 70;  % Checks if grade is greater than 70 (true)

accountBalance = 100;
needsRefill = accountBalance < 50;  % Checks if balance is below 50 (false)
```

**Example:**String Comparisons
```matlab
name = "Ali";
isFirstName = name == "Ali";  % Checks if name is exactly "Alice" (true)

fruit = "apple";
isFavorite = fruit ~= "banana";  % Checks if fruit is not "banana" (true)
```
**Important:** String comparisons in MATLAB are case-sensitive. "Ali" is not the same as "ali".

**Logical Operators (and, or, not)**

MATLAB provides additional operators to combine logical expressions:

* `&` (AND): Both conditions must be true for the overall expression to be true.
* `|` (OR): At least one condition must be true for the overall expression to be true.
* `~` (NOT): Inverts the truth value of the expression.

Here's an example:

```matlab
temperature = 30;
isHot = temperature > 25;
isSunny = true;

goSwimming = isHot & isSunny;  % Only true if both hot and sunny (false)

goForWalk = isHot | ~isSunny;  % True if hot or not sunny (true)
```

**Example :** Combining Relational Operators
```matlab
age = 16;
isTeenager = age >= 13 & age <= 19;  % Checks if age is between 13 and 19 (true)

accountBalance = 40;
needsRefill = accountBalance < 50 | ~isAdult;  % Needs refill if below 50 OR not adult (true)
```

**Applications of Relational Operators**

Relational operators are fundamental for various tasks in MATLAB:

* **Conditional Statements:** Use `if`, `else if`, and `end` statements with logical expressions to control program flow based on conditions.
* **Loops:** Utilize `while` and `for` loops with logical expressions to repeat code as long as a condition remains true.
* **Data Filtering:** Employ logical expressions to select specific data points from matrices or arrays that meet certain criteria.

**Remember:**

* Always enclose variable names and numerical values in single quotes when using them in strings. 
* Use parentheses to group complex logical expressions for proper evaluation.


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
disp(circumference)
```

In this example, we define the width and height of the rectangle as `w=5` and `h=10`, respectively. Then, we use the formula for the circumference of a rectangle, which is `2 * (width + height)`, to calculate the circumference. Finally, we use the `disp` function to display the result, which is the circumference of the rectangle with two decimal places. 

You can adjust the values of `w` and `h` to calculate the circumference of a rectangle with different dimensions.

### Example: Calculate the area of the triangle

```matlab
% Define the base and height of the triangle
b = 6;
h = 4;

% Calculate the area of the triangle
area = 0.5 * b * h;

% Display the result
disp(area)
```

In this example, we define the base and height of the triangle as `b=6` and `h=4`, respectively. Then, we use the formula for the area of a triangle, which is `0.5 * base * height`, to calculate the area. Finally, we use the `disp` function to display the result, which is the area of the triangle with two decimal places.

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

Finally, we use the `disp` function to display the result, which is the semiperimeter of the spherical triangle with two decimal places.

You can adjust the values of `a`, `b`, and `c` to calculate the semiperimeter of a different spherical triangle.

## BUILT-IN FUNCTIONS

- In MATLAB, a built-in function is a pre-written piece of code that's included as part of the software itself. 
- These functions perform various tasks and are essential for mathematical computations, data analysis, visualization, and more.

Key points about built-in functions:

- **Part of MATLAB executable:** Built-in functions are compiled directly into MATLAB and run very efficiently. You can't access or modify their source code.
- **Wide range of functionality:** MATLAB offers a vast collection of built-in functions covering areas like:
  - Mathematical operations (e.g., sine, cosine, addition, multiplication)
  - Matrix manipulation (e.g., creating matrices, finding eigenvalues)
  - Data analysis (e.g., sorting, filtering, statistics)
  - Plotting and visualization (e.g., creating graphs, charts)
  - File I/O (reading and writing data)
- **Using built-in functions:**  Just type the function name followed by parentheses in the MATLAB command window. You can provide input arguments within the parentheses, and the function will perform the operation and return output.

For instance, the `sin(pi/2)` function calculates the sine of pi/2 and returns the value (which is 1).

**Finding out if a function is built-in:**

- Use the `which` command followed by the function name. If it's built-in, it will return the location within MATLAB where the function is stored.
- Even though you can't see the source code, MATLAB provides extensive documentation for built-in functions. This documentation explains what the function does, how to use it with different arguments, and what outputs it produces. You can access this documentation directly from the command window using the `help` command followed by the function name (e.g., `help sin`).

**Example 2.4:** from book

**Example:** Calculate the area of a triangle using Heron's formula:

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
disp(A)
```

In this example, we define the lengths of the sides of the triangle as `a=5`, `b=6`, and `c=7`. Then, we use the semiperimeter formula, which is `s = (a + b + c)/2`, to calculate the semiperimeter of the triangle. Finally, we use Heron's formula, which is `A = sqrt(s * (s - a) * (s - b) * (s - c))`, to calculate the area of the triangle.

The `sqrt` function is the square root function in MATLAB. The `disp` function is used to display the result, which is the area of the triangle with two decimal places.

You can adjust the values of `a`, `b`, and `c` to calculate the area of a different triangle using Heron's formula.

**Example:** Finding the Roots of a Quadratic Equation

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

## pi (π) 

Absolutely, pi (π) is a well-known mathematical constant that represents the ratio of a circle's circumference to its diameter. It's an irrational number, meaning it cannot be expressed as a simple fraction and its decimal representation never repeats or terminates.

In MATLAB, pi is represented by the built-in constant `pi`. You can directly use it in your calculations:

```matlab
result = pi;
disp(result);  % This will display 3.1416
```

Here are some examples of how `pi` can be used in MATLAB:

* Calculate the area of a circle:

```matlab
radius = 5;
area = pi * radius^2;
disp(area);  % This will display the area of the circle
```

* Calculate the circumference of a circle:

```matlab
radius = 5;
circumference = 2 * pi * radius;
disp(circumference);  % This will display the circumference of the circle
```

## log10 

In MATLAB, you can compute the base-10 logarithm (common logarithm) using the built-in function `log10`. Here's how:

**Syntax:**

```matlab
Y = log10(X)
```

**Explanation:**

* `Y`: This represents the output variable that will store the base-10 logarithm of the elements in `X`.
* `X`: This can be a numeric variable, a vector, a matrix, or even a symbolic expression. `log10` operates element-wise on the elements of `X`.

**Examples:**

1. Calculate the base-10 logarithm of 100:

```matlab
result = log10(100);
disp(result);  % This will display 2
```

* MATLAB also provides functions for calculating logarithms with other bases like `log2` (base-2 logarithm) and `log` (natural logarithm, base-e).

**See also:**
- MATLAB documentation for `log10` for more details and specific examples: [https://www.mathworks.com/help/matlab/ref/log10.html](https://www.mathworks.com/help/matlab/ref/log10.html)


## exp

The `exp` function in MATLAB is used to calculate the exponential of a number. An exponential term refers to a value raised to a power, where the base is Euler's number "e" (approximately 2.71828).

Here's how `exp` works in MATLAB:

**Syntax:**

```matlab
Y = exp(X)
```

**Explanation:**

* `Y`: This represents the output variable that will store the exponential result.
* `X`: This can be a numeric variable, a vector, a matrix, or even a symbolic expression. `exp` operates element-wise on the elements of `X`.

**What it Does:**

* `exp(X)` calculates the base-e exponential (e raised to the power of X) for each element in `X`.

**Examples:**

1. Calculate the exponential of 2:

```matlab
result = exp(2);
disp(result);  % This will display approximately 7.3891
```

**See also:**
- MATLAB documentation for `exp` for more details and specific examples: [https://www.mathworks.com/help/matlab/ref/exp.html](https://www.mathworks.com/help/matlab/ref/exp.html)

## Key Terms

## True/False (Mark T for True and F for False)

1. The isa function is a reliable way to check if a variable belongs to a specific data type.
2. Using appropriate data types in your code can improve memory usage and code efficiency.\
3. The exponentiation operator in MATLAB is represented by the `**`.

**Answer Key (True/False):**

1. True
2. True
3. False

## Multiple Choice (Select the best answer)

> Which data type is best suited for storing precise scientific calculations that require a wide range of values?
1. char
2. int8
3. double
4. string

> What is the output of the following code: cast('100', 'uint8')?
1. 100
2. '100'
3. Error
4. 100.0

> What is the advantage of using string data types compared to character arrays for storing text data?

1. Strings can only store a fixed length of text.
2. Strings offer built-in functions for various string operations. (Correct Answer)
3. Strings require less memory than character arrays.
4. There's no significant difference for short text data.

> When working with memory limitations and calculations involving whole numbers, what data type is a good choice?
1. single
2. uint16 (Correct Answer)
3. string
4. complex

> What is the output of 5 / 2?
1. 2.5
2. 2 (integer division)
3. Error (division by zero)
4. Depends on variable types

> What data type is used to represent complex numbers in MATLAB?
1. Integers
2. Doubles
3. Characters
4. Complex

> Which data type in MATLAB is used to represent true or false values?
1. Logical
2. Boolean
3. Binary
4. Bitwise
   
> What function is used to determine the data type of a variable in MATLAB?
1. typeOf
2. typeof
3. class
4. dtype

> How do you calculate the remainder of a division in MATLAB?
1. /
2. mod
3. rem
4. floor

> Which operator raises a number to a power?
1. *
2. ^
3. .
4. floor

> What is the output of -3 ^ 2?
1. -9
2. 9
3. Error (negative base)
4. Depends on variable types

> Which relational operator returns TRUE if the operands are equal?
1. `>` (greater than)
2. `<` (less than)
3. `==` (equal to)
4. `!=` (not equal to)

> What is the output of the following code? 5 ~= 7
1. 0
2. 1
3. Error
4. Depends on variable values

## Fill in the Blanks

1. The whos command displays a list of all currently defined variables in your workspace, including their name, size, and __________.
2. Logical data types in MATLAB can hold two values: _________ and __________.
3. In MATLAB, the maximum value that can be represented by the uint8 data type is ___________..
4. The maximum value that can be represented by the int16 data type in MATLAB is ___________.

**Answer Key (Fill in the Blanks):**

1. Class (data type)
2. true (1) , false (0)
3. 255
4. 32767

## Exercises

## Review Questions

## References and Bibliography

[1] Raj Kumar Bansal, A. K. Goel, and Manoj Kumar Sharma, MATLAB and its applications in engineering : [based iôn MATLAB 7.5 (R2007b)]. Delhi: Pearson, 2012.
- [^1]: [Factorial of input - MATLAB factorial - MathWorks](https://www.mathworks.com/help/matlab/ref/factorial.html)
