---
layout: fill-in-the-blanks
title: Python Functions Fill-in-the-Blanks Practice
description: Practice writing and using Python functions with these fill-in-the-blank exercises.
difficulty:
  beginner: true
  intermediate: false
  advanced: false
topic: Functions
questions:
  - In Python, you create a class using the ________ keyword.  
  - A class is a ________ for creating objects (instances).  
  - Objects are ________ of a class that have attributes (data) and methods (functions).  
  - The `__init__` method is a special method that is automatically called when a new ________ of a class is created.
  - Instance attributes are ________ to each instance (object) of a class.  
  - The `self` parameter is used to access the ________ and ________ of an object within its methods.
  - Class attributes are shared across all ________ of the class, while instance attributes are specific to each ________.
  - To access an attribute of an object, use the ________ notation (e.g., `object.attribute`).  
  - Changing the value of a ________ attribute will reflect across all objects of the class.
  - Methods are ________ defined within a class that operate on the object's data.  
examples:
  - code: |
        class Car:
            def describe(self):
                print(f"{self.year} {self.make} {self.model}")
    prompt: The `describe` method is a ________ of the `Car` class.
    answer: method
  - code: |
        class Student:
            def set_grade(self, new_grade):
                self.grade = new_grade
    prompt: The `set_grade` method is used to ________ the grade of a student.
    answer: update
answers:
  - class
  - blueprint  
  - instances
  - object
  - unique
  - attributes
  - methods
  - objects
  - object
  - dot
  - class
  - functions  
resources:
  - name: Learn Classes and Objects
    url: //python/docs/classes.md
  - name: Real Python Function Basics
    url: https://realpython.com/defining-your-own-python-function/
---