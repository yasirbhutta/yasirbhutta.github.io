# DELETE Statement in PostgreSQL

## 1. Introduction

In PostgreSQL, the `DELETE` statement is used to remove existing records from a database table.

Sometimes information stored in a database needs to be removed.

Real-life example:

Imagine a university database containing student records.

The university may need to:

- Delete a student record entered by mistake.
- Remove a student who was registered incorrectly.
- Delete records of students who have withdrawn, according to university policy.
- Remove all records from a temporary table.

We can perform these tasks using the `DELETE` statement.

## 2. Basic Syntax

```
DELETE FROM table_name
WHERE condition;
```

Understanding the syntax:

- `DELETE FROM`: Specifies the table from which records will be deleted.
- `table_name`: Name of the table.
- `WHERE`: Specifies which records should be deleted.
- `condition`: Identifies the records to remove.

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

## 4. Delete a Single Record

Suppose we want to delete the student whose ID is 1.

```
DELETE FROM students
WHERE student_id = 1;
```

Understand the query:

1. `DELETE FROM students` specifies the students table.
2. `WHERE student_id = 1` identifies the student to delete.
3. PostgreSQL removes the matching record.

Verify the deletion:

```
SELECT *
FROM students;
```

The record of student ID 1 will no longer appear.

## 5. Delete Multiple Records

We can delete multiple records by using a condition that matches several rows.

Example: Delete all students from Multan.

```
DELETE FROM students
WHERE city = 'Multan';
```

This query deletes every record where the city is Multan.

Important: Always check how many records match your condition before deleting them.

```
SELECT *
FROM students
WHERE city = 'Multan';
```

## 6. Delete Records Using Comparison Operators

We can use comparison operators in the `WHERE` clause.

Example 1: Delete students older than 21.

```
DELETE FROM students
WHERE age > 21;
```

Example 2: Delete students whose fee is less than 45,000.

```
DELETE FROM students
WHERE fee < 45000;
```

Example 3: Delete student ID 3.

```
DELETE FROM students
WHERE student_id = 3;
```

## 7. Delete Records Using AND

The `AND` operator allows us to apply multiple conditions.

Example: Delete students from Multan whose age is greater than 20.

```
DELETE FROM students
WHERE city = 'Multan'
AND age > 20;
```

Both conditions must be true for a record to be deleted.

## 8. Delete Records Using OR

The `OR` operator allows us to delete records that match at least one condition.

Example: Delete students whose IDs are 2 or 4.

```
DELETE FROM students
WHERE student_id = 2
OR student_id = 4;
```

## 9. Delete Records Using IN

The `IN` operator makes it easier to specify multiple values.

Example: Delete students with IDs 1, 3, and 5.

```
DELETE FROM students
WHERE student_id IN (1, 3, 5);
```

This is shorter than writing multiple OR conditions.

## 10. Delete Records Using BETWEEN

The `BETWEEN` operator can be used to delete records within a range.

Example: Delete students whose ages are between 18 and 20.

```
DELETE FROM students
WHERE age BETWEEN 18 AND 20;
```

Important: `BETWEEN` includes both boundary values.

## 11. Delete All Records from a Table

If we execute a `DELETE` statement without a `WHERE` clause, PostgreSQL deletes all records from the table.

```
DELETE FROM students;
```

After executing this query, the students table will contain no records.

Important warning

Never execute `DELETE FROM table_name` without understanding its effect. It removes all rows from the specified table.

Remember: The table structure remains unchanged. Only its records are deleted.

## 12. Use RETURNING to View Deleted Records

PostgreSQL provides the `RETURNING` clause to display the records deleted by a query.

Example:

```
DELETE FROM students
WHERE student_id = 2
RETURNING *;
```

This query deletes student ID 2 and immediately displays the deleted record.

You can also return selected columns:

```
DELETE FROM students
WHERE student_id = 3
RETURNING student_id, student_name;
```

## 13. DELETE vs TRUNCATE vs DROP

These three SQL commands are used for different purposes.

| Command      | Purpose                                            |
| ------------ | -------------------------------------------------- |
| `DELETE`     | Removes selected records or all records.           |
| `TRUNCATE`   | Quickly removes all records from a table.          |
| `DROP TABLE` | Removes the entire table, including its structure. |

Example 1: DELETE

```
DELETE FROM students
WHERE student_id = 1;
```

Removes only the specified student's record.

Example 2: TRUNCATE

```
TRUNCATE TABLE students;
```

Removes all records while keeping the table structure.

Example 3: DROP TABLE

```
DROP TABLE students;
```

Removes the entire students table.

## 14. Use ROLLBACK to Recover Deleted Records

PostgreSQL supports transactions. If a deletion is performed inside a transaction and has not been committed, we can cancel it using `ROLLBACK`.

Example:

```
BEGIN;

DELETE FROM students
WHERE student_id = 1;

ROLLBACK;
```

The deletion is cancelled, and the record is restored.

If we want to make the deletion permanent, use `COMMIT` instead:

```
BEGIN;

DELETE FROM students
WHERE student_id = 1;

COMMIT;
```

Important: `ROLLBACK` works only before the transaction is committed. It cannot undo a deletion that has already been committed.

## 15. Common Mistakes

| Mistake                         | Explanation                                   |
| ------------------------------- | --------------------------------------------- |
| Missing WHERE                   | All records may be deleted.                   |
| Incorrect condition             | The wrong records may be deleted.             |
| Wrong table name                | The specified table must exist.               |
| Ignoring foreign keys           | Related records may prevent deletion.         |
| Assuming DELETE removes a table | DELETE removes rows, not the table structure. |

Incorrect example:

```
DELETE FROM students;
```

If your intention is to delete only one student, this query is dangerous because it deletes all student records.

Correct example:

```
DELETE FROM students
WHERE student_id = 1;
```

## 16. Complete Practical Examples

Try these queries using the students table.

Example 1: Delete student ID 4.

```
DELETE FROM students
WHERE student_id = 4;
```

Example 2: Delete students from Lahore.

```
DELETE FROM students
WHERE city = 'Lahore';
```

Example 3: Delete students whose fee is greater than 50,000.

```
DELETE FROM students
WHERE fee > 50000;
```

Example 4: Delete students with IDs 1, 2, and 3.

```
DELETE FROM students
WHERE student_id IN (1, 2, 3);
```

Example 5: Delete a student and display the deleted record.

```
DELETE FROM students
WHERE student_id = 5
RETURNING *;
```

## 17. Practice Exercises

Use the students table created in this lesson.

Exercise 1: Delete Single Records

Write queries to:

1. Delete the student whose ID is 1.
2. Delete the student whose ID is 3.
3. Delete the student whose ID is 5.

Exercise 2: Delete Using Conditions

Write queries to:

1. Delete students from Multan.
2. Delete students older than 21.
3. Delete students whose fee is less than 45,000.
4. Delete students whose age is between 18 and 20.

Exercise 3: Delete Using Logical Operators

Write queries to:

1. Delete students from Lahore AND older than 20.
2. Delete students whose IDs are 2 OR 4.
3. Delete students whose IDs are 1, 3, and 5 using IN.

Exercise 4: Understand SQL Commands

Explain the difference between:

1. `DELETE FROM students;`
2. `TRUNCATE TABLE students;`
3. `DROP TABLE students;`

Exercise 5: Use RETURNING

Write a query that deletes student ID 2 and displays the deleted record.

## 18. Review Questions

1. What is the purpose of the DELETE statement?
2. What is the purpose of the WHERE clause with DELETE?
3. What happens if WHERE is omitted?
4. Can we delete multiple records using one query?
5. What is the purpose of the RETURNING clause?
6. What is the difference between DELETE and TRUNCATE?
7. What is the difference between DELETE and DROP TABLE?
8. How can we cancel a deletion using ROLLBACK?
9. Does DELETE remove the table structure?

## 19. Quick Revision

| SQL Keyword   | Purpose                                     |
| ------------- | ------------------------------------------- |
| `DELETE FROM` | Removes records from a table.               |
| `WHERE`       | Specifies which records to delete.          |
| `AND`         | Requires all conditions to be true.         |
| `OR`          | Requires at least one condition to be true. |
| `IN`          | Matches values from a list.                 |
| `BETWEEN`     | Checks a range.                             |
| `RETURNING`   | Displays deleted records.                   |
| `ROLLBACK`    | Cancels uncommitted changes.                |
| `COMMIT`      | Makes transaction changes permanent.        |

Remember: Always verify your WHERE condition before executing DELETE. A missing or incorrect condition can result in permanent data loss after the transaction is committed.

Next Lesson: ALTER TABLE in PostgreSQL

Students will learn how to modify an existing table by adding, renaming, changing, and dropping columns.