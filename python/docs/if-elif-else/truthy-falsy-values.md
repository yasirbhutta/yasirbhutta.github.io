---
layout: page
title: Python Conditional Statements Tutorial - Truthy and Falsy Values
description: Learn Python conditional statements with this comprehensive tutorial. Master if, elif, and else with examples, syntax, and practical tasks for beginners..
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

