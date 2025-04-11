---
layout: default
title: Find and Fix Mistakes in Python Classes - Common Errors Explained.
description: Learn how to identify and fix common mistakes in Python classes with this beginner-friendly exercise. Perfect for understanding constructors, instance variables, and methods.
---

# Find and Fix Mistakes in Python Classes: Common Errors Explained

## Exercise #1: Fixing Constructor and Method Errors (Beginner)

Below is a Python class with mistakes. Your task is to identify and fix the errors to make the code functional.

**Code with Mistakes**

```python
class Person:
    def __init__(name, age):
        name = name
        age = age

    def greet():
        print("Hello, my name is " + self.name)

person1 = Person("Alice", 30)
person1.greet()
```

> **Hint:**  
> - Check the parameters of the `__init__` method and ensure they are correctly assigned to instance variables using `self`.  
> - Verify that the `greet` method includes `self` as a parameter.

[View Solution](solutions/find-fix-mistakes-classes1.md)

