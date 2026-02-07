---
layout: page
title: Nested if‑elif‑else Statements in Python – With Examples
description: Learn how to use nested if‑elif‑else statements in Python to handle complex decision-making. Includes clear syntax, beginner-friendly examples, and practical use cases.
keywords: nested if statements Python, Python nested conditions, Python nested if elif else, conditional logic in Python, Python decision making, beginner Python conditions, nested control flow Python, Python nested example code
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

## 🔹 What is **Nested Conditions** in Python?

**Nested conditions** in Python refer to using one `if` (or `if-elif-else`) statement **inside another**. This allows you to check more complex decision-making scenarios, where the second condition depends on the first being true.

---

### 📌 Basic Structure:

```python
if condition1:
    if condition2:
        # Code runs if both condition1 and condition2 are True
    else:
        # Runs if condition1 is True, but condition2 is False
else:
    # Runs if condition1 is False
```

---

### ✅ Example 1: Checking age and ID

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("Entry denied: No ID")
else:
    print("Entry denied: Too young")
```

* First checks if `age >= 18`
* Then checks if `has_id` is `True` **only if** the age condition passed

---

### ✅ Example 2: Grading system

```python
score = 85

if score >= 50:
    if score >= 75:
        print("Passed with Distinction")
    else:
        print("Passed")
else:
    print("Failed")
```

---

## 🔁 Nesting Levels

You can nest more than once, but **keep it readable**. Too much nesting is hard to manage and understand.

---

## 📌 Tip: Use logical operators (`and`, `or`) to avoid deep nesting:

Instead of:

```python
if age >= 18:
    if has_id:
        print("Entry allowed")
```

You can write:

```python
if age >= 18 and has_id:
    print("Entry allowed")
```

