---
layout: page
title: "Mutable vs Immutable Data Types: Key Differences & Examples (2024 Guide)"
description: Learn the difference between mutable and immutable data types with clear examples. Discover Python's mutable (list, dict, set) and immutable (int, str, tuple) types and why they matter in programming.
keywords: mutable vs immutable, mutable and immutable data types, difference between mutable and immutable, Python mutable types, Python immutable types, list vs tuple mutable, why use immutable objects, thread safety mutable immutable, mutable data examples, immutable data examples, Python list dictionary set, Python string tuple int, when to use mutable types, advantages of immutable objects, mutable vs immutable in programming
author: Muhammad Yasir Bhutta
course: python
topic: tuples
toc: toc/python-toc.html
breadcrumb:
  - title: Home
    url: /
  - title: Python
    url: /python/
  - title: Data Types
    url: /python/docs/data-types.html
---

## Table of the Contents
- [Immutable vs. Mutable](#immutable-vs-mutable)
- [Common Mutable Data Types](#common-immutable-data-types)  
- [Common Immutable Data Types](#common-mutable-data-types)

## Immutable vs. Mutable

### **Immutable**  
An **immutable** object cannot be changed after it is created. Any operation that modifies it will create a new object instead of altering the original.

### **Mutable**  
A **mutable** object can be modified after creation without creating a new object.

---

### **Key Differences**  

| Feature          | Immutable                          | Mutable                          |
|------------------|-----------------------------------|----------------------------------|
| **Modification** | Cannot be changed after creation  | Can be changed after creation    |
| **Memory**       | New object created on modification | Same object modified in-place    |
| **Thread Safety**| Safe for concurrent access        | May require synchronization     |
| **Examples**     | `int`, `str`, `tuple` (Python)    | `list`, `dict`, `set` (Python)   |

---

## **Common Mutable Data Types**  

1. **List** – Can be modified (add, remove, change elements).  
   ```python
   lst = [1, 2, 3]
   lst.append(4)  # Original list is modified
   ```

2. **Dictionary** – Key-value pairs can be added, removed, or updated.  
   ```python
   d = {"a": 1}
   d["b"] = 2  # Original dict is modified
   ```

3. **Set** – Elements can be added or removed.  
   ```python
   s = {1, 2, 3}
   s.add(4)  # Original set is modified
   ```

4. **Bytearray** – Similar to bytes but mutable.  
   ```python
   ba = bytearray(b'hello')
   ba[0] = 72  # Modified in-place
   ```

---

## **Common Immutable Data Types**  

1. **int, float, bool** – Cannot be changed once created.  
2. **str** – Modifying a string creates a new one.  
3. **tuple** – Fixed after creation (but can contain mutable objects).  
4. **frozenset** – Immutable version of a set.  

---

### Integer (Immutable)
Integers are numbers without any fractional part. In Python, integers are immutable, meaning their value cannot be changed once they are created.

**Example:**
```python
x = 10
print(x)  # Output: 10

x = 20  # This creates a new integer object and binds x to it
print(x)  # Output: 20
```
In this example, when `x` is reassigned from 10 to 20, a new integer object is created, and `x` is updated to reference the new object.

### String (Immutable)
Strings are sequences of characters. In Python, strings are also immutable. Any operation that modifies a string will create a new string rather than altering the existing one.

**Example:**
```python
s = "hello"
print(s)  # Output: hello

s = s + " world"  # This creates a new string object
print(s)  # Output: hello world
```
Here, concatenating `" world"` to `s` does not change the original string `"hello"`. Instead, a new string `"hello world"` is created and assigned to `s`.

### Tuple (Immutable)
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

### **Why Does It Matter?**  
- **Immutable objects** are safer in multithreading and can be used as dictionary keys.  
- **Mutable objects** are useful when you need to modify data efficiently without creating copies.  

