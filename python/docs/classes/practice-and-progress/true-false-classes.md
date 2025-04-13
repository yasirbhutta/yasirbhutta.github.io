---
layout: true-false
title: Python Classes True or False Practice.
description: Test your knowledge of Python classes and objects with these fill-in-the-blank exercises. Learn key concepts like attributes, methods, and the __init__ method with answers provided for self-assessment.
keywords: "python classes quiz, true or false python classes, python objects practice, python __init__ method quiz, python attributes and methods, python class attributes vs instance attributes, python self parameter, python beginner classes quiz, python classes and objects exercises, python true or false questions"
difficulty:
  beginner: true
  intermediate: false
  advanced: false
topic: Classes and Objects
questions:
    - In Python, you create a class using the class keyword.  
    - The `__init__` method is called automatically when a new object is created.
    - Instance attributes are shared across all objects of a class.
    - The `self` parameter is used to refer to the current instance of the class
    - Class attributes are defined inside the constructor using the `self` parameter.
    - Methods in a class operate on the object's data.
examples:
  - code: |
        class Car:
            def __init__(self, make, model):
                self.make = make
                self.model = model
        my_car = Car("Toyota", "Corolla")
    prompt: The `__init__` method is used to initialize the attributes of the `Car` class.
    answer: True
  - code: |
        class Student:
            school = "High School"
        student1 = Student()
        student2 = Student()
        student1.school = "Middle School"
    prompt: Changing the `school` attribute of `student1` will also change it for `student2`.
    answer: False
  - code: |
        class Dog:
            def bark(self):
                print("Woof!")
        my_dog = Dog()
        my_dog.bark()
    prompt: The `bark` method is an instance method of the `Dog` class.
    answer: True
  - code: |
        class Circle:
            pi = 3.14
        print(Circle.pi)
    prompt: The `pi` attribute is a class attribute of the `Circle` class.
    answer: True
answers:
    - ✅ True.
    - ✅ True.
    - ❌ False. Instance attributes are unique to each object. It’s class attributes that are shared.
    - ✅ True.
    - ❌ False. Class attributes are defined outside the constructor, directly in the class body.
    - ✅ True.


resources:
    - name: Learn Classes and Objects
      url: https://yasirbhutta.github.io/python/docs/classes.html
---