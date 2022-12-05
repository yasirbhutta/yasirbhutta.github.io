# [PHP](../index.md)

## PHP Basics

- [Download PDF](basics-php.pdf)
- [Download examples Codes](https://github.com/yasirbhutta/php-examples)

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

**Example 1**

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
**Example 2**

```php
<?php
// Show all information, defaults to INFO_ALL
phpinfo();
// Show just the module information.
// phpinfo(8) yields identical results.
phpinfo(INFO_MODULES);
?>
```

**Visual Studio Code - PHP Extension Pack**

[https://marketplace.visualstudio.com/items?itemName=xdebug.php-pack](https://marketplace.visualstudio.com/items?itemName=xdebug.php-pack)

**Example 3**

```php
<?php
/* In PHP, all keywords (e.g. if, else, while, echo, etc.), classes, functions, and user-defined functions are NOT case-sensitive.*/

ECHO "Hello World!<br>";
echo "Hello World!<br>";
EcHo "Hello World!<br>";
?>
```
[GitHub Code](https://github.com/yasirbhutta/php-examples/blob/master/basics/case-01.php)

**Example 4**

```php
<?php
// all variable names are case-sensitive.
$color = "red";
$COLOR="GREEN";
echo "My car is " . $color . "<br>";
echo "My house is " . $COLOR . "<br>";
echo "My boat is " . $coLOR . "<br>";
?>
```
[GitHub code](https://github.com/yasirbhutta/php-examples/blob/master/basics/case-02.php)

### Variables

**Example 1**

```php
<?php

$txt = "W3Schools.com";
echo "I love $txt!";
// produce the same output
echo "<br>";
echo "I love " . $txt . "!";

?>
```
[GitHub code](https://github.com/yasirbhutta/php-examples/blob/master/basics/var-01.php)

**Example 2**

```php
<?php

$x = 5;
$y = 4;
echo $x + $y;

?>
```
[GitHub code](https://github.com/yasirbhutta/php-examples/blob/master/basics/var-02.php)

**Example 3**


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
[GitHub code](https://github.com/yasirbhutta/php-examples/blob/master/basics/var-03.php)

**Example 4**

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
[GitHub code](https://github.com/yasirbhutta/php-examples/blob/master/basics/var-04.php)



