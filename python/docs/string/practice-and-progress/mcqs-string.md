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

{% assign topic_name = "string" %}
{% assign topics = site.data.python.mcqs.topics %}
{% assign selected_topic = topics | where: "topic", topic_name | first %}
{% assign mcqs = selected_topic.questions %}
{% assign resources = selected_topic.resources %}
{% include pap/mcqs-loop.html mcqs=mcqs resources=resources %}