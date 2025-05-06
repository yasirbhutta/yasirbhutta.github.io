---
layout: page
title: "PHP for Statement"
description: Learn PHP basics with this beginner-friendly guide. Understand PHP syntax, variables, functions, and more to start building dynamic web applications.
keywords: PHP basics, PHP tutorial, PHP for beginners, PHP syntax, PHP variables, PHP functions, learn PHP, PHP fundamentals, PHP programming
toc: toc/php.html
course: php
topic: "control-flow"
mini_project: true
next: /php/docs/basics/what-is-php.html
---

### for Statement

- for loops are the most complex loops in PHP. They behave like their C counterparts. The syntax of a for loop is:

#### Syntax - for loop

**Syntax:**

```php
for (initialization; condition; increment) {
    // code to be executed
}
```

- The first expression (expr1) is evaluated (executed) once unconditionally at the beginning of the loop.
- In the beginning of each iteration, expr2 is evaluated. If it evaluates to true, the loop continues and the nested statement(s) are executed. If it evaluates to false, the execution of the loop ends.
- At the end of each iteration, expr3 is evaluated (executed)
- Each of the expressions can be empty or contain multiple expressions separated by commas


Consider the following examples. All of them display the numbers 1 through 10:

```php
<?php

// example 1

for ($i = 1; $i <= 10; $i++) {
    echo $i;
}

// example 2

for ($i = 1; ; $i++) {
    if ($i > 10) {
        break;
    }
    echo $i;
}

// example 3

$i = 1;
for (; ; ) {
    if ($i > 10) {
        break;
    }
    echo $i;
    $i++;
}

// example 4

for ($i = 1, $j = 0; $i <= 10; $j += $i, print $i, $i++);
?>
```

#### Example #3 for loop example

```php
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>PHP - For Loop</title>
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

further reading:

- [for - Manual -PHP](https://www.php.net/manual/en/control-structures.for.php)
