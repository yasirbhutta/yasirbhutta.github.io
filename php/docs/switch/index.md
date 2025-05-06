### switch statement

- The switch statement is similar to a series of IF statements on the same expression.
- In many occasions, you may want to compare the same variable (or expression) with many different values, and execute a different piece of code depending on which value it equals to. This is exactly what the switch statement is for.

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
for **explanation** of the example, see [Switch-Case Example in PHP: Handling Multiple Cases Together](switch/solutions/switch-example3.md)

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
    <h1>PHP - Switch</h1>
    <?php
$favcolor = "blue";
echo "<h2>My favorite color is " . $favcolor . "</h2>";
switch ($favcolor) {
    case "red":
        echo "<h2 style='color:" . $favcolor . "'>Your favorite color is red!</h2>";
        break;
    case "blue":
        echo "<h2 style='color:" . $favcolor . "'>Your favorite color is blue!</h2>";
        break;
    case "green":
        echo "<h2 style='color:" . $favcolor . "'>Your favorite color is green!</h2>";
        break;
    default:
        echo "Your favorite color is neither red, blue, nor green!";
}
?>
</body>

</html>
```

further reading:

- [switch - Manual - PHP](https://www.php.net/manual/en/control-structures.switch.php)
