---
layout: page
title: "Python Math Module: isinf() vs isfinite() Explained"
description: Learn the key differences between math.isinf() and math.isfinite() in Python. Understand how to detect infinite, finite, and NaN values effectively using the math module.
keywords: Python math module, math.isinf vs math.isfinite, check infinity in Python, detect finite values Python, Python isfinite function, Python isinf function, Python math checks, Python NaN and infinity, Python numerical validation
author: Muhammad Yasir Bhutta
course: python
topic: math-module
show_toc: false
toc: toc/python.html
show_practice_progress: false
show_mini_project: false
prev: /ms-excel/docs/math/
breadcrumb: 
- title: Math
url: /python/docs/math-module/
---

Here’s a clear comparison between `math.isinf(x)` and `math.isfinite(x)` in Python:

---

## **`math.isinf(x)`**

* **Purpose**: Checks whether a value is infinite.
* **Returns**: `True` if `x` is either positive infinity (`+inf`) or negative infinity (`-inf`); otherwise, `False`.
* **Example**:

  ```python
  import math
  print(math.isinf(float('inf')))   # True
  print(math.isinf(10))             # False
  ```

---

## **`math.isfinite(x)`**

* **Purpose**: Checks whether a value is a finite number.
* **Returns**: `True` if `x` is neither infinite (`inf`, `-inf`) nor NaN (Not a Number); otherwise, `False`.
* **Example**:

  ```python
  import math
  print(math.isfinite(10))            # True
  print(math.isfinite(float('inf')))  # False
  print(math.isfinite(float('nan')))  # False
  ```

---

### **Key Differences**

| Feature              | `math.isinf(x)`             | `math.isfinite(x)`            |
| -------------------- | --------------------------- | ----------------------------- |
| **Checks for**       | Infinity (`+inf` or `-inf`) | Not infinite and not NaN      |
| **Returns True if**  | `x` is infinite             | `x` is a normal finite number |
| **Returns False if** | `x` is finite or NaN        | `x` is either infinite or NaN |

---


