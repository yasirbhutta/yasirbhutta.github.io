---
layout: page
title: "PHP Basics Tutorial – Variables in PHP"
description: Learn what variables are in PHP and how to use them. This beginner-friendly guide explains variable declaration, assignment, types, and case sensitivity with examples.
keywords: PHP variables, PHP variable types, declaring variables in PHP, assigning values in PHP, PHP dynamic typing, PHP case sensitivity, PHP basics for beginners, PHP data types
toc: toc/php.html
course: php
topic: "basics"
mini_project: true
prev: /php/docs/basics/case-sensitivity.html
next: /php/docs/basics/variable-scope.html
---

## **What are Variables?**
- Variables are used to store values such as strings, numbers, and arrays. 
- In PHP, variables are prefixed with a dollar sign (`$`).

**Understanding PHP Variables:**

- A variable's value can change while the program is running.  
- In PHP, you don’t have to declare a variable before giving it a value.  
- PHP automatically figures out the right data type based on the value you give.  
- Once you create a variable, you can use it again and again in your code.  
- The equals sign (`=`) is used to give a value to a variable.  
- Variable names are case-sensitive, so `$name` and `$Name` are different.


## **Declaring and Assigning Variables**
- Variables do not need to be declared before use in PHP. They are dynamically typed.

### Example #1: Declaring Variables

```php
<?php
$txt = "PHP is fun!";
echo $txt;  // Output: PHP is fun!
?>
```

## **Variable Types**
- PHP automatically converts a variable’s type based on the value assigned to it.

### Example #2
  
```php
<?php
$var = 10;  // Integer
$var = "Hello!";  // String
$var = 3.14;  // Float
?>
```

### Example #3: variable example

```php
<?php

$x = 5;
$y = 4;
echo $x + $y;

?>
```

## References

[1] "PHP Variables," *Tutorial Republic*. [Online]. Available: <https://www.tutorialrepublic.com/php-tutorial/php-variables.php>. [Accessed: Apr. 29, 2025].

