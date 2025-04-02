# Object-Oriented Programming in Python (OOP): Tutorial

## Contents
### Start with the Basics
#### Introduction to OOP
OOP: Introduction
OOP Example
Object Oriented Programming in Python
Is Python Object Oriented?

#### Classes & Objects
How to create a class
Instantiating objects
Adding attributes to a class
Define methods in a class
Passing arguments to methods
Python OOP Example
Object-Oriented Programming in Python: Wrap-Up
#### Methods in Classes
### Core OOP Concepts
#### a. Encapsulation
#### b. Inheritance
#### c. Polymorphism
#### d. Abstraction and Interfaces
### 3. Advanced Topics
#### a. Magic Methods (`__str__`, `__eq__`, etc.)
#### b. Composition over Inheritance
#### c. Class Methods & Static Methods
### 4. OOP Best Practices
### 5. Project: Inventory Management System


---

### **1. Start with the Basics**
#### **a. Classes & Objects**
- **Class**: A template for creating objects (e.g., `Car`).
- **Object**: An instance of a class (e.g., `my_car = Car()`).

**Example**:
```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Instance attribute
        self.model = model

    def drive(self):
        return f"{self.brand} {self.model} is driving!"

# Create an object
my_car = Car("Tesla", "Model S")
print(my_car.drive())  # Output: "Tesla Model S is driving!"
```

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

#### **b. Inheritance**
- Create child classes that inherit from parent classes.

**Example**:
```python
class Animal:
    def speak(self):
        return "Sound"

class Cat(Animal):
    def speak(self):  # Method overriding
        return "Meow"

class Dog(Animal):
    def speak(self):
        return "Woof"

animals = [Cat(), Dog()]
for animal in animals:
    print(animal.speak())  # Output: "Meow", "Woof"
```

---

#### **c. Polymorphism**
- Different classes can share the same method name but behave uniquely.

**Example**:
```python
class Rectangle:
    def area(self, length, width):
        return length * width

class Circle:
    def area(self, radius):
        return 3.14 * radius ** 2

# Both classes have an `area` method, but work differently
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