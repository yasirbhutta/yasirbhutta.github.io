# Student Notes: CASE Expression in PostgreSQL

## 1. Introduction

In real life, we often make decisions based on conditions.

For example, a teacher checks a student's marks:

- If marks are 80 or above, the grade is A.
- If marks are 70 or above, the grade is B.
- If marks are 60 or above, the grade is C.
- Otherwise, the student receives grade F.

In PostgreSQL, we can use the CASE expression to perform this type of conditional operation.

## 2. What is the CASE Expression?

The `CASE` expression checks conditions and returns a value based on the first condition that is true.

It is similar to `if-else` statements in programming languages such as C++ and Python.

Syntax:

```
SELECT
    column_name,
    CASE
        WHEN condition1 THEN result1
        WHEN condition2 THEN result2
        WHEN condition3 THEN result3
        ELSE default_result
    END AS new_column_name
FROM table_name;
```

Important keywords:

- `CASE`: Starts the conditional expression.
- `WHEN`: Specifies a condition.
- `THEN`: Specifies the result if the condition is true.
- `ELSE`: Specifies the default result if no condition is true.
- `END`: Ends the CASE expression.
- `AS`: Gives a name to the resulting column.

## 3. Create a Sample Table

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
INSERT INTO students (student_id, student_name, marks)
VALUES
    (1, 'Ali', 85),
    (2, 'Sara', 72),
    (3, 'Ahmed', 65),
    (4, 'Usman', 45),
    (5, 'Ayesha', 90);
```

Display all records:

```
SELECT * FROM students;
```

## 4. Simple CASE Expression

Let's assign grades to students based on their marks.

```
SELECT
    student_name,
    marks,
    CASE
        WHEN marks >= 80 THEN 'A'
        WHEN marks >= 70 THEN 'B'
        WHEN marks >= 60 THEN 'C'
        ELSE 'F'
    END AS grade
FROM students;
```

Expected output:

| student_name | marks | grade |
| ------------ | ----- | ----- |
| Ali          | 85    | A     |
| Sara         | 72    | B     |
| Ahmed        | 65    | C     |
| Usman        | 45    | F     |
| Ayesha       | 90    | A     |

Understand the query:

1. PostgreSQL checks whether marks are 80 or above.
2. If true, it returns A.
3. Otherwise, it checks whether marks are 70 or above.
4. It continues checking the conditions in order.
5. If no condition is true, it returns F.

Important: PostgreSQL stops at the first matching `WHEN` condition.

## 5. CASE Expression with ELSE

The `ELSE` part is optional.

Consider this query:

```
SELECT
    student_name,
    marks,
    CASE
        WHEN marks >= 50 THEN 'Pass'
        ELSE 'Fail'
    END AS result
FROM students;
```

Expected output:

| student_name | marks | result |
| ------------ | ----- | ------ |
| Ali          | 85    | Pass   |
| Sara         | 72    | Pass   |
| Ahmed        | 65    | Pass   |
| Usman        | 45    | Fail   |
| Ayesha       | 90    | Pass   |

If we omit `ELSE`, PostgreSQL returns `NULL` when none of the conditions is true.

## 6. CASE Expression with UPDATE

We can also use CASE inside an `UPDATE` statement.

Suppose we want to assign performance categories to students.

```
ALTER TABLE students
ADD COLUMN performance VARCHAR(20);
```

Update the performance column:

```
UPDATE students
SET performance =
    CASE
        WHEN marks >= 80 THEN 'Excellent'
        WHEN marks >= 60 THEN 'Good'
        WHEN marks >= 50 THEN 'Average'
        ELSE 'Poor'
    END;
```

Check the updated records:

```
SELECT * FROM students;
```

Now each student has a performance category based on their marks.

## 7. CASE Expression with ORDER BY

We can use CASE to control the sorting order of records.

For example, display students in the following priority:

1. Students who passed.
2. Students who failed.

```
SELECT
    student_name,
    marks,
    CASE
        WHEN marks >= 50 THEN 1
        ELSE 2
    END AS priority
FROM students
ORDER BY priority;
```

Students with priority `1` appear first.

We can also sort without displaying the priority column:

```
SELECT student_name, marks
FROM students
ORDER BY
    CASE
        WHEN marks >= 50 THEN 1
        ELSE 2
    END;
```

## 8. CASE Expression with Aggregate Functions

CASE can also be used with aggregate functions.

For example, count how many students passed and failed.

```
SELECT
    COUNT(
        CASE WHEN marks >= 50 THEN 1 END
    ) AS passed_students,

    COUNT(
        CASE WHEN marks < 50 THEN 1 END
    ) AS failed_students
FROM students;
```

Expected output:

| passed_students | failed_students |
| --------------- | --------------- |
| 4               | 1               |

This is useful for preparing reports.

## 9. Simple CASE vs Searched CASE

PostgreSQL supports two forms of CASE expressions.

A. Searched CASE

Checks conditions using comparison operators.

```
SELECT
    student_name,
    CASE
        WHEN marks >= 80 THEN 'A'
        WHEN marks >= 60 THEN 'B'
        ELSE 'C'
    END AS grade
FROM students;
```

B. Simple CASE

Compares one expression with different possible values.

```
SELECT
    student_name,
    CASE marks
        WHEN 85 THEN 'Excellent'
        WHEN 72 THEN 'Good'
        WHEN 45 THEN 'Needs Improvement'
        ELSE 'Other'
    END AS performance
FROM students;
```

| Searched CASE                 | Simple CASE                         |
| ----------------------------- | ----------------------------------- |
| Uses conditions after WHEN    | Compares one expression with values |
| Supports `>=`, `<`, `=`, etc. | Uses equality comparisons           |
| Suitable for ranges           | Suitable for specific values        |

## 10. CASE vs IF-ELSE

| CASE Expression                         | IF-ELSE                        |
| --------------------------------------- | ------------------------------ |
| Used in SQL queries                     | Used in programming logic      |
| Returns a value                         | Controls program execution     |
| Can be used in SELECT, UPDATE, ORDER BY | Used in procedural code        |
| Evaluates conditions in order           | Executes a matching code block |

Remember: CASE is an expression that returns a value; it is not a replacement for every programming control structure.

## 11. Practice Exercises

Use the `students` table created in this lesson.

### Beginner Level

1. Write a query to display student names and marks.
2. Use CASE to display `Pass` if marks are 50 or above; otherwise display `Fail`.
3. Assign grade A to students with marks 80 or above and grade B to all other students.

### Intermediate Level

4. Assign grades using these conditions:
   - 90 or above: A+
   - 80 or above: A
   - 70 or above: B
   - 60 or above: C
   - Below 60: F
5. Use CASE with ORDER BY to display students with higher marks first, followed by lower marks.
6. Count the number of students in each result category using conditional aggregation.

### Advanced Level

7. Add a column named `grade` to the students table and update it using CASE.
8. Write a query that displays student name, marks, grade, and performance category.
9. Generate a report showing the total number of passed and failed students.

## 12. Review Questions

1. What is a CASE expression in PostgreSQL?
2. What is the purpose of WHEN and THEN?
3. Why do we use ELSE?
4. Is ELSE compulsory?
5. What happens when no condition matches and ELSE is omitted?
6. Can CASE be used with UPDATE?
7. What is the difference between simple CASE and searched CASE?
8. Can CASE be used with ORDER BY?

## 13. Quick Revision

| Keyword | Purpose                                 |
| ------- | --------------------------------------- |
| CASE    | Starts conditional evaluation           |
| WHEN    | Defines a condition or comparison value |
| THEN    | Returns a value when matched            |
| ELSE    | Returns a default value                 |
| END     | Ends the CASE expression                |

Remember: CASE allows us to make decisions directly inside SQL queries.

## Next Lesson

Views in PostgreSQL

You will learn how to create, use, update, and delete views, and how views simplify complex SQL queries.