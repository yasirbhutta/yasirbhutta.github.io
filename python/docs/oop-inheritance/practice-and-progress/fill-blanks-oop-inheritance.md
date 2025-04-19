---
layout: page
title: Inheritance in Pyhton - Fill in the Blanks
description: --
keywords: ---
toc: toc/python-toc.html
topic: "oop-inheritance"
course: "python"
prev: /python/docs/oop-inheritance/practice-and-progress/true-false-oop-inheritance.html
next: /python/docs/oop-inheritance/practice-and-progress/mcqs-oop-inheritance.html
---

{% assign topic = "oop-inheritance" %}
{% assign topics = site.data.python.fill-blanks.topics %}
{% assign selected_topic = topics | where: "topic", topic | first %}
{% assign questions = selected_topic.questions %}
{% assign examples = selected_topic.examples %}
{% assign resources = selected_topic.resources %}
{% include pap/fill-blanks-loop.html questions=questions examples=examples resources=resources topic=topic %}



