---
layout: page
title: Find and Fix Mistakes – Python Inheritance Practice Questions.
description: Practice Python OOP inheritance by identifying and fixing common mistakes in code examples.
keywords: python, oop, inheritance, practice questions, find and fix, error correction
author: Muhammad Yasir Bhutta.
---

### **1. Question:**
```python
class Father:
    def __init__(self, name):
        name = name

class Child(Father):
    pass

c = Child("Ali")
print(c.name)
```

**What’s the mistake? How would you fix it?**

**Mistake:**  
The `name` parameter is assigned to itself; it should be assigned to an instance variable.

**Fix:**  
```python
class Father:
    def __init__(self, name):
        self.name = name
```

---

### **2. Question:**
```python
class Animal:
    def sound():
        print("Some sound")

class Dog(Animal):
    pass

d = Dog()
d.sound()
```

**What’s the mistake? How would you fix it?**

**Mistake:**  
The `sound` method is missing the `self` parameter.

**Fix:**  
```python
class Animal:
    def sound(self):
        print("Some sound")
```

---

### **3. Question:**
```python
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, school):
        self.school = school
```

**What’s the mistake? How would you fix it?**

**Mistake:**  
The `Student` class overrides the constructor without calling the parent’s constructor.

**Fix:**  
```python
class Student(Person):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school
```

---

### **4. Question:**
```python
class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

obj = A()
obj.show()
```

**Mistake Prompt:**  
Change the code so that an object of `B` calls the `show` method of `A`.

**Fix:**  
Use `super()` or explicitly call `A.show(self)` inside class B:
```python
class B(A):
    def show(self):
        super().show()
```

Here are 10 Python inheritance code questions with intentional mistakes. Learners need to identify/fix the errors:

---

**Q1: Missing Super Initialization**  
```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, model):
        self.model = model  # Error: Forgot super().__init__

car = Car("Tesla", "Model S")  # Throws error
```
**Error:** `Car` doesn't call `Vehicle.__init__`  
**Fix:** Add `super().__init__(brand)` in `Car.__init__`

---

**Q2: Method Override Gone Wrong**  
```python
class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):
        print("Child method")  # Error: Parent method not called

child = Child()
child.show()  # Only shows "Child method"
```
**Error:** Parent method not preserved  
**Fix:** Add `super().show()` in Child's `show()`

---

**Q3: Multiple Inheritance MRO Confusion**  
```python
class Parent1:
    def display(self):
        print("Parent1")

class Parent2:
    def display(self):
        print("Parent2")

class Child(Parent1, Parent2):
    pass  # Which display() is called?

obj = Child()
obj.display()  # Outputs "Parent1" - is this intended?
```
**Mistake:** Parent order might be unexpected  
**Test:** Change inheritance order to `(Parent2, Parent1)`

---

**Q4: Private Variable Access**  
```python
class Base:
    def __init__(self):
        self.__secret = 123  # Name mangled

class Derived(Base):
    def get_secret(self):
        return self.__secret  # Error: AttributeError

d = Derived()
print(d.get_secret())
```
**Error:** Can't access `__secret` directly in subclass  
**Fix:** Use `_Base__secret` or make it protected (`_secret`)

---

**Q5: Inheritance vs Composition**  
```python
class Engine:
    def start(self):
        print("Engine started")

class Car(Engine):  # Bad inheritance
    def drive(self):
        self.start()

car = Car()
car.drive()  # Works but poor design
```
**Mistake:** `Car` isn't an `Engine` subtype  
**Fix:** Use composition (`self.engine = Engine()`)

---

**Q6: Static Method Inheritance**  
```python
class MathOps:
    @staticmethod
    def add(a, b):
        return a + b

class AdvancedMath(MathOps):
    def add(a, b, c):  # Missing @staticmethod
        return a + b + c

result = AdvancedMath.add(1, 2, 3)  # TypeError
```
**Error:** Forgot `@staticmethod` decorator  
**Fix:** Add `@staticmethod` above `AdvancedMath.add`

---

**Q7: Diamond Problem in Python**  
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
**Test:** Analyze MRO with `print(D.__mro__)`

---

**Q8: Property Override Failure**  
```python
class Account:
    @property
    def balance(self):
        return self._balance

class Savings(Account):
    def balance(self):  # Forgot @property
        return self._balance * 1.05  # Broken

sa = Savings()
sa.balance  # Throws AttributeError
```
**Error:** `balance` becomes method, not property  
**Fix:** Add `@property` decorator in `Savings`

---

**Q9: Parent Argument Mismatch**  
```python
class Shape:
    def __init__(self, color):
        self.color = color

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()  # Error: Missing color arg
        self.radius = radius

c = Circle("red", 5)  # TypeError
```
**Fix:** `super().__init__(color)` + adjust parameters

---

**Q10: Inheriting Non-Class**  
```python
name = "BaseClass"

class MyClass(name):  # Error: 'str' is not a class
    pass
```
**Mistake:** Trying to inherit from string  
**Fix:** Inherit from proper base class (e.g., `object`)

