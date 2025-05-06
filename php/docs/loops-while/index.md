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

### while Statement

- while loops are the simplest type of loop in PHP. They behave just like their C counterparts. The basic form of a while statement is:

>while (expr)  
    statement  

- The meaning of a while statement is simple. It tells PHP to execute the nested statement(s) repeatedly, as long as the while expression evaluates to true.
- The value of the expression is checked each time at the beginning of the loop, so even if this value changes during the execution of the nested statement(s), execution will not stop until the end of the iteration (each time PHP runs the statements in the loop is one iteration).
- If the while expression evaluates to false from the very beginning, the nested statement(s) won't even be run once.
- Like with the if statement, you can group multiple statements within the same while loop by surrounding a group of statements with curly braces, or by using the alternate syntax:

>while (expr):  
    statement  
    ...  
endwhile;

The following examples are identical, and both print the numbers 1 through 10:

#### Example #1 while loop example

```php
<?php
/* example 1 */

$i = 1;
while ($i <= 10) {
    echo $i++;  /* the printed value would be
                   $i before the increment
                   (post-increment) */
}

/* example 2 */

$i = 1;
while ($i <= 10):
    echo $i;
    $i++;
endwhile;
?>
```

#### Example #2 while loop example

```php
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>PHP - While Loop</title>
    </head>
    <body>
    <?php

$x = 1;
while($x <= 5) {
    echo "The number is: $x <br>";
    $x++;
}
?>
    </body>
</html>
```

further reading:

- [while - Manual - PHP](https://www.php.net/manual/en/control-structures.while.php)

