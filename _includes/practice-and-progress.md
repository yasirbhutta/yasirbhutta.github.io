## Practice & Progress

{% assign practice_links = 
  "True or False:practice-and-progress/true-false,
   Fill in the Blanks:practice-and-progress/fill-blanks,
   Python Basics MCQs - Test Your Knowledge:practice-and-progress/mcqs,
   Find and Fix Mistakes:practice-and-progress/find-fix-mistakes,
   Python Basics Quiz:practice-and-progress/find-fix-mistakes,
   Python Exercises for Basics:practice-and-progress/coding-exercises,
   Python Basics Mini Project:practice-and-progress/mini-project,
   Review Questions:practice-and-progress/review-questions" | split: "," %}

    
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
- [{{ parts[0] }}]({{ topic }}/{{ parts[1] }}-{{ topic }}.html)
{% endfor %}