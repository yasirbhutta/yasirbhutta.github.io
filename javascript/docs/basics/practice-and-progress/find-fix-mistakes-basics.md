---
layout: page
title: Find and Fix Mistakes – Javascript.
description: Practice Python OOP inheritance by identifying and fixing common mistakes in code examples.
keywords: python, oop, inheritance, practice questions, find and fix, error correction
author: Muhammad Yasir Bhutta.
toc: toc/javascript.html
topic: "basics"
course: "javascript"
prev: /python/docs/oop-inheritance/practice-and-progress/true-false-oop-inheritance.html
next: /python/docs/oop-inheritance/practice-and-progress/exercises-oop-inheritance.html
---

{% assign topic_name = "basics" %}
{% assign topics = site.data.javascript.find-and-fix.topics %}
{% assign selected_topic = topics | where: "topic", topic_name | first %}
{% assign questions = selected_topic.questions %}
{% assign resources = selected_topic.resources %}
{% include pap/find-and-fix-loop.html questions=questions resources=resources %}
