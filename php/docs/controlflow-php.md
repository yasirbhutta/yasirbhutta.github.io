# PHP

## Control Flow Statements

- [Download examples code](https://github.com/yasirbhutta/php-examples/tree/master/basics)

### if Statement

- The if construct is one of the most important features of many languages, PHP included.
- It allows for conditional execution of code fragments. PHP features an if structure that is similar to that of C.
- If statements can be nested infinitely within other if statements, which provides you with complete flexibility for conditional execution of the various parts of your program.

#### Syntax - if Statement

>if (expr)  
  statement

#### Syntax - if-elseif-else Statement

> if (condition) {  
    code to be executed if this condition is true;  
} elseif (condition) {  
    code to be executed if this condition is true;  
} else {  
    code to be executed if all conditions are false;  
}  

further reading:

- [if - Manual - PHP](https://www.php.net/manual/en/control-structures.if.php)

The following example would display a is bigger than b if $a is bigger than $b:

#### Example #1 if example

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

### switch statement

- The switch statement is similar to a series of IF statements on the same expression. 
- In many occasions, you may want to compare the same variable (or expression) with many different values, and execute a different piece of code depending on which value it equals to. This is exactly what the switch statement is for.

#### syntax

#### Example #1 switch structure

```php
<?php
// This switch statement:

switch ($i) {
    case 0:
        echo "i equals 0";
        break;
    case 1:
        echo "i equals 1";
        break;
    case 2:
        echo "i equals 2";
        break;
}

// Is equivalent to:

if ($i == 0) {
    echo "i equals 0";
} elseif ($i == 1) {
    echo "i equals 1";
} elseif ($i == 2) {
    echo "i equals 2";
}
?>
```

#### Example #2 switch example

```php
<?php
switch ($i) {
    case 0:
        echo "i equals 0";
    case 1:
        echo "i equals 1";
    case 2:
        echo "i equals 2";
}
?>
```

The statement list for a case can also be empty, which simply passes control into the statement list for the next case.

#### Example #3 switch with empty case example

```php
<?php
switch ($i) {
    case 0:
    case 1:
    case 2:
        echo "i is less than 3 but not negative";
        break;
    case 3:
        echo "i is 3";
}
?>
```

A special case is the default case. This case matches anything that wasn't matched by the other cases. For example:

#### Example #4 default case

```php
<?php
switch ($i) {
    case 0:
        echo "i equals 0";
        break;
    case 1:
        echo "i equals 1";
        break;
    case 2:
        echo "i equals 2";
        break;
    default:
       echo "i is not equal to 0, 1 or 2";
}
?>
```

A case value may be given as an expression. However, that expression will be evaluated on its own and then loosely compared with the switch value. That means it cannot be used for complex evaluations of the switch value. For example:

#### Example #5 switch example

```php
<?php
$target = 1;
$start = 3;

switch ($target) {
    case $start - 1:
        print "A";
        break;
    case $start - 2:
        print "B";
        break;
    case $start - 3:
        print "C";
        break;
    case $start - 4:
        print "D";
        break;
}

// Prints "B"
?>
```

It's possible to use a semicolon instead of a colon after a case like:

#### Example #6 switch example

```php
<?php
switch($equipments)
{
    case 'keyboard';
    case 'mouse';
    case 'motherboard';
    case 'speaker';
        echo 'Good choice';
        break;
    default;
        echo 'Please make a new selection...';
        break;
}
?>
```

#### Example #7 switch example

```php
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>PHP - Switch</title>
    </head>
    <body>
    <?php
$favcolor = "yellow";

switch ($favcolor) {
    case "red":
        echo "Your favorite color is red!";
        break;
    case "blue":
        echo "Your favorite color is blue!";
        break;
    case "green":
        echo "Your favorite color is green!";
        break;
    default:
        echo "Your favorite color is neither red, blue, nor green!";
}
?>
    </body>
</html>
```

### for Statement

- for loops are the most complex loops in PHP. They behave like their C counterparts. The syntax of a for loop is:

#### Syntax - for loop

>for (expr1; expr2; expr3)
    statement

- The first expression (expr1) is evaluated (executed) once unconditionally at the beginning of the loop.
- In the beginning of each iteration, expr2 is evaluated. If it evaluates to true, the loop continues and the nested statement(s) are executed. If it evaluates to false, the execution of the loop ends.
- At the end of each iteration, expr3 is evaluated (executed)
- Each of the expressions can be empty or contain multiple expressions separated by commas

further reading:

- [for - Manual -PHP](https://www.php.net/manual/en/control-structures.for.php)

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

Further reading:

- [foreach - Manual - PHP](https://www.php.net/manual/en/control-structures.foreach.php)

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

further reading:

- [while - Manual - PHP](https://www.php.net/manual/en/control-structures.while.php)

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

### The do-while Statement

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

Muhammad Yasir Bhutta

- [Web](https://yasirbhutta.github.io/)
- [Youtube](https://www.youtube.com/yasirbhutta)
- [Facebook](https://www.facebook.com/yasirbhutta786)
- [Twitter](https://twitter.com/yasirbhutta)
