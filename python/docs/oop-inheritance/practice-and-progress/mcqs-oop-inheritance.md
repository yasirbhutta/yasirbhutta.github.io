---
layout: page
title: Multiple Choice Questions (MCQs) on Inheritance in Python – OOP Practice
description: Boost your Python skills with these MCQs on Object-Oriented Programming and Inheritance. Ideal for beginners, students, and job seekers to test and strengthen their understanding of Python OOP concepts.
keywords: Python inheritance MCQs, OOP MCQ Python, multiple choice questions Python inheritance, Python class and object quiz, object oriented programming Python MCQs, Python OOP practice test, Python inheritance quiz questions, Python interview questions OOP, Python MCQ with answers, inheritance concepts in Python
author: Muhammad Yasir Bhutta
toc: toc/python-toc.html
topic: "oop-inheritance"
course: "python"
prev: /python/docs/oop-inheritance/practice-and-progress/true-false-oop-inheritance.html
next: /python/docs/oop-inheritance/practice-and-progress/find-fix-mistakes-oop-inheritance.html
---

{% assign topic_name = "oop-inheritance" %}
{% assign topics = site.data.python.mcqs.topics %}
{% assign selected_topic = topics | where: "topic", topic_name | first %}
{% assign mcqs = selected_topic.questions %}
{% assign resources = selected_topic.resources %}
{% include pap/mcqs-loop.html mcqs=mcqs resources=resources %}


❓What is the output of the following Python code?

class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        print("Hello from Child")
        Parent.greet(self)     
        super().greet()         

obj = Child()
obj.greet()

Options:

A.

Hello from Child
Hello from Parent
Hello from Parent

B.

Hello from Parent
Hello from Child
Hello from Parent

C.

Hello from Child
Hello from Child
Hello from Parent

D.

Hello from Parent
Hello from Parent
Hello from Child

