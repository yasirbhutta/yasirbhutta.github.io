---
layout: page
title: "Difference Between Expressions and Statements in Java | Java Basics Explained"
description: "Learn the key differences between expressions and statements in Java. Understand how expressions produce values, statements perform actions, with examples and beginner-friendly explanations."
keywords: ""
---

## **1️⃣ Expression**

* **Definition:**
  An **expression** is a combination of **variables, operators, and values** that **produces a single value**.

* **Key point:** Expressions **always return a value**.

* **Examples:**

```java
int a = 5;
int b = 3;

// Arithmetic expression
int sum = a + b;  // 'a + b' is an expression that produces 8

// Relational expression
boolean result = a > b;  // 'a > b' is an expression that produces true

// Logical expression
boolean check = (a > 2) && (b < 5);  // produces true
```

* **Inside an expression, you can have:**

  * Arithmetic operators: `+ - * / %`
  * Relational operators: `> < == != >= <=`
  * Logical operators: `&& || !`
  * Unary operators: `++ -- !`

---

## **2️⃣ Statement**

* **Definition:**
  A **statement** is a **complete line of code that performs an action**.

* **Key point:** Statements **do not necessarily produce a value**, but they **execute an action**.

* **Examples:**

```java
int a = 5;             // declaration statement
int b = 3;             // declaration statement
int sum = a + b;       // expression inside a statement
System.out.println(sum);  // statement (prints value, action performed)
a++;                   // statement (increments a by 1)
```

* **Types of statements in Java:**

  * **Expression statements:** e.g., `a = 5;`
  * **Control statements:** e.g., `if`, `for`, `while`
  * **Declaration statements:** e.g., `int x = 10;`

---

## **3️⃣ Main Difference Table**

| Feature           | Expression                            | Statement                                      |
| ----------------- | ------------------------------------- | ---------------------------------------------- |
| **Definition**    | Produces a value                      | Performs an action                             |
| **Returns value** | Yes                                   | No (usually)                                   |
| **Example**       | `a + b`, `x > y`, `!flag`             | `int a = 5;`, `System.out.println(a);`, `a++;` |
| **Used in**       | Assignments, calculations, conditions | Executing code, controlling flow               |

---

### 🔑 **Quick Tip**

* Every **expression can be part of a statement**, but **not every statement is an expression**.

Example:

```java
int a = 5 + 3; // '5 + 3' is expression, 'int a = 5 + 3;' is statement
```
---

## 📘 **Related Topics**

- [Java Expressions: Types, Examples & Practice Questions | Complete Guide](index.md)

