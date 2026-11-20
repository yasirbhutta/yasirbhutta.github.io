# WHERE Clause in PostgreSQL

## 1. Introduction

In PostgreSQL, the `WHERE` clause is used to filter records based on specified conditions.

It allows us to retrieve only those records that match our requirements.

Real-life example:

Imagine a university database containing 5,000 student records.

The Registrar Office may need to:

- Find a student with ID 101.
- Display students from Multan.
- Find students who are older than 20.
- Display students who belong to the Computer Science department.

Instead of displaying all records, we can use the `WHERE` clause to retrieve specific records.

## 2. Basic Syntax

```
SELECT column1, column2
FROM table_name
WHERE condition;
```

Understanding the syntax:

- `SELECT`: Specifies the columns to retrieve.
- `FROM`: Specifies the table.
- `WHERE`: Specifies the filtering condition.
- `condition`: Defines which records should be displayed.

## 3. Create a Table for Practice

Let's create a students table.

```
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    student_name VARCHAR(100),
    age INTEGER,
    city VARCHAR(50),
    department VARCHAR(50),
    fee NUMERIC(10, 2)
);
```

Insert sample records:

```
INSERT INTO students
    (student_id, student_name, age, city, department, fee)
VALUES
    (1, 'Ali', 20, 'Multan', 'Computer Science', 50000),
    (2, 'Ahmad', 22, 'Lahore', 'Information Technology', 45000),
    (3, 'Usman', 19, 'Multan', 'Mathematics', 40000),
    (4, 'Sara', 21, 'Lahore', 'Computer Science', 50000),
    (5, 'Ayesha', 23, 'Dera Ghazi Khan', 'Information Technology', 45000),
    (6, 'Hassan', 18, 'Multan', 'Computer Science', 50000);
```

## 4. Filter Records Using WHERE

Suppose we want to find a student whose ID is 1.

```
SELECT *
FROM students
WHERE student_id = 1;
```

This query displays only the record where `student_id` equals 1.

## 5. Comparison Operators

Comparison operators are used to compare values in SQL conditions.

| Operator | Meaning                  | Example     |
| -------- | ------------------------ | ----------- |
| `=`      | Equal to                 | `age = 20`  |
| `<>`     | Not equal to             | `age <> 20` |
| `!=`     | Not equal to             | `age != 20` |
| `>`      | Greater than             | `age > 20`  |
| `<`      | Less than                | `age < 20`  |
| `>=`     | Greater than or equal to | `age >= 20` |
| `<=`     | Less than or equal to    | `age <= 20` |

### Example 1: Equal to (=)

Find students from Multan.

```
SELECT *
FROM students
WHERE city = 'Multan';
```

### Example 2: Not Equal to (

)

Find students who are not from Multan.

```
SELECT *
FROM students
WHERE city <> 'Multan';
```

### Example 3: Greater Than (>)

Find students older than 20.

```
SELECT *
FROM students
WHERE age > 20;
```

### Example 4: Less Than (=)

Find students whose age is 20 or above.

```
SELECT *
FROM students
WHERE age >= 20;
```

### Example 6: Less Than or Equal To ( 19;

````

Both conditions must be satisfied.

## 7. Filter Records Using OR

The `OR` operator is used when at least one of the specified conditions must be true.

**Example:** Find students who belong to Multan or Lahore.

```sql
SELECT *
FROM students
WHERE city = 'Multan'
OR city = 'Lahore';
````

A record is displayed if either condition is true.

## 8. Filter Records Using NOT

The `NOT` operator reverses a condition.

Example: Find students who do not belong to Multan.

```
SELECT *
FROM students
WHERE NOT city = 'Multan';
```

The same result can be obtained using:

```
SELECT *
FROM students
WHERE city <> 'Multan';
```

## 9. Use IN Operator

The `IN` operator checks whether a value matches any value in a given list.

Example: Find students from Multan, Lahore, or Islamabad.

```
SELECT *
FROM students
WHERE city IN ('Multan', 'Lahore', 'Islamabad');
```

This is shorter than writing multiple OR conditions.

## 10. Use BETWEEN Operator

The `BETWEEN` operator retrieves values within a specified range.

Example: Find students whose ages are between 20 and 22.

```
SELECT *
FROM students
WHERE age BETWEEN 20 AND 22;
```

Important: `BETWEEN` includes both boundary values. In this example, students aged 20, 21, and 22 are included.

## 11. Use LIKE Operator

The `LIKE` operator is used to search for a particular pattern in text values.

It uses two important wildcard characters:

| Wildcard | Meaning                          |
| -------- | -------------------------------- |
| `%`      | Matches zero or more characters. |
| `_`      | Matches exactly one character.   |

### Example 1: Names Starting with A

```
SELECT *
FROM students
WHERE student_name LIKE 'A%';
```

This finds names starting with A.

### Example 2: Names Ending with A

```
SELECT *
FROM students
WHERE student_name LIKE '%a';
```

This finds names ending with a.

### Example 3: Names Containing the Letter S

```
SELECT *
FROM students
WHERE student_name LIKE '%s%';
```

This finds names containing the letter s.

Note: `LIKE` is case-sensitive in PostgreSQL. Use `ILIKE` for case-insensitive pattern matching.

Example:

```
SELECT *
FROM students
WHERE student_name ILIKE 'a%';
```

This finds names starting with A or a.

## 12. Use IS NULL Operator

In PostgreSQL, `NULL` represents a missing or unknown value.

To find records where a column has no value, use `IS NULL`.

```
SELECT *
FROM students
WHERE city IS NULL;
```

To find records where a column contains a value, use `IS NOT NULL`.

```
SELECT *
FROM students
WHERE city IS NOT NULL;
```

Important: Do not use `= NULL` to check for NULL values.

## 13. Combine Multiple Conditions

We can combine comparison operators and logical operators to create more specific queries.

Example: Find students from Multan or Lahore who are at least 20 years old.

```
SELECT *
FROM students
WHERE (city = 'Multan' OR city = 'Lahore')
AND age >= 20;
```

Parentheses help control the order in which conditions are evaluated.

## 14. Complete Practical Examples

Try the following queries:

Example 1: Find all students from Lahore.

```
SELECT *
FROM students
WHERE city = 'Lahore';
```

Example 2: Find students whose fee is 50,000.

```
SELECT *
FROM students
WHERE fee = 50000;
```

Example 3: Find students older than 20.

```
SELECT student_name, age
FROM students
WHERE age > 20;
```

Example 4: Find Computer Science students.

```
SELECT *
FROM students
WHERE department = 'Computer Science';
```

Example 5: Find students from Multan with a fee of 50,000.

```
SELECT *
FROM students
WHERE city = 'Multan'
AND fee = 50000;
```

Example 6: Find students whose names start with S.

```
SELECT *
FROM students
WHERE student_name LIKE 'S%';
```

## 15. Practice Exercises

Use the students table created in this lesson.

Exercise 1: Basic Filtering

Write queries to:

1. Find the student whose ID is 3.
2. Find students from Lahore.
3. Find students older than 20.
4. Find students whose fee is less than 50,000.

Exercise 2: Comparison Operators

Write queries to:

1. Find students aged 20 or above.
2. Find students whose age is not equal to 20.
3. Find students whose fee is greater than or equal to 45,000.

Exercise 3: Logical Operators

Write queries to:

1. Find students from Multan AND older than 19.
2. Find students from Lahore OR Multan.
3. Find Computer Science students whose fee is 50,000.

Exercise 4: IN and BETWEEN

Write queries to:

1. Find students from Multan, Lahore, or Dera Ghazi Khan.
2. Find students aged between 19 and 22.
3. Find students whose fee is between 40,000 and 50,000.

Exercise 5: LIKE

Write queries to:

1. Find students whose names start with A.
2. Find students whose names end with n.
3. Find students whose names contain the letter s, regardless of case.

## 16. Review Questions

1. What is the purpose of the WHERE clause?
2. What is the difference between `=` and `<>`?
3. What is the difference between AND and OR?
4. Why do we use the IN operator?
5. What is the purpose of BETWEEN?
6. What do `%` and `_` represent in LIKE?
7. What is the difference between LIKE and ILIKE?
8. How do we find records containing NULL values?
9. Why do we use parentheses when combining conditions?

## 17. Quick Revision

| SQL Keyword / Operator | Purpose                                          |
| ---------------------- | ------------------------------------------------ |
| `WHERE`                | Filters records.                                 |
| `=`                    | Checks equality.                                 |
| `<>`                   | Checks inequality.                               |
| `>` / `<`              | Compares values.                                 |
| `AND`                  | Requires all conditions to be true.              |
| `OR`                   | Requires at least one condition to be true.      |
| `NOT`                  | Reverses a condition.                            |
| `IN`                   | Matches values from a list.                      |
| `BETWEEN`              | Checks a range.                                  |
| `LIKE`                 | Matches a text pattern.                          |
| `ILIKE`                | Matches a text pattern without case sensitivity. |
| `IS NULL`              | Finds missing values.                            |

Next Lesson: ORDER BY Clause in PostgreSQL

Students will learn how to sort query results in ascending and descending order using one or multiple columns.