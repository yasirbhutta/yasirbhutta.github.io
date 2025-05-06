---
layout: page
title: "PHP for Loop Tutorial with Syntax and Examples"
description: Master the for loop in PHP to execute code repeatedly with control. Explore syntax, practical examples, and best practices for efficient PHP programming.
keywords: php for loop, php loop examples, php loops tutorial, php for loop syntax, php programming, control structures in php, php docs, how to use for loop in php
toc: toc/php.html
course: php
topic: "control-flow"
mini_project: true
prev: /php/docs/switch/
next: /php/docs/loops-foreach/
---

## 🔁 `for` Statement in PHP

The `for` loop is one of the most commonly used loops in PHP. It lets you repeat a block of code a certain number of times. If you've used `for` loops in languages like C or JavaScript, PHP's version will feel familiar.

---

## 📌 Syntax

```php
for (initialization; condition; increment) {
    // Code to be repeated
}
```

### 🧩 Explanation:

* **initialization** – This runs **once** at the beginning. It's usually used to set up a counter variable.
* **condition** – This is checked **before every loop**. If it's `true`, the loop runs again. If it's `false`, the loop stops.
* **increment** – This runs **at the end of every loop iteration**, usually to update the counter.

> 💡 All three parts are optional, but at least the semicolons (`;`) must be there.

---

## ✅ Simple Example

```php
<?php
for ($i = 1; $i <= 5; $i++) {
    echo "Number: $i <br>";
}
?>
```

**Output:**

```
Number: 1  
Number: 2  
Number: 3  
Number: 4  
Number: 5
```

---

## 🔄 More Examples

### Example 1 – Classic `for` loop

```php
for ($i = 1; $i <= 10; $i++) {
    echo $i;
}
```

### Example 2 – No condition in the `for` loop

```php
for ($i = 1; ; $i++) {
    if ($i > 10) {
        break; // Stop the loop manually
    }
    echo $i;
}
```

### Example 3 – All parts inside the loop

```php
$i = 1;
for (; ; ) {
    if ($i > 10) break;
    echo $i;
    $i++;
}
```

## 🌐 Example in an HTML Page

```php
<!DOCTYPE html>
<html lang="en">
<head>
    <title>PHP For Loop</title>
</head>
<body>

<?php
for ($x = 0; $x <= 10; $x++) {
    echo "The number is: $x <br>";
}
?>

</body>
</html>
```

---

## 📝 Summary

* Use `for` loops when you know **exactly how many times** you want to run a block of code.
* You can skip any part of the loop structure, but be careful to avoid **infinite loops**.
* The loop ends when the condition becomes `false`.

---

further reading:

- [for - Manual -PHP](https://www.php.net/manual/en/control-structures.for.php)
