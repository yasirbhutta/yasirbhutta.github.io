---
layout: page
title: Python MRO (Method Resolution Order) – OOP Guide
description: Understand MRO (Method Resolution Order) in Python OOP. Learn how Python resolves method calls in multiple inheritance using C3 linearization with examples.
keywords: Python MRO, method resolution order, Python inheritance, OOP MRO, multiple inheritance Python, C3 linearization, Python class hierarchy, method lookup order, Python OOP tutorial
toc: toc/python.html
author: Muhammad Yasir Bhutta
course: python
topic: oop-inheritance
show_toc: true
toc: toc/python.html
show_practice_progress: true
show_mini_project: false
prev: /python/docs/basics/
next: /python/docs/operators/practice-and-progress/find-fix-mistakes-variables.html
breadcrumb:
  - title: Home
    url: /
  - title: Python
    url: /python/
  - title: OOP
    url: /python/docs/oop/
  - title: Inheritance
    url: /python/docs/oop-inheritance/
---

## 🧠 What is MRO?

MRO stands for **Method Resolution Order**. It defines the **order in which Python looks for methods and attributes** in a hierarchy of classes when you use `super()`.

---

## 🪜 Why is MRO Needed?

Consider a "diamond inheritance" like this:

```
     A
    / \
   B   C
    \ /
     D
```

- All classes eventually inherit from `A`.
- Without MRO, Python could accidentally call `A` multiple times — causing bugs.
- MRO ensures that each class’s method (like `__init__`) is called **once**, and in a predictable order.

---

## 🔄 How MRO Works

Python uses the **C3 Linearization Algorithm** to compute MRO.

```python
class A:
    def __init__(self):
        print("A initialized")

class B(A):
    def __init__(self):
        super().__init__()
        print("B initialized")

class C(A):
    def __init__(self):
        super().__init__()
        print("C initialized")

class D(B, C):
    def __init__(self):
        super().__init__()  # Initializes B -> C -> A
        print("D initialized")

d = D()  # Output order might surprise beginners
```

---

### 📦 Class Definitions

```python
class A:
    def __init__(self):
        print("A initialized")
```
- Base class `A`. It prints a message when initialized.

```python
class B(A):
    def __init__(self):
        super().__init__()
        print("B initialized")
```
- Class `B` inherits from `A`.
- It calls `super().__init__()`, which refers to `A.__init__`.

```python
class C(A):
    def __init__(self):
        super().__init__()
        print("C initialized")
```
- Similarly, `C` inherits from `A`.

```python
class D(B, C):
    def __init__(self):
        super().__init__()  # MRO applies here
        print("D initialized")
```
- `D` inherits from both `B` and `C`. This is where **MRO** kicks in.

---

### 🤯 What Happens When You Call `d = D()`?

When we create an instance of `D`, the following happens:

1. Python looks at the **MRO** (Method Resolution Order) of class `D`.
2. `D` inherits from `B` and `C`, and both inherit from `A`. So Python uses **C3 linearization** to resolve this.

To see the MRO:
```python
print(D.mro())
```
Output:
```python
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
```
This means:
1. Start at `D`
2. Then look in `B`
3. Then `C`
4. Then `A`
5. Finally, `object` (the root class of all Python classes)

## 🛠️ How `super()` Uses MRO

When you call `super().__init__()` inside `D`, Python uses the MRO list:
- It goes to the next class after `D` → that’s `B`
- `B`'s `super()` calls the next one → `C`
- `C`'s `super()` calls the next → `A`
- `A` doesn’t use `super()`, so it ends there

**No class is repeated**, and the initialization flows down this path.

---

### 🔄 Final Output Order:

```python
A initialized
C initialized
B initialized
D initialized
```

Explanation:

- `D.__init__` → `B.__init__` → `C.__init__` → `A.__init__`
- Then the print statements in reverse order as the stack unwinds.

---

## 📌 Summary

- **MRO ensures consistency** in how classes are searched.
- `super()` follows the MRO chain.
- You can always check MRO with: `ClassName.mro()` or `help(ClassName)`
- MRO prevents the **diamond problem** by avoiding multiple calls to the same base class.

