
# Lesson 1.9: Understanding Tables, Rows, Columns and Records

## 1. Introduction

Relational databases store information in tables.

To work with PostgreSQL, students must understand four important terms:

- Table
- Row
- Column
- Record

## 2. What Is a Table?

A table is a database object that stores related data in rows and columns.

Example: A university may use a `students` table to store student information.

## 3. What Is a Column?

A column represents a particular type of information stored in a table.

For example:

- student_id
- student_name
- age
- department

Each column has a name and a data type.

## 4. What Is a Row?

A row represents one complete entry in a table.

For example, the information of one student is stored in one row.

## 5. What Is a Record?

A record is another term for a row.

It represents a complete set of related values in a table.

## 6. Practical Example

Consider the following `students` table:

| student_id | student_name | age | department |
|---:|---|---:|---|
| 101 | Ali | 20 | CS |
| 102 | Ahmed | 21 | IT |
| 103 | Sara | 19 | Mathematics |
| 104 | Ayesha | 22 | English |

Understanding this table:

- Table name: `students`
- Number of columns: 4
- Number of rows: 4
- First row: Student record of Ali
- First column: `student_id`
- Second column: `student_name`

## 7. Understanding a Table Structure

```sql
CREATE TABLE students (
    student_id INT,
    student_name VARCHAR(100),
    age INT,
    department VARCHAR(50)
);
```

Explanation:

| Column | Data Type | Purpose |
|---|---|---|
| student_id | INT | Stores student ID |
| student_name | VARCHAR(100) | Stores student name |
| age | INT | Stores age |
| department | VARCHAR(50) | Stores department name |

## 8. Retrieving Table Data

To view all records:

```sql
SELECT * FROM students;
```

To view only student names:

```sql
SELECT student_name
FROM students;
```

To view student names and ages:

```sql
SELECT student_name, age
FROM students;
```

## 9. Quick Summary

- A table stores related information.
- A column represents a field or attribute.
- A row represents one entry.
- A record is another name for a row.
- A table contains rows and columns.

## Practice Questions

Consider the following table:

| employee_id | employee_name | salary | department |
|---:|---|---:|---|
| 1 | Ali | 50000 | IT |
| 2 | Ahmed | 60000 | HR |
| 3 | Sara | 55000 | Finance |
| 4 | Ayesha | 65000 | IT |

Answer the following questions:

1. What is the table name if this table stores employee information?
2. How many columns are present?
3. How many rows are present?
4. What is the name of the third column?
5. What is the salary of Sara?
6. Which row contains Ahmed's information?
7. Write an SQL query to retrieve all columns.
8. Write an SQL query to retrieve only employee names.

---
