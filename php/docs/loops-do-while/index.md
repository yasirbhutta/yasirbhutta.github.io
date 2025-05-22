---
layout: page
title: "PHP do...while Loop Explained with Syntax & Examples"
description: Learn how the do...while loop works in PHP. Discover its syntax, how it differs from while, and view practical examples to master this loop construct.
keywords: php do while loop, php do while syntax, php loops tutorial, php loop examples, php control structures, php do while vs while, php programming, php docs
toc: toc/php.html
course: php
topic: "control-flow"
mini_project: true
prev: /php/docs/loops-while/
next: /php/docs/forms/
---

## 🔄 The `do-while` Loop in PHP

A `do-while` loop is very similar to a `while` loop, but with one key difference: the condition is **checked after** the loop’s code has been executed. This means the loop **always runs at least once**, regardless of whether the condition is true or false at the start.

---

### 🧠 Key Differences Between `do-while` and `while` Loops

* **`while` Loop:** Checks the condition **before** executing the loop. If the condition is false initially, the loop will **never run**.
* **`do-while` Loop:** Executes the loop **once**, then checks the condition. If the condition is false after the first iteration, the loop stops.

---

### ✅ Syntax of `do-while` Loop

```php
do {
    // Code to execute
} while (condition);
```

* **Code to execute:** This block will run **at least once**.
* **Condition:** The loop continues running as long as this condition is true.

---

### 📝 Example #1: Basic `do-while` Loop

```php
<?php
$i = 0;
do {
    echo $i;  // This will print 0
} while ($i > 0);  // The condition is false, so the loop stops after one iteration
?>
```

**Explanation:**

* `$i` is initially 0.
* The loop runs **once** before the condition `$i > 0` is checked.
* Since `$i > 0` is false, the loop stops after the first iteration.

---

### 📝 Example #2: Looping with `do-while`

```php
<!DOCTYPE html>
<html lang="en">
<head>
    <title>PHP - Do While Loop Example</title>
</head>
<body>

<?php
$x = 6;  // Set initial value of $x

do {
    echo "The number is: $x <br>";  // Prints $x
    $x++;  // Increments $x
} while ($x <= 5);  // Loop stops because $x is no longer <= 5
?>

</body>
</html>
```

**Output:**

```
The number is: 6
```

**Explanation:**

* The loop executes once with `$x = 6`, printing "The number is: 6".
* The condition `$x <= 5` is checked after the first iteration, and since it's false, the loop stops.

---

### ⚡ Key Points:

* The `do-while` loop **always runs at least once**, regardless of the condition.
* The **condition is checked after the code runs**, unlike the `while` loop where the condition is checked first.
* It's useful when you want the loop body to run **at least once** before any checks are made (e.g., user input or menu selection).

---



## further reading:

- [do-while - Manaual - PHP](https://www.php.net/manual/en/control-structures.do.while.php)