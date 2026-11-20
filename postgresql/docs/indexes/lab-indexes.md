# PostgreSQL Lab: Indexes and Query Performance

## Lab Overview

In this lab, students will learn how PostgreSQL indexes help retrieve data efficiently. They will create different types of indexes, examine query execution plans, compare query performance, and identify situations where indexes are useful.

**Database:** DVD Rental  
**DBMS:** PostgreSQL  
**Level:** Beginner to Intermediate

## Learning Objectives

After completing this lab, students should be able to:

1. Explain the purpose of an index in a database.
2. Understand how indexes improve data retrieval.
3. Create and remove indexes.
4. Create single-column and composite indexes.
5. Create unique, partial, and expression indexes.
6. Understand the difference between Sequential Scan and Index Scan.
7. Use `EXPLAIN` and `EXPLAIN ANALYZE`.
8. Evaluate the impact of indexes on query performance.

## Part A: Understanding Indexes

### Task 1: Understand the Purpose of an Index

Consider a book containing hundreds of pages. If you want to find a particular topic, you can:

- Read every page one by one.
- Use the index at the end of the book to locate the topic.

A database index works in a similar way. It helps PostgreSQL locate records without necessarily checking every row in a table.

**Important points:**

- An index can improve data retrieval.
- An index requires additional storage.
- Indexes can make INSERT, UPDATE, and DELETE operations slower because PostgreSQL must maintain the indexes.
- An index does not guarantee that every query will run faster.
- PostgreSQL automatically creates indexes for PRIMARY KEY and UNIQUE constraints.

### Task 2: Explore Existing Indexes

Use the following query to view indexes in the current database:

```sql
SELECT
    tablename,
    indexname,
    indexdef
FROM pg_indexes
WHERE schemaname = 'public'
ORDER BY tablename, indexname;
```

**Student Activity:**

1. Execute the query.
2. Identify the tables having indexes.
3. Find the primary key indexes.
4. Identify indexes created on foreign key columns.
5. Observe the columns included in each index.

## Part B: Creating and Managing Indexes

### Task 3: Create a Single-Column Index

Create an index on the `amount` column of the `payment` table.

```sql
CREATE INDEX idx_payment_amount
ON payment (amount);
```

Retrieve payment records using the indexed column:

```sql
SELECT *
FROM payment
WHERE amount = 5.99;
```

**Student Activity:**

1. Create the index.
2. Execute the SELECT query.
3. Identify the purpose of the index.
4. Verify that the index exists.

### Task 4: Create an Index on a Date Column

Create an index on the `payment_date` column.

```sql
CREATE INDEX idx_payment_date
ON payment (payment_date);
```

Retrieve payments made after a particular date:

```sql
SELECT *
FROM payment
WHERE payment_date >= TIMESTAMP '2007-02-01 00:00:00';
```

**Student Activity:**

Modify the query to retrieve payments made within a date range.

### Task 5: Create a Composite Index

A composite index is created using two or more columns.

Create an index on `customer_id` and `payment_date`.

```sql
CREATE INDEX idx_payment_customer_date
ON payment (customer_id, payment_date);
```

Execute the following query:

```sql
SELECT *
FROM payment
WHERE customer_id = 1
AND payment_date >= TIMESTAMP '2007-02-01 00:00:00';
```

**Student Activity:**

1. Identify the columns included in the index.
2. Execute the query.
3. Modify the query to filter only by `customer_id`.
4. Try filtering only by `payment_date`.
5. Observe how the order of columns in a composite index affects its usefulness.

### Task 6: Create a Unique Index

A unique index prevents duplicate values in the indexed column or combination of columns.

Create a unique index on the `email` column of the customer table:

```sql
CREATE UNIQUE INDEX idx_customer_email_unique
ON customer (email);
```

**Note:** This command will work only if the existing data contains no duplicate email values.

Check for duplicate email addresses:

```sql
SELECT
    email,
    COUNT(*) AS total
FROM customer
GROUP BY email
HAVING COUNT(*) > 1;
```

**Student Activity:**

1. Check for duplicate email addresses.
2. Create the unique index if the data permits it.
3. Understand why a unique index rejects duplicate values.

### Task 7: Create an Expression Index

An expression index is created using an expression or function rather than a simple column reference.

Create an index on lowercase customer email addresses:

```sql
CREATE INDEX idx_customer_lower_email
ON customer (LOWER(email));
```

Execute the following query:

```sql
SELECT *
FROM customer
WHERE LOWER(email) = LOWER('MARY.SMITH@EXAMPLE.COM');
```

**Student Activity:**

1. Create the expression index.
2. Execute the query.
3. Explain why the query uses the `LOWER()` function.

### Task 8: Create a Partial Index

A partial index contains entries for only those rows that satisfy a specified condition.

Create an index for active customers:

```sql
CREATE INDEX idx_customer_active
ON customer (customer_id)
WHERE active = true;
```

Execute the following query:

```sql
SELECT *
FROM customer
WHERE active = true;
```

**Student Activity:**

1. Create the partial index.
2. Explain why it contains only active customer records.
3. Modify the query to retrieve inactive customers.
4. Discuss when a partial index can be useful.

### Task 9: Create an Index Using IF NOT EXISTS

PostgreSQL supports `IF NOT EXISTS` to avoid an error when an index with the same name already exists.

```sql
CREATE INDEX IF NOT EXISTS idx_payment_amount
ON payment (amount);
```

**Student Activity:**

Execute the command more than once and observe the result.

### Task 10: Drop an Index

Use `DROP INDEX` to remove an index.

```sql
DROP INDEX idx_payment_amount;
```

To avoid an error if the index does not exist:

```sql
DROP INDEX IF EXISTS idx_payment_amount;
```

**Student Activity:**

1. Remove the index created in Task 3.
2. Verify that it has been removed.
3. Drop another practice index.

## Part C: Understanding Query Execution Plans

### Task 11: Use EXPLAIN

The `EXPLAIN` command displays the execution plan PostgreSQL intends to use for a query.

Execute:

```sql
EXPLAIN
SELECT *
FROM payment
WHERE amount = 5.99;
```

Observe the execution plan.

Important terms:

| Term | Meaning |
|---|---|
| Seq Scan | PostgreSQL checks rows sequentially. |
| Index Scan | PostgreSQL retrieves rows using an index. |
| Bitmap Index Scan | PostgreSQL uses an index to identify matching rows for a bitmap operation. |
| Bitmap Heap Scan | PostgreSQL retrieves the matching table rows using the bitmap. |
| Cost | Estimated cost of executing a plan. |
| Rows | Estimated number of rows returned. |

### Task 12: Use EXPLAIN ANALYZE

`EXPLAIN ANALYZE` executes the query and displays its actual execution statistics.

```sql
EXPLAIN ANALYZE
SELECT *
FROM payment
WHERE amount = 5.99;
```

Observe:

- Actual execution time
- Estimated rows
- Actual rows
- Scan method
- Planning time

**Important:** Unlike `EXPLAIN`, `EXPLAIN ANALYZE` actually executes the query. Use it carefully with INSERT, UPDATE, and DELETE statements.

### Task 13: Compare Execution Plans

First, examine the query plan:

```sql
EXPLAIN ANALYZE
SELECT *
FROM payment
WHERE amount = 5.99;
```

Create an index:

```sql
CREATE INDEX idx_payment_amount
ON payment (amount);
```

Execute the same query again:

```sql
EXPLAIN ANALYZE
SELECT *
FROM payment
WHERE amount = 5.99;
```

Compare the execution plans.

**Student Activity:**

Record the following observations:

| Observation | Before Index | After Index |
|---|---|---|
| Scan method | | |
| Estimated cost | | |
| Actual execution time | | |
| Actual rows | | |

**Important:** PostgreSQL may still choose a Sequential Scan when it estimates that scanning the table is cheaper. This is normal, especially for small tables or queries that return a large proportion of the rows. Creating an index does not guarantee that PostgreSQL will use it.

### Task 14: Update Table Statistics

PostgreSQL uses table statistics to estimate the cost of different execution plans.

Use `ANALYZE` to update statistics:

```sql
ANALYZE payment;
```

You can also analyze a specific table column:

```sql
ANALYZE payment (amount);
```

**Student Activity:**

1. Execute `ANALYZE payment`.
2. Run `EXPLAIN` again.
3. Observe whether the estimated plan changes.

## Part D: Independent Lab Exercises

Complete the following exercises independently.

### Exercise 1: Create an Index

Create an index named `idx_film_release_year` on the `release_year` column of the `film` table.

### Exercise 2: Search Using an Indexed Column

Retrieve all films released in 2006.

```sql
SELECT *
FROM film
WHERE release_year = 2006;
```

Use `EXPLAIN ANALYZE` to inspect the execution plan.

### Exercise 3: Create a Rental Date Index

Create an index on the `rental_date` column of the `rental` table.

Retrieve rentals made after a specified date.

### Exercise 4: Create a Composite Index

Create a composite index on the following columns of the `rental` table:

- `customer_id`
- `rental_date`

Write a query to retrieve a customer's rentals within a date range.

### Exercise 5: Create a Unique Index

Check whether the `customer` table contains duplicate email addresses. If no duplicates exist, create a unique index on `email`.

### Exercise 6: Create an Expression Index

Create an index on the uppercase version of the customer's last name.

Write a query using the same expression.

### Exercise 7: Create a Partial Index

Create a partial index for films having a rental rate greater than 2.00.

Write a query to retrieve films that satisfy the condition.

### Exercise 8: Examine Existing Indexes

Display all indexes in the `public` schema.

Identify:

- Index names
- Table names
- Indexed columns
- Index definitions

### Exercise 9: Compare Query Plans

Select a suitable query from the `payment` table.

1. Execute `EXPLAIN ANALYZE`.
2. Create an appropriate index.
3. Execute the same query again.
4. Compare both execution plans.
5. Write your observations.

### Exercise 10: Remove Unnecessary Indexes

Drop the practice indexes created during this lab.

Use:

```sql
DROP INDEX IF EXISTS index_name;
```

Replace `index_name` with the actual index name.

## Part E: Combined Practical Challenges

### Challenge 1: Customer Payment Search

Create an appropriate index to support searching payments by customer and payment date.

Write a query to retrieve payments for a particular customer within a specified date range.

Use `EXPLAIN ANALYZE` to examine the execution plan.

### Challenge 2: Film Search

Create an appropriate index to support searching films by title.

Write a query to retrieve films with a specified title.

Compare the execution plan before and after creating the index.

### Challenge 3: Rental Performance

Create an appropriate index to support retrieving rental records for a particular customer.

Write a query to retrieve the customer's rental history.

Explain why the selected index may improve query performance.

### Challenge 4: Index Selection

Consider the following query:

```sql
SELECT *
FROM payment
WHERE customer_id = 1
AND amount > 5.00
ORDER BY payment_date DESC;
```

Determine which columns could be included in an index to support this query.

Create a suitable index and examine the execution plan.

Explain whether PostgreSQL uses the index.

## Part F: Submission Requirements

Students must submit:

1. SQL statements used to create indexes.
2. SQL statements used to remove indexes.
3. Screenshots of index definitions.
4. Execution plans generated using `EXPLAIN ANALYZE`.
5. Before-and-after comparison of query execution plans.
6. Written observations about query performance.
7. Answers to the review questions.

## Assessment Criteria

| Assessment Area | Marks |
|---|---:|
| Creating and managing indexes | 20 |
| Single-column and composite indexes | 15 |
| Unique, partial, and expression indexes | 15 |
| Using EXPLAIN and EXPLAIN ANALYZE | 20 |
| Query plan comparison | 15 |
| Independent exercises and challenges | 10 |
| Documentation and observations | 5 |
| **Total** | **100** |

## Review Questions

1. What is an index in PostgreSQL?
2. Why do databases use indexes?
3. What is the difference between a table and an index?
4. What is a B-tree index?
5. What is the difference between a single-column and composite index?
6. What is a unique index?
7. What is a partial index?
8. What is an expression index?
9. What is the purpose of `EXPLAIN`?
10. What is the difference between `EXPLAIN` and `EXPLAIN ANALYZE`?
11. What is a Sequential Scan?
12. What is an Index Scan?
13. Why might PostgreSQL choose a Sequential Scan even when an index exists?
14. How can indexes affect INSERT, UPDATE, and DELETE operations?
15. Why should database administrators avoid creating unnecessary indexes?

## Quick Revision

| Command | Purpose |
|---|---|
| `CREATE INDEX` | Creates an index. |
| `CREATE UNIQUE INDEX` | Creates an index that prevents duplicate indexed values. |
| `DROP INDEX` | Removes an index. |
| `EXPLAIN` | Displays the estimated execution plan. |
| `EXPLAIN ANALYZE` | Executes a query and displays actual execution statistics. |
| `ANALYZE` | Updates table statistics. |
| `pg_indexes` | Provides information about database indexes. |

