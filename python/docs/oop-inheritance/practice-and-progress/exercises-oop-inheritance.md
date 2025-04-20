---
layout: page
title: Inheritance in Pyhton - Fill in the Blanks
description: --
keywords: ---
toc: toc/python-toc.html
topic: "oop-inheritance"
course: "python"
prev: /python/docs/oop-inheritance/practice-and-progress/fill-blanks-oop-inheritance.html
next: /python/docs/oop-inheritance/practice-and-progress/mcqs-oop-inheritance.html
---

{% assign topic = "oop-inheritance" %}
{% assign topics = site.data.python.coding-exercises.topics %}
{% assign selected_topic = topics | where: "topic", topic | first %}
{% assign exercises = selected_topic.exercises %}
<!-- {% assign examples = selected_topic.examples %} -->
<!-- {% assign resources = selected_topic.resources %} -->
{% include pap/coding-exercises-loop.html exercises=exercises topic=topic %}


<!-- ## 🧪 Practice Time!

### 📝 Exercise 1:
Create a class `Employee` with a method `work()`.  
Create a class `Manager` that inherits from `Employee` and adds a method `manage()`.

### 📝 Exercise 2:
Create a class `Teacher` that inherits from `Person`.  
Override the `introduce()` method to say:  
`"Hello, I'm Mr./Ms. [name] and I teach students."`

### 📝 Exercise 3:
In the `Teacher` class, use `super()` inside `introduce()` so it also prints the original greeting.

Exercise 1: Create a Vehicle class and a Car class that inherits from it. Add a method to the Car class to display the car's brand.

Exercise 2: Override a method in the Car class to display a custom message.
 -->
