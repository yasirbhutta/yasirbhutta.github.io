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
{% assign topics = site.data.python.rq.topics %}
{% assign selected_topic = topics | where: "topic", topic | first %}
{% assign questions = selected_topic.questions %}
{% include pap/rq-loop.html questions=questions topic=topic %}