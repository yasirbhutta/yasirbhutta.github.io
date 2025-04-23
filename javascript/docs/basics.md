---
layout: page
title: "JavaScript Basics" 
description: "Master JavaScript fundamentals with this beginner-friendly guide. Learn about variables, functions, user input, DOM manipulation, and external scripts through practical examples and interactive exercises."  
keywords: "JavaScript basics, learn JavaScript, JavaScript tutorial, beginner JavaScript, JavaScript variables, JavaScript functions, DOM manipulation, JavaScript user input, external JavaScript, JavaScript examples, interactive JavaScript, JavaScript exercises"
toc: toc/javascript.html
topic: "basics"
course: "javascript"
prev: /html-css/docs/html-basics.html
next: html-css/docs/css-basics.html
---

## Contents

- [Intoduction to JavaScript](#-introduction-to-javascript)
- [Script Placement in HTML](#-script-placement-in-html)
- [Working with Variables and Data Types](#-working-with-variables-and-data-types)
- [Basic Functions](#-basic-functions)
- [User Input with `prompt()`](#-user-input-with-prompt)
- [Changing Content Dynamically (DOM)](#-changing-content-dynamically-dom)
- [External JavaScript File](#-external-javascript-file)
- [Real-World JavaScript Examples for Beginners](basics/real-world-javascript-examples.md)
  
## 🔹 Introduction to JavaScript

- Understand how JavaScript interacts with HTML.

### ✅ Example 1: `document.write()`

```html
<script>
    document.write("Hello World Wide Web");
</script>
```

### ✅ Example 2: `alert()`

```html
<script>
    alert('Hello, world!');
</script>
```
- Demonstrates basic interaction using pop-ups.

---

## 🔹 Script Placement in HTML

**Goal:** Learn where and how to place JavaScript in HTML.

### ✅ 1. Inside `<body>`

```html
<body>
    <h1>Hello World</h1>
    <script>
        alert("This runs from inside the body!");
    </script>
</body>
```

### ✅ 2. Best practice: End of `<body>`

```html
<body>
    <!-- HTML Content -->
    <script src="script.js"></script>
</body>
```

### ✅ 3. Modern approach with `defer`

```html
<head>
    <script src="script.js" defer></script>
</head>
```

---

## 🔹 Working with Variables and Data Types

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

## 🔹 Basic Functions

**Goal:** Learn to create and call functions.

### ✅ Function with `alert()`

```html
<script>
    function greet() {
        alert("Welcome to JavaScript!");
    }
    greet();
</script>
```

### ✅ Multiplication Function

```html
<script>
    function multiply(num1, num2) {
        return num1 * num2;
    }
    alert("Product: " + multiply(5, 6));
</script>
```

---

## 🔹 User Input with `prompt()`

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


**📌 `onclick` Event (JavaScript)**

The `onclick` event in JavaScript runs when a user **clicks on an HTML element**—such as a button, link, or image. It's commonly used to perform actions like submitting forms, showing messages, or toggling features.

🔗 For a detailed explanation, see:  
👉 [🖱️ What is the `onclick` Event in JavaScript?](events/onclick-event.md)  
👉 [📘 What are Events in JavaScript?](events/what-is-events.md)

---

## 🔹 Changing Content Dynamically (DOM)

**Goal:** Modify HTML using JavaScript.

### ✅ Example with `innerHTML`

```html
<h1 id="demo">..............</h1>
<script>
    document.getElementById("demo").innerHTML = "Ya ALLAH!";
</script>
```

---

## 🔹 External JavaScript File

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

For real-world JavaScript examples, See [Real-World JavaScript Examples for Beginners](basics/real-world-javascript-examples.md)


## 🔖 Further Reading & References

- [JavaScript: Adding interactivity](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website/Adding_interactivity)
  

