# [PHP](../index.md)

## PHP Basics

- [Download PDF](basics-php.pdf)
- [Download examples Codes](https://github.com/yasirbhutta/php-examples)

**Visual Studio Code - PHP Extension Pack**

[https://marketplace.visualstudio.com/items?itemName=xdebug.php-pack](https://marketplace.visualstudio.com/items?itemName=xdebug.php-pack)

### Online PHP Editors

- [https://www.tutorialspoint.com/execute_php_online.php](https://www.tutorialspoint.com/execute_php_online.php)
- [https://www.codingrooms.com/compiler/php/](https://www.codingrooms.com/compiler/php/
)

### What is PHP

PHP (recursive acronym for PHP: Hypertext Preprocessor) is a widely-used open source general-purpose scripting language that is especially suited for web development and can be embedded into HTML.

### What is a PHP File?

- PHP files can contain text, HTML, CSS, JavaScript, and PHP code.
- PHP code are executed on the server, and the result is returned to the browser as plain HTML.
- PHP files have extension ".php".


```php
<!DOCTYPE html>
<html>
 <head>
  <title>PHP Test</title>
 </head>
 <body>
 <?php echo '<p>Hello World</p>'; ?> 
 </body>
</html>
```

**Example #2 phpinfo example**

```php
<?php
// Show all information, defaults to INFO_ALL
phpinfo();
// Show just the module information.
// phpinfo(8) yields identical results.
phpinfo(INFO_MODULES);
?>
```

In PHP, all keywords (e.g. if, else, while, echo, etc.), classes, functions, and user-defined functions are NOT case-sensitive.

**Example #3 echo example**

```php
<?php

ECHO "Hello World!<br>";
echo "Hello World!<br>";
EcHo "Hello World!<br>";
?>
```
**Example 3:**[GitHub Code](https://github.com/yasirbhutta/php-examples/blob/master/basics/case-01.php)



### Variables


all variable names are case-sensitive.

**Example #1 variable example**

```php
<?php

$color = "red";
$COLOR="GREEN";
echo "My car is " . $color . "<br>";
echo "My house is " . $COLOR . "<br>";
echo "My boat is " . $coLOR . "<br>";

?>
```
[Download example code](https://github.com/yasirbhutta/php-examples/blob/master/basics/case-02.php)

**Example #2 variable example**

```php
<?php

$txt = "W3Schools.com";
echo "I love $txt!";
// produce the same output
echo "<br>";
echo "I love " . $txt . "!";

?>
```
[Download example code](https://github.com/yasirbhutta/php-examples/blob/master/basics/var-01.php)

**Example #3 variable example**

```php
<?php

$x = 5;
$y = 4;
echo $x + $y;

?>
```
[Download example code](https://github.com/yasirbhutta/php-examples/blob/master/basics/var-02.php)

#### Local scope variable

**Example #1 local scope variable example**

```php
<?php
function myTest() {
    $x = 5; // local scope
    echo "<p>Variable x inside function is: $x</p>";
} 
myTest();

// using x outside the function will generate an error
echo "<p>Variable x outside function is: $x</p>";
?>
```
[Download example code](https://github.com/yasirbhutta/php-examples/blob/master/basics/var-04.php)

#### Global scope variable

**Example #1 global scope variable example**

```php
<?php
$x = 5; // global scope

function myTest() {
    // using x inside this function will generate an error
    echo "<p>Variable x inside function is: $x</p>";
} 
myTest();

echo "<p>Variable x outside function is: $x</p>";
?>
```
[Download example code](https://github.com/yasirbhutta/php-examples/blob/master/basics/var-03.php)

**Example #2 use global scope variable in function**

```php
<?php
$x = 5; // global scope
$y = 10;

function myTest() {
 global $x, $y;  // use global scope variable in function
    $y = $x + $y;
    
}

myTest();
echo $y; // outputs 15
?>
```
[Download example code](https://github.com/yasirbhutta/php-examples/blob/master/basics/var-05.php)

#### $GLOBALS

An associative array containing references to all variables which are currently defined in the global scope of the script. The variable names are the keys of the array.

**Example #1 $GLOBALS example**

```php
<?php
$x = 5;
$y = 10;

function myTest() {
    $GLOBALS['y'] = $GLOBALS['x'] + $GLOBALS['y'];
} 

myTest();
echo $y; // outputs 15
?>
```
[Download example code](https://github.com/yasirbhutta/php-examples/blob/master/basics/var-06.php)

#### Static variable

 A static int variable remains in memory while the program is running. A normal or auto variable is destroyed when a function call where the variable was declared is over. [1]

**Example #1 static variable example**

```php
<?php
function myTest() {
    static $x = 0;
    echo $x . "<br \>";
    $x++;
}

myTest();
myTest();
myTest();
myTest();
?>
```
**Example 11**: [GitHub code](https://github.com/yasirbhutta/php-examples/blob/master/basics/var-07.php)

### String functions


### References

1. [Static variables](https://www.geeksforgeeks.org/static-variables-in-c/)



**Muhammad Yasir Bhutta**

- [Web](https://yasirbhutta.github.io/)
- [Youtube](https://www.youtube.com/yasirbhutta)
- [Facebook](https://www.facebook.com/yasirbhutta786)
- [Twitter](https://twitter.com/yasirbhutta)