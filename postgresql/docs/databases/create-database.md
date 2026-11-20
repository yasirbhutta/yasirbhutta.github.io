---
layout: page
title: How to Create a Database in PostgreSQL
description: Learn how to create a PostgreSQL database using SQL commands or pgAdmin, verify it exists, and understand database naming rules and common errors.
keywords: create database PostgreSQL, CREATE DATABASE command, PostgreSQL database tutorial, create database with pgAdmin, create database with SQL, verify PostgreSQL database
---

## 1. Introduction

A database is an organized collection of information that allows us to store, manage, retrieve, and update data.

In a university, we need to store different types of information, such as:

- Student records
- Teacher records
- Department information
- Course information
- Examination results

To manage this information, we first need to create a database.

Example: We can create a database named `university` to manage university-related information.

## 2. What is CREATE DATABASE?

`CREATE DATABASE` is an SQL command used to create a new database in PostgreSQL.

In simple words, it tells PostgreSQL to create a new place where we can organize and store information.

For example:

```
CREATE DATABASE university;
```

This command creates a new database named `university`.

## 3. Understanding the SQL Command

Let's understand each part of the command.

```
CREATE DATABASE university;
```

| Part         | Explanation                                  |
| ------------ | -------------------------------------------- |
| `CREATE`     | Tells PostgreSQL to create something new.    |
| `DATABASE`   | Specifies that we want to create a database. |
| `university` | Name of the database.                        |
| `;`          | Indicates the end of the SQL statement.      |

Remember: Every SQL statement should normally end with a semicolon (`;`).

## 4. General Syntax

The general syntax for creating a database is:

```
CREATE DATABASE database_name;
```

Here, `database_name` represents the name of the database we want to create.

Examples:

```
CREATE DATABASE university;
```

```
CREATE DATABASE college;
```

```
CREATE DATABASE student_db;
```

Each command creates a separate database with the specified name.

## 5. Creating a Database Using pgAdmin

pgAdmin is a graphical user interface (GUI) tool used to manage PostgreSQL databases.

Follow these steps to create a database.

![How to Backup and Restore PostgreSQL Databases Using pgAdmin — CommandPrompt Inc.](https://images.openai.com/static-rsc-4/SkA-unyTs1PhcWKfC8OAuza4ueyfilStri17CArDFRyv_n7XS3uM-szHHimQpxMbM1VcljC6P6IoTDdae8KeG8nY363KVctXJcKGxMvhUwbZxUkXSYQ-5B5ADKRffU4rP2QknyWn9sWjNzrHLLk90R2ZMTVMuOxRpe2q4Gi0MGQ?purpose=inline)

[commandprompt.com](https://www.commandprompt.com/education/how-to-backup-and-restore-postgresql-databases-using-pgadmin/?utm_source=chatgpt.com)

1. Open pgAdmin.
2. Connect to your PostgreSQL server.
3. Expand the Servers section.
4. Expand the PostgreSQL server.
5. Right-click on Databases.
6. Select Create → Database.

![Complete PostgreSQL Setup: Create Databases, Fix Errors & Manage Users Like a Pro | by Durga Gadiraju | itversity | Medium](https://images.openai.com/static-rsc-4/9g9sk92sml7rFcwURLebmJGfXbGceU3n6aNRgU2J-1U_6KePt8fNsH98A4pU5Z5IhLR0YjPTuFvudtczaEaUGUonQwDS1NGHaM7prfFzp8AMLZNqXBerkJeBVU3kXZ6-91RSs36KjPABDzNkld3sQqxC--bSVvaLZ5xw-HJTaVU?purpose=inline)

[medium.com](https://medium.com/itversity/complete-postgresql-setup-create-databases-fix-errors-manage-users-like-a-pro-ace433f0e670?utm_source=chatgpt.com)

7. Enter `university` in the Database name field.
8. Click Save.

The `university` database will appear under the Databases section.

## 6. Creating a Database Using SQL

We can also create a database by writing an SQL command in the Query Tool.

Step 1: Open Query Tool

- Select an existing database, such as `postgres`.
- Open the Query Tool.

Step 2: Write the SQL command

```
CREATE DATABASE university;
```

Step 3: Execute the command

Click the Execute button or press `F5`.

![Создание базы данных PostgreSQL: команда CREATE DATABASE](https://images.openai.com/static-rsc-4/WRMAAsRfVX81TZrkAv0E3oJI_9CKaVn1BVLXKfceQ0KVpOZk_u4EKdhrqMMYMomkdda_ySqQlxRJbv7vn0MVwTeJZvPVYpeUXl1RIDr-sRVoQ0F7GgEE3HhFQ4zAoX54mRIW1XpLuoPLP60Jftb0OQ_zsFMP1x3bjXmySq4Ilkw?purpose=inline)

[cloud.ru](https://cloud.ru/blog/kak-sozdat-bazu-dannykh-postgresql?utm_source=chatgpt.com)

Expected Result:

```
CREATE DATABASE
```

This message indicates that PostgreSQL has successfully created the database.



Important

&#x20;The `CREATE DATABASE` command cannot be executed inside a transaction block. Run it as a standalone statement.



## 7. How to Verify a Database

After creating a database, we should check whether it exists.

We can use the following SQL query:

```
SELECT datname
FROM pg_database;
```

Explanation:

- `SELECT` retrieves information.
- `datname` represents the database name.
- `FROM pg_database` specifies the PostgreSQL system catalog containing database information.

The query displays the available databases on the PostgreSQL server.

## 8. Important Points to Remember

1. A database must have a name.
2. Database names must be unique within the same PostgreSQL server.
3. A user needs appropriate permission to create a database.
4. Use meaningful database names.
5. Use lowercase names without spaces for beginners.
6. A database can be created using pgAdmin or SQL commands.
7. Creating a database does not automatically create tables inside it.

## 9. Common Errors

| Incorrect Command            | Correct Command               |
| ---------------------------- | ----------------------------- |
| `CREATE university;`         | `CREATE DATABASE university;` |
| `CREATE DATABASE;`           | `CREATE DATABASE university;` |
| `CREATE DATABASE university` | `CREATE DATABASE university;` |

Duplicate database error:

If a database named `university` already exists, PostgreSQL will not allow us to create another database with the same name.

## 10. Practice Exercises

Exercise 1: Write SQL Commands

Write SQL commands to create the following databases:

1. `school`
2. `college`
3. `university`
4. `student_db`
5. `library`

Exercise 2: Practical Activity

Perform the following tasks using pgAdmin:

1. Open pgAdmin and connect to PostgreSQL.
2. Create a database named `university`.
3. Create another database named `college`.
4. Verify both databases in pgAdmin.
5. Write an SQL query to display all database names.
6. Try creating the `university` database again and observe the error.

## 11. Review Questions

1. What is a database?
2. What is the purpose of the `CREATE DATABASE` command?
3. Write the general syntax for creating a database.
4. What is the purpose of the semicolon in SQL?
5. What is pgAdmin?
6. What happens if we try to create a database that already exists?
7. How can we verify that a database has been created?
8. Does creating a database automatically create tables?

## 12. Quick Revision

| Concept         | Command / Explanation              |
| --------------- | ---------------------------------- |
| Create database | `CREATE DATABASE university;`      |
| General syntax  | `CREATE DATABASE database_name;`   |
| List databases  | `SELECT datname FROM pg_database;` |
| GUI tool        | pgAdmin                            |
| SQL execution   | Execute button / F5                |

Key Takeaway: The `CREATE DATABASE` command is the first step in building a database application in PostgreSQL. Before creating tables and inserting records, we must have a database in which to organize our information.

<!-- Next Lesson: Connecting to a Database in PostgreSQL (`\c` command in psql and database selection in pgAdmin). -->