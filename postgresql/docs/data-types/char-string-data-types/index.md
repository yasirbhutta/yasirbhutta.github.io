---
layout: page
title: "Character and String Data Types in PostgreSQL"
description: Learn how to use PostgreSQL character and string data types, including CHAR, VARCHAR, and TEXT, with practical SQL examples and comparisons.
keywords: PostgreSQL character data types, PostgreSQL string data types, CHAR, VARCHAR, TEXT, CHAR vs VARCHAR, VARCHAR vs TEXT, PostgreSQL string examples
---

## **1. What are Character and String Data Types?**

Character and string data types are used to store text, letters, words, names, addresses and other textual information in a database.

For example:

- Student name: Muhammad Yasir
- Department: Computer Science
- Gender: Male
- City: Dera Ghazi Khan
- Email: yasir\@example.com

**Simple definition:**

A character or string data type specifies how PostgreSQL stores textual information in a database column.

## **2. Types of Character and String Data Types**

PostgreSQL provides three commonly used character data types.

**1. CHAR(n)**

Fixed-length character string.

**2. VARCHAR(n)**

Variable-length character string with a maximum length.

**3. TEXT**

Variable-length character string without a declared length limit.

## **3. CHAR(n) – Fixed-Length Character Data Type**

CHAR stands for Character.

It is used to store text with a fixed length.

**Example:**

```
CHAR(5)
```

It means the column has a fixed length of 5 characters.

Consider the following values:

| Inserted value | Stored representation |
| -------------- | --------------------- |
| 'YASIR'        | 'YASIR'               |
| 'ALI'          | 'ALI  '               |
| 'AB'           | 'AB   '               |

PostgreSQL adds spaces at the end of shorter values to fill the specified length.

### **Real-life example**

Suppose a university uses a fixed-length campus code containing exactly 5 characters.

```
CREATE TABLE campuses (
    campus_code CHAR(5)
);
```

Insert records:

```
INSERT INTO campuses
VALUES
('DGK01'),
('DGK');
```

**Important points:**

- CHAR(n) has a fixed declared length.
- Shorter values are padded with spaces.
- Values longer than the declared length are rejected (except excess trailing spaces).
- It is useful when fixed-length character fields are required.

## **4. VARCHAR(n) – Variable-Length Character Data Type**

VARCHAR stands for Variable Character.

It is used to store text of different lengths, up to a specified maximum.

**Example:**

```
VARCHAR(50)
```

It means the column can store text containing up to 50 characters.

Consider these values:

| Value            | Number of characters |
| ---------------- | -------------------- |
| Ali              | 3                    |
| Yasir            | 5                    |
| Muhammad Yasir   | 14                   |
| Computer Science | 16                   |

All these values can be stored in VARCHAR(50).

### **Real-life example**

A university student name may contain different numbers of characters.

```
CREATE TABLE students (
    student_id INTEGER,
    student_name VARCHAR(100)
);
```

Insert records:

```
INSERT INTO students
VALUES
(1, 'Ali'),
(2, 'Muhammad Yasir'),
(3, 'Muhammad Hamza Bhutta');
```

**Important points:**

- VARCHAR(n) stores variable-length text.
- It allows different text lengths.
- It has a maximum character limit.
- It does not add extra spaces to shorter values.
- Values exceeding the specified length are rejected.

## **5. TEXT – Variable-Length Character Data Type**

TEXT is used to store text without specifying a maximum length in the column definition.

It is suitable for storing long textual information.

For example:

- Student addresses
- Course descriptions
- Department descriptions
- Notices
- Feedback
- Comments

### **Real-life example**

A university course may have a detailed description.

```
CREATE TABLE courses (
    course_id INTEGER,
    course_name VARCHAR(100),
    course_description TEXT
);
```

Insert a record:

```
INSERT INTO courses
VALUES (
    101,
    'Database Systems',
    'This course introduces database concepts, SQL, PostgreSQL and database design.'
);
```

**Important points:**

- TEXT stores variable-length strings.
- No maximum length is specified in the column definition.
- It is suitable for long descriptions and paragraphs.
- PostgreSQL supports very large text values, subject to its system limits.

## **6. Difference Between CHAR, VARCHAR and TEXT**

This is the most important comparison for students.

| Feature              | CHAR(n)            | VARCHAR(n)         | TEXT              |
| -------------------- | ------------------ | ------------------ | ----------------- |
| Full name            | Character          | Variable Character | Text              |
| Length               | Fixed              | Variable           | Variable          |
| Maximum length       | n                  | n                  | No declared limit |
| Adds trailing spaces | Yes                | No                 | No                |
| Length restriction   | Yes                | Yes                | No declared limit |
| Best use             | Fixed-length codes | Names and emails   | Long descriptions |

### **Practical comparison**

Consider three columns:

```
CREATE TABLE string_examples (
    code CHAR(5),
    name VARCHAR(50),
    description TEXT
);
```

**Understanding the difference**

CHAR(5)

# **ALI··**

Fixed length: 5 characters. Dots represent trailing spaces.

VARCHAR(50)

# **ALI**

Stores the actual three characters without padding.

TEXT

**ALI is a student of Computer Science.**

Stores longer text without a declared column length.

**Important:** In PostgreSQL, VARCHAR without a length limit and TEXT behave similarly. There is generally no performance advantage to choosing VARCHAR(n) over TEXT. Choose VARCHAR(n) when you want PostgreSQL to enforce a maximum length.

## **7. Practical SQL Example: University Database**

Let's create a university database table using all three character data types.

```
CREATE TABLE university_students (
    student_id INTEGER,
    campus_code CHAR(5),
    student_name VARCHAR(100),
    address TEXT
);
```

Insert records:

```
INSERT INTO university_students
VALUES
(
    1,
    'DGK01',
    'Muhammad Yasir',
    'Dera Ghazi Khan, Punjab, Pakistan'
),
(
    2,
    'DGK02',
    'Muhammad Hamza Bhutta',
    'Dera Ghazi Khan, Punjab, Pakistan'
);
```

Retrieve records:

```
SELECT * FROM university_students;
```

### **Check the length of strings**

PostgreSQL provides the `LENGTH()` function to count characters.

```
SELECT
    student_name,
    LENGTH(student_name)
FROM university_students;
```

Example output:

| student_name          | length |
| --------------------- | ------ |
| Muhammad Yasir        | 14     |
| Muhammad Hamza Bhutta | 21     |

For `CHAR(n)`, trailing spaces are disregarded by `LENGTH()` because PostgreSQL treats it as a blank-padded character type.

## **8. Important String Functions in PostgreSQL**

Students should also become familiar with these basic string functions.

| Function    | Purpose                         | Example                                |
| ----------- | ------------------------------- | -------------------------------------- |
| LENGTH()    | Counts characters               | `LENGTH('Yasir')`                      |
| UPPER()     | Converts to uppercase           | `UPPER('yasir')`                       |
| LOWER()     | Converts to lowercase           | `LOWER('YASIR')`                       |
| TRIM()      | Removes leading/trailing spaces | `TRIM(' Yasir ')`                      |
| CONCAT()    | Joins strings                   | `CONCAT('Muhammad',' Yasir')`          |
| SUBSTRING() | Extracts part of a string       | `SUBSTRING('PostgreSQL' FROM 1 FOR 4)` |

Example:

```
SELECT
    UPPER('yasir') AS uppercase_name,
    LOWER('YASIR') AS lowercase_name,
    LENGTH('Yasir') AS name_length,
    CONCAT('Muhammad', ' Yasir') AS full_name;
```

## **9. Student Practice Exercise**

Choose the most appropriate data type for each field.

| Database field     | Example                   | Suggested data type |
| ------------------ | ------------------------- | ------------------- |
| Campus code        | DGK01                     | CHAR(5)             |
| Student name       | Muhammad Yasir            | VARCHAR(100)        |
| Email address      | yasir\@example.com        | VARCHAR(150)        |
| Home address       | Dera Ghazi Khan, Pakistan | TEXT                |
| Course description | Long paragraph            | TEXT                |
| Department name    | Computer Science          | VARCHAR(100)        |

**Task:** Create a table named `university_departments` with the following columns:

1. department_id
2. department_code
3. department_name
4. department_description

Choose suitable data types for each column.

## **10. Test Your Understanding – MCQs**

**Character Data Types Quiz**

6 MCQs

**Q1. Which PostgreSQL data type stores fixed-length characters?**

A. TEXT

B. VARCHAR

C. CHAR

D. INTEGER

**Q2. What does VARCHAR(50) mean?**

A. Exactly 50 characters

B. Maximum 50 characters

C. 50 words

D. 50 bytes

**Q3. Which data type is suitable for a long course description?**

A. CHAR(5)

B. INTEGER

C. TEXT

D. SMALLINT

**Q4. What happens when a shorter value is stored in CHAR(5)?**

A. An error always occurs

B. Spaces are added at the end

C. Zeros are added

D. The value is deleted

**Q5. Which function converts text into uppercase?**

A. LOWER()

B. TRIM()

C. UPPER()

D. LENGTH()

**Q6. Which statement about TEXT is correct?**

A. It stores only five characters

B. It is fixed-length

C. It has no declared maximum length

D. It stores only numbers

Submit Answers

## **11. Key Points to Remember**

1. CHAR(n) stores fixed-length character strings.
2. VARCHAR(n) stores variable-length strings with a maximum length.
3. TEXT stores variable-length strings without a declared maximum length.
4. CHAR adds trailing spaces to shorter values.
5. VARCHAR and TEXT do not add padding.
6. VARCHAR(n) and TEXT have similar performance characteristics in PostgreSQL.
7. LENGTH() counts characters in a string.

**Official PostgreSQL Documentation:** [Character Types](https://www.postgresql.org/docs/current/datatype-character.html?utm_source=chatgpt.com)



