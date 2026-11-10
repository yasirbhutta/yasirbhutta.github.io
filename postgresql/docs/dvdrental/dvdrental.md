---
layout: page
title: Introduction to the DVD Rental Database
description: Learn about the PostgreSQL DVD Rental sample database, its tables, relationships, installation, restoration, and basic SQL queries using pgAdmin 4.
keywords: PostgreSQL, dvdrental database, PostgreSQL sample database, pgAdmin 4, SQL practice, database tables, SQL queries
---

# Introduction to the DVD Rental Database

## 1. What Is the DVD Rental Database?

The **DVD Rental database (`dvdrental`)** is a sample database provided for learning and practising PostgreSQL.

It represents a DVD rental business where customers can rent movies from different stores.

The database contains realistic business information, including:

- Movies and their categories.
- Actors and their movies.
- Customers and their contact information.
- Store locations and employees.
- DVD inventory.
- Movie rental transactions.
- Customer payments.

The `dvdrental` database contains **15 main tables** in the `public` schema.

It is particularly useful for students who want to learn SQL using realistic business data instead of creating small sample tables themselves.

## 2. Understanding the DVD Rental Business

Before working with SQL queries, let's understand how the DVD rental business works.

Imagine a company that operates several DVD rental stores.

1. The company maintains a collection of movies.
2. Each movie may have several physical DVD copies.
3. Customers visit a store and rent available DVDs.
4. Employees manage customer rentals.
5. Customers pay rental charges.
6. When customers return DVDs, the rental transaction is updated.

The database stores information about all these activities.

**Example:**

A customer named John rents the movie *Academy Dinosaur* from a store.

The database can maintain:

- The movie information in the `film` table.
- The physical DVD copy in the `inventory` table.
- The customer information in the `customer` table.
- The rental transaction in the `rental` table.
- The payment information in the `payment` table.

This business scenario helps students understand why databases contain multiple related tables.

## 3. Overview of the DVD Rental Tables

The database contains 15 main tables. Each table stores information about a particular part of the business.

### 3.1 Film and Actor Information

| Table | Purpose |
|---|---|
| `film` | Stores movie titles, descriptions, release years, rental rates, and other movie details. |
| `actor` | Stores the first and last names of actors. |
| `film_actor` | Connects movies with their actors. |
| `category` | Stores movie categories such as Action, Comedy, and Horror. |
| `film_category` | Connects movies with their categories. |
| `language` | Stores the languages associated with movies. |

### 3.2 Inventory and Store Operations

| Table | Purpose |
|---|---|
| `inventory` | Stores information about individual DVD copies available in stores. |
| `store` | Stores information about DVD rental stores. |
| `staff` | Stores employee information. |

### 3.3 Customer and Rental Activities

| Table | Purpose |
|---|---|
| `customer` | Stores customer names, email addresses, and account information. |
| `rental` | Stores DVD rental transactions, including rental and return dates. |
| `payment` | Stores customer payment transactions. |

### 3.4 Geographical Information

| Table | Purpose |
|---|---|
| `address` | Stores street addresses and postal information. |
| `city` | Stores city names. |
| `country` | Stores country names. |

**Total: 15 main tables**

## 4. Downloading the DVD Rental Database

Before practising SQL queries, students need to download and install the sample database.

The database is available in a compressed ZIP file containing a PostgreSQL backup file.

**Download the database:**

[Download DVD Rental Sample Database](https://neon.com/postgresqltutorial/dvdrental.zip)

**Alternative source:**

[DVD Rental PostgreSQL Project on GitHub](https://github.com/gordonkwokkwok/DVD-Rental-PostgreSQL-Project)

### 4.1 Extract the Downloaded File

1. Download `dvdrental.zip`.
2. Right-click the downloaded ZIP file.
3. Select **Extract All**.
4. Open the extracted folder.
5. Locate the `dvdrental.tar` backup file.

The `.tar` file contains the database backup that we will restore in PostgreSQL.

## 5. Creating the DVD Rental Database

Before restoring the backup, we need to create an empty database.

### Using pgAdmin 4

1. Open **pgAdmin 4**.
2. Connect to your PostgreSQL server.
3. Right-click **Databases**.
4. Select **Create → Database**.
5. Enter the database name:

```text
dvdrental
```

6. Click **Save**.

A new empty database named `dvdrental` will be created.

## 6. Restoring the Database Using pgAdmin 4

Now we will restore the downloaded backup file into the newly created database.

### Step 1: Open the Restore Tool

1. Expand the **Databases** section.
2. Right-click the `dvdrental` database.
3. Select **Restore**.

### Step 2: Select the Backup File

A Restore dialog box will appear.

Configure the following settings:

| Setting | Value |
|---|---|
| Format | Custom or tar |
| Filename | Select `dvdrental.tar` |
| Role name | `postgres` (or an appropriate database role) |

Use the folder icon to browse and select the downloaded backup file.

If the file is not visible, change the file type filter to **All Files**.

### Step 3: Configure Restore Options

Open the Restore options section.

Ensure the following backup sections are enabled:

| Option | Setting |
|---|---|
| Pre-data | Yes |
| Data | Yes |
| Post-data | Yes |
| Do not save owner | Yes (recommended when restoring under a different database user) |

### Step 4: Restore the Database

1. Review the selected settings.
2. Click **Restore**.
3. Wait for the restoration process to finish.
4. Check the process status.
5. Refresh the `dvdrental` database in the pgAdmin browser tree.

After successful restoration, the database tables will be available.

### Troubleshooting: pg_restore Binary Path Error

Sometimes pgAdmin displays an error indicating that it cannot find the `pg_restore` utility.

To resolve this issue:

1. Open **File → Preferences**.
2. Navigate to **Paths → Binary paths**.
3. Locate the PostgreSQL binary path setting.
4. Enter the path to your PostgreSQL `bin` directory.

Example:

```text
C:\Program Files\PostgreSQL\16\bin
```

Replace `16` with your installed PostgreSQL version.

5. Save the settings.
6. Try restoring the database again.

## 7. Exploring the DVD Rental Database in pgAdmin 4

After restoring the database, let's explore its structure.

Follow these steps:

1. Open pgAdmin 4.
2. Connect to your PostgreSQL server.
3. Expand **Databases**.
4. Expand the `dvdrental` database.
5. Expand **Schemas**.
6. Expand the `public` schema.
7. Expand **Tables**.

You will see the available database tables.

The `public` schema contains the 15 main tables used in our exercises.

## 8. Viewing Available Tables Using SQL

We can also retrieve the names of all tables using an SQL query.

**Example: Display all tables in the public schema**

```sql
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'
  AND table_type = 'BASE TABLE'
ORDER BY table_name;
```

**Understanding the Query:**

- `SELECT table_name`: Displays table names.
- `FROM information_schema.tables`: Retrieves information about database tables.
- `WHERE table_schema = 'public'`: Selects tables from the public schema.
- `table_type = 'BASE TABLE'`: Includes actual tables, not views.
- `ORDER BY table_name`: Sorts the table names alphabetically.

**Expected Result:** A list of the 15 main tables.

## 9. Viewing Film Records

Now let's execute our first queries using the `film` table.

### Example 1: Display All Film Records

```sql
SELECT *
FROM public.film;
```

The `*` symbol means that we want to retrieve all columns.

### Example 2: Display Only Film Titles

```sql
SELECT title
FROM public.film;
```

This query displays only the `title` column.

### Example 3: Display the First 10 Films

```sql
SELECT *
FROM public.film
LIMIT 10;
```

The `LIMIT 10` clause restricts the result to the first 10 records returned by the query.

## 10. Viewing Customer Records

The `customer` table stores information about customers registered with the DVD rental business.

### Example 1: Display All Customers

```sql
SELECT *
FROM public.customer;
```

### Example 2: Display Customer Names and Email Addresses

```sql
SELECT
    first_name,
    last_name,
    email
FROM public.customer;
```

This query retrieves only the first name, last name, and email address of each customer.

### Example 3: Display the First 10 Customers

```sql
SELECT *
FROM public.customer
LIMIT 10;
```

## 11. Understanding Table Relationships

The DVD Rental database contains relationships between different tables.

These relationships allow us to retrieve related information from multiple tables.

Let's understand a few examples.

### 11.1 Customer and Rental

One customer can rent multiple DVDs.

- `customer` stores customer information.
- `rental` stores rental transactions.
- The `customer_id` column connects these tables.

**Relationship:** One-to-Many.

### 11.2 Film and Inventory

One film can have multiple physical DVD copies.

- `film` stores movie information.
- `inventory` stores individual DVD copies.
- The `film_id` column connects these tables.

**Relationship:** One-to-Many.

### 11.3 Rental and Payment

A rental transaction can be associated with payment records.

- `rental` stores rental information.
- `payment` stores payment information.
- The `rental_id` column connects these tables.

### 11.4 Film and Actor

One film can have multiple actors, and one actor can appear in multiple films.

The `film_actor` table connects the `film` and `actor` tables.

**Relationship:** Many-to-Many.

We will study these relationships in detail when learning SQL JOIN operations.

## 12. Important Instructions

Before practising the SQL exercises, remember the following points:

1. The `dvdrental` database must be successfully restored before executing the queries.
2. The `dvdrental` database is separate from the default `postgres` database.
3. Must connect to `dvdrental` before running the queries.
4. The examples in this module use the `public` schema.
5. Always check the table and column names before writing SQL queries.

**Note:** In pgAdmin Query Tool, select the `dvdrental` database before executing the SQL examples.


## 15. See Also

- [PostgreSQL Sample Database – Neon](https://neon.com/postgresql/postgresql-getting-started/postgresql-sample-database)
- [PostgreSQL Official Documentation](https://www.postgresql.org/docs/)
