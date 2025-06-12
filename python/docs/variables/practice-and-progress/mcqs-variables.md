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
prev: /python/docs/variables/practice-and-progress/true-false-variables.html
next: /python/docs/variables/practice-and-progress/find-fix-mistakes-variables.html
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

{% assign topic_name = "variables" %}
{% assign topics = site.data.python.mcqs.topics %}
{% assign selected_topic = topics | where: "topic", topic_name | first %}
{% assign mcqs = selected_topic.questions %}
{% assign resources = selected_topic.resources %}
{% include pap/mcqs-loop.html mcqs=mcqs resources=resources %}

## Multiple Choice (Select the best answer)

1. **What is a variable in Python?**
   - A) A reserved word in Python
   - B) A placeholder for storing data values
   - C) A function that prints data
   - D) A built-in library in Python

2. **Which statement best describes a variable in Python?**
   - A) A variable can hold multiple values at once.
   - B) A variable must be declared with a data type.
   - C) A variable is a name that refers to a value.
   - D) A variable is used only in loops.
  
3. **What is the output of the following code?**

   ```python
   x = 10
   print(x)
   ```
   - A) `10`
   - B) `x`
   - C) `Error`
   - D) `None`

4. **Which of the following is not true about variables in Python?**
   - A) Variables can be reassigned to different data types.
   - B) Variables must start with a letter or an underscore.
   - C) Variables are case-sensitive.
   - D) Variables must be declared before use.

5. **What will be the output of the following code?** [Python Quiz #76]

   ```python
   x = 5
   y = x
   x = 7
   print(y)
   ```
      - A) `7`
      - B) `5`
      - C) `0`
      - D) `None`

6. **Why is it important to use meaningful variable names?**
   - A) It is required by the Python interpreter.
   - B) It helps make the code more readable and maintainable.
   - C) It increases the execution speed of the program.
   - D) It is necessary for the code to run without errors.

7. **What will be the output of the following code?** [Python Quiz #77]

   ```python
   a = 1
   b = a
   a = a + 1
   print(a, b)
   ```
      - A) `1 1`
      - B) `2 1`
      - C) `1 2`
      - D) `2 2`

8. **Which of the following is a valid variable name in Python?**
   - A) `2ndValue`
   - B) `value#2`
   - C) `_value2`
   - D) `value-2`

9.  **Which of the following is a correct way to declare a variable in Python?**
   - A) `int x = 5`
   - B) `x = 5`
   - C) `declare x = 5`
   - D) `var x = 5`
   
10. **What is the output of the following code?** [Python Quiz 78]
   ```python
   x = 5
   y = "Hello"
   print(x + y)
   ```
      - A) `5Hello`
      - B) `Hello5`
      - C) `TypeError`
      - D) `Hello 5`
   
11.  **Which of the following is not a valid variable name in Python?**
   - A) `my_var`
   - B) `_var`
   - C) `2var`
   - D) `var2`

12. **Which of the following statements is true about variable assignment in Python?**
   - A) Variables must be declared before they are assigned a value.
   - B) Variables are created when they are first assigned a value.
   - C) Variable names must begin with a number.
   - D) Python variables must be declared with a type.
   

# 38 What is the purpose of declaring a variable in Python?
a) To reserve memory space for the variable
b) To give the variable a name
c) To initialize the variable with a value
d) All of the above
Answer: d

   
**Answer key (Mutiple Choice):**

1. B) A placeholder for storing data values
2. C) A variable is a name that refers to a value.
3. A) `10`
4. D) Variables must be declared before use.
5. B) `5`
6. B) It helps make the code more readable and maintainable.
7. B) `2 1`
8. C) `_value2`
9. B) `x = 5`
10. C) `TypeError`
    - **Explanation:** In Python, the + operator is used for both arithmetic addition and string concatenation. However, it cannot be used to add an integer and a string directly. The code provided attempts to add an integer (x = 5) to a string (y = "Hello"), which is not a valid operation and will result in a TypeError.
11. C) `2var`
    - **Explanation:** In Python, variable names must start with a letter or an underscore and cannot start with a number. Thus, my_var, _var, and var2 are valid, but 2var is not.
12. B) Variables are created when they are first assigned a value.
13. A) `5`  