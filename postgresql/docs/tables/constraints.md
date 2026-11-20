# Constraints in PostgreSQL

## 1. Introduction

In PostgreSQL, constraints are rules applied to table columns to control the type of data that can be stored.

Constraints help maintain accurate, valid, and reliable data in a database.

For example:

- A student's name should not be empty.
- Every student should have a unique student ID.
- A student's age should be within a valid range.
- A student should belong to an existing department.

These rules can be implemented using constraints.

## 2. Types of Constraints

PostgreSQL provides several commonly used constraints:

| Constraint    | Purpose                                             |
| ------------- | --------------------------------------------------- |
| `NOT NULL`    | Prevents a column from storing NULL values.         |
| `UNIQUE`      | Prevents duplicate values.                          |
| `PRIMARY KEY` | Uniquely identifies each row.                       |
| `FOREIGN KEY` | Links records between tables.                       |
| `CHECK`       | Ensures values meet a specified condition.          |
| `DEFAULT`     | Provides a default value when no value is supplied. |

## 3. NOT NULL Constraint

The `NOT NULL` constraint ensures that a column must have a value.

Real-life example: Every student must have a name.

```
CREATE TABLE students (
    student_id INTEGER,
    student_name VARCHAR(100) NOT NULL
);
```

In this example:

- `student_id` can contain a NULL value.
- `student_name` cannot contain a NULL value.

Example:

```
INSERT INTO students (student_id, student_name)
VALUES (1, 'Ali');
```

This query works successfully.

The following query produces an error because the student name is missing:

```
INSERT INTO students (student_id, student_name)
VALUES (2, NULL);
```

## 4. UNIQUE Constraint

The `UNIQUE` constraint ensures that values in a column are not duplicated.

Real-life example: Every student should have a different email address.

```
CREATE TABLE students (
    student_id INTEGER,
    email VARCHAR(100) UNIQUE
);
```

Example:

```
INSERT INTO students (student_id, email)
VALUES (1, 'ali@example.com');

INSERT INTO students (student_id, email)
VALUES (2, 'ahmad@example.com');
```

Both records can be inserted because their email addresses are different.

However, inserting the same email address again will produce an error.

```
INSERT INTO students (student_id, email)
VALUES (3, 'ali@example.com');
```

Important: PostgreSQL allows multiple NULL values in a column with a regular `UNIQUE` constraint.

## 5. PRIMARY KEY Constraint

A `PRIMARY KEY` uniquely identifies every record in a table.

For example, every student has a unique student ID.

```
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    student_name VARCHAR(100)
);
```

Important points:

- A primary key cannot contain NULL values.
- A primary key cannot contain duplicate values.
- A table can have only one primary key constraint.
- A primary key can consist of one or more columns.

Example:

```
INSERT INTO students (student_id, student_name)
VALUES (1, 'Ali');

INSERT INTO students (student_id, student_name)
VALUES (2, 'Ahmad');
```

Both records are valid because their IDs are different.

The following query produces an error because the ID is duplicated:

```
INSERT INTO students (student_id, student_name)
VALUES (1, 'Usman');
```

## 6. FOREIGN KEY Constraint

A `FOREIGN KEY` connects two tables and ensures that a value in one table refers to an existing record in another table.

Real-life example: A student belongs to a department. The department must already exist in the university database.

First, create the departments table:

```
CREATE TABLE departments (
    department_id INTEGER PRIMARY KEY,
    department_name VARCHAR(100)
);
```

Insert some departments:

```
INSERT INTO departments
VALUES
(1, 'Computer Science'),
(2, 'Information Technology'),
(3, 'Mathematics');
```

Now create the students table:

```
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    student_name VARCHAR(100),
    department_id INTEGER REFERENCES departments(department_id)
);
```

Insert a student:

```
INSERT INTO students
VALUES (101, 'Ali', 1);
```

This query works because department ID `1` exists in the departments table.

The following query produces an error because department ID `5` does not exist:

```
INSERT INTO students
VALUES (102, 'Ahmad', 5);
```

Important: A foreign key helps maintain referential integrity between related tables.

## 7. CHECK Constraint

The `CHECK` constraint ensures that values satisfy a specified condition.

Real-life example: A student's age must be at least 16.

```
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    student_name VARCHAR(100),
    age INTEGER CHECK (age >= 16)
);
```

Example:

```
INSERT INTO students
VALUES (1, 'Ali', 20);
```

This query works because the age is greater than or equal to 16.

The following query produces an error:

```
INSERT INTO students
VALUES (2, 'Ahmad', 12);
```

The age does not satisfy the condition.

You can also apply a CHECK constraint to fees:

```
fee NUMERIC(10, 2) CHECK (fee >= 0)
```

This ensures that the fee cannot be negative.

## 8. DEFAULT Constraint

The `DEFAULT` constraint automatically provides a value when a user does not supply one during insertion.

Real-life example: Every new student is considered active by default.

```
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    student_name VARCHAR(100),
    is_active BOOLEAN DEFAULT TRUE
);
```

Example:

```
INSERT INTO students (student_id, student_name)
VALUES (1, 'Ali');
```

The database automatically assigns `TRUE` to `is_active`.

To view the record:

```
SELECT * FROM students;
```

You can also provide a different value explicitly:

```
INSERT INTO students
VALUES (2, 'Ahmad', FALSE);
```

## 9. Complete Practical Example

Let's create a students table using multiple constraints.

```
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    age INTEGER CHECK (age >= 16),
    fee NUMERIC(10, 2) DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE
);
```

Insert student records:

```
INSERT INTO students
    (student_id, student_name, email, age, fee)
VALUES
    (1, 'Ali', 'ali@example.com', 20, 50000),
    (2, 'Ahmad', 'ahmad@example.com', 22, 45000);
```

Display all records:

```
SELECT * FROM students;
```

This table uses five constraints:

- `PRIMARY KEY` for student identification.
- `NOT NULL` for the student name.
- `UNIQUE` for the email address.
- `CHECK` for age validation.
- `DEFAULT` for fee and active status.

## 10. Adding Constraints to an Existing Table

Constraints can also be added after creating a table using `ALTER TABLE`.

For example, add a UNIQUE constraint to the email column:

```
ALTER TABLE students
ADD CONSTRAINT unique_student_email UNIQUE (email);
```

Add a CHECK constraint:

```
ALTER TABLE students
ADD CONSTRAINT check_student_age CHECK (age >= 16);
```

Note: These commands will fail if existing records violate the new constraints.

## 11. Practice Exercises

Exercise 1: Create a Students Table

Create a table named `students` with these columns:

- `student_id` — INTEGER
- `student_name` — VARCHAR(100)
- `email` — VARCHAR(100)
- `age` — INTEGER

Apply the following constraints:

- `student_id` should be the PRIMARY KEY.
- `student_name` should be NOT NULL.
- `email` should be UNIQUE.
- `age` must be greater than or equal to 16.

Exercise 2: Create a Courses Table

Create a table named `courses` with:

- `course_id` — INTEGER PRIMARY KEY
- `course_name` — VARCHAR(100) NOT NULL
- `credit_hours` — INTEGER CHECK (credit_hours > 0)
- `course_fee` — NUMERIC(10, 2) DEFAULT 0

Exercise 3: Create Related Tables

Create two tables:

1. `departments`
2. `teachers`

Apply a PRIMARY KEY to each table and use a FOREIGN KEY in the `teachers` table to reference the `departments` table.

Exercise 4: Test Constraints

Try inserting:

- Two students with the same student ID.
- Two students with the same email.
- A student without a name.
- A student with age 10.

Observe which queries work and which produce errors.

## 12. Review Questions

1. What is a constraint in PostgreSQL?
2. What is the purpose of the NOT NULL constraint?
3. What is the difference between UNIQUE and PRIMARY KEY?
4. Why do we use a FOREIGN KEY?
5. What is the purpose of the CHECK constraint?
6. What happens when a DEFAULT value is not provided?
7. Can a table have more than one PRIMARY KEY constraint?
8. Which SQL command is used to add a constraint to an existing table?

## 13. Quick Revision

| Constraint  | Remember                           |
| ----------- | ---------------------------------- |
| NOT NULL    | Value is required.                 |
| UNIQUE      | No duplicate non-NULL values.      |
| PRIMARY KEY | Unique identification of each row. |
| FOREIGN KEY | Connects related tables.           |
| CHECK       | Validates a condition.             |
| DEFAULT     | Supplies a value automatically.    |

Next Lesson: INSERT INTO Statement in PostgreSQL

Students will learn how to insert single and multiple records into database tables.