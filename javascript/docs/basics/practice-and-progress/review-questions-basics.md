---
layout: page
title: "Review Questions on Javascript Basics – Test Your Understanding"
description: "Reinforce your Python OOP inheritance knowledge with review questions designed to test your grasp of single, multiple, and multilevel inheritance. Ideal for students and beginners."
keywords: Python OOP review questions, Python inheritance quiz, object-oriented programming questions, Python class inheritance test, OOP MCQs Python, Python inheritance assessment, beginner Python OOP questions, review Python OOP concepts
toc: toc/javascript.html
topic: "basics"
course: "javascript"
prev: /javascript/docs/basics/practice-and-progress/fill-blanks-basics.html
next: /javascript/docs/basics/practice-and-progress/mcqs-basics.html
---

{% assign topic = "basics" %}
{% assign topics = site.data.javascript.rq.topics %}
{% assign selected_topic = topics | where: "topic", topic | first %}
{% assign questions = selected_topic.questions %}
{% include pap/rq-loop.html questions=questions topic=topic %}