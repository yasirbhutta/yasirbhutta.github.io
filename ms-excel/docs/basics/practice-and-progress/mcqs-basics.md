---
layout: page
title: "Microsoft Excel MCQs - Test Your Knowledge of Excel Basics"
description: Challenge your understanding of Microsoft Excel with these multiple-choice questions. Covering topics like worksheets, workbooks, formulas, shortcuts, and data entry, this quiz is perfect for beginners to assess and improve their Excel skills.
keywords: Microsoft Excel MCQs, Excel basics quiz, Excel multiple-choice questions, Excel worksheets and workbooks, Excel formulas quiz, Excel shortcuts test, Excel data entry practice, beginner Excel quiz, Excel fundamentals assessment, Microsoft Excel skills test
author: Muhammad Yasir Bhutta
toc: toc/ms-excel-toc.html
topic: "basics"
course: "ms-excel"
prev: /ms-excel/docs/basics/practice-and-progress/true-false-basics.html
next: /ms-excel/docs/basics/practice-and-progress/find-fix-basics.html
---

{% assign topic_name = "basics" %}
{% assign topics = site.data.ms-excel.mcqs.topics %}
{% assign selected_topic = topics | where: "topic", topic_name | first %}
{% assign mcqs = selected_topic.questions %}
{% assign resources = selected_topic.resources %}
{% include pap/mcqs-loop.html mcqs=mcqs resources=resources %}



---
