---
layout: page
title: "PHP Basics Tutorial – Variable Scope in PHP"
description: Understand variable scope in PHP, including local and global variables. Learn how to use the global keyword and access global variables inside functions with clear code examples.
keywords: PHP variable scope, local scope in PHP, global scope in PHP, PHP global keyword, PHP function variables, PHP $GLOBALS, variable accessibility in PHP, PHP scope example
toc: toc/php.html
course: php
topic: "basics"
mini_project: true
prev: /php/docs/basics/variables-in-php.html
next: /php/docs/basics/functions-in-php.html
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

## Tasks

### **Task 1: Understanding Local Scope**
1. **Create a function** called `printLocalVar()` that defines a local variable `$message` with the value `"Hello, PHP!"`.  
2. **Print** `$message` inside the function.  
3. **Call the function** and observe the output.  
4. Now, try to **print `$message` outside the function**. What happens? Explain why.  

#### Example Structure:
```php
<?php
function printLocalVar() {
    // Your code here
}
// Call function and test
?>
```

---

### **Task 2: Working with Global Scope**
1. **Define a global variable** `$counter = 0;` outside any function.  
2. **Create a function** `incrementCounter()` that accesses `$counter` using the `$GLOBALS` array and increments it by `1`.  
3. **Call the function twice** and then **print `$counter`** outside the function. What is the output?  

#### Expected Output:
```
2
```

---

### **Task 3: Modifying Global Variables Inside a Function**
1. **Define a global variable** `$total = 50;`.  
2. **Create a function** `applyDiscount()` that:  
   - Uses the `global` keyword to access `$total`.  
   - Applies a 10% discount (reduce `$total` by 10%).  
3. **Call the function** and then **print `$total`** outside the function.  

#### Expected Output:
```
45
```

---

## References

[1] "Variable Scope," *PHP Manual*. [Online]. Available: <https://www.php.net/manual/en/language.variables.scope.php>. [Accessed: Apr. 29, 2025].
