---
layout: page
title: "C++ for Loop Solutions and Examples"
description: "Explore solved C++ while loop exercises, including a multiplication table, algorithm analysis, dry run, complete code, code explanation, and sample output."
keywords: C++ while loop solutions, C++ while loop examples, while loop exercises, C++ multiplication table, LOOP-COD-006, C++ loop programming, counter loop C++
---

# Contents

- [# Solution: loop-cod-030 — Display a Right-Angled Triangle Pattern Using Nested For Loops](#loop-cod-030)

---

<a id="loop-cod-030"></a>

# Solution: loop-cod-030 — Display a Right-Angled Triangle Pattern Using Nested For Loops

## 1. Problem Analysis

We need to write a C++ program that displays a right-angled triangle pattern using nested `for` loops.

The program should display:
- **5 rows**
- The first row contains 1 star.
- The second row contains 2 stars.
- The third row contains 3 stars.
- The fourth row contains 4 stars.
- The fifth row contains 5 stars.

**Understanding the problem:**

- The outer `for` loop controls the number of rows.
- The inner `for` loop controls the number of stars in each row.
- The number of stars increases by 1 in each new row.
- `cout << "* ";` displays a star followed by a space.
- `cout << endl;` moves the cursor to the next line after completing each row.

**Expected pattern:**

```text
*
* *
* * *
* * * *
* * * * *
```

## 2. Algorithm or Pseudocode

1. Start the program.
2. Set the outer loop variable `i` to 1.
3. Repeat the outer loop while `i <= 5`:
   - Set the inner loop variable `j` to 1.
   - Repeat the inner loop while `j <= i`:
     - Display `* `.
     - Increment `j` by 1.
   - Move to the next line.
   - Increment `i` by 1.
4. Stop the program.

## 3. Dry Run Table

The outer loop executes 5 times. The inner loop executes according to the current value of the outer loop variable `i`.

| Outer Loop (`i`) | Inner Loop (`j`) | Number of Stars | Output |
|---|---|---:|---|
| 1 | 1 | 1 | `*` |
| 2 | 1, 2 | 2 | `* *` |
| 3 | 1, 2, 3 | 3 | `* * *` |
| 4 | 1, 2, 3, 4 | 4 | `* * * *` |
| 5 | 1, 2, 3, 4, 5 | 5 | `* * * * *` |

**Loop execution:**

- Outer loop: 5 iterations.
- Inner loop: 1, 2, 3, 4, and 5 iterations respectively.
- Total executions of the inner loop body: 1 + 2 + 3 + 4 + 5 = **15 times**.
- Total stars displayed: **15**.

## 4. Complete C++ Code

```cpp
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

## 5. Code Explanation

Let's understand the code step by step.

**Step 1: Include the input/output library**

```cpp
#include <iostream>
```

- Includes the input/output library.
- Allows us to use `cout` to display output on the screen.

**Step 2: Use the standard namespace**

```cpp
using namespace std;
```

- Allows us to use `cout` and `endl` without writing `std::` before them.

**Step 3: Main function**

```cpp
int main()
{
```

- The execution of the C++ program starts from the `main()` function.

**Step 4: Outer for loop**

```cpp
for (int i = 1; i <= 5; i++)
```

- `int i = 1`: Initializes the outer loop variable with 1.
- `i <= 5`: The loop continues while `i` is less than or equal to 5.
- `i++`: Increments `i` by 1 after each iteration.

**Purpose:** Controls the number of rows. The loop executes 5 times, creating 5 rows.

**Step 5: Inner for loop**

```cpp
for (int j = 1; j <= i; j++)
```

- `int j = 1`: Initializes the inner loop variable with 1.
- `j <= i`: The loop continues while `j` is less than or equal to the current value of `i`.
- `j++`: Increments `j` by 1 after each iteration.

**Purpose:** Controls the number of stars in each row.

**Important:** Notice that the inner loop condition is `j <= i`, not `j <= 5`.

This means:
- When `i = 1`, the inner loop executes 1 time.
- When `i = 2`, the inner loop executes 2 times.
- When `i = 3`, the inner loop executes 3 times.
- When `i = 4`, the inner loop executes 4 times.
- When `i = 5`, the inner loop executes 5 times.

Therefore, the number of stars increases in every new row.

**Step 6: Display the star**

```cpp
cout << "* ";
```

- Displays one star followed by a space.
- Executes according to the current value of `i`.

**Step 7: Move to the next line**

```cpp
cout << endl;
```

- Moves the cursor to the next line.
- Executes after the inner loop completes.
- Ensures that each row starts on a new line.

**Step 8: Return statement**

```cpp
return 0;
```

- Indicates that the program has executed successfully.

### How Nested Loops Work

Remember:

- The outer loop starts with `i = 1`.
- The inner loop executes 1 time and displays 1 star.
- The cursor moves to the next line.
- The outer loop increments `i` to 2.
- The inner loop executes 2 times and displays 2 stars.
- This process continues until the outer loop completes 5 iterations.

**Important concept:**

In this pattern, the outer loop controls the rows, while the inner loop controls the number of stars in each row based on the current value of the outer loop variable.

## 6. Sample Output

```text
*
* *
* * *
* * * *
* * * * *
```

## 7. Modification Tasks

Try modifying the original program to solve the following exercises.

### Task 1: Display a Triangle with 7 Rows

Modify the program to display a right-angled triangle with 7 rows.

Expected output:

```text
*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *
```

### Task 2: Display a Triangle with 3 Rows

Modify the program to display a right-angled triangle with only 3 rows.

Expected output:

```text
*
* *
* * *
```

### Task 3: Display a Triangle Using Hash Symbols

Replace the star (`*`) with the hash symbol (`#`).

Display a triangle with 5 rows.

Expected output:

```text
#
# #
# # #
# # # #
# # # # #
```

### Task 4: Take the Number of Rows from the User

Modify the program to ask the user to enter the number of rows.

Use nested `for` loops to display the triangle according to the entered number.

**Example input:**

```text
Enter number of rows: 4
```

Expected output:

```text
*
* *
* * *
* * * *
```

### Task 5: Display a Triangle Using Numbers

Modify the inner loop to display numbers instead of stars.

Each row should display numbers starting from 1 up to the current row number.

Expected output:

```text
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

### Task 6: Display a Triangle Using Row Numbers

Modify the program so that each row displays the current outer loop variable `i` instead of a star.

Expected output:

```text
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
```

---

### Key Learning Points

After completing this example, students should understand:

1. How nested `for` loops work.
2. How the outer loop controls the number of rows.
3. How the inner loop controls the number of stars in each row.
4. How to use the outer loop variable (`i`) in the inner loop condition.
5. How to create increasing patterns using nested loops.
6. The difference between a rectangular pattern and a triangular pattern.

**Remember:**

- **Rectangle pattern:** The inner loop condition uses a fixed number, such as `j <= 5`.
- **Triangle pattern:** The inner loop condition uses the outer loop variable, such as `j <= i`.

This small difference in the inner loop condition changes the entire pattern!