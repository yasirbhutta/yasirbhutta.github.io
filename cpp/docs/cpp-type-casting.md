---
layout: page
title: "Type Casting in C++"
description: "Learn type casting in C++ with simple explanations and examples. Understand implicit and explicit casting, conversion between int and float, and how C++ handles data type conversion in programs."
keywords: type casting in C++, C++ type conversion, implicit casting in C++, explicit casting in C++, int to float conversion, float to int conversion, C++ data types, casting operators in C++, C++ tutorial, C++ programming examples, beginner C++, conversion in C++, type conversion examples, C++ casting explained
---

## 1. What is Type Casting?

**Type casting** means converting a value from **one data type to another data type**.

For example:

```cpp
int x = 10;
double y = x;
```

Here, `int` is converted to `double`.

```text
int → double
```

---

# 2. Types of Type Casting

There are two basic types:

1. **Implicit Type Casting**
2. **Explicit Type Casting**

---

## 3. Implicit Type Casting

**Implicit casting happens automatically.**

The compiler performs the conversion without being told.

### Example

```cpp
int x = 10;
double y = x;

cout << y;
```

### Output

```text
10
```

Here:

```text
int → double
```

The compiler automatically converts `10` into `10.0`.

### Remember

> **Implicit = Automatic**

---

## 4. Explicit Type Casting

**Explicit casting is done by the programmer.**

The programmer tells C++ which data type to convert the value into.

### Example

```cpp
double x = 10.75;
int y = (int)x;

cout << y;
```

### Output

```text
10
```

Here:

```text
double → int
```

The decimal part `.75` is removed.

### Remember

> **Explicit = Programmer tells C++**

---

# 5. Another Example

```cpp
int a = 5;
int b = 2;

double result = (double)a / b;

cout << result;
```

### Output

```text
2.5
```

The programmer explicitly converts `a`:

```text
int → double
```

So the calculation becomes:

```text
5.0 / 2 = 2.5
```

---

## 6. Implicit vs Explicit Casting

| Implicit Casting             | Explicit Casting                |
| ---------------------------- | ------------------------------- |
| Automatic                    | Done by programmer              |
| Compiler performs conversion | Programmer specifies conversion |
| No special casting syntax    | Casting syntax is used          |
| `double y = x;`              | `int y = (int)x;`               |
| Example: `int → double`      | Example: `double → int`         |


# 7. Exmaples

## Example 1: Implicit Casting — `int` to `double`

```cpp
#include <iostream>
using namespace std;

int main() {
    int num = 10;
    double result = num;

    cout << result;

    return 0;
}
```

**Output:**

```text
10
```

**Understand the Code:**

* `num` is an `int`.
* `result` is a `double`.
* C++ automatically converts `int` to `double`.
* This is **implicit casting**.

---

## Example 2: Explicit Casting — `double` to `int`

```cpp
#include <iostream>
using namespace std;

int main() {
    double num = 15.75;
    int result = (int)num;

    cout << result;

    return 0;
}
```

**Output:**

```text
15
```

**Understand the Code:**

* `num` contains `15.75`.
* `(int)num` converts it to an integer.
* The decimal part `.75` is removed.
* This is **explicit casting**.

---

## Example 3: Explicit Casting in Division

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 5;
    int b = 2;

    double result = (double)a / b;

    cout << result;

    return 0;
}
```

**Output:**

```text
2.5
```

**Understand the Code:**

* Normally, `5 / 2` gives `2` because both values are integers.
* `(double)a` converts `5` into `5.0`.
* Now the calculation becomes `5.0 / 2`.
* The result is `2.5`.

### ⭐ Remember

**Implicit casting:** C++ does it automatically.

**Explicit casting:** The programmer does it using:

```cpp
(type)value
```

Example:

```cpp
(double)a
(int)num
```

