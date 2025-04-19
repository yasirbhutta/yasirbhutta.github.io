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

<p><strong>Topic:</strong> {{ topic }}</p>

<hr />

<h2>🔍 Fill in the Blanks</h2>
<ol>
  {% for question in questions %}
    <li>{{ question }}</li>
    <details>
        <summary>✅ Answer</summary>
        <p><strong>{{ question.answer }}</strong></p>
        {% if question.explanation %}
          <p><em>{{ question.explanation }}</em></p>
        {% endif %}
      </details>
      <hr>
  {% endfor %}
</ol>

<hr />

{% if examples %}
<h2>🧠 Example-Based Fill in the Blanks</h2>
<ol>
  {% for example in examples %}
    <li>
      <pre><code>{{ example.code | escape }}</code></pre>
      <p>{{ example.prompt }}</p>
      <!-- <p><strong>Answer:</strong> <code>{{ example.answer }}</code></p> -->
    </li>
  {% endfor %}
</ol>
{% endif %}
<hr />

<h2>🗝️ Answer Key</h2>

<h3>✅ Answers for Fill in the Blanks</h3>
<ol>
  {% for answer in page.answers %}
    <li>{{ answer }}</li>
  {% endfor %}
</ol>

{% if page.examples %}
<h3>💡 Answers for Example-Based Fill in the Blanks</h3>
<ol>
  {% for example in page.examples %}
    <li>{{ example.answer }}</li>
  {% endfor %}
</ol>
{% endif %}
<hr />

<h2>📚 Related Resources</h2>
<ul>
  {% for resource in include.resources %}
    <li><a href="{{ resource.url }}">{{ resource.name }}</a></li>
  {% endfor %}
</ul>


