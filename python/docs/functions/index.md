---
layout: page
title: "Functions in Python: Complete Guide with Syntax, Examples, and Practice Tasks" 
description: Master functions in Python with this beginner-friendly guide. Learn how to define functions, use return statements, default and keyword arguments, and solve practical coding tasks with real-world examples.  
keywords: Functions in Python, Python function examples, how to define a function in Python, Python return statement, Python default arguments, Python keyword arguments, Python function tasks, Python beginner exercises, learn Python functions, Python programming basics
author: Muhammad Yasir Bhutta
course: python
topic: functions
show_toc: true
toc: toc/python.html
show_practice_progress: true
show_mini_project: null
prev: /python/docs/list-comprehension/
next: /python/docs/functions/#return-statement
breadcrumb:
  - title: Home
    url: /
  - title: Python
    url: /Python/
  - title: Functions
    url: /python/functions
---

## Table of Contents

1. [What is a Function?](#1-what-is-a-function)
2. [How to Write a Function](#2-how-to-write-a-function)
3. [Return Statement](#3-return-statement)
4. [Default Arguments](#4-default-arguments)
5. [Keyword Arguments](#5-keyword-arguments)
6. [Tasks](#6-tasks)

---

## 1. What is a Function?

 A function is a block of reusable code that performs a specific task. It's reusable, which means you can call it multiple times in your program. This helps to organize your code, make it more readable, and avoid repetition.

**Why Do We Use Functions?**

We use functions in Python for several reasons:

- **Code Reusability:** You can call a function multiple times instead of repeating code. This saves time and effort.
- **Modularity:** Breaking down a large program into smaller, manageable chunks (functions) makes it easier to understand and maintain.
- **Avoiding Repetition:** Functions prevent you from writing the same code over and over, reducing errors and improving efficiency."

## 2. How to Write a Function

To define a function, you use the `def` keyword followed by the function name, parentheses for parameters, and a colon. The code block that defines the function is indented.

**Syntax:** 

```python
def function_name(parameters):
  # Function body
  # Code to be executed
```

### Example 1: Defining and Calling a Function

```python
def greet(name):
  print("Hello,", name + "!")

# Calling the function
greet("Ahmad")  # Output: Hello, Ahmad!
```

**Explanation:**

- `def greet(name):` defines a function named `greet` that takes one parameter, `name`.
- `print("Hello,", name + "!")` is the function body, which prints a greeting message using the provided name.
- `greet("Ahmad")` calls the function with the argument "Ahmad".

**Key Points:**

- **Parameters:** These are variables passed to the function when it's called. For more details, See [Parameters and Arguments in Python Functions](parameters-arguments.md)
- **Return Value:** A function can optionally return a value using the `return` statement.
- **Docstrings:** It's good practice to include a docstring (a string that explains the function's purpose) after the function definition.

## 3. Return Statement

   - Functions can return values using the `return` keyword.

### Example 2: Function with a Return Value

```python
def add(x, y):
  return x + y

result = add(3, 5)
print(result)  # Output: 8
```

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1602443888929206"
     crossorigin="anonymous"></script>
<ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-1602443888929206"
     data-ad-slot="6296238623"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>


## 4. Default Arguments

   - You can assign default values to parameters, which makes them optional when calling the function.

[Video: Learn How to Use Default Parameters in Function Definition](https://www.youtube.com/watch?v=2z_K1YChX1A&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=21)
  
### Example 6.3:

   ```python
   def greet(name, message="Hello"):
       print(f"{message}, {name}!")

   greet("Alice")           # Uses default message "Hello"
   greet("Alice", "Hi")      # Overrides default with "Hi"
   ```

## 5. Keyword Arguments
  
  - Python allows you to specify arguments by name, making your code more readable.

### Example 6.4: 

   ```python
   def multiply(a, b):
       return a * b

   result = multiply(b=3, a=5)  # You can specify arguments in any order
   ```
---

## 6. Tasks

### Task 6.1: Create a Function to Calculate the Area of a Rectangle

**Function Requirements:**
1. Define a function named `calculate_area` that takes two parameters: `length` and `width`.
2. The function should calculate the area of the rectangle (Area = Length × Width) and return the result.

**Input:**
- Length (a positive float or integer)
- Width (a positive float or integer)

**Output:**
- The area of the rectangle (a float)

**Expected Output**
```
The area of the rectangle with length 5 and width 3 is: 15
```

**Additional Test Cases**

1. **Input:** `length = 7`, `width = 2`
   - **Output:** `The area of the rectangle with length 7 and width 2 is: 14`

2. **Input:** `length = 10.5`, `width = 4.2`
   - **Output:** `The area of the rectangle with length 10.5 and width 4.2 is: 44.1`

### Task 6.2: Create a Function to Check if a Number is Even or Odd

**Function Requirements:**
1. Define a function named `is_even` that takes one parameter: `number`.
2. The function should determine if the number is even or odd.
3. It should return the string `"Even"` if the number is even, and `"Odd"` if the number is odd.

**Input:**
- A single integer (positive or negative)

**Output:**
- A string: either `"Even"` or `"Odd"`

**Expected Output**
```
The number 4 is: Even
```

### Additional Test Cases

Encourage beginners to test the function with various numbers:

1. **Input:** `num = 7`
   - **Output:** `The number 7 is: Odd`

2. **Input:** `num = -2`
   - **Output:** `The number -2 is: Even`

3. **Input:** `num = 0`
   - **Output:** `The number 0 is: Even`

### Task 6.3: Basic Default Argument Task

   - **Task:** Write a function `greet` that takes a name as an argument and a greeting message with a default value of "Hello". If no greeting is provided, the function should use "Hello."
   - **Example:** `greet("Alice")` should output `"Hello, Alice!"` and `greet("Alice", "Good morning")` should output `"Good morning, Alice!"`

### Task 4: Create a Function with Multiple Defaults and Modify One

   - **Task:** Write a function `calc_price` that accepts `price`, `tax=0.05`, and `discount=0`. Calculate the final price after applying tax and discount. Test with various keyword arguments to see how changes affect the result.
   - 
   - **Example:** `calc_price(100)`, `calc_price(100, discount=0.1)`, `calc_price(100, tax=0.07, discount=0.1)`

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1602443888929206"
     crossorigin="anonymous"></script>
<ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-1602443888929206"
     data-ad-slot="6296238623"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

[video: Guard Statements in Python: Explained Simply](https://youtu.be/rzY31wSKvXc)

[Python Quiz - Functions](https://forms.gle/ZxyA5p98T9f8CZsA6)

## Task 5: Fix the Errors

1. **Fixing Errors in Function Calls and Assignments** 
   
```python
def greet():
    print("Hello World!")

greeting = greet
```

2. **Which of the following will cause a syntax error due to incorrect indentation in Python?**

A)
```python
print("Hello World!")
```

B)
```python
def my_function():
print("Hello World!")
```

C)
```python
if x == 10:
    print("x is 10")
```

D)
```python
x = 10
```

*Answer:* B


