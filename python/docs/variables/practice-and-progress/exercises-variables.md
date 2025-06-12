---
layout: page
title: "Python Coding Exercises: Variables, Naming Rules, Dynamic Typing & None"
description: Practice Python with hands-on coding exercises for beginners. Master variables, naming conventions, dynamic typing, and the None constant with real-world examples and challenges.
keywords: python coding exercises, Python variable exercises, Python naming rules, dynamic typing in Python, Python None constant, beginner Python practice, learn Python through exercises
author: Muhammad Yasir Bhutta
course: python
topic: variables
show_toc: false
toc: toc/python.html
show_practice_progress: false
show_mini_project: false
prev: /python/docs/variables/practice-and-progress/fill-blanks-variables.html
next: /python/docs/variables/practice-and-progress/mcqs-variables.html
breadcrumb:
  - title: Home
    url: /
  - title: Python
    url: /python/
  - title: Basics
    url: /python/docs/basics/
  - title: Variables
    url: /python/docs/variables/
---

{% assign topic = "variables" %}
{% assign topics = site.data.python.coding-exercises.topics %}
{% assign selected_topic = topics | where: "topic", topic | first %}
{% assign exercises = selected_topic.exercises %}
{% include pap/coding-exercises-loop.html exercises=exercises topic=topic %}

## Exercises

### Exercise 1: Basic Variable Assignment

1. Create a variable called `name` and assign your name to it.
2. Create a variable called `age` and assign your age to it.
3. Create a variable called `city` and assign the city you live in to it.
4. Print all three variables.

### Exercise 2: Variable Reassignment

1. Create a variable called `favorite_color` and assign your favorite color to it.
2. Print the value of `favorite_color`.
3. Reassign a new color to `favorite_color`.
4. Print the new value of `favorite_color`.

### Exercise 3: Variable Operations

1. Create two variables called `a` and `b` and assign them the values 5 and 10, respectively.
2. Create a new variable called `sum` and assign it the value of `a` plus `b`.
3. Create a new variable called `difference` and assign it the value of `a` minus `b`.
4. Create a new variable called `product` and assign it the value of `a` times `b`.
5. Print the values of `sum`, `difference`, and `product`.

### Exercise 4: String Concatenation

1. Create a variable called `first_name` and assign your first name to it.
2. Create a variable called `last_name` and assign your last name to it.
3. Create a new variable called `full_name` and assign it the value of `first_name` concatenated with `last_name` (with a space in between).
4. Print the value of `full_name`.

**Example Solution:**
```python
first_name = "Alice"
last_name = "Johnson"

full_name = first_name + " " + last_name
print(full_name)
```

### Exercise 5: Input and Variables

1. Use the `input()` function to get the user's name and store it in a variable called `user_name`.
2. Use the `input()` function to get the user's age and store it in a variable called `user_age`.
3. Print a message saying "Hello [user_name], you are [user_age] years old."

**Example Solution:**
```python
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")

print("Hello", user_name + ", you are", user_age, "years old.")
```
6. Calculate the Area of a Circle with Radius [Example Solution](https://www.youtube.com/watch?v=QoECA8v_2tQ)
7. How to Swap Variables Without a Third Variable in Python. [Example Solution](https://youtu.be/CVy3A48WXeE)
8.  How to assign multiple values to multiple variables. [Example Solution](https://youtu.be/ur8rkDPzuSU)
