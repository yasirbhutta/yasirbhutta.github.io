---
layout: page
title: "Standard Input in C++ Using `cin`"
description: "Learn how to use C++ cin for standard input with beginner-friendly examples. Understand cin >> syntax, multiple inputs, user input, and simple C++ programs for reading integers, floats, chars, and strings."
keywords: C++ cin, cin in C++, C++ input, standard input in C++, cin >>, C++ user input, input output in C++, C++ program examples, C++ beginner tutorial, learn C++ input, C++ string input, C++ integer input
---

## 1. What is Standard Input?

In C++, **standard input** is used to take data from the user through the keyboard.

The standard input object in C++ is:

```cpp
cin
```

`cin` is provided by the **`<iostream>`** library.

We commonly use `cin` to take:

* Integers
* Floating-point numbers
* Characters
* Words
* Multiple values

---

# 2. Basic Syntax of `cin`

The basic syntax is:

```cpp
cin >> variable;
```

### Understanding the Syntax

* `cin` → standard input object.
* `>>` → **extraction operator**, which takes data from the keyboard.
* `variable` → the variable where the input is stored.

Think of it as:

```text
Keyboard → cin → Variable
```

### Example

```cpp
int age;

cin >> age;
```

If the user enters:

```text
20
```

the value `20` is stored in the variable `age`.

---

# 3. Taking Multiple Inputs

We can take multiple values using a single `cin` statement.

### Syntax

```cpp
cin >> a >> b >> c;
```

For example:

```cpp
int a, b, c;

cin >> a >> b >> c;
```

If the user enters:

```text
10 20 30
```

then:

```text
a = 10
b = 20
c = 30
```

### Important

The user can enter the values separated by **spaces** or by pressing **Enter**.

For example, both are valid:

```text
10 20 30
```

or:

```text
10
20
30
```

---

# 4. Input an Integer

### Question

Write a C++ program that asks the user to enter an integer and displays the entered value.

### Program

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

### Sample Output

```text
Enter an integer: 25
You entered: 25
```

### Understand the Code

```cpp
int num;
```

Creates an integer variable named `num`.

```cpp
cin >> num;
```

Takes an integer from the user and stores it in `num`.

```cpp
cout << "You entered: " << num;
```

Displays the value stored in `num`.

---

# 5. Input Two Numbers and Add Them

### Question

Write a C++ program that takes two integers from the user and displays their sum.

### Program

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

### Sample Output

```text
Enter two numbers: 10 20
Sum = 30
```

### Understand the Code

```cpp
cin >> a >> b;
```

takes two values from the user:

* First value → stored in `a`
* Second value → stored in `b`

Then:

```cpp
a + b
```

calculates their sum.

---

# 6. Input a Floating-Point Number

### Question

Write a C++ program that reads a floating-point number from the user and displays it.

### Program

```cpp
#include <iostream>
using namespace std;

int main() {

    float value;

    cout << "Enter a floating-point value: ";
    cin >> value;

    cout << "You entered: " << value;

    return 0;
}
```

### Sample Output

```text
Enter a floating-point value: 12.5
You entered: 12.5
```

### Remember

Use `float` when you want to store numbers that may contain a decimal part.

For example:

```text
12.5
7.25
100.75
```

---

# 7. Input a Character

### Question

Write a C++ program that asks the user to enter a single character and displays it.

### Program

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

### Sample Output

```text
Enter a character: A
You entered: A
```

### Remember

A `char` variable stores a **single character**.

Examples:

```text
A
B
7
$
```

---

# 8. Input a Word

### Question

Write a C++ program that reads a single word from the user and displays a welcome message.

### Program

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {

    string name;

    cout << "Enter your name: ";
    cin >> name;

    cout << "Welcome, " << name << "!";

    return 0;
}
```

### Sample Output

```text
Enter your name: Ali
Welcome, Ali!
```

### Understand the Code

```cpp
string name;
```

creates a variable named `name` that can store text.

```cpp
cin >> name;
```

takes a **single word** from the user.

### Important

`cin >>` stops reading when it encounters a **space**.

For example, if the user enters:

```text
Muhammad Yasir
```

with:

```cpp
cin >> name;
```

only:

```text
Muhammad
```

will be stored in `name`.

To read a complete line containing spaces, we use `getline()`:

```cpp
getline(cin, name);
```

We will study `getline()` separately.

---

# 9. `cin` with Different Data Types

The type of variable determines what kind of input we expect.

| Data Type | Example Input | Example Variable |
| --------- | ------------- | ---------------- |
| `int`     | `25`          | `int age;`       |
| `float`   | `12.5`        | `float marks;`   |
| `double`  | `125.75`      | `double price;`  |
| `char`    | `A`           | `char grade;`    |
| `string`  | `Ali`         | `string name;`   |

Example:

```cpp
int age;
float marks;
char grade;
string name;

cin >> age;
cin >> marks;
cin >> grade;
cin >> name;
```

---

# 10. `cin` and `cout` Together

In most beginner programs, `cin` and `cout` are used together.

* `cout` → displays a message or result.
* `cin` → takes input from the user.

### Example

```cpp
#include <iostream>
using namespace std;

int main() {

    int age;

    cout << "Enter your age: ";
    cin >> age;

    cout << "Your age is: " << age;

    return 0;
}
```

Think of the process as:

```text
        User
         │
         │ enters data
         ▼
        cin
         │
         ▼
      Variable
         │
         ▼
        cout
         │
         ▼
       Screen
```

---

# 11. `std::cin`

We can also use `cin` without:

```cpp
using namespace std;
```

In that case, we write:

```cpp
std::cin >> age;
```

### Example

```cpp
#include <iostream>

int main() {

    int age;

    std::cout << "Enter your age: ";
    std::cin >> age;

    std::cout << "Your age is: " << age;

    return 0;
}
```

Here, `std::cin` means that `cin` belongs to the **standard (`std`) namespace**.

---

# Quick Review

| Component             | Purpose                        |
| --------------------- | ------------------------------ |
| `#include <iostream>` | Provides input/output features |
| `cin`                 | Takes input from the user      |
| `>>`                  | Extraction operator            |
| `cout`                | Displays output on the screen  |
| `<<`                  | Insertion operator             |
| `int`                 | Stores integer values          |
| `float`               | Stores decimal values          |
| `char`                | Stores a single character      |
| `string`              | Stores text                    |

---

# Key Points to Remember

### `cin`

Used to **take input from the user**.

```cpp
cin >> age;
```

### `>>`

Called the **extraction operator**.

```cpp
cin >> variable;
```

It extracts data from the input stream and stores it in the variable.

### Multiple Inputs

```cpp
cin >> a >> b >> c;
```

### `cout` vs `cin`

```text
cin  → Input  → User → Program
cout → Output → Program → Screen
```

---

# Practice Questions

### Practice 1 – Student Age

Write a C++ program that asks the user to enter their age and displays:

```text
Your age is: 20
```

### Practice 2 – Two Numbers

Write a C++ program that takes two integers from the user and displays their:

* Sum
* Difference
* Product

### Practice 3 – Student Marks

Write a C++ program that takes marks of three subjects and displays the total marks.

### Practice 4 – Rectangle

Write a C++ program that takes the length and width of a rectangle and calculates its area.

Formula:

```text
Area = Length × Width
```

### Practice 5 – Student Information

Write a C++ program that takes the following information from the user:

* Name
* Age
* Department
* Marks

Then display all the information using `cout`.

---

## Remember

```text
cin  → Takes input from the user
cout → Displays output on the screen

>>   → Extraction operator
<<   → Insertion operator
```

**`cin` is used for input, while `cout` is used for output.**
