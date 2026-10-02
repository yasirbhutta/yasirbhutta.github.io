---
layout: page
title: "C++ Preprocessor Directives: #include, #define & Examples"
description: "Learn what C++ preprocessor directives do and how they work before compilation. Explore #include, #define, and conditional directives with a simple code example."
keywords: C++ preprocessor directives, preprocessor directive in C++, C++ #include, C++ #define, conditional compilation in C++, C++ preprocessor examples, C++ tutorial for beginners
---

### What is a Preprocessor Directive in C++?

A **preprocessor directive** is a special instruction in a C++ program that is processed **before the actual compilation of the program**.

* It starts with the **`#` symbol**.
* It does **not** end with a semicolon (`;`).
* It tells the **preprocessor** to perform a specific task before the compiler compiles the code.

### Example

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hello World";
    return 0;
}
```

Here:

```cpp
#include <iostream>
```

is a **preprocessor directive**.

It tells the preprocessor to include the contents of the **iostream** header file before compilation.

### Common Preprocessor Directives

| Directive  | Purpose                               |
| ---------- | ------------------------------------- |
| `#include` | Includes a header file                |
| `#define`  | Defines a constant or macro           |
| `#if`      | Starts a conditional section          |
| `#ifdef`   | Checks whether a macro is defined     |
| `#ifndef`  | Checks whether a macro is not defined |

**Simple definition for students:**

> **A preprocessor directive is an instruction beginning with `#` that is processed before the C++ program is compiled.**
