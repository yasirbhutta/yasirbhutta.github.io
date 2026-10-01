---
layout: page
title: "C++ `sizeof` Operator"
description: "Learn how the sizeof operator works in C++ with easy examples. Understand how to find the size of variables and data types in bytes for memory management and C++ programming."
keywords: sizeof operator in C++, C++ sizeof, sizeof variable, sizeof data type, size of data types in C++, memory size in C++, C++ tutorial, C++ programming examples, beginner C++, bytes in C++, data type size, sizeof examples, C++ memory management
---

## 1. What is the `sizeof` Operator?

The **`sizeof` operator** is used to find the **size of a data type or variable in bytes**.

### Syntax

```cpp
sizeof(variable)
```

or

```cpp
sizeof(data_type)
```

The result of `sizeof` is given in **bytes**.

---

## 2. Example: `sizeof` with Data Types

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << sizeof(int) << endl;
    cout << sizeof(float) << endl;
    cout << sizeof(double) << endl;
    cout << sizeof(char) << endl;

    return 0;
}
```

**Possible Output:**

```text
4
4
8
1
```

> **Note:** The size of some data types can vary depending on the compiler and computer system. `char` is always 1 byte.

---

## 3. Example: `sizeof` with Variables

```cpp
#include <iostream>
using namespace std;

int main() {
    int age = 20;
    double salary = 50000.5;
    char grade = 'A';

    cout << sizeof(age) << endl;
    cout << sizeof(salary) << endl;
    cout << sizeof(grade) << endl;

    return 0;
}
```

**Possible Output:**

```text
4
8
1
```

### Understand the Code

* `sizeof(age)` → finds the size of the `int` variable.
* `sizeof(salary)` → finds the size of the `double` variable.
* `sizeof(grade)` → finds the size of the `char` variable.

---

## 4. `sizeof` Does Not Give the Value

Consider:

```cpp
int age = 20;

cout << age << endl;
cout << sizeof(age) << endl;
```

**Output:**

```text
20
4
```

Here:

* `age` gives the **value** → `20`
* `sizeof(age)` gives the **memory size** → `4 bytes` on a typical system.

---

## 5. `sizeof` with Arrays

`sizeof` can also be used with arrays.

```cpp
#include <iostream>
using namespace std;

int main() {
    int numbers[5];

    cout << sizeof(numbers);

    return 0;
}
```

If an `int` is 4 bytes:

```text
5 × 4 = 20 bytes
```

**Output:**

```text
20
```

---

## 6. Finding the Number of Elements in an Array

We can use `sizeof` to find the number of elements in an array:

```cpp
int numbers[5];

int total = sizeof(numbers) / sizeof(numbers[0]);

cout << total;
```

**Output:**

```text
5
```

### Why?

```text
sizeof(numbers)     = 20 bytes
sizeof(numbers[0])  = 4 bytes

20 / 4 = 5
```

Therefore, the array contains **5 elements**.

---

# ⭐ Quick Revision

| Expression                         | Purpose                  |
| ---------------------------------- | ------------------------ |
| `sizeof(int)`                      | Size of `int`            |
| `sizeof(float)`                    | Size of `float`          |
| `sizeof(x)`                        | Size of variable `x`     |
| `sizeof(array)`                    | Total size of array      |
| `sizeof(array) / sizeof(array[0])` | Number of array elements |

### Remember

> **`sizeof` tells us how many bytes are occupied by a data type, variable, or object.**

**Important:** `sizeof` returns a size in **bytes**, not bits.
