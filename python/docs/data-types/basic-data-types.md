---
layout: page
title: Python Basic Data Types
description: Master Python data types with this comprehensive guide. Learn about numeric, string, boolean, and collection data types with examples, exercises, and tasks. Perfect for beginners and professionals to enhance their Python programming skills.
keywords: Python data types, Python numeric types, Python string type, Python boolean type, Python collection types, Python data type examples, Python data type exercises, Python programming for beginners, learn Python data types, Python coding tasks
toc: toc/python.html
---

## Table of Contents

1. [Numeric Types (int, float, complex)](#1-numeric-types-int-float-complex)
2. [Text Type (str)](#2-text-type-str)
3. [Boolean Type (bool)](#3-boolean-type-bool)
   
In Python, data types define the kind of value a variable can hold and the operations that can be performed on it. They act as blueprints, specifying how data is stored and manipulated in your programs.

## 1. **Numeric Types (int, float, complex)**
    - `int`: Stores whole (non-decimal) numbers, like `10`, `-5`, or `9999`.
    - `float`: Represents floating-point numbers with decimals, like `3.14`, `-2.5e2` (scientific notation), or `1.2345678901234567` (limited precision).
    - `complex`: Holds complex numbers with a real and imaginary part, like `3+2j` or `1.5-4.7j`.

- [Example #1: How to use int variable](https://www.youtube.com/watch?v=t1aQ9igm4gY&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=101)
- [Example #2: int variable](https://www.youtube.com/watch?v=Vhrk3vnw-2o&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=112)
- [Example #3: float variable](https://www.youtube.com/watch?v=1PdD1ssbgUo&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=106)

```python
# Integer (int) to store age
age = 25

# Float (float) to store price with decimals
price = 14.99

# Complex number (complex) - not as common in everyday use
complex_num = 3 + 2j  # Imaginary unit represented by j
```

## 2. **Text Type (str)**
    - `str`: Represents textual data enclosed in single or double quotes, such as `"Hello, world!"`, `'This is a string'`, or multi-line strings using triple quotes (''' or """).

```python
# String (str) to store a name
name = "Alice"

# String with a sentence
greeting = "Hello, how are you?"

# Multi-line string using triple quotes
message = """This is a message
that spans multiple lines."""
```

## 3. **Boolean Type (bool)**
    - `bool`: Represents logical values: `True` or `False`. Used for conditional statements and boolean expressions.

```python
# Boolean (bool) for a true/false condition
is_raining = True

# Using booleans in an if statement
if is_raining:
    print("Bring an umbrella!")
```

- [Example #1: Exploring Boolean Values and Type Checking with isinstance() and bool() functions](https://www.youtube.com/watch?v=gR1HrgGHp2Y&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=36)

## **Task 1: Type Checking in Python**  
Write a Python program that:  
- Declares three different types of numbers: an integer, a float, and a complex number.  
- Uses the `type()` function to check the data type of each number.  
- Prints the data type of each number in a descriptive way.  

**Example Output:**  
```
The type of variable x is: <class 'int'>  
The type of variable y is: <class 'float'>  
The type of variable z is: <class 'complex'>  
```
---