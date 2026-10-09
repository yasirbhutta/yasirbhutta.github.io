---
layout: page
title: "Standard Output in C++ Using `cout`"
description: "Learn how to use C++ cout for standard output with clear examples. Understand cout syntax, printing text, variables, and formatted output in beginner-friendly C++ programs."
keywords: C++ cout, cout in C++, standard output in C++, C++ output, cout syntax, C++ print, C++ iostream, C++ beginner tutorial, C++ examples, C++ program output, learn C++ output, display output in C++
---

## 1. What is Standard Output?

In C++, **standard output** is used to display information on the computer screen.

The standard output object in C++ is:

```cpp
cout
```

`cout` is provided by the **`<iostream>`** library.

We commonly use `cout` to display:

* Text
* Numbers
* Variables
* Calculation results
* Multiple values

---

# 2. Basic Syntax of `cout`

The basic syntax is:

```cpp
cout << "Your message here";
```

### Complete Program

```cpp
#include <iostream>
using namespace std;

int main() {

    cout << "Hello World!";

    return 0;
}
```

### Output

```text
Hello World!
```

---

# 3. Understanding the Code

### `#include <iostream>`

```cpp
#include <iostream>
```

Includes the **input/output stream library**.

It provides objects such as `cout` and `cin`.

---

### `cout`

```cpp
cout
```

`cout` is the **standard output object** used to display information on the screen.

---

### `<<` Insertion Operator

```cpp
cout << "Hello World!";
```

The `<<` symbol is called the **insertion operator**[1].

It sends the data on its right side to `cout`, which displays it on the screen.

Think of it as:

```text
Data → cout → Screen
```

---

# 4. Printing Text

We can use `cout` to display text.

### Example

```cpp
cout << "Hello World!";
```

### Output

```text
Hello World!
```

Text must be written inside **double quotation marks (`" "`)**.

---

# 5. Printing Numbers

`cout` can also display numbers.

### Example

```cpp
cout << 100;
```

### Output

```text
100
```

We do not use quotation marks when displaying a number.

Compare:

```cpp
cout << 100;
```

Output:

```text
100
```

Whereas:

```cpp
cout << "100";
```

also displays:

```text
100
```

However, the first is a **number**, while the second is **text**.

---

# 6. Printing Variables

`cout` can be used to display the value stored in a variable.

### Example

```cpp
int a = 10;

cout << a;
```

### Output

```text
10
```

We do not put the variable name inside quotation marks.

### Example with Text

```cpp
int a = 10;

cout << "Value of a is: " << a;
```

### Output

```text
Value of a is: 10
```

### Understand the Code

```cpp
cout << "Value of a is: " << a;
```

There are two things being displayed:

1. `"Value of a is: "` → text
2. `a` → value stored in the variable

The insertion operator `<<` connects them.

---

# 7. Printing Multiple Values

We can use multiple `<<` operators in one `cout` statement.

### Example

```cpp
int age = 20;
float marks = 85.5;

cout << "Age: " << age << endl;
cout << "Marks: " << marks;
```

### Output

```text
Age: 20
Marks: 85.5
```

---

# 8. Printing Multiple Lines

We can use `endl` to move the cursor to the next line.

### Example

```cpp
cout << "Line 1" << endl;
cout << "Line 2";
```

### Output

```text
Line 1
Line 2
```

We can also use the newline escape sequence `\n`:

```cpp
cout << "Line 1\n";
cout << "Line 2";
```

Both `endl` and `\n` can be used to move to the next line.

---

# 9. `cout` with Input and Calculation

`cout` is often used together with `cin`.

* `cin` → takes input from the user.
* `cout` → displays output to the user.

Think of the process as:

```text
User Input → cin → Variables → Calculation → cout → Screen
```

---

# Example 1: Add Two Numbers

### Question

Write a C++ program that takes two floating-point numbers from the user, adds them, and displays the sum.

### Program

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

### Sample Output

```text
Enter first number: 12.5
Enter second number: 7.5
The sum is: 20
```

### What This Program Does

1. Declares three `float` variables: `num1`, `num2`, and `sum`.
2. Takes the first number from the user.
3. Takes the second number from the user.
4. Adds the two numbers.
5. Stores the result in `sum`.
6. Uses `cout` to display the result.

### Important Line

```cpp
cout << "The sum is: " << sum << endl;
```

Here:

* `"The sum is: "` → displays text.
* `sum` → displays the calculated value.
* `endl` → moves the cursor to the next line.

---

# Example 2: Calculate the Area of a Rectangle

### Question

Write a C++ program that takes the height and width of a rectangle from the user, calculates its area using:

```text
Area = Height × Width
```

and displays the result.

### Program

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

### Sample Output

```text
Enter height of the rectangle: 5.5
Enter width of the rectangle: 4
The area of the rectangle is: 22
```

### What This Program Does

1. Declares `height`, `width`, and `area` as `float` variables.
2. Takes the height from the user.
3. Takes the width from the user.
4. Calculates the area:

```cpp
area = height * width;
```

5. Displays the calculated area using `cout`.

---

# 10. Using `std::cout`

We can also use `cout` without writing:

```cpp
using namespace std;
```

In that case, we write:

```cpp
std::cout << "Hello World!";
```

### Example

```cpp
#include <iostream>

int main() {

    std::cout << "Hello World!";

    return 0;
}
```

Here, `std::cout` means that `cout` belongs to the **standard (`std`) namespace**.

For beginners, we commonly use:

```cpp
using namespace std;
```

so that we can simply write:

```cpp
cout
```

instead of:

```cpp
std::cout
```

---

# 11. Quick Review

| Component             | Purpose                                  |
| --------------------- | ---------------------------------------- |
| `#include <iostream>` | Provides input/output features           |
| `cout`                | Displays output on the screen            |
| `<<`                  | Insertion operator; sends data to `cout` |
| `endl`                | Moves the cursor to the next line        |
| `\n`                  | Moves the cursor to the next line        |
| `cin`                 | Takes input from the user                |
| `std::cout`           | `cout` from the standard namespace       |

---

# Key Points to Remember

### `cout`

Used to **display output**.

```cpp
cout << "Hello";
```

### `<<`

Called the **insertion operator**.

```cpp
cout << value;
```

### Text

Write text inside double quotation marks:

```cpp
cout << "Hello World!";
```

### Variable

Do not use quotation marks around a variable:

```cpp
int age = 20;

cout << age;
```

### Text + Variable

Use multiple `<<` operators:

```cpp
cout << "Age: " << age;
```

### New Line

Use either:

```cpp
cout << "Hello" << endl;
```

or:

```cpp
cout << "Hello\n";
```

---

## Coding Exercises

### Practice 1 – Student Information

Write a C++ program that takes the student's **name, age, and marks** as input and displays them using `cout`.

### Practice 2 – Calculate Total

Write a C++ program that takes the prices of three items from the user, calculates the total, and displays the result.

### Practice 3 – Calculate Rectangle Perimeter

Write a C++ program that takes the length and width of a rectangle and calculates:

```text
Perimeter = 2 × (Length + Width)
```

Display the result using `cout`.

### Practice 4 – Calculate Average

Write a C++ program that takes marks of three subjects, calculates the average, and displays the result.

---

## Remember

```text
cin  → Input  → User → Program
cout → Output → Program → Screen
```

**`cin` takes data from the user, while `cout` displays data on t**

## References and Bibliography

- [1]“operator overloading - cppreference.com,” Cppreference.com, 2026. https://en.cppreference.com/cpp/language/operators (accessed Oct. 06, 2026).