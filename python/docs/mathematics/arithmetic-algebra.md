# Python Programming for Mathematics: Basic Arithmetic and Algebra

Basic arithmetic and algebra are foundational topics in mathematics, encompassing essential operations and rules used in everything from basic calculations to more advanced math. Here’s a detailed breakdown of these concepts in Python.

---

### 1. **Basic Arithmetic Operations**

Arithmetic operations are simple calculations performed on numbers, involving addition, subtraction, multiplication, division, and more. Here’s a look at each operation in Python:

   ```python
   # Arithmetic operations examples
   a = 10
   b = 3

   addition = a + b        # Addition (10 + 3 = 13)
   subtraction = a - b     # Subtraction (10 - 3 = 7)
   multiplication = a * b  # Multiplication (10 * 3 = 30)
   division = a / b        # Division (10 / 3 = 3.333...)
   ```

   - **Addition** (`+`): Combining two numbers.
   - **Subtraction** (`-`): Removing one number from another.
   - **Multiplication** (`*`): Repeated addition, represented as `a * b`.
   - **Division** (`/`): Splitting a number into equal parts.

   **Special Operations**:
   - **Floor Division** (`//`): Divides two numbers and rounds down to the nearest integer.

     ```python
     floor_division = a // b  # Result: 3
     ```

   - **Modulus** (`%`): Finds the remainder after division.

     ```python
     modulus = a % b  # Result: 1 (remainder of 10 divided by 3)
     ```

   - **Exponentiation** (`**`): Raises a number to the power of another.

     ```python
     power = a ** b  # 10 raised to the power of 3 = 1000
     ```

### 2. **Order of Operations (PEMDAS)**

When multiple operations are in an expression, Python follows an order of operations (PEMDAS):
   - **Parentheses** (`()`): Calculations inside parentheses are done first.
   - **Exponentiation** (`**`): Powers are calculated next.
   - **Multiplication and Division** (`*`, `/`, `//`, `%`): Done left to right.
   - **Addition and Subtraction** (`+`, `-`): Done last, left to right.

   ```python
   result = (2 + 3) * 4 ** 2 / 2  # Result: 40.0
   ```

### 3. **Variables in Arithmetic Expressions**

Variables allow storing and reusing values in calculations. They can represent any number, making expressions dynamic.

   ```python
   x = 5
   y = 10

   # Expression using variables
   result = x * y + 2
   ```

   By changing variable values, you can reuse the same expression for different calculations.

### 4. **Algebraic Expressions**

Algebraic expressions involve variables, constants, and arithmetic operations. In programming, they allow representing equations dynamically, enabling us to build mathematical models and solve problems.

   - **Basic Expression**: Combines variables and constants with operators.

     ```python
     a = 5
     b = 3
     result = 2 * a + 3 * b - 4  # Equivalent to 2a + 3b - 4
     ```

   - **Reassignment in Expressions**: Variables can update their values within expressions.

     ```python
     count = 10
     count += 5  # count is now 15
     ```

### 5. **Solving Linear Equations**

Linear equations are algebraic equations where each term is either a constant or the product of a constant and a single variable. They can be solved in Python using expressions and basic algebra.

   - **Single-variable Equations** (e.g., `2x + 3 = 7`):
     
     To solve `2x + 3 = 7` for `x`:

     ```python
     # Rearrange equation to isolate x
     x = (7 - 3) / 2  # Result: x = 2
     ```

   - **Multi-variable Equations**: For systems of linear equations, use libraries like `NumPy` or `SymPy`.

     ```python
     # Using NumPy for solving system of equations
     import numpy as np

     A = np.array([[2, 1], [1, -1]])  # Coefficients matrix
     B = np.array([7, 1])             # Constants matrix

     solution = np.linalg.solve(A, B)  # Solution for x and y
     ```

### 6. **Algebraic Properties**

These properties simplify arithmetic and algebraic expressions.

   - **Commutative Property**: Order does not matter for addition or multiplication.
     
     ```python
     a + b == b + a
     a * b == b * a
     ```

   - **Associative Property**: Grouping does not matter for addition or multiplication.
     
     ```python
     (a + b) + c == a + (b + c)
     (a * b) * c == a * (b * c)
     ```

   - **Distributive Property**: `a * (b + c) == a * b + a * c`
     
     ```python
     a = 2
     b = 3
     c = 4
     distributive_result = a * (b + c) == (a * b) + (a * c)
     ```

### 7. **Inequalities**

Inequalities compare two expressions using `<`, `>`, `<=`, and `>=`. Python evaluates inequalities and returns `True` or `False`.

   ```python
   x = 7
   y = 5

   is_greater = x > y       # True
   is_less_equal = x <= 10  # True
   ```

   **Solving Inequalities**:
   Solving an inequality is similar to solving an equation, but reversing the inequality sign when multiplying/dividing by a negative number.

   ```python
   # For inequality 2x - 3 < 7
   x = (7 + 3) / 2  # x < 5
   ```

### 8. **Working with Expressions and Simplifications**

In Python, the `SymPy` library allows you to symbolically define variables and manipulate algebraic expressions.

   ```python
   from sympy import symbols, expand, simplify

   x, y = symbols('x y')

   # Define an algebraic expression
   expression = (x + y) ** 2

   # Expand and simplify expressions
   expanded = expand(expression)        # x**2 + 2*x*y + y**2
   simplified = simplify(expanded)      # Simplifies if possible
   ```

### Summary Table of Concepts

| Concept                | Example                              | Description                                       |
|------------------------|--------------------------------------|---------------------------------------------------|
| Basic Arithmetic       | `a + b`, `a * b`, `a / b`           | Basic operations like add, subtract, multiply, etc. |
| Order of Operations    | `(2 + 3) * 4 ** 2 / 2`              | PEMDAS order of evaluation                         |
| Variables in Expressions | `result = x + y * 2`              | Combining variables and constants                  |
| Solving Linear Equations | `np.linalg.solve(A, B)`           | Solving linear equations with Python               |
| Algebraic Properties   | `a + b == b + a`                    | Commutative, associative, distributive properties  |
| Inequalities           | `x > y`, `x <= 10`                 | Comparing values and conditions                    |
| SymPy for Expressions  | `expand((x + y) ** 2)`             | Symbolic math operations                           |

---

This guide provides a solid base in arithmetic and algebra with Python, from basic operations to manipulating algebraic expressions. Let me know if you'd like further examples or practice problems on any of these topics!