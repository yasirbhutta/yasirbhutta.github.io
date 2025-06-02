---
layout: page
title:  "PHP Basics True or False Questions – Test Your Core PHP Knowledge"
description: Boost your PHP skills with these essential true or false questions on PHP basics. Perfect for beginners and interview preparation. Test your knowledge now!.
keywords: PHP basics, PHP quiz, PHP true or false, core PHP questions, PHP test online, PHP interview questions, learn PHP, PHP for beginners, PHP basics quiz, PHP practice test, PHP fundamentals, PHP MCQ, PHP assessment, PHP online quiz, PHP knowledge check
topic: "basics"
course: "php"
prev: /php/docs/basics/
next: /php/docs/basics/practice-and-progress/mcqs-basics.html
mini_project: false
---

{% assign topic = "basics" %}
{% assign topics = site.data.php.true-false.topics %}
{% assign selected_topic = topics | where: "topic", topic | first %}
{% assign questions = selected_topic.questions %}
<!-- {% assign examples = selected_topic.examples %} -->
{% assign resources = selected_topic.resources %}
{% include pap/true-false-loop.html questions=questions resources=resources topic=topic %}


### 🔍 **True / False Questions**

1. JavaScript can be used both on the client-side and server-side.
   ✅ **True**

2. PHP code is executed by the browser.
   ❌ **False** — PHP is executed on the server.

3. CSS is a server-side scripting language.
   ❌ **False** — CSS is a client-side style language.

4. Server-side scripts cannot access a database.
   ❌ **False** — That’s one of their main purposes.

5. AJAX helps send data to the server without refreshing the page.
   ✅ **True**

---
