---
layout: page
title: "Java Expressions: Types, Examples & Practice Questions | Complete Guide"
description: "Master Java expressions with comprehensive guide covering arithmetic, relational, logical, assignment, conditional, and ternary expressions with real examples and practice questions."
keywords: "Java expressions, arithmetic expressions, relational expressions, logical expressions, assignment expressions, conditional expressions, ternary operator, Java operators, expression examples"
---

## 1️⃣ Arithmetic Expressions

Used for calculations.

```java
int a = 10;
int b = 3;

int sum = a + b;        // 13
int diff = a - b;       // 7
int product = a * b;    // 30
int quotient = a / b;   // 3 (integer division)
int remainder = a % b;  // 1
```

👉 `a + b`, `a * b`, `a % b` are **expressions**.

---

## 2️⃣ Relational (Comparison) Expressions

Used to compare values. Result is **true** or **false**.

```java
int x = 5;
int y = 8;

boolean result1 = x < y;   // true
boolean result2 = x == y;  // false
boolean result3 = x != y;  // true
```

---

## 3️⃣ Logical Expressions

Used to combine conditions.

```java
int age = 20;
boolean hasID = true;

boolean canEnter = (age >= 18) && hasID;  // true
```

Operators:

* `&&` → AND
* `||` → OR
* `!` → NOT

---

## 4️⃣ Assignment Expressions

Assign values to variables.

```java
int num = 10;
num += 5;   // same as num = num + 5 (15)
num *= 2;   // same as num = num * 2 (30)
```

---

## 5️⃣ Unary Expressions

Operate on a single value.

```java
int count = 5;

count++;  // 6 (increment)
count--;  // 5 (decrement)

boolean isOpen = false;
boolean status = !isOpen; // true
```

---

## 6️⃣ Conditional (Ternary) Expression

A shortcut for `if-else`.

```java
int marks = 75;

String result = (marks >= 50) ? "Pass" : "Fail";
```

---

## 7️⃣ String Expressions

Used with text.

```java
String firstName = "Yasir";
String lastName = "Bhutta";

String fullName = firstName + " " + lastName;
// Yasir Bhutta
```

---

## 8️⃣ Mixed Expressions

Combining different types.

```java
int a = 5;
int b = 2;

double result = a / (double) b;  // 2.5
```

---

## 9️⃣ Expression inside `System.out.println()`

Very common for beginners.

```java
System.out.println(10 + 5);          // 15
System.out.println("Sum = " + (10 + 5)); // Sum = 15
```

---

## 📝 Practice Questions (Java Expressions)

**Q1.** What will be the output?

```java
System.out.println(8 + 2 * 5);
```

---

**Q2.** What is the value of `result`?

```java
int a = 6;
int b = 4;
boolean result = a >= b;
```

---

**Q3.** What will be printed?

```java
int x = 10;
System.out.println(x++ + 5);
```

---

**Q4.** Identify the expression in the statement:

```java
double avg = (a + b + c) / 3.0;
```

---

**Q5.** What is the output?

```java
System.out.println(15 % 4);
```

---

**Q6.** What will be printed?

```java
int num = 5;
System.out.println(num > 3 && num < 10);
```

---

**Q7.** What is the value of `status`?

```java
int marks = 45;
String status = (marks >= 50) ? "Pass" : "Fail";
```

---

**Q8.** Which operator is used to reverse a boolean value?

```java
boolean flag = false;
```

---

**Q9.** What will be the output?

```java
System.out.println("Result: " + 10 + 20);
```

---

**Q10.** What is the result of this expression?

```java
int result = 20 / 4 + 3 * 2;
```

---

## 🧪 Tasks

### 🔹 Lab 1: Basic Calculator

Write a Java program that:

* Declares two integer variables
* Performs **+ − × ÷ %**
* Prints all results

---

### 🔹 Lab 2: Increment & Decrement

* Declare an integer variable
* Apply `++` and `--`
* Print values **before and after** operations

---

### 🔹 Lab 3: Even or Odd

* Take an integer
* Use an expression to check even or odd
* Print the result

---

### 🔹 Lab 4: Maximum of Two Numbers

* Declare two numbers
* Use a **ternary expression**
* Print the larger number

---

### 🔹 Lab 5: Pass or Fail System

* Declare `marks`
* Print `"Pass"` if marks ≥ 50, else `"Fail"`

---

### 🔹 Lab 6: Logical Operator Practice

* Declare `age` and `hasID`
* Allow entry if:

  * age ≥ 18 AND hasID is true

---

### 🔹 Lab 7: Simple Interest

* Declare `principal`, `rate`, `time`
* Use an expression to calculate simple interest

Formula:

```
SI = (P × R × T) / 100
```

---

### 🔹 Lab 8: Positive, Negative, or Zero

* Declare a number
* Use **if-else with expressions**
* Print the result

---

### 🔹 Lab 9: String Expression

* Declare first and last name
* Combine them using `+`
* Print full name

---

### 🔹 Lab 10: Operator Precedence Test

* Write a program using:

```java
int result = 10 + 2 * 3 - 4 / 2;
```

* Print and explain the output

---

## 📘 **Related Topics**

- [Difference Between Expressions and Statements in Java | Java Basics Explained](expressions-statements.md)
- [Data Types and Variables](data-types-variables-java.md)
- [Type Casting](type-casting.md)
