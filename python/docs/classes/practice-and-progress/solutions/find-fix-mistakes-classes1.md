---
layout: fix-mistakes-solution
title: Python Classes - Find and Fix Mistakes with Code Examples.
description: Learn how to identify and fix common mistakes in Python classes with this step-by-step guide. Perfect for beginners to understand constructors, instance variables, and methods in object-oriented programming.

difficulty:
  beginner: true
  intermediate: false
  advanced: false

topic: Classes

buggy_code: |
  class Person:
      def __init__(name, age):
          name = name
          age = age

      def greet():
          print("Hello, my name is " + self.name)

  person1 = Person("Alice", 30)
  person1.greet()

mistakes: 
  - "Missing `self` in the constructor parameter list. The first parameter of any instance method must be `self`."

corrected_code: |
  class Person:
      def __init__(self, name, age):
          self.name = name
          self.age = age

      def greet(self):
          print("Hello, my name is " + self.name)

  person1 = Person("Alice", 30)
  person1.greet()

related_challenges:
  - name: Find and Fix Mistakes in Python Classes
    url: ../find-fix-mistakes-classes.md
---