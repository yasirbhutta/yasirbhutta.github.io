---
layout: page
title: "Boolean Data Type in PostgreSQL"
description: Learn how to use the PostgreSQL BOOLEAN data type to store TRUE, FALSE, and NULL values, with practical examples of inserting, retrieving, and updating Boolean data.
keywords: PostgreSQL BOOLEAN, Boolean data type, TRUE and FALSE values, NULL values, PostgreSQL Boolean examples, Boolean queries, PostgreSQL logical data
---

## **1. Introduction: What is a Boolean?**

In real life, many questions have only two possible answers:

- Is a student present? **Yes or No**
- Is a fee paid? **Yes or No**
- Is a course active? **Yes or No**
- Is a user account enabled? **Yes or No**

In PostgreSQL, we use the **BOOLEAN** data type to store these two-state values.

## **2. Boolean Values in PostgreSQL**

PostgreSQL supports three Boolean states:

| Value   | Meaning                 |
| ------- | ----------------------- |
| `TRUE`  | Yes                     |
| `FALSE` | No                      |
| `NULL`  | Unknown or not provided |

**Important:** `NULL` is not the same as `FALSE`. It means that the value is unknown or missing.

## **3. Creating a Table with BOOLEAN**

Let's create a student table:

```
CREATE TABLE students (
    student_id INTEGER,
    student_name VARCHAR(100),
    fee_paid BOOLEAN,
    is_active BOOLEAN
);
```

Here:

- `student_id` stores the student's ID.
- `student_name` stores the student's name.
- `fee_paid` stores whether the fee has been paid.
- `is_active` stores whether the student is active.

## **4. Inserting Boolean Values**

```
INSERT INTO students
VALUES
(1, 'Ali', TRUE, TRUE),
(2, 'Ahmed', FALSE, TRUE),
(3, 'Sara', TRUE, FALSE),
(4, 'Ayesha', NULL, TRUE);
```

PostgreSQL also accepts these Boolean representations:

| TRUE    | FALSE   |
| ------- | ------- |
| `TRUE`  | `FALSE` |
| `'t'`   | `'f'`   |
| `'yes'` | `'no'`  |
| `'1'`   | `'0'`   |

For beginners, use `TRUE` and `FALSE` because they are clear and readable.

## **5. Retrieving Boolean Data**

**Find students whose fees have been paid:**

```
SELECT *
FROM students
WHERE fee_paid = TRUE;
```

You can also write:

```
SELECT *
FROM students
WHERE fee_paid;
```

**Find students whose fees have not been paid:**

```
SELECT *
FROM students
WHERE fee_paid = FALSE;
```

**Find students with unknown fee status:**

```
SELECT *
FROM students
WHERE fee_paid IS NULL;
```

**Find students with a known fee status:**

```
SELECT *
FROM students
WHERE fee_paid IS NOT NULL;
```

## **6. Updating Boolean Values**

Suppose a student has paid the fee. We can update the record:

```
UPDATE students
SET fee_paid = TRUE
WHERE student_id = 2;
```

To deactivate a student:

```
UPDATE students
SET is_active = FALSE
WHERE student_id = 1;
```

## **7. BOOLEAN vs INTEGER**

| Feature      | BOOLEAN         | INTEGER        |
| ------------ | --------------- | -------------- |
| Stores       | True/False      | Whole numbers  |
| Example      | `TRUE`          | `1`            |
| Typical use  | Fee paid or not | Student age    |
| Storage      | 1 byte          | 4 bytes        |
| Main purpose | Logical values  | Numeric values |

Use `BOOLEAN` when a field represents a yes/no condition. Do not use `INTEGER` just to store `1` or `0` for such conditions.

## **8. Practical Exercise**

Create a table named `courses` with the following columns:

| Column        | Data Type    |
| ------------- | ------------ |
| course_id     | INTEGER      |
| course_name   | VARCHAR(100) |
| is_active     | BOOLEAN      |
| is_compulsory | BOOLEAN      |

**Tasks:**

1. Create the table.
2. Insert three courses.
3. Mark one course as inactive.
4. Display only active courses.
5. Display compulsory courses.
6. Find courses where the compulsory status is unknown.

## **9. Quick MCQ Quiz**

**Question 1. Which PostgreSQL data type stores TRUE or FALSE values?**

A. INTEGER

B. BOOLEAN

C. VARCHAR

D. NUMERIC



**Question 2. Which value represents an unknown Boolean state?**

A. FALSE

B. 0

C. NULL

D. TRUE



**Question 3. Which condition finds records where fee_paid is unknown?**

A. fee_paid = FALSE

B. fee_paid IS NULL

C. fee_paid = TRUE

D. fee_paid = 0



0 of 3 answered

Check answers

## **10. Key Points to Remember**

- `BOOLEAN` stores logical values.
- PostgreSQL supports `TRUE`, `FALSE`, and `NULL`.
- Use `IS NULL` to check unknown values.
- Use `IS NOT NULL` to check known values.
- Prefer `BOOLEAN` over `INTEGER` for yes/no conditions.

**Next lecture:** PostgreSQL Constraints — `NOT NULL`, `UNIQUE`, `PRIMARY KEY`, `FOREIGN KEY`, and `CHECK`.

Reference: [PostgreSQL Official Documentation: Boolean Type](https://www.postgresql.org/docs/current/datatype-boolean.html?utm_source=chatgpt.com)