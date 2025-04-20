---
layout: page
title: Inheritance in Pyhton - True or False
description: --
keywords: ---
toc: toc/python-toc.html
topic: "oop-inheritance"
course: "python"
prev: /python/docs/oop-inheritance/practice-and-progress/fill-blanks-oop-inheritance.html
next: /python/docs/oop-inheritance/practice-and-progress/mcqs-oop-inheritance.html
---

{% assign topic = "oop-inheritance" %}
{% assign topics = site.data.python.rq.topics %}
{% assign selected_topic = topics | where: "topic", topic | first %}
{% assign questions = selected_topic.questions %}
<!-- {% assign examples = selected_topic.examples %} -->
<!-- {% assign resources = selected_topic.resources %} -->
{% include pap/rq-loop.html questions=questions topic=topic %}