---
layout: page
title: "PHP do-while Statement"
description: Learn PHP basics with this beginner-friendly guide. Understand PHP syntax, variables, functions, and more to start building dynamic web applications.
keywords: PHP basics, PHP tutorial, PHP for beginners, PHP syntax, PHP variables, PHP functions, learn PHP, PHP fundamentals, PHP programming
toc: toc/php.html
course: php
topic: "control-flow"
mini_project: true
prev: /php/docs/loops-while/
next: /php/docs/forms.html
---

## The do-while Statement

- do-while loops are very similar to while loops, except the truth expression is checked at the end of each iteration instead of in the beginning.
- The main difference from regular while loops is that the first iteration of a do-while loop is guaranteed to run (the truth expression is only checked at the end of the iteration), whereas it may not necessarily run with a regular while loop (the truth expression is checked at the beginning of each iteration, if it evaluates to false right from the beginning, the loop execution would end immediately).

#### Syntax - do-while loop

>do {  
    code to be executed;  
} while (condition is true);  

further reading:

- [do-while - Manaual - PHP](https://www.php.net/manual/en/control-structures.do.while.php)

#### Example #1 do-while loop example

```php
<?php
$i = 0;
do {
    echo $i;
} while ($i > 0);
?>
```

The above loop would run one time exactly, since after the first iteration, when truth expression is checked, it evaluates to false ($i is not bigger than 0) and the loop execution ends.

#### Example #2 dowhile loop example

```php
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>PHP - Do While </title>
    </head>
    <body>
    <?php
/*$x = 1; 
do {
    echo "The number is: $x <br>";
    $x++;
} while ($x <= 5);*/

// example2

$x = 6;
do {
    echo "The number is: $x <br>";
    $x++;
} while ($x <= 5);
?>
    </body>
</html>
```
