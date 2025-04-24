---
layout: page
title: "Microsoft Excel Basics - Exercises for Beginners"
meta_description: "Practice your Microsoft Excel skills with these beginner-friendly exercises. Learn how to insert, delete, rename, hide, and unhide worksheets to strengthen your understanding of Excel basics."
keywords: "Microsoft Excel basics, Excel exercises for beginners, Excel worksheet management, insert worksheet, delete worksheet, rename worksheet, hide worksheet, unhide worksheet, Excel workbook practice, beginner Excel skills"
toc: toc/ms-excel-toc.html
topic: "basics"
course: "ms-excel"
prev: /ms-excel/docs/basics/practice-and-progress/fill-blanks-basics.html
next: /ms-excel/docs/basics/practice-and-progress/mcqs-basics.html
---

{% assign topic = "basics" %}
{% assign topics = site.data.ms-excel.coding-exercises.topics %}
{% assign selected_topic = topics | where: "topic", topic | first %}
{% assign exercises = selected_topic.exercises %}
{% include pap/coding-exercises-loop.html exercises=exercises topic=topic %}
