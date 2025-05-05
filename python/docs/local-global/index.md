---
layout: page
title: "Local and Global Variables in Python: Explained with Examples and Tasks | Python for Beginners"
description: Learn the difference between local and global variables in Python with simple explanations, practical examples, and beginner-friendly tasks. Understand constants, best practices, and how to manage variables effectively in your programs.
keywords: local variables in Python, global variables in Python, Python constants, Python variable examples, Python beginner tasks, Python global keyword, Python local vs global variables, Python programming basics, how to use variables in Python, Python coding exercises, Python for Beginners, python tutorial for beginners
toc: toc/python-toc.html
course: python
topic: "local-global"
mini_project: false
---

## Local Variables

## What is a Local Variable?

- **Local variables** are variables declared inside a function. They can only be accessed within that function and are **destroyed** when the function completes execution..
- It **only exists** while the function is running.
- You **cannot use** it **outside** the function.

**Characteristics:**
- Created when the function starts
- Only accessible within the function
- Destroyed when the function exits
  
---
## Example:

```python
def greet():
    message = "Hello, world!"  # local variable
    print(message)

greet()

# This will cause an error:
# print(message)
```
> `message` is local to `greet()` and can't be accessed outside.

---
## Key Points:
- Local variables are **created when** the function **starts**.
- They are **destroyed when** the function **ends**.
- They **do not affect** variables outside the function.

---
## Task for Students:

Write a function called `add_numbers` that:
- Takes two numbers as input.
- Adds them together.
- Stores the result in a **local variable**.
- Prints the result.

---
**Example Solution:**
```python
def add_numbers(a, b):
    result = a + b
    print("Sum:", result)

add_numbers(5, 10)
```

---

## Global Variables and Constants

## What is a Global Variable?

- A **global variable** is a variable that is **declared outside all functions** and can be accessed throughout the entire program..
- It **can be used** both **inside** and **outside** functions.

---
## Example:

```python
name = "Ali"  # global variable

def greet():
    print("Hello", name)

greet()
print("Goodbye", name)
```
> `name` is accessible inside and outside the function.

---

## Changing a Global Variable Inside a Function

- If you **want to modify** a global variable **inside a function**, you must use the `global` keyword.

```python
count = 0

def increment():
    global count
    count += 1

increment()
print(count)  # Output: 1
```

> Without `global`, Python would create a **new local variable** named `count`.

**Python Tutorial: Local vs Global Variables in Python**

{% assign video_type = "short" %}
{% assign video_id = "WvAsrn5A2ms" %}

{% include youtube-video.html video_type=video_type video_id=video_id %}

---

## Constants

- A **constant** is a variable that **should not change** once assigned.
- In Python, constants are typically declared as global variables with **ALL_CAPS** names by convention.
- **Python does not force constants**, but developers treat them as unchangeable.

In programming:
- A convention is a common habit or best practice that developers choose to follow to make code more readable and consistent.
- Python itself does not force it, but good programmers still follow it.

---
### Example:

```python
PI = 3.14159  # constant

def area_of_circle(radius):
    return PI * radius * radius

print(area_of_circle(5))
```

---

```python
PI = 3.14159  # This is a constant (by convention)
TAX_RATE = 0.20  # Another constant

def calculate_tax(amount):
    return amount * TAX_RATE

print(calculate_tax(100))  # Output: 20.0
```

## Best Practices:

1. Avoid excessive use of **global variables** as they can make code harder to maintain
2. Use ALL_CAPS for constants to indicate they shouldn't be modified
3. When you must use global variables, declare them clearly at the top of your file
---

## Tasks:

### Task #1: Global Variable Task
- Create a global variable called `language` set to `"Python"`.
- Write a function `show_language()` that prints `"I love Python!"` using the global variable.

### Task #2:
- Define a constant `GRAVITY = 9.8`.
- Write a function `weight_on_earth(mass)` that calculates and returns the weight.

### Task #3:
Create a program with:
1. A global constant DISCOUNT set to 0.10
2. A global variable total_purchases initialized to 0
3. A function make_purchase(amount) that adds to total_purchases and applies the discount
4. A function show_total() that prints the current total