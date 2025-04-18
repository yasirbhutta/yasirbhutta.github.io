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

<!-- 
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
{% endfor %} -->



<h1>{{ site.data.python.course }} Questions</h1>

{% assign topic_to_display = "oop-inheritance" %}

{% for topic in site.data.python_questions.topics %}
  {% if topic.topic == topic_to_display %}
    <h2>{{ topic.topic }}</h2>
    <ul>
      {% for question in topic.questions %}
        <li>
          <strong>{{ question.question }}</strong> <br>
          <p><em>Difficulty: {{ question.difficulty }}</em></p>
          <ul>
            {% for option in question.options %}
              <li>{{ option }}</li>
            {% endfor %}
          </ul>
          <p><strong>Answer:</strong> {{ question.answer }}</p>
          <p><em>{{ question.explanation }}</em></p>
        </li>
      {% endfor %}
    </ul>
  {% endif %}
{% endfor %}
