---
layout: page
title: "Learn String Methods & Formatting: MCQs"
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
{% assign topics = site.data.python.fill-blanks.topics %}
{% assign selected_topic = topics | where: "topic", topic | first %}
{% assign questions = selected_topic.questions %}
{% assign examples = selected_topic.examples %}
{% assign resources = selected_topic.resources %}
{% include pap/fill-blanks-loop.html questions=questions examples=examples resources=resources topic=topic %}