---
layout: page
title: Nested Conditions of if, elif, else in Python
description: Learn Python conditional statements with this comprehensive tutorial. Master if, elif, and else with examples, syntax, and practical tasks for beginners..
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

