---
layout: page
title: "Understanding Python Lambda Functions: A Comprehensive Guide"
description: Learn how to use Python lambda functions with this detailed guide. Discover syntax, examples, and use cases to enhance your programming skills.
keywords: Python lambda functions, lambda function tutorial, Python programming, lambda function examples, Python syntax, functional programming in Python
toc: toc/python-toc.html
course: python
topic: "lambda"
mini_project: false
---

## Python Anonymous (Lambda) Functions

- A lambda function in Python is a small, anonymous function that can be defined without name.
- Lamdba functions are used to write functions consisting of a single statement.
- A lambda function can take any number of arguments, but can only have one expression.
- It is created using the 'lambda' keyword, and it is often used as an argument to a higher-order function (a function that takes another function as an argument).

**Syntax:**

The syntax of a lambda is

```python
lambda arguments:express
```

**Example #1: Add 10 Using Lambda in Python**

Following code is used to write the function to add 10 in given number.

```python
def add_ten(x)
    return x + 10
```

above function can be written by the lamdba function in python.

```python

add_ten = lambda x: x + 10
print(add_ten(5) # 15

```

**Example #2:** Multiply two numbers using lambda

use of lambda function to multiple two numbers

```python
mul = lambda a, b : a * b
print(mul(2,4)) # 8
```

**Example #3: Check Even Number**

```python
is_even = lambda x: x % 2 == 0
print(is_even(6))  # Output: True
```

**Example #4:** Immediately invoked function expression

```python
(lambda x, y : x + y)(6,8) # 14
```

The lambda function above is defined and then immediately called with two arguments (6,8). it retuns the value **14**, which is the sum of the arguments.

**Example #5:**

```python
def multiply(x, y):
    return x * y

# Using lambda function to call multiply
result = (lambda x, y: multiply(x, y))(5, 3)
print(result)  # Output: 15

# Assigning lambda function to a variable
mult = lambda x, y: multiply(x, y)
result = mult(6, 2)
print(result)  # Output: 12
```

**Example #6:**

```python
lambda x, y : x + y

_(6,8) # 14
```

**Note:** In the interactive interpreter, the single underscore**(_)** is bound to the last expression evalued.

**Python Tutorial: How to Use of Lambda function**

{% assign video_type = "short" %}
{% assign video_id = "Z8Zeen4WwJQ" %}

{% include youtube-video.html video_type=video_type video_id=video_id %}

{% assign video_type = "short" %}
{% assign video_id = "N3UAUI6cEVA" %}

{% include youtube-video.html video_type=video_type video_id=video_id %}

---

## Tasks

### Task 1: Add Two Numbers
Create a lambda function that adds two numbers.  

**Input**: `3, 5`  
**Expected Output**: `8`  

---

### Task 2: Multiply two number
Write a lambda function that multiplies two numbers.

**Input:** 4, 6

**Expected Output:** Output: 24

---

### Task 3: Cube of a Number
Create a lambda function to compute the cube of a number.  

**Input**: `3`  
**Expected Output**: `27`  

---

### Task 4: Average of Two Numbers
Create a lambda function to compute the average of two numbers.  

**Input**: `10, 20`  
**Expected Output**: `15.0` 

