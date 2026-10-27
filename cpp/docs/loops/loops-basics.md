---
layout: page
title: "C++ Loops: Introduction, Uses, and Beginner Examples"
description: "Learn what loops are in C++, why programmers use them, and how repetition, conditions, and stopping rules work through beginner-friendly examples."
keywords: C++ loops, introduction to loops, loop programming basics, why use loops in C++, repetition in programming, loop conditions, beginner C++ examples, programming fundamentals, C++ for university students, repetitive tasks in code
---

## Learning Objectives

By the end of this lesson, students will be able to:

1. Explain what a loop is.
2. Understand why loops are used in programming.
3. Identify repetitive tasks in real-life situations.
4. Compare code written with and without loops.
5. Understand the basic idea of repetition, a condition, and stopping a loop.

## 1. What Is a Loop?

A loop is a programming structure that repeats a block of code multiple times.

In real life, we often repeat the same task. For example:

- A teacher takes attendance for 50 students.
- A student practises a question 10 times.
- A university system sends notifications to many students.
- A program displays a message 5 times.

Instead of writing the same instructions repeatedly, we can use a loop.

Simple definition: A loop allows us to execute the same instructions repeatedly without writing them again and again.

## 2. Why Do We Need Loops?

Suppose we want to display a message five times.

Without a loop:

```cpp

#include <iostream>
using namespace std;

int main()
{
    cout << "Welcome to Ghazi University!" << endl;
    cout << "Welcome to Ghazi University!" << endl;
    cout << "Welcome to Ghazi University!" << endl;
    cout << "Welcome to Ghazi University!" << endl;
    cout << "Welcome to Ghazi University!" << endl;

    return 0;
}

```

Output:

```
Welcome to Ghazi University!
Welcome to Ghazi University!
Welcome to Ghazi University!
Welcome to Ghazi University!
Welcome to Ghazi University!
```

Problem: We have written the same instruction five times. What if we need to display it 100 times?

Writing 100 separate `cout` statements would be unnecessary and difficult to maintain.

We can solve this problem using a loop.

## 3. Our First Loop Program

We will use a `while` loop to display the same message five times.

```cpp

#include <iostream>
using namespace std;

int main()
{
    int i = 1;

    while (i <= 5)
    {
        cout << "Welcome to Ghazi University!" << endl;
        i++;
    }

    return 0;
}

```

Output:

```
Welcome to Ghazi University!
Welcome to Ghazi University!
Welcome to Ghazi University!
Welcome to Ghazi University!
Welcome to Ghazi University!
```

The output is the same, but the code is shorter and easier to manage.

## 4. Understand the Code Step by Step

Let's understand the program in simple language.

### Step 1: Create a variable

```cpp
int i = 1;
```

- `int` means the variable stores an integer.
- `i` is the variable name.
- `1` is its initial value.

Think of `i` as a counter that keeps track of how many times we have repeated the task.

### Step 2: Check the condition

```cpp
while (i <= 5)
```

The condition checks whether `i` is less than or equal to 5.

- If the condition is true, the loop body executes.
- If the condition is false, the loop stops.

### Step 3: Execute the instruction

```cpp
cout << "Welcome to Ghazi University!" << endl;
```

This statement displays the message.

### Step 4: Update the counter

```cpp
i++;
```

This increases `i` by 1.

For example:

```cpp
i++;
```

is equivalent to:

```cpp
i = i + 1;
```

Without this update, the condition would remain true indefinitely in this example, creating an infinite loop.

## 5. Trace Table: How Does the Loop Work?

A trace table helps us understand how a program executes step by step.

| Iteration | Value of `i` | Condition `i <= 5` | Action          |
| --------- | ------------ | ------------------ | --------------- |
| 1         | 1            | True               | Display message |
| 2         | 2            | True               | Display message |
| 3         | 3            | True               | Display message |
| 4         | 4            | True               | Display message |
| 5         | 5            | True               | Display message |
| End check | 6            | False              | Stop the loop   |

Notice that the loop checks the condition again after each update. When `i` becomes **6**, the condition is `false`, so the program exits the loop.

## 6. Understand Loops Through a Simple Analogy

Imagine placing five books on a table, one by one.

[Closed book on desk by blackboard](https://images.openai.com/static-rsc-4/Q1rE4qNHPpftN5H5wcbPVpihHSqJWjQk-bovs4qoHd-5eVp8-hvpYoQLpYsDn1SzQVQJUELZBa5jMjSbIiOjJHYKGdCVutVn8fxMqaPy4u4TDyf5_mJhd7dHL8pOi3MN9JevPJAXtcol-nWcT_EtpnJxD1fcj_HQMHnabqobpuzFn8JX0jOsoBvwFHSdlMDa?purpose=inline)

1. Initialization

Start counting from book number 1.

[Books on the desk](https://images.openai.com/static-rsc-4/wMKk2MGC1Dwam05YJj6UtGluCMpAadNSDSIIPakgvGSXgKuBqkhhVVxHXHwqhfJhRxLEhehhpxpAShWYNZJk31MP4mVUNEQac5bHMcFmarauG8DnE5S1X9Pr3IB9MWR6HRHZ-plRj5CxbM1JbB5a9Km1qJC_ozL5TK3a_KqB9Hk1gEJNp0AC04Uu-gOIAEi_?purpose=inline)

2. Condition

Ask: Have we placed five books or fewer?

[a diligent boy sits at a Desk and puts books on stacks.](https://images.openai.com/static-rsc-4/2avBCyQGROrskvRD89P8dbo_YqyWPADCaGuiOlWeudu1ZsLDSnY2Msbuz91tNnn1zvfbrsDJKViChlIFtzkgl9OZjxbbUDQXPK7-PHQXNBwwG2S0r6ebyH5fOEguhV-aghBMyNwVRjKNMHIq2UEg8GTWnaTW05VQvMec5DmzcIgW0Ff_CCV0scCaTVvM9Ia2?purpose=inline)

3. Repetition and update

Place another book and increase the count.

[Business Research Methods – Online Course – FutureLearn](https://images.openai.com/static-rsc-4/TJwS5_Pnf5B00BC59WsOk34BkamjBkJayxvkg8hDbs_eosoHCK72KmDCV11jZvUcrFNR0QvD2pNPZpex8NKCR88bDsd_eWSbDyeiv6Ddg-PmD7VNUSbLurp87NJdkb1WqNd9fGYwwGCEY9gE7H3RCEa5YuxL9y3VJOe7UeqGtGw?purpose=inline)

4. Stop

Stop when five books have been placed.

The same idea applies to programming: check, execute, update, and repeat until the condition becomes false.
