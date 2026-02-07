---
layout: page
title: Truthy and Falsy Values in Python – Conditional Logic Simplified
description: Understand how truthy and falsy values work in Python. Learn which values evaluate to True or False in conditional statements, with examples and practical tips for beginners.
keywords: truthy falsy Python, Python boolean logic, Python condition evaluation, Python true false values, falsy values list Python, Python truthy values explained, conditional checks Python, Python boolean conversion
author: "Muhammad Yasir Bhutta"
toc: toc/python.html
course: "python"
topic: "if-elif-else"
prev: /python/docs/lists/practice-and-progress/mini-projects-lists.html
next: /python/docs/functions.html
show_practice_progress: true
show_mini_project: null
show_toc: true
breadcrumb: 
- title: if-elif-else
url: /python/docs/if-elif-else/
---

In Python, some values are treated as `True` or `False` automatically when used in conditions.

#### Falsy values (evaluated as `False`):

* `None`
* `False`
* `0` (any numeric zero)
* `""` (empty string)
* `[]` (empty list)
* `{}` (empty dict)
* `set()` (empty set)

#### Everything else is **truthy**.

```python
username = ""

if username:
    print("Welcome,", username)
else:
    print("Please enter a valid username")
```

Since `username` is an empty string (`""`), it's falsy — the `else` block runs.

---

### ✅ Quick Practice Example

```python
score = 75

if score:
    if score >= 90:
        print("Grade A")
    elif score >= 75:
        print("Grade B")
    else:
        print("Grade C")
else:
    print("No score provided")
```

