---
layout: post
title: "JavaScript Math.floor() Explained" 
description: "Learn how to use JavaScript’s Math.floor() function to round numbers down to the nearest integer. Includes clear examples and real-world use cases for web development and random number generation."  
keywords: "JavaScript Math.floor, JavaScript rounding, round down JavaScript, JavaScript number functions, Math.floor tutorial, JavaScript floor example, JavaScript Math methods, JavaScript basics, beginner JavaScript"
toc: toc/javascript.html
topic: "basics"
course: "javascript"
prev: /html-css/docs/html-basics.html
next: html-css/docs/css-basics.html
---

In JavaScript, `Math.floor()` is a built-in function that **rounds a number *down* to the nearest integer**.

### Syntax:
```javascript
Math.floor(x)
```

- `x` is the number you want to round down.

### Example:
```javascript
Math.floor(4.7);  // returns 4
Math.floor(4.1);  // returns 4
Math.floor(-4.7); // returns -5
```

### When is it used?

`Math.floor()` is often used with `Math.random()` to generate random **integers**:

```javascript
// Random integer between 0 and 9
let randomInt = Math.floor(Math.random() * 10);
```
