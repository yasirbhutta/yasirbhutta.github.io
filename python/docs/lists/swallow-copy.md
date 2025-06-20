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

## 4. ✅ When to Use Shallow Copy

Use shallow copy when:

* You want a new outer container.
* You don’t plan to modify nested objects separately.

---

## 📘 **Related Topics**

* **What is a Deep Copy in Python?** – In Python, a **shallow copy** is a new object that is a **copy of the original object**, but it **does not create copies of nested objects** (objects inside objects).
  👉 [Learn more](deep-copy.md)


