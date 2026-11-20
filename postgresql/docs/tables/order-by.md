# ORDER BY Clause in PostgreSQL

## 1. Introduction

In PostgreSQL, the `ORDER BY` clause is used to sort records in a table or query result.

We can arrange records in:

- Ascending order (ASC): Smallest to largest, A to Z, or oldest to newest.
- Descending order (DESC): Largest to smallest, Z to A, or newest to oldest.

Real-life example:

Imagine a university database containing student records. The Registrar Office may need to:

- Display students alphabetically by name.
- Arrange students by age, from youngest to oldest.
- Display students according to their fees, from highest to lowest.
- Sort students by department and then by name.

The `ORDER BY` clause makes these tasks possible.

## 2. Basic Syntax

```
SELECT column1, column2
FROM table_name
ORDER BY column_name ASC;
```

Understanding the syntax:

- `SELECT`: Specifies the columns to retrieve.
- `FROM`: Specifies the source table.
- `ORDER BY`: Specifies the column used for sorting.
- `ASC`: Sorts records in ascending order.

## 3. Create a Table for Practice

Let's create a students table.

```
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    student_name VARCHAR(100),
    age INTEGER,
    city VARCHAR(50),
    department VARCHAR(50),
    fee NUMERIC(10, 2)
);
```

Insert sample records:

```
INSERT INTO students
    (student_id, student_name, age, city, department, fee)
VALUES
    (1, 'Ali', 20, 'Multan', 'Computer Science', 50000),
    (2, 'Ahmad', 22, 'Lahore', 'Information Technology', 45000),
    (3, 'Usman', 19, 'Multan', 'Mathematics', 40000),
    (4, 'Sara', 21, 'Lahore', 'Computer Science', 55000),
    (5, 'Ayesha', 23, 'Dera Ghazi Khan', 'Information Technology', 45000),
    (6, 'Hassan', 18, 'Multan', 'Computer Science', 50000);
```

## 4. Sort Records in Ascending Order

The `ASC` keyword sorts records in ascending order.

For example, display students according to their ages, from youngest to oldest.

```
SELECT *
FROM students
ORDER BY age ASC;
```

Understand the result:

The records will be arranged according to age:

18, 19, 20, 21, 22, 23.

Important: `ASC` is the default sorting order in PostgreSQL. Therefore, writing `ASC` is optional.

The following query produces the same result:

```
SELECT *
FROM students
ORDER BY age;
```

## 5. Sort Records in Descending Order

The `DESC` keyword sorts records in descending order.

For example, display students from oldest to youngest.

```
SELECT *
FROM students
ORDER BY age DESC;
```

The records will be arranged as:

23, 22, 21, 20, 19, 18.

## 6. Sort Text Values Alphabetically

We can also sort text values alphabetically.

Example: Display students according to their names from A to Z.

```
SELECT *
FROM students
ORDER BY student_name ASC;
```

To arrange names from Z to A:

```
SELECT *
FROM students
ORDER BY student_name DESC;
```

## 7. Sort Records Using a Specific Column

We can sort records using any suitable column.

Example 1: Sort by student ID

```
SELECT *
FROM students
ORDER BY student_id ASC;
```

Example 2: Sort by fee from lowest to highest

```
SELECT *
FROM students
ORDER BY fee ASC;
```

Example 3: Sort by fee from highest to lowest

```
SELECT *
FROM students
ORDER BY fee DESC;
```

Example 4: Sort by city alphabetically

```
SELECT *
FROM students
ORDER BY city ASC;
```

## 8. Sort Records Using Multiple Columns

Sometimes we need to sort records using more than one column.

For example, first arrange students by department and then arrange students within each department by name.

```
SELECT *
FROM students
ORDER BY department ASC, student_name ASC;
```

Understand the query:

1. PostgreSQL first sorts records by department.
2. Students belonging to the same department are then sorted by name.

Another example:

```
SELECT *
FROM students
ORDER BY city ASC, age DESC;
```

This query:

1. Sorts students by city from A to Z.
2. Within each city, sorts students from oldest to youngest.

## 9. Use ORDER BY with WHERE

We can combine `WHERE` and `ORDER BY` to filter and sort records.

Example: Find students from Multan and arrange them by age.

```
SELECT *
FROM students
WHERE city = 'Multan'
ORDER BY age ASC;
```

Another example: Find Computer Science students and arrange them by fee from highest to lowest.

```
SELECT *
FROM students
WHERE department = 'Computer Science'
ORDER BY fee DESC;
```

Important: In a SELECT query, `WHERE` comes before `ORDER BY`.

## 10. Use ORDER BY with Selected Columns

We do not need to display every column to sort records.

```
SELECT student_name, age
FROM students
ORDER BY age DESC;
```

This query displays only student names and ages, arranged from oldest to youngest.

## 11. Sorting NULL Values

PostgreSQL also allows us to control where NULL values appear in sorted results.

Use:

- `NULLS FIRST` to display NULL values first.
- `NULLS LAST` to display NULL values last.

Example:

```
SELECT *
FROM students
ORDER BY age ASC NULLS LAST;
```

This is useful when some records have missing values.

## 12. Complete Practical Examples

Try the following queries using the students table.

Example 1: Display all students by name

```
SELECT *
FROM students
ORDER BY student_name;
```

Example 2: Display students by age, oldest first

```
SELECT student_name, age
FROM students
ORDER BY age DESC;
```

Example 3: Display students by fee, highest first

```
SELECT student_name, fee
FROM students
ORDER BY fee DESC;
```

Example 4: Display Multan students alphabetically

```
SELECT *
FROM students
WHERE city = 'Multan'
ORDER BY student_name ASC;
```

Example 5: Display students by department and age

```
SELECT student_name, department, age
FROM students
ORDER BY department ASC, age DESC;
```

## 13. Practice Exercises

Use the students table created in this lesson.

Exercise 1: Basic Sorting

Write queries to:

1. Display all students by student ID in ascending order.
2. Display all students by age in ascending order.
3. Display all students by age in descending order.
4. Display all students alphabetically by name.

Exercise 2: Sort Using Different Columns

Write queries to:

1. Display students according to their fee, lowest first.
2. Display students according to their fee, highest first.
3. Display students according to their city alphabetically.
4. Display students according to their department.

Exercise 3: Multiple Column Sorting

Write queries to:

1. Sort students by city and then by name.
2. Sort students by department and then by age.
3. Sort students by city in ascending order and fee in descending order.

Exercise 4: Combine WHERE and ORDER BY

Write queries to:

1. Find Multan students and sort them by age.
2. Find Computer Science students and sort them by fee.
3. Find students aged 20 or above and arrange them alphabetically.

## 14. Review Questions

1. What is the purpose of the ORDER BY clause?
2. What is the difference between ASC and DESC?
3. What is the default sorting order in PostgreSQL?
4. Can we sort records using text columns?
5. Can we sort records using multiple columns?
6. What happens when we use ORDER BY with WHERE?
7. What is the purpose of NULLS FIRST and NULLS LAST?
8. Does ORDER BY permanently change the order of records stored in a table?

## 15. Quick Revision

| SQL Keyword   | Purpose                         |
| ------------- | ------------------------------- |
| `ORDER BY`    | Sorts query results.            |
| `ASC`         | Sorts in ascending order.       |
| `DESC`        | Sorts in descending order.      |
| `NULLS FIRST` | Places NULL values first.       |
| `NULLS LAST`  | Places NULL values last.        |
| `WHERE`       | Filters records before sorting. |

Remember: `ORDER BY` changes the order of the query results, not the physical storage order of records in the table.

