---
layout: page
title:  Microsoft Excel Basics Quiz – True or False Questions for Beginners
description: Test your understanding of JavaScript fundamentals with this beginner-friendly true or false quiz. Learn key concepts like variables, functions, DOM manipulation, and script placement in a fun and simple format.
keywords: JavaScript quiz, JavaScript true or false questions, JS basics quiz, beginner JavaScript test, JavaScript fundamentals, JavaScript MCQ, JavaScript for beginners, DOM quiz, JavaScript variables, JS functions
toc: toc/javascript.html
topic: "basics"
course: "ms-excel"
prev: /ms-excel/docs/basics.html
next: /ms-excel/docs/basics/practice-and-progress/mcqs-basics.html
---

{% assign topic = "basics" %}
{% assign topics = site.data.ms-excel.true-false.topics %}
{% assign selected_topic = topics | where: "topic", topic | first %}
{% assign questions = selected_topic.questions %}
<!-- {% assign examples = selected_topic.examples %} -->
{% assign resources = selected_topic.resources %}
{% include pap/true-false-loop.html questions=questions resources=resources topic=topic %}
