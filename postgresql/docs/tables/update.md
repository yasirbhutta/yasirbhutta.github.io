# UPDATE Statement in PostgreSQL

## 1. Introduction

In PostgreSQL, the `UPDATE` statement is used to modify existing records in a database table.

Sometimes information stored in a database needs to be corrected or changed.

Real-life example:

Imagine a university database containing student records.

The university may need to:

- Correct a student's name.
- Update a student's email address.
- Change a student's city.
- Update semester fees.
- Change a student's department.

We can perform these tasks using the `UPDATE` statement.

## 2. Basic Syntax

```
UPDATE table_name
SET column1 = value1,
    column2 = value2
WHERE condition;
```

Understanding the syntax:

- `UPDATE`: Specifies the table whose records we want to modify.
- `table_name`: Name of the table.
- `SET`: Specifies the columns and their new values.
- `WHERE`: Specifies which records should be updated.

## 3. Create a Table for Practice

Let's create a students table.

```
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    student_name VARCHAR(100),
    email VARCHAR(100),
    age INTEGER,
    city VARCHAR(50),
    fee NUMERIC(10, 2)
);
```

Insert sample records:

```
INSERT INTO students
    (student_id, student_name, email, age, city, fee)
VALUES
    (1, 'Ali', 'ali@example.com', 20, 'Multan', 50000),
    (2, 'Ahmad', 'ahmad@example.com', 21, 'Lahore', 45000),
    (3, 'Usman', 'usman@example.com', 22, 'Multan', 40000),
    (4, 'Sara', 'sara@example.com', 19, 'Lahore', 55000),
    (5, 'Ayesha', 'ayesha@example.com', 23, 'Multan', 45000);
```

View the records:

```
SELECT *
FROM students;
```

## 4. Update a Single Column

Suppose we want to change Ali's city from Multan to Lahore.

```
UPDATE students
SET city = 'Lahore'
WHERE student_id = 1;
```

Understand the query:

1. `UPDATE students` selects the students table.
2. `SET city = 'Lahore'` specifies the new city.
3. `WHERE student_id = 1` identifies the student whose record should be updated.

Verify the change:

```
SELECT *
FROM students
WHERE student_id = 1;
```

## 5. Update Multiple Columns

We can update more than one column in a single query.

Example: Change Ahmad's email address and city.

```
UPDATE students
SET
    email = 'ahmad.new@example.com',
    city = 'Multan'
WHERE student_id = 2;
```

This query updates both columns in the same student record.

## 6. Update Records Using Comparison Conditions

We can use comparison operators in the `WHERE` clause.

Example 1: Increase the fee of students whose current fee is 40,000.

```
UPDATE students
SET fee = 45000
WHERE fee = 40000;
```

Example 2: Change the city of students older than 21 to Islamabad.

```
UPDATE students
SET city = 'Islamabad'
WHERE age > 21;
```

Example 3: Change the department or another column for students meeting a specific condition.

```
UPDATE students
SET fee = 50000
WHERE age >= 20;
```

This query updates the fee of every student aged 20 or above.

## 7. Update Records Using AND

The `AND` operator allows us to apply multiple conditions.

Example: Update the fee of Computer Science students from Multan.

```
UPDATE students
SET fee = 55000
WHERE city = 'Multan'
AND student_id = 1;
```

Both conditions must be true for a record to be updated.

## 8. Update Records Using OR

The `OR` operator allows us to update records that match at least one condition.

Example: Change the city of students whose IDs are 3 or 4.

```
UPDATE students
SET city = 'Islamabad'
WHERE student_id = 3
OR student_id = 4;
```

## 9. Update Records Using IN

The `IN` operator makes it easier to match multiple values.

Example: Update the fee of students with IDs 1, 3, and 5.

```
UPDATE students
SET fee = 60000
WHERE student_id IN (1, 3, 5);
```

## 10. Update All Records in a Table

If we execute an UPDATE statement without a `WHERE` clause, PostgreSQL updates every record in the table.

Example:

```
UPDATE students
SET fee = 50000;
```

This query sets the fee of all students to 50,000.

Important warning

Always check the `WHERE` condition before executing an UPDATE query. Without it, all records may be modified unintentionally.

## 11. Use RETURNING to View Updated Records

PostgreSQL provides the `RETURNING` clause to display the records affected by an UPDATE statement.

Example:

```
UPDATE students
SET city = 'Lahore'
WHERE student_id = 1
RETURNING *;
```

This query updates the student's city and immediately displays the updated record.

You can also return selected columns:

```
UPDATE students
SET fee = 60000
WHERE student_id = 2
RETURNING student_id, student_name, fee;
```

## 12. Use UPDATE with a Calculation

We can perform mathematical calculations while updating values.

Example: Increase the fee of every student by 10%.

```
UPDATE students
SET fee = fee * 1.10;
```

Another example: Increase the age of a particular student by one year.

```
UPDATE students
SET age = age + 1
WHERE student_id = 1;
```

## 13. Verify Updated Records

After updating records, use the `SELECT` statement to verify the changes.

```
SELECT *
FROM students;
```

To check a particular student:

```
SELECT *
FROM students
WHERE student_id = 1;
```

## 14. Common Mistakes

| Mistake                 | Explanation                                            |
| ----------------------- | ------------------------------------------------------ |
| Missing WHERE           | All records may be updated.                            |
| Incorrect column name   | The column must exist in the table.                    |
| Incorrect data type     | The new value must be compatible with the column type. |
| Missing quotation marks | Text values require single quotation marks.            |
| Incorrect condition     | The wrong records may be updated.                      |

Incorrect example:

```
UPDATE students
SET city = 'Lahore';
```

This updates every student's city, not just one student's city.

Correct example:

```
UPDATE students
SET city = 'Lahore'
WHERE student_id = 1;
```

## 15. Complete Practical Examples

Try these queries using the students table.

Example 1: Change the city of student ID 2 to Multan.

```
UPDATE students
SET city = 'Multan'
WHERE student_id = 2;
```

Example 2: Change the email address of student ID 3.

```
UPDATE students
SET email = 'usman.new@example.com'
WHERE student_id = 3;
```

Example 3: Increase the fee of students by 5%.

```
UPDATE students
SET fee = fee * 1.05;
```

Example 4: Update students whose age is greater than 20.

```
UPDATE students
SET city = 'Islamabad'
WHERE age > 20;
```

Example 5: Update a record and display the result.

```
UPDATE students
SET fee = 65000
WHERE student_id = 4
RETURNING *;
```

## 16. Practice Exercises

Use the students table created in this lesson.

Exercise 1: Update Single Columns

Write queries to:

1. Change the city of student ID 1 to Islamabad.
2. Change the email address of student ID 2.
3. Change the fee of student ID 3 to 50,000.
4. Change the age of student ID 4 to 22.

Exercise 2: Update Multiple Columns

Write queries to:

1. Change the city and email of student ID 1.
2. Change the age and fee of student ID 2.
3. Change the city and fee of student ID 3.

Exercise 3: Update Using Conditions

Write queries to:

1. Increase the fee of students by 10%.
2. Change the city of students older than 21 to Lahore.
3. Set the fee to 60,000 for students from Multan.
4. Update students whose IDs are 1, 3, and 5.

Exercise 4: Use RETURNING

Write queries to:

1. Update student ID 1 and display the updated record.
2. Update the fee of student ID 2 and display only the student name and fee.
3. Update the city of student ID 3 and display the new city.

## 17. Review Questions

1. What is the purpose of the UPDATE statement?
2. What is the purpose of the SET keyword?
3. Why do we use the WHERE clause with UPDATE?
4. What happens when WHERE is omitted?
5. Can we update multiple columns in one query?
6. Can we use AND and OR with UPDATE?
7. What is the purpose of the RETURNING clause?
8. How can we increase a student's fee by 10%?
9. How can we verify updated records?

## 18. Quick Revision

| SQL Keyword | Purpose                                     |
| ----------- | ------------------------------------------- |
| `UPDATE`    | Modifies existing records.                  |
| `SET`       | Assigns new values to columns.              |
| `WHERE`     | Specifies which records to update.          |
| `AND`       | Requires all conditions to be true.         |
| `OR`        | Requires at least one condition to be true. |
| `IN`        | Matches values from a list.                 |
| `RETURNING` | Displays updated records.                   |

Remember: Use `WHERE` carefully with UPDATE. Without a WHERE condition, all records in the table are updated.

Next Lesson: DELETE Statement in PostgreSQL

Students will learn how to delete specific records and remove all records from a table using the `DELETE` statement.