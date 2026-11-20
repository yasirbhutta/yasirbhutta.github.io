# Student Notes: Backup and Restore in PostgreSQL

## 1. Introduction

Databases contain important information such as student records, employee details, examination results, fee records, and university information.

If a database is accidentally deleted, damaged, or affected by a system failure, important information may be lost.

To protect database information, PostgreSQL provides backup and restore facilities.

For example, a university may create regular backups of its student database so that the information can be recovered if a problem occurs.

In this lesson, we will learn how to:

- Create database backups.
- Restore a database from a backup.
- Back up individual tables.
- Restore individual tables.
- Use PostgreSQL backup tools.
- Perform backup and restore operations through pgAdmin.

## 2. What Is a Database Backup?

A database backup is a copy of database information saved in a separate file.

This file can be used to recover the database if the original database is lost or damaged.

For example:

Suppose a university has a database named `university_db`.

We can create a backup file:

```
university_db.backup
```

If the original database is accidentally deleted, we can use this backup file to restore the database.

## 3. What Is Database Restore?

Database restore means recovering database information from a previously created backup file.

For example:

- Original database: `university_db`
- Backup file: `university_db.backup`
- Restored database: `university_db`

The restore operation uses the backup file to recreate the database objects and data.

## 4. Why Are Backup and Restore Important?

Database backups are important for several reasons:

1. Data Protection: Protect important records from accidental loss.
2. System Failure: Recover information after hardware or software failure.
3. Human Errors: Recover data after accidental deletion or modification.
4. Migration: Move databases between servers.
5. Disaster Recovery: Restore services after major incidents.
6. Testing: Create copies of production databases for testing.

## 5. PostgreSQL Backup Tools

PostgreSQL provides several tools for creating and restoring backups.

| Tool         | Purpose                                                       |
| ------------ | ------------------------------------------------------------- |
| `pg_dump`    | Creates a backup of one database                              |
| `pg_restore` | Restores backups created in custom, directory, or tar formats |
| `pg_dumpall` | Creates a backup of all databases and global objects          |
| `psql`       | Executes SQL commands and restores plain SQL backups          |

Important: `pg_dump` and `pg_restore` are command-line utilities included with PostgreSQL.

## 6. Understanding PostgreSQL Backup Formats

PostgreSQL supports different backup formats.

| Format    | Description                                            |
| --------- | ------------------------------------------------------ |
| Plain SQL | Stores SQL statements in a text file                   |
| Custom    | Stores backup in PostgreSQL's custom archive format    |
| Directory | Stores backup in a directory containing multiple files |
| Tar       | Stores backup in a tar archive                         |

The most commonly used formats are:

- Plain SQL (`.sql`)
- Custom (`.backup`)

Recommendation: Use the custom format when you want flexible restoration options through `pg_restore`.

## 7. Creating a Backup Using pg_dump

The `pg_dump` utility creates a backup of a PostgreSQL database.

Syntax:

```
pg_dump -U username -d database_name -f backup_file.sql
```

Explanation:

- `pg_dump`: PostgreSQL backup utility.
- `-U`: Specifies the database username.
- `-d`: Specifies the database name.
- `-f`: Specifies the output backup file.

Example:

```
pg_dump -U postgres -d university_db -f university_backup.sql
```

This command creates a plain SQL backup file named:

```
university_backup.sql
```

## 8. Creating a Custom Format Backup

We can create a custom-format backup using the `-F c` option.

Example:

```
pg_dump -U postgres -d university_db -F c -f university_backup.backup
```

Explanation:

- `-F c`: Specifies custom format.
- `-f`: Specifies the backup file.

The custom-format backup can be restored using `pg_restore`.

## 9. Creating a Backup Using pgAdmin

pgAdmin provides a graphical interface for creating database backups.

[How to Dump Your Database – Data Science for Social Good](https://images.openai.com/static-rsc-4/0BBBitFP2t-tOMOJjFIGrOlRSVj3jOWeXIyIQlMki2T-z7B940YawwAsBXGat3o6ziZtGV7AGg0w3ZIZ9aydm797bj1Wg5lY4lJNx7ziyC4Kfewx3mhCEjyqt1DFYRh9Htg8pTWyPD8Gr9YsIokdkpTNzo4gBxLaIDEznoJ3z5U?purpose=inline)

[Backup Dialog — pgAdmin 4 9.12 documentation](https://images.openai.com/static-rsc-4/t2nG29Fn_76-h5dxuyEKOl_2lqoU3oKyqViZ3JBEaDWwGh-rfFWaUYisxQ07RF-tWJvcQ8Ol7KjFOq9Yx9-bHqU0LaIeqFkw4ZKVOZODDwz7BaBd4EFjn7pOIb0ThyH5X9sfqC88lyi6ptypRdsE8zX4-FzKz56zYlqnQg0Hj54?purpose=inline)

Follow these steps:

1. Open pgAdmin.
2. Connect to your PostgreSQL server.
3. Expand the Databases folder.
4. Right-click the database you want to back up.
5. Select Backup.
6. Open the General tab.
7. Enter the backup file name.
8. Select the backup format, such as Custom.
9. Configure additional options if required.
10. Click Backup.

After successful completion, pgAdmin creates the backup file at the specified location.

## 10. Restoring a Plain SQL Backup Using psql

A plain SQL backup contains SQL statements that recreate database objects and insert data.

We can restore it using the `psql` utility.

Syntax:

```
psql -U username -d database_name -f backup_file.sql
```

Example:

```
psql -U postgres -d university_db -f university_backup.sql
```

This executes the SQL statements stored in the backup file against the specified database.

Important: The target database normally needs to exist before restoring a plain SQL backup. If the backup contains commands to create the database, use an appropriate connection and restore procedure.

## 11. Creating a New Database Before Restoring

If you want to restore the backup into a new database, first create the database.

Connect to PostgreSQL and execute:

```
CREATE DATABASE university_restore;
```

Then restore the plain SQL backup:

```
psql -U postgres -d university_restore -f university_backup.sql
```

This restores the backup contents into `university_restore`.

## 12. Restoring a Custom Format Backup Using pg_restore

The `pg_restore` utility restores custom, directory, and tar-format backups.

Syntax:

```
pg_restore -U username -d database_name backup_file
```

Example:

```
pg_restore -U postgres -d university_restore university_backup.backup
```

This restores the custom-format backup into the `university_restore` database.

Important: The target database must exist before using this command unless you use the appropriate create-database option.

## 13. Restoring a Custom Backup with Database Creation

We can use the `-C` option to create the database during restoration.

Example:

```
pg_restore -U postgres -C -d postgres university_backup.backup
```

Here:

- `-C`: Creates the database using the database name stored in the backup.
- `-d postgres`: Connects to the existing `postgres` database before restoration.

This is useful when the backup contains the database creation information.

## 14. Backup and Restore Using pgAdmin

We can also restore a database through pgAdmin.

[How to Restore a Database in pgAdmin 4](https://images.openai.com/static-rsc-4/ubQ3-tyET0ZgTQ-_XVTwpW20Bc6oyqTMVNsNAKs7MtVwT2CQaRAI9kBqjp0F2eioLIUchYPs5_ntGQk5FyS8nHFgYbLfaw56o6cCn8E1K4ugXTr9SBUzaEGcno1uM7g3VnclLFNU_owOgSx-30fIX3mwb0JqJ1s3GqmNAu0bMFM?purpose=inline)

[Restore Dialog — pgAdmin 4 9.17 documentation](https://images.openai.com/static-rsc-4/EK19X33laHS3on33WX6RASW4WKeBGZXm1exd55T5TDAOdBDS_8EmqAvWrV-V9qWzETv1F_ea_vHS8uYbxIQpofPkxLU9svrar1g0cAwBX-Y1Pe7l3sQAX5wTGyTZTEaPPtNKulpH17Snah8U4nt3K7gAsorsi1lF8-kqvEdgfrw?purpose=inline)

4

Follow these steps:

1. Open pgAdmin.
2. Connect to your PostgreSQL server.
3. Create a new empty database if required.
4. Right-click the destination database.
5. Select Restore.
6. Open the General tab.
7. Select the backup file.
8. Choose the correct format.
9. Configure restore options if required.
10. Click Restore.

After successful restoration, refresh the database and check its tables.

Note: The Restore option in pgAdmin is generally used for custom, tar, and directory archives. For plain SQL files, use the Query Tool or the `psql` utility.

## 15. Backing Up a Specific Table

Sometimes, we do not need to back up the complete database.

We can back up an individual table using `pg_dump` with the `-t` option.

Syntax:

```
pg_dump -U username -d database_name -t table_name -f backup.sql
```

Example:

```
pg_dump -U postgres -d university_db -t students -f students_backup.sql
```

This creates a backup of the `students` table.

## 16. Restoring a Specific Table

A custom-format backup can be used to restore selected tables.

Example:

```
pg_restore -U postgres -d university_restore -t students university_backup.backup
```

This restores the `students` table from the custom backup.

The destination database should exist, and any required dependent objects should be considered.

## 17. Backing Up All PostgreSQL Databases

The `pg_dumpall` utility creates a backup of all databases in a PostgreSQL server, along with global objects such as roles and tablespaces.

Syntax:

```
pg_dumpall -U postgres -f all_databases.sql
```

This creates a plain SQL file containing the server-wide backup.

To restore it:

```
psql -U postgres -d postgres -f all_databases.sql
```

Important: Restoring a full-server backup may require appropriate privileges. It can also recreate or conflict with existing roles and databases, so review the backup before restoring it on a server that already contains data.

## 18. Viewing the Contents of a Backup

Before restoring a custom-format backup, we can view the objects stored inside it.

Use the `-l` option with `pg_restore`.

Example:

```
pg_restore -l university_backup.backup
```

This displays information about the database objects included in the backup, such as:

- Tables
- Views
- Functions
- Sequences
- Data

This is useful when you want to inspect a backup before restoring it.

## 19. Backing Up Only the Database Structure

Sometimes, we need to back up the database structure without its records.

This is called a schema-only backup.

Example:

```
pg_dump -U postgres -d university_db --schema-only -f schema_backup.sql
```

This backs up database objects such as:

- Tables
- Views
- Functions
- Constraints
- Indexes

It does not include the table records.

## 20. Backing Up Only the Data

We can also create a backup containing only the table data without the database structure.

Example:

```
pg_dump -U postgres -d university_db --data-only -f data_backup.sql
```

This backup contains data insertion commands but does not recreate the database structure.

Remember:

| Option          | Purpose                    |
| --------------- | -------------------------- |
| `--schema-only` | Back up database structure |
| `--data-only`   | Back up table data         |
| Default         | Back up structure and data |

## 21. Backing Up a Database with Compression

PostgreSQL custom-format backups support compression.

Example:

```
pg_dump -U postgres -d university_db -F c -Z 6 -f university_backup.backup
```

Here:

- `-F c`: Creates a custom-format backup.
- `-Z 6`: Sets the compression level.
- `-f`: Specifies the backup file.

The compression level can range from 0 to 9, depending on the PostgreSQL version and supported options.

Compression helps reduce backup storage requirements.

## 22. Checking PostgreSQL Backup Tools

Sometimes, the PostgreSQL command-line tools are not recognized by the operating system.

We can check whether they are installed and accessible.

Example:

```
pg_dump --version
```

Check the restore utility:

```
pg_restore --version
```

Check the psql utility:

```
psql --version
```

If these commands are not recognized, check whether the PostgreSQL `bin` directory is included in the system's PATH environment variable.

On Windows, the tools are commonly located in a directory similar to:

```
C:\Program Files\PostgreSQL\17\bin
```

The version number may be different on your computer.

## 23. Understanding Backup and Restore Commands

Let's compare the most commonly used commands.

| Command                 | Purpose                                           |
| ----------------------- | ------------------------------------------------- |
| `pg_dump`               | Back up one database                              |
| `pg_restore`            | Restore archive-format backups                    |
| `pg_dumpall`            | Back up all databases and global objects          |
| `psql`                  | Execute SQL scripts and restore plain SQL backups |
| `pg_restore -l`         | Display archive contents                          |
| `pg_dump --schema-only` | Back up database structure                        |
| `pg_dump --data-only`   | Back up database records                          |

## 24. Practical Lab: Backup and Restore a Database

Let's perform a complete practical exercise using a database named `university_db`.

### Step 1: Create a Database

```
CREATE DATABASE university_db;
```

### Step 2: Connect to the Database

In pgAdmin, select `university_db` and open the Query Tool.

### Step 3: Create a Table

```
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    department VARCHAR(50)
);
```

### Step 4: Insert Sample Records

```
INSERT INTO students
VALUES
(1, 'Ali', 'Computer Science'),
(2, 'Sara', 'Information Technology'),
(3, 'Ahmed', 'Mathematics');
```

### Step 5: Verify the Records

```
SELECT * FROM students;
```

### Step 6: Create a Custom Backup

Run this command in the operating system terminal:

```
pg_dump -U postgres -d university_db -F c -f university_backup.backup
```

### Step 7: Create a New Database

```
CREATE DATABASE university_restore;
```

### Step 8: Restore the Backup

Run:

```
pg_restore -U postgres -d university_restore university_backup.backup
```

### Step 9: Verify the Restored Records

Connect to `university_restore` and execute:

```
SELECT * FROM students;
```

Expected output:

| student_id | student_name | department             |
| ---------- | ------------ | ---------------------- |
| 1          | Ali          | Computer Science       |
| 2          | Sara         | Information Technology |
| 3          | Ahmed        | Mathematics            |

Practical completed

The records from the original database have been restored into a new database.

## 25. Important Backup and Restore Best Practices

1. Create database backups regularly.
2. Store backup files separately from the original database server.
3. Keep more than one backup copy.
4. Use meaningful backup file names.
5. Include the backup date in the file name.
6. Protect backup files because they may contain confidential information.
7. Verify that backup files are readable.
8. Test restoration periodically.
9. Keep a backup before major database changes or migrations.
10. Document the backup and recovery procedure.

Example backup file naming:

```
university_backup_2026-11-09.backup
```

Important: A backup is useful only if it can be restored successfully. Always test your recovery procedure.

## 26. Common Backup and Restore Errors

### Error 1: Password Authentication Failed

Reason: The database username or password is incorrect.

Solution: Verify the PostgreSQL username and password.

### Error 2: Database Does Not Exist

Reason: The destination database has not been created.

Solution: Create the database before restoring, or use an appropriate database-creation option.

### Error 3: Permission Denied

Reason: The database user does not have sufficient permissions.

Solution: Use an account with the required privileges.

### Error 4: Backup File Not Found

Reason: The backup file path is incorrect.

Solution: Check the file location and name.

### Error 5: Unsupported Backup Format

Reason: The wrong utility is being used for the backup format.

Solution:

- Use `psql` for plain SQL backups.
- Use `pg_restore` for custom, directory, and tar backups.

### Error 6: Objects Already Exist

Reason: The destination database already contains objects with the same names.

Solution: Restore into a clean database or carefully use appropriate cleanup options. Be cautious because cleanup options can delete existing objects.

## 27. Practice Exercises

### Beginner Level

Exercise 1: Create a database named `college_db`.

Exercise 2: Create a table named `students` with student ID, name, and department.

Exercise 3: Insert five student records.

Exercise 4: Create a plain SQL backup using `pg_dump`.

Exercise 5: Check the PostgreSQL backup utility version.

### Intermediate Level

Exercise 6: Create a custom-format backup of `college_db`.

Exercise 7: Create a new database named `college_restore`.

Exercise 8: Restore the custom backup into `college_restore`.

Exercise 9: Verify that all student records have been restored.

Exercise 10: Create a schema-only backup of `college_db`.

### Advanced Level

Exercise 11: Create a data-only backup.

Exercise 12: Create a backup of only the `students` table.

Exercise 13: Display the contents of a custom-format backup using `pg_restore -l`.

Exercise 14: Create a compressed custom-format backup.

Exercise 15: Back up all PostgreSQL databases using `pg_dumpall`.

## 28. Review Questions

1. What is a database backup?
2. What is database restoration?
3. Why are backups important?
4. What is the purpose of `pg_dump`?
5. What is the purpose of `pg_restore`?
6. What is the difference between `pg_dump` and `pg_dumpall`?
7. What is the difference between plain SQL and custom-format backups?
8. Which utility restores a plain SQL backup?
9. What does the `--schema-only` option do?
10. What does the `--data-only` option do?
11. How can we back up an individual table?
12. Why should we test database restoration regularly?

## 29. Quick Revision

| Task                  | Command                                                            |
| --------------------- | ------------------------------------------------------------------ |
| Plain SQL backup      | `pg_dump -U postgres -d university_db -f backup.sql`               |
| Custom backup         | `pg_dump -U postgres -d university_db -F c -f backup.backup`       |
| Restore plain SQL     | `psql -U postgres -d university_restore -f backup.sql`             |
| Restore custom backup | `pg_restore -U postgres -d university_restore backup.backup`       |
| Backup all databases  | `pg_dumpall -U postgres -f all.sql`                                |
| Backup one table      | `pg_dump -U postgres -d university_db -t students -f students.sql` |
| Schema-only backup    | `pg_dump -U postgres -d university_db --schema-only -f schema.sql` |
| Data-only backup      | `pg_dump -U postgres -d university_db --data-only -f data.sql`     |
| List backup contents  | `pg_restore -l backup.backup`                                      |
| Check tool version    | `pg_dump --version`                                                |

Next Lesson: PostgreSQL User Management and Roles

In the next lesson, students will learn how to create database users, create roles, assign permissions, change passwords, and manage database access using `CREATE USER`, `CREATE ROLE`, `GRANT`, and `REVOKE`.