---
layout: page
title: --.
description: --.
keywords: --.
author: "Muhammad Yasir Bhutta"
toc: toc/python-toc.html
topic: ""
course: ""
prev: ""
next: ""
---

{% assign topic = "strings" %}
{% assign topics = site.data.python.coding-exercises.topics %}
{% assign selected_topic = topics | where: "topic", topic | first %}
{% assign exercises = selected_topic.exercises %}
{% include pap/coding-exercises-loop.html exercises=exercises topic=topic %}