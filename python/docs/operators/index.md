---
layout: page
title: Python Operators Explained with Examples | Arithmetic, Logical, Comparison & More
description: Master Python operators with clear examples. Learn how arithmetic, assignment, logical, comparison, identity, membership, and bitwise operators work in Python.  
keywords: python operators, python arithmetic operators, logical operators in python, comparison operators, python operator examples, python bitwise operators, assignment operators, identity operators, membership operators, python programming basics, python tutorials
toc: toc/python.html
author: Muhammad Yasir Bhutta
course: python
topic: operators
show_toc: true
toc: toc/python.html
show_practice_progress: true
show_mini_project: false
prev: /python/docs/basics/
next: /python/docs/operators/practice-and-progress/find-fix-mistakes-variables.html
breadcrumb:
  - title: Home
    url: /
  - title: Python
    url: /python/
  - title: Basics
    url: /python/docs/basics/
  - title: Operators
    url: /python/docs/operators/
---

## Table of Contents

1. [What is Operators](#what-is-operators)
2. [Major operator categories](#major-operator-categories)
   - [2.1 Arithmetic Operators](#1-arithmetic-operators)
   - [2.2 Comparison Operators](#2-comparison-operators)
   - [2.3 Assignment Operators](#3-assignment-operators)
     - [Compound assignment](#compound-assignment)
   - [2.4 Logical Operators](#4-logical-operators)
   - [2.5 Identity Operators](#5-identity-operators)
   - [2.6 Membership Operators](#6-membership-operators)
   - [2.7 Bitwise Operators](#7-bitwise-operators)
3.  [Object Caching in Python](#object-caching-in-python-understanding-memory-optimization-for-small-integers)
   
## What is Operators

- Operators in Python are special symbols that perform specific operations on values and variables.
- They are essential for calculations, comparisons, assignments, and logical operations within your code.

## Major operator categories

### 1. Arithmetic Operators:

- Used for performing basic mathematical calculations.
- Operators: `+` (addition), `-` (subtraction), `*` (multiplication), `/` (division), `//` (floor division), `%` (modulo), `**` (exponentiation)

[video: Basic Mathematical Operations with Examples](https://youtu.be/fDul88llyHM)

- Examples:

```python
result = 10 + 5  # Addition
difference = 15 - 7  # Subtraction
product = 4 * 6  # Multiplication
quotient = 12 / 3  # Division
integer_quotient = 17 // 4  # Floor division
remainder = 25 % 4  # Modulo
square = 5 ** 2  # Exponentiation
```

For more details on floor division, see [What is the `//` Operator in Python?](../posts/floor-division.md)

### 2. Comparison Operators:

- Used to compare values and return a Boolean result (True or False).
- Operators: `==` (equal to), `!=` (not equal to), `>` (greater than), `<` (less than), `>=` (greater than or equal to), `<=` (less than or equal to)

[video: How to Use Comparision Operators in Python](https://youtu.be/esjtrurnl78)

**Examples:**

```python
is_equal = 7 == 7  # True
is_greater = 12 > 9  # True
is_less_or_equal = 5 <= 5  # True
```

### 3. Assignment Operators:

- Used to assign values to variables.
- Operators: `=` 
- Examples:

```python
x = 10  # Simple assignment
```
#### Compound assignment: 

A **compound assignment** is a combination of an operator and an assignment that performs an operation on a variable and then assigns the result back to that variable in a single step.

For example, in the code:

```python
message += " Welcome!"
```

This is a **compound assignment** using the `+=` operator. Here’s what it does:
1. It concatenates (adds) `" Welcome!"` to the existing value of the `message` variable.
2. Then, it assigns the result back to `message`.

In general, the format of compound assignment operators is:

- `+=` : Adds and assigns
- `-=` : Subtracts and assigns
- `*=` : Multiplies and assigns
- `/=` : Divides and assigns
- `%=` : Takes the modulus and assigns

This shorthand avoids writing out the operation in a longer form, such as:

```python
message = message + " Welcome!"
```

The `+=` operator helps to keep the code more concise and readable.

**Example:**

```python
x += 5  # Add 5 to x
x *= 2  # Multiply x by 2
```
### 4. Logical Operators:

- Used to combine Boolean expressions.
- Operators: `and`, `or`, `not`

- Examples:

```python
is_valid = (age >= 18) and (has_license == True)
is_allowed = (is_member) or (has_ticket)
```

### 5. Identity Operators:

- In Python, the `is` operator is used to compare the identities of two objects. It checks whether two references point to the same object in memory, not whether the values of the two objects are equal. 
- Operators: `is`, `is not`

Here's a simple example to illustrate the difference between `is` and `==`:

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # Output: True, because the lists have the same content
print(a is b)  # Output: False, because they are different objects in memory
print(a is c)  # Output: True, because both references point to the same object
```

In this example:
- `a == b` is `True` because the values in both lists are the same.
- `a is b` is `False` because they are two different objects in memory, even though their contents are identical.
- `a is c` is `True` because `c` is assigned to the same object as `a`, so they reference the same memory location.
  
**Example 2**

```python
x = 5
y = 5
result = x is y  # True (they refer to the same integer object)
```
## Object Caching in Python: Understanding Memory Optimization for Small Integers

- In Python, small integer objects (typically between -5 and 256) are cached to optimize memory usage and performance. This means that if you create multiple variables with the same value within this range, they all point to the same memory location, instead of creating new objects each time. 
- This behavior is part of Python's optimization to save memory and improve performance, as small integers are frequently used. [1]

Here's an example to explain the concept:

```python
# Assigning variables within the cached range
a = 100
b = 100

# Checking if the IDs are the same
print(id(a))  # Outputs the memory address of 'a'
print(id(b))  # Outputs the memory address of 'b'

# Since both 'a' and 'b' are within the cached range, their IDs are the same
print(a is b)  # True, as both refer to the same cached object

# Assigning variables outside the cached range
x = 300
y = 300

# Checking if the IDs are the same
print(id(x))  # Outputs the memory address of 'x'
print(id(y))  # Outputs the memory address of 'y'

# Since 'x' and 'y' are outside the cached range, they are different objects
print(x is y)  # False, as 'x' and 'y' refer to different objects
```

**Explanation:**

1. **Cached Objects**: The values `a` and `b` are both set to `100`, which falls within the default cached range of small integers. As a result, Python uses the same memory location for both, which is why `id(a)` and `id(b)` are the same, and `a is b` returns `True`.

2. **Non-Cached Objects**: The values `x` and `y` are both set to `300`, which is outside the cached range. Therefore, Python creates separate objects for each, and `id(x)` and `id(y)` are different, meaning `x is y` returns `False`.

This caching behavior saves memory for frequently used small integers and makes the comparison of such objects faster.

### 6. Membership Operators:

- Used to check if a value is present in a sequence (like a list or string).
- Operators: `in`, `not in`

- Examples:

```python
numbers = [1, 3, 5, 7]
is_present = 5 in numbers  # True
is_missing = 2 not in numbers  # True
```

### 7. Bitwise Operators:

- Used to perform operations on the binary representation of numbers.
- Operators: `&` (bitwise AND), `|` (bitwise OR), `^` (bitwise XOR), `~` (bitwise NOT), `<<` (left shift), `>>` (right shift)
- These are less common in general-purpose programming, but useful in certain domains like low-level programming or cryptography.

## `id()` function

In Python, the `id()` function returns the "identity" of an object, which is a unique integer that serves as a constant for the object during its lifetime. The `id` is often the memory address of the object. Here's a simple example:

```python
x = 10
print(id(x))

y = "hello"
print(id(y))
```

This code will print the unique identifiers for the variables `x` and `y`. If you have specific objects or variables in mind that you would like to see the `id` for, please let me know!

**Python operators examples:**

- [Walrus Operator in Python](https://youtube.com/shorts/vhEz75XZlJI)


## Coding Exercises

### Beginner Exercises

### Exercise #1: Rectangle Area and Perimeter Calculation

**Task:** Write a program to calculate the area and perimeter of a rectangle.

**Input:**
- A floating-point number `length`, representing the length of the rectangle.
- A floating-point number `width`, representing the width of the rectangle.

**Output:**
- Print the area of the rectangle.
- Print the perimeter of the rectangle.

**Example:**

- **Input:**  
  `length = 5.0`  
  `width = 3.0`  
- **Output:**  
  `Area: 15.0`  
  `Perimeter: 16.0`  

- **Input:**  
  `length = 7.5`  
  `width = 2.5`  
- **Output:**  
  `Area: 18.75`  
  `Perimeter: 20.0`  

#### Exercise 2: Converts temperature from Celsius to Fahrenheit
**Task:** Create a program that converts temperature from Celsius to Fahrenheit using the formula: `(Celsius * 9/5) + 32`.

#### Exercise 3: Calculating Sum, Difference, Product, and Quotient
**Task:** Write a program that takes two numbers and prints their sum, difference, product, and quotient.

#### Exercise 4: Basic Assignment
**Task**: Assign the value `10` to the variable `a` and print the value of `a`.

#### Exercise 5: Compound Assignment with Addition (`+=`) 
**Task**: 
1. Assign the value `15` to a variable `x`.
2. Use the `+=` operator to add `5` to `x`.
3. Print the new value of `x`.

#### Exercise 6: Compound Assignment with Subtraction (`-=`) [Easy]
**Task**: 
1. Assign the value `20` to a variable `y`.
2. Use the `-=` operator to subtract `7` from `y`.
3. Print the new value of `y`.

#### Exercise 7: Modulus Assignment (`%=`)
**Task**: 
1. Assign `13` to a variable `m`.
2. Use the `%=` operator to assign the remainder when `m` is divided by `5`.
3. Print the result.

#### Exercise 8: Swap Variables Using Assignment Operators [Easy]
**Task**: Swap the values of two variables `a = 10` and `b = 20` without using a third variable or tuple assignment.

#### Exercise 9: Complex Assignment Expression
**Task**: 
1. Create three variables: `a = 4`, `b = 5`, and `c = 6`.
2. Use a single line with assignment operators to update the values of all three variables, such that:
   - `a` is multiplied by `2`.
   - `b` is increased by `10`.
   - `c` is divided by `3`.
3. Print the values of all three variables.

#### Exercise 10:
**Task:** Write a program that checks if two variables point to the same object using the `is` operator.

#### Exercise 11:
**Task:** Create a list of fruits and write a program that checks if "apple" is in the list using the `in` operator.
      
### Intermediate Exercises

**Bitwise Operators**

1. Write a program that takes two numbers as input and prints their bitwise AND, OR, and XOR.
2. Use the left shift operator (`<<`) to multiply a number by 4 and the right shift operator (`>>`) to divide a number by 2.
   
### Advanced Exercises

### Practical Mini-Project
1. **Shopping Cart**: Create a shopping cart program. Initialize a total cost as 0. Add the cost of items using `+=` as items are added. Print the total cost when all items have been added.
2. **Odd or Even Checker**: Write a program that takes a number and uses the modulo operator (`%`) to check if it is even or odd.

## Review Questions

## References and Bibliography

[1] “Python memory management,” Discussions on Python.org, Apr. 02, 2023. https://discuss.python.org/t/python-memory-management/25391 (accessed Jul. 27, 2024).
‌