---
layout: page
title: "C++ do-while Loop Solutions and Examples"
description: "Explore solved C++ do-while loop exercises, including a menu-driven calculator, algorithm analysis, dry runs, complete code, and sample output."
keywords: C++ do-while loop solutions, C++ do-while examples, do-while loop exercises, C++ loop solutions, menu-driven calculator C++, switch statement C++, LOOP-COD-019
---

# Contents

- [LOOP-COD-019: Simple Calculator Menu](#loop-cod-019)

---

<a id="loop-cod-019"></a>

## LOOP-COD-019: Simple Calculator Menu

## 1. Problem Analysis

The task is to develop a menu-driven calculator using a `do-while` loop.

The program should repeatedly display a menu and allow the user to perform addition or subtraction until the user selects Exit.

**Input:**

- User's menu choice (`1`, `2`, or `3`).
- Two numbers for addition or subtraction.

**Processing:**

- If the choice is `1`, add the two numbers.
- If the choice is `2`, subtract the second number from the first.
- If the choice is `3`, terminate the loop.
- For any other choice, display an error message.

**Output:**

- Sum of two numbers.
- Difference between two numbers.
- Error message for an invalid choice.
- `Calculator closed.` when the user exits.

**Programming concepts required:**

- `do-while` loop
- `switch` statement
- Variables
- User input and output
- Arithmetic operators

## 2. Algorithm / Pseudocode

1. Start the program.
2. Declare variables for the menu choice and two numbers.
3. Display the calculator menu.
4. Ask the user to enter a choice.
5. Check the user's choice:
   - If choice is `1`:
     - Ask for two numbers.
     - Calculate their sum.
     - Display the sum.
   - If choice is `2`:
     - Ask for two numbers.
     - Calculate their difference.
     - Display the difference.
   - If choice is `3`:
     - Display `Calculator closed.`
   - Otherwise:
     - Display an invalid choice message.
6. Repeat the menu while the choice is not `3`.
7. End the program.

Pseudocode

```text
START

DO
    DISPLAY calculator menu
    INPUT choice

    SWITCH choice
        CASE 1:
            INPUT num1, num2
            sum = num1 + num2
            DISPLAY sum
            BREAK

        CASE 2:
            INPUT num1, num2
            difference = num1 - num2
            DISPLAY difference
            BREAK

        CASE 3:
            DISPLAY "Calculator closed."
            BREAK

        DEFAULT:
            DISPLAY "Invalid choice."

WHILE choice is not equal to 3

STOP
```

## 3. Dry Run Table

A dry run helps us understand how the program executes with the given sample input.

Given input:

```
1
10 5
2
10 5
3
```

| Step | Choice | Number 1 | Number 2 | Operation / Action | Result             |
| ---- | ------ | -------- | -------- | ------------------ | ------------------ |
| 1    | 1      | 10       | 5        | Addition           | 15                 |
| 2    | 2      | 10       | 5        | Subtraction        | 5                  |
| 3    | 3      | —        | —        | Exit               | Calculator closed. |

Understanding the loop:

- First iteration: The user selects Addition. The program calculates `10 + 5 = 15`.
- Second iteration: The user selects Subtraction. The program calculates `10 - 5 = 5`.
- Third iteration: The user selects Exit. The program displays the closing message.
- The loop terminates because the choice is `3`.

## 4. Complete C++ Code

```cpp
#include <iostream>
using namespace std;

int main()
{
    int choice;
    float num1, num2;

    do
    {
        cout << "\n===== Simple Calculator =====" << endl;
        cout << "1. Addition" << endl;
        cout << "2. Subtraction" << endl;
        cout << "3. Exit" << endl;

        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice)
        {
            case 1:
                cout << "Enter two numbers: ";
                cin >> num1 >> num2;

                cout << "Sum = " << num1 + num2 << endl;
                break;

            case 2:
                cout << "Enter two numbers: ";
                cin >> num1 >> num2;

                cout << "Difference = " << num1 - num2 << endl;
                break;

            case 3:
                cout << "Calculator closed." << endl;
                break;

            default:
                cout << "Invalid choice! Please try again." << endl;
        }

    } while (choice != 3);

    return 0;
}
```

## 5. Code Explanation

Let's understand the important parts of the program.

### A. Declare variables

```cpp
int choice;
float num1, num2;
```

- `choice` stores the menu option entered by the user.
- `num1` stores the first number.
- `num2` stores the second number.
- `float` allows the calculator to work with decimal numbers.

### B. The do-while loop

```cpp
do
{
    // Menu and calculator operations

} while (choice != 3);
```

A `do-while` loop executes its body at least once before checking the condition.

Here, `choice != 3` means the loop continues as long as the user does not select Exit.

When the user enters `3`, the condition becomes false, and the loop terminates.

### C. Display the menu

```cpp
cout << "\n===== Simple Calculator =====" << endl;
cout << "1. Addition" << endl;
cout << "2. Subtraction" << endl;
cout << "3. Exit" << endl;
```

These statements display the calculator menu each time the loop executes.

### D. Get the user's choice

```cpp
cout << "Enter your choice: ";
cin >> choice;
```

The program asks the user to select an option and stores it in the `choice` variable.

### E. Use the switch statement

```cpp
switch (choice)
```

The `switch` statement checks the selected menu option and executes the matching case.

- `case 1`: Performs addition.
- `case 2`: Performs subtraction.
- `case 3`: Displays the closing message.
- `default`: Handles invalid choices.

### F. Perform addition

```cpp
cin >> num1 >> num2;
cout << "Sum = " << num1 + num2 << endl;
```

The program takes two numbers and adds them using the `+` operator.

### G. Perform subtraction

```cpp
cin >> num1 >> num2;
cout << "Difference = " << num1 - num2 << endl;
```

The program subtracts the second number from the first using the `-` operator.

### H. Understand the break statement

```
break;
```

The `break` statement terminates the current `switch` case. It does not terminate the `do-while` loop.

The loop continues until the user selects `3`.

## 6. Sample Output

```
===== Simple Calculator =====
1. Addition
2. Subtraction
3. Exit
Enter your choice: 1
Enter two numbers: 10 5
Sum = 15

===== Simple Calculator =====
1. Addition
2. Subtraction
3. Exit
Enter your choice: 2
Enter two numbers: 10 5
Difference = 5

===== Simple Calculator =====
1. Addition
2. Subtraction
3. Exit
Enter your choice: 3
Calculator closed.
```

## 7. Modification Task

Now modify the existing calculator program to practise independently.

### Task 1: Add Multiplication

- Add a new menu option: `3. Multiplication`.
- If the user selects `3`, ask for two numbers.
- Multiply the numbers and display the result.

### Task 2: Update the Exit Option

- Change the Exit option from `3` to `4`.
- Update the loop condition accordingly.
- Display `Calculator closed.` when the user selects `4`.

### Task 3: Add Division

- Add a new menu option: `4. Division`.
- Ask for two numbers.
- Display their division result.
- Check whether the second number is zero before performing division.

**Challenge:** Update the menu and program so that all four arithmetic operations work correctly, and the user can continue calculating until selecting Exit.

**Key Learning Point:** The `do-while` loop is useful for menu-driven programs because it displays the menu at least once and repeats it until the user chooses to exit.