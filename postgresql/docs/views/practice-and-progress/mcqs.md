---
title: "MCQs: Views and Materialized Views in PostgreSQL"
description: "Test your PostgreSQL knowledge with multiple-choice questions on views, materialized views, SQL commands, refreshing, and catalog queries."
keywords: PostgreSQL MCQs, PostgreSQL views quiz, materialized views quiz, SQL multiple-choice questions, CREATE VIEW, CREATE MATERIALIZED VIEW, refresh materialized view, PostgreSQL practice questions, database administration
---

## Section 1: Views in PostgreSQL

### 1. What is a View in PostgreSQL?

A. A physical copy of a table  
B. A virtual table based on an SQL query  
C. A database backup  
D. A database index  

### 2. Which SQL command is used to create a View?

A. `MAKE VIEW`  
B. `ADD VIEW`  
C. `CREATE VIEW`  
D. `NEW VIEW`

### 3. Which SQL statement retrieves records from a View?

A. `GET VIEW`  
B. `SELECT`  
C. `SHOW VIEW`  
D. `FETCH VIEW`

### 4. Does a regular View normally store the result data physically?

A. Yes, always  
B. No, it stores the query definition  
C. It stores a backup  
D. It stores indexes only

### 5. Which command removes a View?

A. `DELETE VIEW`  
B. `REMOVE VIEW`  
C. `DROP VIEW`  
D. `TRUNCATE VIEW`

### 6. Which command changes the definition of an existing View?

A. `UPDATE VIEW`  
B. `CREATE OR REPLACE VIEW`  
C. `ALTER TABLE`  
D. `MODIFY VIEW`

### 7. Which SQL command renames a View in PostgreSQL?

A. `ALTER VIEW`  
B. `UPDATE VIEW`  
C. `RENAME TABLE`  
D. `CHANGE VIEW`

### 8. Can a View be created using a JOIN operation?

A. Yes  
B. No  
C. Only with INNER JOIN  
D. Only with LEFT JOIN

### 9. Which system catalog view provides information about regular Views?

A. `pg_views`  
B. `pg_tables`  
C. `pg_indexes`  
D. `pg_matviews`

### 10. What happens when underlying table data changes?

A. The regular View reflects the changes when queried  
B. The View must always be recreated  
C. The View is automatically deleted  
D. The database must be restarted

## Section 2: Materialized Views in PostgreSQL

### 11. What is a Materialized View?

A. A virtual table only  
B. A stored result of an SQL query  
C. A database user  
D. A database trigger

### 12. Which SQL command creates a Materialized View?

A. `CREATE VIEW`  
B. `CREATE TABLE`  
C. `CREATE MATERIALIZED VIEW`  
D. `MAKE MATERIALIZED VIEW`

### 13. Which command updates the stored data of a Materialized View?

A. `UPDATE MATERIALIZED VIEW`  
B. `REFRESH MATERIALIZED VIEW`  
C. `ALTER MATERIALIZED VIEW`  
D. `RELOAD VIEW`

### 14. Does a Materialized View automatically reflect changes in its underlying tables?

A. Yes, immediately  
B. No, it requires refreshing  
C. Only after restarting PostgreSQL  
D. Only when an index exists

### 15. Which PostgreSQL system catalog view provides information about Materialized Views?

A. `pg_tables`  
B. `pg_indexes`  
C. `pg_matviews`  
D. `pg_database`

### 16. What does the `ispopulated` column in `pg_matviews` indicate?

A. Whether the Materialized View has an index  
B. Whether the Materialized View contains populated data  
C. Whether the View has an owner  
D. Whether the View has been renamed

### 17. Which option creates a Materialized View without initially storing its query results?

A. `WITH DATA`  
B. `WITH NO DATA`  
C. `WITHOUT INDEX`  
D. `NO REFRESH`

### 18. What must be done before querying a Materialized View created using `WITH NO DATA`?

A. Rename it  
B. Create a primary key  
C. Refresh it  
D. Drop it

### 19. Which command removes a Materialized View?

A. `DROP VIEW`  
B. `DROP MATERIALIZED VIEW`  
C. `DELETE MATERIALIZED VIEW`  
D. `TRUNCATE VIEW`

### 20. Can an index be created on a Materialized View?

A. Yes  
B. No  
C. Only a primary key  
D. Only a foreign key

## Section 3: SQL and Query Understanding

### 21. What does the following SQL statement do?

```sql
CREATE VIEW active_customers AS
SELECT *
FROM customer
WHERE active = true;
```

A. Creates a table named `active_customers`  
B. Creates a View containing active customers  
C. Deletes inactive customers  
D. Updates the customer table

### 22. What is the purpose of this SQL statement?

```sql
CREATE MATERIALIZED VIEW mv_payment_summary AS
SELECT
    customer_id,
    SUM(amount) AS total_payment
FROM payment
GROUP BY customer_id;
```

A. Creates a regular View  
B. Creates a stored summary of customer payments  
C. Deletes payment records  
D. Creates an index on payment

### 23. What is the result of executing the following command?

```sql
REFRESH MATERIALIZED VIEW mv_payment_summary;
```

A. Deletes the Materialized View  
B. Renames the Materialized View  
C. Recalculates and updates its stored results  
D. Creates a new table

### 24. Which query displays all Materialized View names?

A.

```sql
SELECT matviewname
FROM pg_matviews;
```

B.

```sql
SELECT viewname
FROM pg_views;
```

C.

```sql
SELECT tablename
FROM pg_tables;
```

D.

```sql
SELECT indexname
FROM pg_indexes;
```

### 25. Which SQL statement renames a Materialized View?

A.

```sql
ALTER MATERIALIZED VIEW mv_old
RENAME TO mv_new;
```

B.

```sql
UPDATE MATERIALIZED VIEW mv_old;
```

C.

```sql
RENAME VIEW mv_old TO mv_new;
```

D.

```sql
CHANGE MATERIALIZED VIEW mv_old TO mv_new;
```

### 26. What is the default behavior when creating a Materialized View without specifying `WITH DATA` or `WITH NO DATA`?

A. It is created without data  
B. It is created and populated with data  
C. It is created as a regular View  
D. It generates an error

### 27. What is a major advantage of a Materialized View?

A. It always contains the latest data automatically  
B. It can provide faster access to previously computed results  
C. It eliminates the need for database tables  
D. It prevents all data duplication

### 28. Which command allows a Materialized View to be refreshed while allowing concurrent reads?

A. `REFRESH MATERIALIZED VIEW CONCURRENTLY`  
B. `UPDATE MATERIALIZED VIEW CONCURRENTLY`  
C. `ALTER MATERIALIZED VIEW CONCURRENTLY`  
D. `CREATE MATERIALIZED VIEW CONCURRENTLY`

### 29. What is required for REFRESH MATERIALIZED VIEW CONCURRENTLY?

A. A foreign key
B. A qualifying unique index covering all rows
C. A trigger
D. A primary key on every source table

### 30. Which statement correctly compares a regular View and a Materialized View?

A. Both always store query results physically  
B. A regular View stores query results, while a Materialized View does not  
C. A regular View stores a query definition, while a Materialized View stores query results  
D. Both require manual refresh after data changes
