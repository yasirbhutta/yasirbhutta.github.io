---
layout: page
title: Python abstraction MCQs – Test Your OOP Knowledge
description: Challenge your understanding of Python's Object-Oriented Programming with these multiple-choice questions on abstraction. Ideal for beginners, students, and job seekers to reinforce key OOP concepts.
keywords: python abstraction, oop in python, python mcqs, abstraction quiz, python multiple choice questions, learn with yasir, yasirbhutta, python classes, python access modifiers, python getter setter, python name mangling, python oop practice, python abstraction tutorial
author: Muhammad Yasir Bhutta
toc: toc/python.html
topic: "oop-abstraction"
course: "python"
prev: /python/docs/oop-abstraction/practice-and-progress/fill-blanks-oop-abstraction.html
next: /python/docs/oop-abstraction/practice-and-progress/find-fix-mistakes-oop-abstraction.html
---

{% assign topic_name = "oop-abstraction" %}
{% assign topics = site.data.python.mcqs.topics %}
{% assign selected_topic = topics | where: "topic", topic_name | first %}
{% assign mcqs = selected_topic.questions %}
{% assign resources = selected_topic.resources %}
{% include pap/mcqs-loop.html mcqs=mcqs resources=resources %}

## More ...

### 1. What is abstraction in Python?

A. Hiding unnecessary details and showing only essential features
B. Combining variables
C. Using loops
D. Creating objects

**Answer:** A ([GeeksforGeeks][2])

---

### 2. Which module is used for abstraction in Python?

A. math
B. sys
C. abc
D. os

**Answer:** C

---

### 3. What is an Abstract Base Class (ABC)?

A. A class with no methods
B. A class that cannot be instantiated directly
C. A normal class
D. A private class

**Answer:** B ([GeeksforGeeks][2])

---

### 4. Which decorator is used for abstract methods?

A. @staticmethod
B. @classmethod
C. @abstractmethod
D. @property

**Answer:** C

---

### 5. Identify the output:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 100

obj = Circle()
print(obj.area())
```

A. Error
B. 0
C. 100
D. None

**Answer:** C

---

### 6. What is the main benefit of abstraction?

A. Faster execution
B. Simplicity by hiding complexity
C. More memory usage
D. Redundant code

**Answer:** B ([GeeksforGeeks][2])

---

### 7. Which statement is TRUE about abstraction?

A. Shows internal logic
B. Hides implementation details
C. Removes methods
D. Only works with loops

**Answer:** B

---

### 8. What will happen if a subclass does not implement abstract methods?

A. Runs successfully
B. Gives warning
C. Raises error
D. Returns None

**Answer:** C

---

### 9. Which real-life example best represents abstraction?

A. Writing code
B. ATM machine interface
C. Variable declaration
D. Loop execution

**Answer:** B

---

### 10. Encapsulation vs Abstraction — which is correct?

A. Both are same
B. Encapsulation hides data, abstraction hides implementation
C. Encapsulation shows details
D. Abstraction exposes everything

**Answer:** B ([Boot.dev][3])


### 16. Fix missing import

```python
class Shape(ABC):
    def area(self):
        pass
```

What is missing?

A. `from abc import ABC`
B. `import math`
C. `import sys`
D. Nothing

**Answer:** A

---

### 17. Fix abstract method declaration

```python
from abc import ABC

class Shape(ABC):
    def area(self):
        pass
```

What is the correction?

A. Add `@abstractmethod`
B. Remove class
C. Add constructor
D. Use static method

**Answer:** A

---

### 18. Identify error in subclass

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    pass

obj = Circle()
```

What is the fix?

A. Implement `area()` in `Circle`
B. Remove ABC
C. Add constructor
D. Use private method

**Answer:** A

---

### 19. Fix incorrect decorator usage

```python
from abc import ABC, abstractmethod

class A(ABC):
    @abstract
    def show(self):
        pass
```

What is the correction?

A. Replace `@abstract` with `@abstractmethod`
B. Remove decorator
C. Add constructor
D. Use `@staticmethod`

**Answer:** A

### 20. Fix instantiation issue

```python
from abc import ABC, abstractmethod

class Test(ABC):
    @abstractmethod
    def show(self):
        pass

obj = Test()
```

What is the fix?

A. Create subclass and implement method
B. Remove ABC
C. Add variable
D. Use static method

**Answer:** A

# 🔥 Mixed Concept (Encapsulation + Abstraction)

### 21. Fix access issue

```python
class A:
    def __init__(self):
        self.__x = 10

class B(A):
    def show(self):
        print(self.__x)
```

What is the fix?

A. Use `self._A__x`
B. Make variable global
C. Remove class
D. Use static method

**Answer:** A

---

### 22. Fix abstract + encapsulation

```python
from abc import ABC, abstractmethod

class Bank(ABC):
    def __init__(self):
        self.__balance = 100

    @abstractmethod
    def get_balance(self):
        pass

class ATM(Bank):
    pass

obj = ATM()
```

What is the fix?

A. Implement `get_balance()` in ATM
B. Remove constructor
C. Make variable public
D. Delete abstract method

**Answer:** A


---

[1]: https://yasirbhutta.github.io/python/docs/oop-encapsulation/ "Encapsulation in Python OOP: A Beginner’s Guide | Learn with Yasir"
[2]: https://www.geeksforgeeks.org/python/data-abstraction-in-python/ "Data Abstraction in Python - GeeksforGeeks"
[3]: https://www.boot.dev/blog/python/python-encapsulation-vs-abstraction/ "Python Encapsulation vs Abstraction: What Matters | Boot.dev"



