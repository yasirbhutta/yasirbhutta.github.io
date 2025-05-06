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
