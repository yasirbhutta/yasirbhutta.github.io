---
layout: page
title: "C++ Loop Structure Review Questions"
description: "Review C++ loop structures with questions about while loops, loop conditions, counters, increments, repeated statements, and infinite loops."
keywords: C++ loop review questions, C++ loops questions, C++ while loop questions, loop structures in C++, C++ iteration review, loop conditions, loop counters, loop increment, infinite loops in C++, C++ programming practice
---

# 1. Basics Loop

1. What is a loop in C++?
2. Why do we use loops instead of writing the same statement repeatedly?

# Section 1: `while` Loop

1. What is a `while` loop in C++? Explain its purpose with an example.
2. What is the syntax of a `while` loop?
3. How does a `while` loop work? Explain its execution step by step.
4. What is the difference between a `while` loop and an `if` statement?
5. What is an infinite loop? Explain why it occurs in a `while` loop and write a C++ example.
6. What happens if the condition of a `while` loop is false at the beginning?
7. Why is initialization important in a `while` loop?
8. What happens if the loop control variable is not updated?
9. How can you use a `while` loop to repeatedly take input until the user enters `0`?
10. What is the difference between a `counter-controlled loop` and a `sentinel-controlled loop`? Give an example of each.

**Answer:** 

## 1. Counter-Controlled Loop

A counter-controlled loop repeats a fixed number of times. A counter variable keeps track of the number of repetitions.

Example: Display numbers from 1 to 5

```cpp
int i = 1;

while (i <= 5)
{
    cout << i << endl;
    i++;
}
```

How it works:

- Initialization: `i = 1`
- Condition: `i <= 5`
- Update: `i++`
- The loop stops when `i` becomes 6.

Output:

```
1
2
3
4
5
```

## 2. Sentinel-Controlled Loop

A sentinel-controlled loop repeats until the user enters a special value called a sentinel value. This value signals the loop to stop.

Example: Accept numbers until the user enters 0

```cpp
int num;

cout << "Enter a number (0 to stop): ";
cin >> num;

while (num != 0)
{
    cout << "You entered: " << num << endl;

    cout << "Enter a number (0 to stop): ";
    cin >> num;
}
```

Sample Output:

```
Enter a number (0 to stop): 10
You entered: 10
Enter a number (0 to stop): 25
You entered: 25
Enter a number (0 to stop): 7
You entered: 7
Enter a number (0 to stop): 0
```

Here, `0` is the sentinel value. The loop stops when the user enters `0`.

## 3. Key Differences

| Feature            | Counter-Controlled Loop  | Sentinel-Controlled Loop                 |
| ------------------ | ------------------------ | ---------------------------------------- |
| Repetitions        | Usually known in advance | Depend on user input or data             |
| Control            | Counter variable         | Sentinel value                           |
| Stopping condition | Counter reaches a limit  | Sentinel value is entered or encountered |
| Example            | Print numbers 1 to 10    | Accept numbers until 0 is entered        |

Remember:

- Counter-controlled: Repeat a known number of times.
- Sentinel-controlled: Repeat until a special stopping value is received.

11. Can a `while` loop execute zero times? Explain with an example.
12. Identify three common mistakes students make when writing `while` loops and explain how to correct them.

# Section 2: `do-while` Loop

1. What is the difference between a `while` loop and a `do-while` loop?
