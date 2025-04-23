---
layout: page
title: "Real World JavaScript Examples for Beginners – Practical Coding Guide" 
description: "Explore real-world JavaScript examples tailored for beginners. Learn how to build dynamic web features with hands-on code snippets, including DOM manipulation, form validation, and interactive web apps."  
keywords: "JavaScript examples, real-world JavaScript, beginner JavaScript projects, JavaScript DOM, interactive JavaScript, JavaScript practice, JavaScript code snippets, JavaScript tutorials, form validation JavaScript, web development"
toc: toc/javascript.html
topic: "basics"
course: "javascript"
prev: /html-css/docs/html-basics.html
next: html-css/docs/css-basics.html
---

## Contents
- Dynamically Change Style with JavaScript
  1. [Change Text Color on Button Click](#-1-change-text-color-on-button-click)
  2. [Change Font Size Dynamically](#-2-change-font-size-dynamically)
  3. [Change Background Color Randomly](#-3-change-background-color-randomly)
  4. [Highlight Form Field on Focus](#️-4-highlight-form-field-on-focus)
  5. [Toggle Visibility (Show/Hide Div)](#️-5-toggle-visibility-showhide-div)
  6. [Add or Remove CSS Class](#-6-add-or-remove-css-class)
  7. [Change Button Text and Style on Click](#-7-change-button-text-and-style-on-click)
- More Examples
  8. [Show/Hide Password Field](#-8-showhide-password-field)
  9. [Live Character Counter](#️-9-live-character-counter)
  10. [Greeting Based on Time](#-10-greeting-based-on-time)
  11. [Simple Calculator](#-11-simple-calculator)
  12. [Dark Mode Toggle](#-12-dark-mode-toggle)
  13. [Disable Button After Click](#-13-disable-button-after-click)
  14. [Real-Time Clock](#-14-real-time-clock)

## 🛠️ Dynamically Change Style with JavaScript

### 🎨 1. Change Text Color on Button Click

- Change text color interactively using JavaScript.

```html
<p id="text">Click the button to change my color!</p>
<button onclick="changeColor()">Change Color</button>

<script>
  function changeColor() {
    document.getElementById("text").style.color = "blue";
  }
</script>
```

🧠 *Used in interactive stories, quizzes, or themed messages.*

---

### 🔠 2. Change Font Size Dynamically

- Let users increase font size for better readability.

```html
<p id="resizeText">Resize me!</p>
<button onclick="increaseFont()">Increase Font</button>

<script>
  function increaseFont() {
    document.getElementById("resizeText").style.fontSize = "2em";
  }
</script>
```

🧠 *Helpful in accessibility or reading mode features.*

---

### 🌈 3. Change Background Color Randomly

- Make it fun with a random color generator!

```html
<button onclick="randomBg()">Random Background</button>

<script>
  function randomBg() {
    const colors = ["#f8b400", "#00b894", "#6c5ce7", "#d63031"];
    const color = colors[Math.floor(Math.random() * colors.length)];
    document.body.style.backgroundColor = color;
  }
</script>
```

🧠 *Used in color pickers, design tools, and fun quizzes.*

**See also:**
- [What is `const` in JavaScript?](const.md)
- [JavaScript Math.floor() Explained](/javascript/docs/math/math-floor.md)
- [JavaScript Math.random() Explained](/javascript//docs/math/math-random.md)
  
---

### ✏️ 4. Highlight Form Field on Focus

- Improve form UX by highlighting active fields.

```html
<input type="text" id="name" onfocus="highlight(this)" onblur="removeHighlight(this)">

<script>
  function highlight(element) {
    element.style.backgroundColor = "#ffffcc";
  }

  function removeHighlight(element) {
    element.style.backgroundColor = "";
  }
</script>
```

🧠 *Used to improve form UX on signup/login pages.*

---

### 👁️ 5. Toggle Visibility (Show/Hide Div)

- Show or hide sections like FAQs or dropdowns.
  
```html
<div id="info" style="display:none;">
  This is some hidden information.
</div>
<button onclick="toggleInfo()">Show/Hide Info</button>

<script>
  function toggleInfo() {
    const div = document.getElementById("info");
    div.style.display = div.style.display === "none" ? "block" : "none";
  }
</script>
```

🧠 *Great for FAQs, dropdowns, and read-more sections.*

---

### 🧪 6. Add or Remove CSS Class

- Use class toggling for cleaner and reusable styles.

```html
<p id="para">Watch me get fancy!</p>
<button onclick="toggleFancy()">Toggle Style</button>

<style>
  .fancy {
    font-weight: bold;
    color: red;
    text-transform: uppercase;
  }
</style>

<script>
  function toggleFancy() {
    document.getElementById("para").classList.toggle("fancy");
  }
</script>
```

🧠 *Modern and scalable method for styling elements dynamically.*

---

### 🌗 7. Change Button Text and Style on Click

```html
<button id="modeBtn" onclick="switchMode()">Enable Dark Mode</button>

<script>
  function switchMode() {
    const btn = document.getElementById("modeBtn");
    document.body.classList.toggle("dark");

    if (document.body.classList.contains("dark")) {
      btn.textContent = "Disable Dark Mode";
      btn.style.backgroundColor = "black";
      btn.style.color = "white";
    } else {
      btn.textContent = "Enable Dark Mode";
      btn.style.backgroundColor = "";
      btn.style.color = "";
    }
  }
</script>

<style>
  .dark {
    background-color: #222;
    color: #eee;
  }
</style>
```

🧠 *Useful in websites with themes or accessibility options.*

---

## More Examples

### 🔐 8. Show/Hide Password Field
**Use Case:** Toggle visibility of a password input.

```html
<input type="password" id="password">
<button onclick="togglePassword()">Show/Hide</button>

<script>
  function togglePassword() {
    const pwd = document.getElementById("password");
    pwd.type = pwd.type === "password" ? "text" : "password";
  }
</script>
```

🧠 *Used in login/signup forms.*

---

### ✍️ 9. Live Character Counter
**Use Case:** Show how many characters are typed in a form input.

```html
<textarea id="msg" onkeyup="countChar()"></textarea>
<p>Characters: <span id="count">0</span></p>

<script>
  function countChar() {
    const text = document.getElementById("msg").value;
    document.getElementById("count").textContent = text.length;
  }
</script>
```

🧠 *Useful for Twitter/X post limit, feedback forms, etc.*

---

### ⏰ 10. Greeting Based on Time
**Use Case:** Personalize greeting on websites.

```html
<p id="greet"></p>

<script>
  const hour = new Date().getHours();
  let greeting;

  if (hour < 12) {
    greeting = "Good Morning!";
  } else if (hour < 18) {
    greeting = "Good Afternoon!";
  } else {
    greeting = "Good Evening!";
  }

  document.getElementById("greet").textContent = greeting;
</script>
```

🧠 *Used on dashboards, landing pages, e-commerce portals.*

---

### ➕ 11. Simple Calculator
**Use Case:** Basic operations using form and JS.

```html
<input type="number" id="num1"> +
<input type="number" id="num2">
<button onclick="calculate()">=</button>
<span id="result"></span>

<script>
  function calculate() {
    let a = parseFloat(document.getElementById("num1").value);
    let b = parseFloat(document.getElementById("num2").value);
    document.getElementById("result").textContent = a + b;
  }
</script>
```

🧠 *Great intro to arithmetic and DOM.*

---

### 🌙 12. Dark Mode Toggle
**Use Case:** Switch between light and dark theme.

```html
<button onclick="toggleTheme()">Toggle Dark Mode</button>

<script>
  function toggleTheme() {
    document.body.classList.toggle("dark-mode");
  }
</script>

<style>
  .dark-mode {
    background-color: black;
    color: white;
  }
</style>
```

🧠 *Used on most modern websites for better user experience.*

---

### 🚫 13. Disable Button After Click
**Use Case:** Prevent multiple form submissions.

```html
<button onclick="submitForm(this)">Submit</button>

<script>
  function submitForm(btn) {
    btn.disabled = true;
    btn.textContent = "Submitted!";
  }
</script>
```

🧠 *Common in forms and transactions.*

---

### 🕒 14. Real-Time Clock
**Use Case:** Display the current time live.

```html
<p id="clock"></p>

<script>
  function updateClock() {
    const now = new Date().toLocaleTimeString();
    document.getElementById("clock").textContent = now;
  }

  setInterval(updateClock, 1000);
</script>
```

🧠 *Great for dashboards or digital clocks.*

---
