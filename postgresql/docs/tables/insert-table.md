# INSERT INTO Statement in PostgreSQL

## 1. Introduction

After creating a database and its tables, the next step is to add data to those tables.

In PostgreSQL, the `INSERT INTO` statement is used to insert new records (rows) into a table.

Real-life example:

Imagine a university maintaining student records. Whenever a new student takes admission, the university adds that student's information to the students table.

We can perform this task using the `INSERT INTO` statement.

## 2. Basic Syntax

```
INSERT INTO table_name (column1, column2, column3)
VALUES (value1, value2, value3);
```

Understanding the syntax:

- `INSERT INTO`: Specifies that we want to add a new record.
- `table_name`: Name of the table.
- `column1, column2`: Names of the columns.
- `VALUES`: Specifies the values to insert.
- `value1, value2`: Actual data for the columns.

## 3. Create a Table for Practice

Before inserting data, let's create a students table.

```
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    age INTEGER,
    city VARCHAR(50)
);
```

Our table contains five columns:

| Column       | Data Type    | Description   |
| ------------ | ------------ | ------------- |
| student_id   | INTEGER      | Student ID    |
| student_name | VARCHAR(100) | Student name  |
| email        | VARCHAR(100) | Email address |
| age          | INTEGER      | Student age   |
| city         | VARCHAR(50)  | City name     |

## 4. Insert a Single Record

Let's insert one student record.

```
INSERT INTO students
    (student_id, student_name, email, age, city)
VALUES
    (1, 'Ali', 'ali@example.com', 20, 'Multan');
```

Understand the code:

| Column       | Value            |
| ------------ | ---------------- |
| student_id   | 1                |
| student_name | Ali              |
| email        | ali\@example.com |
| age          | 20               |
| city         | Multan           |

The database inserts one new row into the students table.

## 5. Insert Multiple Records

We can insert multiple records using a single `INSERT INTO` statement.

```
INSERT INTO students
    (student_id, student_name, email, age, city)
VALUES
    (2, 'Ahmad', 'ahmad@example.com', 21, 'Lahore'),
    (3, 'Usman', 'usman@example.com', 22, 'Dera Ghazi Khan'),
    (4, 'Sara', 'sara@example.com', 19, 'Multan'),
    (5, 'Ayesha', 'ayesha@example.com', 20, 'Lahore');
```

Each set of parentheses represents one record.

## 6. Insert Data into Selected Columns

Sometimes we do not need to provide values for every column.

For example, suppose we want to insert only the student ID and name.

```
INSERT INTO students
    (student_id, student_name)
VALUES
    (6, 'Hassan');
```

PostgreSQL will automatically assign `NULL` to the columns that were not provided, if they allow NULL values.

Important: If a column has a `DEFAULT` constraint, PostgreSQL uses its default value instead of NULL.

## 7. Insert Using DEFAULT Values

Suppose we have a courses table:

```
CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    credit_hours INTEGER DEFAULT 3,
    is_active BOOLEAN DEFAULT TRUE
);
```

Insert a course without specifying credit hours and active status:

```
INSERT INTO courses (course_id, course_name)
VALUES (1, 'Database Systems');
```

PostgreSQL automatically assigns:

- `credit_hours = 3`
- `is_active = TRUE`

You can also explicitly use the `DEFAULT` keyword:

```
INSERT INTO courses
    (course_id, course_name, credit_hours, is_active)
VALUES
    (2, 'Programming Fundamentals', DEFAULT, DEFAULT);
```

## 8. Insert Data Without Specifying Column Names

You can insert data without writing column names.

```
INSERT INTO students
VALUES (7, 'Bilal', 'bilal@example.com', 23, 'Islamabad');
```

Important: When you omit column names, you must provide values in the exact order of the table columns. You must also account for every column.

For beginners, using explicit column names is recommended because it makes SQL easier to understand and maintain.

## 9. View Inserted Records

After inserting records, use the `SELECT` statement to view the data.

```
SELECT * FROM students;
```

The `*` symbol means all columns.

To view selected columns:

```
SELECT student_id, student_name, city
FROM students;
```

## 10. Common Mistakes

| Mistake                 | Explanation                                            |
| ----------------------- | ------------------------------------------------------ |
| Missing quotation marks | Text values require single quotation marks.            |
| Wrong number of values  | The number of values must match the specified columns. |
| Duplicate primary key   | A primary key value cannot be repeated.                |
| Missing required value  | A NOT NULL column must receive a value.                |
| Incorrect data type     | Values must be compatible with the column's data type. |

Incorrect example:

```
INSERT INTO students (student_id, student_name)
VALUES (8, Ali);
```

The name `Ali` is text, so it needs single quotation marks.

Correct example:

```
INSERT INTO students (student_id, student_name)
VALUES (8, 'Ali');
```

## 11. Complete Practical Exercise

Perform the following tasks in PostgreSQL:

Task 1: Create a table named `teachers` with these columns:

- `teacher_id` — INTEGER PRIMARY KEY
- `teacher_name` — VARCHAR(100) NOT NULL
- `email` — VARCHAR(100)
- `department` — VARCHAR(50)
- `salary` — NUMERIC(10, 2)

Task 2: Insert one teacher record.

Task 3: Insert three teacher records using a single INSERT statement.

Task 4: Insert a teacher using only `teacher_id` and `teacher_name`.

Task 5: Display all teacher records.

Task 6: Display only teacher names and departments.

## 12. Review Questions

1. What is the purpose of the `INSERT INTO` statement?
2. What is the difference between inserting a single record and multiple records?
3. Why do we specify column names in an INSERT statement?
4. What happens when a column value is not provided?
5. What is the purpose of the `DEFAULT` keyword?
6. Why do text values require single quotation marks?
7. Which SQL statement is used to display inserted records?

## 13. Quick Revision

| SQL Statement | Purpose                           |
| ------------- | --------------------------------- |
| `INSERT INTO` | Adds new records.                 |
| `VALUES`      | Specifies the data to insert.     |
| `DEFAULT`     | Uses a column's default value.    |
| `SELECT *`    | Displays all columns and records. |

