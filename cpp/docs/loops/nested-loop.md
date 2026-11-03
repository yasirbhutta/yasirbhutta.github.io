---
layout: page
title: "C++ Nested Loops: Patterns, Examples, and Tracing"
description: "Learn C++ nested loops by tracing outer and inner iterations, printing star and number patterns, and using break and continue in beginner-friendly examples."
keywords: C++ nested loops, nested for loops, C++ loop patterns, star patterns in C++, number patterns in C++, nested loop examples, outer and inner loops, trace nested loops, break and continue in C++, C++ programming for beginners
---

## 1. Learning Objectives

By the end of this lecture, students will be able to:

- Understand nested loops.
- Explain the relationship between outer and inner loops.
- Trace nested loops step by step.
- Create star and number patterns.
- Use `break` to terminate a loop.
- Use `continue` to skip an iteration.

## 2. What Is a Nested Loop?

A nested loop is a loop placed inside another loop.

Think of a classroom with 3 rows of students, with 4 students in each row. The outer loop represents the rows, while the inner loop represents the students in each row.

[Inspiration for Classroom Seating Arrangements | Teach Starter](https://images.openai.com/static-rsc-4/hrwgAfjyfV575J51kC9zTaqDesDuDb_UeOTp2CMrv60uY2w2yJbZOEEUU-P1rxo-VRvo2UsFkX_iqSeaasgl7qz1gloZbd_WqsBaKYwQPsm6Eq5CxFTmKHmqVGEl7SnVLvKkZly1hYBbS7jXBKHbWNRuRrVINmBKOTfuHjlg6tM?purpose=inline)

[teachstarter.com](https://www.teachstarter.com/gb/blog/inspiration-for-classroom-seating-arrangements-2/)

The outer loop runs once for each row. For every outer-loop iteration, the inner loop completes all its iterations.

## 3. Example 1: Print a Rectangle of Stars

```
#include <iostream>
using namespace std;

int main()
{
    for (int i = 1; i <= 3; i++)
    {
        for (int j = 1; j <= 4; j++)
        {
            cout << "* ";
        }

        cout << endl;
    }

    return 0;
}
```

Output:

```
* * * *
* * * *
* * * *
```

### Understand the Code

- The outer loop (`i`) runs 3 times, producing 3 rows.
- The inner loop (`j`) runs 4 times for every row, printing 4 stars.
- `cout << endl;` moves to the next line after each row.

Total stars: \\(3 \times 4 = 12\\)

### Trace the Execution

| Outer loop `i` | Inner loop `j` | Action        |
| -------------- | -------------- | ------------- |
| 1              | 1, 2, 3, 4     | Print 4 stars |
| 2              | 1, 2, 3, 4     | Print 4 stars |
| 3              | 1, 2, 3, 4     | Print 4 stars |

## 4. Example 2: Right-Angle Triangle of Stars

```
#include <iostream>
using namespace std;

int main()
{
    for (int i = 1; i <= 5; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            cout << "* ";
        }

        cout << endl;
    }

    return 0;
}
```

Output:

```
*
* *
* * *
* * * *
* * * * *
```

### Understand the Code

The key statement is:

```
for (int j = 1; j <= i; j++)
```

Unlike the previous example, the inner loop depends on the outer loop's counter `i`.

- When `i = 1`, print 1 star.
- When `i = 2`, print 2 stars.
- When `i = 3`, print 3 stars.
- Continue until 5 rows are printed.

### Modify the Code

1. Print a triangle with 7 rows.
2. Replace `*` with `#`.
3. Print numbers instead of stars, as shown below.

```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

## 5. Example 3: Number Pattern

```
#include <iostream>
using namespace std;

int main()
{
    for (int i = 1; i <= 4; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            cout << i << " ";
        }

        cout << endl;
    }

    return 0;
}
```

Output:

```
1
2 2
3 3 3
4 4 4 4
```

### Understand the Code

Notice the difference between `i` and `j`:

- `i` determines the row number and the value printed.
- `j` determines how many times that value is printed.

### Modify the Code

Produce this pattern:

```
1 1 1 1
2 2 2 2
3 3 3 3
4 4 4 4
```

Hint: Keep the inner loop's condition independent of `i`, so every row contains four numbers.

## 6. Example 4: Multiplication Tables Using Nested Loops

```
#include <iostream>
using namespace std;

int main()
{
    for (int i = 1; i <= 3; i++)
    {
        cout << "Table of " << i << endl;

        for (int j = 1; j <= 5; j++)
        {
            cout << i << " x " << j
                 << " = " << i * j << endl;
        }

        cout << endl;
    }

    return 0;
}
```

Sample output:

```
Table of 1
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
1 x 5 = 5

Table of 2
2 x 1 = 2
2 x 2 = 4
...
```

### Understand the Code

The outer loop selects the table. The inner loop calculates five multiplication results for each table.

### Modify the Code

1. Display tables from 1 to 10.
2. Display each table up to 10.
3. Ask the user how many tables to display.

## 7. The `break` Statement

The `break` statement immediately terminates the nearest enclosing loop. Execution continues with the statement after that loop.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://learn.microsoft.com\&sz=32)

Microsoft Learn

+1



Real-life example: A student is searching a list for a particular student ID. Once the ID is found, there is no need to continue searching.

### Example: Stop at Number 5

```
#include <iostream>
using namespace std;

int main()
{
    for (int i = 1; i <= 10; i++)
    {
        if (i == 5)
        {
            break;
        }

        cout << i << " ";
    }

    return 0;
}
```

Output:

```
1 2 3 4
```

### Understand the Code

- The loop starts at 1.
- When `i` becomes 5, the condition `i == 5` is true.
- `break` terminates the loop immediately.
- The number 5 is not printed because `break` executes before `cout`.

### Modify the Code

1. Stop the loop when `i == 7`.
2. Print numbers from 1 to 100, but stop at 15.
3. Ask the user to enter numbers and stop when they enter 0.

## 8. The `continue` Statement

The `continue` statement skips the remaining statements in the current iteration and moves to the next iteration. In a `for` loop, the update expression still executes.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.learncpp.com\&sz=32)

Break and continue – Learn C++

+1



### Example: Skip Number 5

```
#include <iostream>
using namespace std;

int main()
{
    for (int i = 1; i <= 10; i++)
    {
        if (i == 5)
        {
            continue;
        }

        cout << i << " ";
    }

    return 0;
}
```

Output:

```
1 2 3 4 6 7 8 9 10
```

### Understand the Code

When `i` becomes 5, `continue` skips the `cout` statement for that iteration. The loop then moves to the next value, 6.

### Modify the Code

1. Skip number 3.
2. Skip all even numbers.
3. Print numbers from 1 to 20, skipping multiples of 5.

## 9. Difference Between `break` and `continue`

| `break`                                                        | `continue`                                    |
| -------------------------------------------------------------- | --------------------------------------------- |
| Terminates the loop.                                           | Skips the current iteration.                  |
| No further iterations occur in that loop.                      | The loop continues with the next iteration.   |
| Useful when a task is complete or a stopping condition is met. | Useful when certain values should be ignored. |

Easy way to remember:

- `break` = Stop.
- `continue` = Skip and continue.

## 10. Important Concept: `break` in Nested Loops

A `break` inside an inner loop terminates only the inner loop. The outer loop continues normally.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.programiz.com\&sz=32)

Programiz

+1



```
#include <iostream>
using namespace std;

int main()
{
    for (int i = 1; i <= 3; i++)
    {
        for (int j = 1; j <= 4; j++)
        {
            if (j == 3)
            {
                break;
            }

            cout << j << " ";
        }

        cout << endl;
    }

    return 0;
}
```

Output:

```
1 2
1 2
1 2
```

The inner loop stops whenever `j` reaches 3. The outer loop still creates all three rows.

## 11. Coding Exercises

Practice tracker

0/6 completed

Basic

1\. Rectangle of stars

Use nested loops to print 4 rows, with 6 stars in each row.

Basic

2\. Number triangle

Print a triangle where row 1 contains 1, row 2 contains 1 2, and so on up to row 6.

Intermediate

3\. Multiplication tables

Print the multiplication tables from 2 to 5, each up to 10.

Intermediate

4\. Skip multiples

Print numbers from 1 to 50 but use continue to skip multiples of 3.

Intermediate

5\. Stop at a value

Print numbers from 1 to 100 but use break to stop when the counter reaches 25.

Challenge

6\. User-defined pattern

Ask the user for the number of rows and print a right-angle triangle of stars.

## 12. Quick Revision Quiz

1\. What does a nested loop mean?

A loop inside another loop

A loop without a condition

A loop that executes only once



2\. What does \`break\` do?

Skips one output

Stops the nearest enclosing loop

Restarts the program



3\. What does \`continue\` do in a \`for\` loop?

Ends the entire program

Skips the current iteration and proceeds to the next

Repeats the same value forever



4\. If the outer loop runs 3 times and the inner loop prints 4 stars each time, how many stars are printed?

7

12

16



Check Answers

## 13. Lesson Summary

- Nested loops are useful for patterns, tables, and grids.
- The outer loop commonly controls rows, while the inner loop controls columns.
- `break` stops the nearest enclosing loop.
- `continue` skips the current iteration.
- Practise tracing the values of both loop counters before writing more complex patterns.

Recommended next lesson: Loop applications and problem-solving — factorials, number sums, digit counting, and menu-driven programs.