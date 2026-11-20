# Student Notes: Stored Procedures in PostgreSQL

## 1. Introduction

Imagine a university needs to perform several operations when a student submits a fee payment:

1. Record the fee payment.
2. Update the student's outstanding balance.
3. Update the payment status.
4. Generate a confirmation message.

Instead of executing these SQL statements separately every time, we can group them into a reusable database program.

PostgreSQL provides Stored Procedures for this purpose.

## 2. What is a Stored Procedure?

A Stored Procedure is a reusable block of SQL and procedural code stored inside a database.

It can perform one or more database operations, such as:

- INSERT records.
- UPDATE records.
- DELETE records.
- Retrieve and process data.
- Perform calculations.
- Execute conditional operations.

Unlike a function, a procedure does not require a return value.

## 3. Why Do We Use Stored Procedures?

Stored procedures are useful because they:

1. Allow us to reuse database operations.
2. Reduce repeated SQL code.
3. Organize complex database tasks.
4. Support conditional logic and loops.
5. Help centralize business rules.
6. Can control transaction operations in suitable contexts.

## 4. Function vs Stored Procedure

Both functions and procedures allow us to write reusable database code, but they have different purposes.

| Function                                                          | Stored Procedure                                   |
| ----------------------------------------------------------------- | -------------------------------------------------- |
| Created using `CREATE FUNCTION`                                   | Created using `CREATE PROCEDURE`                   |
| Called using `SELECT` or within SQL expressions                   | Called using `CALL`                                |
| Must declare a return type                                        | Does not require a RETURNS clause                  |
| Returns a value or result set                                     | Performs operations and can use output parameters  |
| Can be used inside SELECT queries                                 | Cannot be used directly as a SELECT expression     |
| Cannot independently manage transactions using COMMIT or ROLLBACK | Can manage transactions in permitted CALL contexts |

Remember:

- Function: Performs a task and returns a result.
- Procedure: Performs a task, often involving multiple database operations.

## 5. Creating a Sample Table

Let's create a table named `students`.

```
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    department VARCHAR(50),
    marks INT
);
```

Insert sample records:

```
INSERT INTO students
VALUES
    (1, 'Ali', 'Computer Science', 85),
    (2, 'Sara', 'Mathematics', 72),
    (3, 'Ahmed', 'Computer Science', 65),
    (4, 'Usman', 'Physics', 45);
```

Display the records:

```
SELECT * FROM students;
```

## 6. Creating Your First Stored Procedure

Let's create a simple procedure that displays a message using PostgreSQL's `RAISE NOTICE`.

Syntax:

```
CREATE PROCEDURE procedure_name()
LANGUAGE plpgsql
AS $$
BEGIN
    -- SQL statements
END;
$$;
```

Example:

```
CREATE PROCEDURE welcome_message()
LANGUAGE plpgsql
AS $$
BEGIN
    RAISE NOTICE 'Welcome to PostgreSQL';
END;
$$;
```

Understand the code:

| Keyword             | Purpose                           |
| ------------------- | --------------------------------- |
| `CREATE PROCEDURE`  | Creates a procedure               |
| `welcome_message()` | Procedure name                    |
| `LANGUAGE plpgsql`  | Specifies the procedural language |
| `BEGIN`             | Starts the procedure body         |
| `RAISE NOTICE`      | Displays an informational message |
| `END`               | Ends the procedure body           |

## 7. Calling a Stored Procedure

We execute a stored procedure using the `CALL` command.

Syntax:

```
CALL procedure_name();
```

Example:

```
CALL welcome_message();
```

Expected message:

```
NOTICE: Welcome to PostgreSQL
```

Unlike a function, we do not call a procedure using SELECT.

## 8. Creating a Procedure with Parameters

A procedure can accept input values through parameters.

For example, let's create a procedure that displays a student's name.

```
CREATE PROCEDURE show_student(
    p_student_name VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    RAISE NOTICE 'Student Name: %', p_student_name;
END;
$$;
```

Call the procedure:

```
CALL show_student('Ali');
```

Expected message:

```
NOTICE: Student Name: Ali
```

Understand the code:

- `p_student_name` is an input parameter.
- `VARCHAR` defines its data type.
- `CALL` executes the procedure.
- `'Ali'` is passed as the input value.
- `%` is a placeholder in the RAISE NOTICE message.

## 9. Procedure to Insert a Student Record

Now let's create a practical procedure that inserts a new student into the table.

```
CREATE PROCEDURE add_student(
    p_student_id INT,
    p_student_name VARCHAR,
    p_department VARCHAR,
    p_marks INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO students (
        student_id,
        student_name,
        department,
        marks
    )
    VALUES (
        p_student_id,
        p_student_name,
        p_department,
        p_marks
    );

    RAISE NOTICE 'Student record inserted successfully';
END;
$$;
```

Execute the procedure:

```
CALL add_student(
    5,
    'Ayesha',
    'Mathematics',
    90
);
```

Check the table:

```
SELECT * FROM students;
```

Ayesha's record will now appear in the students table.

Important: If the student ID already exists, the primary key constraint will prevent the duplicate record.

## 10. Procedure to Update Student Marks

Suppose a student's marks need to be updated.

We can create a procedure for this operation.

```
CREATE PROCEDURE update_student_marks(
    p_student_id INT,
    p_new_marks INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE students
    SET marks = p_new_marks
    WHERE student_id = p_student_id;

    RAISE NOTICE 'Student marks updated';
END;
$$;
```

Call the procedure:

```
CALL update_student_marks(1, 95);
```

Check the updated record:

```
SELECT *
FROM students
WHERE student_id = 1;
```

Ali's marks will now be 95.

## 11. Procedure with IF-ELSE Conditions

Procedures can use conditional statements.

For example, let's create a procedure that checks whether a student has passed or failed.

```
CREATE PROCEDURE check_student_result(
    p_marks INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF p_marks >= 50 THEN
        RAISE NOTICE 'Result: Pass';
    ELSE
        RAISE NOTICE 'Result: Fail';
    END IF;
END;
$$;
```

Call the procedure:

```
CALL check_student_result(75);
```

Output:

```
NOTICE: Result: Pass
```

Try another example:

```
CALL check_student_result(40);
```

Output:

```
NOTICE: Result: Fail
```

## 12. Procedure with DELETE Operation

We can also create a procedure to delete a student record.

```
CREATE PROCEDURE delete_student(
    p_student_id INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM students
    WHERE student_id = p_student_id;

    RAISE NOTICE 'Delete operation completed';
END;
$$;
```

Call the procedure:

```
CALL delete_student(5);
```

Check the records:

```
SELECT * FROM students;
```

The student with ID 5 will be deleted.

Note: In a real application, it is useful to check whether the student exists before deleting the record.

## 13. IN, OUT and INOUT Parameters

PostgreSQL procedures support three important parameter modes.

| Parameter | Purpose                                              |
| --------- | ---------------------------------------------------- |
| IN        | Receives an input value                              |
| OUT       | Returns an output value                              |
| INOUT     | Receives an input value and returns an updated value |

### A. IN Parameter

An IN parameter receives a value.

```
CREATE PROCEDURE display_marks(
    IN p_marks INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    RAISE NOTICE 'Marks: %', p_marks;
END;
$$;
```

Execute:

```
CALL display_marks(85);
```

### B. OUT Parameter

An OUT parameter returns a value from a procedure.

```
CREATE PROCEDURE get_total_students(
    OUT total INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT COUNT(*)
    INTO total
    FROM students;
END;
$$;
```

Execute:

```
CALL get_total_students(NULL);
```

The result contains the total number of student records.

### C. INOUT Parameter

An INOUT parameter receives an initial value and returns the modified value.

Example: Increase a number by 10.

```
CREATE PROCEDURE increase_number(
    INOUT num INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    num := num + 10;
END;
$$;
```

Execute:

```
CALL increase_number(20);
```

Expected output:

| num |
| --- |
| 30  |

## 14. Replacing an Existing Procedure

We can modify an existing procedure using `CREATE OR REPLACE PROCEDURE`.

Example:

```
CREATE OR REPLACE PROCEDURE welcome_message()
LANGUAGE plpgsql
AS $$
BEGIN
    RAISE NOTICE 'Welcome to Ghazi University';
END;
$$;
```

Execute the updated procedure:

```
CALL welcome_message();
```

## 15. Deleting a Stored Procedure

We can delete a procedure using `DROP PROCEDURE`.

Syntax:

```
DROP PROCEDURE procedure_name(parameter_types);
```

Example:

```
DROP PROCEDURE welcome_message();
```

To avoid an error if the procedure does not exist:

```
DROP PROCEDURE IF EXISTS welcome_message();
```

For procedures with parameters, specify their data types.

```
DROP PROCEDURE IF EXISTS show_student(VARCHAR);
```

## 16. Transactions in Stored Procedures

One important feature of PostgreSQL procedures is that they can manage transactions in permitted execution contexts.

For example, a procedure can contain:

```
COMMIT;
```

or:

```
ROLLBACK;
```

However, transaction control is restricted. A procedure generally cannot execute transaction-control commands when called inside an explicit transaction block or when other restrictions apply.

For beginners, remember:

- Functions generally execute within the transaction of the statement that calls them.
- Procedures can perform transaction control in permitted contexts.

We will study practical transaction handling in more detail separately.

## 17. Common Mistakes

1. Using SELECT instead of CALL to execute a procedure.
2. Forgetting to specify parameter data types.
3. Passing the wrong number of arguments.
4. Using RETURN as if a procedure were a function.
5. Forgetting the `$$` delimiters.
6. Forgetting to close the PL/pgSQL block with `END;`.
7. Assuming every procedure can execute COMMIT or ROLLBACK in every context.

## 18. Practice Exercises

Use the `students` table created in this lesson.

### Beginner Level

1. Create a procedure named `welcome_message()` that displays a welcome message.
2. Create a procedure that accepts a student name and displays it.
3. Create a procedure that accepts marks and displays Pass or Fail.
4. Create a procedure that displays the department name.

### Intermediate Level

5. Create a procedure to insert a new student record.
6. Create a procedure to update student marks using student ID.
7. Create a procedure to delete a student using student ID.
8. Create a procedure to display the total number of students.
9. Create a procedure using an IF-ELSE condition to check student grades.

### Advanced Level

10. Create a procedure using an OUT parameter to return the total number of students.
11. Create a procedure using an INOUT parameter to increase student marks by 5.
12. Create a procedure that accepts a department name and displays the number of students in that department.
13. Create a procedure that updates student marks only when the new marks are between 0 and 100.
14. Replace an existing procedure using CREATE OR REPLACE PROCEDURE.

## 19. Review Questions

1. What is a stored procedure?
2. Why do we use stored procedures?
3. What is the difference between a function and a procedure?
4. Which command creates a procedure?
5. How do we execute a procedure?
6. What is the purpose of CALL?
7. What is an IN parameter?
8. What is an OUT parameter?
9. What is an INOUT parameter?
10. Can a procedure perform INSERT, UPDATE and DELETE operations?
11. How do we replace an existing procedure?
12. How do we delete a procedure?
13. Can PostgreSQL procedures manage transactions?

## 20. Quick Revision

| Command / Keyword             | Purpose                           |
| ----------------------------- | --------------------------------- |
| `CREATE PROCEDURE`            | Creates a stored procedure        |
| `CALL`                        | Executes a procedure              |
| `IN`                          | Receives input                    |
| `OUT`                         | Returns output                    |
| `INOUT`                       | Receives and returns a value      |
| `CREATE OR REPLACE PROCEDURE` | Creates or updates a procedure    |
| `DROP PROCEDURE`              | Deletes a procedure               |
| `RAISE NOTICE`                | Displays an informational message |

Remember: Stored procedures allow us to save and execute reusable database operations using the CALL command.

## Next Lesson

Triggers in PostgreSQL

You will learn how to execute database actions automatically when records are inserted, updated, or deleted.