---
layout: page
title: "Learn String Methods & Formatting: True or False"
description: --.
keywords: --.
author: "Muhammad Yasir Bhutta"
toc: toc/python-toc.html
topic: "strings"
course: "python"
prev: /python/docs/strings.html
next: /python/docs/strings/practice-and-progress/fill-blanks-strings.html
---

{% assign topic = "strings" %}
{% assign topics = site.data.python.true-false.topics %}
{% assign selected_topic = topics | where: "topic", topic | first %}
{% assign questions = selected_topic.questions %}
{% assign resources = selected_topic.resources %}

{% include pap/true-false-loop.html questions=questions resources=resources topic=topic %}