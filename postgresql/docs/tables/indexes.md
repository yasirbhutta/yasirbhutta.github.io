# Student Notes: Indexes in PostgreSQL

## 1. Introduction

Imagine a university has a database containing 50,000 student records.

You want to find a student named Ali.

Without an index, PostgreSQL may need to check records one by one until it finds the matching student.

This can take more time when a table contains a large number of records.

To make searching faster, databases use indexes.

Think of an index in a database like the index at the back of a textbook. Instead of reading every page to find a topic, you use the index to locate it quickly.

## 2. What is an Index in PostgreSQL?

An index is a database object that helps PostgreSQL find records more efficiently.

It stores information about selected table columns so PostgreSQL can locate matching rows without always scanning the entire table.

Example:

Suppose we frequently search for students using their student ID.

```
SELECT *
FROM students
WHERE student_id = 5;
```

We can create an index on the `student_id` column to help PostgreSQL perform this search efficiently.

## 3. Why Do We Use Indexes?

Indexes are useful for:

1. Faster searching: Find records more efficiently.
2. Faster filtering: Improve queries that use WHERE conditions.
3. Faster sorting: Help with certain ORDER BY operations.
4. Faster JOIN operations: Improve searches using related columns.
5. Uniqueness: Enforce unique values in selected columns.

Important: Indexes can improve query performance, but they also require storage space and can slow down INSERT, UPDATE, and DELETE operations because the indexes must be maintained.

## 4. Create a Sample Table

Let's create a table named `students`.

```
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    department VARCHAR(50),
    marks INT,
    city VARCHAR(50)
);
```

Insert sample records:

```
INSERT INTO students
    (student_id, student_name, department, marks, city)
VALUES
    (1, 'Ali', 'Computer Science', 85, 'Multan'),
    (2, 'Sara', 'Mathematics', 72, 'Lahore'),
    (3, 'Ahmed', 'Computer Science', 65, 'DG Khan'),
    (4, 'Usman', 'Physics', 45, 'Multan'),
    (5, 'Ayesha', 'Mathematics', 90, 'Karachi');
```

## 5. Creating an Index

We can create an index on a table column using `CREATE INDEX`.

Syntax:

```
CREATE INDEX index_name
ON table_name (column_name);
```

Example:

Create an index on the `student_name` column.

```
CREATE INDEX idx_student_name
ON students (student_name);
```

The index `idx_student_name` has been created.

Now PostgreSQL can use this index when it considers it beneficial for queries involving `student_name`.

## 6. Searching with an Indexed Column

Let's search for a student named Ali.

```
SELECT *
FROM students
WHERE student_name = 'Ali';
```

PostgreSQL may use the index on `student_name` to locate the record efficiently.

Important: Creating an index does not guarantee that PostgreSQL will use it for every query. PostgreSQL's query planner chooses the execution plan based on estimated cost.

For a small table, PostgreSQL may prefer a sequential scan.

## 7. Creating an Index on Multiple Columns

Sometimes we frequently search using more than one column.

For example, we want to find students by department and city.

We can create a composite index (also called a multicolumn index).

Syntax:

```
CREATE INDEX index_name
ON table_name (column1, column2);
```

Example:

```
CREATE INDEX idx_department_city
ON students (department, city);
```

Now consider this query:

```
SELECT *
FROM students
WHERE department = 'Computer Science'
AND city = 'Multan';
```

The composite index may help PostgreSQL execute this query more efficiently.

Important: The order of columns matters. An index on `(department, city)` is generally most useful for conditions involving `department` first, or both columns together.

## 8. Creating a UNIQUE Index

A unique index prevents duplicate values in the indexed column or combination of columns.

Syntax:

```
CREATE UNIQUE INDEX index_name
ON table_name (column_name);
```

Example:

Suppose we want every student email address to be unique.

First, add an email column:

```
ALTER TABLE students
ADD COLUMN email VARCHAR(100);
```

Create a unique index:

```
CREATE UNIQUE INDEX idx_student_email
ON students (email);
```

Now PostgreSQL will not allow duplicate non-NULL email addresses.

Note: A UNIQUE constraint is usually preferable when the main purpose is to enforce uniqueness.

```
ALTER TABLE students
ADD CONSTRAINT unique_student_email
UNIQUE (email);
```

PostgreSQL automatically creates a unique index to enforce this constraint.

## 9. Checking Existing Indexes

In pgAdmin, you can find indexes under:

`Database → Schemas → public → Tables → students → Indexes`

You can also use this SQL query to list indexes belonging to the `students` table:

```
SELECT
    indexname,
    indexdef
FROM pg_indexes
WHERE tablename = 'students';
```

This displays the index names and their definitions.

## 10. Deleting an Index

We can delete an index using `DROP INDEX`.

Syntax:

```
DROP INDEX index_name;
```

Example:

```
DROP INDEX idx_student_name;
```

To avoid an error if the index does not exist:

```
DROP INDEX IF EXISTS idx_student_name;
```

Important: Dropping an index does not delete the original table or its records.

However, do not directly drop an index that supports a PRIMARY KEY or UNIQUE constraint. Remove the corresponding constraint if that is what you intend.

## 11. Types of Indexes in PostgreSQL

PostgreSQL supports several index types.

| Index Type | Common Use                                        |
| ---------- | ------------------------------------------------- |
| B-tree     | Equality and range searches; default index type   |
| Hash       | Equality comparisons                              |
| GIN        | Searching within arrays, JSONB and full-text data |
| GiST       | Geometric and range-related searches              |
| BRIN       | Very large tables with naturally ordered data     |

For beginners, start with B-tree indexes because PostgreSQL uses B-tree as the default index type.

Example:

```
CREATE INDEX idx_student_marks
ON students USING BTREE (marks);
```

This is equivalent to:

```
CREATE INDEX idx_student_marks
ON students (marks);
```

## 12. Understanding Query Performance with EXPLAIN

PostgreSQL provides `EXPLAIN` to show how a query will be executed.

Syntax:

```
EXPLAIN
SELECT *
FROM students
WHERE student_name = 'Ali';
```

It displays the query execution plan.

To see actual execution statistics, use:

```
EXPLAIN ANALYZE
SELECT *
FROM students
WHERE student_name = 'Ali';
```

Understand the output:

You may see one of these scan methods:

- `Seq Scan`: PostgreSQL scans the table rows.
- `Index Scan`: PostgreSQL uses an index to find rows.
- `Bitmap Index Scan`: PostgreSQL uses an index to identify matching rows before accessing the table.

Because our sample table contains only five records, PostgreSQL may choose a sequential scan even when an index exists.

For meaningful performance testing, use a larger table.

## 13. Index vs Table Scan

| Index Scan                          | Sequential Scan                  |
| ----------------------------------- | -------------------------------- |
| Uses an index to locate records     | Reads table records sequentially |
| Often useful for selective searches | Often useful for small tables    |
| Requires an index                   | Does not require an index        |
| Index requires additional storage   | No separate index is needed      |

Remember: An index is not always faster. PostgreSQL chooses the method it estimates will be more efficient.

## 14. Common Mistakes

1. Creating too many indexes on a table.
2. Creating indexes on columns that are rarely searched.
3. Expecting every query to use an index.
4. Forgetting that indexes require additional storage.
5. Creating a composite index without considering column order.
6. Assuming an index automatically improves every INSERT, UPDATE, and DELETE operation.

## 15. Practice Exercises

Use the `students` table created in this lesson.

### Beginner Level

1. Create an index named `idx_student_name` on the `student_name` column.
2. Create an index on the `department` column.
3. Display all indexes belonging to the students table.
4. Delete the index on the department column.

### Intermediate Level

5. Create a composite index on `department` and `city`.
6. Write a SELECT query that searches students by department and city.
7. Add an email column and create a unique index on it.
8. Use EXPLAIN to examine a query that searches by student name.

### Advanced Level

9. Create a B-tree index on the marks column.
10. Compare the query plans before and after creating an index.
11. Create a table containing a large number of records and test index performance.
12. Explain why PostgreSQL might choose a sequential scan instead of an index scan.

## 16. Review Questions

1. What is an index in PostgreSQL?
2. Why do we create indexes?
3. What is the purpose of CREATE INDEX?
4. What is a composite index?
5. What is a UNIQUE index?
6. What is the default index type in PostgreSQL?
7. How can we delete an index?
8. Do indexes require additional storage?
9. Can indexes slow down INSERT and UPDATE operations?
10. What is the purpose of EXPLAIN ANALYZE?
11. What is the difference between Index Scan and Sequential Scan?
12. Does PostgreSQL always use an index when one exists?

## 17. Quick Revision

| Command                        | Purpose                                                   |
| ------------------------------ | --------------------------------------------------------- |
| `CREATE INDEX`                 | Creates an index                                          |
| `CREATE UNIQUE INDEX`          | Creates an index that prevents duplicate non-NULL values  |
| `CREATE INDEX ... USING BTREE` | Creates a B-tree index                                    |
| `DROP INDEX`                   | Deletes an index                                          |
| `EXPLAIN`                      | Displays the query execution plan                         |
| `EXPLAIN ANALYZE`              | Executes a query and displays actual execution statistics |

Remember: Indexes help PostgreSQL find data efficiently, especially when working with large tables. However, create indexes carefully because they also have storage and maintenance costs.

## Next Lesson

Transactions in PostgreSQL

You will learn how to use `BEGIN`, `COMMIT`, and `ROLLBACK` to manage database operations safely and maintain data consistency.