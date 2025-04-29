---
layout: page
title: "PHP Basics Tutorial – Variable Scope in PHP"
description: Understand variable scope in PHP, including local and global variables. Learn how to use the global keyword and access global variables inside functions with clear code examples.
keywords: PHP variable scope, local scope in PHP, global scope in PHP, PHP global keyword, PHP function variables, PHP $GLOBALS, variable accessibility in PHP, PHP scope example
toc: toc/php.html
course: php
topic: "basics"
mini_project: true
---

## **What is Variable Scope?**
- The scope of a variable refers to where it is accessible within the code.
  
## **Local Scope**:
- A variable defined inside a function is **local** to that function and cannot be accessed outside.

#### Example: Local Scope

```php
<?php
function testFunction() {
    $x = 10;  // Local variable
    echo $x;  // Output: 10
}

testFunction();
echo $x;  // Error: Undefined variable
?>
```

## **Global Scope**:
- Variables defined outside functions are **global** and can be accessed globally.

```php
<?php
$x = 10;  // Global variable

function testFunction() {
    echo $GLOBALS['x'];  // Accessing global variable
}

testFunction();  // Output: 10
?>
```

$GLOBALS - The $GLOBALS array is an associative array with the name of the global variable being the key and the contents of that variable being the value of the array element.

- $GLOBALS exists in any scope, this is because $GLOBALS is a superglobal.

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

### **Global Keyword**:
- To use a global variable inside a function, use the `global` keyword.

```php
<?php
$x = 10;  // Global variable

function testFunction() {
    global $x;
    echo $x;  // Output: 10
}

testFunction();
?>
```

## References

[1] "Variable Scope," *PHP Manual*. [Online]. Available: <https://www.php.net/manual/en/language.variables.scope.php>. [Accessed: Apr. 29, 2025].
