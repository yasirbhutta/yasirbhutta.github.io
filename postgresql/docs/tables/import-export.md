# Student Notes: Importing and Exporting Data in PostgreSQL

## 1. Introduction

In database management, we often need to transfer data between PostgreSQL and external files.

For example, a university may need to:

- Import student records from an Excel-exported CSV file.
- Import employee information from another system.
- Export student results for reporting.
- Export fee records for financial analysis.
- Create backups of data for further processing.

PostgreSQL supports importing and exporting data using CSV, text files, SQL commands, and graphical tools such as pgAdmin.

## 2. What Is Data Import?

Data import means transferring data from an external file into a database table.

For example:

Suppose we have a CSV file containing student records:

students.csv

```
student_id,student_name,department,marks
1,Ali,Computer Science,85
2,Sara,Information Technology,92
3,Ahmed,Mathematics,78
4,Hina,Physics,88
```

We can import this information into a PostgreSQL table.

## 3. What Is Data Export?

Data export means transferring data from a database table or query into an external file.

For example, we can export student records from PostgreSQL into a CSV file.

The exported file can then be opened in:

- Microsoft Excel
- LibreOffice Calc
- Python
- Other database systems

## 4. Create a Sample Table

Before importing data, create a table in PostgreSQL.

```
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    department VARCHAR(100),
    marks NUMERIC(5,2)
);
```

This table contains four columns:

| Column       | Data type    | Purpose         |
| ------------ | ------------ | --------------- |
| student_id   | INT          | Student ID      |
| student_name | VARCHAR(50)  | Student name    |
| department   | VARCHAR(100) | Department name |
| marks        | NUMERIC(5,2) | Student marks   |

## 5. Importing CSV Data Using COPY

PostgreSQL provides the `COPY` command to import data from a file into a table.

Syntax:

```
COPY table_name
FROM 'file_path'
WITH (
    FORMAT CSV,
    HEADER TRUE,
    DELIMITER ','
);
```

Explanation:

- `COPY`: Transfers data between a file and a table.
- `table_name`: Destination table.
- `FROM`: Specifies the source file.
- `FORMAT CSV`: Specifies CSV format.
- `HEADER TRUE`: Skips the first row containing column names.
- `DELIMITER ','`: Specifies a comma as the separator.

Example:

```
COPY students
FROM '/path/to/students.csv'
WITH (
    FORMAT CSV,
    HEADER TRUE,
    DELIMITER ','
);
```

Replace the example path with the actual file path on the PostgreSQL server.

Important: SQL `COPY` reads the file from the database server's file system, not necessarily from your own computer.

## 6. Understanding HEADER TRUE

Consider the following CSV file:

```
student_id,student_name,department,marks
1,Ali,Computer Science,85
2,Sara,Information Technology,92
```

The first row contains column names, not actual student records.

When we use:

```
HEADER TRUE
```

PostgreSQL skips the first row.

Without this option, PostgreSQL may try to insert the column names as data, causing a data conversion error.

## 7. Importing CSV Data Using psql \copy

The `\copy` command is useful when the CSV file is stored on your own computer rather than the database server.

Syntax:

```
\copy table_name FROM 'file_path' WITH (FORMAT CSV, HEADER TRUE);
```

Example:

```
\copy students FROM 'C:/Data/students.csv' WITH (FORMAT CSV, HEADER TRUE);
```

Here:

- `\copy` is a psql client command.
- The file is read from the computer running psql.
- The data is transferred into the PostgreSQL database.

Important: `\copy` is not an SQL statement. It is a command available in the `psql` terminal.

## 8. Importing Data Using pgAdmin

pgAdmin provides a graphical interface for importing CSV files.

[How to Import CSV into PostgreSQL: COPY Command, pgAdmin, and Automated Pipelines](https://images.openai.com/static-rsc-4/w3tMblXx3D01qdjfR0LsHg7t23d8K_SpXrdtn_VobfTCBovzosxj0gJKJP-P8ZWBwIdYJ1eMDFlo70uA5WenNj0SsNZnXKPL6QGOp-5LeYnGN-uQ_xHISc29d6PjH5uoXZeBxJvLe0ZrH_FMb6TFHNUaNK7Fcc64i7RoCVMqOgE?purpose=inline)

[Import/Export Data Dialog — pgAdmin 4 9.12 documentation](https://images.openai.com/static-rsc-4/E0U0Y55kRdu4_uNAU-D5kOPfhxpGa73Mk7sm3CYlWnUjJJ-ka_YFVIMgM2DTwTuej-p-sTx5gnoLPjI912ab52coprR6MyiNjQFjPFS2oindXUd9jv5qXIZ3dYPrTBCmtjOD5kR9WNXbnPB-_rmQOne_rek78RlbJQtyucdemmY?purpose=inline)

[How to Import or Export CSVs to PostgreSQL Using pgAdmin — CommandPrompt Inc.](https://images.openai.com/static-rsc-4/hHSR6RZGO771qwmqZJwovQpEuxQxewEcVixEqP78KIM6mfbtrS3NbqLCo_xaaEF69e9y4EW-PGSysWfWZlfc4hYpNSkxOx04KxXfgiSVLiSBFrxSVwxNAr4X_kzYXrvCLmtSVwoxz2pBiIoFDk1kOW-h7JWh_S7X-RTtAu0Iefo?purpose=inline)

6

Follow these steps:

1. Open pgAdmin.
2. Connect to your PostgreSQL server.
3. Expand the required database.
4. Expand the `Schemas` folder.
5. Expand the `public` schema.
6. Expand the `Tables` folder.
7. Right-click the destination table.
8. Select Import/Export Data.
9. Select the Import option.
10. Browse and select the CSV file.
11. Choose the CSV format.
12. Enable the Header option if the first row contains column names.
13. Configure the delimiter and other options.
14. Click OK to start importing.

After importing, execute:

```
SELECT * FROM students;
```

Verify that the records have been imported correctly.

## 9. Exporting Data Using COPY

PostgreSQL also allows us to export table data into a CSV file.

Syntax:

```
COPY table_name
TO 'file_path'
WITH (
    FORMAT CSV,
    HEADER TRUE,
    DELIMITER ','
);
```

Example:

```
COPY students
TO '/path/to/students_export.csv'
WITH (
    FORMAT CSV,
    HEADER TRUE,
    DELIMITER ','
);
```

This exports all records from the `students` table into a CSV file.

The exported file will contain column names in the first row.

## 10. Exporting Data Using psql \copy

We can also export data to a CSV file on our own computer using `\copy`.

Example:

```
\copy students TO 'C:/Data/students_export.csv' WITH (FORMAT CSV, HEADER TRUE);
```

The file will be created on the computer running psql.

This is useful when you do not have direct access to the database server's file system.

## 11. Exporting Selected Columns

Sometimes, we do not need to export all columns.

We can export only the required columns using a query.

Example:

```
COPY (
    SELECT student_id, student_name, marks
    FROM students
)
TO '/path/to/student_marks.csv'
WITH (
    FORMAT CSV,
    HEADER TRUE
);
```

This exports only:

- Student ID
- Student name
- Marks

## 12. Exporting Filtered Records

We can also export records that meet specific conditions.

Example: Export students who obtained 80 or more marks.

```
COPY (
    SELECT *
    FROM students
    WHERE marks >= 80
)
TO '/path/to/high_achievers.csv'
WITH (
    FORMAT CSV,
    HEADER TRUE
);
```

Only students with marks greater than or equal to 80 will be exported.

## 13. Exporting Sorted Records

We can combine `ORDER BY` with the export query.

Example: Export students in descending order of marks.

```
COPY (
    SELECT *
    FROM students
    ORDER BY marks DESC
)
TO '/path/to/sorted_students.csv'
WITH (
    FORMAT CSV,
    HEADER TRUE
);
```

## 14. Importing Data into Specific Columns

Sometimes, a CSV file contains only a few columns of a table.

We can specify the destination columns in the `COPY` command.

Example:

```
COPY students (
    student_id,
    student_name,
    department
)
FROM '/path/to/students.csv'
WITH (
    FORMAT CSV,
    HEADER TRUE
);
```

In this example, the CSV file must contain values corresponding to the three specified columns.

The `marks` column must have a default value or allow `NULL`; otherwise, the import may fail.

## 15. Using a Different Delimiter

CSV files normally use commas to separate values.

However, some files use:

- Semicolons (`;`)
- Tabs
- Pipes (`|`)

We can specify a different delimiter.

Example:

Suppose the file contains:

```
student_id;student_name;department;marks
1;Ali;Computer Science;85
2;Sara;Information Technology;92
```

Import it using:

```
COPY students
FROM '/path/to/students.csv'
WITH (
    FORMAT CSV,
    HEADER TRUE,
    DELIMITER ';'
);
```

## 16. Exporting Data in Text Format

PostgreSQL also supports text format.

Example:

```
COPY students
TO '/path/to/students.txt'
WITH (
    FORMAT TEXT,
    DELIMITER '|'
);
```

This exports records using the pipe symbol as the separator.

Example output:

```
1|Ali|Computer Science|85
2|Sara|Information Technology|92
```

## 17. Importing and Exporting Data with NULL Values

Sometimes, a CSV file contains empty values.

Example:

```
student_id,student_name,department,marks
1,Ali,Computer Science,85
2,Sara,Information Technology,
```

By default, an unquoted empty field in CSV input represents `NULL`.

We can also specify a NULL representation.

Example:

```
COPY students
FROM '/path/to/students.csv'
WITH (
    FORMAT CSV,
    HEADER TRUE,
    NULL 'NULL'
);
```

In this case, a field containing the unquoted text `NULL` is interpreted as a SQL `NULL` value.

## 18. Importing and Exporting Data: COPY vs \copy

Both commands transfer data between files and PostgreSQL tables, but they work differently.

| Feature          | COPY                      | \copy               |
| ---------------- | ------------------------- | ------------------- |
| Type             | SQL command               | psql command        |
| File location    | Database server           | Client computer     |
| Execution        | PostgreSQL server         | psql client         |
| File permissions | Server permissions        | Client permissions  |
| Use              | Server-side file transfer | Local file transfer |

Remember:

- Use `COPY` when the file is accessible to the PostgreSQL server.
- Use `\copy` when the file is on the computer running psql.
- Use pgAdmin's Import/Export option when you prefer a graphical interface.

## 19. Common Import and Export Errors

### Error 1: Permission Denied

Reason: The PostgreSQL server does not have permission to read or write the specified file.

Solution: Check the file permissions or use `\copy` from psql.

### Error 2: File Does Not Exist

Reason: The specified file path is incorrect or inaccessible.

Solution: Verify the file path and location.

### Error 3: Invalid Input Syntax

Reason: The CSV value does not match the destination column's data type.

For example, inserting `ABC` into an integer column.

Solution: Check the CSV data and column data types.

### Error 4: Duplicate Primary Key

Reason: The imported file contains a student ID that already exists in the table.

Solution: Check for duplicate records before importing.

### Error 5: Column Count Does Not Match

Reason: The CSV file contains a different number of columns than the specified destination columns.

Solution: Check the CSV structure and the `COPY` column list.

## 20. Important Points to Remember

1. Importing means transferring data into a database.
2. Exporting means transferring data out of a database.
3. PostgreSQL supports CSV and text formats.
4. `COPY` is a PostgreSQL SQL command.
5. `\copy` is a psql client command.
6. `HEADER TRUE` skips the first row during CSV import.
7. `DELIMITER` specifies the separator.
8. `COPY TO` exports data.
9. `COPY FROM` imports data.
10. We can export selected and filtered records using a query.
11. pgAdmin provides a graphical Import/Export feature.
12. File permissions and data types should be checked before importing or exporting.

## 21. Practice Exercises

### Beginner Level

Exercise 1: Create a table named `employee` with the following columns:

- employee_id
- employee_name
- department
- salary

Exercise 2: Create a CSV file containing five employee records.

Exercise 3: Import the CSV file into the `employee` table using pgAdmin.

Exercise 4: Display all imported employee records.

Exercise 5: Export all employee records into a CSV file.

### Intermediate Level

Exercise 6: Export only employee names and departments.

Exercise 7: Export employees whose salary is greater than 50,000.

Exercise 8: Export employee records in descending order of salary.

Exercise 9: Import a semicolon-separated CSV file.

Exercise 10: Export employee records using the `\copy` command.

### Advanced Level

Exercise 11: Import data into selected columns of an existing table.

Exercise 12: Export the result of a query containing `WHERE`, `ORDER BY`, and selected columns.

Exercise 13: Import a CSV file containing empty fields and examine how PostgreSQL handles `NULL` values.

Exercise 14: Identify and resolve a data type mismatch during CSV import.

Exercise 15: Compare importing the same CSV file using pgAdmin, `COPY`, and `\copy`.

## 22. Review Questions

1. What is data importing?
2. What is data exporting?
3. What is the purpose of the `COPY` command?
4. What is the difference between `COPY` and `\copy`?
5. What does `HEADER TRUE` mean?
6. What is the purpose of the `DELIMITER` option?
7. How can we export selected columns?
8. How can we export records that meet a specific condition?
9. Why might a CSV import fail?
10. How can we import a CSV file using pgAdmin?

## 23. Quick Revision

| Command / Option      | Purpose                     |
| --------------------- | --------------------------- |
| `COPY table FROM`     | Import data                 |
| `COPY table TO`       | Export data                 |
| `\copy`               | Client-side import/export   |
| `FORMAT CSV`          | Use CSV format              |
| `FORMAT TEXT`         | Use text format             |
| `HEADER TRUE`         | Handle column headings      |
| `DELIMITER`           | Specify field separator     |
| `NULL`                | Specify NULL representation |
| `WHERE`               | Filter exported records     |
| `ORDER BY`            | Sort exported records       |
| pgAdmin Import/Export | Graphical data transfer     |

Next Lesson: PostgreSQL Backup and Restore

In the next lesson, students will learn how to create database backups, restore databases, and use PostgreSQL tools such as `pg_dump` and `pg_restore`.