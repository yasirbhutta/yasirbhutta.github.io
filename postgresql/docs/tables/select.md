# SELECT Statement in PostgreSQL

## 1. Introduction

After inserting records into a database table, we often need to retrieve and view that information.

In PostgreSQL, the `SELECT` statement is used to retrieve data from one or more tables.

Real-life example:

Imagine a university database containing thousands of student records. The Registrar Office may need to:

- View all student records.
- View only student names.
- View student names and email addresses.
- Find a particular student's information.

All these tasks can be performed using the `SELECT` statement.

## 2. Basic Syntax

```
SELECT column1, column2
FROM table_name;
```

Understanding the syntax:

- `SELECT`: Specifies which columns you want to retrieve.
- `column1, column2`: Names of the columns.
- `FROM`: Specifies the table name.
- `table_name`: The table from which data is retrieved.

## 3. Create a Table for Practice

Let's create a students table.

```
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    student_name VARCHAR(100),
    email VARCHAR(100),
    age INTEGER,
    city VARCHAR(50)
);
```

Insert some sample records:

```
INSERT INTO students
    (student_id, student_name, email, age, city)
VALUES
    (1, 'Ali', 'ali@example.com', 20, 'Multan'),
    (2, 'Ahmad', 'ahmad@example.com', 21, 'Lahore'),
    (3, 'Usman', 'usman@example.com', 22, 'Dera Ghazi Khan'),
    (4, 'Sara', 'sara@example.com', 19, 'Multan'),
    (5, 'Ayesha', 'ayesha@example.com', 20, 'Lahore');
```

## 4. Select All Columns

To retrieve all columns from a table, use the asterisk (`*`) symbol.

```
SELECT *
FROM students;
```

Understand the code:

- `SELECT` tells PostgreSQL to retrieve data.
- `*` means all columns.
- `FROM students` specifies the students table.

This query displays all columns and records from the students table.

## 5. Select Specific Columns

Sometimes we do not need all the information.

For example, if we only want student names:

```
SELECT student_name
FROM students;
```

To retrieve student names and email addresses:

```
SELECT student_name, email
FROM students;
```

To retrieve student IDs, names, and cities:

```
SELECT student_id, student_name, city
FROM students;
```

Important: Write column names separated by commas.

## 6. Select a Single Column with a Different Display Name

We can use the `AS` keyword to give a temporary name to a column in the query result.

This is called a column alias.

```
SELECT student_name AS name
FROM students;
```

The result displays the column heading as `name` instead of `student_name`.

Another example:

```
SELECT
    student_name AS name,
    city AS hometown
FROM students;
```

Important: An alias changes the display name in the query result. It does not rename the actual table column.

## 7. Remove Duplicate Values Using DISTINCT

Sometimes a column contains repeated values.

For example, multiple students may belong to the same city.

To display each city only once, use `DISTINCT`.

```
SELECT DISTINCT city
FROM students;
```

To retrieve unique combinations of cities and ages:

```
SELECT DISTINCT city, age
FROM students;
```

Important: `DISTINCT` removes duplicate combinations of the selected columns.

## 8. Select All Records in a Specific Column

Suppose we want to retrieve all student ages.

```
SELECT age
FROM students;
```

This query displays the age of every student, including repeated values.

To display only unique ages:

```
SELECT DISTINCT age
FROM students;
```

## 9. Understanding SELECT and FROM

Consider the following query:

```
SELECT student_name, city
FROM students;
```

Think of it as asking two questions:

1. `SELECT`: What information do I want?
2. `FROM`: Where should PostgreSQL get that information?

This is the basic idea behind retrieving data from a database.

## 10. Complete Practical Examples

Try the following queries using the students table.

Example 1: Display all students

```
SELECT *
FROM students;
```

Example 2: Display only student names

```
SELECT student_name
FROM students;
```

Example 3: Display student names and ages

```
SELECT student_name, age
FROM students;
```

Example 4: Display unique cities

```
SELECT DISTINCT city
FROM students;
```

Example 5: Display student names with readable column headings

```
SELECT
    student_name AS "Student Name",
    email AS "Email Address"
FROM students;
```

## 11. Practice Exercises

Use the `students` table created in this lesson.

Exercise 1: Retrieve All Records

Write a query to display all records from the students table.

Exercise 2: Select Specific Columns

Write queries to display:

- Only student names.
- Student names and email addresses.
- Student IDs and student names.
- Student names, ages, and cities.

Exercise 3: Use DISTINCT

Write queries to display:

- All unique cities.
- All unique student ages.

Exercise 4: Use Column Aliases

Write a query that displays:

- `student_name` as `Name`.
- `email` as `Email Address`.
- `city` as `Home City`.

Exercise 5: Think and Practice

What is the difference between these two queries?

```
SELECT city
FROM students;
```

```
SELECT DISTINCT city
FROM students;
```

## 12. Review Questions

1. What is the purpose of the SELECT statement?
2. What does the asterisk (`*`) represent?
3. Why do we use the FROM keyword?
4. How can we retrieve only selected columns?
5. What is the purpose of DISTINCT?
6. What is a column alias?
7. Does an alias permanently rename a table column?
8. What is the difference between SELECT and SELECT DISTINCT?

## 13. Quick Revision

| SQL Keyword | Purpose                           |
| ----------- | --------------------------------- |
| `SELECT`    | Retrieves data.                   |
| `*`         | Selects all columns.              |
| `FROM`      | Specifies the source table.       |
| `AS`        | Assigns a temporary column alias. |
| `DISTINCT`  | Removes duplicate results.        |

Next Lesson: WHERE Clause in PostgreSQL

Students will learn how to filter records using conditions, comparison operators, and logical operators.