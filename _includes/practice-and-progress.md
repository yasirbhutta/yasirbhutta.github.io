## Practice & Progress

{% assign practice_links = 
  "True or False:{{ topic }}/practice-and-progress/true-false-{{ topic }}.md,
   Fill in the Blanks:{{ topic }}/practice-and-progress/fill-blanks-{{ topic }}.md,
   Python Basics MCQs: Test Your Knowledge:{{ topic }}/practice-and-progress/mcqs-{{ topic }}.md,
   Find and Fix Mistakes:{{ topic }}/practice-and-progress/find-fix-mistakes-{{ topic }}.md,
   Python Basics Quiz:../quizzes/{{ topic }}-quiz.md,
   Python Exercises for Basics:{{ topic }}/practice-and-progress/coding-exercises-{{ topic }}.md,
   Python Basics Mini Project: Build a Simple Expense Tracker:{{ topic }}/practice-and-progress/mini-project-{{ topic }}.md,
   Review Questions:{{ topic }}/practice-and-progress/review-questions-{{ topic }}.md" | split: "," %}

{% for link in practice_links %}
  {% assign parts = link | split: ":" %}
  {% if forloop.index == 3 %}
  ---
  ### Multiple-Choice Questions (MCQs)
  {% endif %}
  {% if forloop.index == 4 %}
  ---
  ### Find and Fix Mistakes
  {% endif %}
  {% if forloop.index == 6 %}
  ---
  ### Coding Exercises
  {% endif %}
  {% if forloop.index == 7 %}
  ---
  ### Mini Projects
  {% endif %}
  {% if forloop.index == 8 %}
  ---
  {% endif %}
- [{{ parts[0] }}]({{ parts[1] }})
{% endfor %}