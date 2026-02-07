---
layout: page
title: Python Classes MCQs - Test Your Knowledge of Object-Oriented Programming.
description: Challenge your understanding of Python classes with these multiple-choice questions. Perfect for beginners to practice key concepts like class creation, object instances, constructors, and methods in Python.
keywords: "class, name, self, object, instance, dog, print, init"
toc: toc/python.html
topic: "classes"
course: "python"
prev: /python/docs/classes/practice-and-progress/fill-blanks-classes.html
next: /python/docs/classes/practice-and-progress/find-fix-mistakes-classes.html
---
# Multiple-Choice Questions (MCQs)

1. **What keyword is used to define a class in Python?**
   - A) object
   - B) class
   - C) define
   - D) declare

**Watch this video for the answer:** [https://youtu.be/zVYzk_gnTY4](https://youtu.be/zVYzk_gnTY4)

2. **What is the correct way to create a class in Python?**
    - A) class MyClass: 
    - B) create MyClass: 
    - C) define MyClass: 
    - D) new MyClass:

Answer: a) class MyClass:

3. **What is the correct way to create an object instance of a class?**
   - A) Calling the class definition directly
   - B) Assigning the class name to a variable
   - C) Using the new keyword
   - D) Calling the class name with parentheses

4. **What will be the output?**

```python
class Dog:
  name = "Unknown"

  def bark(self):
    print("Woof!")

dog1 = Dog()
dog1.name = "Buddy"
dog2 = Dog()

print(dog1.name, dog2.name)
```

   - A) Buddy Unknown
   - B) Unknown Unknown
   - C) Buddy Buddy
   - D) It depends on the dog breed
  
5. **What is the purpose of the self parameter in a method?**
   - A) To store the method name
   - B) To refer to the current object instance
   - C) To pass data to other methods
   - D) All of the above

6. **What is the primary purpose of a class constructor?**
   - A) To define the name of the class
   - B) To initialize the object's data members
   - C) To allocate memory for the object
   - D) All of the above

7. **What is the purpose of the __init__ method in a Python class?**
    - A) To define static properties
    - B) To store the object's type
    - C) To initialize the object's attributes
    - D) To compare objects for equality
  
8. **What will be the output of the following code?**

```python
class Test:
    def __init__(self, x):
        self.x = x

t = Test(5)
print(t.x)
```
   - A) Error
   - B) 0
   - C) 5
   - D) None
  
9. Which keyword is used to create an object of a class?
   -  A) object
   -  B) new
   -  C) self
   -  D) No keyword is needed

10. **Identify the class attribute in the following code:**

```python
class Dog:
    species = "Canis familiaris"
    
    def __init__(self, name):
        self.name = name

d = Dog("Buddy")
```
    - A) `name`  
    - B) `species`  
    - C) `__init__`  
    - D) `Dog`

11. **What will be the output of the following code?**

```python
class Car:
    wheels = 4  # Class attribute

    def __init__(self, color):
        self.color = color  # Instance attribute

car1 = Car("Red")
car2 = Car("Blue")
Car.wheels = 6

print(car1.wheels)
print(car2.wheels)
```

- **A)**
```
4
4
```

**B)**
```
6
6
```

**C)**
```
4
6
```

**D)**
Error

12. **Which of the following statements is true?**
    - A) Instance attributes are shared across all instances.  
    - B) Class attributes can only be accessed through class name.  
    - C) Class attributes are shared across all instances.  
    - D) Instance attributes are defined outside the `__init__` method.

> **Correct Answer:** **C.**  
> **Explanation:** Class attributes are shared across all instances. Instance attributes are unique to each object.

---

13. **What happens if an instance modifies a class attribute?**

```python
class Item:
    category = "Grocery"

    def __init__(self, name):
        self.name = name

item1 = Item("Soap")
item1.category = "Cosmetic"

print(Item.category)
print(item1.category)
```

**A)**
```
Grocery
Cosmetic
```

**B)**
```
Cosmetic
Cosmetic
```

**C)**
```
Cosmetic
Grocery
```

**D)**
Error

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1602443888929206"
     crossorigin="anonymous"></script>
<ins class="adsbygoogle"
     style="display:block"
     data-ad-format="autorelaxed"
     data-ad-client="ca-pub-1602443888929206"
     data-ad-slot="7879511511"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
