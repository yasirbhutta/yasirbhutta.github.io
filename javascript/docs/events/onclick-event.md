---
layout: post
title: "JavaScript onclick Event: Beginner’s Guide with Real-World Examples" 
description: "Discover how the JavaScript onclick event works and how to use it in real-life projects. Learn with beginner-friendly examples like toggling dark mode, adding items to a cart, and more."  
keywords: "JavaScript onclick, onclick event example, JavaScript click event, onclick function, real world JavaScript examples, onclick tutorial for beginners, toggle dark mode JavaScript, add to cart JavaScript, JavaScript event handling"
toc: toc/javascript.html
topic: "basics"
course: "javascript"
---


## 🖱️ What is the `onclick` Event in JavaScript?

The `onclick` event in JavaScript is triggered when a user **clicks on an HTML element** (like a button, link, image, etc.). You can use it to run a function or perform some action when the user clicks.

---

## 🧪 Basic Usage (Inline)

### ✅ Example:
```html
<button onclick="sayHello()">Click Me</button>

<script>
  function sayHello() {
    alert("Hello there!");
  }
</script>
```

🟢 **What happens?**  
When you click the button, it calls the `sayHello()` function and shows an alert.

---

## 🎯 Real-World Usage Examples

### 1. **Toggle Dark Mode**
```html
<button onclick="toggleDarkMode()">Toggle Dark Mode</button>

<script>
  function toggleDarkMode() {
    document.body.classList.toggle("dark-mode");
  }
</script>
```

You might see this on websites that support dark/light themes.

---

### 2. **Add Item to Cart (eCommerce)**
```html
<button onclick="addToCart(101)">Add to Cart</button>

<script>
  function addToCart(productId) {
    console.log("Added product with ID:", productId);
    // Here you'd usually make an API call
  }
</script>
```

Used in online stores when a user clicks “Add to Cart”.

---

### 3. **Show/Hide Password**
```html
<input type="password" id="password">
<button onclick="togglePassword()">Show/Hide</button>

<script>
  function togglePassword() {
    let input = document.getElementById("password");
    input.type = input.type === "password" ? "text" : "password";
  }
</script>
```

Common on login or sign-up forms.

---

## ✨ Better Practice: Using `addEventListener`
Although `onclick` works fine, using `addEventListener` is cleaner and separates HTML from JavaScript.

```html
<button id="myButton">Click Me</button>

<script>
  document.getElementById("myButton").addEventListener("click", function() {
    alert("Clicked using addEventListener!");
  });
</script>
```

