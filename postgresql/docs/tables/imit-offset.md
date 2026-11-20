# LIMIT and OFFSET in PostgreSQL

## 1. Introduction

In PostgreSQL, `LIMIT` and `OFFSET` are used to control how many records are retrieved from a table and which records are displayed.

These clauses are especially useful when working with tables containing thousands or millions of records.

Real-life example:

Imagine a university database containing 10,000 student records.

The Registrar Office may need to:

- Display only the first 10 students.
- Display the next 10 students.
- Show records 21 to 30.
- Display student records page by page.

PostgreSQL provides `LIMIT` and `OFFSET` to perform these tasks.

## 2. LIMIT Clause

The `LIMIT` clause specifies the maximum number of records to retrieve.

Basic syntax:

```
SELECT column1, column2
FROM table_name
LIMIT number;
```

Example: Display only the first five student records.

```
SELECT *
FROM students
LIMIT 5;
```

This query retrieves a maximum of five records.

Important: Without `ORDER BY`, PostgreSQL does not guarantee which five records will be returned.

## 3. LIMIT with ORDER BY

We can combine `LIMIT` with `ORDER BY` to retrieve specific records in a defined order.

Example: Display the five youngest students.

```
SELECT *
FROM students
ORDER BY age ASC
LIMIT 5;
```

Understand the query:

1. `ORDER BY age ASC` sorts students from youngest to oldest.
2. `LIMIT 5` retrieves only the first five records.

Another example: Display the three students with the highest fees.

```
SELECT *
FROM students
ORDER BY fee DESC
LIMIT 3;
```

## 4. OFFSET Clause

The `OFFSET` clause specifies how many records PostgreSQL should skip before returning results.

Basic syntax:

```
SELECT column1, column2
FROM table_name
OFFSET number;
```

Example: Skip the first five records.

```
SELECT *
FROM students
ORDER BY student_id
OFFSET 5;
```

This query skips the first five records and returns the remaining records.

## 5. Use LIMIT and OFFSET Together

We can combine `LIMIT` and `OFFSET` to retrieve a specific group of records.

Basic syntax:

```
SELECT column1, column2
FROM table_name
ORDER BY column_name
LIMIT number
OFFSET number;
```

Example: Display records 6 to 10.

```
SELECT *
FROM students
ORDER BY student_id
LIMIT 5
OFFSET 5;
```

Understand the query:

- `ORDER BY student_id` arranges records by student ID.
- `OFFSET 5` skips the first five records.
- `LIMIT 5` retrieves the next five records.

## 6. Understanding LIMIT and OFFSET with Examples

Suppose our students table contains the following records:

| Student ID | Student Name |
| ---------- | ------------ |
| 1          | Ali          |
| 2          | Ahmad        |
| 3          | Usman        |
| 4          | Sara         |
| 5          | Ayesha       |
| 6          | Hassan       |
| 7          | Bilal        |
| 8          | Zain         |
| 9          | Hamza        |
| 10         | Fatima       |

Let's understand different queries.

Example 1: First three students

```
SELECT *
FROM students
ORDER BY student_id
LIMIT 3;
```

Result: Students 1, 2, and 3.

Example 2: Skip the first three students

```
SELECT *
FROM students
ORDER BY student_id
OFFSET 3;
```

Result: Students 4 to 10.

Example 3: Display students 4 to 6

```
SELECT *
FROM students
ORDER BY student_id
LIMIT 3
OFFSET 3;
```

Result: Students 4, 5, and 6.

Example 4: Display students 7 to 10

```
SELECT *
FROM students
ORDER BY student_id
LIMIT 4
OFFSET 6;
```

Result: Students 7, 8, 9, and 10.

## 7. Understanding Pagination

Pagination means dividing a large collection of records into smaller groups called pages.

For example, if a university has 100 student records and we display 10 records per page, we will have 10 pages.

We can calculate the OFFSET using this formula:

\\[ \text{OFFSET} = (\text{Page Number} - 1) \times \text{Records Per Page} \\]

Suppose we want to display 10 records per page.

| Page Number | LIMIT | OFFSET |
| ----------- | ----- | ------ |
| 1           | 10    | 0      |
| 2           | 10    | 10     |
| 3           | 10    | 20     |
| 4           | 10    | 30     |
| 5           | 10    | 40     |

SQL for Page 1:

```
SELECT *
FROM students
ORDER BY student_id
LIMIT 10 OFFSET 0;
```

SQL for Page 2:

```
SELECT *
FROM students
ORDER BY student_id
LIMIT 10 OFFSET 10;
```

SQL for Page 3:

```
SELECT *
FROM students
ORDER BY student_id
LIMIT 10 OFFSET 20;
```

This approach is commonly used in websites and applications to display records page by page.

## 8. Combine LIMIT and OFFSET with WHERE

We can also filter records before applying pagination.

Example: Display the first five Computer Science students.

```
SELECT *
FROM students
WHERE department = 'Computer Science'
ORDER BY student_id
LIMIT 5;
```

Example: Display the next five Computer Science students.

```
SELECT *
FROM students
WHERE department = 'Computer Science'
ORDER BY student_id
LIMIT 5 OFFSET 5;
```

## 9. Important Points

1. `LIMIT` controls the maximum number of returned records.
2. `OFFSET` skips a specified number of records.
3. `ORDER BY` should be used to ensure a predictable order.
4. `LIMIT` and `OFFSET` do not delete or modify records.
5. Pagination is a common application of these clauses.
6. Large OFFSET values can become inefficient because PostgreSQL still has to process skipped rows.

## 10. Complete Practical Examples

Try these queries using the students table.

Example 1: Display the first 10 students.

```
SELECT *
FROM students
ORDER BY student_id
LIMIT 10;
```

Example 2: Display the five students with the highest fees.

```
SELECT *
FROM students
ORDER BY fee DESC, student_id ASC
LIMIT 5;
```

Example 3: Display students from the second page, assuming 10 records per page.

```
SELECT *
FROM students
ORDER BY student_id
LIMIT 10 OFFSET 10;
```

Example 4: Display the first three oldest students.

```
SELECT *
FROM students
ORDER BY age DESC, student_id ASC
LIMIT 3;
```

## 11. Practice Exercises

Use the students table created in previous lessons.

Exercise 1: LIMIT

Write queries to:

1. Display the first five students.
2. Display the first 10 students.
3. Display the three students with the highest fees.
4. Display the five youngest students.

Exercise 2: OFFSET

Write queries to:

1. Skip the first five students.
2. Skip the first 10 students.
3. Skip the first three students and display the remaining records.

Exercise 3: LIMIT and OFFSET

Write queries to:

1. Display students 6 to 10.
2. Display students 11 to 15.
3. Display students 16 to 20.
4. Display the second page containing 10 records.

Exercise 4: Combine SQL Clauses

Write queries to:

1. Find Computer Science students and display the first five records.
2. Find students from Multan and display the first three records.
3. Display the five students with the highest fees, arranged by student ID when fees are equal.

## 12. Review Questions

1. What is the purpose of the LIMIT clause?
2. What is the purpose of the OFFSET clause?
3. What is the difference between LIMIT and OFFSET?
4. Why should we use ORDER BY with LIMIT?
5. What is pagination?
6. How do we retrieve the second page containing 10 records?
7. Does LIMIT modify or delete records from a table?
8. How can we combine WHERE, ORDER BY, LIMIT, and OFFSET?

## 13. Quick Revision

| SQL Clause | Purpose                                   |
| ---------- | ----------------------------------------- |
| `LIMIT`    | Restricts the number of returned records. |
| `OFFSET`   | Skips a specified number of records.      |
| `ORDER BY` | Sorts the records.                        |
| `WHERE`    | Filters records.                          |

Remember:

- `LIMIT 5` means retrieve a maximum of five records.
- `OFFSET 5` means skip the first five records.
- `LIMIT 5 OFFSET 5` means skip five records and retrieve the next five.

Next Lesson: UPDATE Statement in PostgreSQL

Students will learn how to modify existing records in a database table using the `UPDATE` statement.