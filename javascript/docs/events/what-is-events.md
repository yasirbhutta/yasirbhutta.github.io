---
layout: page
title: "JavaScript Events Explained: A Beginner's Guide with Examples"
description: "Learn what events are in JavaScript and how to use them effectively. This beginner-friendly guide covers click events, keyboard events, and more with simple examples."
keywords: "JavaScript events, JS event handling, JavaScript click event, addEventListener, keyboard event JavaScript, JavaScript for beginners, event listener tutorial"
toc: toc/javascript.html
topic: "basics"
course: "javascript"
---

In JavaScript, **events** are actions or occurrences that happen in the browser, often as a result of user interaction. JavaScript can "listen" for these events and respond to them using functions called **event handlers**.

### 🧠 Common Examples of Events:
- `click` – When a user clicks on an element.
- `mouseover` – When a user hovers over an element.
- `keydown` – When a user presses a key.
- `submit` – When a form is submitted.
- `load` – When a page or image is loaded.

---

### 🧪 Example:

```html
<button onclick="sayHello()">Click me</button>

<script>
  function sayHello() {
    alert('Hello!');
  }
</script>
```

This is an example of an **inline event handler**. When the button is clicked, the `sayHello` function runs and shows an alert.

---

### ✅ A Better Way (Using `addEventListener`)
```html
<button id="myBtn">Click Me</button>

<script>
  document.getElementById("myBtn").addEventListener("click", function() {
    alert("Hello from event listener!");
  });
</script>
```

This is more flexible and preferred in modern JavaScript.
