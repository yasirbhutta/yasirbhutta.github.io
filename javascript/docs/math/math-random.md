---
layout: page
title: "JavaScript Math.random() Explained"
description: "Discover how to use JavaScript’s Math.random() function to generate random numbers. Learn the syntax, beginner-friendly examples, and real-world use cases like simulating dice rolls and random selection."
keywords: "JavaScript Math.random, random number JavaScript, JavaScript random function, generate random number, JavaScript dice roll, Math.random examples, JavaScript tutorial for beginners, JavaScript random integer, JavaScript number functions, web development JavaScript"
toc: toc/javascript.html
topic: "basics"
course: "javascript"
prev: /html-css/docs/html-basics.html
next: html-css/docs/css-basics.html
---

## 🔢 What is `Math.random()` in JavaScript?

`Math.random()` is a built-in JavaScript method that returns a **pseudo-random floating-point number** between `0` (inclusive) and `1` (exclusive). That means it can return `0`, but **never** `1`.

---

## 📚 Syntax

```javascript
Math.random()
```

- No parameters are needed.
- Returns a number like `0.6543`, `0.1234`, etc.

---

## 🧪 Simple Examples

### 1. Random number between 0 and 1:
```javascript
let num = Math.random();
console.log(num); // e.g., 0.734562
```

### 2. Random number between 0 and 10:
```javascript
let num = Math.random() * 10;
console.log(num); // e.g., 7.3456
```

### 3. Random integer between 1 and 100:
```javascript
let num = Math.floor(Math.random() * 100) + 1;
console.log(num); // e.g., 84
```

---

## 🌍 Real-World Example: Dice Roll Simulator 🎲

Simulate rolling a 6-sided dice:

```javascript
function rollDice() {
  return Math.floor(Math.random() * 6) + 1;
}

console.log("You rolled:", rollDice()); // Outputs a number between 1 and 6
```

---

## 💡 Why Use `Math.random()`?

- Creating games
- Randomizing colors or content. [Example: Change Background Color Randomly](/javascript/docs/basics/real-world-javascript-examples.md#-3-change-background-color-randomly)
- Simulating chance (coin flips, dice, etc.)
- Shuffling arrays or selecting random items

