# Lecture 7: Choosing the Right Loop in C++ and Solving Mixed Problems

## 1. Learning Objectives

By the end of this lecture, students will be able to:

- Differentiate between `for`, `while`, and `do-while` loops.
- Choose the correct loop for a given problem.
- Trace a loop step by step using a trace table.
- Solve mixed loop problems independently.
- Identify and correct common loop errors.

## 2. Real-Life Understanding

Think about these situations:

Situation 1: Print numbers from 1 to 10

You know the starting number, ending number, and number of repetitions.

Best choice: `for` loop

Situation 2: Keep asking for a password until it is correct

You do not know how many attempts will be needed.

Best choice: `while` loop

Situation 3: Display a menu at least once

The menu must appear before the user decides whether to continue.

Best choice: `do-while` loop

## 3. Compare the Three Loops

| Feature            | `for`                  | `while`                           | `do-while`                  |
| ------------------ | ---------------------- | --------------------------------- | --------------------------- |
| Condition checked  | Before each iteration  | Before each iteration             | After each iteration        |
| Minimum executions | Zero                   | Zero                              | One                         |
| Best used when     | Repetitions are known  | Repetitions depend on a condition | Code must run at least once |
| Initialization     | Usually in loop header | Usually before loop               | Usually before loop         |
| Update             | Usually in loop header | Usually inside loop               | Usually inside loop         |

Remember: All three loops can solve many of the same problems. Choose the loop that makes the program easiest to understand.

## 4. Example 1 — Use a `for` Loop

Task: Print the numbers from 1 to 5.

```
#include <iostream>
using namespace std;

int main() {
    for (int i = 1; i <= 5; i++) {
        cout << i << " ";
    }

    return 0;
}
```

Output

```
1 2 3 4 5
```

### Understand the Code

- `int i = 1`: starts counting at 1.
- `i <= 5`: continues while `i` is at most 5.
- `i++`: increases `i` by 1.
- `cout << i`: displays the current value.

### Trace Table

| Iteration | `i` | `i <= 5` | Output     |
| --------- | --- | -------- | ---------- |
| 1         | 1   | True     | 1          |
| 2         | 2   | True     | 2          |
| 3         | 3   | True     | 3          |
| 4         | 4   | True     | 4          |
| 5         | 5   | True     | 5          |
| 6         | 6   | False    | Loop stops |

Modify the Code: Print numbers from 10 to 1 in descending order.

## 5. Example 2 — Use a `while` Loop

Task: Keep adding positive numbers until the user enters `0`. Then display their sum.

```
#include <iostream>
using namespace std;

int main() {
    int number;
    int sum = 0;

    cout << "Enter a number (0 to stop): ";
    cin >> number;

    while (number != 0) {
        sum = sum + number;

        cout << "Enter a number (0 to stop): ";
        cin >> number;
    }

    cout << "Total sum = " << sum;

    return 0;
}
```

Sample output

```
Enter a number (0 to stop): 5
Enter a number (0 to stop): 3
Enter a number (0 to stop): 2
Enter a number (0 to stop): 0
Total sum = 10
```

### Understand the Code

1. `sum = 0` initializes the total.
2. The program reads a number before entering the loop.
3. If the number is not zero, it adds it to `sum`.
4. It asks for another number.
5. When the user enters zero, the loop stops.

### Trace Table

| Step | `number` | Condition `number != 0` | `sum` |
| ---- | -------- | ----------------------- | ----- |
| 1    | 5        | True                    | 5     |
| 2    | 3        | True                    | 8     |
| 3    | 2        | True                    | 10    |
| 4    | 0        | False                   | 10    |

Important: In this example, zero is a sentinel value. It signals the program to stop and is not added to the sum.

Modify the Code: Count how many non-zero numbers the user enters before stopping.

## 6. Example 3 — Use a `do-while` Loop

Task: Display a simple menu at least once and repeat it while the user chooses option 1.

```
#include <iostream>
using namespace std;

int main() {
    int choice;

    do {
        cout << "\n1. Continue";
        cout << "\n2. Exit";
        cout << "\nEnter your choice: ";
        cin >> choice;

    } while (choice == 1);

    cout << "Program ended.";

    return 0;
}
```

Sample output

```
1. Continue
2. Exit
Enter your choice: 1

1. Continue
2. Exit
Enter your choice: 2
Program ended.
```

### Understand the Code

- The menu is displayed first.
- The user enters a choice.
- If the choice is `1`, the menu appears again.
- If the choice is anything other than `1`, the loop ends.

Notice the semicolon after the condition:

```
} while (choice == 1);
```

A `do-while` loop requires this semicolon.

Modify the Code: Add a third option, `3. Display a message`, and use a `switch` statement to handle the menu choices.

## 7. Mixed Problem — Find the Factorial

Task: Calculate the factorial of a positive integer.

For example:

\\[ 5! = 5 \times 4 \times 3 \times 2 \times 1 = 120 \\]

We will use a `for` loop because the number of iterations is known after the user enters the number.

```
#include <iostream>
using namespace std;

int main() {
    int n;
    long long factorial = 1;

    cout << "Enter a non-negative integer: ";
    cin >> n;

    if (n < 0) {
        cout << "Please enter a non-negative integer.";
    } else {
        for (int i = 1; i <= n; i++) {
            factorial = factorial * i;
        }

        cout << "Factorial = " << factorial;
    }

    return 0;
}
```

### Trace Table for `n = 4`

| Iteration | `i` | Calculation   | `factorial` |
| --------- | --- | ------------- | ----------- |
| Initial   | —   | Initial value | 1           |
| 1         | 1   | `1 * 1`       | 1           |
| 2         | 2   | `1 * 2`       | 2           |
| 3         | 3   | `2 * 3`       | 6           |
| 4         | 4   | `6 * 4`       | 24          |

Output:

```
Factorial = 24
```

Understand the Code: The variable `factorial` stores the running product. It starts at 1 because multiplying by 1 does not change the product. This also gives the correct result for `0!`, which is 1.

Modify the Code: Calculate the sum of the first `n` natural numbers instead of the factorial.

## 8. Mixed Problem — Count Digits Using a `while` Loop

Task: Count the digits in a positive integer.

```
#include <iostream>
using namespace std;

int main() {
    int number;
    int count = 0;

    cout << "Enter a positive integer: ";
    cin >> number;

    if (number <= 0) {
        cout << "Please enter a positive integer.";
    } else {
        while (number > 0) {
            number = number / 10;
            count++;
        }

        cout << "Number of digits = " << count;
    }

    return 0;
}
```

### Trace Table for `number = 4527`

| Iteration | Number before division | Number after division | Count |
| --------- | ---------------------- | --------------------- | ----- |
| 1         | 4527                   | 452                   | 1     |
| 2         | 452                    | 45                    | 2     |
| 3         | 45                     | 4                     | 3     |
| 4         | 4                      | 0                     | 4     |

Output:

```
Number of digits = 4
```

Why does this work? Integer division by 10 removes the last digit. The loop repeats until no digits remain.

## 9. Practice — Choose the Right Loop

1\. Print all even numbers from 2 to 100.

for

while

do-while

2\. Keep asking for a number until the user enters -1.

for

while

do-while

3\. Display a menu at least once before checking the user's choice.

for

while

do-while

4\. Repeat a calculation exactly 20 times.

for

while

do-while

Check Answers

## 10. Independent Coding Exercises

Students should write, run, and test each program.

1. Using `for`: Display the multiplication table of a number entered by the user.
2. Using `while`: Calculate the sum of the digits of an integer.
3. Using `do-while`: Create a menu-driven program that repeats until the user selects Exit.
4. Mixed loops: Ask the user to enter 5 numbers and find the largest number.
5. Problem-solving: Keep accepting marks until the user enters `-1`. Display the number of valid marks entered and their average. Assume valid marks are from 0 to 100.

For each exercise, students should prepare a trace table for at least one sample input.

## 11. Common Mistakes

- Infinite loop: Forgetting to update the loop variable or read new input.
- Wrong condition: Using `i < 5` when the task requires printing through 5.
- Wrong initial value: Starting a product calculation at 0 instead of 1.
- Incorrect `do-while` syntax: Forgetting the semicolon after `while (condition)`.
- Poor loop selection: Using a complicated loop structure when a simple `for` loop is enough.
- Trace-table error: Updating the total or counter in the wrong order.

## Lecture Summary

- Use `for` when the number of repetitions is known.
- Use `while` when repetition depends on a condition.
- Use `do-while` when the body must execute at least once.
- Use trace tables to understand how variables change during each iteration.
- Always test boundary cases, such as zero, one repetition, and the stopping value.

Next suggested lecture: Loop-based problem solving with nested loops, number patterns, and debugging common loop errors.