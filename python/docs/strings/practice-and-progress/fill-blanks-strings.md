---
layout: page
title: "Learn String Methods & Formatting: MCQs"
description: --.
keywords: --.
author: "Muhammad Yasir Bhutta"
toc: toc/python-toc.html
topic: "strings"
course: "python"
prev: /python/docs/strings/practice-and-progress/true-false-strings.html
next: /python/docs/strings/practice-and-progress/mcqs-strings.html
---

{% assign topic = "string" %}
{% assign topics = site.data.python.fill-blanks.topics %}
{% assign selected_topic = topics | where: "topic", topic | first %}
{% assign questions = selected_topic.questions %}
{% assign examples = selected_topic.examples %}
{% assign resources = selected_topic.resources %}
{% include pap/fill-blanks-loop.html questions=questions examples=examples resources=resources topic=topic %}