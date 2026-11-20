# Student Notes: UNION and UNION ALL in PostgreSQL

## 1. Introduction

Imagine a university has two separate student lists:

- Current Students
- Former Students

You want to combine both lists into one result.

In PostgreSQL, we can use UNION and UNION ALL to combine the results of multiple `SELECT` statements.

Both operators combine records vertically (one result below another).

## 2. What is UNION?

The `UNION` operator combines the results of two or more `SELECT` statements and removes duplicate rows.

Syntax:

```
SELECT column1, column2
FROM table1

UNION

SELECT column1, column2
FROM table2;
```

Important: UNION removes duplicate rows from the combined result.

## 3. What is UNION ALL?

The `UNION ALL` operator also combines the results of two or more `SELECT` statements, but it keeps duplicate rows.

Syntax:

```
SELECT column1, column2
FROM table1

UNION ALL

SELECT column1, column2
FROM table2;
```

Important: UNION ALL does not remove duplicate rows.

## 4. Create Sample Tables

Let's create two tables for university students.

Table 1: Current Students

```
CREATE TABLE current_students (
    student_id INT,
    student_name VARCHAR(50),
    city VARCHAR(50)
);
```

Insert records:

```
INSERT INTO current_students
VALUES
    (1, 'Ali', 'Multan'),
    (2, 'Sara', 'Lahore'),
    (3, 'Ahmed', 'DG Khan');
```

Table 2: Former Students

```
CREATE TABLE former_students (
    student_id INT,
    student_name VARCHAR(50),
    city VARCHAR(50)
);
```

Insert records:

```
INSERT INTO former_students
VALUES
    (2, 'Sara', 'Lahore'),
    (4, 'Usman', 'Multan'),
    (5, 'Ayesha', 'Karachi');
```

## 5. Using UNION

Let's combine both student tables using UNION.

```
SELECT student_id, student_name, city
FROM current_students

UNION

SELECT student_id, student_name, city
FROM former_students;
```

Expected output:

| student_id | student_name | city    |
| ---------- | ------------ | ------- |
| 1          | Ali          | Multan  |
| 2          | Sara         | Lahore  |
| 3          | Ahmed        | DG Khan |
| 4          | Usman        | Multan  |
| 5          | Ayesha       | Karachi |

Explanation:

- PostgreSQL retrieves records from both tables.
- It combines the records into one result.
- The duplicate record of Sara is included only once.
- The result contains five unique rows.

## 6. Using UNION ALL

Now combine the same tables using UNION ALL.

```
SELECT student_id, student_name, city
FROM current_students

UNION ALL

SELECT student_id, student_name, city
FROM former_students;
```

Expected output:

| student_id | student_name | city    |
| ---------- | ------------ | ------- |
| 1          | Ali          | Multan  |
| 2          | Sara         | Lahore  |
| 3          | Ahmed        | DG Khan |
| 2          | Sara         | Lahore  |
| 4          | Usman        | Multan  |
| 5          | Ayesha       | Karachi |

Explanation:

- PostgreSQL retrieves records from both tables.
- It combines all records.
- The duplicate record of Sara appears twice.
- The result contains six rows.

## 7. Difference Between UNION and UNION ALL

| UNION                             | UNION ALL                                            |
| --------------------------------- | ---------------------------------------------------- |
| Combines multiple SELECT results  | Combines multiple SELECT results                     |
| Removes duplicate rows            | Keeps duplicate rows                                 |
| Returns unique rows               | Returns all rows                                     |
| Usually requires extra processing | Usually faster because it does not remove duplicates |

Visual Understanding

CURRENT STUDENTS (3 ROWS)

Ali

Sara

Ahmed

FORMER STUDENTS (3 ROWS)

Sara

Usman

Ayesha

UNION

# 5

Unique rows

UNION ALL

# 6

All rows, including duplicate

## 8. Rules for Using UNION and UNION ALL

When combining SELECT statements, follow these rules:

Rule 1: Same number of columns

Both SELECT statements must return the same number of columns.

Correct:

```
SELECT student_id, student_name
FROM current_students

UNION

SELECT student_id, student_name
FROM former_students;
```

Incorrect:

```
SELECT student_id, student_name
FROM current_students

UNION

SELECT student_id
FROM former_students;
```

Rule 2: Compatible data types

Corresponding columns must have compatible data types.

For example, an integer column should be combined with another integer-compatible column.

Rule 3: Same column order

The columns must appear in the same logical order.

```
SELECT student_id, student_name
FROM current_students

UNION

SELECT student_id, student_name
FROM former_students;
```

Rule 4: Column names come from the first SELECT

The resulting column names are based on the first SELECT statement.

## 9. Using ORDER BY with UNION

We can sort the combined result using `ORDER BY`.

For example, display students alphabetically by name.

```
SELECT student_id, student_name, city
FROM current_students

UNION

SELECT student_id, student_name, city
FROM former_students

ORDER BY student_name;
```

Important: Write `ORDER BY` after the final SELECT statement. It sorts the combined result, not each individual table separately.

## 10. UNION vs JOIN

Students often confuse UNION with JOIN.

Both combine data, but they work differently.

UNION: Combines rows vertically

```
SELECT student_name
FROM current_students

UNION

SELECT student_name
FROM former_students;
```

The results are placed one below another.

JOIN: Combines columns horizontally

For example, suppose we have two tables:

`students`

| student_id | student_name |
| ---------- | ------------ |
| 1          | Ali          |
| 2          | Sara         |

`departments`

| student_id | department       |
| ---------- | ---------------- |
| 1          | Computer Science |
| 2          | Mathematics      |

Query:

```
SELECT
    students.student_name,
    departments.department
FROM students
JOIN departments
ON students.student_id = departments.student_id;
```

Result:

| student_name | department       |
| ------------ | ---------------- |
| Ali          | Computer Science |
| Sara         | Mathematics      |

Remember:

- UNION combines rows vertically.
- JOIN combines columns horizontally.

## 11. Common Mistakes

Mistake 1: Different number of columns

Both SELECT statements must return the same number of columns.

Mistake 2: Incompatible data types

Corresponding columns must have compatible data types.

Mistake 3: Expecting UNION to remove duplicates based on one column only

UNION removes duplicate complete rows based on all selected columns.

For example:

```
SELECT student_id, student_name
FROM current_students

UNION

SELECT student_id, student_name
FROM former_students;
```

If two rows have the same student name but different student IDs, both rows remain in the result.

## 12. Practice Exercises

Use the `current_students` and `former_students` tables created in this lesson.

### Beginner Level

1. Display all student names from both tables using UNION.
2. Display all student names using UNION ALL.
3. Combine student IDs and names from both tables using UNION.
4. Sort the combined student list alphabetically.

### Intermediate Level

5. Combine student names and cities from both tables using UNION.
6. Use UNION ALL to display all records from both tables.
7. Count the total number of rows returned by UNION ALL.
8. Count the number of unique rows returned by UNION.

### Advanced Level

9. Create a third table named `new_students` and insert three records. Combine all three tables using UNION.
10. Combine all three tables using UNION ALL.
11. Find out how UNION behaves when two records have the same name but different student IDs.
12. Write a query that combines student names from both tables and sorts them in descending order.

## 13. Review Questions

1. What is UNION in PostgreSQL?
2. What is UNION ALL?
3. What is the main difference between UNION and UNION ALL?
4. Does UNION remove duplicate rows?
5. Does UNION ALL remove duplicate rows?
6. What happens if SELECT statements return different numbers of columns?
7. Can we use ORDER BY with UNION?
8. What is the difference between UNION and JOIN?
9. Does UNION remove duplicate values from one column or duplicate complete rows?
10. Which operator is generally faster and why?

## 14. Quick Revision

| SQL Operator | Purpose                                        |
| ------------ | ---------------------------------------------- |
| UNION        | Combines results and removes duplicate rows    |
| UNION ALL    | Combines results and keeps duplicate rows      |
| JOIN         | Combines related data from tables horizontally |
| ORDER BY     | Sorts the combined result                      |

Key point: Use UNION when you need unique rows. Use UNION ALL when you need all rows, including duplicates.

