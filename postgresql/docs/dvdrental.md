---
layout: page
title: DBA Student Final Project Guidelines
description: Comprehensive guidelines for designing, implementing, optimizing, and documenting a database project. Ideal for final-year DBA students working with PostgreSQL or similar RDBMS.
keywords: DBA project guidelines, database design, ERD modeling, normalization, PostgreSQL, SQL procedures, triggers, database security, CRUD integration, Python database connectivity
toc: toc/postgresql.html
topic: postgresql
breadcrumb:
  - title: PostgreSQL
    url: /postgresql/
---

The **dvdrental** database is a popular sample dataset for PostgreSQL, designed to mimic the business processes of a 2000s-era DVD rental store. It is essentially the "PostgreSQL version" of the Sakila database originally created for MySQL.

It consists of **15 tables** that cover everything from inventory and film details to customer payments and store locations.

---

## 1. Core Schema Overview
The database is structured into a few logical groups that handle different aspects of the business.

### Film & Actor Data
* **`film`**: The central table containing titles, descriptions, release years, and rental rates.
* **`actor`**: Stores names of actors.
* **`film_actor`**: A bridge table for the many-to-many relationship between films and actors.
* **`category`** & **`film_category`**: Used to group movies (e.g., Action, Comedy, Horror).
* **`language`**: Stores the language of the film.

### Inventory & Store Operations
* **`inventory`**: Tracks individual physical copies of a movie. One `film` can have many `inventory` items across different stores.
* **`store`**: Contains store locations and connects to the manager (`staff`).
* **`staff`**: Information about the employees.

### Customer & Rental Activity
* **`customer`**: Stores user data, email, and whether they are active.
* **`rental`**: Records every time a customer takes a DVD. This table tracks `rental_date` and `return_date`.
* **`payment`**: Tracks the financial transactions tied to a rental.

### Geography
* **`address`**, **`city`**, **`country`**: A normalized hierarchy for storing locations of both stores and customers.

---

## 2. Why it is Great for Learning
If you are practicing stored procedures or complex queries, this database is ideal because it provides:
* **Realistic Relationships:** It uses foreign keys and bridge tables (like `film_actor`) to simulate real-world data complexity.
* **Varying Data Types:** Includes timestamps, decimals for money, and text for descriptions.
* **Transaction Scenarios:** As we saw in the `process_return` example, the link between `rental` and `payment` is perfect for practicing ACID properties and transaction management.

---

## 3. How to Load It

The database is usually provided as a `.tar` file. To get it into your local Postgres instance:

1.  **Download** the `dvdrental.zip` (standard on most tutorial sites).
   
- **NEON Download**: [Download DVD Rental Sample Database](https://neon.com/postgresqltutorial/dvdrental.zip)
- **Alternative (GitHub):** [Gordon Kwok's DVD-Rental Repo](https://github.com/gordonkwokkwok/DVD-Rental-PostgreSQL-Project)

2.  **Extract** it to get `dvdrental.tar`.
3.  **Create** a fresh database: `CREATE DATABASE dvdrental;`
4.  **Restore** it via command line:
    ```bash
    pg_restore -U postgres -d dvdrental C:\path\to\dvdrental.tar
    ```

(Note: Replace postgres with your username and provide the correct path to the file.)

5. **Verification**
To make sure everything loaded correctly, connect to the database and list the tables:

```SQL
\c dvdrental
\dt
```

You should see 15 tables, including actor, film, customer, and rental.

## Restoring the `dvdrental` database using the **pgAdmin 4** GUI

Restoring the `dvdrental` database using the **pgAdmin 4** GUI is a straightforward process. Since the download is a `.tar` file, you will use the built-in **Restore** tool.

Follow these steps to get the database up and running:

---

## 1. Create the Destination Database
Before you can restore the data, you need an empty "container" for it.

1.  Open **pgAdmin 4** and connect to your server.
2.  Right-click on **Databases** > **Create** > **Database...**
3.  Name the database `dvdrental`.
4.  Click **Save**.

---

## 2. Open the Restore Tool
1.  Right-click on your newly created `dvdrental` database in the browser tree.
2.  Select **Restore...** from the context menu.

---

## 3. Configure Restore Settings
A dialog box will appear. Fill in the following details:

* **Format:** Select **Directory** or **Custom or tar** (Since the file is `dvdrental.tar`, choose **Custom or tar**).
* **Filename:** Click the **folder icon** to browse your computer.
    * *Note:* In the file browser, make sure to change the file type filter to **All Files (*)** so you can see and select the `.tar` file.
* **Role name:** Usually set to `postgres` (or your specific superuser).

---

## 4. Set Restore Options (Important)
Click the **Restore options** tab at the top of the dialog. To ensure a clean import, toggle these to **Yes**:

* **Pre-data:** Yes
* **Data:** Yes
* **Post-data:** Yes
* **Do not save owner:** Yes (This is helpful if the file was created by a user with a different name than yours).

---

## 5. Execute and Verify
1.  Click the **Restore** button. 
2.  You will see a notification in the bottom right corner saying "Process started."
3.  Once it finishes (you'll see "Process completed"), right-click on the `dvdrental` database and select **Refresh**.
4.  Navigate to **Schemas** > **public** > **Tables**. You should now see all 15 tables.

---

### Troubleshooting Tip: "Binary Path" Error
If pgAdmin says it cannot find the `pg_restore` utility, you need to tell it where your PostgreSQL "bin" folder is:
1.  Go to **File** > **Preferences**.
2.  Navigate to **Paths** > **Binary paths**.
3.  Scroll down to **PostgreSQL Binary Path** and enter the path to your version (e.g., `C:\Program Files\PostgreSQL\16\bin`).
4.  Click **Save** and try the restore again.

## See Also

- [PostgreSQL Sample Database - neon.com](https://neon.com/postgresql/postgresql-getting-started/postgresql-sample-database)