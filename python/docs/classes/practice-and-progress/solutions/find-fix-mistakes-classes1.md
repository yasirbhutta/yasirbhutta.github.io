---
layout: default
title: Python Classes - Find and Fix Mistakes with Code Examples.
description: Learn how to identify and fix common mistakes in Python classes with this step-by-step guide. Perfect for beginners to understand constructors, instance variables, and methods in object-oriented programming.
---

# Find and Fix Mistakes in Python Classes: Common Errors Explained

- **Difficulty Levels:** Beginner ✅ | Intermediate | Advanced  
  This exercise is designed for beginners to understand constructors and methods in Python classes.
- **Topic:** Classes

## **Code with Mistakes**  
Below is a Python class with mistakes. Your task is to identify and fix the errors to make the code functional.
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

---

## **Mistakes Explained**  
Here are the common mistakes in the code and their explanations:
1. **Missing `self` in the constructor parameter list**: The first parameter of any instance method, including `__init__`, must be `self`.
2. **Wrong assignment in `__init__`**: It should assign values to instance variables using `self`, not the parameter names themselves.
3. **Missing `self` in method parameter**: `greet()` should take `self` as a parameter.
4. **Using `self.name` without defining `self.name`** properly in the constructor.

---

## **Corrected Code**  
Below is the corrected version of the code with all mistakes fixed:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name)

person1 = Person("Alice", 30)
person1.greet()
```

---

## Related Challenges