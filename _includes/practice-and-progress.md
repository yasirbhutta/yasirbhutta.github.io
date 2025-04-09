## Practice & Progress

{% assign practice_links = 
  "True or False:basics/practice-and-progress/true-false-{{ topic }}.md,
   Fill in the Blanks:basics/practice-and-progress/fill-blanks-{{ topic }}.md,
   Python Basics MCQs: Test Your Knowledge:basics/practice-and-progress/mcqs-{{ topic }}.md,
   Find and Fix Mistakes:basics/practice-and-progress/find-fix-mistakes-{{ topic }}.md,
   Python Basics Quiz:../quizzes/{{ topic }}-quiz.md,
   Python Exercises for Basics:basics/practice-and-progress/coding-exercises-{{ topic }}.md,
   Python Basics Mini Project: Build a Simple Expense Tracker:basics/practice-and-progress/mini-project-{{ topic }}.md,
   Review Questions:basics/practice-and-progress/review-questions-{{ topic }}.md" | split: "," %}

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