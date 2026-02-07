---
layout: page
title: "JavaScript const Explained for Beginners – Easy Guide with Examples"
description: "Learn what const means in JavaScript with this simple guide for beginners. Understand how to use const with numbers, arrays, and objects, and why it's useful for writing safer code."
keywords: "JavaScript const, const in JavaScript, JavaScript variables, JavaScript tutorial for beginners, let vs const, const example JavaScript, beginner JavaScript, ES6 variables, const array JavaScript, JavaScript object const"
toc: toc/javascript.html
topic: "basics"
course: "javascript"
---

## 🧠 What is `const` in JavaScript?

`const` is a way to **create a variable** in JavaScript, but one that **cannot be changed later**.  
It stands for **"constant"** — something that stays the same.

---

## 📌 Basic Rule

Once you give a value to a `const` variable, you **cannot change** that value.

---

## 🧾 Syntax

```javascript
const name = "John";
```

---

## ✅ Easy Examples

### 1. Constant value:
```javascript
const pi = 3.14;
console.log(pi); // 3.14

// You can't change it later:
// pi = 3.14159; // ❌ This will give an error
```

---

### 2. With an array (list of items):

```javascript
const colors = ["red", "blue"];
colors.push("green"); // ✅ You can add items
console.log(colors); // ["red", "blue", "green"]

// colors = ["yellow"]; // ❌ Not allowed: you can't assign a new array
```

---

### 3. With an object:

```javascript
const user = { name: "Alice", age: 25 };
user.age = 26; // ✅ You can change properties
console.log(user); // { name: "Alice", age: 26 }

// user = { name: "Bob" }; // ❌ Not allowed
```

---

## 💡 When Should Beginners Use `const`?

- When the value **shouldn’t change** (like a name, total, or settings).
- It helps **avoid mistakes** and makes your code easier to read.

---
