---
layout: page
title: "Logical Operators in `if` Statements"
description: "Learn how to combine conditions in C++ if statements using the logical AND (&&), OR (||), and NOT (!) operators, with beginner-friendly examples and practical programs."
keywords: C++ logical operators, logical AND operator in C++, logical OR operator in C++, logical NOT operator in C++, && operator in C++, || operator in C++, ! operator in C++, combining conditions in C++, logical operators in if statements, C++ conditional expressions, C++ decision making, C++ tutorial for beginners
---

## 1. Learning Objectives

After completing this lesson, you will be able to:

- Use logical operators inside `if` and `if-else` statements.
- Combine multiple conditions using `&&`, `||`, and `!`.
- Understand how changing variable values affects program output.
- Write programs to solve real-life problems.

## 2. Quick Revision: Logical Operators

# &&

AND

Both conditions must be true.

**Example:** marks >= 50 && attendance >= 75

# ||

OR

At least one condition must be true.

Example: marks >= 90 || attendance == 100

# !

NOT

Reverses a condition from true to false or false to true.

Example: !(marks >= 50)

## Example 1: Student Pass or Fail Using AND (`&&`)

Problem: A student passes only if marks are at least 50 and attendance is at least 75%.

### Step 1 — Understand the problem

Suppose a student obtains 65 marks and has 80% attendance.

We need to check two conditions:

1. Are marks greater than or equal to 50?
2. Is attendance greater than or equal to 75%?

Both conditions must be true for the student to pass.

### Step 2 — Write the code

```

#include <iostream>
using namespace std;

int main() {
    int marks = 65;
    int attendance = 80;

    if (marks >= 50 && attendance >= 75) {
        cout << "Pass";
    } else {
        cout << "Fail";
    }

    return 0;
}

```

### Step 3 — Understand the code

| Code                   | Explanation                                    |
| ---------------------- | ---------------------------------------------- |
| `int marks = 65;`      | Stores the student's marks.                    |
| `int attendance = 80;` | Stores attendance percentage.                  |
| `marks >= 50`          | True because 65 is greater than 50.            |
| `attendance >= 75`     | True because 80 is greater than 75.            |
| `&&`                   | Checks whether both conditions are true.       |
| `if`                   | Executes when the complete condition is true.  |
| `else`                 | Executes when the complete condition is false. |

### Step 4 — Trace the conditions

Marks >= 50

TRUE

Attendance >= 75

TRUE

TRUE && TRUE

TRUE

Output

Pass

### Step 5 — Modify the code

Change only the variable values and predict the output.

### Experiment with marks and attendance

Marks

## 65

0

50

100

Attendance (%)

## 80%

0%

75%

100%

Condition: marks >= 50 && attendance >= 75

Output: Pass

Marks condition: True; Attendance condition: True.

Your task: Set marks to `70` and attendance to `60`. Explain why the output is `Fail`.

## Example 2: Scholarship Eligibility Using AND (`&&`)

Problem: A student can receive a scholarship if family income is below Rs. 50,000 per month and marks are at least 80.

### Step 1 — Understand the problem

Both conditions must be satisfied:

- Family income is less than 50,000.
- Marks are at least 80.

### Step 2 — Write the code

```

#include <iostream>
using namespace std;

int main() {
    int income = 40000;
    int marks = 85;

    if (income < 50000 && marks >= 80) {
        cout << "Eligible for scholarship";
    } else {
        cout << "Not eligible";
    }

    return 0;
}

```

### Step 3 — Understand the code

- `income < 50000` → True.
- `marks >= 80` → True.
- `true && true` → True.

Output:

```
Eligible for scholarship
```

### Step 4 — Modify the code

Try these changes one by one.

| Income | Marks | Expected output          |
| ------ | ----- | ------------------------ |
| 40,000 | 85    | Eligible for scholarship |
| 60,000 | 85    | Not eligible             |
| 40,000 | 70    | Not eligible             |
| 60,000 | 70    | Not eligible             |

Learning point: If either condition becomes false, the AND expression becomes false.

## Example 3: Bonus Eligibility Using OR (`||`)

Problem: An employee receives a bonus if sales are at least Rs. 100,000 OR the employee has completed 10 years of service.

### Step 1 — Understand the problem

Only one condition needs to be true.

### Step 2 — Write the code

```

#include <iostream>
using namespace std;

int main() {
    int sales = 80000;
    int serviceYears = 12;

    if (sales >= 100000 || serviceYears >= 10) {
        cout << "Bonus approved";
    } else {
        cout << "Bonus not approved";
    }

    return 0;
}

```

### Step 3 — Understand the code

- `sales >= 100000` → False.
- `serviceYears >= 10` → True.
- `false || true` → True.

Output:

```
Bonus approved
```

### Step 4 — Modify the code

Change the values and predict the output.

| Sales   | Service years | Expected output    |
| ------- | ------------- | ------------------ |
| 120,000 | 5             | Bonus approved     |
| 80,000  | 12            | Bonus approved     |
| 120,000 | 12            | Bonus approved     |
| 80,000  | 5             | Bonus not approved |

Learning point: OR returns false only when both conditions are false.

## Example 4: NOT (`!`) — Checking Registration

Problem: Display a message if a student is not registered.

### Step 1 — Write the code

```

#include <iostream>
using namespace std;

int main() {
    bool registered = false;

    if (!registered) {
        cout << "Please register first";
    } else {
        cout << "Registration complete";
    }

    return 0;
}

```

### Step 2 — Understand the code

The variable `registered` is a Boolean variable. It can store `true` or `false`.

- `registered = false`
- `!registered` becomes `true`.
- The first block executes.

Output:

```
Please register first
```

### Step 3 — Modify the code

Change:

```
bool registered = false;
```

to:

```
bool registered = true;
```

Expected output:

```
Registration complete
```

Learning point: The NOT operator reverses the Boolean value.

## 5. Independent Practice Exercises

Write each program yourself. Follow the steps: Understand the problem → Write the code → Trace the conditions → Modify the code → Test the output.

## Exercise 1 — Driving Eligibility

AND · Easy

A person can drive if their age is at least 18 and they have a valid driving licence.

Tasks

1. Declare `age` and `hasLicence`.
2. Use `&&` in an `if-else` statement.
3. Display `Allowed to drive` or `Not allowed to drive`.
4. Test with age 20 and a valid licence, then age 17 and a valid licence.

## Exercise 2 — Exam Admission

OR · Easy

A student can enter an examination hall if they have an admit card OR special permission.

Tasks

1. Declare two Boolean variables: `hasAdmitCard` and `hasPermission`.
2. Use `||` in an `if-else` statement.
3. Display `Entry allowed` or `Entry denied`.
4. Test all four combinations of `true` and `false`.

## Exercise 3 — Free Delivery

AND · Intermediate

An online store offers free delivery when the order amount is at least Rs. 3,000 and the customer lives within the delivery area.

Tasks

1. Input the order amount.
2. Input whether the customer is in the delivery area.
3. Use `&&` to check both conditions.
4. Display `Free delivery` or `Delivery charges apply`.

## Exercise 4 — Library Access

NOT · Intermediate

Display `Account active` if the student's library account is not blocked.

Tasks

1. Declare `bool isBlocked = false;`.
2. Use `!` inside the `if` statement.
3. Display `Account active` or `Account blocked`.
4. Change `isBlocked` to `true` and observe the output.

## Exercise 5 — University Admission

Mixed operators · Challenge

A student qualifies if their marks are at least 60 and they have either a valid entry test result OR an approved exemption.

Tasks

1. Declare variables for marks, entry test status, and exemption status.
2. Combine `&&` and `||` in one `if` condition.
3. Display `Eligible for admission` or `Not eligible`.
4. Test at least four combinations of values.


**Important:** When combining `&&` and `||` in the same condition, use parentheses to make the intended logic clear. For example:

```
if (marks >= 60 && (hasTestResult || hasExemption))
```

This means the student needs marks of at least 60 and must have either a valid test result or an approved exemption.