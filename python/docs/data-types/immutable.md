---
layout: page
title: "Why Integers, Strings, and Tuples Are Immutable in Python"
description: Why Integers, Strings, and Tuples Are Immutable in Python.
keywords: Why Integers, Strings, and Tuples Are Immutable in Python, tuples in Python, immutable types in python
author: Muhammad Yasir Bhutta
course: python
topic: tuples
toc: toc/ms-excel-toc.html
breadcrumb:
  - title: Home
    url: /
  - title: Python
    url: /python/
  - title: Data Types
    url: /python/docs/data-types.html
---

## Integer (Immutable)
Integers are numbers without any fractional part. In Python, integers are immutable, meaning their value cannot be changed once they are created.

**Example:**
```python
x = 10
print(x)  # Output: 10

x = 20  # This creates a new integer object and binds x to it
print(x)  # Output: 20
```
In this example, when `x` is reassigned from 10 to 20, a new integer object is created, and `x` is updated to reference the new object.

## String (Immutable)
Strings are sequences of characters. In Python, strings are also immutable. Any operation that modifies a string will create a new string rather than altering the existing one.

**Example:**
```python
s = "hello"
print(s)  # Output: hello

s = s + " world"  # This creates a new string object
print(s)  # Output: hello world
```
Here, concatenating `" world"` to `s` does not change the original string `"hello"`. Instead, a new string `"hello world"` is created and assigned to `s`.

## Tuple (Immutable)
Tuples are ordered collections of elements. Like integers and strings, tuples are immutable. Once a tuple is created, you cannot change its contents.

**Example:**
```python
t = (1, 2, 3)
print(t)  # Output: (1, 2, 3)

# Attempting to modify the tuple will raise an error
try:
    t[0] = 4
except TypeError as e:
    print(e)  # Output: 'tuple' object does not support item assignment

# You can create a new tuple
t = (4, 5, 6)
print(t)  # Output: (4, 5, 6)
```
In this example, trying to change the first element of `t` results in a `TypeError` because tuples are immutable. To change the contents, a new tuple must be created.

These examples illustrate that integers, strings, and tuples in Python are immutable, meaning their values cannot be changed after they are created.
