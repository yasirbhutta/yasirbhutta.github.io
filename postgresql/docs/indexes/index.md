# Indexes in PostgreSQL

## 1. Introduction

An Index is a database object that helps PostgreSQL find records more quickly.

When a table contains thousands or millions of records, searching every row can take time. An index helps PostgreSQL locate the required records without checking every row in the table.

Real-life example:

Imagine a textbook with 500 pages. You want to find a topic called "Database Indexing."

- Without an index, you may need to check every page.
- With an index, you can look up the topic in the book's index and go directly to the relevant page.

PostgreSQL indexes work in a similar way.

## 2. Why Do We Need Indexes?

Consider the `customer` table in the DVD Rental database.

Suppose we want to find a customer using their email address.

```
SELECT *
FROM customer
WHERE email = 'MARY.SMITH@EXAMPLE.COM';
```

Without a suitable index, PostgreSQL may need to scan the table to find the matching record.

An index on the `email` column can make this search faster.

## 3. Create an Index

Use the `CREATE INDEX` command to create an index.

Syntax:

```
CREATE INDEX index_name
ON table_name (column_name);
```

Example: Create an index on the `email` column of the `customer` table.

```
CREATE INDEX idx_customer_email
ON customer (email);
```

Explanation:

- `CREATE INDEX`: Creates a new index.
- `idx_customer_email`: Name of the index.
- `ON customer`: Specifies the table.
- `(email)`: Specifies the column to be indexed.

## 4. Search Using an Indexed Column

After creating the index, execute the following query:

```
SELECT *
FROM customer
WHERE email = 'MARY.SMITH@EXAMPLE.COM';
```

PostgreSQL can use the index to locate the matching customer.

Important: Creating an index does not guarantee that PostgreSQL will use it for every query. The query planner chooses the execution method based on estimated cost, table size, and available statistics.

## 5. Create an Index on Multiple Columns

We can create an index using more than one column. This is called a Composite Index or Multicolumn Index.

Example: Create an index on `first_name` and `last_name`.

```
CREATE INDEX idx_customer_name
ON customer (first_name, last_name);
```

This index can help queries that filter using:

```
SELECT *
FROM customer
WHERE first_name = 'MARY';
```

It can also help queries that filter using both columns:

```
SELECT *
FROM customer
WHERE first_name = 'MARY'
AND last_name = 'SMITH';
```

However, it is generally most useful when queries use the first column (`first_name`) or both columns. It is not normally as useful for searching only by `last_name`.

## 6. Create a Unique Index

A Unique Index ensures that duplicate values are not allowed in the indexed column or combination of columns.

For example, email addresses should generally be unique for customers.

```
CREATE UNIQUE INDEX idx_customer_email_unique
ON customer (email);
```

If duplicate non-NULL email values exist, PostgreSQL will not create this index.

Note: PostgreSQL also allows multiple NULL values in a normal unique index by default.

### Difference Between Index and Unique Index

| Index                        | Unique Index                        |
| ---------------------------- | ----------------------------------- |
| Improves data retrieval      | Improves data retrieval             |
| Allows duplicate values      | Prevents duplicate indexed values   |
| Created using `CREATE INDEX` | Created using `CREATE UNIQUE INDEX` |

## 7. Create an Index for Sorting

Indexes can also help with queries that sort records.

For example:

```
CREATE INDEX idx_film_title
ON film (title);
```

Now execute:

```
SELECT *
FROM film
ORDER BY title;
```

PostgreSQL may use the index to retrieve records in the required order.

## 8. Types of Indexes in PostgreSQL

PostgreSQL supports several index types.

| Index Type | Common Purpose                               |
| ---------- | -------------------------------------------- |
| B-tree     | Equality and range searches                  |
| Hash       | Equality searches                            |
| GIN        | Searching composite values, arrays and JSONB |
| GiST       | Geometric, range and specialized searches    |
| BRIN       | Large tables with naturally ordered data     |
| SP-GiST    | Specialized partitioned search structures    |

B-tree is the default index type and is suitable for most ordinary database searches.

### Example: Create a B-tree Index

```
CREATE INDEX idx_payment_amount
ON payment USING BTREE (amount);
```

The following command also creates a B-tree index because it is the default:

```
CREATE INDEX idx_payment_amount
ON payment (amount);
```

## 9. Understand Index Performance Using EXPLAIN

PostgreSQL provides the `EXPLAIN` command to show how a query is planned and executed.

For example:

```
EXPLAIN
SELECT *
FROM customer
WHERE email = 'MARY.SMITH@EXAMPLE.COM';
```

The output may contain:

- `Seq Scan`: Sequential Scan, which checks rows in the table.
- `Index Scan`: Uses an index to retrieve matching rows.
- `Bitmap Index Scan`: Uses an index to identify matching rows before retrieving them.

To execute the query and see actual execution time and row counts, use:

```
EXPLAIN ANALYZE
SELECT *
FROM customer
WHERE email = 'MARY.SMITH@EXAMPLE.COM';
```

Important: `EXPLAIN ANALYZE` actually executes the query. It is useful for understanding query performance.

## 10. List Indexes on a Table

Use the following command in the PostgreSQL `psql` terminal:

```
\d customer
```

It displays table information, including indexes.

You can also query PostgreSQL's system catalog:

```
SELECT
    indexname,
    indexdef
FROM pg_indexes
WHERE tablename = 'customer';
```

## 11. Delete an Index

Use `DROP INDEX` to delete an index.

Syntax:

```
DROP INDEX index_name;
```

Example:

```
DROP INDEX idx_customer_name;
```

To avoid an error if the index does not exist:

```
DROP INDEX IF EXISTS idx_customer_name;
```

## 12. Advantages of Indexes

1. Improve data retrieval speed.
2. Help search records efficiently.
3. Can improve sorting and filtering operations.
4. Support unique constraints.
5. Can improve performance of certain joins.
6. Help PostgreSQL execute complex queries efficiently.

## 13. Disadvantages of Indexes

Indexes also have some disadvantages:

1. They require additional disk storage.
2. They can slow down INSERT operations.
3. They can slow down UPDATE operations when indexed columns change.
4. They can slow down DELETE operations because indexes also need maintenance.
5. Too many unnecessary indexes can reduce overall database performance.

Remember: Create indexes on columns that are frequently used in search conditions, joins, sorting, and other performance-sensitive queries. Do not create indexes on every column.

## 14. Practical Exercises

Use the PostgreSQL DVD Rental database (`dvdrental`) to complete these exercises.

Exercise 1: Create an index on the `customer.email` column.

Exercise 2: Create an index on the `film.title` column.

Exercise 3: Create a composite index on `customer.first_name` and `customer.last_name`.

Exercise 4: Create a unique index on the `customer.email` column.

Exercise 5: Create an index on the `payment.amount` column.

Exercise 6: Use `EXPLAIN` to examine a query that searches for a customer by email.

Exercise 7: Use `EXPLAIN ANALYZE` to examine a query that searches for films by title.

Exercise 8: Display all indexes created on the `customer` table.

Exercise 9: Delete the index created on `film.title`.

Exercise 10: Compare query execution plans before and after creating an index on a suitable column.

## 15. Review Questions

1. What is an index in PostgreSQL?
2. Why do we create indexes?
3. What is the difference between an ordinary index and a unique index?
4. What is a composite index?
5. Which index type is the default in PostgreSQL?
6. What is the purpose of the `EXPLAIN` command?
7. What is the difference between `EXPLAIN` and `EXPLAIN ANALYZE`?
8. What is a Sequential Scan?
9. What are the disadvantages of creating too many indexes?
10. Which command is used to delete an index?

## 16. Quick Revision

| Task                    | SQL Command                     |
| ----------------------- | ------------------------------- |
| Create index            | `CREATE INDEX`                  |
| Create unique index     | `CREATE UNIQUE INDEX`           |
| Create B-tree index     | `CREATE INDEX ... USING BTREE`  |
| Create composite index  | `CREATE INDEX ... (col1, col2)` |
| Examine query plan      | `EXPLAIN`                       |
| Analyze query execution | `EXPLAIN ANALYZE`               |
| List indexes            | Query `pg_indexes`              |
| Delete index            | `DROP INDEX`                    |

Next lesson: PostgreSQL Sequences

We will learn how to create sequences, generate automatic numeric values, use `NEXTVAL` and `CURRVAL`, and understand how sequences are used with `SERIAL` and identity columns.