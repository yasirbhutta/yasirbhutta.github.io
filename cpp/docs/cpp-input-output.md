---
layout: page
title: "Programming in C++ – Input and Output"
description: "Learn C++ input and output with cin, cout, escape sequences, and manipulators. Includes practical examples, code snippets, and beginner-friendly exercises for taking user input, printing output, and formatting data. Perfect for students mastering C++ basics."
keywords: C++ input output, cin cout, C++ iostream, escape sequences, C++ manipulators, endl setw, C++ user input, standard output, C++ beginner tutorial, C++ examples, C++ practice problems, learn C++
---

[ Download PDF](/downloads/cpp-input-output.pdf)

## Standard Output

In C++, the standard output command is used to print data to the screen.
The syntax uses **`cout`**, which is part of the **iostream** library.

### ✅ **Basic Syntax**

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Your message here";
    return 0;
}
```

### 🔍 Explanation

* `#include <iostream>` → includes the input/output stream library.
* `cout` → standard output object.
* `<<` → *insertion operator* (sends data to output).

### 📌 Examples

#### 1. Printing text

```cpp
cout << "Hello World!";
```

#### 2. Printing variables

```cpp
int a = 10;
cout << "Value of a is: " << a;
```

#### 3. Printing multiple lines

```cpp
cout << "Line 1" << endl;
cout << "Line 2";
```

### ✔ Alternative (without `using namespace std`)

```cpp
std::cout << "Hello World!";
```

---

#### Example

**Question:** Write a C++ program that takes two floating-point numbers as input from the user, adds them, and displays the sum on the screen.

```cpp
#include <iostream>
using namespace std;

int main() {
    float num1, num2, sum;

    cout << "Enter first number: ";
    cin >> num1;

    cout << "Enter second number: ";
    cin >> num2;

    sum = num1 + num2;

    cout << "The sum is: " << sum << endl;

    return 0;
}
```

### ✔ What this program does:

* Takes two floating-point numbers as input.
* Adds them.
* Displays the result using `cout`.

---

#### Example

**Question:** Write a C++ program that takes the height and width of a rectangle as input from the user, calculates its area using the formula area = height × width, and displays the result on the screen.

```cpp
#include <iostream>
using namespace std;

int main() {
    float height, width, area;

    cout << "Enter height of the rectangle: ";
    cin >> height;

    cout << "Enter width of the rectangle: ";
    cin >> width;

    area = height * width;

    cout << "The area of the rectangle is: " << area << endl;

    return 0;
}
```

## Escape Sequences

# ✅ **1. Newline (`\n`)**

### **Question Statement**

Write a C++ program that prints two lines of text using the newline escape sequence `\n`.

### **Example**

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hello World!\n";
    cout << "Welcome to C++.";
    return 0;
}
```

---

# ✅ **2. Tab (`\t`)**

### **Question Statement**

Write a C++ program that prints a list of items, each separated by a tab (`\t`).

### **Example**

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Item\tPrice\n";
    cout << "Apple\t100\n";
    cout << "Mango\t150\n";
    return 0;
}
```

---

# ✅ **3. Backslash (`\\`)**

### **Question Statement**

Write a C++ program that displays a file path containing backslashes using the escape sequence `\\`.

### **Example**

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "File path: C:\\Users\\Student\\Documents";
    return 0;
}
```

---

# ✅ **4. Double Quote (`\"`)**

### **Question Statement**

Write a C++ program that prints a sentence containing double quotation marks using the escape sequence `\"`.

### **Example**

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "He said, \"C++ is fun!\"";
    return 0;
}
```

---

# ✅ **5. Single Quote (`\'`)**

### **Question Statement**

Write a C++ program that prints a character enclosed in single quotes using the escape sequence `\'`.

### **Example**

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "The character is: \'A\'";
    return 0;
}
```

---

# ✅ **6. Carriage Return (`\r`)**

(Overwrites from the beginning of the line; behavior depends on console.)

### **Question Statement**

Write a C++ program that prints a word and then overwrites it using the carriage return `\r`.

### **Example**

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hello\rHi";
    return 0;
}
```

---

## C++ Manipulators

# ✅ **1. Manipulator: `endl`**

### **Question Statement**

Write a C++ program that prints two lines of text using the manipulator `endl` to move the cursor to the next line.

### **Example**

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hello, C++ beginners!" << endl;
    cout << "This line is printed using endl.";
    return 0;
}
```

---

# ✅ **2. Manipulator: `setw`**

### **(Note: `setw` requires `<iomanip>` library)**

### **Question Statement**

Write a C++ program that prints a simple table of numbers using the manipulator `setw` to align the output in columns.

### **Example**

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    cout << setw(10) << "Number" << setw(10) << "Square" << endl;
    cout << setw(10) << 2 << setw(10) << 4 << endl;
    cout << setw(10) << 5 << setw(10) << 25 << endl;
    cout << setw(10) << 10 << setw(10) << 100 << endl;

    return 0;
}
```

---

## Standard Input

## ⭐ **1. Basic Syntax of `cin`**

### **Syntax**

```cpp
cin >> variable;
```

* `cin` → standard input stream
* `>>` → extraction operator (takes input from keyboard)
* `variable` → where the input is stored

You can take multiple inputs in one line:

```cpp
cin >> a >> b >> c;
```

---

# ✅ **Example 1: Input a Single Integer**

### **Question Statement**

Write a C++ program that asks the user to enter an integer and displays the entered value.

### **Example**

```cpp
#include <iostream>
using namespace std;

int main() {
    int num;

    cout << "Enter an integer: ";
    cin >> num;

    cout << "You entered: " << num;
    return 0;
}
```

---

# ✅ **Example 2: Input Two Numbers and Add Them**

### **Question Statement**

Write a C++ program that takes two integers as input from the user using `cin` and prints their sum.

### **Example**

```cpp
#include <iostream>
using namespace std;

int main() {
    int a, b;

    cout << "Enter two numbers: ";
    cin >> a >> b;

    cout << "Sum = " << a + b;
    return 0;
}
```

---

# ✅ **Example 3: Input a Floating-Point Number**

### **Question Statement**

Write a C++ program that reads a floating-point number from the user and shows it on the screen.

### **Example**

```cpp
#include <iostream>
using namespace std;

int main() {
    float value;

    cout << "Enter a float value: ";
    cin >> value;

    cout << "You entered: " << value;
    return 0;
}
```

---

# ✅ **Example 4: Input a Character**

### **Question Statement**

Write a C++ program that asks the user to input a single character and prints it.

### **Example**

```cpp
#include <iostream>
using namespace std;

int main() {
    char ch;

    cout << "Enter a character: ";
    cin >> ch;

    cout << "You entered: " << ch;
    return 0;
}
```

---

# ✅ **Example 5: Input a Word (Single String)**

### **Question Statement**

Write a C++ program that reads a single word using `cin` and displays a message with that word.

### **Example**

```cpp
#include <iostream>
using namespace std;

int main() {
    string name;

    cout << "Enter your name: ";
    cin >> name;

    cout << "Welcome, " << name << "!";
    return 0;
}
```

---







