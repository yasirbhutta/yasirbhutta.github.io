---
layout: page
title: "Understanding Python Multiple Inheritance: Concepts, MRO, and Examples"
description: "Learn about Python multiple inheritance, including syntax, the Method Resolution Order (MRO), the Diamond Problem, and practical use cases like Mixins."
keywords: "python multiple inheritance, python mro, python mixins, diamond problem, python oop"
---
Yes, Python supports **multiple inheritance**, where a child class can inherit from multiple parent classes. Here's a breakdown:

---

### Key Concepts:
1. **Syntax**:
   ```python
   class Parent1:
       def method1(self):
           print("Parent1 method")

   class Parent2:
       def method2(self):
           print("Parent2 method")

   class Child(Parent1, Parent2):  # Inherits from Parent1 and Parent2
       pass

   obj = Child()
   obj.method1()  # Output: Parent1 method
   obj.method2()  # Output: Parent2 method
   ```

2. **Method Resolution Order (MRO)**:
   - Python uses the **C3 linearization algorithm** to resolve conflicts when methods/attributes have the same name in multiple parents.
   - The order of parent classes matters (e.g., `Child(Parent1, Parent2)` vs. `Child(Parent2, Parent1)`).
   - View MRO with `Child.__mro__` or `Child.mro()`.

3. **Diamond Problem**:
   - Occurs when a class inherits from two classes that themselves inherit from a common base class.
   - Example:
     ```python
     class A:
         def greet(self):
             print("A")
     class B(A):
         def greet(self):
             print("B")
     class C(A):
         def greet(self):
             print("C")
     class D(B, C):
         pass

     d = D()
     d.greet()  # Output: B (due to MRO: D -> B -> C -> A)
     ```

4. **Practical Use Cases**:
   - **Mixins**: Small reusable classes that add specific features (e.g., logging, serialization).
   - Example:
     ```python
     class JSONMixin:
         def to_json(self):
             import json
             return json.dumps(self.__dict__)

     class User(JSONMixin):
         def __init__(self, name):
             self.name = name

     u = User("Alice")
     print(u.to_json())  # Output: {"name": "Alice"}
     ```

---

### Why Use Multiple Inheritance?
- ✅ Combine features from multiple classes.
- ✅ Avoid code duplication via mixins.
- 🚫 Use sparingly to avoid complexity (favor composition over inheritance if possible).

---

### Example of Method Conflict:
```python
class Father:
    def skill(self):
        print("Cooking")

class Mother:
    def skill(self):
        print("Programming")

class Child(Father, Mother):  # Father's method takes priority
    pass

c = Child()
c.skill()  # Output: Cooking (due to MRO)
```

---

In Python, multiple inheritance is powerful but requires careful design to avoid ambiguity! 🐍