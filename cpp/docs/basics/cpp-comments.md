---
layout: page
title: "C++ Comments Tutorial | Single-Line and Multi-Line Comments"
description: "Learn how to use comments in C++ with examples. Understand single-line and multi-line comments, why comments are important, and how they improve readability in C++ programs."
keywords: C++ comments, single line comments in C++, multi line comments in C++, comment syntax in C++, C++ tutorial, C++ programming examples, beginner C++, code comments, comments in programming, C++ readability, how to write comments in C++, C++ syntax, comment examples in C++
---

## 1. What are Comments?

**Comments** are notes written inside a program to explain the code.

Comments are **ignored by the compiler**, so they do not affect the execution of the program.

### Why do we use comments?

Comments help us to:

* Explain the purpose of code
* Make programs easier to understand
* Remember what a section of code does
* Make code easier to maintain

---

# 2. Types of Comments in C++

There are two common types of comments:

1. **Single-line comments**
2. **Multi-line comments**

---

# 3. Single-Line Comments

A **single-line comment** is used to write a comment on one line.

It starts with:

```cpp
//
```

Everything after `//` on that line is treated as a comment.

### Example 1

```cpp
#include <iostream>
using namespace std;

int main() {
    // This is a single-line comment

    cout << "Hello World";

    return 0;
}
```

### Output

```text
Hello World
```

The compiler ignores:

```cpp
// This is a single-line comment
```

---

## Example 2: Comment After Code

```cpp
int age = 20;  // Store student's age
```

Here:

* `int age = 20;` → actual code
* `// Store student's age` → comment

---

# 4. Multi-Line Comments

A **multi-line comment** is used when the comment covers **more than one line**.

It starts with:

```cpp
/*
```

and ends with:

```cpp
*/
```

### Example

```cpp
#include <iostream>
using namespace std;

int main() {

    /*
       This program displays
       a simple message
       on the screen.
    */

    cout << "Hello World";

    return 0;
}
```

### Output

```text
Hello World
```

Everything between:

```cpp
/*
```

and:

```cpp
*/
```

is ignored by the compiler.

---

# 5. Difference Between Single-Line and Multi-Line Comments

| Single-Line Comment         | Multi-Line Comment          |
| --------------------------- | --------------------------- |
| Used for one line           | Used for multiple lines     |
| Starts with `//`            | Starts with `/*`            |
| Ends at the end of the line | Ends with `*/`              |
| Example: `// My comment`    | Example: `/* My comment */` |

---

# 6. Complete Example

```cpp
#include <iostream>
using namespace std;

int main() {

    // Declare two numbers
    int a = 10;
    int b = 20;

    /*
       Add the two numbers
       and display the result.
    */
    int sum = a + b;

    cout << sum;

    return 0;
}
```

### Output

```text
30
```

---

# ⭐ Quick Revision

### Single-Line Comment

```cpp
// This is a comment
```

### Multi-Line Comment

```cpp
/*
   This is a
   multi-line comment
*/
```

### Remember

> **Comments are written for programmers, not for the compiler.**

They help make C++ programs **clear, readable, and easy to understand**.
