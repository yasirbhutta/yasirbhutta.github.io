# Lesson 1.5: Introduction to PostgreSQL

## 1. What Is PostgreSQL?

PostgreSQL is a powerful, open-source relational database management system (RDBMS).

It is used to store, organize, retrieve, and manage data.

PostgreSQL uses SQL (Structured Query Language) to communicate with relational databases.

In simple words:

**PostgreSQL is database software that helps us create databases and manage information using SQL.**

## 2. What Does Open Source Mean?

Open-source software is software whose source code is available under a license that allows users to use, study, modify, and distribute it according to the license terms.

PostgreSQL is available free of charge under the PostgreSQL License, a permissive open-source license.

## 3. What Is SQL?

SQL stands for **Structured Query Language**.

It is used to communicate with relational database systems.

Using SQL, we can:

- Create databases.
- Create tables.
- Insert records.
- Retrieve records.
- Update records.
- Delete records.
- Manage database permissions.

## 4. First PostgreSQL Query

After connecting to a PostgreSQL database, we can execute an SQL command.

```sql
SELECT version();
```

This command displays information about the installed PostgreSQL version.

Another simple query is:

```sql
SELECT 'Hello, PostgreSQL!';
```

Expected result:

| ?column? |
|---|
| Hello, PostgreSQL! |

## 5. Understanding the Query

```sql
SELECT 'Hello, PostgreSQL!';
```

- `SELECT` is an SQL command used to retrieve or calculate a result.
- `'Hello, PostgreSQL!'` is a text value.
- `;` marks the end of the SQL statement.

## 6. PostgreSQL Applications

PostgreSQL is used in:

- Web applications
- University management systems
- Banking and financial systems
- E-commerce websites
- Business applications
- Data analysis systems
- Geographic information systems

## 7. Quick Summary

- PostgreSQL is an open-source relational DBMS.
- It stores and manages data.
- It uses SQL to communicate with databases.
- It supports a wide range of applications.

## Practice Questions

1. What is PostgreSQL?
2. What does RDBMS stand for?
3. What does open-source mean?
4. What does SQL stand for?
5. Write two examples of applications that can use PostgreSQL.
6. What is the purpose of `SELECT version();`?

---
