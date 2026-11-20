# Student Notes: JOINS in PostgreSQL

## 1. Introduction

In a relational database, information is usually stored in multiple tables rather than one large table.

For example, a university may maintain separate tables for:

- Students
- Departments
- Teachers
- Courses
- Enrollments

Sometimes we need information from more than one table.

For example:

- Display student names with their department names.
- Display course names with teacher names.
- Display students with their enrolled courses.
- Find departments that have no students.

PostgreSQL provides JOINs to retrieve related information from multiple tables.

## 2. What is a JOIN?

A JOIN is used to combine related rows from two or more tables based on a common column.

Consider these two tables:

students

| student_id | student_name | department_id |
| ---------- | ------------ | ------------- |
| 1          | Ali          | 101           |
| 2          | Sara         | 102           |
| 3          | Ahmed        | 101           |
| 4          | Ayesha       | 103           |

departments

| department_id | department_name  |
| ------------- | ---------------- |
| 101           | Computer Science |
| 102           | Mathematics      |
| 103           | Physics          |

The `department_id` column is common to both tables.

Using JOIN, we can combine student information with department information.

## 3. Prepare Sample Tables

First, create the `departments` table.

```
CREATE TABLE departments (
    department_id INTEGER PRIMARY KEY,
    department_name VARCHAR(100)
);
```

Insert department records:

```
INSERT INTO departments
(department_id, department_name)
VALUES
(101, 'Computer Science'),
(102, 'Mathematics'),
(103, 'Physics'),
(104, 'Chemistry');
```

Now create the `students` table.

```
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    student_name VARCHAR(100),
    department_id INTEGER,
    age INTEGER,
    FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);
```

Insert student records:

```
INSERT INTO students
(student_id, student_name, department_id, age)
VALUES
(1, 'Ali', 101, 20),
(2, 'Sara', 102, 21),
(3, 'Ahmed', 101, 22),
(4, 'Ayesha', 103, 23);
```

Notice that the Chemistry department (104) has no students.

## 4. Types of JOINs in PostgreSQL

PostgreSQL supports several types of JOINs.

| JOIN            | Purpose                                                                            |
| --------------- | ---------------------------------------------------------------------------------- |
| INNER JOIN      | Returns matching records from both tables.                                         |
| LEFT JOIN       | Returns all records from the left table and matching records from the right table. |
| RIGHT JOIN      | Returns all records from the right table and matching records from the left table. |
| FULL OUTER JOIN | Returns all records from both tables, matching where possible.                     |
| CROSS JOIN      | Returns every possible combination of rows from both tables.                       |

## 5. INNER JOIN

An `INNER JOIN` returns only those records that have matching values in both tables.

Syntax:

```
SELECT columns
FROM table1
INNER JOIN table2
ON table1.common_column = table2.common_column;
```

Example: Display student names with department names.

```
SELECT
    students.student_name,
    departments.department_name
FROM students
INNER JOIN departments
ON students.department_id = departments.department_id;
```

Output:

| student_name | department_name  |
| ------------ | ---------------- |
| Ali          | Computer Science |
| Sara         | Mathematics      |
| Ahmed        | Computer Science |
| Ayesha       | Physics          |

Explanation:

1. `FROM students` selects the first table.
2. `INNER JOIN departments` joins the departments table.
3. `ON` specifies the matching condition.
4. Only records with matching department IDs appear.

The Chemistry department does not appear because it has no matching student.

## 6. LEFT JOIN

A `LEFT JOIN` returns:

- All records from the left table.
- Matching records from the right table.
- `NULL` values when no matching record exists in the right table.

Syntax:

```
SELECT columns
FROM table1
LEFT JOIN table2
ON table1.common_column = table2.common_column;
```

Example: Display all departments with their students.

```
SELECT
    departments.department_name,
    students.student_name
FROM departments
LEFT JOIN students
ON departments.department_id = students.department_id;
```

Output:

| department_name  | student_name |
| ---------------- | ------------ |
| Computer Science | Ali          |
| Computer Science | Ahmed        |
| Mathematics      | Sara         |
| Physics          | Ayesha       |
| Chemistry        | NULL         |

Explanation:

- All four departments appear in the result.
- The Chemistry department has no students.
- PostgreSQL displays `NULL` for its student name.

## 7. RIGHT JOIN

A `RIGHT JOIN` returns:

- All records from the right table.
- Matching records from the left table.
- `NULL` values when no matching record exists in the left table.

Example: Display all departments with their students using RIGHT JOIN.

```
SELECT
    departments.department_name,
    students.student_name
FROM students
RIGHT JOIN departments
ON students.department_id = departments.department_id;
```

The result includes all departments, including Chemistry, even though it has no students.

Important: The right table is the table written after `RIGHT JOIN`.

## 8. FULL OUTER JOIN

A `FULL OUTER JOIN` returns all records from both tables.

It includes:

- Matching records from both tables.
- Unmatched records from the left table.
- Unmatched records from the right table.

Example:

```
SELECT
    students.student_name,
    departments.department_name
FROM students
FULL OUTER JOIN departments
ON students.department_id = departments.department_id;
```

In our sample data, all students have matching departments, but Chemistry has no students. Therefore, Chemistry appears with a `NULL` student name.

If either table has unmatched records, those records also appear in the result.

## 9. CROSS JOIN

A `CROSS JOIN` returns every possible combination of rows from two tables.

This is also called the Cartesian Product.

Syntax:

```
SELECT columns
FROM table1
CROSS JOIN table2;
```

Example:

```
SELECT
    students.student_name,
    departments.department_name
FROM students
CROSS JOIN departments;
```

We have:

- 4 student records.
- 4 department records.

The result contains:

\\[ 4 \times 4 = 16 \text{ rows} \\]

Explanation: Each student is combined with every department, regardless of the department ID.

## 10. Using Table Aliases with JOIN

A table alias is a short temporary name given to a table inside a query.

It makes SQL queries shorter and easier to read.

Example:

```
SELECT
    s.student_name,
    d.department_name
FROM students AS s
INNER JOIN departments AS d
ON s.department_id = d.department_id;
```

Here:

- `s` is the alias for `students`.
- `d` is the alias for `departments`.

We can use these aliases instead of writing full table names.

## 11. JOIN with WHERE

We can combine JOIN with the `WHERE` clause to filter the joined results.

Example: Display students belonging to the Computer Science department.

```
SELECT
    s.student_name,
    d.department_name
FROM students AS s
INNER JOIN departments AS d
ON s.department_id = d.department_id
WHERE d.department_name = 'Computer Science';
```

Output:

| student_name | department_name  |
| ------------ | ---------------- |
| Ali          | Computer Science |
| Ahmed        | Computer Science |

## 12. JOIN with ORDER BY

We can use `ORDER BY` to sort the results of a JOIN query.

Example: Display students and their departments in alphabetical order of student names.

```
SELECT
    s.student_name,
    d.department_name
FROM students AS s
INNER JOIN departments AS d
ON s.department_id = d.department_id
ORDER BY s.student_name ASC;
```

## 13. Difference Between JOIN Types

| JOIN Type       | What does it return?                                    |
| --------------- | ------------------------------------------------------- |
| INNER JOIN      | Only matching records from both tables                  |
| LEFT JOIN       | All left-table records and matching right-table records |
| RIGHT JOIN      | All right-table records and matching left-table records |
| FULL OUTER JOIN | All records from both tables                            |
| CROSS JOIN      | Every possible combination of rows                      |

## 14. Visual Understanding of JOINs

INNER JOIN

Only the overlapping records.

LEFT JOIN

All of A and matching records from B.

RIGHT JOIN

All of B and matching records from A.

FULL OUTER JOIN

All records from both A and B.

Green areas represent the records included in each JOIN. CROSS JOIN is different: it creates every possible row combination.

## 15. Common Mistakes to Avoid

1. Forgetting the ON condition: Most JOINs need a matching condition.
2. Using the wrong columns: Join columns should represent related information.
3. Ambiguous column names: If both tables have a column named `department_id`, specify the table or alias, such as `s.department_id`.
4. Confusing LEFT and RIGHT: The position of the table determines which records are preserved.
5. Unexpected duplicate rows: A matching value may occur multiple times, producing multiple result rows.

## 16. Practice Exercises

Use the `students` and `departments` tables created in this lesson.

Beginner Level

1. Display student names with their department names using INNER JOIN.
2. Display all departments with their student names using LEFT JOIN.
3. Display all departments using RIGHT JOIN.
4. Display all records from both tables using FULL OUTER JOIN.
5. Display every possible combination of students and departments using CROSS JOIN.

Intermediate Level

6. Display students belonging to the Mathematics department.
7. Display student names and department names in alphabetical order.
8. Display only students older than 20 with their department names.
9. Display all departments and count their students, including departments with zero students.

Hint for Exercise 9: Use `LEFT JOIN`, `COUNT()`, and `GROUP BY`.

Advanced Level

10. Display the total number of students in each department.
11. Display departments having more than one student.
12. Display department names and average student age.
13. Display departments with no students.

Hint for Exercise 13: Use `LEFT JOIN` with `WHERE students.student_id IS NULL`.

## 17. Review Questions

1. What is a JOIN in PostgreSQL?
2. Why do we use JOINs?
3. What is the difference between INNER JOIN and LEFT JOIN?
4. What is the purpose of RIGHT JOIN?
5. What does FULL OUTER JOIN return?
6. What is a CROSS JOIN?
7. What is the purpose of the ON clause?
8. What is a table alias?
9. Can we use WHERE with JOIN?
10. Why might a JOIN query return duplicate rows?

## 18. Quick Revision

Remember these basic JOIN patterns:

```
-- INNER JOIN
SELECT *
FROM students s
INNER JOIN departments d
ON s.department_id = d.department_id;

-- LEFT JOIN
SELECT *
FROM students s
LEFT JOIN departments d
ON s.department_id = d.department_id;

-- RIGHT JOIN
SELECT *
FROM students s
RIGHT JOIN departments d
ON s.department_id = d.department_id;

-- FULL OUTER JOIN
SELECT *
FROM students s
FULL OUTER JOIN departments d
ON s.department_id = d.department_id;

-- CROSS JOIN
SELECT *
FROM students s
CROSS JOIN departments d;
```

## 19. Next Lesson

SELF JOIN in PostgreSQL
