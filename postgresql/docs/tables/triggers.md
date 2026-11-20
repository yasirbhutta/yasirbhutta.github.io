# Student Notes: Triggers in PostgreSQL

## 1. Introduction

Imagine a university database that stores student records.

Whenever a student is added, updated, or deleted, the university may want to automatically record that activity.

For example:

- When a new student is added, record the insertion.
- When a student's marks are changed, save the old and new marks.
- When a student record is deleted, maintain a record of the deletion.
- When marks are entered, check that they are between 0 and 100.

Can PostgreSQL perform these tasks automatically?

Yes. PostgreSQL uses Triggers to perform actions automatically when specified database events occur.

## 2. What is a Trigger?

A Trigger is a database mechanism that automatically executes a specified function when a particular event occurs on a table or view.

In simple words:

A trigger tells PostgreSQL:

"When a particular database operation happens, automatically perform this action."

For example:

```
-- Automatically execute an action
-- whenever a new student is inserted.
```

A trigger is associated with a table or view.

Important: In PostgreSQL, a trigger executes a special function called a Trigger Function.

## 3. Why Do We Use Triggers?

Triggers are useful for automating database tasks.

Common uses include:

| Purpose            | Example                            |
| ------------------ | ---------------------------------- |
| Audit records      | Record when a student is added     |
| Data validation    | Ensure marks are between 0 and 100 |
| Automatic updates  | Update a modified timestamp        |
| Change tracking    | Save old and new marks             |
| Related operations | Update another table automatically |

Note: Triggers should be used carefully because automatic actions can make database behavior harder to understand and debug.

## 4. Types of Trigger Events

PostgreSQL supports the following main trigger events:

| Event    | Description                                 |
| -------- | ------------------------------------------- |
| INSERT   | When a new record is inserted               |
| UPDATE   | When an existing record is updated          |
| DELETE   | When a record is deleted                    |
| TRUNCATE | When all records are removed using TRUNCATE |

For example:

```
INSERT INTO students
VALUES (4, 'Usman', 'Physics', 78);
```

An INSERT trigger can automatically execute when this statement runs.

## 5. When Does a Trigger Execute?

PostgreSQL provides different trigger timings.

### 5.1 BEFORE Trigger

A BEFORE trigger executes before the database operation is completed.

It is commonly used for:

- Validating data.
- Modifying values before saving.
- Checking business rules.

Example:

```
BEFORE INSERT ON students
```

### 5.2 AFTER Trigger

An AFTER trigger executes after the database operation has taken place.

It is commonly used for:

- Recording audit information.
- Tracking changes.
- Performing related operations.

Example:

```
AFTER INSERT ON students
```

### 5.3 INSTEAD OF Trigger

An INSTEAD OF trigger executes instead of the requested operation.

It is mainly used with views.

For example, it can handle an INSERT operation on a view by performing the appropriate operation on its underlying tables.

## 6. Row-Level and Statement-Level Triggers

PostgreSQL provides two trigger execution levels.

### Row-Level Trigger

A row-level trigger executes separately for every affected row.

```
FOR EACH ROW
```

Example:

If an UPDATE statement modifies five student records, the trigger executes five times.

### Statement-Level Trigger

A statement-level trigger executes once for the entire SQL statement.

```
FOR EACH STATEMENT
```

Example:

If an UPDATE statement modifies five student records, the trigger executes only once.

| Row-Level                         | Statement-Level                                 |
| --------------------------------- | ----------------------------------------------- |
| Executes for each affected row    | Executes once per SQL statement                 |
| Uses `FOR EACH ROW`               | Uses `FOR EACH STATEMENT`                       |
| Can access OLD and NEW row values | Cannot access individual OLD and NEW row values |

## 7. Create a Sample Students Table

We will use a students table to understand triggers.

### Step 1: Create the Table

```
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    department VARCHAR(50),
    marks INT
);
```

### Step 2: Insert Sample Records

```
INSERT INTO students
VALUES
(1, 'Ali', 'Computer Science', 85),
(2, 'Sara', 'Mathematics', 72),
(3, 'Ahmed', 'Computer Science', 65);
```

### Step 3: Display Records

```
SELECT * FROM students;
```

Expected output:

| student_id | student_name | department       | marks |
| ---------- | ------------ | ---------------- | ----- |
| 1          | Ali          | Computer Science | 85    |
| 2          | Sara         | Mathematics      | 72    |
| 3          | Ahmed        | Computer Science | 65    |

## 8. What is a Trigger Function?

A trigger function is a special PostgreSQL function that contains the instructions to be executed by a trigger.

Unlike an ordinary function, a trigger function:

- Must return the `TRIGGER` data type.
- Is executed through a trigger.
- Can access special variables such as `NEW` and `OLD`.

### Basic Syntax

```
CREATE OR REPLACE FUNCTION function_name()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN

    -- Write trigger instructions here

    RETURN NEW;

END;
$$;
```

Understanding the syntax:

| Keyword                      | Purpose                                 |
| ---------------------------- | --------------------------------------- |
| `CREATE OR REPLACE FUNCTION` | Creates or replaces a function          |
| `RETURNS TRIGGER`            | Specifies that it is a trigger function |
| `LANGUAGE plpgsql`           | Uses PostgreSQL's procedural language   |
| `BEGIN`                      | Starts the function body                |
| `RETURN NEW`                 | Returns the new row                     |
| `END`                        | Ends the function body                  |

## 9. Understanding NEW and OLD

PostgreSQL provides two special variables inside row-level trigger functions.

### NEW

`NEW` represents the new row being inserted or updated.

Example:

```
NEW.student_name
NEW.marks
NEW.department
```

### OLD

`OLD` represents the existing row before an update or deletion.

Example:

```
OLD.student_name
OLD.marks
OLD.department
```

### Difference Between NEW and OLD

| Operation | NEW           | OLD           |
| --------- | ------------- | ------------- |
| INSERT    | New row       | Not available |
| UPDATE    | Updated row   | Previous row  |
| DELETE    | Not available | Deleted row   |

For example, when marks change from 70 to 85:

- `OLD.marks` = 70
- `NEW.marks` = 85

This makes it possible to track changes in student records.

## 10. Create Your First Trigger: Record Student Insertions

Suppose we want PostgreSQL to automatically record every new student added to the students table.

We will create an audit table and a trigger.

### Step 1: Create an Audit Table

```
CREATE TABLE student_audit (
    audit_id SERIAL PRIMARY KEY,
    student_id INT,
    action TEXT,
    action_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

This table stores information about student activities.

### Step 2: Create a Trigger Function

```
CREATE OR REPLACE FUNCTION log_student_insert()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN

    INSERT INTO student_audit(student_id, action)
    VALUES (NEW.student_id, 'INSERT');

    RETURN NEW;

END;
$$;
```

Understanding the code:

1. The function is named `log_student_insert()`.
2. It returns `TRIGGER`.
3. `NEW.student_id` accesses the ID of the newly inserted student.
4. The INSERT statement records the activity in `student_audit`.
5. `RETURN NEW` returns the new row.

### Step 3: Create the Trigger

```
CREATE TRIGGER student_insert_trigger
AFTER INSERT ON students
FOR EACH ROW
EXECUTE FUNCTION log_student_insert();
```

Understanding the code:

| Part                     | Meaning                        |
| ------------------------ | ------------------------------ |
| `CREATE TRIGGER`         | Creates a trigger              |
| `student_insert_trigger` | Trigger name                   |
| `AFTER INSERT`           | Executes after insertion       |
| `ON students`            | Attached to the students table |
| `FOR EACH ROW`           | Executes for each inserted row |
| `EXECUTE FUNCTION`       | Calls the trigger function     |

### Step 4: Test the Trigger

Insert a new student:

```
INSERT INTO students
VALUES (4, 'Usman', 'Physics', 78);
```

Now check the audit table:

```
SELECT * FROM student_audit;
```

Expected output:

| audit_id | student_id | action |
| -------- | ---------- | ------ |
| 1        | 4          | INSERT |

Result

The trigger automatically recorded the insertion. We did not manually insert anything into the audit table.

## 11. Create a BEFORE Trigger for Data Validation

Suppose student marks must always be between 0 and 100.

We can use a BEFORE trigger to validate marks before saving a record.

### Step 1: Create the Trigger Function

```
CREATE OR REPLACE FUNCTION validate_student_marks()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN

    IF NEW.marks < 0 OR NEW.marks > 100 THEN

        RAISE EXCEPTION
        'Marks must be between 0 and 100';

    END IF;

    RETURN NEW;

END;
$$;
```

Understanding the code:

- `NEW.marks` accesses the marks being inserted or updated.
- `IF` checks whether marks are outside the allowed range.
- `RAISE EXCEPTION` stops the operation and displays an error.
- `RETURN NEW` allows valid data to proceed.

### Step 2: Create the Trigger

```
CREATE TRIGGER check_student_marks
BEFORE INSERT OR UPDATE ON students
FOR EACH ROW
EXECUTE FUNCTION validate_student_marks();
```

This trigger executes before every INSERT or UPDATE operation on the students table.

### Step 3: Test with Valid Marks

```
INSERT INTO students
VALUES (5, 'Hina', 'Physics', 90);
```

Expected result: The record is inserted successfully.

### Step 4: Test with Invalid Marks

```
INSERT INTO students
VALUES (6, 'Bilal', 'Mathematics', 120);
```

Expected error:

```
ERROR: Marks must be between 0 and 100
```

The record will not be inserted.

## 12. Create a Trigger to Track Updated Marks

Suppose we want to maintain a record whenever a student's marks are changed.

We need to store:

- Student ID
- Previous marks
- New marks
- Date and time of change

### Step 1: Create an Audit Table

```
CREATE TABLE student_marks_audit (
    audit_id SERIAL PRIMARY KEY,
    student_id INT,
    old_marks INT,
    new_marks INT,
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Step 2: Create a Trigger Function

```
CREATE OR REPLACE FUNCTION log_marks_update()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN

    INSERT INTO student_marks_audit
    (student_id, old_marks, new_marks)

    VALUES
    (OLD.student_id, OLD.marks, NEW.marks);

    RETURN NEW;

END;
$$;
```

Here:

- `OLD.marks` stores the previous marks.
- `NEW.marks` stores the updated marks.

### Step 3: Create the Trigger

```
CREATE TRIGGER student_marks_update_trigger
AFTER UPDATE OF marks ON students
FOR EACH ROW
EXECUTE FUNCTION log_marks_update();
```

This trigger executes after the marks column is updated.

### Step 4: Update Student Marks

```
UPDATE students
SET marks = 95
WHERE student_id = 1;
```

### Step 5: Check the Audit Table

```
SELECT * FROM student_marks_audit;
```

Expected output:

| audit_id | student_id | old_marks | new_marks |
| -------- | ---------- | --------- | --------- |
| 1        | 1          | 85        | 95        |

The trigger automatically saved the previous and updated marks.

## 13. Create a Trigger to Record Deleted Students

Suppose we want to record the ID of every student whose record is deleted.

For DELETE operations, we use `OLD` because the deleted row is no longer available as a new row.

### Step 1: Create a Trigger Function

```
CREATE OR REPLACE FUNCTION log_student_delete()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN

    INSERT INTO student_audit(student_id, action)
    VALUES (OLD.student_id, 'DELETE');

    RETURN OLD;

END;
$$;
```

### Step 2: Create the Trigger

```
CREATE TRIGGER student_delete_trigger
AFTER DELETE ON students
FOR EACH ROW
EXECUTE FUNCTION log_student_delete();
```

### Step 3: Delete a Student

```
DELETE FROM students
WHERE student_id = 3;
```

### Step 4: Check the Audit Table

```
SELECT * FROM student_audit;
```

Expected output includes:

| student_id | action |
| ---------- | ------ |
| 4          | INSERT |
| 3          | DELETE |

The deletion is recorded automatically.

## 14. BEFORE vs AFTER Triggers

| BEFORE Trigger                            | AFTER Trigger                                           |
| ----------------------------------------- | ------------------------------------------------------- |
| Executes before the operation             | Executes after the operation                            |
| Can modify `NEW` values                   | Cannot change the already stored row through `NEW`      |
| Useful for validation                     | Useful for audit logging                                |
| Can stop the operation using an exception | Can also raise an exception and roll back the statement |

Important: The return value of an AFTER trigger is ignored. For BEFORE INSERT and UPDATE triggers, return `NEW` to allow the row operation to proceed. For BEFORE DELETE, return `OLD` to allow deletion.

## 15. Row-Level vs Statement-Level Example

### Row-Level Trigger

```
CREATE TRIGGER example_row_trigger
AFTER UPDATE ON students
FOR EACH ROW
EXECUTE FUNCTION log_marks_update();
```

This example illustrates row-level execution. The function should be designed for the relevant UPDATE operation.

### Statement-Level Trigger

A statement-level trigger executes once per SQL statement, regardless of how many rows are affected.

```
CREATE OR REPLACE FUNCTION show_update_notice()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN

    RAISE NOTICE 'Students table was updated';

    RETURN NULL;

END;
$$;
```

Create the trigger:

```
CREATE TRIGGER students_update_notice
AFTER UPDATE ON students
FOR EACH STATEMENT
EXECUTE FUNCTION show_update_notice();
```

Test:

```
UPDATE students
SET department = 'Computer Science'
WHERE marks > 70;
```

The notice appears once for the UPDATE statement, not once per updated student.

## 16. How to Delete a Trigger

If a trigger is no longer required, we can remove it using `DROP TRIGGER`.

### Syntax

```
DROP TRIGGER trigger_name ON table_name;
```

### Example

```
DROP TRIGGER student_insert_trigger ON students;
```

To avoid an error if the trigger does not exist:

```
DROP TRIGGER IF EXISTS student_insert_trigger ON students;
```

Important: A trigger is attached to a table. Therefore, the table name must be specified when dropping it.

The trigger function is a separate database object. It can be removed separately when it is no longer used:

```
DROP FUNCTION log_student_insert();
```

Do not drop a trigger function while an existing trigger still depends on it.

## 17. Enable and Disable a Trigger

PostgreSQL also allows us to temporarily disable or enable a trigger.

### Disable a Trigger

```
ALTER TABLE students
DISABLE TRIGGER student_insert_trigger;
```

### Enable a Trigger

```
ALTER TABLE students
ENABLE TRIGGER student_insert_trigger;
```

When a trigger is disabled, it does not execute for the relevant operations until it is enabled again.

## 18. Important Points to Remember

1. A trigger executes automatically when a specified database event occurs.
2. A trigger is attached to a table or view.
3. A trigger calls a trigger function.
4. A trigger function must return `TRIGGER`.
5. `NEW` represents the new row in INSERT and UPDATE operations.
6. `OLD` represents the previous row in UPDATE and DELETE operations.
7. BEFORE triggers are useful for validation and modifying data.
8. AFTER triggers are useful for audit logging.
9. `FOR EACH ROW` executes once for every affected row.
10. `FOR EACH STATEMENT` executes once for the entire SQL statement.
11. Trigger functions are not called directly using `SELECT` or `CALL`.
12. Trigger operations are part of the same transaction. If a trigger raises an exception, the triggering operation is rolled back.
13. TRUNCATE triggers are statement-level; PostgreSQL does not support row-level TRUNCATE triggers.

## 19. Practice Exercises

Try these exercises using the `students` table.

### Beginner Level

1. Create a trigger that displays a notice when a new student is inserted.
2. Create a BEFORE INSERT trigger to prevent negative marks.
3. Create a trigger that records student deletions in an audit table.

### Intermediate Level

4. Create a trigger that records old and new department names whenever a student's department changes.
5. Create a trigger that records the date and time whenever student marks are updated.
6. Create a statement-level trigger that displays a notice whenever the students table is updated.

### Advanced Level

7. Create an audit system that records INSERT, UPDATE, and DELETE operations.
8. Create a trigger that automatically converts student names to uppercase before insertion.
9. Create a trigger that prevents a student's marks from being reduced below their previous marks.

## 20. Review Questions

1. What is a trigger in PostgreSQL?
2. What is a trigger function?
3. Why do we use triggers?
4. What is the difference between BEFORE and AFTER triggers?
5. What is the purpose of `NEW`?
6. What is the purpose of `OLD`?
7. What is the difference between row-level and statement-level triggers?
8. Which trigger timing is commonly used for data validation?
9. How can we delete a trigger?
10. Can we call a trigger function directly using `CALL`?

## 21. Quick Revision

| Concept            | Description                                           |
| ------------------ | ----------------------------------------------------- |
| Trigger            | Automatically executes an action when an event occurs |
| Trigger Function   | Function executed by a trigger                        |
| INSERT             | New record is added                                   |
| UPDATE             | Existing record is modified                           |
| DELETE             | Record is removed                                     |
| BEFORE             | Executes before the operation                         |
| AFTER              | Executes after the operation                          |
| INSTEAD OF         | Replaces an operation, mainly on views                |
| NEW                | New row values                                        |
| OLD                | Previous or deleted row values                        |
| FOR EACH ROW       | Executes for each affected row                        |
| FOR EACH STATEMENT | Executes once per SQL statement                       |
| DROP TRIGGER       | Removes a trigger                                     |

## 22. Next Lesson

Next Topic: Common Table Expressions (CTEs) in PostgreSQL

In the next lesson, students will learn how to use the `WITH` clause to create temporary named query results and write more readable SQL queries.