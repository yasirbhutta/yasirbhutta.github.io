---
layout: page
title: "C++ Operators"
description: "Learn C++ operators with easy explanations, examples, and practice. Understand arithmetic, assignment, relational, logical, unary, binary, increment, and decrement operators in C++ programming."
keywords: C++ operators, arithmetic operators in C++, assignment operator, relational operators, logical operators, unary operators, binary operators, increment operator, decrement operator, C++ tutorial, C++ programming examples, beginner C++, operator precedence, operators in C++
---

## 1. What is an Operator?

An **operator** is a symbol used to perform an operation on one or more values or variables.

### Example

```cpp
int a = 10;
int b = 5;

int result = a + b;
```

Here:

* `a` and `b` are **operands**.
* `+` is an **operator**.
* `a + b` is an **expression**.
* The result is `15`.

---

# 2. What is an Expression?

An **expression** is a combination of values, variables, and operators that produces a result.

### Examples

```cpp
a + b
```

```cpp
marks >= 50
```

```cpp
age >= 18 && age <= 60
```

Each of these expressions produces a result.

---

# 3. Types of Operators Based on Number of Operands

Operators can be classified according to the number of operands they work with.

## 3.1 Unary Operators

A **unary operator** works with **one operand**.

### Examples

```cpp
x++;
```

```cpp
-x;
```

```cpp
!isStudent;
```

Only one variable/value is involved.

### Common Unary Operators

| Operator | Meaning     | Example |
| -------- | ----------- | ------- |
| `++`     | Increment   | `x++`   |
| `--`     | Decrement   | `x--`   |
| `-`      | Negative    | `-x`    |
| `!`      | Logical NOT | `!x`    |

---

## 3.2 Binary Operators

A **binary operator** works with **two operands**.

### Example

```cpp
a + b
```

Here:

* `a` → first operand
* `+` → operator
* `b` → second operand

Other examples:

```cpp
a - b
a * b
a > b
a == b
```

### Remember

**Unary → one operand**

```cpp
x++;
```

**Binary → two operands**

```cpp
x + y;
```

---

# 4. Types of C++ Operators

The main operators we will study are:

1. Arithmetic Operators
2. Assignment Operator
3. Compound Assignment Operators
4. Increment and Decrement Operators
5. Relational Operators
6. Logical Operators

---

# 5. Arithmetic Operators

Arithmetic operators are used to perform **mathematical calculations**.

| Operator | Name              | Example |
| -------- | ----------------- | ------- |
| `+`      | Addition          | `a + b` |
| `-`      | Subtraction       | `a - b` |
| `*`      | Multiplication    | `a * b` |
| `/`      | Division          | `a / b` |
| `%`      | Modulus/Remainder | `a % b` |

### Example

```cpp
int a = 10;
int b = 3;

cout << a + b;   // 13
cout << a - b;   // 7
cout << a * b;   // 30
cout << a / b;   // 3
cout << a % b;   // 1
```

### Important Point: `/` Division Operator

The `/` operator is used for division.

**The result depends on the data type of the operands.**

### 1. Both Operands are `int`

If both operands are integers, C++ performs **integer division**.

```cpp
int a = 10;
int b = 3;

cout << a / b;
```

**Output:**

```text
3
```

Although mathematically:

```text
10 ÷ 3 = 3.3333...
```

C++ gives:

```text
3
```

because both `a` and `b` are `int`.

> **Important:** The decimal part is removed when integer division is performed.

---

### 2. One Operand is `float`

If at least one operand is a `float`, the division produces a decimal result.

```cpp
float a = 10;
int b = 3;

cout << a / b;
```

**Output:**

```text
3.33333
```

Here:

```text
float / int → decimal result
```

---

### 3. Both Operands are `float`

```cpp
float a = 10;
float b = 3;

cout << a / b;
```

**Output:**

```text
3.33333
```

Here:

```text
float / float → decimal result
```

---

### 4. Using `double`

`double` can also be used for decimal calculations.

```cpp
double a = 10;
double b = 3;

cout << a / b;
```

**Output:**

```text
3.33333
```

### Remember

| Operand Types     | Example        |    Result |
| ----------------- | -------------- | --------: |
| `int / int`       | `10 / 3`       |       `3` |
| `float / int`     | `10.0f / 3`    | `3.33333` |
| `int / float`     | `10 / 3.0f`    | `3.33333` |
| `float / float`   | `10.0f / 3.0f` | `3.33333` |
| `double / double` | `10.0 / 3.0`   | `3.33333` |

### Important Rule

> **If both operands are `int`, the result of `/` is integer division. If at least one operand is a floating-point type (`float` or `double`), the result can contain decimal values.**

---

### Important Point: `%` Remainder Operator

The `%` operator gives the **remainder after integer division**.

```cpp
int a = 10;
int b = 3;

cout << a % b;
```

**Output:**

```text
1
```

Because:

```text
10 ÷ 3 = 3 remainder 1
```

Therefore:

```text
10 / 3 = 3
10 % 3 = 1
```

### Another Example

```cpp
int a = 20;
int b = 6;

cout << a / b << endl;
cout << a % b << endl;
```

**Output:**

```text
3
2
```

Because:

```text
20 ÷ 6 = 3 remainder 2
```

### Remember

```text
/  → gives the quotient
%  → gives the remainder
```

For example:

```text
17 / 5 = 3
17 % 5 = 2
```

# 6. Assignment Operator

The assignment operator is:

```cpp
=
```

It is used to **assign a value to a variable**.

### Example

```cpp
int age = 20;
```

This means:

> Store the value `20` in the variable `age`.

Another example:

```cpp
int x = 10;

x = 25;
```

Now:

```text
x = 25
```

### Important

Do not confuse:

```cpp
=
```

with:

```cpp
==
```

`=` means **assignment**.

`==` means **comparison**.

Example:

```cpp
x = 10;    // Assign 10 to x
x == 10;   // Check whether x is 10
```

---

# 7. Compound Assignment Operators

Compound assignment operators provide a shorter way to update a variable.

### Example

Instead of:

```cpp
x = x + 5;
```

we can write:

```cpp
x += 5;
```

Both have the same effect.

### Common Compound Assignment Operators

| Operator | Example  | Equivalent To |
| -------- | -------- | ------------- |
| `+=`     | `x += 5` | `x = x + 5`   |
| `-=`     | `x -= 5` | `x = x - 5`   |
| `*=`     | `x *= 5` | `x = x * 5`   |
| `/=`     | `x /= 5` | `x = x / 5`   |
| `%=`     | `x %= 5` | `x = x % 5`   |

### Example

```cpp
int marks = 70;

marks += 5;
```

Now:

```text
marks = 75
```

---

# 8. Increment Operator `++`

The increment operator increases a value by **1**.

```cpp
int x = 5;

x++;
```

Now:

```text
x = 6
```

It is equivalent to:

```cpp
x = x + 1;
```

There are two forms:

```cpp
x++;
```

**Post-increment**

and:

```cpp
++x;
```

**Pre-increment**

Both increase the value by 1. The difference becomes important when the operator is used inside a larger expression.

---

# 9. Decrement Operator `--`

The decrement operator decreases a value by **1**.

```cpp
int x = 5;

x--;
```

Now:

```text
x = 4
```

It is equivalent to:

```cpp
x = x - 1;
```

There are two forms:

```cpp
x--;
```

**Post-decrement**

and:

```cpp
--x;
```

**Pre-decrement**

---

# 10. Relational Operators

Relational operators are used to **compare two values**.

The result of a comparison is either:

```text
true
```

or:

```text
false
```

### Relational Operators

| Operator | Meaning                  | Example  |
| -------- | ------------------------ | -------- |
| `>`      | Greater than             | `a > b`  |
| `<`      | Less than                | `a < b`  |
| `>=`     | Greater than or equal to | `a >= b` |
| `<=`     | Less than or equal to    | `a <= b` |
| `==`     | Equal to                 | `a == b` |
| `!=`     | Not equal to             | `a != b` |

### Example

```cpp
int marks = 75;

cout << (marks >= 50);
```

The expression is:

```cpp
marks >= 50
```

Since 75 is greater than 50, the result is:

```text
true
```

---

# 11. Logical Operators

Logical operators are used to **combine or reverse conditions**.

There are three main logical operators:

| Operator | Name | Meaning                      |    |                                     |
| -------- | ---- | ---------------------------- | -- | ----------------------------------- |
| `&&`     | AND  | Both conditions must be true |    |                                     |
| `        |      | `                            | OR | At least one condition must be true |
| `!`      | NOT  | Reverses the condition       |    |                                     |

---

## 11.1 AND Operator `&&`

The `&&` operator returns true when **both conditions are true**.

### Example

```cpp
age >= 18 && marks >= 50
```

This means:

> Age must be 18 or above **AND** marks must be 50 or above.

---

## 11.2 OR Operator `||`

The `||` operator returns true when **at least one condition is true**.

### Example

```cpp
day == 6 || day == 7
```

This means:

> Day is 6 **OR** day is 7.

---

## 11.3 NOT Operator `!`

The `!` operator reverses a Boolean value or condition.

### Example

```cpp
bool isStudent = true;

cout << !isStudent;
```

The result becomes:

```text
false
```

Because `!` changes `true` to `false` and `false` to `true`.

---

# 12. Operators in `if` Statements

Operators are commonly used to create conditions in `if` statements.

### Example 1

```cpp
int marks = 75;

if (marks >= 50)
{
    cout << "Pass";
}
```

Here:

```cpp
marks >= 50
```

is a **condition/expression** using a relational operator.

### Example 2

```cpp
int age = 20;
int marks = 75;

if (age >= 18 && marks >= 50)
{
    cout << "Eligible";
}
```

Here:

* `>=` → Relational operator
* `&&` → Logical operator
* `age >= 18` → First condition
* `marks >= 50` → Second condition

---

# 13. Operator Summary

| Category            | Operators             | Purpose                   |    |                               |
| ------------------- | --------------------- | ------------------------- | -- | ----------------------------- |
| Arithmetic          | `+ - * / %`           | Mathematical calculations |    |                               |
| Assignment          | `=`                   | Assign a value            |    |                               |
| Compound Assignment | `+= -= *= /= %=`      | Update a variable         |    |                               |
| Increment           | `++`                  | Increase by 1             |    |                               |
| Decrement           | `--`                  | Decrease by 1             |    |                               |
| Relational          | `> < >= <= == !=`     | Compare values            |    |                               |
| Logical             | `&&                   |                           | !` | Combine or reverse conditions |
| Unary               | `++ -- - !`           | Work with one operand     |    |                               |
| Binary              | `+ - * / > < ==` etc. | Work with two operands    |    |                               |

---

# 14. Quick Revision

### Operator

A symbol used to perform an operation.

### Operand

A value or variable on which an operator works.

### Expression

A combination of values, variables, and operators that produces a result.

### Unary

Works with **one operand**.

```cpp
x++;
```

### Binary

Works with **two operands**.

```cpp
x + y;
```

### Arithmetic

Used for calculations.

```cpp
+  -  *  /  %
```

### Relational

Used for comparison.

```cpp
>  <  >=  <=  ==  !=
```

### Logical

Used to combine or reverse conditions.

```cpp
&&  ||  !
```

### Assignment

Used to assign a value.

```cpp
=
```

### Compound Assignment

Used to update a value in a shorter way.

```cpp
+=  -=  *=  /=  %=
```

### Increment / Decrement

Used to increase or decrease a value by 1.

```cpp
++  --
```

