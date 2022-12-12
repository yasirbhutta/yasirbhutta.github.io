# PHP

## Control Flow Statements

- [Download examples code](https://github.com/yasirbhutta/php-examples/tree/master/basics)

### if Statement

#### Syntax - if statement

> if (condition) {  
    code to be executed if this condition is true;  
} elseif (condition) {  
    code to be executed if this condition is true;  
} else {  
    code to be executed if all conditions are false;  
}  

#### Example #1 IF example

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
// if..elseif..elese
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

#### Example #2 switch example

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

for (expr1; expr2; expr3)
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

#### Syntax - foreach loop

>foreach ($array as $value) {
    code to be executed;
}

#### Example #4 foreach loop example

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

### while Statement

#### Syntax - while loop

>while (condition is true) {
    code to be executed;
}

#### Example #5 while loop example

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

### The dowhile Statement

- do while loop would execute its statements at least once, even if the condition is false the first time.

#### Syntax - dowhile loop

>do {
    code to be executed;
} while (condition is true);

#### Example #6 dowhile loop example

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

### The break Statement

### The continue Statement

### The try Statement
