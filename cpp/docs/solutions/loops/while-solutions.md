---
layout: page
title: "C++ while Loop Solutions and Examples"
description: "Explore solved C++ while loop exercises, including a multiplication table, algorithm analysis, dry run, complete code, code explanation, and sample output."
keywords: C++ while loop solutions, C++ while loop examples, while loop exercises, C++ multiplication table, LOOP-COD-006, C++ loop programming, counter loop C++
---

# Contents

- [Solution: LOOP-COD-006 — Multiplication Table](#loop-cod-006)

---

<a id="loop-cod-006"></a>

# Solution: LOOP-COD-006 — Multiplication Table

## 1. Problem Analysis

The task is to write a C++ program that asks the user to enter an integer and displays its multiplication table from 1 to 10 using a `while` loop.

**Input:**

- One integer entered by the user.

**Processing:**

- Initialize a counter variable with `1`.
- Multiply the entered number by the counter.
- Increase the counter by `1` after each iteration.
- Repeat until the counter becomes greater than `10`.

**Output:**

- Display the multiplication table from 1 to 10.

**Programming concepts required:**

- Variables
- User input and output
- `while` loop
- Arithmetic multiplication operator (`*`)
- Increment operator (`++`)

## 2. Algorithm / Pseudocode

**Algorithm**

1. Start the program.
2. Declare two integer variables: `num` and `i`.
3. Ask the user to enter a number.
4. Store the entered number in `num`.
5. Initialize `i = 1`.
6. While `i` is less than or equal to `10`:
   - Calculate `num * i`.
   - Display the multiplication expression and its result.
   - Increase `i` by `1`.
7. Stop the loop when `i` becomes greater than `10`.
8. End the program.

**Pseudocode**

```text
START

DECLARE num, i

DISPLAY "Enter a number: "
INPUT num

SET i = 1

WHILE i <= 10
    result = num * i
    DISPLAY num, " x ", i, " = ", result
    i = i + 1
END WHILE

STOP
```

## 3. Dry Run Table

A dry run helps us understand how the `while` loop executes step by step.

Given input: `7`

Initially:

- `num = 7`
- `i = 1`

| Iteration | num | i  | Calculation | Result |
| --------- | --- | -- | ----------- | ------ |
| 1         | 7   | 1  | 7 × 1       | 7      |
| 2         | 7   | 2  | 7 × 2       | 14     |
| 3         | 7   | 3  | 7 × 3       | 21     |
| 4         | 7   | 4  | 7 × 4       | 28     |
| 5         | 7   | 5  | 7 × 5       | 35     |
| 6         | 7   | 6  | 7 × 6       | 42     |
| 7         | 7   | 7  | 7 × 7       | 49     |
| 8         | 7   | 8  | 7 × 8       | 56     |
| 9         | 7   | 9  | 7 × 9       | 63     |
| 10        | 7   | 10 | 7 × 10      | 70     |

What happens after the 10th iteration?

- The value of `i` becomes `11`.
- The condition `i <= 10` becomes false.
- The loop terminates.

## 4. Complete C++ Code

```cpp
#include <iostream>
using namespace std;

int main()
{
    int num, i;

    cout << "Enter a number: ";
    cin >> num;

    i = 1;

    while (i <= 10)
    {
        cout << num << " x " << i
             << " = " << num * i << endl;

        i++;
    }

    return 0;
}
```

## 5. Code Explanation

Let's understand the important parts of the program.

### A. Declare variables

```cpp
int num, i;
```

- `num` stores the integer entered by the user.
- `i` works as a counter to control the loop.

### B. Get input from the user

```cpp
cout << "Enter a number: ";
cin >> num;
```

The program asks the user to enter an integer and stores it in `num`.

For example, if the user enters `7`, then `num = 7`.

### C. Initialize the counter

```cpp
i = 1;
```

The counter starts at `1` because we need to display the multiplication table from 1 to 10.

### D. Understand the while loop

```cpp
while (i <= 10)
```

This condition checks whether the counter is less than or equal to `10`.

- If the condition is true, the loop body executes.
- If the condition is false, the loop stops.

### E. Display the multiplication table

```cpp
cout << num << " x " << i
     << " = " << num * i << endl;
```

This statement displays the multiplication expression and calculates its result.

**For example:**

- `num = 7`
- `i = 3`
- `7 * 3 = 21`

**Output:**

```cpp
7 x 3 = 21
```

### F. Increment the counter

```cpp
i++;
```

The `++` operator increases the value of `i` by `1`.

**For example:**

- Before increment: `i = 3`
- After increment: `i = 4`

The loop then checks the condition again.

Important: Without `i++`, the counter would never increase, and the loop would continue indefinitely (infinite loop).

## 6. Sample Output

### Sample Input

```
Enter a number: 7
```

### Expected Output

```
Multiplication Table of 7
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
```

To display the heading `Multiplication Table of 7`, add this statement after reading the input:

```
cout << "Multiplication Table of " << num << endl;
```

## 7. Modification Task

Now modify the existing program to practise independently.

### Task 1: Change the Table Range

Modify the program to display the multiplication table from 1 to 15 instead of 1 to 10.

### Task 2: Reverse the Table

Display the multiplication table in reverse order, from 10 down to 1.

Expected output for input `5`:

```
5 x 10 = 50
5 x 9 = 45
5 x 8 = 40
...
5 x 1 = 5
```

### Task 3: Multiple Tables

Modify the program to ask the user for a `starting number` and an `ending number`. Display the multiplication table only within that range.
