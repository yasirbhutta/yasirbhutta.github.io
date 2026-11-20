# Introduction to Tables in PostgreSQL

Student Notes | Database Management Systems (DBMS)

## 1. Introduction

In the previous lessons, we learned how to create, rename, and delete databases in PostgreSQL.

Now, let's learn how to store information inside a database.

A database can contain multiple tables. A table is used to organize information into rows and columns.

For example, a university database may contain different tables for:

- Students
- Teachers
- Departments
- Courses
- Examinations

Each table stores information about a particular subject.

## 2. What is a Table?

A table is a database object that stores information in the form of rows and columns.

Real-life example:

Consider a university that maintains student information.

[Understanding Database Table Structure: Rows, Columns, Fields, and Records | Akshita Patel posted on the topic | LinkedIn](https://images.openai.com/static-rsc-4/IGSfkiOeuXopQ8zMYSKjmYVwcUgVbaJgQoJO_QuA2qTC9lNfQyYFAIUCCq0vU2jOnzROpAXASaJLFTzc5emrpnjy5tB9N2cxvm9qbDkUq0k8_q14JMueWcpZlaAavPGc_bZWZ23f50-7G1t9i-orl_sYi6XAg-Nehpz5iW7nRWg?purpose=inline)

[linkedin.com](https://www.linkedin.com/posts/akshita-patel-60b1151a1_database-datamanagement-sql-activity-7364214021987696641-HNaD?utm_source=chatgpt.com)

The table contains the following information:

| Student ID | Student Name | Age | Department  |
| ---------- | ------------ | --- | ----------- |
| 101        | Ali          | 20  | CS          |
| 102        | Ahmed        | 21  | IT          |
| 103        | Sara         | 19  | Mathematics |
| 104        | Usman        | 22  | CS          |

This table stores information about four students.

## 3. Understanding Rows and Columns

A table consists of two basic components: rows and columns.

### A. What is a Row?

A row represents one complete record in a table.

For example:

| Student ID | Student Name | Age | Department |
| ---------- | ------------ | --- | ---------- |
| 101        | Ali          | 20  | CS         |

This row contains the complete information of one student.

Remember: A row is also called a record or tuple.

### B. What is a Column?

A column represents a particular type of information stored in a table.

For example:

| Student ID |
| ---------- |
| 101        |
| 102        |
| 103        |
| 104        |

The `Student ID` column stores the identification numbers of students.

Other examples of columns include:

- Student Name
- Age
- Department
- Email Address

Remember: A column is also called a field or attribute.

## 4. Understanding Table Structure

Consider the following students table:

| student_id | name  | age | department  |
| ---------- | ----- | --- | ----------- |
| 101        | Ali   | 20  | CS          |
| 102        | Ahmed | 21  | IT          |
| 103        | Sara  | 19  | Mathematics |

In this example:

| Component         | Value                             |
| ----------------- | --------------------------------- |
| Table name        | students                          |
| Number of columns | 4                                 |
| Number of records | 3                                 |
| Column names      | student_id, name, age, department |

[SQL Interview Cheat Sheet |   LearnSQL.com](https://images.openai.com/static-rsc-4/Kiho4Ian2wGonBKto9v66xpPZO_vWLfz6RicG7bketF-ibnNap0gvA2qqD4INZWNXt63MakVshDbcnUzgmJ5ywk5t60IMSgddTS2iTS09McLoyh8_qED4v4U7RMNSZpB4cg3ghlPiQDbBUg4IncXtdIjDAe-SS9H0BdBliPxNtE?purpose=inline)

[learnsql.com](https://learnsql.com/blog/sql-interview-cheat-sheet/?utm_source=chatgpt.com)

## 5. What is CREATE TABLE?

`CREATE TABLE` is an SQL command used to create a new table inside a database.

Before creating a table, we should connect to the database where we want to store the table.

For example, we have a database named `university`. Now, we want to create a table named `students`.

## 6. SQL Syntax for Creating a Table

The general syntax is:

```
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype
);
```

Explanation:

| Part           | Description                          |
| -------------- | ------------------------------------ |
| `CREATE TABLE` | Creates a new table.                 |
| `table_name`   | Name of the table.                   |
| `column1`      | First column name.                   |
| `datatype`     | Type of information a column stores. |
| `;`            | Ends the SQL statement.              |

## 7. Create Your First Table

Let's create a table named `students`.

SQL Command:

```
CREATE TABLE students (
    student_id INTEGER,
    name VARCHAR(100),
    age INTEGER,
    department VARCHAR(100)
);
```

Understanding the Code:

1. `CREATE TABLE students` creates a table named `students`.
2. `student_id INTEGER` creates a column for student identification numbers.
3. `name VARCHAR(100)` creates a column for student names.
4. `age INTEGER` creates a column for student ages.
5. `department VARCHAR(100)` creates a column for department names.

Expected Result

CREATE TABLE

PostgreSQL displays this message when the table is created successfully.

## 8. Understanding Data Types

A data type defines what kind of information a column can store.

For example:

| Data Type     | Purpose                 | Example          |
| ------------- | ----------------------- | ---------------- |
| INTEGER       | Whole numbers           | 101              |
| VARCHAR(100)  | Variable-length text    | Ali              |
| TEXT          | Text of variable length | Computer Science |
| DATE          | Date values             | 2026-11-09       |
| BOOLEAN       | True or false           | TRUE             |
| NUMERIC(10,2) | Decimal numbers         | 25000.50         |

Examples:

```
student_id INTEGER
```

Stores whole numbers.

```
name VARCHAR(100)
```

Stores text up to 100 characters.

```
fee NUMERIC(10,2)
```

Stores numeric values with up to two decimal places.

We will study data types in detail in the next lesson.

## 9. Creating a Table Using pgAdmin

We can also create a table using the graphical interface of pgAdmin.

[Como importar CSVs para o PostgreSQL usando o pgAdmin |   LearnSQL.com.br](https://images.openai.com/static-rsc-4/_ND4aNEydzvg_MTykYKceXVDo9IEK5vGM-4ToWgvADKZA7eNSUBESEbNfTAOSp9SGOTRt8gxCDsXgLbW3g3VmIXLLvxzHO_dn4Z2NZJMSSfjvbP3fUGNvQqj65u1eKbDY7E9-v0vvzl6mTGMFoO8bTu18UxX7VPtke5CE1JNf_4?purpose=inline)

[learnsql.com.br](https://learnsql.com.br/blog/como-importar-csvs-para-o-postgresql-usando-o-pgadmin/?utm_source=chatgpt.com)

Follow these steps:

1. Open pgAdmin.
2. Expand Servers.
3. Expand Databases.
4. Expand the `university` database.
5. Expand Schemas.
6. Expand the `public` schema.
7. Right-click on Tables.
8. Select Create → Table.

[Table Dialog — pgAdmin 4 9.14 documentation](https://images.openai.com/static-rsc-4/SRAC3sZtOXelUHnj7KdK93NQ3qD5C9gxmFYd3_s41saN4YoBCiFC6uVMbZLoIEkB1ox-GLDRZG7aZ1HeSgSSD9cVNa7M_eXedq6gmJF4CCmPy5dCJ-hsJX834D7jTQtiWPYg9tiXMemxcFmGGptXiWRe9OJfdmSN0CqXrdIACFA?purpose=inline)

[pgadmin.org](https://www.pgadmin.org/docs/pgadmin4/9.14/table_dialog.html?utm_source=chatgpt.com)

9. Enter `students` as the table name.
10. Open the Columns tab.
11. Add the required column names and data types.
12. Click Save.

The `students` table will appear under the Tables section.

## 10. Verify the Table

After creating a table, we should verify that it exists.

We can use the following SQL query:

```
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public';
```

This query displays the names of tables in the `public` schema of the current database.

To view the table structure, use:

```
SELECT *
FROM students;
```

This query displays the records currently stored in the table. If the table is empty, the result will contain no records.

## 11. Important Points to Remember

1. A database can contain multiple tables.
2. A table stores information in rows and columns.
3. A row represents one record.
4. A column represents one type of information.
5. Every column has a name and a data type.
6. The `CREATE TABLE` command creates a new table.
7. Tables are created inside a database and belong to a schema.

## 12. Practice Exercises

Exercise 1: Identify Rows and Columns

Consider the following table:

| employee_id | employee_name | age | salary |
| ----------- | ------------- | --- | ------ |
| 1           | Ali           | 25  | 50000  |
| 2           | Ahmed         | 28  | 60000  |
| 3           | Sara          | 24  | 55000  |

Answer the following questions:

1. What is the table name if we call it `employees`?
2. How many columns are there?
3. How many records are there?
4. Which column stores employee names?
5. What is the salary of Ahmed?

Exercise 2: Write SQL Commands

Write SQL commands to create the following tables.

1. `teachers` with teacher_id, name, age, and department.
2. `courses` with course_id, course_name, and credit_hours.
3. `departments` with department_id and department_name.
4. `books` with book_id, title, author, and price.

Exercise 3: Practical Activity

Using PostgreSQL:

1. Connect to the `university` database.
2. Create a table named `students`.
3. Add four columns: student_id, name, age, and department.
4. Verify that the table has been created.
5. Display the table structure using pgAdmin.

## 13. Review Questions

1. What is a table in PostgreSQL?
2. What is the difference between a row and a column?
3. What is a record?
4. What is an attribute?
5. Which SQL command is used to create a table?
6. What is a data type?
7. Can a database contain multiple tables?
8. What is the purpose of the `VARCHAR(100)` data type?

## 14. Quick Revision

| Concept      | Explanation                         |
| ------------ | ----------------------------------- |
| Database     | Collection of organized information |
| Table        | Collection of rows and columns      |
| Row          | One complete record                 |
| Column       | One type of information             |
| Data Type    | Defines the kind of data            |
| CREATE TABLE | Creates a new table                 |

Key Takeaway: A database stores information in tables. Each table consists of rows and columns. The `CREATE TABLE` command is used to create tables in PostgreSQL.

Next Lesson: PostgreSQL Data Types — INTEGER, VARCHAR, TEXT, DATE, BOOLEAN, and NUMERIC.