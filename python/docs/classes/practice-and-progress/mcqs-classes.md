---
layout: default
title: Python Classes MCQs: Test Your Knowledge of Object-Oriented Programming.
description: Challenge your understanding of Python classes with these multiple-choice questions. Perfect for beginners to practice key concepts like class creation, object instances, constructors, and methods in Python.
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
