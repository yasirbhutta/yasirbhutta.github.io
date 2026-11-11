---
layout: page
title: "C++ Loop Structure Review Questions"
description: "Review C++ loop structures with questions about while loops, loop conditions, counters, increments, repeated statements, and infinite loops."
keywords: C++ loop review questions, C++ loops questions, C++ while loop questions, loop structures in C++, C++ iteration review, loop conditions, loop counters, loop increment, infinite loops in C++, C++ programming practice
---

## Section 1: `while` Loop

1. What is a loop in C++?
2. Why do we use loops instead of writing the same statement repeatedly?
2. What is a `while` loop in C++? Explain its purpose with an example.
3. What is the syntax of a `while` loop?
4. How does a `while` loop work? Explain its execution step by step.
5. What is the difference between a `while` loop and an `if` statement?
6. What is an infinite loop? Explain why it occurs in a `while` loop and write a C++ example.
7. What happens if the condition of a `while` loop is false at the beginning?
8. Why is initialization important in a `while` loop?
9. What happens if the loop control variable is not updated?
10. How can you use a `while` loop to repeatedly take input until the user enters `0`?
11. What is the difference between a `counter-controlled loop` and a `sentinel-controlled loop`? Give an example of each.
12. Can a `while` loop execute zero times? Explain with an example.
13. Identify three common mistakes students make when writing `while` loops and explain how to correct them.

## Section 2: `do-while` Loop

1. What is the difference between a `while` loop and a `do-while` loop?
2. Why does a do-while loop execute at least once?
3. Can a do-while loop execute when its condition is initially false? Explain with an example.

## Section 3: `for` Loop

1. What are the three parts of a for loop header?
2. What is the output of for (int i = 1; i <= 3; i++) cout << i << " ";
3. Why does for (int i = 1; i >= 5; i++) print nothing?
4. What does a semicolon directly after the loop header do?

## Section 4: `break` and `continue` Loop

1. What is the purpose of the `break` statement?
2. What is the purpose of the `continue` statement?
3. What happens when `break` is executed inside a loop?
4. Does `continue` terminate a loop?
5. What is the difference between `break` and `continue`?
6. Can we use `break` and `continue` in a while loop?
7. What happens when `continue` is used before updating the loop-control variable in a while loop?

**Answer:**

When `continue` is used before updating the loop-control variable in a `while` loop, the update statement may be skipped. As a result, the loop-control variable may never change, causing an infinite loop.

**Example:**

```cpp
int i = 1;

while (i <= 5)
{
    if (i == 3)
    {
        continue;
    }

    cout << i << " ";
    i++;
}
```

**Explanation:**

- The loop prints 1 and 2.
- When `i` becomes 3, the `continue` statement executes.
- The remaining statements, including `i++`, are skipped.
- The value of `i` remains 3.
- The loop repeatedly checks the same condition and never terminates.

Correct approach:

```cpp
int i = 1;

while (i <= 5)
{
    if (i == 3)
    {
        i++;
        continue;
    }

    cout << i << " ";
    i++;
}
```

**Output:**

```
1 2 4 5
```

**Remember:** Always ensure that the loop-control variable is updated appropriately before `continue` in a `while` loop to avoid an infinite loop.

---

8. How do `break` and `continue` behave in nested loops?