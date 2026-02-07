---
layout: page
title: Introduction to Python Dictionaries – Concepts, Usage, and Examples
description: Learn the basics of Python dictionaries with this beginner-friendly guide. Understand key-value pairs, how to create, access, update, and manipulate dictionaries in Python with practical examples and coding tasks. Perfect for students and professionals to master Python dictionaries.
keywords: Python dictionaries, Python dictionary tutorial, create dictionary in Python, access dictionary values, update dictionary Python, manipulate dictionary Python, Python dictionary examples, beginner Python dictionaries, Python data structures, learn Python
course: python
topic: dictionaries
toc: toc/python.html
show_toc: true
show_practice_progress: true
show_mini_project: false
prev: /python/docs/dictionaries/
next: /python/docs/dictionaries/dict-methods.html
breadcrumb: 
- title: Python
url: /python/
---

## Table of Contents

1. [Creating a Dictionary](#1-creating-a-dictionary)
2. [Accessing Values](#2-accessing-values)
3. [Adding or Updating Elements](#3-adding-or-updating-elements)
4. [Common Mistake](#4-common-mistake)  

In Python, a **dictionary** is a collection of key-value pairs. Each key in a dictionary is unique, and it is associated with a value. Dictionaries are used to store data values like a map or a real-life dictionary where each word (key) has a definition (value). They are mutable, meaning you can change, add, or remove items after the dictionary is created.

**Example:**

> Think of a Python dictionary like a real dictionary: each word (key) has a definition (value).

## 1. **Creating a Dictionary**

You create a dictionary using curly braces `{}` with keys and values separated by a colon `:`. Multiple key-value pairs are separated by commas.

```python
# Creating a dictionary with student information
student = {
    "name": "John",      # Key: "name", Value: "John"
    "age": 20,           # Key: "age", Value: 20
    "courses": ["Math", "Science"]  # Key: "courses", Value: list of courses
}
```

## 2. **Accessing Values**

You can access the value associated with a specific key by using square brackets `[]` or the `get()` method.

```python
# Accessing values
print(student["name"])  # Output: John
print(student.get("age"))  # Output: 20
```

## 3. **Adding or Updating Elements**

You can add a new key-value pair or update an existing one by assigning a value to the key.

```python
# Adding a new key-value pair
student["grade"] = "A"

# Updating an existing value
student["age"] = 21
```

## 4. **Common Mistake:**  

Trying to use a list as a key will cause an error because lists are not hashable.

## 5. **Tasks**

### **Task 1: Creating a Dictionary**  
Write a Python program that:  
- Creates a dictionary with **two items** (name and age).  
- Prints the dictionary.  
- Prints only the **name** from the dictionary.  

**Example Output:**  
```
Person: {'name': 'Alice', 'age': 25}
Name: Alice
```

---

### **Task 2: Adding to a Dictionary**  
Write a Python program that:  
- Creates a dictionary with **name and country**.  
- Adds a new key **"hobby"** with a value.  
- Prints the updated dictionary.  

**Example Output:**  
```
Original Dictionary: {'name': 'John', 'country': 'USA'}
Updated Dictionary: {'name': 'John', 'country': 'USA', 'hobby': 'Reading'}
```

---


