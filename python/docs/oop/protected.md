---
layout: page
title: "What Does Protected Access Level Mean in Python?"
description: Learn Python OOP encapsulation with real-world examples. Understand public, protected, and private access levels for clean, secure, and maintainable code.
keywords: Python OOP, encapsulation in Python, Python access levels, protected variables Python, private vs protected Python, Python class example, object oriented programming Python, Python beginner tutorial, Python inheritance, Python class access control
author: Muhammad Yasir Bhutta
course: python
prev: /python/docs/oop-encapsulation/
breadcrumb:
  - title: Home
    url: /
  - title: OOP
    url: /python/docs/oop/
  - title: OOP
    url: /python/docs/oop-encapsulation/
---

In Python OOP, **protected access** is a **convention** that suggests a variable or method **should not be accessed directly** from outside the class — but **it still can be**.

---

## 🔍 Definition:

> A **protected member** in Python is defined by prefixing its name with a **single underscore `_`**.

```python
class Car:
    def __init__(self):
        self._speed = 100  # protected variable

    def show_speed(self):
        print(f"Speed: {self._speed} km/h")
```

* `_speed` is **protected**, meaning:

  * It **should be accessed only within the class or its subclasses**.
  * It **can still be accessed** outside the class, but it's **not recommended**.

---

### 📘 Why Use Protected?

* To **warn other developers**: “This is meant for internal or subclass use.”
* To support **inheritance**, where child classes can access or modify it.
* To **organize your code** and control data flow better.

---

### 📚 Example with Inheritance:

```python
class Car:
    def __init__(self):
        self._speed = 100  # protected

    def show_speed(self):
        print(f"Speed: {self._speed} km/h")

class SportsCar(Car):
    def boost(self):
        self._speed += 50

car = SportsCar()
car.boost()
car.show_speed()  # ✅ Speed: 150 km/h
```

Even though `_speed` is marked as protected, the subclass can access and modify it.

---

### ⚠️ Accessing Protected Members from Outside:

```python
car = Car()
print(car._speed)  # ⚠️ Possible, but not recommended
```

Python allows it, but by convention, you're **not supposed to do it**. Think of it as a **"handle with care"** warning.

---

### ✅ Summary

| Access Level | Syntax   | Meaning                                     |
| ------------ | -------- | ------------------------------------------- |
| Public       | `name`   | Free to access anywhere                     |
| Protected    | `_name`  | Suggests limited access (class or subclass) |
| Private      | `__name` | Strongest hiding (name mangling in Python)  |

---

## 📘 **Related Topics**

* **Encapsulation in Python OOP** – Learn Python OOP encapsulation with Beginner's examples.
  👉 [Learn more](../oop-encapsulation/)