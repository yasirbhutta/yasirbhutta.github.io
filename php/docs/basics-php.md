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
**Example 1**

```php
<?php
// Show all information, defaults to INFO_ALL
phpinfo();
// Show just the module information.
// phpinfo(8) yields identical results.
phpinfo(INFO_MODULES);
?>
```
**Example 2**

**Visual Studio Code - PHP Extension Pack**

[https://marketplace.visualstudio.com/items?itemName=xdebug.php-pack](https://marketplace.visualstudio.com/items?itemName=xdebug.php-pack)


```php
In PHP, all keywords (e.g. if, else, while, echo, etc.), classes, functions, and user-defined functions are NOT case-sensitive.
<?php

ECHO "Hello World!<br>";
echo "Hello World!<br>";
EcHo "Hello World!<br>";
?>
```
**Example 3:**[GitHub Code](https://github.com/yasirbhutta/php-examples/blob/master/basics/case-01.php)


all variable names are case-sensitive.
```php
<?php
// 
$color = "red";
$COLOR="GREEN";
echo "My car is " . $color . "<br>";
echo "My house is " . $COLOR . "<br>";
echo "My boat is " . $coLOR . "<br>";
?>
```
**Example 4:**[GitHub code](https://github.com/yasirbhutta/php-examples/blob/master/basics/case-02.php)

### Variables

```php
<?php

$txt = "W3Schools.com";
echo "I love $txt!";
// produce the same output
echo "<br>";
echo "I love " . $txt . "!";

?>
```
**Example 5**:[GitHub code](https://github.com/yasirbhutta/php-examples/blob/master/basics/var-01.php)


```php
<?php

$x = 5;
$y = 4;
echo $x + $y;

?>
```
**Example 6**: [GitHub code](https://github.com/yasirbhutta/php-examples/blob/master/basics/var-02.php)

#### global scope variable

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
**Example 7**: [GitHub code](https://github.com/yasirbhutta/php-examples/blob/master/basics/var-03.php)

#### local scope variable

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
**Example 8:**[GitHub code](https://github.com/yasirbhutta/php-examples/blob/master/basics/var-04.php)