# C++ Lecture 6: Loop Applications and Problem-Solving

Subject: Programming Fundamentals | Level: Beginner

This lecture applies `for`, `while`, and `do-while` loops to practical programming problems, including factorials, number sums, digit counting, and menu-driven programs.

## 1. Learning Objectives

By the end of this lecture, students will be able to:

- Calculate factorials using loops.
- Find the sum of a sequence of numbers.
- Count the digits of a number.
- Calculate the sum of digits.
- Reverse a number using a loop.
- Develop a simple menu-driven program.

## 2. Example 1: Calculate the Factorial of a Number

The factorial of a positive integer is the product of all positive integers from 1 up to that number.

For example:

\\[ 5! = 5 \times 4 \times 3 \times 2 \times 1 = 120 \\]

Remember that \\(0! = 1\\).

### C++ Code

```
#include <iostream>
using namespace std;

int main()
{
    int n;
    long long factorial = 1;

    cout << "Enter a number (0 to 20): ";
    cin >> n;

    if (n < 0 || n > 20)
    {
        cout << "Please enter a number from 0 to 20.";
    }
    else
    {
        for (int i = 1; i <= n; i++)
        {
            factorial = factorial * i;
        }

        cout << "Factorial = " << factorial;
    }

    return 0;
}
```

### Understand the Code

- `factorial = 1` initializes the product.
- The loop starts from 1 and continues up to `n`.
- `factorial = factorial * i` multiplies the running result by each number.
- The range check prevents negative input and values above 20, which exceed the range of a typical 64-bit signed `long long` factorial calculation.

For input `5`, the calculation is:

| `i` | Calculation | Factorial |
| --- | ----------- | --------- |
| 1   | 1 × 1       | 1         |
| 2   | 1 × 2       | 2         |
| 3   | 2 × 3       | 6         |
| 4   | 6 × 4       | 24        |
| 5   | 24 × 5      | 120       |

Output:

```
Enter a number (0 to 20): 5
Factorial = 120
```

### Modify the Code

1. Use a `while` loop instead of a `for` loop.
2. Display the multiplication steps as well as the answer.
3. Test the program with input `0`.

## 3. Example 2: Calculate the Sum of Digits

Suppose the user enters `456`. The sum of its digits is:

\\[ 4 + 5 + 6 = 15 \\]

### C++ Code

```
#include <iostream>
using namespace std;

int main()
{
    int n;
    int sum = 0;

    cout << "Enter a positive integer: ";
    cin >> n;

    if (n < 0)
    {
        cout << "Please enter a non-negative integer.";
    }
    else
    {
        while (n > 0)
        {
            int digit = n % 10;
            sum = sum + digit;
            n = n / 10;
        }

        cout << "Sum of digits = " << sum;
    }

    return 0;
}
```

### Understand the Code

Two operators are important:

- `n % 10` gives the last digit.
- `n / 10` removes the last digit when both operands are integers.

For example, if `n = 456`:

| Current `n` | `n % 10` | Sum | New `n` |
| ----------- | -------- | --- | ------- |
| 456         | 6        | 6   | 45      |
| 45          | 5        | 11  | 4       |
| 4           | 4        | 15  | 0       |

When `n` becomes 0, the loop stops.

Output:

```
Enter a positive integer: 456
Sum of digits = 15
```

### Modify the Code

1. Find the sum of digits of `1234`.
2. Count how many digits are even.
3. Count how many digits are odd.

## 4. Example 3: Count the Digits of a Number

For example, the number `58321` contains five digits.

### C++ Code

```
#include <iostream>
using namespace std;

int main()
{
    int n;
    int count = 0;

    cout << "Enter an integer: ";
    cin >> n;

    if (n < 0)
    {
        n = -n;
    }

    if (n == 0)
    {
        count = 1;
    }
    else
    {
        while (n > 0)
        {
            count++;
            n = n / 10;
        }
    }

    cout << "Number of digits = " << count;

    return 0;
}
```

### Understand the Code

- `count = 0` initializes the digit counter.
- `count++` increases the count by 1 for each digit.
- `n = n / 10` removes the last digit.
- Zero needs special handling because it has one digit, even though the loop condition `n > 0` would initially be false.

Sample output:

```
Enter an integer: 58321
Number of digits = 5
```

### Modify the Code

1. Test the program with `700`.
2. Test it with `0`.
3. Test it with `-12345`.

## 5. Example 4: Reverse a Number

A number is reversed by taking its last digit and adding it to a new number.

For example:

`1234` becomes `4321`.

### C++ Code

```
#include <iostream>
using namespace std;

int main()
{
    int n;
    int reverse = 0;

    cout << "Enter a positive integer: ";
    cin >> n;

    if (n < 0)
    {
        cout << "Please enter a non-negative integer.";
    }
    else
    {
        while (n > 0)
        {
            int digit = n % 10;
            reverse = reverse * 10 + digit;
            n = n / 10;
        }

        cout << "Reversed number = " << reverse;
    }

    return 0;
}
```

### Understand the Code

The key statement is:

```
reverse = reverse * 10 + digit;
```

Multiplying `reverse` by 10 shifts its existing digits one place to the left, making room for the new last digit.

For input `1234`:

| Digit extracted | Calculation  | New reverse |
| --------------- | ------------ | ----------- |
| 4               | 0 × 10 + 4   | 4           |
| 3               | 4 × 10 + 3   | 43          |
| 2               | 43 × 10 + 2  | 432         |
| 1               | 432 × 10 + 1 | 4321        |

Output:

```
Enter a positive integer: 1234
Reversed number = 4321
```

Note: Leading zeros disappear when a number is stored as an integer. For example, reversing `1200` produces `21`.

### Modify the Code

1. Reverse `56789`.
2. Test the program with `1005`.
3. Modify the program to check whether a number is a palindrome, such as `121`.

## 6. Example 5: Menu-Driven Calculator

A menu-driven program repeatedly displays options until the user chooses to exit.

### C++ Code

```
#include <iostream>
using namespace std;

int main()
{
    int choice;
    double a, b;

    do
    {
        cout << "\n--- Simple Calculator ---" << endl;
        cout << "1. Addition" << endl;
        cout << "2. Subtraction" << endl;
        cout << "3. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        if (choice == 1 || choice == 2)
        {
            cout << "Enter two numbers: ";
            cin >> a >> b;

            if (choice == 1)
            {
                cout << "Result = " << a + b << endl;
            }
            else
            {
                cout << "Result = " << a - b << endl;
            }
        }
        else if (choice == 3)
        {
            cout << "Calculator closed." << endl;
        }
        else
        {
            cout << "Invalid choice." << endl;
        }

    }
    while (choice != 3);

    return 0;
}
```

### Understand the Code

- The `do-while` loop displays the menu at least once.
- `choice` stores the selected option.
- The `if-else` statements determine which operation to perform.
- The menu repeats until the user enters `3`.

### Modify the Code

1. Add multiplication as option 3 and move Exit to option 4.
2. Add division as another operation.
3. Display a warning if the user tries to divide by zero.

## 7. Coding Exercises

Solve the following tasks independently.

### Level 1 — Basic

1\. Print all numbers from 1 to 100.

2\. Calculate the sum of numbers from 1 to n.

3\. Print the multiplication table of a number.

4\. Count the digits of an integer.

5\. Calculate the sum of the digits of an integer.

6\. Reverse an integer using a loop.

7\. Calculate the factorial of a number.

8\. Check whether a number is a palindrome.

9\. Display all even numbers between two user-entered limits.

10\. Create a menu-driven calculator using do-while.

0 of 10 completed

## 8. Quick Revision Quiz

1\. What does \`n % 10\` return for n = 456?

45

6

456



2\. What is the value of 5!?

25

60

120



3\. Which loop is suitable for a menu that should appear at least once?

do-while

if only

No loop



4\. What does integer division \`456 / 10\` produce in C++?

45.6

45

46



Check Answers

## 9. Lesson Summary

- Loops automate repeated calculations.
- Factorial problems use multiplication and a running product.
- Digit problems commonly use `% 10` and `/ 10`.
- Nested loops handle repeated rows and columns.
- `break` stops a loop, while `continue` skips an iteration.
- `do-while` is useful for menus that should appear at least once.

Suggested next lecture: Choosing the right loop (`for` vs `while` vs `do-while`) and solving mixed loop problems with trace tables.