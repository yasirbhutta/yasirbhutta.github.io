---
layout: page
title: "PHP foreach Statement"
description: Learn PHP basics with this beginner-friendly guide. Understand PHP syntax, variables, functions, and more to start building dynamic web applications.
keywords: PHP basics, PHP tutorial, PHP for beginners, PHP syntax, PHP variables, PHP functions, learn PHP, PHP fundamentals, PHP programming
toc: toc/php.html
course: php
topic: "control-flow"
mini_project: true
prev: /php/docs/loops-for/
next: /php/docs/loops-while/
---

### foreach Statement

- The foreach construct provides an easy way to iterate over arrays.
- foreach works only on arrays and objects, and will issue an error when you try to use it on a variable with a different data type or an uninitialized variable.

There are two syntaxes:

#### Syntax - foreach loop

>foreach (iterable_expression as $value)  
    statement  
foreach (iterable_expression as $key => $value)  
    statement  

- The first form traverses the iterable given by iterable_expression. On each iteration, the value of the current element is assigned to $value.
- The second form will additionally assign the current element's key to the $key variable on each iteration.

In order to be able to directly modify array elements within the loop precede $value with **&**. In that case the value will be assigned by reference.

#### Example #1 foreach loop example

```php
<?php
$arr = array(1, 2, 3, 4);
foreach ($arr as &$value) {
    $value = $value * 2;
}
// $arr is now array(2, 4, 6, 8)
unset($value); // break the reference with the last element
?>
```

**Warning:** Reference of a $value and the last array element remain even after the foreach loop. It is recommended to destroy it by unset().

#### Example #2 foreach loop example

```php
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>PHP - foreach</title>
    </head>
    <body>
    
    <?php

$colors = array("red", "green", "blue", "yellow","pink");

foreach ($colors as $i)
{
echo "<h1 style=". "background-color:$i>" . $i ."</h1><br>";
}
?>
    </body>
</html>
```

Some more examples to demonstrate usage:

```php
<?php

/* foreach example 1: value only */

$a = array(1, 2, 3, 17);

foreach ($a as $v) {
    echo "Current value of \$a: $v.\n";
}

/* foreach example 2: value (with its manual access notation printed for illustration) */

$a = array(1, 2, 3, 17);

$i = 0; /* for illustrative purposes only */

foreach ($a as $v) {
    echo "\$a[$i] => $v.\n";
    $i++;
}

/* foreach example 3: key and value */

$a = array(
    "one" => 1,
    "two" => 2,
    "three" => 3,
    "seventeen" => 17
);

foreach ($a as $k => $v) {
    echo "\$a[$k] => $v.\n";
}

/* foreach example 4: multi-dimensional arrays */
$a = array();
$a[0][0] = "a";
$a[0][1] = "b";
$a[1][0] = "y";
$a[1][1] = "z";

foreach ($a as $v1) {
    foreach ($v1 as $v2) {
        echo "$v2\n";
    }
}

/* foreach example 5: dynamic arrays */

foreach (array(1, 2, 3, 4, 5) as $v) {
    echo "$v\n";
}
?>
```

Further reading:

- [foreach - Manual - PHP](https://www.php.net/manual/en/control-structures.foreach.php)
