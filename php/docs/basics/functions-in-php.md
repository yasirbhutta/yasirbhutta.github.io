---
layout: page
title: "PHP Basics Tutorial – Functions in PHP"
description: Learn about functions in PHP, including how to define them, pass arguments, return values, and use default parameters. This guide includes clear examples for beginners.
keywords: PHP functions, defining functions in PHP, PHP function arguments, return values in PHP, PHP default parameters, PHP function examples, PHP basics, reusable code in PHP
toc: toc/php.html
course: php
topic: "basics"
mini_project: true
---

## **What is a Function?**
- A function is a block of reusable code that performs a specific task.

## **Defining a Function**

```php
<?php
function sayHello() {
    echo "Hello, PHP!";
}

sayHello();  // Output: Hello, PHP!
?>
```

## **Functions with Arguments**
- Functions can accept parameters to make them more flexible.

```php
<?php
function greet($name) {
    echo "Hello, $name!";
}

greet("Alice");  // Output: Hello, Alice!
?>
```

## **Returning Values**
- Functions can return values using the `return` statement.

```php
<?php
function add($a, $b) {
    return $a + $b;
}

echo add(5, 3);  // Output: 8
?>
```

## **Default Argument Values**
- You can provide default values for function arguments.

```php
<?php
function setHeight($height = 150) {
    echo "The height is: $height cm";
}

setHeight();  // Output: The height is: 150 cm
setHeight(180);  // Output: The height is: 180 cm
?>
```
