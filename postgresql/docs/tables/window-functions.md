# Student Notes: Window Functions in PostgreSQL

## 1. Introduction

Imagine a university has a database containing students and their marks.

The university wants to perform different tasks:

- Assign a rank to every student based on marks.
- Find the highest-scoring student in each department.
- Calculate the average marks of each department.
- Display each student's marks along with the department average.
- Calculate a running total of student fees.

We can perform these tasks using Window Functions in PostgreSQL.

Window functions allow us to perform calculations across a group of related rows while keeping individual rows in the result.

## 2. What is a Window Function?

A Window Function performs a calculation across a set of related rows, called a window, without combining those rows into a single result.

In simple words:

A window function calculates information about related rows while keeping every individual record visible.

For example, suppose we have the following student records:

| Student | Department | Marks |
| ------- | ---------- | ----- |
| Ali     | CS         | 85    |
| Sara    | CS         | 90    |
| Ahmed   | IT         | 75    |
| Hina    | IT         | 95    |

We want to display each student's marks along with the average marks of their department.

A normal `GROUP BY` query returns one row per department. A window function can display all four students along with their department averages.

## 3. Create a Sample Table

We will use a students table for practical examples.

### Step 1: Create the Table

```
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    department VARCHAR(50),
    marks INT
);
```

### Step 2: Insert Sample Records

```
INSERT INTO students
VALUES
(1, 'Ali', 'Computer Science', 85),
(2, 'Sara', 'Computer Science', 90),
(3, 'Ahmed', 'Information Technology', 75),
(4, 'Hina', 'Information Technology', 95),
(5, 'Usman', 'Mathematics', 80),
(6, 'Ayesha', 'Mathematics', 88),
(7, 'Bilal', 'Computer Science', 70),
(8, 'Zara', 'Information Technology', 85);
```

### Step 3: Display Records

```
SELECT *
FROM students;
```

## 4. Understanding GROUP BY vs Window Functions

Before learning window functions, understand the difference between `GROUP BY` and `OVER()`.

### Using GROUP BY

Calculate average marks department-wise.

```
SELECT
    department,
    AVG(marks) AS average_marks
FROM students
GROUP BY department;
```

Expected output:

| department             | average_marks |
| ---------------------- | ------------- |
| Computer Science       | 81.67         |
| Information Technology | 85            |
| Mathematics            | 84            |

Notice that GROUP BY returns only three rows.

### Using a Window Function

```
SELECT
    student_name,
    department,
    marks,
    AVG(marks) OVER (
        PARTITION BY department
    ) AS department_average
FROM students;
```

Expected output:

| student_name | department             | marks | department_average |
| ------------ | ---------------------- | ----- | ------------------ |
| Ali          | Computer Science       | 85    | 81.67              |
| Sara         | Computer Science       | 90    | 81.67              |
| Bilal        | Computer Science       | 70    | 81.67              |
| Ahmed        | Information Technology | 75    | 85                 |
| Hina         | Information Technology | 95    | 85                 |
| Zara         | Information Technology | 85    | 85                 |
| Usman        | Mathematics            | 80    | 84                 |
| Ayesha       | Mathematics            | 88    | 84                 |

The window function displays the average for each department while keeping all student records.

## 5. Understanding the OVER() Clause

The `OVER()` clause defines the window of rows used by a window function.

### Basic Syntax

```
SELECT
    column_name,
    window_function() OVER ()
FROM table_name;
```

Example:

```
SELECT
    student_name,
    marks,
    AVG(marks) OVER () AS overall_average
FROM students;
```

This calculates the average marks of all students and displays the same average alongside every student.

### Understanding OVER()

| Component      | Purpose                                   |
| -------------- | ----------------------------------------- |
| `OVER()`       | Defines the window                        |
| `PARTITION BY` | Divides rows into groups                  |
| `ORDER BY`     | Defines the order of rows                 |
| `ROWS`         | Defines a specific row-based window frame |

We will learn these components step by step.

## 6. PARTITION BY

`PARTITION BY` divides records into separate groups for window calculations.

For example, calculate the average marks of each department.

```
SELECT
    student_name,
    department,
    marks,
    AVG(marks) OVER (
        PARTITION BY department
    ) AS department_average
FROM students;
```

Understanding the query:

1. `AVG(marks)` calculates average marks.
2. `OVER()` defines the window.
3. `PARTITION BY department` divides students by department.
4. The average is calculated separately for each department.

Important: PARTITION BY does not remove individual rows. Every student remains in the result.

## 7. ORDER BY Inside OVER()

We can use `ORDER BY` inside `OVER()` to define the order in which rows are processed.

For example:

```
SELECT
    student_name,
    marks,
    ROW_NUMBER() OVER (
        ORDER BY marks DESC
    ) AS row_number
FROM students;
```

Expected output:

| student_name | marks | row_number |
| ------------ | ----- | ---------- |
| Hina         | 95    | 1          |
| Sara         | 90    | 2          |
| Ayesha       | 88    | 3          |
| Ali          | 85    | 4          |
| Zara         | 85    | 5          |
| Usman        | 80    | 6          |
| Ahmed        | 75    | 7          |
| Bilal        | 70    | 8          |

The highest marks receive row number 1.

Note: The query's final output order is not guaranteed unless an outer `ORDER BY` is specified. For predictable results, use:

```
SELECT
    student_name,
    marks,
    ROW_NUMBER() OVER (
        ORDER BY marks DESC, student_id
    ) AS row_number
FROM students
ORDER BY marks DESC, student_id;
```

## 8. ROW_NUMBER() Function

`ROW_NUMBER()` assigns a unique sequential number to each row within a window.

### Syntax

```
ROW_NUMBER() OVER (
    ORDER BY column_name
)
```

### Example: Assign Numbers to Students

```
SELECT
    student_name,
    department,
    marks,
    ROW_NUMBER() OVER (
        ORDER BY marks DESC, student_id
    ) AS row_number
FROM students
ORDER BY marks DESC, student_id;
```

This assigns a unique number to every student based on marks.

### ROW_NUMBER() with PARTITION BY

Suppose we want to assign numbers separately within each department.

```
SELECT
    student_name,
    department,
    marks,
    ROW_NUMBER() OVER (
        PARTITION BY department
        ORDER BY marks DESC, student_id
    ) AS row_number
FROM students
ORDER BY department, row_number;
```

Each department starts numbering from 1.

## 9. RANK() Function

`RANK()` assigns a rank to each row based on the specified ordering.

If two or more rows have the same value, they receive the same rank. The next rank is skipped.

### Syntax

```
RANK() OVER (
    ORDER BY column_name DESC
)
```

### Example

```
SELECT
    student_name,
    marks,
    RANK() OVER (
        ORDER BY marks DESC
    ) AS student_rank
FROM students
ORDER BY marks DESC;
```

Expected output:

| student_name | marks | student_rank |
| ------------ | ----- | ------------ |
| Hina         | 95    | 1            |
| Sara         | 90    | 2            |
| Ayesha       | 88    | 3            |
| Ali          | 85    | 4            |
| Zara         | 85    | 4            |
| Usman        | 80    | 6            |
| Ahmed        | 75    | 7            |
| Bilal        | 70    | 8            |

Notice that Ali and Zara both receive rank 4. The next rank is 6, not 5.

## 10. DENSE_RANK() Function

`DENSE_RANK()` also assigns ranks based on values.

However, unlike `RANK()`, it does not skip the next rank when two or more rows have the same value.

### Syntax

```
DENSE_RANK() OVER (
    ORDER BY column_name DESC
)
```

### Example

```
SELECT
    student_name,
    marks,
    DENSE_RANK() OVER (
        ORDER BY marks DESC
    ) AS dense_rank
FROM students
ORDER BY marks DESC;
```

Expected output:

| student_name | marks | dense_rank |
| ------------ | ----- | ---------- |
| Hina         | 95    | 1          |
| Sara         | 90    | 2          |
| Ayesha       | 88    | 3          |
| Ali          | 85    | 4          |
| Zara         | 85    | 4          |
| Usman        | 80    | 5          |
| Ahmed        | 75    | 6          |
| Bilal        | 70    | 7          |

## 11. Difference Between ROW_NUMBER(), RANK(), and DENSE_RANK()

These three functions are commonly used for ranking and numbering records.

| Function     | Same values receive same result? | Skips numbers? |
| ------------ | -------------------------------- | -------------- |
| ROW_NUMBER() | No                               | No             |
| RANK()       | Yes                              | Yes            |
| DENSE_RANK() | Yes                              | No             |

### Easy Example

Suppose the marks are:

```
95, 90, 85, 85, 80
```

The results will be:

| Marks | ROW_NUMBER | RANK | DENSE_RANK |
| ----- | ---------- | ---- | ---------- |
| 95    | 1          | 1    | 1          |
| 90    | 2          | 2    | 2          |
| 85    | 3          | 3    | 3          |
| 85    | 4          | 3    | 3          |
| 80    | 5          | 5    | 4          |

Remember:

- ROW_NUMBER gives every row a different number.
- RANK gives equal values equal ranks and skips the next rank.
- DENSE_RANK gives equal values equal ranks without skipping.

## 12. Aggregate Functions as Window Functions

We have already learned aggregate functions such as:

- COUNT()
- SUM()
- AVG()
- MIN()
- MAX()

We can also use these functions with `OVER()`.

### 12.1 COUNT() OVER()

Count the number of students in each department.

```
SELECT
    student_name,
    department,
    COUNT(*) OVER (
        PARTITION BY department
    ) AS total_students
FROM students;
```

### 12.2 SUM() OVER()

Calculate the total marks of each department.

```
SELECT
    student_name,
    department,
    marks,
    SUM(marks) OVER (
        PARTITION BY department
    ) AS department_total_marks
FROM students;
```

### 12.3 AVG() OVER()

Calculate the average marks of each department.

```
SELECT
    student_name,
    department,
    marks,
    AVG(marks) OVER (
        PARTITION BY department
    ) AS average_marks
FROM students;
```

### 12.4 MAX() OVER()

Display the highest marks in each department.

```
SELECT
    student_name,
    department,
    marks,
    MAX(marks) OVER (
        PARTITION BY department
    ) AS highest_marks
FROM students;
```

### 12.5 MIN() OVER()

Display the lowest marks in each department.

```
SELECT
    student_name,
    department,
    marks,
    MIN(marks) OVER (
        PARTITION BY department
    ) AS lowest_marks
FROM students;
```

## 13. Running Total Using SUM()

A running total is a continuously updated total calculated row by row.

For example, suppose we want to calculate the running total of student marks.

```
SELECT
    student_name,
    marks,
    SUM(marks) OVER (
        ORDER BY student_id
        ROWS BETWEEN UNBOUNDED PRECEDING
        AND CURRENT ROW
    ) AS running_total
FROM students
ORDER BY student_id;
```

Expected output:

| student_name | marks | running_total |
| ------------ | ----- | ------------- |
| Ali          | 85    | 85            |
| Sara         | 90    | 175           |
| Ahmed        | 75    | 250           |
| Hina         | 95    | 345           |
| Usman        | 80    | 425           |
| Ayesha       | 88    | 513           |
| Bilal        | 70    | 583           |
| Zara         | 85    | 668           |

Understanding the query:

- `ORDER BY student_id` defines the calculation order.
- `UNBOUNDED PRECEDING` starts from the first row.
- `CURRENT ROW` ends at the current row.
- `SUM(marks)` calculates the running total.

## 14. Understanding ROWS BETWEEN

The `ROWS BETWEEN` clause defines which rows are included in a window calculation.

Common options:

| Option                | Meaning                  |
| --------------------- | ------------------------ |
| `UNBOUNDED PRECEDING` | Start from the first row |
| `CURRENT ROW`         | Include the current row  |
| `UNBOUNDED FOLLOWING` | Continue to the last row |
| `1 PRECEDING`         | Include one previous row |
| `1 FOLLOWING`         | Include one next row     |

### Example: Sum of Current and Previous Row

```
SELECT
    student_name,
    marks,
    SUM(marks) OVER (
        ORDER BY student_id
        ROWS BETWEEN 1 PRECEDING
        AND CURRENT ROW
    ) AS recent_total
FROM students
ORDER BY student_id;
```

For each student, this calculates the sum of their marks and the previous student's marks, except for the first student who has no previous row.

## 15. LAG() Function

`LAG()` retrieves a value from a previous row.

For example, we want to compare each student's marks with the previous student's marks.

### Syntax

```
LAG(column_name) OVER (
    ORDER BY column_name
)
```

### Example

```
SELECT
    student_name,
    marks,
    LAG(marks) OVER (
        ORDER BY student_id
    ) AS previous_marks
FROM students
ORDER BY student_id;
```

Expected output:

| student_name | marks | previous_marks |
| ------------ | ----- | -------------- |
| Ali          | 85    | NULL           |
| Sara         | 90    | 85             |
| Ahmed        | 75    | 90             |
| Hina         | 95    | 75             |
| Usman        | 80    | 95             |
| Ayesha       | 88    | 80             |
| Bilal        | 70    | 88             |
| Zara         | 85    | 70             |

The first student has no previous row, so PostgreSQL returns NULL.

## 16. LEAD() Function

`LEAD()` retrieves a value from a following row.

For example:

```
SELECT
    student_name,
    marks,
    LEAD(marks) OVER (
        ORDER BY student_id
    ) AS next_student_marks
FROM students
ORDER BY student_id;
```

Expected output:

| student_name | marks | next_student_marks |
| ------------ | ----- | ------------------ |
| Ali          | 85    | 90                 |
| Sara         | 90    | 75                 |
| Ahmed        | 75    | 95                 |
| Hina         | 95    | 80                 |
| Usman        | 80    | 88                 |
| Ayesha       | 88    | 70                 |
| Bilal        | 70    | 85                 |
| Zara         | 85    | NULL               |

The last student has no following row, so PostgreSQL returns NULL.

### Difference Between LAG() and LEAD()

| LAG()                            | LEAD()                            |
| -------------------------------- | --------------------------------- |
| Retrieves a previous row's value | Retrieves a following row's value |
| Looks backward                   | Looks forward                     |

## 17. FIRST_VALUE() Function

`FIRST_VALUE()` returns the first value in the defined window frame.

Example: Display the highest marks in each department alongside every student.

```
SELECT
    student_name,
    department,
    marks,
    FIRST_VALUE(marks) OVER (
        PARTITION BY department
        ORDER BY marks DESC
    ) AS highest_marks
FROM students
ORDER BY department, marks DESC;
```

Because the rows are ordered by marks in descending order, the first value is the highest mark in each department.

## 18. LAST_VALUE() Function

`LAST_VALUE()` returns the last value in the defined window frame.

Example:

```
SELECT
    student_name,
    department,
    marks,
    LAST_VALUE(marks) OVER (
        PARTITION BY department
        ORDER BY marks DESC
        ROWS BETWEEN UNBOUNDED PRECEDING
        AND UNBOUNDED FOLLOWING
    ) AS lowest_marks
FROM students
ORDER BY department, marks DESC;
```

The complete window frame is specified so that LAST_VALUE returns the last mark in the entire department partition.

## 19. Using PARTITION BY with RANK()

Suppose we want to rank students separately within each department.

```
SELECT
    student_name,
    department,
    marks,
    RANK() OVER (
        PARTITION BY department
        ORDER BY marks DESC
    ) AS department_rank
FROM students
ORDER BY department, department_rank;
```

Expected output:

| student_name | department             | marks | department_rank |
| ------------ | ---------------------- | ----- | --------------- |
| Sara         | Computer Science       | 90    | 1               |
| Ali          | Computer Science       | 85    | 2               |
| Bilal        | Computer Science       | 70    | 3               |
| Hina         | Information Technology | 95    | 1               |
| Zara         | Information Technology | 85    | 2               |
| Ahmed        | Information Technology | 75    | 3               |
| Ayesha       | Mathematics            | 88    | 1               |
| Usman        | Mathematics            | 80    | 2               |

Each department starts its ranking from 1.

## 20. Named Windows Using WINDOW

PostgreSQL allows us to define a named window using the `WINDOW` clause.

This is useful when multiple window functions use the same window definition.

### Example

```
SELECT
    student_name,
    department,
    marks,
    AVG(marks) OVER department_window AS average_marks,
    RANK() OVER department_window AS department_rank
FROM students
WINDOW department_window AS (
    PARTITION BY department
    ORDER BY marks DESC
);
```

Here, `department_window` is a reusable window definition.

Both window functions use the same partitioning and ordering.

## 21. Window Functions vs GROUP BY

| Window Functions                     | GROUP BY                                              |
| ------------------------------------ | ----------------------------------------------------- |
| Keeps individual rows in the result  | Combines rows into groups                             |
| Uses `OVER()`                        | Uses `GROUP BY`                                       |
| Supports ranking and row comparisons | Commonly used for aggregate calculations              |
| Can calculate running totals         | Does not directly calculate row-by-row running totals |
| Can use `PARTITION BY`               | Groups by specified columns                           |

## 22. Important Points to Remember

1. Window functions perform calculations across related rows.
2. Window functions use the `OVER()` clause.
3. `PARTITION BY` divides rows into groups.
4. `ORDER BY` defines the order of rows in a window.
5. `ROW_NUMBER()` assigns unique row numbers.
6. `RANK()` assigns ranks and skips numbers after ties.
7. `DENSE_RANK()` assigns ranks without skipping numbers.
8. `SUM() OVER()` can calculate running totals.
9. `AVG() OVER()` calculates averages while keeping individual rows.
10. `LAG()` retrieves values from previous rows.
11. `LEAD()` retrieves values from following rows.
12. `FIRST_VALUE()` returns the first value in a window frame.
13. `LAST_VALUE()` returns the last value in a window frame.
14. Window functions are different from GROUP BY because they preserve individual rows.

## 23. Practice Exercises

### Beginner Level

1. Display all students with their row numbers based on student ID.
2. Assign a rank to all students based on marks in descending order.
3. Calculate the average marks of all students using `AVG() OVER()`.
4. Display each student's marks along with the highest marks in the entire table.
5. Count the number of students in each department using `COUNT() OVER()`.

### Intermediate Level

6. Assign row numbers separately within each department.
7. Calculate department-wise average marks without using GROUP BY.
8. Display the highest-ranking student in each department.
9. Use `RANK()` and `DENSE_RANK()` to compare student rankings.
10. Calculate a running total of student marks.
11. Display each student's marks alongside the previous student's marks using LAG().
12. Display each student's marks alongside the next student's marks using LEAD().

### Advanced Level

13. Find the top two students in each department using `ROW_NUMBER()`.
14. Find students who share the highest rank in their department using `RANK()`.
15. Calculate the difference between each student's marks and the previous student's marks.
16. Calculate a department-wise running total of marks using `PARTITION BY` and `ORDER BY`.
17. Use multiple window functions in a single SELECT statement.
18. Use a named window with the `WINDOW` clause.

## 24. Review Questions

1. What is a window function?
2. What is the purpose of the `OVER()` clause?
3. What is the difference between PARTITION BY and ORDER BY?
4. What is the difference between ROW_NUMBER() and RANK()?
5. What is the difference between RANK() and DENSE_RANK()?
6. Can we use AVG() as a window function?
7. What is a running total?
8. What is the purpose of ROWS BETWEEN?
9. What does LAG() do?
10. What does LEAD() do?
11. What is the difference between GROUP BY and window functions?
12. What is the purpose of the WINDOW clause?

## 25. Quick Revision

| Function / Keyword | Purpose                             |
| ------------------ | ----------------------------------- |
| `OVER()`           | Defines the window                  |
| `PARTITION BY`     | Divides rows into groups            |
| `ORDER BY`         | Defines row order                   |
| `ROW_NUMBER()`     | Assigns unique row numbers          |
| `RANK()`           | Assigns ranks with gaps             |
| `DENSE_RANK()`     | Assigns ranks without gaps          |
| `COUNT() OVER()`   | Counts rows in a window             |
| `SUM() OVER()`     | Calculates a sum over a window      |
| `AVG() OVER()`     | Calculates an average over a window |
| `LAG()`            | Retrieves a previous row's value    |
| `LEAD()`           | Retrieves a following row's value   |
| `FIRST_VALUE()`    | Returns the first value             |
| `LAST_VALUE()`     | Returns the last value              |
| `ROWS BETWEEN`     | Defines a row-based window frame    |
| `WINDOW`           | Defines a reusable named window     |

## 26. Next Lesson

Next Topic: PostgreSQL Date and Time Functions

Students will learn how to work with dates, times, timestamps, extract years and months, calculate date differences, and format date and time values using PostgreSQL.