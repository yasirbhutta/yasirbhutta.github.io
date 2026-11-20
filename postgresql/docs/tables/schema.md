# Student Notes: PostgreSQL Schema Management

## 1. Introduction

In PostgreSQL, a database can contain multiple schemas.

A schema is a logical container used to organize database objects, such as:

- Tables
- Views
- Functions
- Sequences
- Indexes
- Stored procedures

Think of a database as a university and schemas as different departments within that university.

For example:

- `public` – general database objects
- `admissions` – admission-related objects
- `academics` – academic records
- `finance` – financial records
- `examinations` – examination records

Schemas help us organize database objects and manage access.

## 2. What Is a Schema?

A schema is a named collection of database objects inside a PostgreSQL database.

Consider this structure:

university_db

public

students, departments

admissions

applications, applicants

academics

courses, enrollments

finance

fees, payments

All these schemas belong to the same database, `university_db`.

## 3. Understanding the public Schema

PostgreSQL creates a schema named `public` by default in a newly created database, unless its configuration or template has been changed.

For example:

```
CREATE TABLE public.students (
    student_id INT,
    student_name VARCHAR(100)
);
```

Here:

- `public` is the schema name.
- `students` is the table name.

The complete name of the table is:

```
public.students
```

This is called a schema-qualified table name.

## 4. Viewing Existing Schemas

We can view schemas using the `psql` command.

```
\dn
```

To display additional information:

```
\dn+
```

We can also use an SQL query:

```
SELECT schema_name
FROM information_schema.schemata
ORDER BY schema_name;
```

This displays the available schemas in the current database.

## 5. Creating a Schema

We can create a new schema using the `CREATE SCHEMA` command.

Syntax:

```
CREATE SCHEMA schema_name;
```

Example:

```
CREATE SCHEMA admissions;
```

This creates a schema named `admissions`.

We can verify it using:

```
\dn
```

## 6. Creating Multiple Schemas

We can create multiple schemas for different departments.

```
CREATE SCHEMA academics;

CREATE SCHEMA finance;

CREATE SCHEMA examinations;

CREATE SCHEMA hostel;
```

Now the database can organize objects separately for each department.

## 7. Creating a Table Inside a Schema

To create a table inside a particular schema, write the schema name before the table name.

Syntax:

```
CREATE TABLE schema_name.table_name (
    column_name data_type
);
```

Example:

```
CREATE TABLE admissions.applications (
    application_id INT PRIMARY KEY,
    applicant_name VARCHAR(100),
    program_name VARCHAR(100)
);
```

This creates the `applications` table inside the `admissions` schema.

Its complete name is:

```
admissions.applications
```

## 8. Inserting Data into a Schema Table

We can insert records by using the schema-qualified table name.

```
INSERT INTO admissions.applications
(application_id, applicant_name, program_name)
VALUES
(1, 'Ali', 'BS Computer Science'),
(2, 'Ahmed', 'BS Information Technology');
```

The records are stored in the `admissions.applications` table.

## 9. Retrieving Data from a Schema Table

Use the `SELECT` statement with the schema and table name.

```
SELECT *
FROM admissions.applications;
```

This retrieves all records from the `applications` table inside the `admissions` schema.

## 10. Creating Tables with the Same Name in Different Schemas

PostgreSQL allows tables with the same name in different schemas.

For example:

```
CREATE TABLE admissions.students (
    student_id INT,
    student_name VARCHAR(100)
);
```

```
CREATE TABLE academics.students (
    student_id INT,
    student_name VARCHAR(100)
);
```

Both tables can exist because they belong to different schemas.

Their complete names are:

- `admissions.students`
- `academics.students`

To access a particular table, specify its schema.

```
SELECT * FROM admissions.students;
```

```
SELECT * FROM academics.students;
```

## 11. Renaming a Schema

We can rename an existing schema using `ALTER SCHEMA`.

Syntax:

```
ALTER SCHEMA old_name
RENAME TO new_name;
```

Example:

```
ALTER SCHEMA admissions
RENAME TO student_admissions;
```

The schema is now named `student_admissions`.

Its existing objects remain associated with the renamed schema.

## 12. Changing the Owner of a Schema

Every schema has an owner.

We can change the owner using `ALTER SCHEMA`.

Syntax:

```
ALTER SCHEMA schema_name
OWNER TO new_owner;
```

Example:

```
ALTER SCHEMA academics
OWNER TO postgres;
```

This changes the owner of the `academics` schema to `postgres`.

The new owner must be an existing role, and the executing user must have the necessary privileges.

## 13. Deleting a Schema

We can delete a schema using `DROP SCHEMA`.

Syntax:

```
DROP SCHEMA schema_name;
```

Example:

```
DROP SCHEMA hostel;
```

This deletes the `hostel` schema if it is empty.

If the schema contains database objects, PostgreSQL will normally prevent its deletion.

## 14. Deleting a Schema with CASCADE

Sometimes we want to delete a schema along with all its objects.

We can use `CASCADE`.

Example:

```
DROP SCHEMA hostel CASCADE;
```

This deletes the schema and its dependent objects, including tables and views.

Use with caution

`CASCADE` can permanently delete important database objects and data.

## 15. Using IF NOT EXISTS

Suppose we try to create a schema that already exists.

PostgreSQL will return an error.

We can avoid this error using `IF NOT EXISTS`.

```
CREATE SCHEMA IF NOT EXISTS admissions;
```

If the schema already exists, PostgreSQL will not create another one.

## 16. Using IF EXISTS

Suppose we want to delete a schema that may not exist.

We can use `IF EXISTS`.

```
DROP SCHEMA IF EXISTS hostel;
```

If the schema does not exist, PostgreSQL displays a notice instead of returning an error.

## 17. Understanding the Search Path

PostgreSQL uses a setting called `search_path` to determine which schemas to search when we use an object name without specifying its schema.

For example:

```
SELECT *
FROM students;
```

PostgreSQL searches the schemas listed in the current search path.

To display the current search path:

```
SHOW search_path;
```

A common default value is:

```
"$user", public
```

This means PostgreSQL searches a schema matching the current username first, followed by `public`.

The actual value can vary depending on configuration.

## 18. Changing the Search Path

We can change the search path using `SET search_path`.

Example:

```
SET search_path TO admissions, public;
```

Now PostgreSQL searches `admissions` before `public`.

We can access the applications table without writing its schema name:

```
SELECT *
FROM applications;
```

PostgreSQL will search for `applications` in the schemas listed in the search path, in order.

Important: If tables with the same name exist in multiple schemas, PostgreSQL uses the first matching object in the search path.

## 19. Granting Schema Permissions

We can grant permissions on a schema to a user or role.

For example, allow `teacher_user` to access objects in the `academics` schema:

```
GRANT USAGE
ON SCHEMA academics
TO teacher_user;
```

To allow the user to create objects in the schema:

```
GRANT CREATE
ON SCHEMA academics
TO teacher_user;
```

Difference:

| Permission | Purpose                                                     |
| ---------- | ----------------------------------------------------------- |
| `USAGE`    | Access objects in the schema, subject to object permissions |
| `CREATE`   | Create objects in the schema                                |

Schema access alone does not grant permission to read or modify table data.

## 20. Revoking Schema Permissions

We can remove schema permissions using `REVOKE`.

Example:

```
REVOKE CREATE
ON SCHEMA academics
FROM teacher_user;
```

This removes the `CREATE` permission from `teacher_user` on the `academics` schema.

To remove `USAGE`:

```
REVOKE USAGE
ON SCHEMA academics
FROM teacher_user;
```

## 21. Moving a Table from One Schema to Another

We can move an existing table between schemas using `ALTER TABLE ... SET SCHEMA`.

Syntax:

```
ALTER TABLE old_schema.table_name
SET SCHEMA new_schema;
```

Example:

```
ALTER TABLE public.students
SET SCHEMA academics;
```

The table is moved from `public` to `academics`.

Its new complete name is:

```
academics.students
```

The table's data is retained.

## 22. Viewing Tables Inside a Specific Schema

In the `psql` terminal, we can use:

```
\dt admissions.*
```

This displays tables in the `admissions` schema.

To view tables in all schemas:

```
\dt *.*
```

We can also use SQL:

```
SELECT table_schema, table_name
FROM information_schema.tables
WHERE table_schema = 'admissions'
  AND table_type = 'BASE TABLE'
ORDER BY table_name;
```

## 23. Schema vs Database

Students often confuse databases and schemas.

Let's understand the difference.

| Database                                                          | Schema                                                 |
| ----------------------------------------------------------------- | ------------------------------------------------------ |
| A database is a collection of schemas and other database objects. | A schema organizes database objects within a database. |
| A PostgreSQL server can contain multiple databases.               | A database can contain multiple schemas.               |
| A connection is made to a particular database.                    | A schema is accessed within the connected database.    |
| Created using `CREATE DATABASE`.                                  | Created using `CREATE SCHEMA`.                         |
| Deleted using `DROP DATABASE`.                                    | Deleted using `DROP SCHEMA`.                           |

Remember: A schema is inside a database. It is not a separate database.

## 24. Practical Example: University Database

Suppose we want to organize a university database into four schemas.

Step 1: Create schemas

```
CREATE SCHEMA admissions;

CREATE SCHEMA academics;

CREATE SCHEMA examinations;

CREATE SCHEMA finance;
```

Step 2: Create a table in admissions

```
CREATE TABLE admissions.applicants (
    applicant_id INT PRIMARY KEY,
    applicant_name VARCHAR(100),
    program VARCHAR(100)
);
```

Step 3: Create a table in academics

```
CREATE TABLE academics.courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100),
    credit_hours INT
);
```

Step 4: Create a table in examinations

```
CREATE TABLE examinations.results (
    result_id INT PRIMARY KEY,
    student_id INT,
    marks NUMERIC(5,2)
);
```

Step 5: Create a table in finance

```
CREATE TABLE finance.fees (
    fee_id INT PRIMARY KEY,
    student_id INT,
    amount NUMERIC(10,2)
);
```

Step 6: Display all schemas

```
SELECT schema_name
FROM information_schema.schemata
ORDER BY schema_name;
```

Step 7: Display all tables

```
SELECT table_schema, table_name
FROM information_schema.tables
WHERE table_schema IN (
    'admissions',
    'academics',
    'examinations',
    'finance'
)
ORDER BY table_schema, table_name;
```

We now have a university database organized into separate schemas.

## 25. Practice Exercises

### Beginner Level

1. Display all schemas in your PostgreSQL database.
2. Create a schema named `library`.
3. Create another schema named `hostel`.
4. Create a table named `books` inside the `library` schema.
5. Insert three records into `library.books`.
6. Retrieve all records from `library.books`.

### Intermediate Level

7. Create two schemas named `students` and `teachers`.
8. Create a table named `records` in both schemas.
9. Rename the `hostel` schema to `student_hostel`.
10. Move a table from `public` to `library`.
11. Change the owner of a schema.
12. Display all tables inside the `library` schema.

### Advanced Level

13. Create four schemas for a university: `admissions`, `academics`, `finance`, and `examinations`.
14. Create one table in each schema.
15. Grant `USAGE` permission on `academics` to `teacher_user`.
16. Grant `CREATE` permission on `library` to `teacher_user`.
17. Change the search path to `academics, public`.
18. Revoke the `CREATE` permission from `teacher_user`.
19. Delete an empty schema using `DROP SCHEMA`.
20. Explain the difference between `DROP SCHEMA` and `DROP SCHEMA CASCADE`.

## 26. Review Questions

1. What is a schema in PostgreSQL?
2. Why do we use schemas?
3. What is the default schema in PostgreSQL?
4. Which command creates a schema?
5. Which command displays existing schemas in psql?
6. How can we create a table inside a schema?
7. How can we rename a schema?
8. What is the purpose of `DROP SCHEMA CASCADE`?
9. What is the purpose of `search_path`?
10. What is the difference between `USAGE` and `CREATE` permissions?
11. How can we move a table from one schema to another?
12. What is the difference between a database and a schema?

## 27. Quick Revision

| Command                      | Purpose                                   |
| ---------------------------- | ----------------------------------------- |
| `CREATE SCHEMA`              | Create a schema                           |
| `\dn`                        | Display schemas                           |
| `ALTER SCHEMA`               | Modify a schema                           |
| `DROP SCHEMA`                | Delete an empty schema                    |
| `DROP SCHEMA CASCADE`        | Delete a schema and its dependent objects |
| `GRANT USAGE`                | Grant schema usage                        |
| `GRANT CREATE`               | Allow object creation                     |
| `REVOKE`                     | Remove permissions                        |
| `SET search_path`            | Change schema search order                |
| `ALTER TABLE ... SET SCHEMA` | Move a table to another schema            |
| `\dt schema_name.*`          | Display tables in a schema                |

Next Lesson: PostgreSQL Sequences and SERIAL / IDENTITY Columns

Students will learn how PostgreSQL generates automatic numbers for primary keys, how sequences work, and the difference between `SERIAL` and `IDENTITY`.