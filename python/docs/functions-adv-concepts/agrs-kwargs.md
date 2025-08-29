---
layout: page
title: "*args and **kwargs in Python – Beginner’s Guide with Examples and Coding Tasks" 
description: Master the use of *args and **kwargs in Python functions with this beginner-friendly guide. Learn how to handle arbitrary positional and keyword arguments, combine them, and apply unpacking with practical examples and coding exercises. Perfect for students and new Python programmers.  
keywords: Python *args, Python **kwargs, Python function arguments, arbitrary arguments Python, Python function examples, Python unpacking, beginner Python functions, Python coding tasks, learn Python functions, Python programming
course: python
topic: args-kwargs
show_toc: true
toc: toc/python.html
show_practice_progress: null
show_mini_project: null
prev: /python/docs/local-global/
next: /python/docs/lambda/
breadcrumb:
  - title: Home
    url: /
  - title: Python
    url: /Python/
  - title: Functions
    url: /python/docs/functions
---

## Table of Contents

1. [Arbitrary Positional Arguments (`*args`)](#1-arbitrary-positional-arguments-args)
2. [Arbitrary Keyword Arguments (`**kwargs`)](#2-arbitrary-keyword-arguments-kwargs)
3. [Combined Use of `*args` and `**kwargs`](#3-combined-use-of-args-and-kwargs)
4. [Tasks](#4-tasks)

---

## 1. Arbitrary Positional Arguments (`*args`)
   
These allow a function to take any number of positional arguments. Inside the function, `*args` collects all the positional arguments as a tuple.

- [Video: How to Use *args in Python Functions](../../videos/arg-python-video.md)
- [Video: Understanding *args in Functions - How to Add Any Number of Arguments with *args](../../videos/arg-python-example-video.md)

**Example:**
```python
def greet(*names):
    for name in names:
        print(f"Hello, {name}!")

greet("Ali", "Hamza", "Ahmad")
```
**Output:**
```
Hello, Ali!
Hello, Hamza!
Hello, Ahmad!
```

In this example, the `greet` function can take any number of names. The `*names` collects them into a tuple (`names`), which can be iterated over.

## 2. Arbitrary Keyword Arguments (`**kwargs`)

These allow a function to accept any number of keyword arguments (arguments passed as key-value pairs). Inside the function, `**kwargs` collects these as a dictionary.

- [Video: How to use **kwargs in Python](https://www.youtube.com/watch?v=_NMaZ9EO0zI&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=2)

**Example:**
```python
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Ali", age=25, city="Multan")
```
**Output:**
```
name: Ali
age: 25
city: Multan
```

In this case, the function accepts any number of keyword arguments and collects them into a dictionary (`info`), which you can then work with inside the function.

## 3. Combined Use of `*args` and `**kwargs`

You can also use both `*args` and `**kwargs` in the same function to handle a combination of positional and keyword arguments.

**Example:**
```python
def display_data(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

display_data(1, 2, 3, name="Ali", age=25)
```
**Output:**
```
Positional arguments: (1, 2, 3)
Keyword arguments: {'name': 'Ali', 'age': 25}
```

**Key Points:**
- `*args` collects all positional arguments into a tuple.
- `**kwargs` collects all keyword arguments into a dictionary.
- You can use both `*args` and `**kwargs` together to handle any type of arguments passed to a function.

Based on the \*args and \*\*kwargs overview from the page you shared, here are **beginner-friendly coding tasks** to help solidify understanding of these concepts:

---

## 4. Tasks

### 4.1 **Sum Any Numbers**

* **Objective**: Create `sum_all(*nums)` that returns the sum of any passed numbers.
* **Example**:

  ```python
  def sum_all(*nums):
      return sum(nums)

  print(sum_all(1, 2, 3, 4))  # Should print 10
  ```

---

### 4.2 **Keyword Profile Constructor**

* **Objective**: Make `construct_profile(**kwargs)` that returns a user info dictionary.
* **Example**:

  ```python
  def construct_profile(**kwargs):
      return kwargs

  profile = construct_profile(name="Ayesha", age=30, profession="Engineer")
  print(profile)
  ```

---

### 4.3 **Mixed Arguments Logger**

* **Objective**: Define `log(*args, **kwargs)` that prints each positional argument and each key-value pair on separate lines.
* **Example**:

  ```python
  def log(*args, **kwargs):
      for a in args:
          print(f"ARG: {a}")
      for k, v in kwargs.items():
          print(f"KWARG: {k} = {v}")

  log(10, 20, user="Ali", status="active")
  ```

---

### 4.5 **Unpacking with `*` and `**`**

* **Objective**: Practice unpacking lists and dictionaries into function calls.
* **Example**:

  ```python
  def multiply(a, b, c):
      print(a * b * c)

  nums = [2, 3, 4]
  multiply(*nums)  # Unpacks to multiply(2,3,4)

  def print_person(name, age, city):
      print(f"{name}, {age}, from {city}")

  info = {"name": "Sara", "age": 28, "city": "Lahore"}
  print_person(**info)
  ```

---

## 🧠 Practice & Progress

- [📝 Multiple-Choice Questions (MCQs)](practice-and-progress/mcqs-args-kwargs.md)
