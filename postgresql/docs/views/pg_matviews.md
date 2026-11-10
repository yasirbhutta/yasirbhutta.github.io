---
layout: page
title: "PostgreSQL pg_matviews: List Materialized Views"
description: Learn how to query PostgreSQL's pg_matviews system catalog to list materialized views and inspect their schemas, definitions, and population status.
keywords: PostgreSQL pg_matviews, list materialized views, PostgreSQL system catalog, materialized view definition, PostgreSQL schema, ispopulated, pg_matviews query, database administration, PostgreSQL tutorial
---

## What is `pg_matviews` in PostgreSQL?

`pg_matviews` is a system catalog view in PostgreSQL that provides information about Materialized Views available in the current database.

It helps database administrators and developers inspect existing Materialized Views, including their names, schemas, definitions, and whether they are populated.

### 1. Display all Materialized Views

```sql
SELECT *
FROM pg_matviews;
```

This query displays information about all Materialized Views in the current database.

### 2. Display selected information

```sql
SELECT
    schemaname,
    matviewname,
    matviewowner,
    ispopulated
FROM pg_matviews;
```

Explanation:

| Column         | Description                                            |
| -------------- | ------------------------------------------------------ |
| `schemaname`   | Schema containing the Materialized View.               |
| `matviewname`  | Name of the Materialized View.                         |
| `matviewowner` | Owner of the Materialized View.                        |
| `ispopulated`  | Indicates whether the Materialized View contains data. |
| `definition`   | SQL query used to define the Materialized View.        |

### 3. Find a specific Materialized View

For example, find a Materialized View named `mv_customer_payment_summary`:

```sql
SELECT *
FROM pg_matviews
WHERE matviewname = 'mv_customer_payment_summary';
```

### 4. Display Materialized View definitions

```sql
SELECT
    matviewname,
    definition
FROM pg_matviews;
```

This query displays the SQL definitions used to create Materialized Views.

### 5. Difference between `pg_views` and `pg_matviews`

| Feature                  | `pg_views`                      | `pg_matviews`                        |
| ------------------------ | ------------------------------- | ------------------------------------ |
| Purpose                  | Information about regular Views | Information about Materialized Views |
| Stores query definition  | Yes                             | Yes                                  |
| Stores query result data | No                              | Yes                                  |
| Requires refresh         | No                              | Yes, when source data changes        |
| System catalog view      | Yes                             | Yes                                  |

Important: `pg_matviews` does not store the actual Materialized View results. It provides metadata about Materialized Views. The actual stored results are available by querying the Materialized View itself.
