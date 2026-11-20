# Student Notes: GROUP BY Clause in PostgreSQL

## 1. Introduction

In a database, we often need to organize records into groups and calculate information for each group.

For example, a university may want to know:

- How many students belong to each city?
- What is the total fee collected from each city?
- What is the average age of students in each city?
- What is the highest fee paid by students in each city?

PostgreSQL provides the GROUP BY clause to group records based on one or more columns.

We commonly use `GROUP BY` with aggregate functions such as:

- `COUNT()`
- `SUM()`
- `AVG()`
- `MIN()`
- `MAX()`

## 2. What is GROUP BY?

`GROUP BY` is an SQL clause that groups rows having the same values in one or more columns.

Syntax:

```
SELECT column_name, aggregate_function(column_name)
FROM table_name
GROUP BY column_name;
```

Example:

Suppose we have five students from different cities. We want to count how many students belong to each city.

Instead of counting each city separately, we can use `GROUP BY`.

## 3. Create a Sample Table

Let's create a table named `students`.

```
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    student_name VARCHAR(100),
    age INTEGER,
    city VARCHAR(50),
    fee NUMERIC(10, 2)
);
```

Insert sample records:

```
INSERT INTO students
(student_id, student_name, age, city, fee)
VALUES
(1, 'Ali', 20, 'Multan', 15000),
(2, 'Ahmed', 22, 'DG Khan', 18000),
(3, 'Sara', 21, 'Multan', 20000),
(4, 'Ayesha', 23, 'Lahore', 17000),
(5, 'Usman', 20, 'Lahore', 16000),
(6, 'Hassan', 22, 'DG Khan', 19000),
(7, 'Fatima', 21, 'Multan', 18000);
```

View all records:

```
SELECT * FROM students;
```

## 4. Count Students City-Wise

We want to find the number of students from each city.

SQL Query:

```
SELECT city, COUNT(*) AS total_students
FROM students
GROUP BY city;
```

Output:

| city    | total_students |
| ------- | -------------- |
| DG Khan | 2              |
| Lahore  | 2              |
| Multan  | 3              |

Explanation:

1. `SELECT city` displays the city name.
2. `COUNT(*)` counts students.
3. `GROUP BY city` creates a separate group for each city.
4. Each group is counted separately.

## 5. Calculate Total Fee City-Wise

We want to calculate the total fee collected from students in each city.

SQL Query:

```
SELECT
    city,
    SUM(fee) AS total_fee
FROM students
GROUP BY city;
```

Output:

| city    | total_fee |
| ------- | --------- |
| DG Khan | 37000.00  |
| Lahore  | 33000.00  |
| Multan  | 53000.00  |

Explanation:

- `SUM(fee)` calculates the total fee.
- `GROUP BY city` calculates the total separately for each city.

## 6. Calculate Average Age City-Wise

We can calculate the average age of students in each city.

```
SELECT
    city,
    AVG(age) AS average_age
FROM students
GROUP BY city;
```

Output:

| city    | average_age |
| ------- | ----------- |
| DG Khan | 22.0        |
| Lahore  | 21.5        |
| Multan  | 20.67       |

The average is calculated separately for each city.

## 7. Find Minimum and Maximum Fee City-Wise

We can use `MIN()` and `MAX()` with `GROUP BY`.

Example 1: Minimum fee in each city

```
SELECT
    city,
    MIN(fee) AS minimum_fee
FROM students
GROUP BY city;
```

Example 2: Maximum fee in each city

```
SELECT
    city,
    MAX(fee) AS maximum_fee
FROM students
GROUP BY city;
```

These queries display the smallest and largest fee in each city.

## 8. Use Multiple Aggregate Functions with GROUP BY

We can use multiple aggregate functions in a single query.

Example: Display student statistics for each city

```
SELECT
    city,
    COUNT(*) AS total_students,
    SUM(fee) AS total_fee,
    AVG(fee) AS average_fee,
    MIN(fee) AS minimum_fee,
    MAX(fee) AS maximum_fee
FROM students
GROUP BY city;
```

This query displays:

- Total students in each city.
- Total fee collected from each city.
- Average fee in each city.
- Minimum fee in each city.
- Maximum fee in each city.

## 9. GROUP BY with WHERE

The `WHERE` clause filters records before they are grouped.

Example: Count students city-wise whose age is greater than 20.

```
SELECT
    city,
    COUNT(*) AS total_students
FROM students
WHERE age > 20
GROUP BY city;
```

Explanation:

1. `WHERE age > 20` selects students older than 20.
2. `GROUP BY city` groups the selected students by city.
3. `COUNT(*)` counts students in each group.

## 10. GROUP BY with Multiple Columns

We can group records using more than one column.

Example: Group students by city and age.

```
SELECT
    city,
    age,
    COUNT(*) AS total_students
FROM students
GROUP BY city, age;
```

In this query, students are grouped according to both their city and age.

For example, students from Multan who are 21 years old will belong to one group.

## 11. GROUP BY with ORDER BY

We can sort grouped results using `ORDER BY`.

Example: Display cities according to the highest number of students first.

```
SELECT
    city,
    COUNT(*) AS total_students
FROM students
GROUP BY city
ORDER BY total_students DESC;
```

Explanation:

- `GROUP BY city` groups students by city.
- `COUNT(*)` counts students in each city.
- `ORDER BY total_students DESC` displays the highest count first.

Use `ASC` for ascending order and `DESC` for descending order.

## 12. Difference Between WHERE and GROUP BY

| WHERE                         | GROUP BY                                   |
| ----------------------------- | ------------------------------------------ |
| Filters individual records.   | Groups records with common values.         |
| Works before grouping.        | Creates groups for aggregate calculations. |
| Used to select specific rows. | Used to calculate results for each group.  |

Example:

```
SELECT city, COUNT(*)
FROM students
WHERE age > 20
GROUP BY city;
```

Here, `WHERE` filters students first, and `GROUP BY` groups the remaining students by city.

## 13. Important Rules of GROUP BY

Remember these rules:

1. `GROUP BY` is commonly used with aggregate functions.
2. You can group records using one or multiple columns.
3. A selected column that is not inside an aggregate function generally needs to appear in the `GROUP BY` clause.
4. `WHERE` filters rows before grouping.
5. `ORDER BY` sorts the final grouped results.
6. Aggregate functions generally ignore NULL values.

## 14. Practice Exercises

Use the `students` table to solve the following exercises.

Beginner Level

1. Count students in each city.
2. Calculate the total fee collected from each city.
3. Calculate the average age of students in each city.
4. Find the minimum fee in each city.
5. Find the maximum fee in each city.

Intermediate Level

6. Display the total number of students and total fee for each city in one query.
7. Count students city-wise whose age is greater than 20.
8. Display cities according to total fee in descending order.
9. Calculate the average fee for each city.
10. Group students by city and age and count the students in each group.

Advanced Level

11. Display city-wise student count and average fee, sorted by average fee from highest to lowest.
12. Display city-wise total fee for students whose age is greater than 20.
13. Display all aggregate statistics for each city in one query.

## 15. Review Questions

1. What is the purpose of the GROUP BY clause?
2. Why do we use GROUP BY with aggregate functions?
3. What is the difference between WHERE and GROUP BY?
4. Can we group records using multiple columns?
5. Can we use ORDER BY with GROUP BY?
6. What does `COUNT(*)` calculate within each group?
7. What happens when we use `GROUP BY city`?
8. Which clause filters records before grouping?

## 16. Quick Revision

| Requirement              | SQL Example |
| ------------------------ | ----------- |
| Count students city-wise | `COUNT(*)`  |
| Total fee city-wise      | `SUM(fee)`  |
| Average age city-wise    | `AVG(age)`  |
| Minimum fee city-wise    | `MIN(fee)`  |
| Maximum fee city-wise    | `MAX(fee)`  |

Basic GROUP BY pattern:

```
SELECT
    column_name,
    COUNT(*) AS total_records
FROM table_name
GROUP BY column_name;
```

## 17. Next Lesson

HAVING Clause in PostgreSQL

Learn how to filter grouped results, such as displaying only those cities that have more than two students or whose total fee exceeds a specified amount.