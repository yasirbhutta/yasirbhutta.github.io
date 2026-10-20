---
layout: page
title: "PostgreSQL Practice Exercises"
description: Practice PostgreSQL user creation and permission management by creating a trainee role, granting database access, testing table permissions, and using GRANT and REVOKE in a realistic lab exercise.
keywords: PostgreSQL practice exercises, database permissions, user creation, GRANT, REVOKE, psql, trainee user, dvdrental, SQL access control, PostgreSQL tutorial, database admin tasks, schema permissions, table privileges, SQL lab exercise
---

# Problem Statement 1: PostgreSQL User Creation and Permission Management

A database administrator wants to provide a new trainee, named `trainee`, with controlled access to the PostgreSQL `dvdrental` database.

The administrator must create a new database user, allow the user to connect to the database, and test the user's permissions. Initially, the trainee should not have permission to read data from the `film` table. The administrator will then grant `SELECT` permission on that table and verify that the trainee can retrieve records successfully.

## Tasks

1. Connect to PostgreSQL using the administrator account.
2. Create a new user named `trainee` with a password.
3. Grant the user permission to connect to the `dvdrental` database.
4. Log in to the database using the `trainee` account.
5. Test access to the `film` table before granting `SELECT` permission.
6. Grant `SELECT` permission on the `film` table to `trainee`.
7. Log in again as `trainee` and retrieve the first 10 film records.
8. Verify the current database user and explain the difference between database connection permission and table access permission.

