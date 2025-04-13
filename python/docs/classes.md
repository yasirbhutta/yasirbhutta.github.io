---
layout: default
title: Object-Oriented Programming in Python (OOP) - Tutorial
description: Learn Python programming from scratch with our free, beginner-friendly tutorials. Access open-source content, download PDF lessons, and start coding today!
---

# Classes and Objects in Python

## Contents:

1. **Introduction to Classes & Objects**  
   - What is a class? (Blueprint for objects)  
   - What is an object? (Instance of a class)  

2. **How to Create a Class**  
   - Basic syntax: `class MyClass:`  
   - Naming conventions (PascalCase).  

3. **The `__init__` Method (Constructor)**  
   - Purpose: Initialize object attributes.  
   - Syntax: `def __init__(self, ...)`  

4. **The `self` Keyword** *(Explain early—it’s everywhere!)*  
   - What is `self`? (Reference to the instance).  
   - Why it’s needed (access attributes/methods).  

5. **Instantiating Objects**  
   - How to create an object: `obj = MyClass()`.  
   - How `__init__` is called automatically.  

6. **Adding Attributes to a Class**  
   - Instance attributes (per-object, e.g., `self.name = name`).  
   - Class attributes (shared, e.g., `class_var = 0`).  
   - **Class vs. Instance Variables** (Compare them here).  

7. **Defining Methods in a Class**  
   - What are methods? (Functions inside a class).  
   - Example: `def greet(self): print("Hello!")`.  

8. **Passing Arguments to Methods**  
   - Methods with parameters: `def set_age(self, age):`.  
   - Default arguments (e.g., `def __init__(self, name="Anonymous")`).  

9. **Practical OOP Examples** *(Apply all concepts!)*  
   - Example 1: A `Dog` class with `name`, `breed`, `bark()`.  
   - Example 2: A `Car` class with `make`, `model`, `year`, and `describe()`.  
   - Example 3: A `Student` class with `name`, `age`, `grade` simple  
   - Example 4: A `BankAccount` class with `balance`, `deposit()`, and `withdraw()`.  
   - Example 5: A `Student` class with `name`, `age`, `grade`, and methods like `introduce()`.

their name, age, and grade.
---

## **1. Introduction to Classes & Objects**  
### **Class**  
- A **class** is a blueprint for creating objects.  
- Defines the structure (attributes & methods) that objects will have.  
- Example: A `Car` class defines properties like `color`, `model`, and actions like `drive()`.  

### **Object**  
- An **object** is an instance of a class.  
- Created from the class blueprint.  
- Example: A `Toyota` car (object) created from the `Car` class.  

---  

## **2. How to Create a Class**  
### **Syntax**  
```python  
class ClassName:  
    # Attributes & methods go here  
```  
- **Naming Convention**: Use **PascalCase** (e.g., `MyClass`, `BankAccount`).  

---  

## **3. The `__init__` Method (Constructor)**  
### **Purpose**  
- Automatically called when an object is created.  
- Used to **initialize attributes** (set initial values).  

### **Syntax**  
```python  
def __init__(self, param1, param2):  
    self.attribute1 = param1  
    self.attribute2 = param2  
```  
- Example:  
```python  
class Dog:  
    def __init__(self, name):  
        self.name = name  # Initialize 'name' attribute  
```  

---  

## **4. The `self` Keyword**  
### **What is `self`?**  
- Refers to the **current instance** of the class.  
- Used to access attributes & methods inside the class.  

### **Why is it needed?**  
- Without `self`, Python wouldn’t know which object’s attributes to modify.  
- Example:  
```python  
class Dog:  
    def __init__(self, name):  
        self.name = name  # 'self.name' belongs to this Dog object  
```  

---  

## **5. Instantiating Objects**  
### **How to Create an Object**  
```python  
object_name = ClassName(arguments)  
```  
- Example:  
```python  
my_dog = Dog("Buddy")  # Calls __init__ automatically  
```  

---  

## **6. Adding Attributes to a Class**  
### **Instance Attributes**  
- Unique to each instance (object) of a class.  
- Store data specific to that object. 
- Defined within the `__init__` constructor method, using the `self` parameter.

```python  
class Dog:  
    def __init__(self, name):  
        self.name = name  # Instance attribute  
```  

### **Class Attributes**  
- Shared by all objects of the class.  
- Defined outside `__init__`.  
```python  
class Dog:  
    species = "Canine"  # Class attribute (shared)  
```  

### **Class vs. Instance Attributes**  
| Feature       | Class Attribute | Instance Attribute |  
|--------------|----------------|-------------------|  
| **Scope**    | Shared by all objects | Unique per object |  
| **Defined**  | Outside `__init__` | Inside `__init__` |  

---  

## **7. Defining Methods in a Class**  
### **What are Methods?**  
- Functions defined inside a class.  
- Must take `self` as the first parameter.  

### **Example**  
```python  
class Dog:  
    def bark(self):  
        print("Woof!")  

my_dog = Dog()  
my_dog.bark()  # Output: "Woof!"  
```  

---  

## **8. Passing Arguments to Methods**  
### **Methods with Parameters**  
```python  
class Dog:  
    def set_age(self, age):  
        self.age = age  

my_dog = Dog()  
my_dog.set_age(3)  # Sets age to 3  
```  

### **Default Arguments**  
```python  
class Dog:  
    def __init__(self, name="Unknown"):  
        self.name = name  

dog1 = Dog()          # name = "Unknown"  
dog2 = Dog("Buddy")   # name = "Buddy"  
```  

---  

## **9. Practical OOP Examples**  
### **Example 1: `Dog` Class**  
```python  
class Dog:  
    species = "Canine"  # Class attribute  

    def __init__(self, name, breed):  
        self.name = name   # Instance attribute  
        self.breed = breed  

    def bark(self):  
        print(f"{self.name} says Woof!")  

# Create objects  
dog1 = Dog("Buddy", "Labrador")  
dog2 = Dog("Max", "Beagle")  

dog1.bark()  # Output: "Buddy says Woof!"  
```  

### **Example 2: `Car` Class**  

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe(self):
        print(f"{self.year} {self.make} {self.model}")

my_car = Car("Toyota", "Corolla", 2020)
my_car.describe()  # Output: 2020 Toyota Corolla
```

### **Example 3: `Student` Class**  

```python
# Class Definition
class Student:
    # Constructor
    def __init__(self, name, age, grade): # self refers to the current object being created.
        self.name = name
        self.age = age
        self.grade = grade
    # Method
    def info(self):
        print(f"Name = {self.name} Age = {self.age} Grade = {self.grade}")

# Object Creation

student1 = Student("Hamza", 8, 3)
student2 = Student("Muhammad", 15, 10)

# Accessing Attributes and Methods

print(student1.name)
student1.info()
student2.info()
```

### **Example 4: `BankAccount` Class**  
```python  
class BankAccount:  
    def __init__(self, balance=0):  
        self.balance = balance  

    def deposit(self, amount):  
        self.balance += amount  

    def withdraw(self, amount):  
        if amount <= self.balance:  
            self.balance -= amount  
        else:  
            print("Insufficient funds!")  

# Usage  
account = BankAccount(100)  
account.deposit(50)  
account.withdraw(30)  
print(account.balance)  # Output: 120  
```  

### **Example 5: `Student` Class** 
Represents a student with their name, age, and grade.

```python
class Student:

    def __init__(self, name, age, grade):
        """Initializes a Student object with the given attributes."""
        self.name = name
        self.age = age
        self.grade = grade

    def get_name(self):
        """Returns the student's name."""
        return self.name

    def get_age(self):
        """Returns the student's age."""
        return self.age

    def get_grade(self):
        """Returns the student's grade."""
        return self.grade

    def set_grade(self, new_grade):
        """Updates the student's grade."""
        self.grade = new_grade

    def introduce(self):
        """Prints a self-introduction message."""
        print("Hello, my name is", self.name, "and I'm in grade", self.grade)

# Example usage
student1 = Student("Hamza", 8, 3)
student2 = Student("Muhammad", 16, 10)

student1.introduce()  # Output: Hello, my name is Alice and I'm in grade 9
print(student2.get_name())  # Output: Bob
student2.set_grade(11)
print(student2.get_grade())  # Output: 11
```

**Python Tutorial in Urdu: How to Create a Class**

<div class="yt-video">
<iframe src="https://www.youtube.com/embed/zVYzk_gnTY4?si=jUf1_YFa3zgVGyR5" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

**Python Tutorial: Python Classes - What is Class Constructor**

<div class="yt-short">
<iframe src="https://www.youtube.com/embed/eeat2bsZFL0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

**Python Tutorial in Urdu: How to Create Classes and Instance Attributes**

<div class="yt-video">
<iframe src="https://www.youtube.com/embed/tNARiqDveP4?si=8l9lXAgnyWARiqWl" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

{% assign topic = "classes" %}
{% include practice-and-progress.html topic=topic %}

## References and Bibliography

- [Classes - Python documentation](https://docs.python.org/3/tutorial/classes.html)
- [Python Attributes – Class and Instance Attribute Examples - freecodecamp.org](https://www.freecodecamp.org/news/python-attributes-class-and-instance-attribute-examples/)

