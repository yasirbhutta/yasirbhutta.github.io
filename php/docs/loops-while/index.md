---
layout: page
title: "PHP while Loop Guide with Syntax and Examples"
description: Understand the while loop in PHP for repeated execution based on conditions. Includes syntax, examples, and tips to write cleaner looping logic in PHP.
keywords: php while loop, php loops tutorial, while loop syntax php, php programming basics, php control structures, php documentation, php while loop examples
toc: toc/php.html
course: php
topic: "control-flow"
mini_project: true
prev: /php/docs/loops-foreach/
next: /php/docs/loops-do-while/
---

## 🔁 PHP `while` Loop

The `while` loop is one of the simplest and most commonly used loops in PHP. It allows you to run a block of code **as long as** a specified condition is **true**.

### 🧠 How it Works

The basic syntax of a `while` loop is:

```php
while (condition) {
    // Code to execute as long as condition is true
}
```

* **Before** each iteration (loop cycle), PHP checks the condition.
* If the condition is `true`, the code inside the loop runs.
* Once the condition becomes `false`, the loop stops.
* If the condition is `false` from the start, the loop will not run at all.

### 🔄 Alternate Syntax

You can also use an alternate form, especially useful in templates or HTML-heavy code:

```php
while (condition):
    // Code to execute
endwhile;
```

---

### ✅ Example 1: Counting from 1 to 10

```php
<?php
$i = 1;

while ($i <= 10) {
    echo $i . " ";
    $i++;  // Increases $i by 1 each time
}
?>
```

**Output:**

```
1 2 3 4 5 6 7 8 9 10
```

👉 In this example:

* The loop starts with `$i = 1`.
* It runs as long as `$i <= 10`.
* After each loop, `$i` increases by 1 using `$i++`.

---

### ✅ Example 2: Using Alternate Syntax

```php
<?php
$i = 1;

while ($i <= 10):
    echo $i . " ";
    $i++;
endwhile;
?>
```

This gives the same output as Example 1, just with a different style of writing.

---

### ✅ Example 3: Inside an HTML Page

```php
<!DOCTYPE html>
<html lang="en">
<head>
    <title>PHP - While Loop Example</title>
</head>
<body>

<?php
$x = 1;

while ($x <= 5) {
    echo "The number is: $x <br>";
    $x++;
}
?>

</body>
</html>
```

**Output in browser:**

```
The number is: 1
The number is: 2
The number is: 3
The number is: 4
The number is: 5
```

---

### 📝 Tips

* Always make sure your condition will eventually become false. Otherwise, you’ll create an **infinite loop** that never stops.
* The loop variable (like `$i` or `$x`) usually gets updated inside the loop to avoid infinite looping.
* Use `.` to **concatenate** (join) strings and variables, like in `echo $i . " ";`.

---

further reading:

- [while - Manual - PHP](https://www.php.net/manual/en/control-structures.while.php)

