---
layout: default
title: --.
description: --.
keywords: --.
author: "Muhammad Yasir Bhutta"
toc: toc/
topic: ""
course: ""
prev: ""
next: ""
---

{% assign topic = "string" %}
{% assign topics = site.data.python.true-false.topics %}
{% assign selected_topic = topics | where: "topic", topic | first %}
{% assign questions = selected_topic.questions %}
{% assign resources = selected_topic.resources %}

{% include pap/true-false-loop.html questions=questions resources=resources topic=topic %}