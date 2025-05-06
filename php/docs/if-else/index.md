---
layout: page
title: "PHP if else Statement Explained with Syntax & Examples"
description: Learn PHP basics with this beginner-friendly guide. Understand PHP syntax, variables, functions, and more to start building dynamic web applications.
keywords: PHP if else, PHP conditional statements, PHP if statement syntax, PHP if else examples, PHP elseif tutorial, PHP control structures, Learn PHP basics
toc: toc/php.html
course: php
topic: "control-flow"
mini_project: true
prev: /php/docs/control-flow.html
next: /php/docs/switch/
---

## What is an if else Statement in PHP?

- The if construct is one of the most important features of many languages, PHP included.
- It allows for conditional execution of code fragments. PHP features an if structure that is similar to that of C.
- If statements can be nested infinitely within other if statements, which provides you with complete flexibility for conditional execution of the various parts of your program.

## PHP if else Syntax

```php
if (condition) {
    // code to execute if condition is true
} else {
    // code to execute if condition is false
}
```

## Syntax - if-elseif-else Statement

```php
if (condition) {  
    code to be executed if this condition is true;  
} elseif (condition) {  
    code to be executed if this condition is true;  
} else {  
    code to be executed if all conditions are false;  
}  
```

The following example would display a is bigger than b if $a is bigger than $b:

## Example #1: Using elseif in PHP

```php
<?php
if ($a > $b) {
    echo "a is greater than b";
} elseif ($a == $b) {
    echo "a is equal to b";
} else {
    echo "a is less than b";
}
?>
```

#### Example #2 IF example

```php
<!DOCTYPE html>
<html lang="en">

<head>
    <title>PHP - The if...elseif....else Statement</title>
</head>

<body>
    <?php

    // i for Minutes with leading zero, s for Seconds with leading zero
    echo "Today is " . date("d/m/Y") . "<br>";
    echo "Minutes:" . date("i");
    echo "<br> Seconds:" . date("s") . "<br>";
    //
    // if..elseif..else
    //
    $t = date("H");
    if ($t < "10") {
        echo "Have a good morning!";
    } elseif ($t < "20") {
        echo "Have a good day!";
    } else {
        echo "Have a good night!";
    }
    ?>
</body>
</html>
```

further reading:

- [if - Manual - PHP](https://www.php.net/manual/en/control-structures.if.php)
