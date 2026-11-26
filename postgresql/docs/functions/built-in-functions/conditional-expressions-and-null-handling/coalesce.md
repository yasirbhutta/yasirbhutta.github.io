---
layout: page
title: "COALESCE() Function in PostgreSQL"
description: Learn how to use the PostgreSQL COALESCE() function to handle NULL values by returning the first non-NULL value from a list of expressions, with practical SQL examples and data handling techniques.
keywords: PostgreSQL COALESCE function, COALESCE() in PostgreSQL, PostgreSQL NULL handling, replace NULL values, first non-NULL value, PostgreSQL conditional expressions, SQL NULL handling examples
---

`COALESCE()` is a PostgreSQL function that returns the **first non-NULL value** from a list of expressions.

In simple words, it checks values from left to right and returns the first value that is not `NULL`.

## **1. Real-life example**

Suppose a university maintains student contact information. Some students have not provided their phone numbers.

| Student Name | Phone Number |
| ------------ | ------------ |
| Ali          | 03001234567  |
| Ahmed        | NULL         |
| Sara         | 03111234567  |

If a phone number is missing, we can display `Not Provided` instead of `NULL`.

## **2. Syntax**

```
COALESCE(value1, value2, value3, ...);
```

- PostgreSQL checks `value1` first.
- If it is `NULL`, it checks `value2`.
- It continues until it finds a non-NULL value.
- If all values are `NULL`, the result is `NULL`.

## **3. Simple examples**

**Example 1: First value is NULL**

```
SELECT COALESCE(NULL, 'Hello', 'World');
```

Output:

```
Hello
```

**Example 2: First value is available**

```
SELECT COALESCE('Ali', 'Ahmed', 'Sara');
```

Output:

```
Ali
```

**Example 3: All values are NULL**

```
SELECT COALESCE(NULL, NULL, NULL);
```

Output:

```
NULL
```

## **4. Practical example with a student table**

Suppose we have this table:

```
CREATE TABLE students (
    student_id INTEGER,
    student_name VARCHAR(100),
    phone VARCHAR(20)
);
```

Insert some records:

```
INSERT INTO students VALUES
(1, 'Ali', '03001234567'),
(2, 'Ahmed', NULL),
(3, 'Sara', '03111234567');
```

Now retrieve student information:

```
SELECT
    student_name,
    COALESCE(phone, 'Not Provided') AS phone_number
FROM students;
```

Expected output:

| student_name | phone_number |
| ------------ | ------------ |
| Ali          | 03001234567  |
| Ahmed        | Not Provided |
| Sara         | 03111234567  |

Notice that `COALESCE()` replaces the `NULL` value with `Not Provided` in the query result. It does not change the original table data.

## **5. COALESCE() with numeric values**

Suppose some students have not received their scholarship amounts.

```
SELECT
    student_name,
    COALESCE(scholarship_amount, 0) AS scholarship
FROM student_scholarships;
```

If `scholarship_amount` is `NULL`, the query displays `0`.

## **6. COALESCE() vs NULLIF()**

These functions perform different tasks:

| Function     | Purpose                                     |
| ------------ | ------------------------------------------- |
| `COALESCE()` | Returns the first non-NULL value            |
| `NULLIF()`   | Returns NULL when two expressions are equal |

Example:

```
SELECT COALESCE(NULL, 100);
```

Output: `100`

```
SELECT NULLIF(100, 100);
```

Output: `NULL`

## **7. Practical exercise**

Create a table named `employees` with these columns:

- `employee_id` — INTEGER
- `employee_name` — VARCHAR(100)
- `email` — VARCHAR(100)
- `salary` — NUMERIC(10,2)

Tasks:

1. Insert three employees.
2. Set the email of one employee to `NULL`.
3. Set the salary of another employee to `NULL`.
4. Use `COALESCE()` to display `Email Not Provided` when email is NULL.
5. Use `COALESCE()` to display `0` when salary is NULL.

## **8. Quick MCQ**

**What will be the output of the following SQL statement?**

```
SELECT COALESCE(NULL, NULL, 50, 100);
```

A. NULL

B. 50

C. 100

D. 0

Check Answer



**Key point:** Use `COALESCE()` when you want to handle missing (`NULL`) values and display a meaningful default value.

Official documentation: [PostgreSQL COALESCE Documentation](https://www.postgresql.org/docs/current/functions-conditional.html?utm_source=chatgpt.com)