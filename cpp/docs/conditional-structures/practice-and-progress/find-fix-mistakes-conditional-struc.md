---
layout: page
title: "C++ Conditional Structures: Fix the Mistake"
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


# Section 1: `if` Statement

## Question 1: Missing Semicolon

**Task:** Find and fix the mistake in the following program.

### Incorrect Code

```cpp
int x = 10;

if (x > 5);
{
    cout << "Greater";
}
```

---

## Question 2:

**Task:** Find and fix the mistake in the following program.

### Incorrect Code

```cpp
int x = 10;

if x > 5
{
    cout << "Greater";
}
```

---

## Question 1:

**Task:** Find and fix the mistake in the following program.

### Incorrect Code

```cpp
int marks = 60;

if (marks >= 50)
{
    cout << "Pass";
}
else (marks < 50)
{
    cout << "Fail";
}
```

## Question 1:

**Task:** The program should print Eligible for people aged 18 or older.

### Incorrect Code

```cpp
int age = 16;

if (age >= 18)
{
    cout << "Eligible";
}
else
{
    cout << "Not Eligible";
}
cout << "Eligible";
```

---

## Question 1:

**Task:** The program should print Pass when marks are 50 or above. Identify the mistake.


### Incorrect Code

```cpp
int marks = 50;

if (marks > 50)
{
    cout << "Pass";
}
else
{
    cout << "Fail";
}
```

---

## Question 1:

**Task:**  The program should print the greater number. What is the mistake?

### Incorrect Code

```cpp
int a = 10;
int b = 20;

if (a > b)
{
    cout << b;
}
else
{
    cout << a;
}
```

---

## Question 1:

**Task:** The program should print `Even` for an even number. What is the mistake?

### Incorrect Code

```cpp
int n = 7;

if (n % 2 == 1)
{
    cout << "Even";
}
else
{
    cout << "Odd";
}
```

---
