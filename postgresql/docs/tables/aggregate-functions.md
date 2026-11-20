# Student Notes: Aggregate Functions in PostgreSQL

## 1. Introduction

In a database, we often need to calculate information from multiple records.

For example, a university may want to know:

- How many students are registered?
- What is the total fee collected?
- What is the average student age?
- What is the highest fee?
- What is the lowest fee?

PostgreSQL provides Aggregate Functions to perform these calculations.

An aggregate function takes values from multiple rows and returns a single result.

## 2. Common Aggregate Functions

PostgreSQL provides several aggregate functions.

| Function  | Purpose                 |
| --------- | ----------------------- |
| `COUNT()` | Counts rows or values   |
| `SUM()`   | Calculates the total    |
| `AVG()`   | Calculates the average  |
| `MIN()`   | Finds the minimum value |
| `MAX()`   | Finds the maximum value |

## 3. Prepare a Sample Table

We will use a table named `students`.

```
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    student_name VARCHAR(100),
    age INTEGER,
    city VARCHAR(50),
    fee NUMERIC(10, 2)
);
```

Insert some sample records:

```
INSERT INTO students
(student_id, student_name, age, city, fee)
VALUES
(1, 'Ali', 20, 'Multan', 15000),
(2, 'Ahmed', 22, 'Dera Ghazi Khan', 18000),
(3, 'Sara', 21, 'Multan', 20000),
(4, 'Ayesha', 23, 'Lahore', 17000),
(5, 'Usman', 20, 'Lahore', 16000);
```

View all records:

```
SELECT * FROM students;
```

## 4. COUNT() Function

The `COUNT()` function counts the number of rows or non-NULL values.

Example 1: Count all students

```
SELECT COUNT(*)
FROM students;
```

Output:

| count |
| ----- |
| 5     |

Explanation:

- `COUNT(*)` counts all rows.
- There are five student records in the table.

Example 2: Count student names

```
SELECT COUNT(student_name)
FROM students;
```

This counts rows where `student_name` is not `NULL`.

Example 3: Count students from Multan

```
SELECT COUNT(*)
FROM students
WHERE city = 'Multan';
```

Output:

| count |
| ----- |
| 2     |

## 5. SUM() Function

The `SUM()` function calculates the total of numeric values.

Example: Calculate the total student fee

```
SELECT SUM(fee)
FROM students;
```

Output:

| sum      |
| -------- |
| 86000.00 |

Explanation:

PostgreSQL adds all values in the `fee` column:

15,000 + 18,000 + 20,000 + 17,000 + 16,000 = 86,000.

## 6. AVG() Function

The `AVG()` function calculates the average of numeric values.

Example: Calculate the average student age

```
SELECT AVG(age)
FROM students;
```

Output:

| avg                 |
| ------------------- |
| 21.2000000000000000 |

Example: Calculate the average fee

```
SELECT AVG(fee)
FROM students;
```

The result is 17,200.

Explanation:

Average = Total of values ÷ Number of values.

## 7. MIN() Function

The `MIN()` function returns the smallest value.

Example: Find the minimum student fee

```
SELECT MIN(fee)
FROM students;
```

Output:

| min      |
| -------- |
| 15000.00 |

Example: Find the youngest student's age

```
SELECT MIN(age)
FROM students;
```

Output: `20`

## 8. MAX() Function

The `MAX()` function returns the largest value.

Example: Find the maximum student fee

```
SELECT MAX(fee)
FROM students;
```

Output:

| max      |
| -------- |
| 20000.00 |

Example: Find the oldest student's age

```
SELECT MAX(age)
FROM students;
```

Output: `23`

## 9. Using Multiple Aggregate Functions

We can use multiple aggregate functions in one SQL query.

Example: Calculate student statistics

```
SELECT
    COUNT(*) AS total_students,
    SUM(fee) AS total_fee,
    AVG(fee) AS average_fee,
    MIN(fee) AS minimum_fee,
    MAX(fee) AS maximum_fee
FROM students;
```

Output:

| total_students | total_fee | average_fee | minimum_fee | maximum_fee |
| -------------- | --------- | ----------- | ----------- | ----------- |
| 5              | 86000.00  | 17200.00    | 15000.00    | 20000.00    |

Explanation:

- `AS` gives a meaningful name to each result column.
- All five aggregate functions calculate their results from the same table.

## 10. Aggregate Functions with WHERE

We can combine aggregate functions with the `WHERE` clause to calculate results for specific records.

Example 1: Count students from Lahore

```
SELECT COUNT(*)
FROM students
WHERE city = 'Lahore';
```

Example 2: Calculate total fee of students from Multan

```
SELECT SUM(fee)
FROM students
WHERE city = 'Multan';
```

Output: `35000.00`

Example 3: Find the average age of students from Lahore

```
SELECT AVG(age)
FROM students
WHERE city = 'Lahore';
```

Output: `21.5000000000000000`

## 11. Important Concept: NULL Values

Aggregate functions generally ignore `NULL` values.

Consider a table where some students do not have a fee recorded.

```
SELECT COUNT(fee)
FROM students;
```

This counts only rows where `fee` is not `NULL`.

Compare:

```
SELECT COUNT(*)
FROM students;
```

This counts all rows, including rows containing `NULL` values.

Remember:

- `COUNT(*)` counts rows.
- `COUNT(column_name)` counts non-NULL values in that column.
- `SUM()`, `AVG()`, `MIN()`, and `MAX()` ignore NULL values.

## 12. Quick Revision

| Function  | Example    | Purpose               |
| --------- | ---------- | --------------------- |
| `COUNT()` | `COUNT(*)` | Count records         |
| `SUM()`   | `SUM(fee)` | Calculate total fee   |
| `AVG()`   | `AVG(age)` | Calculate average age |
| `MIN()`   | `MIN(fee)` | Find minimum fee      |
| `MAX()`   | `MAX(fee)` | Find maximum fee      |

## 13. Practice Exercises

Use the `students` table to solve the following exercises.

Beginner Level

1. Count the total number of students.
2. Calculate the total student fee.
3. Find the average student age.
4. Find the minimum student fee.
5. Find the maximum student fee.

Intermediate Level

6. Count students from Multan.
7. Calculate the total fee of students from Lahore.
8. Find the average age of students from Multan.
9. Find the maximum fee among students from Lahore.
10. Display total students, average age, and total fee in one query.

## 14. Review Questions

1. What is an aggregate function?
2. What is the purpose of `COUNT()`?
3. What is the difference between `COUNT(*)` and `COUNT(fee)`?
4. Which function calculates the average?
5. Which function finds the smallest value?
6. Can we use aggregate functions with `WHERE`?
7. How do aggregate functions handle NULL values?
8. What is the purpose of `AS` in an aggregate query?

## 15. Next Lesson

GROUP BY Clause in PostgreSQL

In the next lesson, students will learn how to group records and calculate aggregate results for each group, such as counting students city-wise or calculating total fees department-wise.