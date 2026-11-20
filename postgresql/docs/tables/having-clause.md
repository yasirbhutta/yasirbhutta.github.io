# Student Notes: HAVING Clause in PostgreSQL

## 1. Introduction

In the previous lesson, we learned how to use the `GROUP BY` clause to group records and calculate results for each group.

Now imagine that a university wants to:

- Display only cities having more than two students.
- Display cities where the total fee is greater than 40,000.
- Display departments where the average salary is greater than 50,000.
- Display programs having at least 100 students.

To solve these problems, PostgreSQL provides the HAVING clause.

The `HAVING` clause is used to filter grouped results, usually after applying aggregate functions.

## 2. What is HAVING?

The `HAVING` clause filters groups created by the `GROUP BY` clause.

Syntax:

```
SELECT column_name, aggregate_function(column_name)
FROM table_name
GROUP BY column_name
HAVING condition;
```

Remember:

- `WHERE` filters individual rows.
- `GROUP BY` creates groups.
- `HAVING` filters those groups.

## 3. Prepare a Sample Table

We will use the `students` table from the previous lessons.

```
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    student_name VARCHAR(100),
    age INTEGER,
    city VARCHAR(50),
    fee NUMERIC(10, 2)
);
```

Insert sample records:

```
INSERT INTO students
(student_id, student_name, age, city, fee)
VALUES
(1, 'Ali', 20, 'Multan', 15000),
(2, 'Ahmed', 22, 'DG Khan', 18000),
(3, 'Sara', 21, 'Multan', 20000),
(4, 'Ayesha', 23, 'Lahore', 17000),
(5, 'Usman', 20, 'Lahore', 16000),
(6, 'Hassan', 22, 'DG Khan', 19000),
(7, 'Fatima', 21, 'Multan', 18000);
```

View all records:

```
SELECT * FROM students;
```

## 4. HAVING with COUNT()

Suppose we want to display only those cities that have more than two students.

SQL Query:

```
SELECT
    city,
    COUNT(*) AS total_students
FROM students
GROUP BY city
HAVING COUNT(*) > 2;
```

Output:

| city   | total_students |
| ------ | -------------- |
| Multan | 3              |

Explanation:

1. `GROUP BY city` groups students by city.
2. `COUNT(*)` counts students in each group.
3. `HAVING COUNT(*) > 2` displays only groups with more than two students.

## 5. HAVING with SUM()

Suppose we want to display only those cities where the total student fee is greater than 40,000.

SQL Query:

```
SELECT
    city,
    SUM(fee) AS total_fee
FROM students
GROUP BY city
HAVING SUM(fee) > 40000;
```

Output:

| city   | total_fee |
| ------ | --------- |
| Multan | 53000.00  |

Explanation:

- `SUM(fee)` calculates the total fee for each city.
- `HAVING SUM(fee) > 40000` filters the groups according to their total fee.

## 6. HAVING with AVG()

We can use `HAVING` to filter groups according to their average values.

Example: Display cities where the average student age is greater than 21.

```
SELECT
    city,
    AVG(age) AS average_age
FROM students
GROUP BY city
HAVING AVG(age) > 21;
```

Output:

| city    | average_age |
| ------- | ----------- |
| DG Khan | 22.0        |
| Lahore  | 21.5        |

## 7. HAVING with MIN() and MAX()

We can also use `HAVING` with minimum and maximum aggregate functions.

Example 1: Display cities where the minimum student fee is greater than 16,000.

```
SELECT
    city,
    MIN(fee) AS minimum_fee
FROM students
GROUP BY city
HAVING MIN(fee) > 16000;
```

Example 2: Display cities where the maximum student fee is greater than 18,000.

```
SELECT
    city,
    MAX(fee) AS maximum_fee
FROM students
GROUP BY city
HAVING MAX(fee) > 18000;
```

## 8. HAVING with Multiple Conditions

We can use `AND` and `OR` operators in the `HAVING` clause.

Example: Display cities having more than one student AND total fee greater than 35,000.

```
SELECT
    city,
    COUNT(*) AS total_students,
    SUM(fee) AS total_fee
FROM students
GROUP BY city
HAVING COUNT(*) > 1
AND SUM(fee) > 35000;
```

Explanation:

Both conditions must be true for a city to appear in the result.

## 9. WHERE and HAVING Together

We can use `WHERE` and `HAVING` in the same SQL query.

- `WHERE` filters individual records before grouping.
- `HAVING` filters groups after grouping.

Example:

Display cities having more than one student whose age is greater than 20.

```
SELECT
    city,
    COUNT(*) AS total_students
FROM students
WHERE age > 20
GROUP BY city
HAVING COUNT(*) > 1;
```

How this query works:

1. `WHERE age > 20` selects students older than 20.
2. `GROUP BY city` groups the selected students by city.
3. `COUNT(*)` counts students in each city.
4. `HAVING COUNT(*) > 1` displays cities with more than one selected student.

## 10. Difference Between WHERE and HAVING

| WHERE                                            | HAVING                                   |
| ------------------------------------------------ | ---------------------------------------- |
| Filters individual rows.                         | Filters groups.                          |
| Applied before grouping.                         | Applied after grouping.                  |
| Commonly used with individual column conditions. | Commonly used with aggregate conditions. |
| Does not directly filter aggregate results.      | Can filter aggregate results.            |

Example of WHERE:

```
SELECT *
FROM students
WHERE age > 20;
```

Example of HAVING:

```
SELECT city, COUNT(*)
FROM students
GROUP BY city
HAVING COUNT(*) > 2;
```

## 11. SQL Query Execution Order

Understanding the logical order of SQL clauses helps us understand how `WHERE`, `GROUP BY`, and `HAVING` work together.

A simplified logical processing order is:

1\. FROM

Select the table

2\. WHERE

Filter individual rows

3\. GROUP BY

Create groups

4\. HAVING

Filter groups

5\. SELECT

Choose output columns

6\. ORDER BY

Sort the results

7\. LIMIT

Restrict the number of output rows

## 12. Practice Exercises

Use the `students` table to solve the following exercises.

Beginner Level

1. Display cities having more than two students.
2. Display cities where the total fee is greater than 40,000.
3. Display cities where the average student age is greater than 21.
4. Display cities where the maximum fee is greater than 18,000.

Intermediate Level

5. Display cities having at least two students.
6. Display cities where the minimum fee is greater than 15,000.
7. Display cities where the total fee is greater than 30,000 and the number of students is greater than one.
8. Display cities having more than one student whose age is greater than 20.

Advanced Level

9. Display city-wise student count and total fee, but show only cities with total fees greater than 35,000.
10. Display city-wise average fee and sort the results from highest to lowest, showing only cities with an average fee greater than 17,000.
11. Display cities having at least two students and an average age greater than 20.

## 13. Review Questions

1. What is the purpose of the HAVING clause?
2. What is the difference between WHERE and HAVING?
3. Can we use HAVING with COUNT()?
4. Can we use HAVING with SUM()?
5. Why do we use GROUP BY with HAVING?
6. Can WHERE and HAVING be used in the same query?
7. What does `HAVING COUNT(*) > 2` mean?
8. Which clause filters groups after grouping?

## 14. Quick Revision

| Requirement              | SQL Condition             |
| ------------------------ | ------------------------- |
| More than 2 students     | `HAVING COUNT(*) > 2`     |
| Total fee above 40,000   | `HAVING SUM(fee) > 40000` |
| Average age above 21     | `HAVING AVG(age) > 21`    |
| Minimum fee above 15,000 | `HAVING MIN(fee) > 15000` |
| Maximum fee above 18,000 | `HAVING MAX(fee) > 18000` |

Basic HAVING pattern:

```
SELECT
    column_name,
    COUNT(*) AS total_records
FROM table_name
GROUP BY column_name
HAVING COUNT(*) > 2;
```
