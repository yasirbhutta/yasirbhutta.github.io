---
layout: page
title: "C++ Operator Precedence"
description: "Learn C++ operator precedence with clear examples and simple explanations. Understand how arithmetic, relational, logical, assignment, unary, and increment/decrement operators are evaluated in C++ programs."
keywords: C++ operator precedence, operators in C++, arithmetic operator precedence, assignment operators in C++, relational operators, logical operators, unary operators, increment operator, decrement operator, C++ tutorial, C++ programming examples, beginner C++, precedence rules in C++, expression evaluation in C++, C++ operators explained
---

## 1. What is Operator Precedence?

**Operator precedence** tells C++ **which operator should be performed first** when an expression contains more than one operator.

### Example

```cpp
int result = 5 + 3 * 2;
```

Multiplication `*` has higher precedence than addition `+`.

So:

```text
5 + (3 * 2)
= 5 + 6
= 11
```

**Answer: 11**

---

## 2. Basic Rule

Remember:

> **Higher precedence → performed first**

For example:

```cpp
10 - 4 / 2
```

`/` has higher precedence than `-`.

```text
10 - (4 / 2)
= 10 - 2
= 8
```

---

## 3. Common Operator Precedence in C++

For beginners, remember this order:

| Priority | Operators               | Meaning                           |   |            |
| -------- | ----------------------- | --------------------------------- | - | ---------- |
| 1        | `()`                    | Parentheses                       |   |            |
| 2        | `++` `--`               | Increment / Decrement             |   |            |
| 3        | `*` `/` `%`             | Multiplication, Division, Modulus |   |            |
| 4        | `+` `-`                 | Addition, Subtraction             |   |            |
| 5        | `<` `<=` `>` `>=`       | Relational                        |   |            |
| 6        | `==` `!=`               | Equality                          |   |            |
| 7        | `&&`                    | Logical AND                       |   |            |
| 8        | `                       |                                   | ` | Logical OR |
| 9        | `=` `+=` `-=` `*=` `/=` | Assignment                        |   |            |

### Easy way to remember

```text
()
↓
++ --
↓
* / %
↓
+ -
↓
< <= > >=
↓
== !=
↓
&&
↓
||
↓
=
```

---

## 4. Parentheses Have the Highest Priority

Use parentheses `()` when you want something to be calculated first.

```cpp
int result = (5 + 3) * 2;
```

First:

```text
5 + 3 = 8
```

Then:

```text
8 * 2 = 16
```

**Answer: 16**

Compare:

```cpp
int result = 5 + 3 * 2;
```

Answer:

```text
11
```

But:

```cpp
int result = (5 + 3) * 2;
```

Answer:

```text
16
```

---

## 5. `*`, `/`, and `%`

These operators have the same precedence.

```cpp
int x = 20 / 5 * 2;
```

When operators have the **same precedence**, C++ generally evaluates them **from left to right**.

```text
20 / 5 = 4
4 * 2 = 8
```

**Answer: 8**

### Another example

```cpp
int x = 17 % 5 + 2;
```

First `%`:

```text
17 % 5 = 2
```

Then:

```text
2 + 2 = 4
```

**Answer: 4**

---

## 6. `+` and `-`

`+` and `-` have the same precedence and are evaluated from **left to right**.

```cpp
int x = 10 - 3 + 2;
```

First:

```text
10 - 3 = 7
```

Then:

```text
7 + 2 = 9
```

**Answer: 9**

---

---

# 7. Example: Complete Expression

Consider:

```cpp
int result = 5 + 2 * 3;
```

### Step 1: `*`

```text
2 * 3 = 6
```

### Step 2: `+`

```text
5 + 6 = 11
```

Therefore:

```text
result = 11
```

---

# 8. Example with Parentheses

```cpp
int result = (5 + 2) * 3;
```

### Step 1

```text
5 + 2 = 7
```

### Step 2

```text
7 * 3 = 21
```

Therefore:

```text
result = 21
```

---

# 9. Important Rule: Left-to-Right

When two operators have the **same precedence**, they are generally evaluated from **left to right**.

Example:

```cpp
int result = 20 / 5 * 2;
```

```text
20 / 5 = 4
4 * 2 = 8
```

So:

```text
Answer = 8
```

Not:

```text
20 / (5 * 2) = 2
```

---

# 10. Best Practic

When an expression becomes difficult to understand, **use parentheses**.

Instead of:

```cpp
int result = a + b * c - d / e;
```

Think of it as:

```cpp
int result = a + (b * c) - (d / e);
```

Parentheses make the order clear and reduce mistakes.

---

## Quick Revision

### Remember this order:

**Parentheses → Increment/Decrement → Multiply/Divide/Modulus → Add/Subtract → Relational → Equality → AND → OR → Assignment**

```text
()
++ --
* / %
+ -
< <= > >=
== !=
&&
||
=
```

### Golden Rule ⭐

> **First check parentheses, then higher-precedence operators, and when operators have equal precedence, follow their associativity (commonly left-to-right for arithmetic operators).**

## Examples

### C++ Example: Operator Prcedence

**Question:** Write a C++ program to demonstrate the concept of operator precedence in C++.

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 10, b = 5, c = 2;

    // Without parentheses
    int result1 = a + b * c; 
    // Multiplication (*) has higher precedence than addition (+)
    cout << "Result without parentheses (a + b * c): " << result1 << endl;

    // With parentheses
    int result2 = (a + b) * c; 
    // Parentheses change the order of evaluation
    cout << "Result with parentheses ((a + b) * c): " << result2 << endl;

    // Combining multiple operators
    int result3 = a + b - c * 2 / 2;
    // Operator precedence: *, / first, then +, -
    cout << "Result of a + b - c * 2 / 2: " << result3 << endl;

    return 0;
}
```

---

### **Explanation:**

1. **Operator Precedence** determines the **order in which operators are evaluated** in an expression.
2. **Higher precedence operators** are evaluated **first**.

   * Example: `*` and `/` have higher precedence than `+` and `-`.
3. **Parentheses `()`** can be used to **override the default precedence**.
4. **Example:**

   * `a + b * c` → multiplication happens first: `5 * 2 = 10`, then `a + 10 = 20`
   * `(a + b) * c` → parentheses first: `10 + 5 = 15`, then `15 * 2 = 30`

---

