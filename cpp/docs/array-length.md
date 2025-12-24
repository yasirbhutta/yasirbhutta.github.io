---
layout: page
title: "C++ Array Length — How to Get Array Size with sizeof & std::size"
description: "Learn how to determine an array's length in C++ using sizeof, std::size, and template helpers. Clear examples, common pitfalls, and best practices for safe array sizing."
keywords: C++ array length, array size C++, sizeof array, std::size, compute array length, C++ arrays tutorial, array length example, array size pitfalls
---

## What is the length of an array?

The **length (or size)** of an array means:

> **How many elements are stored in the array**

Example:

```cpp
int marks[5] = {60, 70, 80, 90, 100};
```

➡ The length of this array is **5** because it has **5 values**.

---

## Method 1: Finding array length using `sizeof` (Most Common in C++)

### Formula

```cpp
array_length = sizeof(array) / sizeof(array[0]);
```

### Why this works

* `sizeof(array)` → total memory used by the array
* `sizeof(array[0])` → memory used by **one element**
* Dividing gives the **number of elements**

---

### Example 1: Integer Array

```cpp
#include <iostream>
using namespace std;

int main() {
    int numbers[] = {10, 20, 30, 40, 50};

    int length = sizeof(numbers) / sizeof(numbers[0]);

    cout << "Length of array: " << length;

    return 0;
}
```

### Output

```
Length of array: 5
```

---

### Example 2: Character Array

```cpp
#include <iostream>
using namespace std;

int main() {
    char vowels[] = {'a', 'e', 'i', 'o', 'u'};

    int length = sizeof(vowels) / sizeof(vowels[0]);

    cout << "Number of vowels: " << length;

    return 0;
}
```

### Output

```
Number of vowels: 5
```

---

## Method 2: Length of a String (Character Array)

### Using `strlen()` (for strings only)

```cpp
#include <iostream>
#include <cstring>
using namespace std;

int main() {
    char name[] = "Yasir";

    cout << "Length of name: " << strlen(name);

    return 0;
}
```

### Output

```
Length of name: 5
```

🔹 `strlen()` counts characters **excluding** the `'\0'` (null character).

---

## Method 3: Using Loop (Manual Counting – Learning Purpose)

```cpp
#include <iostream>
using namespace std;

int main() {
    int arr[] = {2, 4, 6, 8, 10};
    int count = 0;

    for(int i = 0; i < 5; i++) {
        count++;
    }

    cout << "Array length: " << count;

    return 0;
}
```

⚠️ This works only when you **already know the size**.

---

## Important Note ⚠️

❌ You **cannot** find the length of an array using `sizeof` inside a function when passed as a parameter.

Example (Wrong):

```cpp
void show(int arr[]) {
    cout << sizeof(arr);   // gives size of pointer, not array
}
```

✔ Correct way: pass the size separately.

---

## Summary Table

| Method                           | Used For      | Beginner Friendly |
| -------------------------------- | ------------- | ----------------- |
| `sizeof(array)/sizeof(array[0])` | Any array     | ✅ Best            |
| `strlen()`                       | Strings only  | ✅                 |
| Loop counting                    | Practice only | ⚠️                |

---

## 📘 **Related Topics**

- [C++ One-Dimensional Arrays — Syntax & Examples](cpp-arrays.md)
- 