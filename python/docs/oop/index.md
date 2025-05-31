---
layout: page
title: "Object-Oriented Programming in Python (OOP): Tutorial"
description: Learn Python Object-Oriented Programming (OOP) with examples on classes, objects, inheritance, and polymorphism. Master Python OOP concepts for better coding practices.
keywords: Python OOP, Python classes, Python objects, inheritance in Python, polymorphism Python, encapsulation Python, Python methods, Python attributes, object-oriented programming Python, Python OOP tutorial
author: Muhammad Yasir Bhutta
course: python
topic: oop
toc: toc/python.html
prev: /python/docs/decorators.html
next: /python/docs/classes.html
breadcrumb:
  - title: Home
    url: /
  - title: Python
    url: /python/
---

## Contents

### [1. Start with the Basics](../classes.md)

#### 1.1 Introduction to OOP

- OOP: Introduction
- OOP Example
- Object Oriented Programming in Python
- Is Python Object Oriented?

#### 1.2 Classes & Objects

- How to create a class
- Instantiating objects
- Adding attributes to a class
- Define methods in a class
- Passing arguments to methods
- Python OOP Example
- Object-Oriented Programming in Python: Wrap-Up

#### 1.3 Methods in Classes

### 2. Core OOP Concepts

#### [2.1 Inheritance](../oop-inheritance/)
#### [2.2 Polymorphism](../oop-polymorphism/)
#### [2.3 Encapsulation](../oop-encapsulation/)
#### [2.4 Abstraction and Interfaces](../oop-abstraction/)

### 3. Advanced Topics

#### a. Magic Methods (`__str__`, `__eq__`, etc.)
#### b. Composition over Inheritance
#### c. Class Methods & Static Methods

### 4. OOP Best Practices

### 5. Project: Inventory Management System

---

### **2. Core OOP Concepts**
#### **a. Encapsulation**
- Protect data using **private attributes** (e.g., `_variable` or `__variable`).
- Use `@property` and setters for controlled access.

**Example**:
```python
class Temperature:
    def __init__(self):
        self.__celsius = 0  # Private attribute

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature too low!")
        self.__celsius = value

temp = Temperature()
temp.celsius = 25  # Uses the setter
print(temp.celsius)  # Output: 25
```

---

#### **d. Abstraction**
- Use abstract classes to enforce method definitions in child classes.

**Example**:
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):  # Must be implemented
        return self.side ** 2

# shape = Shape()  # Error: Can't instantiate abstract class
square = Square(4)
print(square.area())  # Output: 16
```

---

### **3. Advanced Topics**
#### **a. Magic Methods (`__str__`, `__eq__`, etc.)**
- Customize object behavior for built-in operations.

**Example**:
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # Overload the '+' operator
        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(1, 2)
v2 = Vector(3, 4)
result = v1 + v2
print(result.x, result.y)  # Output: 4 6
```

---

#### **b. Composition over Inheritance**
- Build complex objects by combining simpler ones (flexible alternative to inheritance).

**Example**:
```python
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition: Car "has-a" Engine

my_car = Car()
print(my_car.engine.start())  # Output: "Engine started"
```

---

#### **c. Class Methods & Static Methods**
- `@classmethod`: For factory methods.
- `@staticmethod`: For utility functions.

**Example**:
```python
class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

    @staticmethod
    def is_adult(age):
        return age >= 18

Student.change_school("XYZ School")
print(Student.school)  # Output: "XYZ School"
print(Student.is_adult(20))  # Output: True
```

---

### **4. Common Pitfalls to Avoid**
1. **Overusing Inheritance**: Prefer composition for flexibility.
2. **Ignoring Encapsulation**: Avoid exposing all data as public.
3. **Forgetting `self`**: Instance methods need `self` as the first parameter.
4. **Circular Dependencies**: Keep class dependencies simple.

---

### **5. Hands-On Projects**
1. **Inventory System**:
   - Classes: `Product`, `Inventory`, `Supplier`.
   - Methods: `add_product()`, `check_stock()`.

2. **Social Media Profile**:
   - Classes: `User`, `Post`, `Comment`.
   - Features: `create_post()`, `like_post()`.

3. **School Management System**:
   - Classes: `Student`, `Teacher`, `Course`.
   - Methods: `enroll()`, `assign_grade()`.

---

### **6. Learning Resources**
- **Free Tutorials**:
  - [Real Python’s OOP Guide](https://realpython.com/python3-object-oriented-programming/)
  - [Corey Schafer’s OOP YouTube Series](https://youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc)
- **Books**:
  - *Python Object-Oriented Programming* by Steven F. Lott
  - *Head First Python* (2nd Edition)

---

### **7. Practice Challenges**
- **Easy**: Create a `BankAccount` class with deposit/withdraw methods.
- **Medium**: Build a `Playlist` class that manages `Song` objects.
- **Hard**: Design a `ChessGame` with classes for `Board`, `Piece`, and `Player`.

---

By focusing on these steps, practicing with projects, and avoiding common mistakes, you’ll master Python OOP efficiently! 🐍💡