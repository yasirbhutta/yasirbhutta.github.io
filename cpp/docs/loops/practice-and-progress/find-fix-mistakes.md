---
layout: page
title: "C++ Loops: Fix the Mistakes"
description: "Practice identifying and correcting common C++ beginner mistakes in syntax, variables, operators, and output with simple debugging exercises."
keywords: C++ debugging exercises, fix C++ mistakes, common C++ errors, beginner C++ practice, C++ syntax errors, variable mistakes in C++, output mistakes in C++, C++ programming exercises, learning C++ by debugging, C++ basics practice
---

## Instructions

For each question:

1. Read the problem statement.
2. Examine the given code carefully.
3. Identify the mistake or mistakes.
4. Explain why the code is incorrect.
5. Correct the code.
6. Compile and run the corrected program.
7. Explain how your correction solves the problem.

**Important:** Try to find the mistake yourself before checking the solution.


# Section 1: `while` Loop

## Question 1: Missing Semicolon

**Task:** Find and fix the mistake in the following program.

### Incorrect Code

```cpp
int i = 1

while (i <= 5)
{
    cout << i << endl;
    i++;
}
```

## Question 2: Incorrect Condition

**Task:** Find and fix the mistake so the program displays numbers from 1 to 5.

### Incorrect Code

```cpp
int i = 1;

while (i >= 5)
{
    cout << i << endl;
    i++;
}
```

## Question 3: Missing Update Statement

**Task:** Find and fix the mistake so the program displays numbers from 1 to 5 and terminates.

### Incorrect Code

```cpp
int i = 1;

while (i <= 5)
{
    cout << i << endl;
}
```

## Question 4: Incorrect Initialization

**Task:** Find and fix the mistake so the program displays numbers from 1 to 10.

### Incorrect Code

```cpp
int i = 0;

while (i <= 10)
{
    cout << i << endl;
    i++;
}
```

## Question 5: Incorrect Increment

**Task:** Find and fix the mistake so the program displays even numbers from 2 to 10.

### Incorrect Code

```cpp
int i = 2;

while (i <= 10)
{
    cout << i << endl;
    i = i + 1;
}
```

## Question 6: Incorrect Decrement

**Task:** Find and fix the mistake so the program displays numbers from 10 down to 1.

### Incorrect Code

```cpp
int i = 10;

while (i >= 1)
{
    cout << i << endl;
    i++;
}
```

## Question 7: Incorrect Comparison Operator

**Task:** Find and fix the mistake so the program displays numbers from 1 to 5.

### Incorrect Code

```cpp
int i = 1;

while (i < 5)
{
    cout << i << endl;
    i++;
}
```

## Question 8: Incorrect Loop Variable

**Task:** Find and fix the mistake so the program displays numbers from 1 to 5.

### Incorrect Code

```cpp
int i = 1;

while (i <= 5)
{
    cout << i << endl;
    j++;
}
```

## Question 9: Incorrect Sum Calculation

**Task:** Find and fix the mistake so the program calculates the sum of numbers from 1 to 5. The expected sum is `15`.

### Incorrect Code

```cpp
int i = 1;
int sum = 0;

while (i <= 5)
{
    sum = i;
    i++;
}

cout << "Sum = " << sum;
```

## Question 10: Incorrect Condition for Odd Numbers

**Task:** Find and fix the mistake so the program displays odd numbers from 1 to 9.

### Incorrect Code

```cpp
int i = 1;

while (i <= 9)
{
    cout << i << endl;
    i = i + 2;
}
```

## Question 11: Incorrect Input Condition

**Task:** Find and fix the mistake so the program continues asking for a number until the user enters `0`.

### Incorrect Code

```cpp
int num;

cout << "Enter a number: ";
cin >> num;

while (num == 0)
{
    cout << "Enter a number: ";
    cin >> num;
}
```

## Question 12: Incorrect Counter Update

**Task:** Find and fix the mistake so the program counts from 1 to 10 and displays the correct count.

### Incorrect Code

```cpp
int i = 1;
int count = 0;

while (i <= 10)
{
    count++;
    i++;
}

cout << "Count = " << i;
```

## Question 13: Incorrect Factorial Calculation

**Task:** Find and fix the mistake so the program calculates the factorial of 5. The expected result is `120`.

### Incorrect Code

```cpp
int n = 5;
int fact = 0;

while (n >= 1)
{
    fact = fact * n;
    n--;
}

cout << "Factorial = " << fact;
```

## Question 14: Incorrect Average Calculation

**Task:** Find and fix the mistake so the program calculates the average of the numbers 10, 20, and 30. The expected average is `20`.

### Incorrect Code

```cpp
int i = 1;
int sum = 0;

while (i <= 3)
{
    sum = sum + i * 10;
    i++;
}

double average = sum / 2;
cout << "Average = " << average;
```

## Question 15: Incorrect Digit Counting

**Task:** Find and fix the mistake so the program counts the digits in `12345`. The expected result is `5`.

### Incorrect Code

```cpp
int num = 12345;
int count = 0;

while (num > 0)
{
    num = num / 10;
    count = 1;
}

cout << "Digits = " << count;
```

## Question 16: Incorrect Reverse Number Logic

**Task:** Find and fix the mistake so the program reverses `1234` and displays `4321`.

### Incorrect Code

```cpp
int num = 1234;
int reverse = 0;

while (num > 0)
{
    int digit = num % 10;
    reverse = reverse + digit;
    num = num / 10;
}

cout << "Reverse = " << reverse;
```

## Question 17: Incorrect Multiple Condition

**Task:** Find and fix the mistake so the program displays numbers from 1 to 20 that are divisible by both 2 and 3.

### Incorrect Code

```cpp
int i = 1;

while (i <= 20)
{
    if (i % 2 == 0 && i % 3 == 0);
    {
        cout << i << endl;
    }

    i++;
}
```

## Question 18: Incorrect Prime Number Check

**Task:** Find and fix the mistake so the program correctly checks whether `7` is a prime number.

### Incorrect Code

```cpp
int num = 7;
int i = 2;
bool isPrime = true;

while (i < num)
{
    if (num % i == 0)
    {
        isPrime = false;
    }

    i++;
}

if (isPrime = true)
{
    cout << "Prime";
}
else
{
    cout << "Not Prime";
}
```

## Question 19: Incorrect Power Calculation

**Task:** Find and fix the mistake so the program calculates \\(2^5\\). The expected result is `32`.

### Incorrect Code

```cpp
int base = 2;
int exponent = 5;
int result = 0;
int i = 1;

while (i <= exponent)
{
    result = result * base;
    i++;
}

cout << "Result = " << result;
```

## Question 20: Incorrect Termination Condition

**Task:** Find and fix the mistake so the program displays numbers from 1 to 100 in steps of 10 and terminates correctly.

### Incorrect Code

```cpp
int i = 1;

while (i != 100)
{
    cout << i << endl;
    i = i + 10;
}
```
