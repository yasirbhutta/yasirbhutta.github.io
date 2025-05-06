---
layout: page
title: "PHP if Statements"
description: Learn PHP basics with this beginner-friendly guide. Understand PHP syntax, variables, functions, and more to start building dynamic web applications.
keywords: PHP basics, PHP tutorial, PHP for beginners, PHP syntax, PHP variables, PHP functions, learn PHP, PHP fundamentals, PHP programming
toc: toc/php.html
course: php
topic: "control-flow"
mini_project: true
prev: /php/docs/control-flow.html
next: /php/docs/switch/
---

## if Statement

- The if construct is one of the most important features of many languages, PHP included.
- It allows for conditional execution of code fragments. PHP features an if structure that is similar to that of C.
- If statements can be nested infinitely within other if statements, which provides you with complete flexibility for conditional execution of the various parts of your program.

### Syntax - if Statement

```php
>if (expr)  
  statement
```

### Syntax - if-elseif-else Statement

```php
> if (condition) {  
    code to be executed if this condition is true;  
} elseif (condition) {  
    code to be executed if this condition is true;  
} else {  
    code to be executed if all conditions are false;  
}  
```

The following example would display a is bigger than b if $a is bigger than $b:

### Example #1 if example

```php
<?php
if ($a > $b)
  echo "a is bigger than b";
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
