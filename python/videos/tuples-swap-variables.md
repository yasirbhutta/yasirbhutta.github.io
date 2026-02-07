---
layout: page
title: "Python tuples example: How to Swap Variables in One Line of Code using Tuple Unpacking"
description: How to Swap Variables in One Line of Code using Tuple Unpacking.
keywords: Swap Variables using Tuple Unpacking, one liner to swap variables, python tuples example, python exercise for beginners
author: Muhammad Yasir Bhutta
course: python
topic: tuples
toc: toc/python.html
prev: /python/docs/tuples/tuples-basics.html
breadcrumb: 
- title: Tuples
url: /python/docs/tuples/
---

{% assign video_type = "video" %}
{% assign video_id = "MCeTYJVktmU" %}
{% include youtube-video.html video_type=video_type video_id=video_id %}

## **📺 Python Tutorial: How to Swap Variables in One Line of Code using Tuple Unpacking**  

**This video covers:**
* ✔️ Exchange the values of two variables using a single line of code.

## Problem Statement

Write a Python function called `swap_variables` that takes two variables, `a` and `b`, as input. The function should swap the values of these two variables using the one-line tuple unpacking technique and then return the new values of `a` and `b` as a tuple.

**Input:**

Two variables of any data type. For example:
```python
x = 10
y = 5
```

**Expected Output:**

A tuple containing the swapped values. For the example input above:
```
(5, 10)
```

**Here's a starting point for the function:**

```python
def swap_variables(a, b):
    # Write your one-line swap using tuple unpacking here
    return a, b

# Example usage:
x = 10
y = 5
swapped_x, swapped_y = swap_variables(x, y)
print(f"Original x: {x}, y: {y}")
print(f"Swapped x: {swapped_x}, y: {swapped_y}")
```

## 📘 **Related Topics**

* **Tuples in Python** – Understand the basics of tuples in Python with clear explanations and practical examples.
  - 👉 [Learn more](../docs/tuples/tuples-basics.md)


