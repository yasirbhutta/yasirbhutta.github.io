---
layout: page
title: "C++ Loop Applications: Factorials, Digits, and Menus"
description: "Apply C++ loops to solve beginner problems: calculate factorials and sums, count or reverse digits, and build a simple menu-driven program with examples."
keywords: C++ loop applications, factorial program in C++, sum of digits in C++, reverse a number in C++, count digits using loops, menu-driven program in C++, C++ loop examples, for loop applications, while loop exercises, programming fundamentals students
---

---

## for loop

### **Syntax of a for loop:**

```cpp
for (initialization; condition; update) {
    // code to execute in each iteration
}
```

* **Initialization**: Runs **once** at the start of the loop. Usually used to declare a loop variable.
* **Condition**: Checked **before each iteration**. If true, the loop continues; if false, the loop stops.
* **Update**: Runs **after each iteration**. Usually increments/decrements the loop variable.

---

### **Example 1: Print numbers 1 to 5**

```cpp
#include <iostream>
using namespace std;

int main() {
    for (int i = 1; i <= 5; i++) { // i starts at 1, loop until i <= 5, i increments by 1
        cout << i << " ";
    }
    return 0;
}
```

**Output:**

```
1 2 3 4 5
```

✅ **Explanation:**

* `int i = 1` → start counting from 1
* `i <= 5` → stop after 5
* `i++` → increment i by 1 each time

---

### **Example 2: Print even numbers from 2 to 10**

```cpp
#include <iostream>
using namespace std;

int main() {
    for (int i = 2; i <= 10; i += 2) { // i increases by 2 each time
        cout << i << " ";
    }
    return 0;
}
```

**Output:**

```
2 4 6 8 10
```

✅ **Explanation:**

* `i += 2` means **add 2 to i each time**, so we get even numbers.

---

### **Example 3: Sum of first 10 natural numbers**

```cpp
#include <iostream>
using namespace std;

int main() {
    int sum = 0;
    for (int i = 1; i <= 10; i++) {
        sum += i; // sum = sum + i
    }
    cout << "Sum = " << sum;
    return 0;
}
```

**Output:**

```
Sum = 55
```

✅ **Explanation:**

* `sum += i` adds each number to the total sum.
* After the loop finishes, `sum` contains the total.

---

### **Key Points for Beginners**

1. A `for` loop is great for **known number of iterations**.
2. You can control the start, end, and increment.
3. The loop can run **forward** (i++) or **backward** (i--).

---

### **Example 4: Basic Multiplication Table**

**Question:**
Write a C++ program that asks the user to enter a number and then displays its multiplication table from 1 to 10 using a **for loop**.

**Example:**

* If the user enters `7`, the program should display:

```
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
...
7 x 10 = 70
```

**Requirements:**

1. Use `cin` to take input from the user.
2. Use a `for` loop to generate the multiplication table.
3. Display the results in a readable format.

---


```cpp
#include <iostream>
using namespace std;

int main() {
    int number;

    // Ask the user for the number
    cout << "Enter a number to display its multiplication table: ";
    cin >> number;

    // Loop from 1 to 10
    for (int i = 1; i <= 10; i++) {
        cout << number << " x " << i << " = " << number * i << endl;
    }

    return 0;
}
```

### ✅ How it works:

1. `cin >> number;` → User inputs the number for which they want the table.
2. `for (int i = 1; i <= 10; i++)` → Loop runs from 1 to 10.
3. Inside the loop, `number * i` calculates each multiplication.
4. `cout` prints the result in a readable format.

**Example Output (if user enters 5):**

```
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50
```

---

### **Example 5: Print Even Numbers from 1 to N**

**Question:**
Write a C++ program that asks the user to enter a positive number `N` and then prints **all even numbers from 1 to N** using a **for loop**.

**Example:**

* Input: `10`
* Output:

```
Even numbers from 1 to 10 are: 2 4 6 8 10
```

**Requirements:**

1. Use `cin` to take input from the user.
2. Use a `for` loop to iterate from 1 to `N`.
3. Use an `if` statement to check if a number is even.
4. Display the even numbers in a single line, separated by spaces.

---

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;

    // Ask the user for a number
    cout << "Enter a positive number: ";
    cin >> n;

    cout << "Even numbers from 1 to " << n << " are: ";

    // For loop to print even numbers
    for (int i = 1; i <= n; i++) {
        if (i % 2 == 0) {  // Check if number is even
            cout << i << " ";
        }
    }

    cout << endl;
    return 0;
}
```

---

### ✅ **How it works:**

1. User inputs a number `n`.
2. Loop `for (int i = 1; i <= n; i++)` runs from 1 to `n`.
3. `if (i % 2 == 0)` checks if the number is even.
4. Prints only even numbers.

---

### **Example Output:**

```
Enter a positive number: 10
Even numbers from 1 to 10 are: 2 4 6 8 10
```

---

### **Example 6: Print a Simple Star Pattern**

---

**Question:**
Write a C++ program that asks the user to enter a positive number `N` and then prints a **right-angled triangle star pattern** with `N` rows using **nested for loops**.

**Example:**

* Input: `5`
* Output:

```
*
**
***
****
*****
```

**Requirements:**

1. Use `cin` to take input from the user.
2. Use a **nested for loop**:

   * Outer loop to control the rows.
   * Inner loop to print stars in each row.
3. Each row should have an increasing number of stars, starting from 1 star in the first row.

---

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;

    // Ask the user for the number of rows
    cout << "Enter the number of rows: ";
    cin >> n;

    // Outer loop for each row
    for (int i = 1; i <= n; i++) {
        // Inner loop to print stars in each row
        for (int j = 1; j <= i; j++) {
            cout << "*";
        }
        cout << endl; // Move to next row
    }

    return 0;
}
```

---

### ✅ **How it works:**

1. User inputs the number of rows `n`.
2. Outer loop `for (int i = 1; i <= n; i++)` → Controls the rows.
3. Inner loop `for (int j = 1; j <= i; j++)` → Prints stars in each row.
4. Each row has an increasing number of stars.

---

### **Example Output:**

```
Enter the number of rows: 5
*
**
***
****
*****
```

---








