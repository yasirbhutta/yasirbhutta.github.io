---
layout: default
title: Microsoft Excel MCQs - Test Your Knowledge of Excel Basics
description: Challenge your understanding of Microsoft Excel with these multiple-choice questions. Covering topics like worksheets, workbooks, formulas, shortcuts, and data entry, this quiz is perfect for beginners to assess and improve their Excel skills.
keywords: "Microsoft Excel MCQs, Excel basics quiz, Excel multiple-choice questions, Excel worksheets and workbooks, Excel formulas quiz, Excel shortcuts test, Excel data entry practice, beginner Excel quiz, Excel fundamentals assessment, Microsoft Excel skills test"
author: Muhammad Yasir Bhutta
toc: toc/python-toc.html
topic: "oop-inheritance"
course: "python"
resources:
  - name: Microsoft Excel Basics
    url: https://yasirbhutta.github.io/ms-excel/docs/basics.html
---

<h1>🐍 Python MCQs</h1>


{% assign topic_name = "oop-inheritance" %}
{% assign topics = site.data.python.topics %}
{% assign selected_topic = topics | where: "topic", topic_name | first %}
{% assign mcqs = selected_topic.questions %}

<h2>{{ selected_topic.topic | capitalize }}</h2>

{% for q in mcqs %}
  <div class="mcq">
    <h3>Q{{ forloop.index }}. {{ q.question | markdownify }}</h3>
    <p><em>Difficulty: {{ q.difficulty }}</em></p>
    <ul>
      {% for option in q.options %}
        <li>{{ option | markdownify }}</li>
      {% endfor %}
    </ul>
    <details>
      <summary>Answer</summary>
      <p><strong>{{ q.answer }}</strong></p>
      {% if q.explanation %}
        <p><em>{{ q.explanation }}</em></p>
      {% endif %}
    </details>
    <hr>
  </div>
{% endfor %}
