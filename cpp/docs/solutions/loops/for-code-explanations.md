---
layout: page
title: "C++ for Loop Code Explanations"
description: "Explore solved C++ while loop exercises, including a multiplication table, algorithm analysis, dry run, complete code, code explanation, and sample output."
keywords: C++ while loop solutions, C++ while loop examples, while loop exercises, C++ multiplication table, LOOP-COD-006, C++ loop programming, counter loop C++
---

# Contents

- [Example 7: Nested `for` Loops – Printing a Rectangle Pattern](#loop-for-exp-007)

---

<a id="loop-for-exp-007"></a>

# Example 7: Nested `for` Loops – Printing a Rectangle Pattern

## 1. Problem Analysis

Problem: Write a C++ program using nested `for` loops to print a rectangular pattern of stars (`*`).

Requirements:

- Print 4 rows.
- Print 5 stars in each row.
- Use an outer `for` loop to control the rows.
- Use an inner `for` loop to print the stars in each row.
- Move to the next line after printing all 5 stars in a row.

Understanding the problem:

Think of the output as a rectangle:

- The outer loop runs 4 times (4 rows).
- The inner loop runs 5 times for each row (5 stars).
- `cout << endl;` moves the cursor to the next line after each row.

## 2. Algorithm

1. Start the program.
2. Initialize the outer loop variable `i = 1`.
3. Repeat the outer loop while `i <= 4`.
4. Inside the outer loop:
   - Initialize the inner loop variable `j = 1`.
   - Repeat the inner loop while `j <= 5`.
   - Print `* ` during each iteration.
   - Increment `j` by 1.
5. After the inner loop finishes, move to the next line using `endl`.
6. Increment `i` by 1.
7. Repeat until the outer loop finishes.
8. End the program.

## 3. Pseudocode

```text
START

FOR i = 1 TO 4

    FOR j = 1 TO 5
        PRINT "* "
    END FOR

    PRINT NEW LINE

END FOR

STOP
```

## 4. Dry Run Table

The outer loop controls the rows, while the inner loop controls the stars printed in each row.

| Outer loop (i) | Inner loop (j) | Output         |
| -------------- | -------------- | -------------- |
| 1              | 1, 2, 3, 4, 5  | \* \* \* \* \* |
| 2              | 1, 2, 3, 4, 5  | \* \* \* \* \* |
| 3              | 1, 2, 3, 4, 5  | \* \* \* \* \* |
| 4              | 1, 2, 3, 4, 5  | \* \* \* \* \* |

Total iterations:

- Outer loop: 4 iterations.
- Inner loop: 5 iterations per outer loop iteration.
- Total stars: 4 × 5 = 20 stars.

## 5. Complete C++ Code

```cpp
#include <iostream>
using namespace std;

int main()
{
    for (int i = 1; i <= 4; i++)
    {
        for (int j = 1; j <= 5; j++)
        {
            cout << "* ";
        }

        cout << endl;
    }

    return 0;
}
```

## 6. Detailed Code Explanation (Line by Line)

### Line 1: Include the input/output library

```cpp
#include <iostream>
```

- Includes the input/output stream library.
- Allows us to use `cout` to display output on the screen.

### Line 2: Use the standard namespace

```cpp
using namespace std;
```

- Allows us to use standard C++ objects such as `cout` and `endl` without writing `std::` before them.

### Line 3: Main function

```cpp
int main()
```

- The `main()` function is the starting point of the program.
- Program execution begins from this function.
- `int` indicates that the function returns an integer value.

### Line 4: Opening curly brace

```
{
```

- Marks the beginning of the `main()` function body.

### Line 5: Outer for loop

```cpp
for (int i = 1; i <= 4; i++)
```

This loop controls the number of rows.

It contains three parts:

| Part        | Explanation                                              |
| ----------- | -------------------------------------------------------- |
| `int i = 1` | Initializes the row counter at 1.                        |
| `i <= 4`    | Continues the loop while `i` is less than or equal to 4. |
| `i++`       | Increases the value of `i` by 1 after each iteration.    |

How it works:

- First iteration: `i = 1` (Row 1).
- Second iteration: `i = 2` (Row 2).
- Third iteration: `i = 3` (Row 3).
- Fourth iteration: `i = 4` (Row 4).

The outer loop executes 4 times, so the program prints 4 rows.

### Line 6: Opening curly brace of the outer loop

```cpp
{
```

- Marks the beginning of the outer loop body.
- The statements inside these braces execute during each iteration of the outer loop.

### Line 7: Inner for loop

```cpp
for (int j = 1; j <= 5; j++)
```

This loop controls the number of stars in each row.

It also contains three parts:

| Part        | Explanation                                              |
| ----------- | -------------------------------------------------------- |
| `int j = 1` | Initializes the star counter at 1.                       |
| `j <= 5`    | Continues the loop while `j` is less than or equal to 5. |
| `j++`       | Increases the value of `j` by 1 after each iteration.    |

How it works:

- First iteration: `j = 1` (First star).
- Second iteration: `j = 2` (Second star).
- Third iteration: `j = 3` (Third star).
- Fourth iteration: `j = 4` (Fourth star).
- Fifth iteration: `j = 5` (Fifth star).

The inner loop executes 5 times for every iteration of the outer loop.

### Line 8: Print the star

```cpp
cout << "* ";
```

- Displays a star (`*`) on the screen.
- The space after the star separates it from the next star.
- This statement executes 5 times during each row.

### Line 9: Closing curly brace of the inner loop

```cpp
}
```

- Marks the end of the inner loop.
- After printing 5 stars, the inner loop terminates.

### Line 10: Move to the next line

```cpp
cout << endl;
```

- Moves the cursor to the next line.
- Executes after the inner loop finishes.
- Ensures that each new row starts on a separate line.

### Line 11: Closing curly brace of the outer loop

```cpp
}
```

- Marks the end of the outer loop.
- The outer loop increments `i` and starts the next row.
- This process continues until 4 rows have been printed.

### Line 12: Return statement

```cpp
return 0;
```

- Terminates the `main()` function.
- Returns `0` to indicate successful program execution.

### Line 13: Closing curly brace

```cpp
}
```

- Marks the end of the `main()` function.

## 7. Sample Output

```
* * * * *
* * * * *
* * * * *
* * * * *
```

## 8. Important Concepts to Remember

| Concept          | Purpose                                   |
| ---------------- | ----------------------------------------- |
| Outer loop (`i`) | Controls the number of rows.              |
| Inner loop (`j`) | Controls the number of stars in each row. |
| `cout << "* ";`  | Prints one star.                          |
| `cout << endl;`  | Moves to the next line.                   |
| Nested loops     | A loop inside another loop.               |

**Remember this simple rule:**

- Outer loop = Rows.
- Inner loop = Columns (stars).
- `endl` = Move to the next row.

