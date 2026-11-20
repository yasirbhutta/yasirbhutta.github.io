# Student Notes: PostgreSQL Constraints in Depth

## 1. Introduction

In PostgreSQL, constraints are rules applied to table columns to maintain the accuracy and reliability of data.

For example, consider a university student table.

We may want to ensure that:

- Every student has a unique student ID.
- A student's name cannot be empty.
- Every student has a valid email address.
- A student's age cannot be negative.
- A student belongs to an existing department.

We can enforce these rules using PostgreSQL constraints.

## 2. What Is a Constraint?

A constraint is a rule that controls what data can be stored in a table.

If someone tries to insert or update data that violates a constraint, PostgreSQL rejects the operation.

For example:

```
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    age INT CHECK (age >= 16)
);
```

This table has three constraints:

1. `PRIMARY KEY`: Student ID must be unique and not null.
2. `NOT NULL`: Student name cannot be null.
3. `CHECK`: Student age must be at least 16.

## 3. Types of Constraints in PostgreSQL

PostgreSQL provides several important constraints.

| Constraint    | Purpose                                           |
| ------------- | ------------------------------------------------- |
| `PRIMARY KEY` | Uniquely identifies each record                   |
| `FOREIGN KEY` | Maintains relationships between tables            |
| `UNIQUE`      | Prevents duplicate values                         |
| `NOT NULL`    | Prevents null values                              |
| `CHECK`       | Ensures values satisfy a condition                |
| `DEFAULT`     | Provides a default value when one is not supplied |

Let's understand each constraint with practical examples.

## 4. PRIMARY KEY Constraint

A primary key uniquely identifies every record in a table.

For example, a university may assign a unique student ID to each student.

Example:

```
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100),
    department VARCHAR(100)
);
```

Insert records:

```
INSERT INTO students
VALUES
(1, 'Ali', 'Computer Science'),
(2, 'Ahmed', 'Information Technology'),
(3, 'Sara', 'Mathematics');
```

The following insertion will fail because student ID `1` already exists:

```
INSERT INTO students
VALUES (1, 'Usman', 'Physics');
```

Important characteristics:

- A primary key cannot contain duplicate values.
- A primary key cannot contain `NULL`.
- A table can have only one primary key constraint.
- A primary key can contain multiple columns. This is called a composite primary key.

## 5. Composite Primary Key

A composite primary key consists of two or more columns that together uniquely identify a record.

Consider a student enrollment table.

A student can enroll in multiple courses, and a course can have multiple students.

```
CREATE TABLE enrollments (
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    PRIMARY KEY (student_id, course_id)
);
```

Here, the combination of `student_id` and `course_id` must be unique.

The following records are allowed:

| student_id | course_id |
| ---------- | --------- |
| 1          | 101       |
| 1          | 102       |
| 2          | 101       |

But this record is not allowed because the combination already exists:

```
INSERT INTO enrollments
VALUES (1, 101, '2026-11-09');
```

## 6. FOREIGN KEY Constraint

A foreign key establishes a relationship between two tables.

For example:

- `departments` stores department information.
- `students` stores student information.
- Every student belongs to a department.

First, create the departments table:

```
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100)
);
```

Insert departments:

```
INSERT INTO departments
VALUES
(1, 'Computer Science'),
(2, 'Mathematics'),
(3, 'Physics');
```

Now create the students table:

```
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100),
    department_id INT,
    FOREIGN KEY (department_id)
    REFERENCES departments(department_id)
);
```

Insert students:

```
INSERT INTO students
VALUES
(101, 'Ali', 1),
(102, 'Ahmed', 2),
(103, 'Sara', 1);
```

The `department_id` in the students table must refer to an existing department.

For example, this insertion will fail if department `10` does not exist:

```
INSERT INTO students
VALUES (104, 'Usman', 10);
```

Remember: A foreign key can contain `NULL` unless the column also has a `NOT NULL` constraint.

## 7. ON DELETE Options in FOREIGN KEY

Suppose a department has students. What happens if someone tries to delete that department?

PostgreSQL provides different foreign key actions.

| Option        | Purpose                                                          |
| ------------- | ---------------------------------------------------------------- |
| `RESTRICT`    | Prevent deletion while referencing records exist                 |
| `NO ACTION`   | Check the relationship constraint when the constraint is checked |
| `CASCADE`     | Delete related child records automatically                       |
| `SET NULL`    | Set referencing foreign key values to NULL                       |
| `SET DEFAULT` | Set referencing foreign key values to their default              |

Example: ON DELETE CASCADE

```
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100)
);
```

```
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100),
    department_id INT,
    FOREIGN KEY (department_id)
    REFERENCES departments(department_id)
    ON DELETE CASCADE
);
```

Now, deleting a department also deletes students associated with it.

```
DELETE FROM departments
WHERE department_id = 1;
```

Use carefully

`ON DELETE CASCADE` can delete many related records automatically.

## 8. UNIQUE Constraint

The `UNIQUE` constraint prevents duplicate values in a column or combination of columns.

For example, each student should have a unique email address.

```
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100),
    email VARCHAR(150) UNIQUE
);
```

Insert records:

```
INSERT INTO students
VALUES
(1, 'Ali', 'ali@example.com'),
(2, 'Ahmed', 'ahmed@example.com');
```

This insertion will fail because the email already exists:

```
INSERT INTO students
VALUES
(3, 'Sara', 'ali@example.com');
```

Important: By default, PostgreSQL allows multiple `NULL` values in a `UNIQUE` column because `NULL` values are treated as distinct for uniqueness checks.

If you want to prevent null values too, combine `UNIQUE` with `NOT NULL`.

## 9. UNIQUE Constraint on Multiple Columns

We can apply a unique constraint to a combination of columns.

For example, a student may enroll in different semesters, but should not have duplicate enrollment records for the same course in the same semester.

```
CREATE TABLE course_enrollments (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    semester VARCHAR(30),
    UNIQUE (student_id, course_id, semester)
);
```

The combination of all three columns must be unique.

## 10. NOT NULL Constraint

The `NOT NULL` constraint ensures that a column must contain a value.

Example:

```
CREATE TABLE teachers (
    teacher_id INT PRIMARY KEY,
    teacher_name VARCHAR(100) NOT NULL,
    email VARCHAR(150)
);
```

The following insertion will fail:

```
INSERT INTO teachers
(teacher_id, email)
VALUES
(1, 'teacher@example.com');
```

The reason is that `teacher_name` is required.

Important: `NOT NULL` prevents missing values, but it does not prevent empty strings such as `''`.

## 11. CHECK Constraint

The `CHECK` constraint ensures that data satisfies a specified condition.

For example, student age must be at least 16.

```
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100),
    age INT CHECK (age >= 16)
);
```

This insertion is allowed:

```
INSERT INTO students
VALUES (1, 'Ali', 20);
```

This insertion is rejected:

```
INSERT INTO students
VALUES (2, 'Ahmed', 12);
```

### More CHECK Examples

Salary must be greater than zero:

```
salary NUMERIC(10,2) CHECK (salary > 0)
```

Marks must be between 0 and 100:

```
marks INT CHECK (marks BETWEEN 0 AND 100)
```

Gender must be one of the specified values:

```
gender VARCHAR(10)
CHECK (gender IN ('Male', 'Female', 'Other'))
```

Important: A `CHECK` constraint passes when its expression evaluates to `TRUE` or `NULL`. Use `NOT NULL` as well if a value is required.

## 12. DEFAULT Constraint

The `DEFAULT` constraint provides a value automatically when an INSERT statement does not supply a value for that column.

Example:

```
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100),
    admission_status VARCHAR(20) DEFAULT 'Pending'
);
```

Insert a student:

```
INSERT INTO students
(student_id, student_name)
VALUES
(1, 'Ali');
```

The database automatically assigns:

```
admission_status = Pending
```

We can also provide a default date:

```
admission_date DATE DEFAULT CURRENT_DATE
```

Important: A default value is used when a column is omitted from the INSERT statement or when `DEFAULT` is explicitly specified. Inserting `NULL` does not automatically use the default.

## 13. Naming Constraints

We can assign meaningful names to constraints using `CONSTRAINT`.

Example:

```
CREATE TABLE students (
    student_id INT,
    student_name VARCHAR(100) NOT NULL,

    CONSTRAINT pk_students
    PRIMARY KEY (student_id),

    CONSTRAINT uq_students_email
    UNIQUE (student_name)
);
```

Meaningful constraint names make database maintenance easier.

A more appropriate example using an email column:

```
CREATE TABLE students (
    student_id INT,
    student_name VARCHAR(100) NOT NULL,
    email VARCHAR(150),

    CONSTRAINT pk_students
    PRIMARY KEY (student_id),

    CONSTRAINT uq_students_email
    UNIQUE (email)
);
```

## 14. Adding a Constraint Using ALTER TABLE

We can add constraints to an existing table.

Suppose we already have a table:

```
CREATE TABLE students (
    student_id INT,
    student_name VARCHAR(100),
    age INT
);
```

Now add a primary key:

```
ALTER TABLE students
ADD CONSTRAINT pk_students
PRIMARY KEY (student_id);
```

Add a unique constraint:

```
ALTER TABLE students
ADD CONSTRAINT uq_students_name
UNIQUE (student_name);
```

Add a check constraint:

```
ALTER TABLE students
ADD CONSTRAINT chk_students_age
CHECK (age >= 16);
```

Add a foreign key:

```
ALTER TABLE students
ADD CONSTRAINT fk_students_department
FOREIGN KEY (department_id)
REFERENCES departments(department_id);
```

The last command requires a `department_id` column to exist in the `students` table.

## 15. Adding NOT NULL to an Existing Column

We can use `ALTER TABLE` to make an existing column mandatory.

```
ALTER TABLE students
ALTER COLUMN student_name
SET NOT NULL;
```

Before running this command, ensure that no existing records contain `NULL` in `student_name`.

To allow null values again:

```
ALTER TABLE students
ALTER COLUMN student_name
DROP NOT NULL;
```

## 16. Adding a DEFAULT to an Existing Column

We can add a default value to an existing column.

```
ALTER TABLE students
ALTER COLUMN age
SET DEFAULT 18;
```

Now, if a new record is inserted without an age value, PostgreSQL uses `18`.

To remove the default:

```
ALTER TABLE students
ALTER COLUMN age
DROP DEFAULT;
```

## 17. Removing a Constraint

We can remove a named constraint using `DROP CONSTRAINT`.

Syntax:

```
ALTER TABLE table_name
DROP CONSTRAINT constraint_name;
```

Example:

```
ALTER TABLE students
DROP CONSTRAINT chk_students_age;
```

This removes the age check constraint.

To remove a primary key:

```
ALTER TABLE students
DROP CONSTRAINT pk_students;
```

Note: PostgreSQL automatically generates names for unnamed constraints. You can inspect the actual names before removing them.

## 18. Viewing Constraints in PostgreSQL

We can use the following SQL query to view constraints in the current database:

```
SELECT
    constraint_name,
    table_name,
    constraint_type
FROM information_schema.table_constraints
WHERE table_schema = 'public'
ORDER BY table_name, constraint_name;
```

Common constraint types include:

| Constraint type | Meaning           |
| --------------- | ----------------- |
| `PRIMARY KEY`   | Primary key       |
| `FOREIGN KEY`   | Foreign key       |
| `UNIQUE`        | Unique constraint |
| `CHECK`         | Check constraint  |

For a quick overview in the `psql` terminal:

```
\d students
```

This displays the table structure, including its constraints.

## 19. Practical Example: University Database

Let's create a small university database structure using different constraints.

Step 1: Create departments table

```
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL UNIQUE
);
```

Step 2: Insert departments

```
INSERT INTO departments
VALUES
(1, 'Computer Science'),
(2, 'Mathematics'),
(3, 'Physics');
```

Step 3: Create students table

```
CREATE TABLE students (
    student_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE,
    age INT CHECK (age >= 16),
    department_id INT,
    admission_status VARCHAR(20) DEFAULT 'Pending',

    CONSTRAINT fk_students_department
    FOREIGN KEY (department_id)
    REFERENCES departments(department_id)
);
```

Step 4: Insert student records

```
INSERT INTO students
(student_name, email, age, department_id)
VALUES
('Ali', 'ali@example.com', 20, 1),
('Ahmed', 'ahmed@example.com', 21, 2),
('Sara', 'sara@example.com', 19, 1);
```

Step 5: View student records

```
SELECT *
FROM students;
```

Step 6: Test the constraints

Try these operations separately:

```
-- Duplicate email
INSERT INTO students
(student_name, email, age, department_id)
VALUES
('Usman', 'ali@example.com', 22, 1);
```

```
-- Invalid age
INSERT INTO students
(student_name, email, age, department_id)
VALUES
('Usman', 'usman@example.com', 12, 1);
```

```
-- Invalid department
INSERT INTO students
(student_name, email, age, department_id)
VALUES
('Usman', 'usman@example.com', 22, 99);
```

Each operation should fail because it violates a different constraint.

## 20. Common Mistakes

1. Creating a primary key on a column that already contains duplicate values.
2. Adding `NOT NULL` when existing records contain null values.
3. Creating a foreign key before the referenced table or column exists.
4. Inserting a foreign key value that does not exist in the parent table.
5. Using `CASCADE` without understanding its effects.
6. Assuming `DEFAULT` replaces explicitly inserted `NULL`.
7. Forgetting that a `CHECK` constraint can accept `NULL` unless `NOT NULL` is also applied.

## 21. Practice Exercises

### Beginner Level

1. Create a table named `students` with a primary key.
2. Make `student_name` a required column.
3. Add a unique constraint to the email column.
4. Add a check constraint requiring age to be at least 16.
5. Add a default value of `Pending` to admission status.

### Intermediate Level

6. Create a `departments` table.
7. Create a foreign key from `students.department_id` to `departments.department_id`.
8. Add a constraint that marks must be between 0 and 100.
9. Add a unique constraint on a combination of two columns.
10. Add a primary key to an existing table using `ALTER TABLE`.
11. Remove a check constraint.
12. Change a column from nullable to `NOT NULL`.

### Advanced Level

13. Create a university database structure with departments, students, courses, and enrollments.
14. Apply primary and foreign key constraints.
15. Apply `ON DELETE CASCADE` to an appropriate relationship.
16. Test `ON DELETE RESTRICT` and `ON DELETE SET NULL`.
17. Create meaningful names for all constraints.
18. Display all constraints using `information_schema`.
19. Explain why `UNIQUE` and `PRIMARY KEY` are different.
20. Design a table that uses all six major constraint types.

## 22. Review Questions

1. What is a constraint in PostgreSQL?
2. What is the purpose of a primary key?
3. What is a composite primary key?
4. What is the purpose of a foreign key?
5. What is the difference between `PRIMARY KEY` and `UNIQUE`?
6. What does `NOT NULL` do?
7. What is the purpose of `CHECK`?
8. What is the purpose of `DEFAULT`?
9. What is the difference between `ON DELETE CASCADE` and `ON DELETE SET NULL`?
10. How can we add a constraint to an existing table?
11. How can we remove a constraint?
12. Why should we give meaningful names to constraints?

## 23. Quick Revision

| Constraint    | Main purpose                 |
| ------------- | ---------------------------- |
| `PRIMARY KEY` | Unique record identification |
| `FOREIGN KEY` | Table relationship           |
| `UNIQUE`      | Prevent duplicate values     |
| `NOT NULL`    | Require a value              |
| `CHECK`       | Validate a condition         |
| `DEFAULT`     | Provide a default value      |

Important SQL commands:

```
-- Add a constraint
ALTER TABLE students
ADD CONSTRAINT chk_age CHECK (age >= 16);

-- Remove a constraint
ALTER TABLE students
DROP CONSTRAINT chk_age;

-- Set NOT NULL
ALTER TABLE students
ALTER COLUMN student_name SET NOT NULL;

-- Set DEFAULT
ALTER TABLE students
ALTER COLUMN admission_status SET DEFAULT 'Pending';
```

Next Lesson: PostgreSQL Views in Depth

Students will learn how to create views, update views, replace views, delete views, and use views to simplify complex SQL queries.