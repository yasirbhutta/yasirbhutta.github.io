---
layout: default
title: Programming in C++
description: Learn c++ programming from scratch with our free, beginner-friendly tutorials. Access open-source content, download PDF lessons, and start coding today!.
keywords: "c++ tutorial for beginners, learn c++ programming, free c++ lessons, c++ pdf tutorials, open-source c++ guide, c++ coding for beginners, c++ exercises and projects, c++ programming basics, downloadable c++ resources, c++ step-by-step guide"
---

## Identifier
## Keywords
## Data Types

---

### **C++ Program: Understanding Data Types**

**Question:** Write a C++ program to demonstrate different data types (int, float, double, char, bool, string) and print example values for each.

```cpp
#include <iostream>
using namespace std;

int main() {
    // Integer: whole numbers
    int age = 20;
    cout << "Integer example (age): " << age << endl;

    // Floating-point: numbers with decimal
    float height = 5.9;
    double weight = 70.5;
    cout << "Float example (height): " << height << endl;
    cout << "Double example (weight): " << weight << endl;

    // Character: single letter or symbol
    char grade = 'A';
    cout << "Character example (grade): " << grade << endl;

    // Boolean: true or false
    bool isStudent = true;
    cout << "Boolean example (isStudent): " << isStudent << endl;

    // String: sequence of characters
    string name = "Ali";
    cout << "String example (name): " << name << endl;

    return 0;
}
```

---

### **Explanation**

1. **int** → Stores whole numbers like 1, 10, -5.
2. **float** → Stores decimal numbers, e.g., 3.14.
3. **double** → Similar to float but with more precision.
4. **char** → Stores a single character like `'A'` or `'x'`.
5. **bool** → Stores `true` or `false`.
6. **string** → Stores text or words like `"Hello"`.

---

### **Sample Output**

```
Integer example (age): 20
Float example (height): 5.9
Double example (weight): 70.5
Character example (grade): A
Boolean example (isStudent): 1
String example (name): Ali
```

> Note: Boolean values print as `1` (true) or `0` (false) in C++.

---

Sure! Here’s a **beginner-friendly example** showing how to use the **character (`char`) data type** in C++ 👇

---

**Question:** Write a C++ program to demonstrate the use of the `char` (character) data type and display example values.

---

### ✅ **C++ Program: Character Data Type Example**

```cpp
#include <iostream>
using namespace std;

int main() {
    // Character variable
    char grade = 'A';
    char symbol = '#';
    char letter = 'Z';

    cout << "Character example 1 (grade): " << grade << endl;
    cout << "Character example 2 (symbol): " << symbol << endl;
    cout << "Character example 3 (letter): " << letter << endl;

    return 0;
}
```

---

### 💡 **Explanation**

* The `char` data type is used to store a **single character**, such as a letter, digit, or symbol.
* Character values are always enclosed in **single quotes (' ')**.
* Each character has an **ASCII code** (a numeric value in computer memory).

---

### 🖥️ **Sample Output**

```
Character example 1 (grade): A
Character example 2 (symbol): #
Character example 3 (letter): Z
```

---

