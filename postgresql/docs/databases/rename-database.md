---
layout: page
title: Fix 'psql' is not recognized on Windows
description: Solutions to fix the 'psql' is not recognized error on Windows by adding PostgreSQL to PATH or reinstalling PostgreSQL with psql.
keywords: psql not recognized, PostgreSQL PATH, Windows environment variables, PostgreSQL installation, pgAdmin, psql windows error
---


# Renaming a Database in PostgreSQL

Student Notes | Database Management Systems (DBMS)

## 1. Introduction

Sometimes, we create a database with an incorrect name or want to change its name to something more meaningful.

PostgreSQL provides the `ALTER DATABASE` command to rename an existing database.

Example:

Suppose we have created a database named:

`college`

Now, we want to change its name to:

`university`

We can rename the database without creating a new one.

## 2. What is ALTER DATABASE?

`ALTER DATABASE` is an SQL command used to modify the properties of an existing database.

We can use this command to:

- Rename a database.
- Change the database owner.
- Modify certain database settings.

In this lesson, we will learn how to rename a database.

## 3. SQL Syntax

The general syntax for renaming a database is:

```
ALTER DATABASE old_database_name
RENAME TO new_database_name;
```

Explanation:

| Part                | Description                                |
| ------------------- | ------------------------------------------ |
| `ALTER DATABASE`    | Specifies the database we want to modify.  |
| `old_database_name` | Current name of the database.              |
| `RENAME TO`         | Specifies that we want to change its name. |
| `new_database_name` | New name of the database.                  |

## 4. Practical Example

Suppose we have an existing database named `college`.

We want to rename it to `university`.

SQL Command:

```
ALTER DATABASE college
RENAME TO university;
```

Explanation:

1. `ALTER DATABASE` tells PostgreSQL that we want to modify a database.
2. `college` is the current database name.
3. `RENAME TO` specifies the renaming operation.
4. `university` is the new database name.

Expected Result

ALTER DATABASE

PostgreSQL displays this message when the database is successfully renamed.

## 5. Important Conditions Before Renaming

PostgreSQL has some important restrictions when renaming a database.

1. You must have permission to rename the database.
2. You cannot rename the database to a name that already exists.
3. You cannot rename the database while connected to that same database.
4. Other active connections to the database must be closed before renaming it.

Important: Always connect to another database, such as `postgres`, before renaming your target database.

## 6. Rename a Database Using pgAdmin

We can also rename a database using pgAdmin.

Follow these steps:

[postgresql - How restore a Heroku PG database on a MAC - Stack Overflow](https://images.openai.com/static-rsc-4/_wgpKzr71vBVOKeZ_p01HsaUkZxBNey8KZzau5bJYsvfSe5KS4N3Mhhvo23UsN8NiuJfw0K4pU7KvYD_4YR3kTFT_cpJZy2eqPw7aFL9LjzbMreJUKe-Q5y2Hky-ilV2Riwng35kS8uDm-QMe1UT9zY0pEdjZfMPSwNm7nIZclY?purpose=inline)

[stackoverflow.com](https://stackoverflow.com/questions/49477196/how-restore-a-heroku-pg-database-on-a-mac?utm_source=chatgpt.com)

1. Open pgAdmin.
2. Connect to your PostgreSQL server.
3. Expand the Databases section.
4. Right-click the database you want to rename.
5. Select Properties.

[How to Rename Databases in PostgreSQL — CommandPrompt Inc.](https://images.openai.com/static-rsc-4/0-UbUHxLQntj9_whyRVkLqYneeL9lg3dJxRMYCDCYFjzpe1OHLN9XE-IyH1NzaLsPnQ3sOzMJe48ddLVh-aojvgK2usToSGj-oUWc-llNsY_sfyW0wTslJUH8EO6OBV_6VsIyVRKwF1TqBBB3Z8U0hyXgLx5vi6Cn0WvqMNIlM0?purpose=inline)

[commandprompt.com](https://www.commandprompt.com/education/rename-databases-postgresql/?utm_source=chatgpt.com)

6. Open the General tab.
7. Change the database name from `college` to `university`.
8. Click Save.

Note: If the database has active connections, close those connections before saving the new name.

## 7. Rename a Database Using SQL in pgAdmin

We can also perform this task through the Query Tool.

Step 1: Connect to another database

For example, select the `postgres` database in pgAdmin and open its Query Tool.

Step 2: Execute the following command

```
ALTER DATABASE college
RENAME TO university;
```

Step 3: Verify the result

Execute:

```
SELECT datname
FROM pg_database;
```

The database list should now contain `university` instead of `college`.

## 8. Common Errors

| Error                                     | Reason                           | Solution                                          |
| ----------------------------------------- | -------------------------------- | ------------------------------------------------- |
| Database is being accessed by other users | Active connections exist         | Close other connections                           |
| Cannot rename the currently open database | Connected to the target database | Connect to `postgres` first                       |
| Database already exists                   | New name is already in use       | Choose another name                               |
| Permission denied                         | Insufficient privileges          | Use an authorized database owner or administrator |

## 9. Practice Exercises

Exercise 1: Write SQL Commands

Write SQL commands to perform the following tasks:

1. Rename `school` to `college`.
2. Rename `college` to `university`.
3. Rename `student_db` to `students`.
4. Rename `library` to `central_library`.

Exercise 2: Practical Activity

Perform these tasks using pgAdmin:

1. Create a database named `my_college`.
2. Connect to the `postgres` database.
3. Rename `my_college` to `my_university`.
4. Verify the new database name.
5. Open the database list and confirm that the old name no longer exists.

## 10. Review Questions

1. Which SQL command is used to rename a database?
2. What is the purpose of `ALTER DATABASE`?
3. Write the general syntax for renaming a database.
4. Can we rename a database while connected to it?
5. Why should we close active connections before renaming?
6. How can we verify that a database has been renamed?
7. What happens if the new database name already exists?

## 11. Quick Revision

| Task            | SQL Command                                    |
| --------------- | ---------------------------------------------- |
| Create database | `CREATE DATABASE college;`                     |
| Rename database | `ALTER DATABASE college RENAME TO university;` |
| List databases  | `SELECT datname FROM pg_database;`             |

Key Takeaway: The `ALTER DATABASE ... RENAME TO` command is used to change the name of an existing PostgreSQL database. Always connect to a different database, such as `postgres`, before performing the renaming operation.

