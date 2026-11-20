# Sequences in PostgreSQL

## 1. Introduction

A Sequence is a database object in PostgreSQL that generates a series of numeric values automatically.

Sequences are commonly used to generate unique identification numbers for table records.

For example, consider a university database containing student records.

| student_id | student_name |
| ---------- | ------------ |
| 1          | Ali          |
| 2          | Ahmed        |
| 3          | Sara         |
| 4          | Ayesha       |
| 5          | Usman        |

Instead of manually entering a student ID for every new student, we can use a Sequence to generate these numbers automatically.

## 2. Why Do We Need Sequences?

Sequences are useful when:

1. We need automatically generated identification numbers.
2. We want unique numbers for new records.
3. We want to avoid manually assigning IDs.
4. We need an automatic numbering system for transactions, orders, and other records.

PostgreSQL sequences are independent database objects. They can be used by multiple tables or columns if required.

## 3. Create a Sequence

Use the `CREATE SEQUENCE` command.

Syntax:

```
CREATE SEQUENCE sequence_name;
```

Example:

```
CREATE SEQUENCE student_id_seq;
```

This creates a sequence named `student_id_seq`.

By default, a sequence starts at 1 and increases by 1.

## 4. Generate Values Using NEXTVAL

The `NEXTVAL()` function generates the next value from a sequence.

Example:

```
SELECT NEXTVAL('student_id_seq');
```

Expected result:

```
 nextval
---------
       1
```

Execute the same command again:

```
SELECT NEXTVAL('student_id_seq');
```

Expected result:

```
 nextval
---------
       2
```

Execute it again:

```
SELECT NEXTVAL('student_id_seq');
```

Expected result:

```
 nextval
---------
       3
```

Each call generates a new sequence value.

Remember: `NEXTVAL()` advances the sequence. It does not simply read the current value.

## 5. Get the Current Sequence Value Using CURRVAL

The `CURRVAL()` function returns the most recently generated value of a sequence in the current database session.

Example:

```
SELECT CURRVAL('student_id_seq');
```

If the last value generated in the current session was 3, the result will be:

```
 currval
---------
       3
```

Important: You must call `NEXTVAL()` at least once for that sequence in the current session before using `CURRVAL()`.

## 6. Create a Sequence with Custom Settings

We can specify the starting value and increment when creating a sequence.

Syntax:

```
CREATE SEQUENCE sequence_name
START WITH starting_value
INCREMENT BY increment_value;
```

Example:

```
CREATE SEQUENCE student_id_seq2
START WITH 100
INCREMENT BY 5;
```

Generate values:

```
SELECT NEXTVAL('student_id_seq2');
```

Expected values from successive calls:

| Call | Generated Value |
| ---- | --------------- |
| 1    | 100             |
| 2    | 105             |
| 3    | 110             |
| 4    | 115             |
| 5    | 120             |

## 7. Create a Sequence with Minimum and Maximum Values

We can also specify the minimum and maximum values.

```
CREATE SEQUENCE invoice_seq
START WITH 1
INCREMENT BY 1
MINVALUE 1
MAXVALUE 1000;
```

This sequence generates numbers from 1 to 1000.

After reaching the maximum value, PostgreSQL reports an error when another value is requested, because cycling is disabled by default.

## 8. Use a Sequence with a Table

Now let's create a student table and use a sequence to generate student IDs.

### Step 1: Create a table

```
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    student_name VARCHAR(100),
    email VARCHAR(100)
);
```

### Step 2: Create a sequence

```
CREATE SEQUENCE students_id_seq
START WITH 1
INCREMENT BY 1;
```

### Step 3: Insert records using NEXTVAL

```
INSERT INTO students (
    student_id,
    student_name,
    email
)
VALUES (
    NEXTVAL('students_id_seq'),
    'Ali',
    'ali@example.com'
);
```

Insert another record:

```
INSERT INTO students (
    student_id,
    student_name,
    email
)
VALUES (
    NEXTVAL('students_id_seq'),
    'Ahmed',
    'ahmed@example.com'
);
```

### Step 4: Retrieve records

```
SELECT *
FROM students;
```

Expected result:

| student_id | student_name | email              |
| ---------- | ------------ | ------------------ |
| 1          | Ali          | ali\@example.com   |
| 2          | Ahmed        | ahmed\@example.com |

The sequence automatically generates a new ID for each inserted record.

## 9. Use SERIAL with a Table

PostgreSQL provides the `SERIAL` data type as a convenient way to create an integer column that uses an automatically generated sequence.

Instead of creating a sequence separately, we can write:

```
CREATE TABLE departments (
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(100)
);
```

Now insert records without specifying `department_id`.

```
INSERT INTO departments (department_name)
VALUES ('Computer Science');
```

Insert another record:

```
INSERT INTO departments (department_name)
VALUES ('Information Technology');
```

Retrieve the records:

```
SELECT *
FROM departments;
```

PostgreSQL automatically generates the department IDs.

Important: `SERIAL` is PostgreSQL-specific shorthand. It creates an integer column with a sequence-backed default; it is not a true SQL data type.

## 10. Use IDENTITY Columns

PostgreSQL also supports identity columns, which provide a standard SQL approach to automatic number generation.

There are two identity options.

### A. GENERATED ALWAYS AS IDENTITY

```
CREATE TABLE teachers (
    teacher_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    teacher_name VARCHAR(100)
);
```

Insert records:

```
INSERT INTO teachers (teacher_name)
VALUES ('Muhammad Ali');
```

PostgreSQL automatically generates the `teacher_id`.

With `GENERATED ALWAYS`, PostgreSQL normally does not allow manually supplying an ID unless `OVERRIDING SYSTEM VALUE` is specified.

### B. GENERATED BY DEFAULT AS IDENTITY

```
CREATE TABLE courses (
    course_id INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    course_name VARCHAR(100)
);
```

Insert a record without specifying the ID:

```
INSERT INTO courses (course_name)
VALUES ('Database Systems');
```

We can also manually supply an ID:

```
INSERT INTO courses (course_id, course_name)
VALUES (100, 'Programming Fundamentals');
```

Difference:

| ALWAYS                                 | BY DEFAULT                     |
| -------------------------------------- | ------------------------------ |
| Automatically generates values         | Automatically generates values |
| Normally rejects manually supplied IDs | Allows manually supplied IDs   |
| Can override using special SQL syntax  | Manual value takes precedence  |

## 11. SERIAL vs. IDENTITY vs. SEQUENCE

| Feature                                  | SEQUENCE                    | SERIAL           | IDENTITY        |
| ---------------------------------------- | --------------------------- | ---------------- | --------------- |
| Type                                     | Independent database object | Column shorthand | Column property |
| Automatic value generation               | Requires configuration      | Yes              | Yes             |
| Can be used with tables                  | Yes                         | Yes              | Yes             |
| Requires a separate sequence declaration | Yes, if created manually    | No               | No              |
| Standard SQL approach                    | No                          | No               | Yes             |

Teaching tip: For beginners, first explain Sequence, then demonstrate `SERIAL`, and finally introduce `IDENTITY`.

## 12. Alter a Sequence

We can modify an existing sequence using `ALTER SEQUENCE`.

For example:

```
ALTER SEQUENCE student_id_seq
INCREMENT BY 2;
```

Now the sequence increases by 2 instead of 1.

We can also restart a sequence:

```
ALTER SEQUENCE student_id_seq
RESTART WITH 100;
```

The next call to `NEXTVAL()` will generate 100.

Caution: Restarting a sequence that is being used by an existing table can generate duplicate IDs if the new values overlap with existing records.

## 13. Delete a Sequence

Use `DROP SEQUENCE` to delete a sequence.

```
DROP SEQUENCE student_id_seq;
```

To avoid an error if the sequence does not exist:

```
DROP SEQUENCE IF EXISTS student_id_seq;
```

## 14. Important Sequence Functions

| Function    | Purpose                                                 |
| ----------- | ------------------------------------------------------- |
| `NEXTVAL()` | Generates the next sequence value                       |
| `CURRVAL()` | Returns the last generated value in the current session |
| `SETVAL()`  | Sets the current sequence value                         |

Example of `SETVAL()`:

```
SELECT SETVAL('student_id_seq', 100);
```

The next call to `NEXTVAL()` normally returns 101.

To make the next call return 100:

```
SELECT SETVAL('student_id_seq', 100, false);
```

## 15. Important Points About Sequences

1. Sequences generate numeric values.
2. Sequence values are not automatically rolled back when a transaction fails.
3. Gaps in sequence numbers are normal.
4. A sequence does not automatically guarantee uniqueness unless the generated value is protected by a `PRIMARY KEY` or `UNIQUE` constraint.
5. Multiple sessions can safely generate values from the same sequence.
6. Sequence values are not necessarily consecutive.

## 16. Practice Exercises

Complete the following exercises in PostgreSQL.

Exercise 1: Create a sequence named `employee_id_seq`.

Exercise 2: Generate five values using `NEXTVAL()`.

Exercise 3: Use `CURRVAL()` to retrieve the last generated value.

Exercise 4: Create a sequence starting from 500 and increasing by 10.

Exercise 5: Create a table named `employees` and use a sequence to generate employee IDs.

Exercise 6: Create a table named `students_serial` using the `SERIAL` data type.

Exercise 7: Create a table named `students_identity` using `GENERATED ALWAYS AS IDENTITY`.

Exercise 8: Create a table using `GENERATED BY DEFAULT AS IDENTITY`.

Exercise 9: Change the increment value of an existing sequence.

Exercise 10: Restart a sequence from 1000.

## 17. Review Questions

1. What is a Sequence in PostgreSQL?
2. Why do we use sequences?
3. What is the purpose of `NEXTVAL()`?
4. What is the difference between `NEXTVAL()` and `CURRVAL()`?
5. What is the purpose of `SETVAL()`?
6. What is the difference between `SERIAL` and `IDENTITY`?
7. What is the difference between `GENERATED ALWAYS` and `GENERATED BY DEFAULT`?
8. Why can gaps appear in sequence numbers?
9. Which command modifies an existing sequence?
10. Which command deletes a sequence?

## 18. Quick Revision

| Task                 | SQL Command                    |
| -------------------- | ------------------------------ |
| Create sequence      | `CREATE SEQUENCE`              |
| Generate next value  | `NEXTVAL()`                    |
| Get current value    | `CURRVAL()`                    |
| Set sequence value   | `SETVAL()`                     |
| Modify sequence      | `ALTER SEQUENCE`               |
| Restart sequence     | `RESTART WITH`                 |
| Delete sequence      | `DROP SEQUENCE`                |
| Automatic integer ID | `SERIAL`                       |
| Identity column      | `GENERATED ALWAYS AS IDENTITY` |

