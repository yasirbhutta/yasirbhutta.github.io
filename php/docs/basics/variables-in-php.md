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

## Tasks

---

### **Task 1: Basic Variable Declaration and Output**
1. Create a PHP script that declares a variable named `$greeting` and assigns it the value `"Hello, PHP!"`.
2. Use `echo` to display the value of `$greeting`.
3. Run the script and verify the output.

**Expected Output:**
```
Hello, PHP!
```

---

### **Task 2: Changing Variable Values**
1. Declare a variable `$number` and assign it the value `10`.
2. Display the value of `$number` using `echo`.
3. Reassign `$number` to `20` and display it again.
4. Finally, reassign `$number` to `"twenty"` (a string) and display it.

**Expected Output:**
```
10
20
twenty
```
---

### **Task 3: Arithmetic with Variables**
1. Declare two variables, `$a` and `$b`, and assign them the values `7` and `3`, respectively.
2. Calculate and display the sum, difference, product, and quotient of `$a` and `$b`.
   - Use `echo` to output each result with a label (e.g., "Sum: 10").

**Expected Output:**
```
Sum: 10
Difference: 4
Product: 21
Quotient: 2.333...
```

---

### **Task 4: Dynamic Typing**
1. Declare a variable `$dynamic` and assign it an integer value (e.g., `100`).
2. Display the value and its type using `echo` and `gettype()` (e.g., `echo gettype($dynamic);`).
3. Reassign `$dynamic` to a string (e.g., `"Dynamic PHP"`) and display its type again.
4. Reassign `$dynamic` to a float (e.g., `3.14`) and display its type once more.

**Expected Output:**
```
100
integer
Dynamic PHP
string
3.14
double
```

---

### **Task 5: Combining Variables**
1. Declare two variables: `$firstName` (assign your name) and `$lastName` (assign your surname).
2. Combine them into a third variable `$fullName` and display it.
   - Hint: Use concatenation (`.` in PHP), e.g., `$fullName = $firstName . " " . $lastName;`.

**Expected Output:**
```
John Doe
```

## References

[1] "PHP Variables," *Tutorial Republic*. [Online]. Available: <https://www.tutorialrepublic.com/php-tutorial/php-variables.php>. [Accessed: Apr. 29, 2025].

