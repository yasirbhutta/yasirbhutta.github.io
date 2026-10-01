---
layout: page
title: "C++ Constants Tutorial | const Keyword in C++"
description: "Learn C++ constants with simple examples and explanations. Understand the const keyword, constant variables, and how to use fixed values in C++ programs."
keywords: C++ constants, const keyword in C++, constant variables, constant in C++, C++ tutorial, C++ programming examples, beginner C++, fixed values in C++, values that do not change, C++ variables, constant declarations, C++ syntax, C++ const examples
---


## 1. What is a Constant?

A **constant** is a value that **does not change during the execution of a program**.

### Example

```cpp
const int age = 20;
```

Here, `age` is a constant. Its value cannot be changed later in the program.

```cpp
age = 25;   // Error
```

---

# 2. Why Do We Use Constants?

Constants are useful when a value should remain the same throughout the program.

### Common examples

* Number of days in a week
* Value of π
* Maximum marks
* Tax rate
* University name or fixed code
* Conversion values

### Example

```cpp
const int DAYS_IN_WEEK = 7;
```

Using a constant makes the program:

* **Easy to understand**
* **Easy to maintain**
* **Less likely to have accidental changes**
* **More readable**

---

# 3. Literal Constants

A **literal constant** is a fixed value written directly in the program.

### Example

```cpp
int age = 20;
```

Here, `20` is a **literal constant**.

```cpp
double price = 250.50;
char grade = 'A';
```

Here:

* `250.50` → literal constant
* `'A'` → literal constant

---

# 4. Types of Literal Constants

The common types of literal constants are:

1. **Integer literals**
2. **Floating-point literals**
3. **Character literals**
4. **String literals**
5. **Boolean literals**

---

## 4.1 Integer Literals

Integer literals are **whole numbers without a decimal point**.

### Examples

```cpp
10
25
100
-50
0
```

Example:

```cpp
int marks = 100;
```

Here, `100` is an integer literal.

---

## 4.2 Floating-Point Literals

Floating-point literals contain a **decimal point**.

### Examples

```cpp
10.5
25.75
3.14
-5.5
```

Example:

```cpp
double price = 250.50;
```

Here, `250.50` is a floating-point literal.

---

## 4.3 Character Literals

A character literal represents **one character** and is written inside **single quotation marks**.

### Examples

```cpp
'A'
'B'
'5'
'$'
```

Example:

```cpp
char grade = 'A';
```

> `'A'` is a character literal.

---

## 4.4 String Literals

A string literal is a sequence of characters written inside **double quotation marks**.

### Examples

```cpp
"Hello"
"Pakistan"
"Computer Science"
```

Example:

```cpp
cout << "Hello World";
```

Here:

```text
"Hello World"
```

is a string literal.

---

## 4.5 Boolean Literals

Boolean literals have only two values:

```cpp
true
false
```

Example:

```cpp
bool passed = true;
```

Here, `true` is a Boolean literal.

---

# 5. `const` Qualifier

The `const` keyword is used to make a variable **constant**.

### Syntax

```cpp
const data_type variable_name = value;
```

### Example

```cpp
const int MAX_MARKS = 100;
```

`MAX_MARKS` cannot be changed.

```cpp
MAX_MARKS = 90;   // Error
```

---

## Example Program

```cpp
#include <iostream>
using namespace std;

int main() {

    const int DAYS = 7;

    cout << DAYS;

    return 0;
}
```

### Output

```text
7
```

### Important

A `const` variable should normally be **initialized when it is declared**:

```cpp
const int x = 10;
```

---

# 6. `#define` Directive

`#define` is a **preprocessor directive** used to define a symbolic constant.

### Syntax

```cpp
#define NAME value
```

### Example

```cpp
#define PI 3.14
```

Now we can use:

```cpp
cout << PI;
```

### Complete Example

```cpp
#include <iostream>
using namespace std;

#define PI 3.14

int main() {

    double radius = 5;
    double area = PI * radius * radius;

    cout << area;

    return 0;
}
```

### Output

```text
78.5
```

---

# 7. `const` vs `#define`

| `const`                      | `#define`                     |
| ---------------------------- | ----------------------------- |
| Uses the `const` keyword     | Uses `#define`                |
| Has a data type              | Does not have a C++ data type |
| Creates a constant variable  | Creates a preprocessor macro  |
| Checked by the compiler      | Replaced by the preprocessor  |
| Example: `const int X = 10;` | Example: `#define X 10`       |

### Which should beginners prefer?

For defining typed constants in modern C++, **`const` is generally preferred** because it works with C++'s type system.

---

# 8. Quick Revision

### Constant

> A value that does not change during program execution.

```cpp
const int DAYS = 7;
```

### Literal Constant

> A fixed value written directly in the program.

```cpp
int age = 20;
```

`20` is a literal constant.

### Common Literal Types

```text
Integer       → 100
Floating      → 3.14
Character     → 'A'
String        → "Hello"
Boolean       → true / false
```

### `const`

```cpp
const int MAX = 100;
```

### `#define`

```cpp
#define PI 3.14
```

### ⭐ Easy Rule to Remember

**Literal = value written directly**

**`const` = constant variable with a type**

**`#define` = preprocessor symbolic constant**
