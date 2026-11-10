---
title: "Practice Exercises: Views and Materialized Views in PostgreSQL"
description: "Practice PostgreSQL Views and Materialized Views through beginner, intermediate, and advanced SQL exercises using a students table and the DVD Rental database."
keywords: PostgreSQL practice exercises, PostgreSQL views, materialized views, CREATE VIEW, CREATE MATERIALIZED VIEW, REFRESH MATERIALIZED VIEW, SQL exercises, database administration
---

## Section 1: Views Using the Students Table

Complete the following exercises using PostgreSQL.

### Step 1: Create the Students Table

First, create a table named `students` with the following columns:

| Column | Data Type | Description |
|---|---|---|
| student_id | SERIAL | Unique student ID |
| student_name | VARCHAR(100) | Student's full name |
| department | VARCHAR(100) | Department name |
| marks | NUMERIC(5,2) | Student marks |
| semester | INTEGER | Current semester |

**Execute the following SQL query:**

```sql
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    department VARCHAR(100),
    marks NUMERIC(5,2),
    semester INTEGER
);
```

### Step 2: Insert Sample Records

Insert the following records into the `students` table:

```sql
INSERT INTO students
    (student_name, department, marks, semester)
VALUES
    ('Ali Khan', 'Computer Science', 85, 1),
    ('Sara Ahmed', 'Computer Science', 92, 2),
    ('Usman Malik', 'Information Technology', 68, 1),
    ('Ayesha Noor', 'Software Engineering', 78, 3),
    ('Hassan Raza', 'Computer Science', 45, 2),
    ('Fatima Zahra', 'Information Technology', 88, 4),
    ('Bilal Ahmad', 'Software Engineering', 55, 1),
    ('Zainab Ali', 'Computer Science', 95, 4),
    ('Hamza Tariq', 'Information Technology', 42, 2),
    ('Mariam Iqbal', 'Software Engineering', 81, 3);
```

Verify the inserted records:

```sql
SELECT * FROM students;
```

### Beginner Level

1. Create a View named `all_students` that displays all columns from the `students` table.
2. Create a View named `student_names` that displays only `student_id` and `student_name`.
3. Retrieve all records from the `student_names` View.
4. Create a View named `cs_students` that displays only students from the Computer Science department.
5. Retrieve all records from the `cs_students` View.
6. Create a View named `passed_students` that displays students who have obtained 50 or more marks.

### Intermediate Level

7. Create a View named `high_performers` that displays students who have obtained 80 or more marks.
8. Create a View named `student_results` that displays student names, departments, and marks.
9. Retrieve records from the `student_results` View in descending order of marks.
10. Create a View named `department_average` that displays each department and its average student marks.
11. Retrieve students from the `all_students` View who belong to the Information Technology department.
12. Create a View that displays the total number of students in each department.

### Advanced Level

13. Create a View named `semester_students` that displays student names, departments, and semesters.
14. Replace the existing `student_names` View and include the `semester` column.
15. Rename the `student_names` View to `student_basic_info` using `ALTER VIEW`.
16. Create an updatable View named `cs_student_records` that displays student records from the Computer Science department.
17. Use the `cs_student_records` View to update a student's department or marks. Verify the change in the original `students` table.
18. Create a Materialized View named `mv_department_average` that calculates average marks for each department.
19. Insert a new student into the original `students` table. Check whether the Materialized View automatically reflects the new record.
20. Refresh the `mv_department_average` Materialized View and verify the updated results.
21. Drop the `student_basic_info` View without deleting the original `students` table.
22. Drop the `mv_department_average` Materialized View.

---

## Section 2: Materialized Views Using the DVD Rental Database

Use the PostgreSQL `dvdrental` sample database to complete the following exercises.

### Beginner Level

1. Create a Materialized View named `mv_customer_payment_summary` that displays each customer's ID and total payment amount.
2. Create a Materialized View named `mv_customer_rental_count` that displays each customer's ID and total number of rentals.
3. Create a Materialized View named `mv_category_film_count` that displays each film category and the total number of films in that category.
4. Retrieve all records from each Materialized View.
5. Use `pg_matviews` to display the names of all Materialized Views in the current database.

### Intermediate Level

6. Create a Materialized View named `mv_customer_details` that displays customer ID, first name, last name, and email.
7. Create a Materialized View showing the total payment amount for each customer, including their first and last names.
8. Create a Materialized View showing the number of rentals made by each customer, along with their names.
9. Create a Materialized View showing the average rental rate for each film category.
10. Create an index on the `customer_id` column of `mv_customer_payment_summary`.
11. Insert a new payment record into the `payment` table and check whether `mv_customer_payment_summary` automatically reflects the change.
12. Refresh `mv_customer_payment_summary` and verify whether the new payment is included.

### Advanced Level

13. Create a Materialized View using `WITH NO DATA`.
14. Check the `ispopulated` column in `pg_matviews` for the Materialized View created in the previous exercise.
15. Try to retrieve records from the unpopulated Materialized View. Observe the result.
16. Refresh the Materialized View and retrieve its records.
17. Create a unique index on `mv_customer_payment_summary` using the `customer_id` column.
18. Execute `REFRESH MATERIALIZED VIEW CONCURRENTLY` on `mv_customer_payment_summary`.
19. Rename a Materialized View using `ALTER MATERIALIZED VIEW`.
20. Drop a Materialized View using `DROP MATERIALIZED VIEW`.

---

## Additional Challenge Tasks

Complete these tasks independently to strengthen your understanding.

1. Create a regular View that combines data from two or more tables in the DVD Rental database.
2. Create a Materialized View that summarizes rental information by customer and month.
3. Compare the behavior of a regular View and a Materialized View after inserting a new record into an underlying table.
4. Create indexes on a Materialized View and investigate their effect on query performance using `EXPLAIN ANALYZE`.
5. Write SQL queries to list all regular Views and Materialized Views in the current database.

