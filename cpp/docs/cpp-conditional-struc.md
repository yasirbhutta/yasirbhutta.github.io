---
layout: page
title: "Programming in C++ – Conditional Structures"
description: "Learn C++"  
keywords: 
---

[ Download PDF](/downloads/cpp-conditional-struc.pdf)

## The if Statement

### Example #1

✅ **Question Statement**

**Write a C++ program that stores the value `2` in a variable `x` and checks whether the value is greater than 5, equal to 5, or less than 5.
Display the appropriate message based on the condition.**


```cpp
#include <iostream>
using namespace std;

int main() {
    // Store a number in the variable x
    int x = 2;

    // Check if x is greater than 5
    if (x > 5) {
        cout << "x is greater than 5." << endl;
    }
    // Check if x is equal to 5
    else if (x == 5) {
        cout << "x is equal to 5." << endl;
    }
    // If both above conditions are false, x must be less than 5
    else {
        cout << "x is less than 5." << endl;
    }

    return 0;
}
```

---

### ✅ **Example #2 Finding the Maximum of Three Numbers**

✅ **Question Statement**

*Write a C++ program that takes three numbers as input from the user and determines which of the three is the largest. Display the maximum number using an if-else.*

```cpp
#include <iostream>
using namespace std;

int main() {
    int a, b, c;

    // Input three numbers
    cout << "Enter first number: ";
    cin >> a;

    cout << "Enter second number: ";
    cin >> b;

    cout << "Enter third number: ";
    cin >> c;

    if (a >= b && a >= c) {
        cout << "The maximum number is: " << a << endl;
    }
    else if (b >= a && b >= c) {
        cout << "The maximum number is: " << b << endl;
    }
    else {
        cout << "The maximum number is: " << c << endl;
    }

    return 0;
}
```

---

## ✅ **Question Statement**

**Write a C++ program that asks the user to enter a test score (0–100).
Based on the score, display the corresponding grade using if-else statements:**

* **A** for 90–100
* **B** for 80–89
* **C** for 70–79
* **D** for 60–69
* **F** for below 60

---

## ✅ **C++ Program: Display Grade Based on Test Score**

```cpp
#include <iostream>
using namespace std;

int main() {
    int score;

    // Input test score from the user
    cout << "Enter your test score (0-100): ";
    cin >> score;

    // Determine and display grade
    if (score >= 90) {
        cout << "Your grade is: A" << endl;
    }
    else if (score >= 80) {
        cout << "Your grade is: B" << endl;
    }
    else if (score >= 70) {
        cout << "Your grade is: C" << endl;
    }
    else if (score >= 60) {
        cout << "Your grade is: D" << endl;
    }
    else {
        cout << "Your grade is: F" << endl;
    }

    return 0;
}
```

---



