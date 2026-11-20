# Student Notes: Mathematical Functions in PostgreSQL

## 1. Introduction

In databases, we often need to perform mathematical calculations on stored data.

For example, a university may need to:

- Calculate students' percentages.
- Calculate increased tuition fees.
- Round marks to whole numbers.
- Calculate the difference between two amounts.
- Find the highest and lowest marks.
- Calculate averages and totals.

PostgreSQL provides built-in mathematical functions to perform these calculations directly in SQL queries.

## 2. What Are Mathematical Functions?

Mathematical functions are built-in PostgreSQL functions that perform calculations on numeric values.

For example:

```
SELECT ROUND(85.756, 2);
```

Output:

```
85.76
```

Here, `ROUND()` is a mathematical function that rounds a number to the specified number of decimal places.

## 3. Create a Sample Table

We will use a table named `student_results` to understand mathematical functions.

```
CREATE TABLE student_results (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    marks NUMERIC(5,2),
    fee NUMERIC(10,2)
);
```

Insert sample records:

```
INSERT INTO student_results
VALUES
(1, 'Ali', 85.75, 12500.50),
(2, 'Sara', 92.40, 15000.75),
(3, 'Ahmed', 67.25, 10000.00),
(4, 'Hina', 78.60, 13500.25),
(5, 'Usman', 55.50, 9000.50);
```

Display the records:

```
SELECT * FROM student_results;
```

## 4. ROUND() Function

The `ROUND()` function rounds a number to the nearest integer or a specified number of decimal places.

Syntax:

```
ROUND(number, decimal_places)
```

Examples:

```
SELECT ROUND(85.756, 2);
```

Output:

```
85.76
```

Round to one decimal place:

```
SELECT ROUND(85.756, 1);
```

Output:

```
85.8
```

Round to the nearest whole number:

```
SELECT ROUND(85.756);
```

Output:

```
86
```

Practical example:

Display student marks rounded to one decimal place.

```
SELECT
    student_name,
    ROUND(marks, 1) AS rounded_marks
FROM student_results;
```

## 5. CEIL() and CEILING() Functions

The `CEIL()` function rounds a number upward to the nearest integer.

PostgreSQL also supports `CEILING()`, which works in the same way.

Examples:

```
SELECT CEIL(4.2);
```

Output:

```
5
```

Another example:

```
SELECT CEILING(7.1);
```

Output:

```
8
```

Remember:

- `CEIL(4.2)` returns `5`.
- `CEIL(-4.2)` returns `-4`.

Practical example:

```
SELECT
    student_name,
    CEIL(marks) AS rounded_marks
FROM student_results;
```

## 6. FLOOR() Function

The `FLOOR()` function rounds a number downward to the nearest integer.

Examples:

```
SELECT FLOOR(4.9);
```

Output:

```
4
```

Another example:

```
SELECT FLOOR(8.7);
```

Output:

```
8
```

Remember:

- `FLOOR(4.9)` returns `4`.
- `FLOOR(-4.2)` returns `-5`.

Practical example:

```
SELECT
    student_name,
    FLOOR(marks) AS rounded_marks
FROM student_results;
```

## 7. TRUNC() Function

The `TRUNC()` function removes decimal digits without rounding the number.

Syntax:

```
TRUNC(number, decimal_places)
```

Example:

```
SELECT TRUNC(85.759, 2);
```

Output:

```
85.75
```

Compare `ROUND()` and `TRUNC()`:

```
SELECT ROUND(85.759, 2);
```

Output: `85.76`

```
SELECT TRUNC(85.759, 2);
```

Output: `85.75`

Practical example:

```
SELECT
    student_name,
    TRUNC(marks, 1) AS truncated_marks
FROM student_results;
```

## 8. ABS() Function

The `ABS()` function returns the absolute value of a number.

An absolute value is always zero or positive.

Examples:

```
SELECT ABS(-25);
```

Output:

```
25
```

```
SELECT ABS(25);
```

Output:

```
25
```

Practical example:

Calculate the absolute difference between two students' marks.

```
SELECT ABS(85.75 - 67.25) AS marks_difference;
```

Output:

```
18.50
```

## 9. POWER() Function

The `POWER()` function raises a number to a specified exponent.

Syntax:

```
POWER(base, exponent)
```

Example:

```
SELECT POWER(2, 3);
```

Output:

```
8
```

Explanation:

\\[ 2^3 = 2 \times 2 \times 2 = 8 \\]

Another example:

```
SELECT POWER(5, 2);
```

Output:

```
25
```

## 10. SQRT() Function

The `SQRT()` function calculates the square root of a number.

Example:

```
SELECT SQRT(81);
```

Output:

```
9
```

Another example:

```
SELECT SQRT(64);
```

Output:

```
8
```

A negative input produces an error for real-valued square roots.

## 11. MOD() Function

The `MOD()` function returns the remainder after division.

Syntax:

```
MOD(dividend, divisor)
```

Example:

```
SELECT MOD(10, 3);
```

Output:

```
1
```

Explanation:

\\[ 10 \div 3 = 3 \text{ remainder } 1 \\]

Another example:

```
SELECT MOD(20, 5);
```

Output:

```
0
```

Practical example: Check even and odd numbers

```
SELECT MOD(10, 2);
```

Output: `0`

If the remainder is `0`, the number is even. Otherwise, it is odd.

## 12. SIGN() Function

The `SIGN()` function tells us whether a number is positive, negative, or zero.

It returns:

- `1` for a positive number.
- `-1` for a negative number.
- `0` for zero.

Examples:

```
SELECT SIGN(25);
```

Output: `1`

```
SELECT SIGN(-25);
```

Output: `-1`

```
SELECT SIGN(0);
```

Output: `0`

## 13. PI() Function

The `PI()` function returns the mathematical constant π (pi).

```
SELECT PI();
```

Output is approximately:

```
3.141592653589793
```

Practical example: Calculate the area of a circle

Formula:

\\[ Area = \pi \times r^2 \\]

SQL:

```
SELECT PI() * POWER(5, 2) AS circle_area;
```

Output is approximately:

```
78.54
```

## 14. EXP() Function

The `EXP()` function calculates the exponential value of a number.

It raises the mathematical constant \\(e\\) to the specified power.

Example:

```
SELECT EXP(1);
```

Output is approximately:

```
2.718281828459045
```

Another example:

```
SELECT EXP(2);
```

## 15. LOG() and LN() Functions

These functions calculate logarithms.

### LN()

The `LN()` function calculates the natural logarithm (base \\(e\\)).

```
SELECT LN(10);
```

### LOG()

The `LOG()` function calculates the base-10 logarithm when given one argument.

```
SELECT LOG(100);
```

Output:

```
2
```

You can also specify a base:

```
SELECT LOG(2, 8);
```

Output:

```
3
```

Explanation:

\\[ 2^3 = 8 \\]

## 16. RANDOM() Function

The `RANDOM()` function generates a random decimal number between `0.0` (inclusive) and `1.0` (exclusive).

```
SELECT RANDOM();
```

Each execution may produce a different result.

Generate a random number between 1 and 10:

```
SELECT FLOOR(RANDOM() * 10) + 1 AS random_number;
```

This function is useful for practice exercises and random sampling. It should not be used for security-sensitive random values.

## 17. GREATEST() Function

The `GREATEST()` function returns the largest value from a list of expressions.

Example:

```
SELECT GREATEST(10, 25, 15, 40, 5);
```

Output:

```
40
```

Practical example:

Find the highest marks among three values.

```
SELECT GREATEST(85, 92, 78) AS highest_marks;
```

## 18. LEAST() Function

The `LEAST()` function returns the smallest value from a list of expressions.

Example:

```
SELECT LEAST(10, 25, 15, 40, 5);
```

Output:

```
5
```

Practical example:

Find the lowest marks among three values.

```
SELECT LEAST(85, 92, 78) AS lowest_marks;
```

## 19. Arithmetic Operators in PostgreSQL

PostgreSQL also provides arithmetic operators for basic calculations.

| Operator | Operation      | Example    | Result |
| -------- | -------------- | ---------- | ------ |
| `+`      | Addition       | `10 + 5`   | 15     |
| `-`      | Subtraction    | `10 - 5`   | 5      |
| `*`      | Multiplication | `10 * 5`   | 50     |
| `/`      | Division       | `10.0 / 2` | 5      |
| `%`      | Remainder      | `10 % 3`   | 1      |
| `^`      | Power          | `2 ^ 3`    | 8      |

Examples:

```
SELECT 10 + 5 AS addition;
SELECT 10 - 5 AS subtraction;
SELECT 10 * 5 AS multiplication;
SELECT 10.0 / 3 AS division;
SELECT 10 % 3 AS remainder;
SELECT 2 ^ 3 AS power;
```

Important: Integer division

When both operands are integers, PostgreSQL removes the fractional part:

```
SELECT 10 / 3;
```

Output:

```
3
```

To get a decimal result, use a decimal or numeric value:

```
SELECT 10.0 / 3;
```

## 20. Practical Examples Using Student Records

Now let's use mathematical functions with our `student_results` table.

### Example 1: Increase Student Fees by 500

```
SELECT
    student_name,
    fee,
    fee + 500 AS updated_fee
FROM student_results;
```

### Example 2: Increase Student Fees by 5%

```
SELECT
    student_name,
    fee,
    ROUND(fee * 1.05, 2) AS increased_fee
FROM student_results;
```

### Example 3: Display Marks Rounded to Two Decimal Places

```
SELECT
    student_name,
    ROUND(marks, 2) AS rounded_marks
FROM student_results;
```

### Example 4: Calculate the Difference Between Marks and 100

```
SELECT
    student_name,
    marks,
    ABS(100 - marks) AS remaining_marks
FROM student_results;
```

### Example 5: Display Marks in Descending Order

```
SELECT
    student_name,
    ROUND(marks) AS rounded_marks
FROM student_results
ORDER BY marks DESC;
```

### Example 6: Find the Highest and Lowest Marks

```
SELECT
    MAX(marks) AS highest_marks,
    MIN(marks) AS lowest_marks
FROM student_results;
```

## 21. Important Points to Remember

1. `ROUND()` rounds a number.
2. `TRUNC()` removes decimal digits without rounding.
3. `CEIL()` rounds upward.
4. `FLOOR()` rounds downward.
5. `ABS()` returns a positive absolute value.
6. `POWER()` calculates powers.
7. `SQRT()` calculates square roots.
8. `MOD()` returns the remainder.
9. `GREATEST()` returns the largest value.
10. `LEAST()` returns the smallest value.
11. Division by zero causes an error.
12. Use `NUMERIC` for financial values where exact decimal precision matters.
13. Most mathematical functions return `NULL` when their input is `NULL`.

## 22. Practice Exercises

### Beginner Level

Exercise 1: Write a query to round `78.456` to two decimal places.

Exercise 2: Find the absolute value of `-150`.

Exercise 3: Find the square root of `144`.

Exercise 4: Calculate the remainder when `25` is divided by `4`.

Exercise 5: Find the largest value among `15`, `30`, `45`, and `20`.

### Intermediate Level

Exercise 6: Display each student's name and marks rounded to the nearest whole number.

Exercise 7: Display each student's fee after increasing it by 10%.

Exercise 8: Display student names and the absolute difference between their marks and 100.

Exercise 9: Display student fees after removing decimal digits without rounding.

Exercise 10: Generate a random integer between 1 and 100.

### Advanced Level

Exercise 11: Display student names, original fees, and fees after a 7.5% increase. Round the new fees to two decimal places.

Exercise 12: Find the difference between the highest and lowest marks in the table.

Exercise 13: Display the remainder when each student's `student_id` is divided by 2. Use it to identify even and odd student IDs.

Exercise 14: Calculate the area of a circle with a radius of 7 using `PI()` and `POWER()`.

Exercise 15: Write a query that displays each student's marks rounded to one decimal place and sorts the result from highest to lowest.

## 23. Review Questions

1. What are mathematical functions in PostgreSQL?
2. What is the difference between `ROUND()` and `TRUNC()`?
3. What is the purpose of `ABS()`?
4. How does `CEIL()` differ from `FLOOR()`?
5. What does the `MOD()` function return?
6. How can we calculate the square root of a number?
7. What is the purpose of `POWER()`?
8. What is the difference between `GREATEST()` and `LEAST()`?
9. What happens when we divide an integer by another integer?
10. Why is the `NUMERIC` data type useful for financial calculations?

## 24. Quick Revision

| Function     | Purpose                 |
| ------------ | ----------------------- |
| `ROUND()`    | Rounds a number         |
| `CEIL()`     | Rounds upward           |
| `FLOOR()`    | Rounds downward         |
| `TRUNC()`    | Removes decimal digits  |
| `ABS()`      | Returns absolute value  |
| `POWER()`    | Calculates power        |
| `SQRT()`     | Calculates square root  |
| `MOD()`      | Returns remainder       |
| `SIGN()`     | Identifies number sign  |
| `PI()`       | Returns pi              |
| `EXP()`      | Calculates exponential  |
| `LN()`       | Natural logarithm       |
| `LOG()`      | Logarithm               |
| `RANDOM()`   | Generates random number |
| `GREATEST()` | Returns largest value   |
| `LEAST()`    | Returns smallest value  |

Next Lesson: JSON and JSONB in PostgreSQL

In the next lesson, students will learn how PostgreSQL stores and retrieves JSON data, how to use JSON operators, and how to work with structured data inside a database column.