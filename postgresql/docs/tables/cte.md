# Student Notes: Common Table Expressions (CTEs) in PostgreSQL

## 1. Introduction

Imagine you want to find students whose marks are greater than the average marks of all students.

You could write a query with a subquery. However, when queries become complex, they can become difficult to read and understand.

PostgreSQL provides Common Table Expressions (CTEs) to make complex SQL queries easier to organize and understand.

A CTE allows us to create a temporary named result that can be used within another SQL query.

## 2. What is a CTE?

CTE stands for Common Table Expression.

A CTE is a temporary named result set that exists only during the execution of a single SQL statement.

In simple words:

A CTE allows us to divide a complex SQL query into smaller, understandable parts.

CTEs are created using the `WITH` keyword.

### Basic Syntax

```
WITH cte_name AS (
    SELECT column1, column2
    FROM table_name
)
SELECT *
FROM cte_name;
```

Understanding the syntax:

| Keyword        | Purpose                      |
| -------------- | ---------------------------- |
| `WITH`         | Starts the CTE               |
| `cte_name`     | Name of the temporary result |
| `AS`           | Introduces the query         |
| `SELECT`       | Retrieves data for the CTE   |
| Final `SELECT` | Uses the CTE result          |

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
(2, 'Sara', 'Mathematics', 72),
(3, 'Ahmed', 'Computer Science', 65),
(4, 'Usman', 'Physics', 78),
(5, 'Hina', 'Mathematics', 90),
(6, 'Bilal', 'Physics', 55);
```

### Step 3: Display Records

```
SELECT *
FROM students;
```

Expected output:

| student_id | student_name | department       | marks |
| ---------- | ------------ | ---------------- | ----- |
| 1          | Ali          | Computer Science | 85    |
| 2          | Sara         | Mathematics      | 72    |
| 3          | Ahmed        | Computer Science | 65    |
| 4          | Usman        | Physics          | 78    |
| 5          | Hina         | Mathematics      | 90    |
| 6          | Bilal        | Physics          | 55    |

## 4. Create Your First CTE

Suppose we want to display students who have obtained more than 75 marks.

### Without CTE

```
SELECT *
FROM students
WHERE marks > 75;
```

### Using CTE

```
WITH high_marks AS (
    SELECT *
    FROM students
    WHERE marks > 75
)
SELECT *
FROM high_marks;
```

Expected output:

| student_id | student_name | department       | marks |
| ---------- | ------------ | ---------------- | ----- |
| 1          | Ali          | Computer Science | 85    |
| 4          | Usman        | Physics          | 78    |
| 5          | Hina         | Mathematics      | 90    |

Understanding the query:

1. `WITH` starts the CTE.
2. `high_marks` is the name of the CTE.
3. The inner SELECT retrieves students with marks greater than 75.
4. The final SELECT displays the CTE result.

## 5. CTE with Selected Columns

We do not always need to retrieve all columns.

For example, display only student names and marks of students who scored at least 80.

```
WITH high_marks AS (
    SELECT student_name, marks
    FROM students
    WHERE marks >= 80
)
SELECT *
FROM high_marks;
```

Expected output:

| student_name | marks |
| ------------ | ----- |
| Ali          | 85    |
| Hina         | 90    |

## 6. CTE with Aggregate Functions

We can use aggregate functions inside a CTE.

Suppose we want to calculate the average marks of all students.

```
WITH average_marks AS (
    SELECT AVG(marks) AS avg_marks
    FROM students
)
SELECT *
FROM average_marks;
```

Expected output:

| avg_marks |
| --------- |
| 74.1667   |

The CTE calculates the average marks and gives the result a name: `average_marks`.

## 7. CTE with WHERE Clause

We can use the result of a CTE in the WHERE clause of the final query.

Suppose we want to find students whose marks are greater than the average marks.

```
WITH average_marks AS (
    SELECT AVG(marks) AS avg_marks
    FROM students
)
SELECT *
FROM students
WHERE marks > (
    SELECT avg_marks
    FROM average_marks
);
```

Expected output:

| student_id | student_name | department       | marks |
| ---------- | ------------ | ---------------- | ----- |
| 1          | Ali          | Computer Science | 85    |
| 2          | Sara         | Mathematics      | 72    |
| 4          | Usman        | Physics          | 78    |
| 5          | Hina         | Mathematics      | 90    |

Correction to observe: The average is approximately 74.17, so Sara's 72 marks are not greater than the average. The correct output is:

| student_id | student_name | department       | marks |
| ---------- | ------------ | ---------------- | ----- |
| 1          | Ali          | Computer Science | 85    |
| 4          | Usman        | Physics          | 78    |
| 5          | Hina         | Mathematics      | 90    |

## 8. CTE with GROUP BY

CTEs can also be used with `GROUP BY`.

Suppose we want to calculate the average marks department-wise.

```
WITH department_average AS (
    SELECT
        department,
        AVG(marks) AS average_marks
    FROM students
    GROUP BY department
)
SELECT *
FROM department_average;
```

Expected output:

| department       | average_marks |
| ---------------- | ------------- |
| Computer Science | 75            |
| Mathematics      | 81            |
| Physics          | 66.5          |

This query first calculates department-wise averages and then displays the result.

## 9. CTE with HAVING

We can use `HAVING` inside a CTE to filter grouped results.

Suppose we want to display departments whose average marks are greater than 70.

```
WITH department_average AS (
    SELECT
        department,
        AVG(marks) AS average_marks
    FROM students
    GROUP BY department
    HAVING AVG(marks) > 70
)
SELECT *
FROM department_average;
```

Expected output:

| department       | average_marks |
| ---------------- | ------------- |
| Computer Science | 75            |
| Mathematics      | 81            |

## 10. CTE with JOIN

We can also use a CTE with JOIN to combine data from multiple tables.

### Step 1: Create a Departments Table

```
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);
```

### Step 2: Insert Records

```
INSERT INTO departments
VALUES
(1, 'Computer Science'),
(2, 'Mathematics'),
(3, 'Physics');
```

### Step 3: Use CTE with JOIN

Suppose we want to display students along with their department information.

```
WITH student_data AS (
    SELECT
        student_id,
        student_name,
        department,
        marks
    FROM students
)
SELECT
    student_data.student_name,
    departments.department_id,
    student_data.department,
    student_data.marks
FROM student_data
INNER JOIN departments
ON student_data.department = departments.department_name;
```

The CTE first prepares student data. The final query joins that result with the departments table.

## 11. Multiple CTEs in One Query

PostgreSQL allows us to define multiple CTEs in a single query.

For example, calculate the average marks and then retrieve students who scored above that average.

```
WITH average_marks AS (
    SELECT AVG(marks) AS avg_marks
    FROM students
),
high_performers AS (
    SELECT *
    FROM students
    WHERE marks > (
        SELECT avg_marks
        FROM average_marks
    )
)
SELECT *
FROM high_performers;
```

Understanding the query:

1. `average_marks` calculates the average marks.
2. `high_performers` selects students above that average.
3. The final SELECT displays the high-performing students.

Multiple CTEs are separated by commas.

## 12. CTE vs Subquery

Both CTEs and subqueries can help solve complex SQL problems.

However, their structure and readability are different.

### Using a Subquery

```
SELECT *
FROM students
WHERE marks > (
    SELECT AVG(marks)
    FROM students
);
```

### Using a CTE

```
WITH average_marks AS (
    SELECT AVG(marks) AS avg_marks
    FROM students
)
SELECT *
FROM students
WHERE marks > (
    SELECT avg_marks
    FROM average_marks
);
```

### Difference

| CTE                               | Subquery                                       |
| --------------------------------- | ---------------------------------------------- |
| Uses the `WITH` keyword           | Written inside another query                   |
| Has a temporary name              | Usually has no independent name                |
| Can improve readability           | Can become difficult to read when nested       |
| Can define multiple named results | Can use nested queries                         |
| Exists for one SQL statement      | Exists within the query in which it is written |

## 13. Recursive CTE

A recursive CTE is a special type of CTE that refers to its own result.

It is useful for working with hierarchical data, such as:

- Employee and manager relationships.
- University organizational structures.
- Category and subcategory relationships.
- Tree structures.

### Example: Generate Numbers from 1 to 5

```
WITH RECURSIVE number_list AS (

    SELECT 1 AS number

    UNION ALL

    SELECT number + 1
    FROM number_list
    WHERE number < 5

)
SELECT *
FROM number_list;
```

Expected output:

| number |
| ------ |
| 1      |
| 2      |
| 3      |
| 4      |
| 5      |

Understanding the query:

A recursive CTE has two main parts.

1\. Initial Query (Anchor)

```
SELECT 1 AS number
```

This starts the process with the number 1.

2\. Recursive Query

```
SELECT number + 1
FROM number_list
WHERE number < 5
```

This adds 1 to the previous result until the condition becomes false.

3\. UNION ALL

Combines the initial result with the results generated by the recursive query.

4\. WITH RECURSIVE

Tells PostgreSQL that the CTE can refer to itself.

## 14. CTE with INSERT

A CTE can also be used with INSERT statements.

For example, insert students with marks greater than or equal to 80 into a separate table.

### Step 1: Create a New Table

```
CREATE TABLE top_students (
    student_id INT,
    student_name VARCHAR(50),
    marks INT
);
```

### Step 2: Insert Using CTE

```
WITH selected_students AS (
    SELECT student_id, student_name, marks
    FROM students
    WHERE marks >= 80
)
INSERT INTO top_students
SELECT *
FROM selected_students;
```

### Step 3: Display the New Table

```
SELECT *
FROM top_students;
```

Expected output:

| student_id | student_name | marks |
| ---------- | ------------ | ----- |
| 1          | Ali          | 85    |
| 5          | Hina         | 90    |

## 15. CTE with UPDATE

A CTE can also help identify records that need to be updated.

For example, increase marks by 5 for students whose marks are below 70.

```
WITH low_marks AS (
    SELECT student_id
    FROM students
    WHERE marks < 70
)
UPDATE students
SET marks = marks + 5
WHERE student_id IN (
    SELECT student_id
    FROM low_marks
);
```

This query:

1. Finds students with marks below 70.
2. Stores their IDs in the CTE.
3. Increases their marks by 5.

## 16. CTE with DELETE

We can also use a CTE to identify records for deletion.

For example, delete students whose marks are below 60.

```
WITH low_marks AS (
    SELECT student_id
    FROM students
    WHERE marks < 60
)
DELETE FROM students
WHERE student_id IN (
    SELECT student_id
    FROM low_marks
);
```

This query first identifies students with marks below 60 and then deletes their records.

Important: Always check the records selected by a CTE before using it with UPDATE or DELETE.

## 17. Important Points to Remember

1. CTE stands for Common Table Expression.
2. CTEs are created using the `WITH` keyword.
3. A CTE is a temporary named result set.
4. A CTE exists only during the execution of one SQL statement.
5. We can use SELECT, INSERT, UPDATE, and DELETE with CTEs.
6. Multiple CTEs can be defined in one query.
7. CTEs improve query organization and readability.
8. Recursive CTEs are useful for hierarchical and sequential data.
9. `WITH RECURSIVE` is used for recursive CTEs.
10. A CTE is not a permanent database table.

## 18. Practice Exercises

### Beginner Level

1. Create a CTE named `high_marks` to display students with marks greater than 80.
2. Create a CTE to display only student names and departments.
3. Create a CTE to calculate the average marks of all students.
4. Create a CTE to display students whose marks are greater than the average marks.

### Intermediate Level

5. Create a CTE to calculate department-wise average marks.
6. Display departments whose average marks are greater than 75.
7. Create two CTEs: one to calculate average marks and another to find students above average.
8. Use a CTE with JOIN to display student names and department IDs.

### Advanced Level

9. Write a recursive CTE to generate numbers from 1 to 20.
10. Use a CTE to insert students with marks greater than 85 into a new table.
11. Use a CTE to increase marks by 10 for students whose marks are below 60.
12. Create a recursive CTE to display an employee reporting hierarchy.

## 19. Review Questions

1. What is a Common Table Expression?
2. What is the purpose of the `WITH` keyword?
3. What is the difference between a CTE and a subquery?
4. Can we create multiple CTEs in one query?
5. How long does a CTE exist?
6. Can we use aggregate functions inside a CTE?
7. Can we use JOIN with a CTE?
8. What is a recursive CTE?
9. What is the purpose of `WITH RECURSIVE`?
10. Can we use CTEs with INSERT, UPDATE, and DELETE?

## 20. Quick Revision

| Concept          | Description                                |
| ---------------- | ------------------------------------------ |
| CTE              | Common Table Expression                    |
| `WITH`           | Starts a CTE                               |
| `AS`             | Defines the CTE query                      |
| CTE Name         | Name of the temporary result               |
| Multiple CTEs    | Multiple named results separated by commas |
| Recursive CTE    | CTE that refers to itself                  |
| `WITH RECURSIVE` | Creates a recursive CTE                    |
| Anchor Query     | Initial result of a recursive CTE          |
| Recursive Query  | Generates subsequent results               |
| `UNION ALL`      | Combines recursive results                 |

## 21. Next Lesson

Next Topic: Window Functions in PostgreSQL

Students will learn how to use `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`, `OVER()`, and `PARTITION BY` to perform calculations across related rows without grouping them into a single result.