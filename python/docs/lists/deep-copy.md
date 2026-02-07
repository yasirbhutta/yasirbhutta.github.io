---
layout: page
title: "Deep Copy in Python – Explained with Examples and Comparison"
description: Learn what a deep copy is in Python, how it differs from a shallow copy, and when to use it. Includes simple explanations, beginner-friendly code examples, and use cases for nested lists and dictionaries.
keywords: deep copy in Python, Python deepcopy example, copy module Python, shallow vs deep copy Python, Python copy nested objects, deep copy dictionary Python, Python deep copy tutorial, beginner Python copy examples, deepcopy vs copy Python
toc: toc/python.html
prev: /python/docs/dss.html
next: /python/docs/lists/lists-basics.html
course: python
topic: lists
show_toc: true
show_practice_progress: true
show_mini_project: false
breadcrumb: 
- title: Lists
url: /python/docs/lists/
---

## Table of Contents

1. [What is a Deep Copy in Python?](#1--what-is-a-deep-copy-in-python)
2. [Why Use Deep Copy?](#2--why-use-deep-copy)
3. [How to Make a Deep Copy?](#3--how-to-make-a-deep-copy)
4. [Beginner-Friendly Example](#4--beginner-friendly-example)
5. [Comparison: Shallow vs Deep Copy](#5--comparison-shallow-vs-deep-copy)
6. [Another Example: Dictionary with Nested List](#6--another-example-dictionary-with-nested-list)


## 1. 🧠 What is a **Deep Copy** in Python?

A **deep copy** creates a **completely independent copy** of an object **and all nested objects inside it**.

> Changes made to the original object **do not affect** the deep copy, and vice versa.

---

## 2. ✅ Why Use Deep Copy?

When your object contains **nested structures** like:

* Lists of lists
* Dictionaries of dictionaries
* Objects containing other objects

…and you want **totally independent copies**, use deep copy.

---

## 3. 📦 How to Make a Deep Copy?

Use the `copy` module:

```python
import copy

deep_copy_object = copy.deepcopy(original_object)
```

---

## 4. 🔍 Beginner-Friendly Example:

```python
import copy

original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)

# Modify deep copy
deep[0][0] = 100

print("Original:", original)  # Output: [[1, 2], [3, 4]]
print("Deep Copy:", deep)     # Output: [[100, 2], [3, 4]]
```

✅ Here, changing `deep[0][0]` **does not affect** the original list.

---

## 5. 🔁 Comparison: Shallow vs Deep Copy

| Feature          | Shallow Copy (`copy.copy()`) | Deep Copy (`copy.deepcopy()`) |
| ---------------- | ---------------------------- | ----------------------------- |
| Copies top-level | ✅                            | ✅                             |
| Copies nested    | ❌ (references only)          | ✅ (real copies)               |
| Independent?     | ❌                            | ✅                             |

---

## 6. 🧪 Another Example: Dictionary with Nested List

```python
import copy

original = {'a': [1, 2]}
deep = copy.deepcopy(original)

deep['a'][0] = 100

print("Original:", original)  # {'a': [1, 2]}
print("Deep Copy:", deep)     # {'a': [100, 2]}
```

## 📘 **Related Topics**

* **What is a Shallow Copy** – In Python, a **shallow copy** is a new object that is a **copy of the original object**, but it **does not create copies of nested objects** (objects inside objects).
  👉 [Learn more](swallow-copy.md)

