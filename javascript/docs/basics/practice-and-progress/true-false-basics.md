---
layout: page
title:  JavaScript Basics Quiz – True or False Questions for Beginners
description: Test your understanding of JavaScript fundamentals with this beginner-friendly true or false quiz. Learn key concepts like variables, functions, DOM manipulation, and script placement in a fun and simple format.
keywords: JavaScript quiz, JavaScript true or false questions, JS basics quiz, beginner JavaScript test, JavaScript fundamentals, JavaScript MCQ, JavaScript for beginners, DOM quiz, JavaScript variables, JS functions
toc: toc/javascript.html
topic: "basics"
course: "javascript"
prev: /javascript
next: /javascript
---

{% assign topic = "basics" %}
{% assign topics = site.data.javascript.true-false.topics %}
{% assign selected_topic = topics | where: "topic", topic | first %}
{% assign questions = selected_topic.questions %}
<!-- {% assign examples = selected_topic.examples %} -->
{% assign resources = selected_topic.resources %}
{% include pap/true-false-loop.html questions=questions resources=resources topic=topic %}