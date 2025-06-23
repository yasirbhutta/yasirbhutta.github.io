---
layout: page
title: "Shallow Copy in Python – Explained with Examples and Use Cases"
description: Understand what a shallow copy is in Python, how to create one, and when to use it. Learn with beginner-friendly examples and comparisons to deep copy for nested objects.
keywords: shallow copy in Python, Python copy vs deepcopy, shallow copy example, Python copy module, copy() method Python, Python list shallow copy, shallow copy dictionary Python, when to use shallow copy, Python object reference copy
toc: toc/python.html
prev: /python/docs/dss.html
next: /python/docs/lists/lists-basics.html
course: python
topic: lists
show_toc: true
show_practice_progress: true
show_mini_project: false
breadcrumb:
  - title: Home
    url: /
  - title: Python
    url: /python/
  - title: Lists
    url: /python/docs/lists/
---

## Table of Contents

1. [What is a Shallow Copy?](#1--what-is-a-shallow-copy)
2. [How to Create a Shallow Copy](#2--how-to-create-a-shallow-copy)
3. [Example](#3--example)
4. [When to Use Shallow Copy](#4--when-to-use-shallow-copy)


In Python, a **shallow copy** is a new object that is a **copy of the original object**, but it **does not create copies of nested objects** (objects inside objects). Instead, it only copies references to those inner objects.

---

## 1. ✅ What is a Shallow Copy?

* It copies the outer object.
* Inner elements (like lists or dictionaries inside a list) are **not copied**, only their **references** are copied.
* Changes to nested objects in the copied object **affect the original**.

---

## 2. 📌 How to Create a Shallow Copy

1. **Using `copy()` method (for lists, dicts, etc.):**

```python
original = [[1, 2], [3, 4]]
shallow = original.copy()
```

2. **Using the `copy` module:**

```python
import copy
shallow = copy.copy(original)
```

---

## 3. 🔍 Example:

```python
import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)

shallow[0][0] = 100

print("Original:", original)  # [[100, 2], [3, 4]]
print("Shallow:", shallow)    # [[100, 2], [3, 4]]
```

✅ The outer list is copied.
❌ The inner lists are **shared**, so modifying `shallow[0][0]` changes `original[0][0]`.

---

Here's a line-by-line explanation of the code:

---

### 🔸 Code:

```python
import copy
```

✅ This imports Python’s built-in `copy` module, which provides functions to perform shallow and deep copies.

---

```python
original = [[1, 2], [3, 4]]
```

✅ A list named `original` is created. It contains **two inner lists**, making it a nested list (a list of lists).

---

```python
shallow = copy.copy(original)
```

✅ This creates a **shallow copy** of `original` and stores it in `shallow`.

* A **new outer list** is created.
* The **inner lists are not copied**; only their **references** are copied.

So now:

* `original` and `shallow` are two different outer lists.
* But `original[0]` and `shallow[0]` point to the **same inner list** `[1, 2]`.

---

```python
shallow[0][0] = 100
```

✅ This changes the first element of the first inner list **through the shallow copy**.

Since the inner list `[1, 2]` is **shared** between `original` and `shallow`, the change affects both.

---

```python
print("Original:", original)  # [[100, 2], [3, 4]]
print("Shallow:", shallow)    # [[100, 2], [3, 4]]
```

✅ Output shows that **both `original` and `shallow` are affected**:

```
Original: [[100, 2], [3, 4]]
Shallow:  [[100, 2], [3, 4]]
```

---

![shallow copy](https://res.cloudinary.com/da0pjikvw/image/upload/c_pad,w_512/v1750654377/shallow-copy_gjknoc.png)

### 🔍 Summary:

* `copy.copy()` only copies the outer list.
* The inner lists are **shared** between `original` and `shallow`.
* Changes to inner lists in the copy will **affect the original**.

---

## 4. ✅ When to Use Shallow Copy

Use shallow copy when:

* You want a new outer container.
* You don’t plan to modify nested objects separately.

---

## 📘 **Related Topics**

* **What is a Deep Copy in Python?** – A deep copy creates a completely independent copy of an object and all nested objects inside it.
  👉 [Learn more](deep-copy.md)


