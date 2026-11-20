# Student Notes: ALTER TABLE in PostgreSQL

## 1. Introduction

In a database, we sometimes need to change the structure of an existing table.

For example, a university creates a `students` table with the following columns:

- Student ID
- Student Name
- Age
- City

Later, the university may need to:

- Add a phone number column.
- Rename the student name column.
- Change the data type of a column.
- Set a default value.
- Remove an unnecessary column.
- Rename the table.

PostgreSQL provides the ALTER TABLE command to make these changes.

Important: `ALTER TABLE` changes the structure of a table, not the actual purpose of its existing records.

## 2. What is ALTER TABLE?

`ALTER TABLE` is a SQL command used to modify the structure of an existing table.

It belongs to DDL (Data Definition Language).

DDL commands are used to create, modify, and delete database objects.

Common DDL commands include:

| Command    | Purpose                              |
| ---------- | ------------------------------------ |
| `CREATE`   | Creates a database object            |
| `ALTER`    | Modifies an existing database object |
| `DROP`     | Deletes a database object            |
| `TRUNCATE` | Removes all records from a table     |

## 3. Create a Sample Table

Before learning ALTER TABLE, create a sample table.

```
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    student_name VARCHAR(100),
    age INTEGER,
    city VARCHAR(50),
    fee NUMERIC(10, 2)
);
```

Insert sample records:

```
INSERT INTO students
(student_id, student_name, age, city, fee)
VALUES
(1, 'Ali', 20, 'Multan', 15000),
(2, 'Ahmed', 22, 'DG Khan', 18000),
(3, 'Sara', 21, 'Lahore', 20000);
```

View the table:

```
SELECT * FROM students;
```

## 4. Add a New Column

Sometimes we need to add a new column to an existing table.

Syntax:

```
ALTER TABLE table_name
ADD COLUMN column_name data_type;
```

Example: Add a phone column

```
ALTER TABLE students
ADD COLUMN phone VARCHAR(20);
```

Explanation:

- `ALTER TABLE` specifies the table to modify.
- `students` is the table name.
- `ADD COLUMN` adds a new column.
- `phone` is the new column name.
- `VARCHAR(20)` defines its data type.

The table now contains a new column named `phone`.

Existing records will have `NULL` in this column unless a default value is specified.

## 5. Add Multiple Columns

PostgreSQL allows us to add multiple columns in one ALTER TABLE statement.

Example:

```
ALTER TABLE students
ADD COLUMN email VARCHAR(100),
ADD COLUMN admission_date DATE;
```

This statement adds two columns:

1. `email`
2. `admission_date`

## 6. Rename a Column

Sometimes we need to change an existing column name.

Syntax:

```
ALTER TABLE table_name
RENAME COLUMN old_name TO new_name;
```

Example:

```
ALTER TABLE students
RENAME COLUMN student_name TO full_name;
```

The column `student_name` is now named `full_name`.

Important: Renaming a column does not delete its existing data.

## 7. Change the Data Type of a Column

We can change the data type of an existing column.

Syntax:

```
ALTER TABLE table_name
ALTER COLUMN column_name TYPE new_data_type;
```

Example: Change the age column to SMALLINT

```
ALTER TABLE students
ALTER COLUMN age TYPE SMALLINT;
```

Explanation:

- `ALTER COLUMN` specifies the column.
- `TYPE` specifies its new data type.
- `SMALLINT` stores smaller integer values than `INTEGER`.

The existing values must be convertible to the new data type. Otherwise, PostgreSQL will return an error.

## 8. Set NOT NULL Constraint

We can modify a column to prevent it from storing NULL values.

Example:

```
ALTER TABLE students
ALTER COLUMN email SET NOT NULL;
```

After this change, PostgreSQL will not allow new records with a NULL email.

Important: This command will fail if existing records contain NULL values in the email column.

## 9. Remove NOT NULL Constraint

We can also allow NULL values again.

Example:

```
ALTER TABLE students
ALTER COLUMN email DROP NOT NULL;
```

Now the email column can contain NULL values.

## 10. Set a Default Value

A default value is automatically assigned when a new record is inserted without specifying that column.

Example: Set the default fee to zero

```
ALTER TABLE students
ALTER COLUMN fee SET DEFAULT 0;
```

Now, if we insert a student without specifying the fee:

```
INSERT INTO students
(student_id, full_name, age, city)
VALUES
(4, 'Usman', 23, 'Multan');
```

PostgreSQL automatically assigns `0` to the fee column.

Important: Setting a default value does not change existing records.

## 11. Remove a Default Value

We can remove an existing default value from a column.

Example:

```
ALTER TABLE students
ALTER COLUMN fee DROP DEFAULT;
```

Now PostgreSQL will no longer automatically assign the default fee.

## 12. Delete a Column

Sometimes a column is no longer required.

We can remove it using `DROP COLUMN`.

Syntax:

```
ALTER TABLE table_name
DROP COLUMN column_name;
```

Example:

```
ALTER TABLE students
DROP COLUMN phone;
```

This removes the `phone` column from the table.

Important warning

Dropping a column also permanently removes the data stored in that column. Make sure it is no longer required before deleting it.

## 13. Rename a Table

We can also change the name of an existing table.

Syntax:

```
ALTER TABLE old_table_name
RENAME TO new_table_name;
```

Example:

```
ALTER TABLE students
RENAME TO university_students;
```

The table is now named `university_students`.

## 14. Verify Table Structure

After modifying a table, we should check its structure.

The following query displays column names, data types, NULL settings, and default values:

```
SELECT
    column_name,
    data_type,
    is_nullable,
    column_default
FROM information_schema.columns
WHERE table_name = 'students'
ORDER BY ordinal_position;
```

This query is useful in pgAdmin's Query Tool.

In the PostgreSQL command-line tool (`psql`), we can also use:

```
\d students
```

## 15. Complete ALTER TABLE Command Reference

| Operation        | SQL Command             |
| ---------------- | ----------------------- |
| Add column       | `ADD COLUMN`            |
| Rename column    | `RENAME COLUMN`         |
| Change data type | `ALTER COLUMN ... TYPE` |
| Set NOT NULL     | `SET NOT NULL`          |
| Remove NOT NULL  | `DROP NOT NULL`         |
| Set default      | `SET DEFAULT`           |
| Remove default   | `DROP DEFAULT`          |
| Delete column    | `DROP COLUMN`           |
| Rename table     | `RENAME TO`             |

## 16. Practice Exercises

Use the `students` table created in this lesson.

Beginner Level

1. Add a column named `phone` with data type `VARCHAR(20)`.
2. Add a column named `email` with data type `VARCHAR(100)`.
3. Add a column named `date_of_birth` with data type `DATE`.
4. Rename the `student_name` column to `full_name`.

Intermediate Level

5. Change the data type of `age` from `INTEGER` to `SMALLINT`.
6. Set the default value of `fee` to `0`.
7. Set the `email` column to `NOT NULL` after ensuring no existing record has a NULL email.
8. Remove the default value from `fee`.

Advanced Level

9. Remove the `phone` column.
10. Rename the `students` table to `university_students`.
11. Display the updated table structure using `information_schema.columns`.

## 17. Review Questions

1. What is the purpose of ALTER TABLE?
2. Which SQL command adds a new column?
3. How can we rename an existing column?
4. How can we change a column's data type?
5. What is the difference between `SET DEFAULT` and `DROP DEFAULT`?
6. What happens when we use `DROP COLUMN`?
7. Does renaming a column delete its existing records?
8. Which SQL command renames an existing table?

## 18. Quick Revision

Remember these important examples:

```
-- Add a column
ALTER TABLE students
ADD COLUMN phone VARCHAR(20);

-- Rename a column
ALTER TABLE students
RENAME COLUMN student_name TO full_name;

-- Change data type
ALTER TABLE students
ALTER COLUMN age TYPE SMALLINT;

-- Set default value
ALTER TABLE students
ALTER COLUMN fee SET DEFAULT 0;

-- Remove a column
ALTER TABLE students
DROP COLUMN phone;

-- Rename a table
ALTER TABLE students
RENAME TO university_students;
```

