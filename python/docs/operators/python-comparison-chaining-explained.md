---
layout: page
title: "Python Comparison Chaining Explained (0 < amount < balance) with Examples"
description: Learn Python comparison chaining with simple examples. Understand how expressions like 0 < amount < balance work, including evaluation steps, short-circuiting, and benefits for beginners.
keywords: python comparison chaining, python chained comparisons, 0 less than amount less than balance python, python logical operators, python and operator vs chaining, python tutorial for beginners, python conditions examples, comparison operators python, python short circuit evaluation, python boolean expressions, learn python basics, python if condition tutorial
toc: toc/python.html
author: Muhammad Yasir Bhutta
course: python
topic: operators
show_toc: true
show_practice_progress: true
show_mini_project: false
breadcrumb: 
- title: Operators
url: /python/docs/operators/
---

---

# **Comparison Chaining in Python**

In Python, the expression:

```python
0 < amount < balance
```

is an example of **comparison chaining**.

It allows you to write multiple conditions in a single, clean statement—just like in mathematics (e.g., “amount is between 0 and balance”).

---

## **How Python Evaluates It**

Python internally treats:

```python
0 < amount < balance
```

as:

```python
(0 < amount) and (amount < balance)
```

---

## **Step-by-Step Logic**

1. **First Check:**
   Python checks if `0 < amount`.

2. **Short-Circuiting:**

   * If this is **False**, Python stops immediately.
   * The second condition is **not checked**.

3. **Second Check:**
   If the first condition is **True**, Python checks if `amount < balance`.

4. **Final Result:**

   * If both conditions are **True**, the result is **True**.
   * Otherwise, the result is **False**.

---

## **Why Use Comparison Chaining?**

### ✅ **1. Better Readability**

* Matches mathematical expressions
* Easy to understand: *“amount is between 0 and balance”*

### ✅ **2. More Efficient**

* The middle value (`amount`) is evaluated **only once**
* Useful when using functions:

  ```python
  0 < get_amount() < balance
  ```

---

## **Examples**

| Scenario         | Values                          | Result |
| ---------------- | ------------------------------- | ------ |
| Valid Range      | `amount = 50`, `balance = 100`  | True   |
| Zero or Negative | `amount = 0`, `balance = 100`   | False  |
| Exceeds Balance  | `amount = 150`, `balance = 100` | False  |

---

## **Important Note (Other Languages)**

In languages like C++ or Java, writing:

```cpp
0 < amount < balance
```

can give **incorrect results**.

Why?

* First, `0 < amount` is evaluated → gives `true` or `false`
* Then, that boolean is compared with `balance` → which is **not intended**

👉 **Python is different**:
It understands the chain and evaluates it correctly as a combined condition.

---

## **Quick Tip**

You can chain multiple comparisons:

```python
0 < amount < balance < limit
```

This is equivalent to:

```python
(0 < amount) and (amount < balance) and (balance < limit)
```

---
