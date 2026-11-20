# Student Notes: String Functions in PostgreSQL

## 1. Introduction

Imagine a university database that stores student names, departments, email addresses, and other text information.

Sometimes we need to modify or manipulate this text.

For example:

- Convert student names into uppercase or lowercase.
- Count the number of characters in a name.
- Combine first name and last name.
- Extract part of an email address.
- Remove unnecessary spaces.
- Replace one word with another.
- Search for a particular word in a text column.

PostgreSQL provides String Functions to perform these operations.

## 2. What is a String?

A string is a sequence of characters.

Examples:

```
Ali
Computer Science
Ghazi University
ali@gmail.com
Pakistan
```

In PostgreSQL, strings are commonly stored using these data types:

| Data Type    | Description                                     | Example       |
| ------------ | ----------------------------------------------- | ------------- |
| `CHAR(n)`    | Fixed-length character string                   | `CHAR(10)`    |
| `VARCHAR(n)` | Variable-length string with a maximum length    | `VARCHAR(50)` |
| `TEXT`       | Variable-length string without a declared limit | `TEXT`        |

Example:

```
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    department TEXT
);
```

## 3. Create a Sample Table

We will use a students table to understand string functions.

### Step 1: Create the Table

```
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(100),
    email VARCHAR(100)
);
```

### Step 2: Insert Sample Records

```
INSERT INTO students
VALUES
(1, 'Ali', 'Khan', 'Computer Science', 'ali@gmail.com'),
(2, 'Sara', 'Ahmed', 'Mathematics', 'sara@gmail.com'),
(3, 'Usman', 'Raza', 'Information Technology', 'usman@gmail.com'),
(4, 'Hina', 'Malik', 'Physics', 'hina@gmail.com'),
(5, 'Bilal', 'Ahmad', 'Chemistry', 'bilal@gmail.com');
```

### Step 3: Display Records

```
SELECT *
FROM students;
```

Expected output:

| student_id | first_name | last_name | department             | email            |
| ---------- | ---------- | --------- | ---------------------- | ---------------- |
| 1          | Ali        | Khan      | Computer Science       | ali\@gmail.com   |
| 2          | Sara       | Ahmed     | Mathematics            | sara\@gmail.com  |
| 3          | Usman      | Raza      | Information Technology | usman\@gmail.com |
| 4          | Hina       | Malik     | Physics                | hina\@gmail.com  |
| 5          | Bilal      | Ahmad     | Chemistry              | bilal\@gmail.com |

## 4. UPPER() Function

The `UPPER()` function converts all characters in a string into uppercase letters.

### Syntax

```
UPPER(string);
```

### Example 1: Convert Text into Uppercase

```
SELECT UPPER('Ghazi University');
```

Expected output:

```
GHAZI UNIVERSITY
```

### Example 2: Convert Student Names into Uppercase

```
SELECT
    first_name,
    UPPER(first_name) AS uppercase_name
FROM students;
```

Expected output:

| first_name | uppercase_name |
| ---------- | -------------- |
| Ali        | ALI            |
| Sara       | SARA           |
| Usman      | USMAN          |
| Hina       | HINA           |
| Bilal      | BILAL          |

## 5. LOWER() Function

The `LOWER()` function converts all characters in a string into lowercase letters.

### Syntax

```
LOWER(string);
```

### Example 1

```
SELECT LOWER('GHAZI UNIVERSITY');
```

Expected output:

```
ghazi university
```

### Example 2

```
SELECT
    first_name,
    LOWER(first_name) AS lowercase_name
FROM students;
```

## 6. INITCAP() Function

The `INITCAP()` function converts the first letter of each word into uppercase and the remaining letters into lowercase.

### Syntax

```
INITCAP(string);
```

### Example 1

```
SELECT INITCAP('ghazi university');
```

Expected output:

```
Ghazi University
```

### Example 2

```
SELECT INITCAP('COMPUTER SCIENCE');
```

Expected output:

```
Computer Science
```

### Example 3: Format Department Names

```
SELECT
    department,
    INITCAP(department) AS formatted_department
FROM students;
```

## 7. LENGTH() Function

The `LENGTH()` function returns the number of characters in a string.

### Syntax

```
LENGTH(string);
```

### Example 1

```
SELECT LENGTH('Pakistan');
```

Expected output:

| length |
| ------ |
| 8      |

### Example 2: Count Characters in Student Names

```
SELECT
    first_name,
    LENGTH(first_name) AS name_length
FROM students;
```

Expected output:

| first_name | name_length |
| ---------- | ----------- |
| Ali        | 3           |
| Sara       | 4           |
| Usman      | 5           |
| Hina       | 4           |
| Bilal      | 5           |

Note: Spaces are also counted as characters.

```
SELECT LENGTH('Ghazi University');
```

Expected output:

```
16
```

## 8. CONCAT() Function

The `CONCAT()` function combines two or more strings into one string.

### Syntax

```
CONCAT(string1, string2, ...);
```

### Example 1: Combine Two Strings

```
SELECT CONCAT('Ghazi', ' University');
```

Expected output:

```
Ghazi University
```

### Example 2: Combine First and Last Names

```
SELECT
    CONCAT(first_name, ' ', last_name) AS full_name
FROM students;
```

Expected output:

| full_name   |
| ----------- |
| Ali Khan    |
| Sara Ahmed  |
| Usman Raza  |
| Hina Malik  |
| Bilal Ahmad |

## 9. CONCAT_WS() Function

`CONCAT_WS()` combines strings using a specified separator.

WS stands for With Separator.

### Syntax

```
CONCAT_WS(separator, string1, string2, ...);
```

### Example 1

```
SELECT CONCAT_WS('-', '2026', '11', '09');
```

Expected output:

```
2026-11-09
```

### Example 2: Combine Student Names

```
SELECT
    CONCAT_WS(' ', first_name, last_name) AS full_name
FROM students;
```

### Difference Between CONCAT() and CONCAT_WS()

| CONCAT()                            | CONCAT_WS()                       |
| ----------------------------------- | --------------------------------- |
| Combines strings directly           | Combines strings with a separator |
| Separator must be included manually | Separator is provided once        |
| `CONCAT('Ali', 'Khan')`             | `CONCAT_WS(' ', 'Ali', 'Khan')`   |

Important: `CONCAT_WS()` skips NULL values after the separator. `CONCAT()` also treats NULL arguments as empty strings.

## 10. SUBSTRING() Function

The `SUBSTRING()` function extracts a specific part of a string.

### Syntax

```
SUBSTRING(string FROM start_position FOR length);
```

- `string`: Original text.
- `start_position`: Position where extraction begins.
- `length`: Number of characters to extract.

### Example 1: Extract Part of a String

```
SELECT SUBSTRING('PostgreSQL' FROM 1 FOR 4);
```

Expected output:

```
Post
```

### Example 2

```
SELECT SUBSTRING('PostgreSQL' FROM 5 FOR 3);
```

Expected output:

```
gre
```

### Example 3: Extract Student Names

```
SELECT
    first_name,
    SUBSTRING(first_name FROM 1 FOR 2) AS short_name
FROM students;
```

Expected output:

| first_name | short_name |
| ---------- | ---------- |
| Ali        | Al         |
| Sara       | Sa         |
| Usman      | Us         |
| Hina       | Hi         |
| Bilal      | Bi         |

## 11. LEFT() Function

The `LEFT()` function returns a specified number of characters from the beginning of a string.

### Syntax

```
LEFT(string, number_of_characters);
```

### Example

```
SELECT LEFT('PostgreSQL', 4);
```

Expected output:

```
Post
```

### Example: First Three Characters

```
SELECT
    first_name,
    LEFT(first_name, 3) AS short_name
FROM students;
```

## 12. RIGHT() Function

The `RIGHT()` function returns a specified number of characters from the end of a string.

### Syntax

```
RIGHT(string, number_of_characters);
```

### Example

```
SELECT RIGHT('PostgreSQL', 3);
```

Expected output:

```
SQL
```

### Example: Extract Email Domains

```
SELECT
    email,
    RIGHT(email, 9) AS email_part
FROM students;
```

For extracting the complete domain regardless of its length, use a more suitable function such as `SPLIT_PART()`, which we will study later.

## 13. TRIM() Function

The `TRIM()` function removes unwanted characters from the beginning, end, or both sides of a string.

It is commonly used to remove extra spaces.

### Syntax

```
TRIM(string);
```

### Example 1: Remove Spaces

```
SELECT TRIM('   Ghazi University   ');
```

Expected output:

```
Ghazi University
```

### Example 2: Remove Leading Spaces

```
SELECT LTRIM('   Pakistan');
```

Expected output:

```
Pakistan
```

### Example 3: Remove Trailing Spaces

```
SELECT RTRIM('Pakistan   ');
```

Expected output:

```
Pakistan
```

### Difference Between TRIM(), LTRIM(), and RTRIM()

| Function  | Purpose                           |
| --------- | --------------------------------- |
| `TRIM()`  | Removes characters from both ends |
| `LTRIM()` | Removes characters from the left  |
| `RTRIM()` | Removes characters from the right |

## 14. REPLACE() Function

The `REPLACE()` function replaces all occurrences of a specified substring with another substring.

### Syntax

```
REPLACE(string, old_text, new_text);
```

### Example 1

```
SELECT REPLACE(
    'Hello World',
    'World',
    'Pakistan'
);
```

Expected output:

```
Hello Pakistan
```

### Example 2: Replace Department Name

```
SELECT
    REPLACE(
        department,
        'Computer Science',
        'CS'
    ) AS short_department
FROM students;
```

This replaces `Computer Science` with `CS`.

## 15. POSITION() Function

The `POSITION()` function returns the starting position of a substring within another string.

### Syntax

```
POSITION(substring IN string);
```

### Example 1

```
SELECT POSITION('SQL' IN 'PostgreSQL');
```

Expected output:

```
8
```

### Example 2: Find the Position of @ in Email

```
SELECT
    email,
    POSITION('@' IN email) AS at_position
FROM students;
```

This identifies the position of the `@` character in each email address.

## 16. STRPOS() Function

`STRPOS()` also returns the position of a substring within a string.

### Syntax

```
STRPOS(string, substring);
```

### Example

```
SELECT STRPOS('PostgreSQL', 'SQL');
```

Expected output:

```
8
```

Note: Both `POSITION()` and `STRPOS()` perform substring position searches. They return 0 if the substring is not found.

## 17. REVERSE() Function

The `REVERSE()` function reverses the order of characters in a string.

### Syntax

```
REVERSE(string);
```

### Example

```
SELECT REVERSE('Pakistan');
```

Expected output:

```
natsikaP
```

### Example: Reverse Student Names

```
SELECT
    first_name,
    REVERSE(first_name) AS reversed_name
FROM students;
```

## 18. REPEAT() Function

The `REPEAT()` function repeats a string a specified number of times.

### Syntax

```
REPEAT(string, number);
```

### Example

```
SELECT REPEAT('SQL ', 3);
```

Expected output:

```
SQL SQL SQL
```

## 19. LPAD() Function

`LPAD()` adds characters to the left side of a string until it reaches the specified length.

### Syntax

```
LPAD(string, length, fill_text);
```

### Example

```
SELECT LPAD('25', 5, '0');
```

Expected output:

```
00025
```

### Example: Format Student IDs

```
SELECT
    student_id,
    LPAD(student_id::TEXT, 5, '0') AS formatted_id
FROM students;
```

Expected output:

| student_id | formatted_id |
| ---------- | ------------ |
| 1          | 00001        |
| 2          | 00002        |
| 3          | 00003        |
| 4          | 00004        |
| 5          | 00005        |

Here, `::TEXT` converts the integer student ID into text.

## 20. RPAD() Function

`RPAD()` adds characters to the right side of a string until it reaches the specified length.

### Syntax

```
RPAD(string, length, fill_text);
```

### Example

```
SELECT RPAD('SQL', 8, '*');
```

Expected output:

```
SQL*****
```

### Difference Between LPAD() and RPAD()

| LPAD()                      | RPAD()                       |
| --------------------------- | ---------------------------- |
| Adds characters to the left | Adds characters to the right |
| `LPAD('25', 5, '0')`        | `RPAD('25', 5, '0')`         |
| `00025`                     | `25000`                      |

## 21. SPLIT_PART() Function

The `SPLIT_PART()` function divides a string using a specified delimiter and returns a selected part.

### Syntax

```
SPLIT_PART(string, delimiter, field_number);
```

### Example 1: Split a Full Name

```
SELECT SPLIT_PART('Ali Khan', ' ', 1);
```

Expected output:

```
Ali
```

### Example 2

```
SELECT SPLIT_PART('Ali Khan', ' ', 2);
```

Expected output:

```
Khan
```

### Example 3: Extract Email Domain

```
SELECT
    email,
    SPLIT_PART(email, '@', 2) AS email_domain
FROM students;
```

Expected output:

| email            | email_domain |
| ---------------- | ------------ |
| ali\@gmail.com   | gmail.com    |
| sara\@gmail.com  | gmail.com    |
| usman\@gmail.com | gmail.com    |
| hina\@gmail.com  | gmail.com    |
| bilal\@gmail.com | gmail.com    |

## 22. STRING_AGG() Function

`STRING_AGG()` combines values from multiple rows into a single string.

It is particularly useful for reports.

### Syntax

```
STRING_AGG(column_name, separator);
```

### Example: Combine Student Names Department-Wise

```
SELECT
    department,
    STRING_AGG(first_name, ', ') AS student_names
FROM students
GROUP BY department;
```

Expected output:

| department             | student_names |
| ---------------------- | ------------- |
| Computer Science       | Ali, Bilal    |
| Mathematics            | Sara          |
| Information Technology | Usman         |
| Physics                | Hina          |
| Chemistry              | Bilal         |

The exact order of names is not guaranteed unless ordering is specified inside `STRING_AGG()`.

For predictable ordering:

```
SELECT
    department,
    STRING_AGG(first_name, ', ' ORDER BY first_name) AS student_names
FROM students
GROUP BY department;
```

## 23. String Functions with WHERE Clause

String functions can also be used to filter records.

### Example 1: Find Names in Uppercase Comparison

```
SELECT *
FROM students
WHERE UPPER(first_name) = 'ALI';
```

This finds Ali even if the stored name has different letter casing.

### Example 2: Find Names Starting with A

```
SELECT *
FROM students
WHERE first_name LIKE 'A%';
```

### Example 3: Find Emails Containing Gmail

```
SELECT *
FROM students
WHERE email LIKE '%gmail%';
```

### Example 4: Find Names with More Than Four Characters

```
SELECT *
FROM students
WHERE LENGTH(first_name) > 4;
```

## 24. Important Points to Remember

1. String functions are used to manipulate text values.
2. `UPPER()` converts text into uppercase.
3. `LOWER()` converts text into lowercase.
4. `INITCAP()` capitalizes the first letter of each word.
5. `LENGTH()` counts characters.
6. `CONCAT()` combines strings.
7. `CONCAT_WS()` combines strings using a separator.
8. `SUBSTRING()` extracts part of a string.
9. `LEFT()` extracts characters from the beginning.
10. `RIGHT()` extracts characters from the end.
11. `TRIM()` removes unwanted characters from both ends.
12. `REPLACE()` replaces specified text.
13. `POSITION()` finds the position of a substring.
14. `REVERSE()` reverses a string.
15. `LPAD()` adds characters to the left.
16. `RPAD()` adds characters to the right.
17. `SPLIT_PART()` extracts a part of a string using a delimiter.
18. `STRING_AGG()` combines values from multiple rows.

## 25. Practice Exercises

### Beginner Level

1. Display all student names in uppercase.
2. Display all student names in lowercase.
3. Display department names using INITCAP().
4. Find the length of every student's first name.
5. Combine first and last names into a full name.
6. Extract the first three characters of every student name.
7. Reverse all student names.

### Intermediate Level

8. Remove extra spaces from a text value using TRIM().
9. Replace the word `Computer Science` with `CS`.
10. Find the position of `@` in each email address.
11. Extract the email domain using SPLIT_PART().
12. Display student IDs in five-digit format using LPAD().
13. Find students whose names contain more than four characters.
14. Find all students whose email addresses end with `gmail.com`.

### Advanced Level

15. Combine student names department-wise using STRING_AGG().
16. Display each department with its student names in alphabetical order.
17. Extract the first and last names from a full-name string.
18. Create a formatted student ID using a prefix such as `GU-`.
19. Replace spaces in department names with underscores.
20. Use multiple string functions in one SELECT statement to create a formatted student report.

## 26. Review Questions

1. What is a string in PostgreSQL?
2. What is the difference between VARCHAR and TEXT?
3. What does UPPER() do?
4. What is the purpose of INITCAP()?
5. How does LENGTH() work?
6. What is the difference between CONCAT() and CONCAT_WS()?
7. What is the purpose of SUBSTRING()?
8. What is the difference between LEFT() and RIGHT()?
9. What does TRIM() do?
10. What is the purpose of REPLACE()?
11. What is the difference between POSITION() and STRPOS()?
12. What is the purpose of SPLIT_PART()?
13. What is the difference between LPAD() and RPAD()?
14. What does STRING_AGG() do?

## 27. Quick Revision

| Function       | Purpose                            |
| -------------- | ---------------------------------- |
| `UPPER()`      | Converts text to uppercase         |
| `LOWER()`      | Converts text to lowercase         |
| `INITCAP()`    | Capitalizes each word              |
| `LENGTH()`     | Counts characters                  |
| `CONCAT()`     | Combines strings                   |
| `CONCAT_WS()`  | Combines strings with a separator  |
| `SUBSTRING()`  | Extracts part of a string          |
| `LEFT()`       | Extracts characters from the left  |
| `RIGHT()`      | Extracts characters from the right |
| `TRIM()`       | Removes characters from both ends  |
| `LTRIM()`      | Removes characters from the left   |
| `RTRIM()`      | Removes characters from the right  |
| `REPLACE()`    | Replaces specified text            |
| `POSITION()`   | Finds substring position           |
| `STRPOS()`     | Finds substring position           |
| `REVERSE()`    | Reverses a string                  |
| `REPEAT()`     | Repeats a string                   |
| `LPAD()`       | Adds characters to the left        |
| `RPAD()`       | Adds characters to the right       |
| `SPLIT_PART()` | Extracts a delimited part          |
| `STRING_AGG()` | Combines values from multiple rows |

## 28. Next Lesson

Next Topic: Mathematical Functions in PostgreSQL

Students will learn how to perform mathematical calculations using `ROUND()`, `CEIL()`, `FLOOR()`, `ABS()`, `POWER()`, `SQRT()`, `MOD()`, and other useful mathematical functions.