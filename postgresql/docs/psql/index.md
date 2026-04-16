---
layout: page
title: "How to Access and Use psql in Windows | PostgreSQL Command-Line Tool"
description: Complete guide to accessing and using psql in Windows. Learn multiple methods to open psql, configure PATH variables, fix 'psql not recognized' errors, and execute SQL commands from the terminal.
keywords: psql windows, PostgreSQL command line, how to use psql, psql not recognized windows, PostgreSQL CLI, psql installation windows, add PostgreSQL to PATH, running psql on Windows, postgresql terminal, psql command line tool
toc: toc/postgresql.html
topic: postgresql
breadcrumb: 
- title: PostgreSQL
  url: /postgresql/
---

## What is **psql** in PostgreSQL?

**`psql`** is the **interactive command-line tool** for working with PostgreSQL.

It allows you to:

* Execute SQL queries
* Manage databases and users
* Run scripts
* View/query data quickly from the terminal

Think of `psql` as a **terminal interface (client)** to communicate with the PostgreSQL server.

---

## Why do we use `psql`?

We use `psql` because it is:

* ⚡ **Fast** – no GUI needed
* 🧰 **Powerful** – supports SQL + special commands
* 🔧 **Administrative** – manage users, roles, databases
* 📜 **Scriptable** – automate tasks using `.sql` files

---

# 🪟 How to Access `psql` in Windows

## ✅ 1. Install PostgreSQL (if not installed)

Download from:

* [https://www.postgresql.org/download/windows/](https://www.postgresql.org/download/windows/)

During installation:

* Set **password for postgres user**
* Keep default port **5432**
* Make sure **Command Line Tools (psql)** is selected

---

## ⚙️ 2. Open psql in Windows

### Method 1: Using SQL Shell (psql) (Easiest)

1. Click **Start Menu**
2. Search:

   ```
   SQL Shell (psql)
   ```
3. Open it

You will see prompts like:

```
Server [localhost]:
Database [postgres]:
Port [5432]:
Username [postgres]:
Password:
```

👉 Press Enter for defaults and enter password.

---

### Method 2: Using Command Prompt (CMD)

#### Step 1: Open CMD

Press:

```
Win + R → type cmd → Enter
```

#### Step 2: Run psql

```bash
psql -U postgres
```

If it does not work, use full path:

```bash
"C:\Program Files\PostgreSQL\16\bin\psql.exe" -U postgres
```

(Version folder may be 15, 14, etc.)

---

### Method 3: Add psql to PATH (Recommended)

So you can run `psql` from anywhere:

#### Steps:

1. Copy this path:

```
C:\Program Files\PostgreSQL\16\bin
```

2. Go to:

```
Control Panel → System → Advanced System Settings → Environment Variables
```

3. Edit **Path**
4. Add new entry:

```
C:\Program Files\PostgreSQL\16\bin
```

for more details, see [Fix 'psql' is not recognized on Windows](fix-psql.md)

5. Restart CMD

Now just type:

```bash
psql -U postgres
```

---

## 🔐 3. Login Examples

### Login as postgres user:

```bash
psql -U postgres
```

### Login with database:

```bash
psql -U postgres -d university_db
```

### Login with host & port:

```bash
psql -U postgres -h localhost -p 5432
```

---

## 📂 4. Useful First Commands after login

```sql
\l        -- list databases
\c postgres   -- connect database
\dt       -- list tables
\du       -- list users
\q        -- quit
```

---

# ⚠️ Common Problems & Fixes

### ❌ “psql is not recognized”

✔ Fix: [Add PostgreSQL `bin` folder to PATH](fix-psql.md)

---

### ❌ Password error

✔ Fix:

* Check password used during installation
* Reset postgres password if needed

---

### ❌ Connection failed

✔ Fix:

* Ensure PostgreSQL service is running:

```
Services → PostgreSQL → Start
```

---

## How to Login into `psql`

### 1. Login with **postgres (default superuser)**

```bash
psql -U postgres
```

If PostgreSQL is running locally:

```bash
psql -U postgres -h localhost -p 5432
```

👉 You will be prompted for a password.

---

### 2. Login into a **specific database**

```bash
psql -U postgres -d mydatabase
```

---

### 3. Login with a **new user**

First create a user:

```sql
CREATE ROLE student_user WITH LOGIN PASSWORD '1234';
```

Then login:

```bash
psql -U student_user -d mydatabase
```

Or:

```bash
psql -U student_user -h localhost -d mydatabase
```

---

### 4. Login using **connection string**

```bash
psql "postgresql://student_user:1234@localhost:5432/mydatabase"
```

---

## 📘 `psql` Backslash Commands (Meta-Commands) with Examples

In **psql (PostgreSQL interactive terminal)**, backslash commands (`\`) are used to manage and explore databases.

👉 Key point:

* Executed by **psql client (not SQL server)**
* Start with `\`
* Very useful for learning and administration

---

# 🔍 1. Essential Discovery Commands (with Examples)

## 📌 `\l` → List all databases

```sql
\l
```

👉 Shows all databases on the PostgreSQL server

---

## 📌 `\dn` → List schemas

```sql
\dn
```

👉 Example output:

* public
* information_schema

---

## 📌 `\dt` → List tables

```sql
\dt
```

👉 Example:

```
List of relations
Schema | Name     | Type  | Owner
-------+----------+-------+-------
public | students | table | postgres
```

---

## 📌 `\di` → List indexes

```sql
\di
```

👉 Shows indexes created on tables

---

## 📌 `\dv` → List views

```sql
\dv
```

👉 Displays all views in current database

---

## 📌 `\df` → List functions

```sql
\df
```

👉 Shows stored functions

---

## 📌 `\du` → List users/roles

```sql
\du
```

👉 Example:

```
Role name | Attributes
----------+----------------
postgres  | Superuser
student   | Create DB
```

---

# 🧭 2. Navigation & Connection Commands

## 📌 `\c database_name` → Connect to database

```sql
\c university_db
```

👉 Output:

```
You are now connected to database "university_db"
```

---

## 📌 `\conninfo` → Show connection details

```sql
\conninfo
```

👉 Example:

```
You are connected to database "university_db" as user "postgres" on host "localhost" at port "5432"
```

---

## 📌 `\q` → Quit psql

```sql
\q
```

👉 Exits PostgreSQL terminal

---

# 📊 3. Inspecting Objects (Very Important for Students)

## 📌 `\d table_name` → Describe table

```sql
\d students
```

👉 Example output:

```
Column | Type         | Constraints
-------+-------------+-------------
id     | integer      | primary key
name   | varchar(50)  |
```

---

## 📌 `\d+ table_name` → Detailed table info

```sql
\d+ students
```

👉 Shows:

* Column details
* Indexes
* Table size
* Comments

---

# 🖥️ 4. System & Output Commands

## 📌 `\x` → Expanded view toggle

```sql
\x
SELECT * FROM students;
```

👉 Output becomes vertical (useful for many columns):

```
id   : 1
name : Ali
```

---

## 📌 `\timing` → Show query execution time

```sql
\timing
SELECT * FROM students;
```

👉 Output:

```
Time: 1.234 ms
```

---

## 📌 `\i filename.sql` → Run SQL file

```sql
\i school.sql
```

👉 Executes all SQL inside file:

```sql
CREATE TABLE students (...);
INSERT INTO students VALUES (...);
```

---

## 📌 `\! command` → Run OS command

```sql
\! ls
```

👉 Example output:

```
school.sql
data.sql
```

Other example:

```sql
\! pwd
```

---

# ❓ 5. Help Commands (Must Know)

## 📌 `\?` → All psql commands

```sql
\?
```

👉 Shows full list of meta-commands

---

## 📌 `\h` → SQL help

```sql
\h
```

---

## 📌 `\h command` → Specific SQL help

```sql
\h CREATE TABLE
```

👉 Shows syntax:

```
CREATE TABLE table_name (
    column_name data_type
);
```

---

# 🧪 Examples

```sql
\l                          -- list databases
\c university_db            -- connect database
\dn                         -- show schemas
\dt                         -- show tables

\d students                -- describe table
SELECT * FROM students;

\x                          -- expanded view
\timing                     -- enable timing

\! ls                       -- check files
\i insert_data.sql         -- run SQL file
```

---

# ⭐ Summary

✔ `\` commands = psql meta-commands
✔ Used for:

* Database navigation
* Table inspection
* System control
* Debugging & learning

---

