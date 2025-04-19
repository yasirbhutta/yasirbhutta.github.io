---
layout: default
title: --
description: --
keywords: ---
toc: toc/python-toc.html
topic: "oop-inheritance"
course: "python"
resources:
  - name: Microsoft Excel Basics
    url: https://yasirbhutta.github.io/ms-excel/docs/basics.html
---

{% assign topic = "oop-inheritance" %}
{% assign topics = site.data.python.fill-blanks.topics %}
{% assign selected_topic = topics | where: "topic", topic | first %}
{% assign questions = selected_topic.questions %}
{% assign examples = selected_topic.examples %}
{% include pap/fill-blanks-loop.html questions=questions examples=examples topic=topic %}



