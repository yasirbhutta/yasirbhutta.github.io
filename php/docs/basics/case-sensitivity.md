---
layout: page
title: "Case Sensitivity in PHP: Keywords, Functions, and Variables Explained"
description: Learn about case sensitivity in PHP. Understand how PHP treats keywords and functions as case-insensitive, while variables are case-sensitive, with clear examples.
keywords: PHP case sensitivity, PHP variables case sensitive, PHP keywords case insensitive, PHP functions case sensitivity, PHP echo case, PHP variable naming, PHP syntax rules
toc: toc/php.html
course: php
topic: "basics"
mini_project: true
prev: /php/docs/basics/installation.html
next: /php/docs/basics/variables-in-php.html
---

## **Case Sensitivity**

### **Keywords and Functions**
- PHP keywords and functions (e.g., `if`, `else`, `echo`) are **not case-sensitive**.
  
### **Variables**
- **Variables are case-sensitive**, meaning `$Var` and `$var` are two different variables.

### Example: Case Insensitivity in PHP

```php
<?php
ECHO "Hello World!<br>";
echo "Hello World!<br>";
EcHo "Hello World!<br>";
?>
```

### Example: Case Sensitivity in Variables

```php
<?php
$color = "red";  // lowercase
$COLOR = "green";  // uppercase
echo "My car is " . $color . "<br>";  // outputs red
echo "My house is " . $COLOR . "<br>";  // outputs green
?>
```
## Tasks

### **Task 1: Experiment with `echo`**
   - Write a PHP script where you use `echo`, `ECHO`, and `EcHo` to print the same message (e.g., "Hello, PHP!").  
   - Observe the output. Does it work the same way for all variations? 

### **Task 2: Test Variable Names**
   - Declare two variables:  
     ```php
     $name = "Alice";
     $NAME = "Bob";
     ```
   - Print both variables. Are they treated as the same or different?  
