---
layout: page
title: Multiple Choice Questions (MCQs) on polymorphism in Python – OOP Practice
description: Boost your Python skills with these MCQs on Object-Oriented Programming and polymorphism. Ideal for beginners, students, and job seekers to test and strengthen their understanding of Python OOP concepts.
keywords: Python polymorphism MCQs, OOP MCQ Python, multiple choice questions Python polymorphism, Python class and object quiz, object oriented programming Python MCQs, Python OOP practice test, Python polymorphism quiz questions, Python interview questions OOP, Python MCQ with answers, polymorphism concepts in Python
author: Muhammad Yasir Bhutta
toc: toc/python.html
topic: "oop-polymorphism"
course: "python"
prev: /python/docs/oop-polymorphism/practice-and-progress/true-false-oop-polymorphism.html
next: /python/docs/oop-polymorphism/practice-and-progress/find-fix-mistakes-oop-polymorphism.html
---

{% assign topic_name = "oop-polymorphism" %}
{% assign topics = site.data.python.mcqs.topics %}
{% assign selected_topic = topics | where: "topic", topic_name | first %}
{% assign mcqs = selected_topic.questions %}
{% assign resources = selected_topic.resources %}
{% include pap/mcqs-loop.html mcqs=mcqs resources=resources %}

## More ...

## 🔹 Basic Concepts

### 1. What does polymorphism mean in Python?

A. One function performing one task
B. One object having one form
C. Same method behaving differently for different objects
D. Different methods behaving same

**Answer:** C
**Explanation:** Polymorphism means “many forms,” allowing the same method to behave differently depending on the object. ([GeeksforGeeks][1])

---

### 2. Which of the following best describes polymorphism?

A. Data hiding
B. Code duplication
C. Same interface, different implementation
D. Function recursion

**Answer:** C

---

### 3. What is the main benefit of polymorphism?

A. Increases code complexity
B. Reduces code reuse
C. Improves flexibility and reusability
D. Removes inheritance

**Answer:** C ([Learn with Yasir][2])

---

## 🔹 Method Overriding

### 4. What is method overriding?

A. Defining multiple methods with same name
B. Changing method name in child class
C. Redefining parent class method in child class
D. Deleting parent method

**Answer:** C ([Learn with Yasir][2])

---

### 5. What will be the output?

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

obj = Dog()
obj.speak()
```

A. Animal speaks
B. Dog barks
C. Error
D. None

**Answer:** B

---

### 6. Which concept allows subclasses to provide specific implementations?

A. Encapsulation
B. Abstraction
C. Method Overriding
D. Inheritance

**Answer:** C

---

## 🔹 Duck Typing

### 7. What is duck typing in Python?

A. Checking object type explicitly
B. Ignoring object behavior
C. Focusing on object behavior instead of type
D. Using only built-in functions

**Answer:** C ([Learn with Yasir][2])

---

### 8. What will be the output?

```python
class A:
    def show(self):
        print("A")

class B:
    def show(self):
        print("B")

def display(obj):
    obj.show()

display(A())
display(B())
```

A. A B
B. B A
C. Error
D. None

**Answer:** A

---

### 9. Duck typing follows which principle?

A. Type checking
B. Behavior checking
C. Memory allocation
D. Compilation

**Answer:** B

---

## 🔹 Operator Overloading

### 10. What is operator overloading?

A. Using operators incorrectly
B. Redefining operators for user-defined classes
C. Removing operators
D. Limiting operators

**Answer:** B ([Learn with Yasir][2])

---

### 11. Which method is used to overload the `+` operator?

A. **sum**()
B. **add**()
C. **plus**()
D. **concat**()

**Answer:** B

---

### 12. What will be the output?

```python
class Test:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return Test(self.x + other.x)

t1 = Test(2)
t2 = Test(3)
t3 = t1 + t2
print(t3.x)
```

A. 5
B. 6
C. Error
D. None

**Answer:** A

---

## 🔹 Real-World Polymorphism

### 13. In a payment system, different payment types use the same method:

```python
process_payment()
```

This is an example of:
A. Encapsulation
B. Polymorphism
C. Inheritance
D. Abstraction

**Answer:** B ([Learn with Yasir][2])

---

### 14. What is the advantage of using a common method like `process_payment()`?

A. Reduces flexibility
B. Requires type checking
C. Allows different implementations
D. Removes classes

**Answer:** C

---

## 🔹 Advanced Concepts

### 15. Python does not support traditional method overloading, but it can be achieved using:

A. Loops
B. Default arguments
C. Inheritance
D. Recursion

**Answer:** B ([Learn with Yasir][2])

---

### 16. What will be the output?

```python
def double(x):
    return x * 2

print(double("Hi"))
```

A. Hi
B. HiHi
C. Error
D. 2Hi

**Answer:** B ([Learn with Yasir][2])

---

### 17. Which of the following shows polymorphism with built-in types?

A. int + int
B. str + str
C. list + list
D. All of the above

**Answer:** D

---

### 18. Which concept allows calling methods without knowing the exact object type?

A. Abstraction
B. Polymorphism
C. Encapsulation
D. Composition

**Answer:** B ([Learn with Yasir][2])

---

### 19. Which of the following is NOT a type of polymorphism in Python?

A. Method Overriding
B. Duck Typing
C. Operator Overloading
D. Function Compilation

**Answer:** D

---

### 20. What is the output?

```python
class Bird:
    def move(self):
        print("Flying")

class Car:
    def move(self):
        print("Driving")

def travel(obj):
    obj.move()

travel(Bird())
travel(Car())
```

A. Flying Driving
B. Driving Flying
C. Error
D. None

**Answer:** A

---

[1]: https://www.geeksforgeeks.org/python/polymorphism-in-python/?utm_source=chatgpt.com "Polymorphism in Python - GeeksforGeeks"
[2]: https://yasirbhutta.github.io/python/docs/oop-polymorphism/?utm_source=chatgpt.com "Python Polymorphism Explained – Types & Examples (OOP Guide) | Learn with Yasir"
