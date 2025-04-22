---
layout: page
title: "JavaScript Basics" 
description: ""  
keywords: ""
toc: toc/javascript.html
topic: "basics"
course: "javascript"
prev: /html-css/docs/html-basics.html
next: html-css/docs/css-basics.html
---

## 🔹 Introduction to JavaScript

- Understand how JavaScript interacts with HTML.

#### ✅ Example 1: `document.write()`
```html
<script>
    document.write("Hello World Wide Web");
</script>
```
- Teaches how to inject content directly into the page.

#### ✅ Example 2: `alert()`
```html
<script>
    alert('Hello, world!');
</script>
```
- Demonstrates basic interaction using pop-ups.

---

### 🔹 Script Placement in HTML

**Goal:** Learn where and how to place JavaScript in HTML.

#### ✅ Inside `<body>`
```html
<body>
    <h1>Hello World</h1>
    <script>
        alert("This runs from inside the body!");
    </script>
</body>
```

#### ✅ Best practice: End of `<body>`
```html
<body>
    <!-- HTML Content -->
    <script src="script.js"></script>
</body>
```

#### ✅ Modern approach with `defer`
```html
<head>
    <script src="script.js" defer></script>
</head>
```

---

### 🔹 Working with Variables and Data Types

**Goal:** Learn to declare and use variables.

```html
<script>
    var str = 'Hello world';
    document.write(str + "<br>");

    var a = 5, b = 10;
    var c = a + b;
    document.write("Sum: " + c + "<br>");

    var myVar = 1;
    myVar = "Allah is the Greatest";
    document.write("<h1>" + myVar + "</h1>");
</script>
```

---

### 🔹 Basic Functions

**Goal:** Learn to create and call functions.

#### ✅ Function with `alert()`
```html
<script>
    function greet() {
        alert("Welcome to JavaScript!");
    }
    greet();
</script>
```

#### ✅ Multiplication Function
```html
<script>
    function multiply(num1, num2) {
        return num1 * num2;
    }
    alert("Product: " + multiply(5, 6));
</script>
```

---

### 🔹 User Input with `prompt()`

```html
<script>
    function doShowName() {
        var name = prompt("What is your name?");
        alert(name + ", you just did something awesome!");
    }
</script>
<button onclick="doShowName()">Click Here</button>
```

- Introduces `prompt()` and user interaction.
- Connects input with output using functions.

---

### 🔹 Changing Content Dynamically (DOM)

**Goal:** Modify HTML using JavaScript.

#### ✅ Example with `innerHTML`
```html
<h1 id="demo">..............</h1>
<script>
    document.getElementById("demo").innerHTML = "Ya ALLAH!";
</script>
```

---

### 🔹 External JavaScript File

**Goal:** Organize JavaScript in separate files.

#### ✅ HTML File
```html
<h1 id="demo">ALLAH</h1>
<form>
    <input type="button" value="Click" onclick="msg()" />
</form>
<script src="scripts/hello.js"></script>
```

#### ✅ `scripts/hello.js`
```javascript
function msg() {
    document.getElementById("demo").innerHTML = "Ya ALLAH!....";
}
```

---


## 🛠️ Real-World JavaScript Examples for Beginners


### 🛠️ Dynamically Change Style with JavaScript

---

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

#### 🔠 2. Change Font Size Dynamically

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

#### ✏️ 3. Highlight Form Field on Focus

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

#### 👁️ 4. Toggle Visibility (Show/Hide Div)

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

#### 🌈 5. Change Background Color Randomly

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

---

#### 🧪 6. Add or Remove CSS Class

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

#### 🌗 7. Change Button Text and Style on Click

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

### More Examples

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

## 🔖 Further Reading & References

- [JavaScript: Adding interactivity](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website/Adding_interactivity)
  

