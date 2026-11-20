# Student Notes: Subqueries in PostgreSQL

## 1. Introduction

In a database, sometimes we need to use the result of one query to complete another query.

For example, a university wants to find students whose fees are higher than the average fee of all students.

To solve this problem, we need two steps:

1. Calculate the average fee of all students.
2. Find students whose fees are greater than that average.

Instead of running two separate queries manually, we can write one query inside another query.

This is called a Subquery.

## 2. What is a Subquery?

A subquery is a SQL query written inside another SQL query.

The inner query provides a result that the outer query uses.

Basic syntax:

```
SELECT column_name
FROM table_name
WHERE column_name operator (
    SELECT column_name
    FROM table_name
);
```

Remember:

- Inner query: The query inside another query.
- Outer query: The main query that uses the result of the inner query.

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
(6, 'Hassan', 22, 'DG Khan', 25000);
```

View all records:

```
SELECT * FROM students;
```

## 4. Simple Subquery Example

Suppose we want to find students whose fees are greater than the average fee.

Step 1: Calculate the average fee.

```
SELECT AVG(fee)
FROM students;
```

Result:

```
18500
```

Step 2: Find students whose fees are greater than 18,500.

```
SELECT *
FROM students
WHERE fee > 18500;
```

Step 3: Combine both queries using a subquery.

```
SELECT *
FROM students
WHERE fee > (
    SELECT AVG(fee)
    FROM students
);
```

Output:

| student_id | student_name | age | city    | fee   |
| ---------- | ------------ | --- | ------- | ----- |
| 3          | Sara         | 21  | Multan  | 20000 |
| 6          | Hassan       | 22  | DG Khan | 25000 |

Explanation:

1. The inner query calculates the average fee.
2. The outer query selects students whose fees are greater than that average.
3. The final result displays Sara and Hassan.

## 5. Subquery with MAX()

Suppose we want to find the student who pays the highest fee.

SQL Query:

```
SELECT *
FROM students
WHERE fee = (
    SELECT MAX(fee)
    FROM students
);
```

Output:

| student_id | student_name | fee   |
| ---------- | ------------ | ----- |
| 6          | Hassan       | 25000 |

Explanation:

- The inner query finds the maximum fee.
- The outer query finds the student whose fee matches that value.

## 6. Subquery with MIN()

Suppose we want to find the student who pays the lowest fee.

```
SELECT *
FROM students
WHERE fee = (
    SELECT MIN(fee)
    FROM students
);
```

Output:

| student_id | student_name | fee   |
| ---------- | ------------ | ----- |
| 1          | Ali          | 15000 |

The inner query finds the lowest fee, and the outer query retrieves the matching student record.

## 7. Subquery with IN Operator

The `IN` operator checks whether a value matches any value in a list or the result of a subquery.

Example: Find students who belong to cities where at least one student is older than 21.

```
SELECT *
FROM students
WHERE city IN (
    SELECT city
    FROM students
    WHERE age > 21
);
```

Explanation:

1. The inner query finds the cities of students older than 21.
2. The outer query finds all students belonging to those cities.

In our sample data, the cities are DG Khan and Lahore.

## 8. Subquery with NOT IN

The `NOT IN` operator selects values that do not match any value returned by the subquery.

Example: Find students who do not belong to cities where a student is older than 21.

```
SELECT *
FROM students
WHERE city NOT IN (
    SELECT city
    FROM students
    WHERE age > 21
);
```

Output:

| student_name | city   |
| ------------ | ------ |
| Ali          | Multan |
| Sara         | Multan |

Important: If a `NOT IN` subquery returns NULL, the result may be unexpected. In such cases, use `NOT EXISTS` or filter out NULL values.

## 9. Subquery with Comparison Operators

We can use comparison operators with subqueries.

| Operator | Meaning                  |
| -------- | ------------------------ |
| `=`      | Equal to                 |
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |
| `<>`     | Not equal to             |

Example: Find students whose age is greater than the average age.

```
SELECT *
FROM students
WHERE age > (
    SELECT AVG(age)
    FROM students
);
```

The inner query calculates the average age, and the outer query finds students older than that average.

## 10. Subquery with EXISTS

The `EXISTS` operator checks whether a subquery returns at least one row.

It returns TRUE if at least one matching row exists.

Suppose we have two tables:

- `students`
- `departments`

We want to find departments that have at least one student.

```
SELECT *
FROM departments d
WHERE EXISTS (
    SELECT 1
    FROM students s
    WHERE s.department_id = d.department_id
);
```

Explanation:

1. The outer query selects departments.
2. The inner query checks whether a student belongs to each department.
3. `EXISTS` returns TRUE when a matching student is found.
4. Only departments with students are displayed.

## 11. Types of Subqueries

Subqueries can be classified according to the number of rows and columns they return and how they relate to the outer query.

| Type                     | Description                             |
| ------------------------ | --------------------------------------- |
| Single-row subquery      | Returns one row.                        |
| Multiple-row subquery    | Returns multiple rows.                  |
| Single-column subquery   | Returns one column.                     |
| Multiple-column subquery | Returns multiple columns.               |
| Correlated subquery      | Depends on values from the outer query. |

A subquery may belong to more than one of these categories.

## 12. What is a Correlated Subquery?

A correlated subquery is an inner query that depends on the outer query.

Unlike a simple subquery, it refers to a column from the outer query.

Example:

Find students whose fees are greater than the average fee of students in their own city.

```
SELECT
    s1.student_name,
    s1.city,
    s1.fee
FROM students s1
WHERE s1.fee > (
    SELECT AVG(s2.fee)
    FROM students s2
    WHERE s2.city = s1.city
);
```

Explanation:

1. The outer query selects a student.
2. The inner query calculates the average fee for that student's city.
3. The outer query compares the student's fee with the city average.
4. This process is evaluated for each student.

For example, Sara's fee is compared with the average fee of students from Multan.

## 13. Difference Between JOIN and Subquery

| JOIN                                             | Subquery                                                    |
| ------------------------------------------------ | ----------------------------------------------------------- |
| Combines related records from multiple tables.   | Uses the result of one query inside another query.          |
| Commonly retrieves columns from multiple tables. | Commonly filters or calculates results using another query. |
| Uses JOIN and ON conditions.                     | Uses a nested SELECT statement.                             |

Both can solve some of the same database problems. The best choice depends on the query and its readability.

## 14. Practice Exercises

Use the `students` table to solve the following exercises.

Beginner Level

1. Find students whose fees are greater than the average fee.
2. Find the student who pays the highest fee.
3. Find the student who pays the lowest fee.
4. Find students whose age is greater than the average age.
5. Find students whose fees are less than the average fee.

Intermediate Level

6. Find students who belong to cities where at least one student is older than 21.
7. Find students whose fees are equal to the highest fee.
8. Find students whose cities are not included in the cities of students older than 21.
9. Find departments that have at least one student using `EXISTS`.

Advanced Level

10. Find students whose fees are greater than the average fee of their own city.
11. Find students whose ages are greater than the average age of their own city.
12. Find students whose fees are greater than the minimum fee paid in their own city.

## 15. Review Questions

1. What is a subquery?
2. What is the difference between an inner query and an outer query?
3. Can we use aggregate functions inside a subquery?
4. What is the purpose of the `IN` operator?
5. What is the difference between `IN` and `NOT IN`?
6. What does the `EXISTS` operator check?
7. What is a correlated subquery?
8. How is a JOIN different from a subquery?

## 16. Quick Revision

Find students with fees greater than the average fee:

```
SELECT *
FROM students
WHERE fee > (
    SELECT AVG(fee)
    FROM students
);
```

Find the student with the highest fee:

```
SELECT *
FROM students
WHERE fee = (
    SELECT MAX(fee)
    FROM students
);
```

Find students from cities where at least one student is older than 21:

```
SELECT *
FROM students
WHERE city IN (
    SELECT city
    FROM students
    WHERE age > 21
);
```

## 17. Next Lesson

UNION and UNION ALL in PostgreSQL

Learn how to combine the results of two or more SELECT queries into a single result set.