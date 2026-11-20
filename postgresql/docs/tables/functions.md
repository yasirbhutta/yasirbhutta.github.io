# Student Notes: Functions in PostgreSQL

## 1. Introduction

Imagine a university frequently needs to calculate the total fee of a student.

Every time, we write the same calculation:

```
SELECT tuition_fee + admission_fee + examination_fee
FROM student_fees;
```

What if we could save this calculation and use it whenever required?

PostgreSQL provides Functions to perform reusable operations.

A function can accept input values, process them, and return a result.

Functions are useful for calculations, data processing, validation, and database operations.

## 2. What is a Function in PostgreSQL?

A Function is a reusable block of code that performs a specific task and can return a value or a result.

For example:

- Calculate student grades.
- Calculate total fees.
- Find the average marks.
- Calculate employee salaries.
- Format dates.
- Process database records.

PostgreSQL provides built-in functions and also allows us to create our own functions.

## 3. Types of Functions in PostgreSQL

PostgreSQL functions can be divided into two common categories:

| Function Type          | Description                    |
| ---------------------- | ------------------------------ |
| Built-in Functions     | Already provided by PostgreSQL |
| User-Defined Functions | Created by database users      |

Examples of built-in functions:

```
SELECT UPPER('ghazi university');

SELECT LOWER('POSTGRESQL');

SELECT LENGTH('Database');

SELECT CURRENT_DATE;
```

We will learn how to create our own functions in this lesson.

## 4. Creating a Sample Table

Let's create a table named `students`.

```
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    marks INT
);
```

Insert sample records:

```
INSERT INTO students
VALUES
    (1, 'Ali', 85),
    (2, 'Sara', 72),
    (3, 'Ahmed', 65),
    (4, 'Usman', 45),
    (5, 'Ayesha', 90);
```

Display records:

```
SELECT * FROM students;
```

## 5. Creating Your First Function

Let's create a simple function that returns a welcome message.

Syntax:

```
CREATE FUNCTION function_name()
RETURNS data_type
LANGUAGE plpgsql
AS $$
BEGIN
    -- SQL statements
    RETURN value;
END;
$$;
```

Example:

```
CREATE FUNCTION welcome_message()
RETURNS VARCHAR
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN 'Welcome to PostgreSQL';
END;
$$;
```

Understand the code:

| Keyword           | Purpose                            |
| ----------------- | ---------------------------------- |
| CREATE FUNCTION   | Creates a new function             |
| welcome_message() | Function name                      |
| RETURNS VARCHAR   | Specifies the return data type     |
| LANGUAGE plpgsql  | Specifies the programming language |
| BEGIN             | Starts the function body           |
| RETURN            | Returns a value                    |
| END               | Ends the function body             |

The `$$` symbols mark the beginning and end of the function body.

## 6. Calling a Function

We can execute a function using `SELECT`.

```
SELECT welcome_message();
```

Expected output:

| welcome_message       |
| --------------------- |
| Welcome to PostgreSQL |

Remember: We use `SELECT` to call a function that returns a value.

## 7. Creating a Function with Parameters

A function can receive input values called parameters.

For example, let's create a function that adds two numbers.

Syntax:

```
CREATE FUNCTION function_name(parameter1 data_type, parameter2 data_type)
RETURNS data_type
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN expression;
END;
$$;
```

Example:

```
CREATE FUNCTION add_numbers(
    num1 INT,
    num2 INT
)
RETURNS INT
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN num1 + num2;
END;
$$;
```

Call the function:

```
SELECT add_numbers(10, 20);
```

Expected output:

| add_numbers |
| ----------- |
| 30          |

Understand the code:

- `num1` receives the first number.
- `num2` receives the second number.
- `num1 + num2` calculates their sum.
- `RETURN` sends the result back.

## 8. Function with Text Parameters

Let's create a function that accepts a student's name and returns a welcome message.

```
CREATE FUNCTION student_welcome(
    student_name VARCHAR
)
RETURNS VARCHAR
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN 'Welcome, ' || student_name;
END;
$$;
```

Call the function:

```
SELECT student_welcome('Ali');
```

Expected output:

| student_welcome |
| --------------- |
| Welcome, Ali    |

Important: The `||` operator joins two text values in PostgreSQL.

## 9. Function for Student Grades

Now let's create a practical function that calculates a student's grade based on marks.

Grade criteria:

| Marks       | Grade |
| ----------- | ----- |
| 80 or above | A     |
| 70–79       | B     |
| 60–69       | C     |
| 50–59       | D     |
| Below 50    | F     |

Create the function:

```
CREATE FUNCTION calculate_grade(
    marks INT
)
RETURNS VARCHAR
LANGUAGE plpgsql
AS $$
BEGIN
    IF marks >= 80 THEN
        RETURN 'A';

    ELSIF marks >= 70 THEN
        RETURN 'B';

    ELSIF marks >= 60 THEN
        RETURN 'C';

    ELSIF marks >= 50 THEN
        RETURN 'D';

    ELSE
        RETURN 'F';
    END IF;
END;
$$;
```

Call the function:

```
SELECT calculate_grade(85);
```

Expected output:

| calculate_grade |
| --------------- |
| A               |

Try another example:

```
SELECT calculate_grade(45);
```

Output:

| calculate_grade |
| --------------- |
| F               |

## 10. Using a Function with SELECT

One of the most useful features of PostgreSQL functions is that we can use them directly in SELECT queries.

For example, calculate the grade of every student.

```
SELECT
    student_id,
    student_name,
    marks,
    calculate_grade(marks) AS grade
FROM students;
```

Expected output:

| student_id | student_name | marks | grade |
| ---------- | ------------ | ----- | ----- |
| 1          | Ali          | 85    | A     |
| 2          | Sara         | 72    | B     |
| 3          | Ahmed        | 65    | C     |
| 4          | Usman        | 45    | F     |
| 5          | Ayesha       | 90    | A     |

This approach allows us to reuse the same grading logic for every student.

## 11. Function with Multiple Parameters

A function can accept multiple parameters.

For example, calculate the total fee by adding tuition, admission, and examination fees.

```
CREATE FUNCTION calculate_total_fee(
    tuition_fee NUMERIC,
    admission_fee NUMERIC,
    examination_fee NUMERIC
)
RETURNS NUMERIC
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN tuition_fee + admission_fee + examination_fee;
END;
$$;
```

Call the function:

```
SELECT calculate_total_fee(40000, 5000, 2000);
```

Expected output:

| calculate_total_fee |
| ------------------- |
| 47000               |

## 12. Function Using a Database Table

Functions can also retrieve data from database tables.

Let's create a function that returns the marks of a student using their student ID.

```
CREATE FUNCTION get_student_marks(
    p_student_id INT
)
RETURNS INT
LANGUAGE plpgsql
AS $$
DECLARE
    student_marks INT;
BEGIN
    SELECT marks
    INTO student_marks
    FROM students
    WHERE student_id = p_student_id;

    RETURN student_marks;
END;
$$;
```

Call the function:

```
SELECT get_student_marks(1);
```

Expected output:

| get_student_marks |
| ----------------- |
| 85                |

### Understanding DECLARE and INTO

- `DECLARE` defines variables inside the function.
- `student_marks INT` creates an integer variable.
- `SELECT ... INTO` stores the query result in that variable.
- `RETURN` sends the variable's value back.

If no matching student exists, this function returns `NULL`.

## 13. Replacing an Existing Function

Suppose we want to change the grading criteria.

We can use `CREATE OR REPLACE FUNCTION`.

```
CREATE OR REPLACE FUNCTION calculate_grade(
    marks INT
)
RETURNS VARCHAR
LANGUAGE plpgsql
AS $$
BEGIN
    IF marks >= 90 THEN
        RETURN 'A+';

    ELSIF marks >= 80 THEN
        RETURN 'A';

    ELSIF marks >= 70 THEN
        RETURN 'B';

    ELSIF marks >= 60 THEN
        RETURN 'C';

    ELSE
        RETURN 'F';
    END IF;
END;
$$;
```

Now test the updated function:

```
SELECT calculate_grade(95);
```

Output: `A+`

## 14. Deleting a Function

We can delete a function using `DROP FUNCTION`.

Syntax:

```
DROP FUNCTION function_name(parameter_data_types);
```

Example:

```
DROP FUNCTION welcome_message();
```

For a function with parameters:

```
DROP FUNCTION add_numbers(INT, INT);
```

To avoid an error if the function does not exist:

```
DROP FUNCTION IF EXISTS welcome_message();
```

Important: PostgreSQL identifies functions by their names and parameter types. This is why we specify the parameter types when dropping a function.

## 15. Built-in Functions in PostgreSQL

PostgreSQL provides many ready-made functions.

Here are some useful examples.

### A. String Functions

| Function   | Purpose                                   |
| ---------- | ----------------------------------------- |
| `UPPER()`  | Converts text to uppercase                |
| `LOWER()`  | Converts text to lowercase                |
| `LENGTH()` | Returns the number of characters          |
| `TRIM()`   | Removes spaces from the beginning and end |
| `CONCAT()` | Joins text values                         |

Examples:

```
SELECT UPPER('postgresql');

SELECT LOWER('DATABASE');

SELECT LENGTH('University');

SELECT TRIM('  Ali  ');

SELECT CONCAT('Ghazi', ' ', 'University');
```

### B. Mathematical Functions

| Function  | Purpose                    |
| --------- | -------------------------- |
| `ABS()`   | Returns the absolute value |
| `ROUND()` | Rounds a number            |
| `CEIL()`  | Rounds up                  |
| `FLOOR()` | Rounds down                |
| `POWER()` | Calculates a power         |

Examples:

```
SELECT ABS(-50);

SELECT ROUND(45.678, 2);

SELECT CEIL(45.2);

SELECT FLOOR(45.9);

SELECT POWER(2, 3);
```

### C. Date and Time Functions

| Function       | Purpose                                   |
| -------------- | ----------------------------------------- |
| `CURRENT_DATE` | Returns the current date                  |
| `CURRENT_TIME` | Returns the current time                  |
| `NOW()`        | Returns the current transaction timestamp |
| `EXTRACT()`    | Extracts a date or time component         |

Examples:

```
SELECT CURRENT_DATE;

SELECT CURRENT_TIME;

SELECT NOW();

SELECT EXTRACT(YEAR FROM CURRENT_DATE);
```

## 16. Function vs Stored Procedure

PostgreSQL supports both functions and procedures.

| Function                                       | Procedure                                                 |
| ---------------------------------------------- | --------------------------------------------------------- |
| Created using `CREATE FUNCTION`                | Created using `CREATE PROCEDURE`                          |
| Called using `SELECT` or other SQL expressions | Called using `CALL`                                       |
| Must declare a return type                     | Does not use a RETURNS clause                             |
| Can return a value or result set               | Can perform operations without returning a function value |
| Can be used in SELECT queries                  | Cannot be used directly as a SELECT expression            |

Example function call:

```
SELECT add_numbers(10, 20);
```

Example procedure call:

```
CALL procedure_name();
```

We will study procedures in a separate lesson.

## 17. Practice Exercises

Use the `students` table created in this lesson.

### Beginner Level

1. Create a function named `welcome_message()` that returns `Welcome to PostgreSQL`.
2. Create a function named `add_numbers()` that accepts two integers and returns their sum.
3. Create a function that accepts a student's name and returns a welcome message.
4. Create a function that accepts marks and returns `Pass` or `Fail`.

### Intermediate Level

5. Create a function that calculates a student's grade.
6. Use the grading function in a SELECT query to display all students and their grades.
7. Create a function that accepts three numbers and returns their average.
8. Create a function that retrieves student marks using student ID.
9. Replace an existing function using CREATE OR REPLACE FUNCTION.

### Advanced Level

10. Create a function that calculates total student fees using three parameters.
11. Create a function that returns the number of students in the students table.
12. Create a function that accepts a department name and returns the number of students in that department.
13. Create a function that retrieves a student's name and marks using their student ID. Consider using `RETURNS TABLE`.
14. Drop a function using DROP FUNCTION.

## 18. Review Questions

1. What is a function in PostgreSQL?
2. What are built-in functions?
3. What are user-defined functions?
4. What is the purpose of CREATE FUNCTION?
5. What does RETURNS specify?
6. Why do we use LANGUAGE plpgsql?
7. What is the purpose of RETURN?
8. What are function parameters?
9. What is the purpose of DECLARE?
10. What does SELECT INTO do?
11. How do we replace an existing function?
12. How do we delete a function?
13. What is the difference between a function and a procedure?

## 19. Quick Revision

| Keyword                      | Purpose                         |
| ---------------------------- | ------------------------------- |
| `CREATE FUNCTION`            | Creates a function              |
| `RETURNS`                    | Defines the return type         |
| `LANGUAGE plpgsql`           | Specifies the function language |
| `DECLARE`                    | Defines variables               |
| `BEGIN`                      | Starts the function body        |
| `RETURN`                     | Returns a result                |
| `END`                        | Ends the function body          |
| `CREATE OR REPLACE FUNCTION` | Creates or updates a function   |
| `DROP FUNCTION`              | Deletes a function              |

Remember: Functions allow us to write reusable SQL logic once and execute it whenever needed.

## Next Lesson

Stored Procedures in PostgreSQL

You will learn how to create procedures, pass parameters, execute database operations using `CALL`, and understand the difference between functions and procedures.