---
layout: page
title: --.
description: --.
keywords: --.
author: "Muhammad Yasir Bhutta"
toc: toc/python-toc.html
topic: "strings"
course: "python"
prev: "/python/docs/strings/practice-and-progress/fill-blanks-strings.html"
next: "/python/docs/strings/practice-and-progress/find-fix-mistakes-strings.html"
---

{% assign topic_name = "strings" %}
{% assign topics = site.data.python.mcqs.topics %}
{% assign selected_topic = topics | where: "topic", topic_name | first %}
{% assign mcqs = selected_topic.questions %}
{% assign resources = selected_topic.resources %}
{% include pap/mcqs-loop.html mcqs=mcqs resources=resources %}