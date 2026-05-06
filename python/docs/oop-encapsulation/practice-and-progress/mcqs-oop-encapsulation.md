---
layout: page
title: Python Encapsulation MCQs – Test Your OOP Knowledge
description: Challenge your understanding of Python's Object-Oriented Programming with these multiple-choice questions on encapsulation. Ideal for beginners, students, and job seekers to reinforce key OOP concepts.
keywords: python encapsulation, oop in python, python mcqs, encapsulation quiz, python multiple choice questions, learn with yasir, yasirbhutta, python classes, python access modifiers, python getter setter, python name mangling, python oop practice, python encapsulation tutorial
author: Muhammad Yasir Bhutta
toc: toc/python.html
topic: "oop-encapsulation"
course: "python"
show_practice_progress: true
show_mini_project: null
show_toc: true
prev: /python/docs/oop-encapsulation/practice-and-progress/fill-blanks-oop-encapsulation.html
next: /python/docs/oop-encapsulation/practice-and-progress/find-fix-mistakes-oop-encapsulation.html
---

### 1. What is encapsulation in Python?

A. Hiding implementation details and showing only essential features
B. Binding data and methods into a single unit
C. Creating multiple classes
D. Executing code automatically

**Answer:** B
**Explanation:** Encapsulation bundles data and methods into a class and restricts direct access. ([Learn with Yasir][1])

---

### 2. Which symbol is used to make a variable private in Python?

A. `#`
B. `_`
C. `__`
D. `@@`

**Answer:** C

---

### 3. What will happen if you try to access a private variable directly?

```python
class Test:
    def __init__(self):
        self.__x = 10

obj = Test()
print(obj.__x)
```

A. 10
B. None
C. Error
D. 0

**Answer:** C

---

### 4. Which method is used to access private data?

A. Constructor
B. Getter method
C. Destructor
D. Static method

**Answer:** B

---

### 5. What is the main purpose of encapsulation?

A. Increase execution speed
B. Protect data from unauthorized access
C. Reduce code length
D. Create loops

**Answer:** B ([Learn with Yasir][1])

---

### 6. Which of the following is a protected variable?

A. `name`
B. `_name`
C. `__name`
D. `#name`

**Answer:** B

---

### 7. Identify the correct output:

```python
class A:
    def __init__(self):
        self.__x = 5

    def get_x(self):
        return self.__x

obj = A()
print(obj.get_x())
```

A. Error
B. 0
C. 5
D. None

**Answer:** C

---

### 8. Encapsulation helps in:

A. Data hiding
B. Code reuse
C. Security
D. All of the above

**Answer:** D

---

### 9. Which of the following is TRUE about Python encapsulation?

A. It strictly enforces private access
B. It uses naming conventions
C. Private variables are globally accessible
D. No methods are used

**Answer:** B ([Learn with Yasir][1])

---

### 10. What will be the output?

```python
class Bank:
    def __init__(self):
        self.__balance = 100

    def deposit(self, amt):
        self.__balance += amt

    def get_balance(self):
        return self.__balance

b = Bank()
b.deposit(50)
print(b.get_balance())
```

A. 100
B. 150
C. Error
D. None

**Answer:** B

### 11. Identify the fix for the error

```python
class Student:
    def __init__(self):
        self.__marks = 90

obj = Student()
print(obj.__marks)
```

What is the correct fix?

A. Change `__marks` to `marks`
B. Access using `obj._Student__marks`
C. Remove class
D. Use `print(__marks)`

**Answer:** B

---

### 12. Fix the getter method issue

```python
class Test:
    def __init__(self):
        self.__x = 10

    def getx():
        return self.__x
```

What is the correction?

A. Add `self` parameter to `getx()`
B. Remove constructor
C. Make variable public
D. Use static method

**Answer:** A

---

### 13. Identify the problem

```python
class Bank:
    def __init__(self):
        self.__balance = 100

b = Bank()
b.__balance = 200
print(b.__balance)
```

What is the fix to correctly update balance?

A. Use `b._Bank__balance = 200`
B. No fix needed
C. Use `b.balance = 200`
D. Delete constructor

**Answer:** A

---

### 14. Fix method call

```python
class A:
    def __init__(self):
        self.__x = 5

    def get_x(self):
        return self.__x

obj = A
print(obj.get_x())
```

What is the correction?

A. Replace `obj = A()`
B. Remove method
C. Use static method
D. Use `__x` directly

**Answer:** A

---

### 15. Identify correct encapsulation practice

```python
class Car:
    def __init__(self):
        self.speed = 100
```

What should be done to encapsulate `speed`?

A. Change to `__speed`
B. Leave as is
C. Remove variable
D. Make global

**Answer:** A


---

[1]: https://yasirbhutta.github.io/python/docs/oop-encapsulation/?utm_source=chatgpt.com "Encapsulation in Python OOP: A Beginner’s Guide | Learn with Yasir"
[2]: https://www.geeksforgeeks.org/python/data-abstraction-in-python/?utm_source=chatgpt.com "Data Abstraction in Python - GeeksforGeeks"
[3]: https://www.boot.dev/blog/python/python-encapsulation-vs-abstraction/?utm_source=chatgpt.com "Python Encapsulation vs Abstraction: What Matters | Boot.dev"