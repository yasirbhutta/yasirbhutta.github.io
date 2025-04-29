---
layout: page
title: "PHP Basics Tutorial – Constants in PHP"
description: Learn what constants are in PHP and how to define them using the define() function. This guide covers constant usage, syntax, and case sensitivity with examples.
keywords: PHP constants, define() in PHP, constant vs variable in PHP, PHP constant example, PHP define case sensitivity, PHP GREETING example, PHP define function, immutable values in PHP
toc: toc/php.html
course: php
topic: "basics"
mini_project: true
---

## **What is a Constant?**
- A constant is a value that cannot be changed once set, unlike variables.
- Constants are defined using `define()`.

## Example #1:

```php
<?php
define("SITE_NAME", "My Awesome Site");
echo SITE_NAME;  // Output: My Awesome Site
?>
```

## Example #2: Defines a named constant

```php
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>PHP - Contants</title>
    </head>
    <body>
        <?php
        // define(name, value, case-insensitive)
        // case-insensitive: Specifies whether the constant name should be case-insensitive. Default is false
        define("GREETING", "Welcome to Department of CS & IT!");

        function myTest() {
            echo GREETING;
        }
        myTest();
        ?> 
    </body>
</html>
```

## References

[1] "define," *PHP Manual*. [Online]. Available: <https://www.php.net/manual/en/function.define.php>. [Accessed: Apr. 29, 2025].

