# Data Types in PostgreSQL

Student Notes | Database Management Systems (DBMS)

## 1. Introduction

In the previous lesson, we learned how to create tables in PostgreSQL.

When creating a table, we need to define what type of information each column will store. For example:

- Student ID stores numbers.
- Student Name stores text.
- Date of Birth stores dates.
- Fee stores numeric values.
- Is Active stores TRUE or FALSE.

To define the type of information a column can store, PostgreSQL provides Data Types.

## 2. What is a Data Type?

A data type defines the kind of information that can be stored in a database column.

In simple words:

A data type tells PostgreSQL what kind of value a column can accept.

Real-Life Example:

Consider a university students table.

| student_id | name  | age | fee      | admission_date |
| ---------- | ----- | --- | -------- | -------------- |
| 101        | Ali   | 20  | 25000.50 | 2026-09-01     |
| 102        | Ahmed | 21  | 30000.00 | 2026-09-02     |
| 103        | Sara  | 19  | 27500.75 | 2026-09-03     |

Each column stores a different type of information.

| Column         | Data Type     | Example    |
| -------------- | ------------- | ---------- |
| student_id     | INTEGER       | 101        |
| name           | VARCHAR(100)  | Ali        |
| age            | INTEGER       | 20         |
| fee            | NUMERIC(10,2) | 25000.50   |
| admission_date | DATE          | 2026-09-01 |

## 3. Common Data Types in PostgreSQL

PostgreSQL supports many data types. In this lesson, we will learn the most commonly used types.

### A. INTEGER

`INTEGER` is used to store whole numbers without decimal points.

Examples:

- 10
- 25
- 100
- 2026

SQL Example:

```
CREATE TABLE students (
    student_id INTEGER,
    age INTEGER
);
```

Here, both `student_id` and `age` store whole numbers.

### B. VARCHAR

`VARCHAR` is used to store variable-length text.

We can specify the maximum number of characters.

Example:

```
CREATE TABLE students (
    name VARCHAR(100)
);
```

This column can store text up to 100 characters.

Example values:

- Ali
- Ahmed
- Muhammad Yasir
- Computer Science

### C. TEXT

`TEXT` is used to store text of variable length without specifying a maximum length.

Example:

```
CREATE TABLE departments (
    description TEXT
);
```

Example values:

- Computer Science Department
- Information Technology Department
- Mathematics Department

Remember: In PostgreSQL, `TEXT` and `VARCHAR` without a length limit have similar practical behavior.

### D. NUMERIC

`NUMERIC` is used to store exact decimal numbers.

It is especially useful for financial information.

Example:

```
CREATE TABLE fees (
    amount NUMERIC(10,2)
);
```

Here:

- `10` represents the maximum total number of digits.
- `2` represents the number of digits after the decimal point.

Example values:

- 25000.50
- 1500.75
- 99999.99

### E. DATE

`DATE` is used to store calendar dates.

The standard date format is:

`YYYY-MM-DD`

Where:

- YYYY = Year
- MM = Month
- DD = Day

Example:

```
CREATE TABLE students (
    admission_date DATE
);
```

Example value:

```
'2026-09-01'
```

### F. BOOLEAN

`BOOLEAN` is used to store logical values.

It has two main values:

- TRUE
- FALSE

Example:

```
CREATE TABLE students (
    is_active BOOLEAN
);
```

Example values:

| student_id | is_active |
| ---------- | --------- |
| 101        | TRUE      |
| 102        | FALSE     |
| 103        | TRUE      |

## 4. Summary of Common Data Types

| Data Type     | Purpose                    | Example                |
| ------------- | -------------------------- | ---------------------- |
| INTEGER       | Whole numbers              | 100                    |
| SMALLINT      | Small whole numbers        | 25                     |
| BIGINT        | Large whole numbers        | 1000000                |
| VARCHAR(100)  | Variable-length text       | Ali                    |
| TEXT          | Longer text                | Department description |
| NUMERIC(10,2) | Exact decimal values       | 25000.50               |
| REAL          | Approximate decimal values | 12.5                   |
| DATE          | Calendar dates             | 2026-09-01             |
| TIME          | Time values                | 10:30:00               |
| TIMESTAMP     | Date and time              | 2026-09-01 10:30:00    |
| BOOLEAN       | True or false              | TRUE                   |

## 5. Practical Example: Create a Students Table

Now let's use different data types together.

Task: Create a `students` table for a university.

SQL Command:

```
CREATE TABLE students (
    student_id INTEGER,
    name VARCHAR(100),
    age INTEGER,
    department TEXT,
    fee NUMERIC(10,2),
    admission_date DATE,
    is_active BOOLEAN
);
```

### Understanding the Code

| Column         | Data Type     | Purpose                       |
| -------------- | ------------- | ----------------------------- |
| student_id     | INTEGER       | Student identification number |
| name           | VARCHAR(100)  | Student name                  |
| age            | INTEGER       | Student age                   |
| department     | TEXT          | Department name               |
| fee            | NUMERIC(10,2) | Student fee                   |
| admission_date | DATE          | Admission date                |
| is_active      | BOOLEAN       | Student active status         |

## 6. Insert Sample Records

After creating the table, we can insert information into it.

```
INSERT INTO students
(student_id, name, age, department, fee, admission_date, is_active)
VALUES
(101, 'Ali', 20, 'Computer Science', 25000.50, '2026-09-01', TRUE),
(102, 'Ahmed', 21, 'Information Technology', 30000.00, '2026-09-02', TRUE),
(103, 'Sara', 19, 'Mathematics', 27500.75, '2026-09-03', FALSE);
```

To display the records:

```
SELECT * FROM students;
```

Expected Result:

| student_id | name  | age | department             | fee      | is_active |
| ---------- | ----- | --- | ---------------------- | -------- | --------- |
| 101        | Ali   | 20  | Computer Science       | 25000.50 | TRUE      |
| 102        | Ahmed | 21  | Information Technology | 30000.00 | TRUE      |
| 103        | Sara  | 19  | Mathematics            | 27500.75 | FALSE     |

## 7. Important Points to Remember

1. Every column in a PostgreSQL table has a data type.
2. INTEGER stores whole numbers.
3. VARCHAR stores variable-length text.
4. TEXT stores text without a specified maximum length.
5. NUMERIC stores exact decimal values.
6. DATE stores calendar dates.
7. BOOLEAN stores TRUE or FALSE.
8. Choosing the correct data type helps maintain data accuracy.

## 8. Practice Exercises

### Exercise 1: Identify the Correct Data Type

Choose an appropriate PostgreSQL data type for each column.

| Column         | Example Value      | Your Data Type |
| -------------- | ------------------ | -------------- |
| student_id     | 101                | ?              |
| student_name   | Muhammad Ali       | ?              |
| age            | 20                 | ?              |
| fee            | 25000.50           | ?              |
| admission_date | 2026-09-01         | ?              |
| is_active      | TRUE               | ?              |
| description    | Department details | ?              |

### Exercise 2: Create a Teachers Table

Create a table named `teachers` with the following columns:

| Column       | Suggested Data Type |
| ------------ | ------------------- |
| teacher_id   | INTEGER             |
| teacher_name | VARCHAR(100)        |
| department   | TEXT                |
| salary       | NUMERIC(10,2)       |
| joining_date | DATE                |
| is_active    | BOOLEAN             |

### Exercise 3: Create a Courses Table

Create a table named `courses` with the following columns:

| Column       | Suggested Data Type |
| ------------ | ------------------- |
| course_id    | INTEGER             |
| course_name  | VARCHAR(100)        |
| credit_hours | INTEGER             |
| course_fee   | NUMERIC(10,2)       |
| is_available | BOOLEAN             |

## 9. Review Questions

1. What is a data type?
2. Why do we define data types when creating a table?
3. Which data type is used to store whole numbers?
4. What is the difference between VARCHAR and TEXT?
5. Which data type is suitable for storing student fees?
6. Which data type is used to store dates?
7. What values can a BOOLEAN column store?
8. What does `NUMERIC(10,2)` mean?

## 10. Quick Revision

| Task                         | Data Type |
| ---------------------------- | --------- |
| Store student ID             | INTEGER   |
| Store student name           | VARCHAR   |
| Store department description | TEXT      |
| Store student fee            | NUMERIC   |
| Store admission date         | DATE      |
| Store active status          | BOOLEAN   |

Key Takeaway: A data type defines what kind of information a database column can store. Selecting the appropriate data type is an important step when designing database tables.

Next Lesson: Constraints in PostgreSQL — NOT NULL, UNIQUE, PRIMARY KEY, DEFAULT, and CHECK.