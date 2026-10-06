---
layout: page
title: "C++ Manipulators Tutorial: endl, setw, and Output Formatting"
description: "Learn C++ manipulators like endl and setw with beginner-friendly examples. Understand how to format output, align columns, and improve console display in C++ programs."
keywords: C++ manipulators, endl in C++, setw in C++, C++ output formatting, C++ iomanip, formatting output in C++, C++ tutorial, C++ examples, beginner C++ programming, C++ alignment, cout manipulators
---

C++ **manipulators** are special tools used with `cout` to control or format the output.

In this lesson, we will learn two commonly used manipulators:

1. `endl` – moves the cursor to the next line.
2. `setw` – sets the width of the output field.

---

# 1. Manipulator: `endl`

### What is `endl`?

`endl` is used with `cout` to:

* Move the cursor to the **next line**.
* Complete the current output line.
* Make the output easier to read.

### Syntax

```cpp
cout << "Text" << endl;
```

### Example

**Question:**
Write a C++ program that prints two lines of text using the manipulator `endl`.

### Program

```cpp
#include <iostream>
using namespace std;

int main() {

    cout << "Hello, C++ beginners!" << endl;
    cout << "This line is printed using endl.";

    return 0;
}
```

### Output

```text
Hello, C++ beginners!
This line is printed using endl.
```

### Understand the Code

```cpp
cout << "Hello, C++ beginners!" << endl;
```

* `cout` displays the text.
* `"Hello, C++ beginners!"` is the text to display.
* `endl` moves the cursor to the next line.

Therefore, the second `cout` statement starts printing from a **new line**.

### Remember

`endl` is mainly used to **move output to the next line**.

---

# 2. Manipulator: `setw`

### What is `setw`?

`setw` means **set width**.

It is used to set the minimum width of the output field. It is especially useful when displaying data in **columns or tables**.

### Important

`setw` is available in the `<iomanip>` library.

Therefore, we need to include:

```cpp
#include <iomanip>
```

### Syntax

```cpp
setw(number)
```

For example:

```cpp
cout << setw(10) << 25;
```

This gives the output field a width of **10 characters**.

---

## Example: Using `setw` to Create a Table

**Question:**
Write a C++ program that prints a simple table of numbers using `setw` to align the output in columns.

### Program

```cpp
#include <iostream>
#include <iomanip>

using namespace std;

int main() {

    cout << setw(10) << "Number"
         << setw(10) << "Square" << endl;

    cout << setw(10) << 2
         << setw(10) << 4 << endl;

    cout << setw(10) << 5
         << setw(10) << 25 << endl;

    cout << setw(10) << 10
         << setw(10) << 100 << endl;

    return 0;
}
```

### Output

```text
    Number    Square
         2         4
         5        25
        10       100
```

### Understand the Code

Consider this statement:

```cpp
cout << setw(10) << 2
     << setw(10) << 4 << endl;
```

* `setw(10)` gives the first value a field width of **10 characters**.
* `2` is displayed within that field.
* The second `setw(10)` gives the next value another field width of **10 characters**.
* `4` is displayed within the second field.
* `endl` moves the cursor to the next line.

This helps us display values in **aligned columns**.

---

## Important Point About `setw`

`setw()` applies only to the **next output item**.

For example:

```cpp
cout << setw(10) << 25 << 50;
```

Here, `setw(10)` applies to `25` only. It does not automatically apply to `50`.

If we want both values to have a width of 10, we write:

```cpp
cout << setw(10) << 25
     << setw(10) << 50;
```

---

# Quick Comparison

| Manipulator | Purpose                                 | Header File  |
| ----------- | --------------------------------------- | ------------ |
| `endl`      | Moves output to the next line           | `<iostream>` |
| `setw()`    | Sets the width of the next output field | `<iomanip>`  |

## Remember

* `endl` → **New line**
* `setw()` → **Set output width**
* `setw()` requires **`<iomanip>`**
* `setw()` affects only the **next output item**

---

# Practice Questions

### Practice 1 – `endl`

Write a C++ program that displays your:

* Name
* Department
* Semester

Use `endl` to print each item on a separate line.

### Practice 2 – `setw`

Write a C++ program to display the following table using `setw(10)`:

```text
Number    Cube
2         8
3         27
4         64
5         125
```

### Practice 3 – Both Manipulators

Write a C++ program that uses both `endl` and `setw()` to display a simple student information table containing:

* Roll No.
* Name
* Marks
