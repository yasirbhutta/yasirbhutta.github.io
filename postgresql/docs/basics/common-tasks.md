# Lesson 1.7: Common Database Tasks in PostgreSQL

## 1. Introduction

PostgreSQL allows users to perform different operations to manage databases and their data.

These operations are commonly performed using SQL commands.

## 2. Creating a Database

The `CREATE DATABASE` command creates a new database.

```sql
CREATE DATABASE university;
```

This command creates a database named `university`.

## 3. Creating a Table

The `CREATE TABLE` command creates a new table inside a database.

```sql
CREATE TABLE students (
    student_id INT,
    student_name VARCHAR(100),
    age INT
);
```

This creates a table named `students` with three columns.

## 4. Inserting Data

The `INSERT INTO` command adds new records to a table.

```sql
INSERT INTO students
(student_id, student_name, age)
VALUES
(101, 'Ali', 20);
```

This inserts one student record.

## 5. Retrieving Data

The `SELECT` command retrieves data from a table.

```sql
SELECT * FROM students;
```

The asterisk `*` means all columns.

## 6. Updating Data

The `UPDATE` command modifies existing records.

```sql
UPDATE students
SET age = 21
WHERE student_id = 101;
```

This changes the age of the student whose ID is 101.

## 7. Deleting Data

The `DELETE` command removes records from a table.

```sql
DELETE FROM students
WHERE student_id = 101;
```

This deletes the student record with ID 101.

## 8. Common PostgreSQL SQL Commands

| Task | SQL Command |
|---|---|
| Create database | CREATE DATABASE |
| Delete database | DROP DATABASE |
| Create table | CREATE TABLE |
| Add records | INSERT INTO |
| Retrieve records | SELECT |
| Update records | UPDATE |
| Delete records | DELETE |
| Modify table structure | ALTER TABLE |
| Create a view | CREATE VIEW |
| Create an index | CREATE INDEX |

## 9. Important Note

The examples in this lesson are introductory examples. Later modules will explain each command in detail.

Also, commands such as `UPDATE` and `DELETE` can affect multiple records if the `WHERE` condition is omitted. Always check the condition before executing them.

## 10. Quick Summary

- PostgreSQL supports different database operations.
- SQL commands are used to manage database objects and data.
- CREATE, INSERT, SELECT, UPDATE, and DELETE are fundamental SQL commands.

## Practice Questions

1. Which command creates a database?
2. Which command creates a table?
3. Which command inserts records?
4. Which command retrieves records?
5. What is the purpose of the WHERE clause?
6. Write an SQL command to retrieve all records from a table named `students`.

---
