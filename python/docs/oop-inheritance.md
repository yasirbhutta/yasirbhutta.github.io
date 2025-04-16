---
title: Inheritance in Python - Beginner's Guide with Examples  
description: Learn inheritance in Python with this beginner-friendly guide. Understand parent and child classes, method overriding, `super()`, and multilevel inheritance with examples. Perfect for Python learners to master object-oriented programming.  
keywords: Python inheritance tutorial, Python OOP inheritance, parent and child classes in Python, method overriding in Python, Python `super()` example, multilevel inheritance Python, Python OOP basics, Python programming for beginners, Python class inheritance examples
layout: page
---

## 🔷 What is Inheritance?

**Inheritance** is a way to create a new class from an existing class.  
It helps us **reuse code**, **extend functionality**, and follow the **DRY (Don't Repeat Yourself)** principle.

### ✅ Key Points:
- The **base class** (or parent class) contains common features.
- The **derived class** (or child class) inherits from the base class and can:
  - Use parent’s methods and attributes
  - Add its own attributes and methods
  - Modify (override) methods from the parent class.

Think of inheritance like a family tree. A child inherits traits (methods and attributes) from their parents, but they can also have their own unique traits.

---

## 🔹 1. Creating a Parent Class

```python
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hi, I'm {self.name}")
```

### 🔍 Explanation:
- `__init__` is the constructor; it runs when the object is created.
- `introduce()` is a method that prints a greeting.

---

## 🔹 2. Creating a Child Class (Inheritance)

```python
class Student(Person):
    pass
```

### 🔍 Explanation:
- `Student` class inherits from `Person` using `(Person)`.
- `pass` means no additional code — it still works because it inherits from `Person`.

```python
s = Student("Ali")
s.introduce()  # Output: Hi, I'm Ali
```

---

## 🔹 3. Adding New Methods to the Child Class

```python
class Student(Person):
    def study(self):
        print(f"{self.name} is studying.")
```

```python
s = Student("Bob")
s.introduce()  # Inherited from Person
s.study()      # Defined in Student
```

---

## 🔹 4. Overriding Methods

You can **change** how a method works in the child class.

```python
class Student(Person):
    def introduce(self):  # Overriding the method
        print(f"Hello, I'm student {self.name}")
```

```python
s = Student("Ahmad")
s.introduce()  # Output: Hello, I'm student Ahmad
```

---

## 🔹 5. Using `super()` to Call the Parent Method

If you override a method, but still want to use the original version from the parent, use `super()`.

```python
class Student(Person):
    def introduce(self):
        super().introduce()  # Call Person's version
        print("I'm also a student.")
```

```python
s = Student("Hamza")
s.introduce()
# Output:
# Hi, I'm Hamza
# I'm also a student.
```

---

## 🔹 6. Multilevel Inheritance (Optional)

```python
class Person:
    def speak(self):
        print("Person speaks")

class Student(Person):
    def study(self):
        print("Student studies")

class GraduateStudent(Student):
    def research(self):
        print("Graduate student does research")

g = GraduateStudent()
g.speak()
g.study()
g.research()
```

### 🔍 Multilevel Inheritance Diagram:
Person (Parent Class)
    ↳ Student (Child Class)
        ↳ GraduateStudent (Grandchild Class)

## 🧠 Summary

| Concept        | Description                                         |
|----------------|-----------------------------------------------------|
| `class Child(Parent)` | Defines a new class that inherits from Parent   |
| `super()`      | Calls a method from the parent class                |
| Method override| Redefine a parent method in the child class         |
| Reusability    | Inheritance helps reuse code and reduce repetition |

---

## Common Mistakes to Avoid
- Forgetting to use `self` in methods.
- Not calling the parent class's `__init__` method when overriding it.
- Overriding a method but forgetting to use `super()` if needed.
