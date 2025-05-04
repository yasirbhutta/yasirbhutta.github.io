Great! Here's the Find and Fix the Mistakes – Lambda Functions worksheet for beginners, now including:

The mistake code

A brief issue statement

The corrected code


Arranged from easy to hard:


---

Find and Fix the Mistakes – Lambda Functions (Beginner Level)


---

Question 1: Missing Colon

Code with Mistake:

double = lambda x x * 2
print(double(4))

Issue: Missing colon (:) in the lambda definition.

Fixed Code:

double = lambda x: x * 2
print(double(4))


---

Question 2: Missing Argument

Code with Mistake:

add = lambda a, b: a + b
print(add(5))

Issue: The function requires two arguments, but only one is provided.

Fixed Code:

add = lambda a, b: a + b
print(add(5, 3))


---

Question 3: Incorrect Lambda Call

Code with Mistake:

print(lambda x: x + 1(3))

Issue: Missing parentheses around the lambda function to call it.

Fixed Code:

print((lambda x: x + 1)(3))


---

Question 4: Too Many Arguments

Code with Mistake:

is_even = lambda x: x % 2 == 0
print(is_even(4, 2))

Issue: Lambda function expects 1 argument, but 2 are given.

Fixed Code:

is_even = lambda x: x % 2 == 0
print(is_even(4))


---

Question 5: Extra Argument in Call

Code with Mistake:

square = lambda x: x * x
print(square(5, 2))

Issue: Function expects 1 argument, but 2 are passed.

Fixed Code:

square = lambda x: x * x
print(square(5))


---

Question 6: Return Statement in Lambda

Code with Mistake:

add = lambda a, b: return a + b
print(add(3, 4))

Issue: lambda functions cannot use the return statement.

Fixed Code:

add = lambda a, b: a + b
print(add(3, 4))


---

Question 7: Missing Iterable in map()

Code with Mistake:

doubled = map(lambda x: x * 2)
print(list(doubled))

Issue: map() is missing the list to apply the function to.

Fixed Code:

doubled = map(lambda x: x * 2, [1, 2, 3])
print(list(doubled))


---

Question 8: Undefined Variable in If-Else

Code with Mistake:

max = lambda a, b : x if (a > b) else b
print(max(1, 2))

Issue: Uses x which is not defined; should use a.

Fixed Code:

max = lambda a, b: a if a > b else b
print(max(1, 2))


---

Question 9: Invalid If-Else Syntax

Code with Mistake:

max = lambda x, y: if x > y then x else y
print(max(3, 7))

Issue: Incorrect syntax for if-else in lambda expression.

Fixed Code:

max = lambda x, y: x if x > y else y
print(max(3, 7))


---

# Python Custom Modules: Find and Fix Mistakes - Beginner Practice Questions

Here are beginner-friendly practice problems to help identify and correct common mistakes in custom Python modules:

## Basic Module Mistakes

### Question 1: Missing Function Definition
```python
# greetings.py
def greet(name
    print(f"Hello, {name}!")

# main.py
import greetings

greetings.greet("Alice")
```

**Mistakes to find:**
1. Missing closing parenthesis in function definition
2. Missing colon at end of function definition line
3. (Bonus) No docstring for the function

### Question 2: Incorrect Import
```python
# math_operations.py
def add(a, b):
    """Add two numbers"""
    return a + b

# main.py
from math_operations import Add

result = Add(5, 3)
```

**Mistakes to find:**
1. Case mismatch in import statement
2. Case mismatch when calling the function

### Question 3: Module Name Conflict
```python
# random.py
def choice(items):
    return items[0]

# main.py
import random

print(random.choice(["apple", "banana"]))
```

**Mistakes to find:**
1. Naming conflict with Python's built-in `random` module
2. Poor implementation of choice function

## Function Organization

### Question 4: Poor Module Organization
```python
# utilities.py
def calculate_area(radius):
    return 3.14 * radius * radius

def calculate_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def reverse_string(s):
    return s[::-1]
```

**Mistakes to find:**
1. No logical grouping of related functions
2. Magic number (3.14) instead of using math.pi
3. No module-level docstring

### Question 5: Duplicate Code
```python
# shapes.py
def circle_area(radius):
    return 3.14 * radius * radius

def cylinder_volume(radius, height):
    return 3.14 * radius * radius * height
```

**Mistakes to find:**
1. Duplicate calculation logic
2. Magic number repeated
3. No reuse of circle_area in cylinder_volume

## Import Issues

### Question 6: Incorrect Relative Import
```python
# package/module1.py
def func1():
    print("Function 1")

# package/module2.py
from module1 import func1

func1()
```

**Mistakes to find:**
1. Incorrect relative import (should use dot notation)
2. Will fail if run from different directory

### Question 7: Unused Import
```python
# calculations.py
import math
import sys

def circle_area(radius):
    return math.pi * radius ** 2
```

**Mistakes to find:**
1. Unused import (sys)
2. No error handling for negative radius

## Solutions

### Solution 1:
```python
# greetings.py
def greet(name):
    """Print a greeting message"""
    print(f"Hello, {name}!")

# main.py remains the same
```

### Solution 2:
```python
# math_operations.py remains the same

# main.py
from math_operations import add  # lowercase 'add'

result = add(5, 3)  # lowercase 'add'
```

### Solution 3:
```python
# my_random.py  # Changed filename
def choice(items):
    """Return first item from list"""
    return items[0]

# main.py
import my_random  # Use the new module name

print(my_random.choice(["apple", "banana"]))
```

### Solution 4:
```python
# utilities.py
"""Collection of utility functions grouped by category"""

import math

# Math utilities
def calculate_area(radius):
    """Calculate area of a circle"""
    return math.pi * radius * radius

def calculate_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

# String utilities
def reverse_string(s):
    """Reverse a string"""
    return s[::-1]
```

### Solution 5:
```python
# shapes.py
import math

def circle_area(radius):
    """Calculate area of a circle"""
    return math.pi * radius * radius

def cylinder_volume(radius, height):
    """Calculate volume of a cylinder"""
    return circle_area(radius) * height  # Reuse circle_area
```

### Solution 6:
```python
# package/module1.py remains the same

# package/module2.py
from .module1 import func1  # Added dot for relative import

func1()
```

### Solution 7:
```python
# calculations.py
import math

def circle_area(radius):
    """Calculate area of a circle with error checking"""
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2
```

## Additional Practice Exercises

1. **Fix the Module Docstring**:
```python
# stats.py
calculate_average(numbers):
    return sum(numbers) / len(numbers)
```
- Add missing function keyword (`def`)
- Add module docstring
- Add function docstring
- Add error handling for empty list

2. **Organize Related Functions**:
```python
# colors.py
hex_to_rgb(hex):
    # conversion code

darken(color, percent):
    # color manipulation code

rgb_to_hex(r, g, b):
    # conversion code
```
- Group conversion functions together
- Add proper docstrings
- Add parameter validation

3. **Fix Import Statements**:
```python
# project/utils/helpers.py
def validate_email(email):
    # validation code

# project/tests/test_helpers.py
from helpers import validate_email
```
- Correct the import path
- Add `__init__.py` files if needed
- Consider absolute vs relative imports

These exercises will help beginners understand common pitfalls when creating and using custom modules in Python.

