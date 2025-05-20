---
layout: page
title: Python- Facebook Graph API
description: Learn Python variables with this beginner-friendly guide. Understand variable naming rules, assignments, and operations with examples and exercises. Perfect for students and professionals starting their Python journey.  
keywords: Python variables, Python variable examples, Python variable exercises, Python variable naming rules, Python variable assignment, Python beginner tutorials, Python programming basics, learn Python variables, Python coding exercises
toc: toc/python.html
---
5. Encapsulation

Encapsulation is the concept of hiding the internal details of a class and providing methods to interact with the data. This is often achieved using private and public attributes.

Attributes that start with an underscore (e.g., _age) are conventionally considered private.


Example:

class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # _age is considered private

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age > 0:
            self._age = age

person = Person("Alice", 30)
person.set_age(35)
print(person.get_age())  # Output: 35
