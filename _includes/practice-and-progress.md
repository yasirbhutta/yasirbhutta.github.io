## Practice & Progress

{% assign practice_links = 
  "practice-and-progress/true-false,
   practice-and-progress/fill-blanks,
   practice-and-progress/mcqs,
   practice-and-progress/find-fix-mistakes,
   /quizzes/quiz,
   practice-and-progress/coding-exercises,
   practice-and-progress/mini-project,
   practice-and-progress/review-questions" | split: "," %}


{% for link in practice_links %}
  {% assign parts = link | split: "/" %}
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