# Student Notes: Date and Time Functions in PostgreSQL

## 1. Introduction

Imagine a university database that stores student admission dates, fee payment dates, examination dates, and attendance records.

The university may need to perform different tasks:

- Display the current date and time.
- Find students admitted in a particular year.
- Extract the month or year from a date.
- Calculate the number of days between two dates.
- Add days or months to a date.
- Format dates in a particular style.
- Calculate a student's age from their date of birth.

PostgreSQL provides Date and Time Functions to perform these operations.

## 2. Date and Time Data Types in PostgreSQL

Before learning date and time functions, understand the commonly used date and time data types.

| Data Type     | Description                                  | Example                  |
| ------------- | -------------------------------------------- | ------------------------ |
| `DATE`        | Stores date only                             | `2026-11-09`             |
| `TIME`        | Stores time only                             | `14:30:00`               |
| `TIMESTAMP`   | Stores date and time without time zone       | `2026-11-09 14:30:00`    |
| `TIMESTAMPTZ` | Stores date and time with time zone handling | `2026-11-09 14:30:00+05` |
| `INTERVAL`    | Stores a duration or time period             | `2 days`                 |

### Examples

```
SELECT DATE '2026-11-09';

SELECT TIME '14:30:00';

SELECT TIMESTAMP '2026-11-09 14:30:00';

SELECT INTERVAL '5 days';
```

## 3. Display Current Date

The `CURRENT_DATE` keyword returns the current date according to the database session's date and time settings.

### Syntax

```
SELECT CURRENT_DATE;
```

Example output:

```
2026-11-09
```

The actual output depends on the date when the query is executed.

## 4. Display Current Time

The `CURRENT_TIME` keyword returns the current time with time zone information.

### Syntax

```
SELECT CURRENT_TIME;
```

Example output:

```
16:10:25.123+05
```

The actual output changes whenever the query is executed.

## 5. Display Current Date and Time

PostgreSQL provides different ways to retrieve the current date and time.

### 5.1 NOW()

`NOW()` returns the current transaction's starting date and time, including time zone information.

```
SELECT NOW();
```

### 5.2 CURRENT_TIMESTAMP

```
SELECT CURRENT_TIMESTAMP;
```

This also returns the current transaction's starting timestamp with time zone information.

### 5.3 LOCALTIMESTAMP

```
SELECT LOCALTIMESTAMP;
```

Returns the current transaction's starting date and time without time zone information.

### Difference

| Function            | Returns                                         |
| ------------------- | ----------------------------------------------- |
| `CURRENT_DATE`      | Current date                                    |
| `CURRENT_TIME`      | Current time with time zone                     |
| `NOW()`             | Current transaction timestamp with time zone    |
| `CURRENT_TIMESTAMP` | Current transaction timestamp with time zone    |
| `LOCALTIMESTAMP`    | Current transaction timestamp without time zone |

Important: `NOW()` and `CURRENT_TIMESTAMP` do not continuously change during a transaction. They return the transaction's starting time.

## 6. Create a Sample Students Table

We will use a students table to understand date functions.

### Step 1: Create the Table

```
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    department VARCHAR(50),
    admission_date DATE,
    date_of_birth DATE
);
```

### Step 2: Insert Sample Records

```
INSERT INTO students
VALUES
(1, 'Ali', 'Computer Science', '2024-09-10', '2005-03-15'),
(2, 'Sara', 'Mathematics', '2023-08-15', '2004-07-20'),
(3, 'Ahmed', 'Physics', '2025-01-20', '2006-11-05'),
(4, 'Hina', 'Computer Science', '2024-02-12', '2005-12-25'),
(5, 'Usman', 'Mathematics', '2025-09-01', '2006-05-10');
```

### Step 3: Display Records

```
SELECT *
FROM students;
```

Expected output:

| student_id | student_name | department       | admission_date | date_of_birth |
| ---------- | ------------ | ---------------- | -------------- | ------------- |
| 1          | Ali          | Computer Science | 2024-09-10     | 2005-03-15    |
| 2          | Sara         | Mathematics      | 2023-08-15     | 2004-07-20    |
| 3          | Ahmed        | Physics          | 2025-01-20     | 2006-11-05    |
| 4          | Hina         | Computer Science | 2024-02-12     | 2005-12-25    |
| 5          | Usman        | Mathematics      | 2025-09-01     | 2006-05-10    |

## 7. EXTRACT() Function

The `EXTRACT()` function retrieves a specific part of a date or timestamp.

For example:

- Year
- Month
- Day
- Hour
- Minute
- Second

### Syntax

```
EXTRACT(field FROM source);
```

### Example 1: Extract Year

```
SELECT
    student_name,
    admission_date,
    EXTRACT(YEAR FROM admission_date) AS admission_year
FROM students;
```

### Example 2: Extract Month

```
SELECT
    student_name,
    admission_date,
    EXTRACT(MONTH FROM admission_date) AS admission_month
FROM students;
```

### Example 3: Extract Day

```
SELECT
    student_name,
    admission_date,
    EXTRACT(DAY FROM admission_date) AS admission_day
FROM students;
```

### Common EXTRACT Fields

| Field     | Description              |
| --------- | ------------------------ |
| `YEAR`    | Extracts year            |
| `MONTH`   | Extracts month           |
| `DAY`     | Extracts day of month    |
| `HOUR`    | Extracts hour            |
| `MINUTE`  | Extracts minute          |
| `SECOND`  | Extracts second          |
| `QUARTER` | Extracts quarter of year |
| `DOW`     | Day of week (Sunday = 0) |
| `ISODOW`  | Day of week (Monday = 1) |
| `DOY`     | Day of year              |
| `WEEK`    | ISO week number          |

Example:

```
SELECT
    EXTRACT(YEAR FROM CURRENT_DATE) AS current_year,
    EXTRACT(MONTH FROM CURRENT_DATE) AS current_month,
    EXTRACT(DAY FROM CURRENT_DATE) AS current_day;
```

## 8. DATE_PART() Function

`DATE_PART()` also extracts a particular part of a date or timestamp.

### Syntax

```
DATE_PART('field', source);
```

### Example: Extract Year

```
SELECT
    student_name,
    DATE_PART('year', admission_date) AS admission_year
FROM students;
```

### Example: Extract Month

```
SELECT
    student_name,
    DATE_PART('month', admission_date) AS admission_month
FROM students;
```

Difference: `EXTRACT()` uses SQL-standard syntax, while `DATE_PART()` uses a function with a text field argument. Both can be used to extract date and time components.

## 9. AGE() Function

The `AGE()` function calculates the difference between two dates or timestamps as an interval.

It is useful for calculating a person's age or the duration between two dates.

### Syntax

```
AGE(end_date, start_date);
```

### Example 1: Calculate Age

```
SELECT
    student_name,
    date_of_birth,
    AGE(CURRENT_DATE, date_of_birth) AS student_age
FROM students;
```

The result is displayed in years, months, and days.

### Example 2: Calculate Difference Between Two Dates

```
SELECT AGE(
    DATE '2026-11-09',
    DATE '2020-01-01'
);
```

Example result:

```
6 years 10 mons 8 days
```

Note: The result is an interval, not a simple number of days.

## 10. Subtract Dates

We can subtract one DATE value from another to calculate the number of days between them.

### Syntax

```
date1 - date2;
```

### Example

```
SELECT
    DATE '2026-11-09' - DATE '2026-11-01' AS total_days;
```

Expected output:

| total_days |
| ---------- |
| 8          |

### Example: Calculate Days Since Admission

```
SELECT
    student_name,
    admission_date,
    CURRENT_DATE - admission_date AS days_since_admission
FROM students;
```

This calculates the number of days between each student's admission date and the current date.

## 11. Add Days to a Date

We can add a number of days to a date using the `+` operator.

### Example

```
SELECT DATE '2026-11-09' + 10 AS new_date;
```

Expected output:

```
2026-11-19
```

### Example: Add Days to Admission Date

```
SELECT
    student_name,
    admission_date,
    admission_date + 30 AS next_date
FROM students;
```

This calculates the date 30 days after each student's admission date.

## 12. Subtract Days from a Date

We can subtract days using the `-` operator.

### Example

```
SELECT DATE '2026-11-09' - 5 AS previous_date;
```

Expected output:

```
2026-11-04
```

### Example: Calculate a Date Before Admission

```
SELECT
    student_name,
    admission_date,
    admission_date - 7 AS previous_date
FROM students;
```

This calculates the date seven days before each student's admission date.

## 13. Add Months and Years Using INTERVAL

PostgreSQL uses `INTERVAL` to add or subtract periods of time.

### Example 1: Add Months

```
SELECT
    DATE '2026-11-09' + INTERVAL '2 months' AS new_date;
```

### Example 2: Add Years

```
SELECT
    DATE '2026-11-09' + INTERVAL '1 year' AS new_date;
```

### Example 3: Subtract Months

```
SELECT
    DATE '2026-11-09' - INTERVAL '3 months' AS previous_date;
```

### Common INTERVAL Values

| Interval       | Meaning         |
| -------------- | --------------- |
| `'5 days'`     | Five days       |
| `'2 weeks'`    | Two weeks       |
| `'3 months'`   | Three months    |
| `'1 year'`     | One year        |
| `'4 hours'`    | Four hours      |
| `'30 minutes'` | Thirty minutes  |
| `'15 seconds'` | Fifteen seconds |

## 14. TO_CHAR() Function

The `TO_CHAR()` function converts a date or timestamp into formatted text.

It is useful when we want to display dates in a particular format.

### Syntax

```
TO_CHAR(date_value, 'format');
```

### Example 1: Display Date as DD-MM-YYYY

```
SELECT
    student_name,
    TO_CHAR(admission_date, 'DD-MM-YYYY') AS formatted_date
FROM students;
```

Example output:

| student_name | formatted_date |
| ------------ | -------------- |
| Ali          | 10-09-2024     |
| Sara         | 15-08-2023     |
| Ahmed        | 20-01-2025     |

### Example 2: Display Month Name

```
SELECT
    student_name,
    TO_CHAR(admission_date, 'DD Month YYYY') AS formatted_date
FROM students;
```

### Common TO_CHAR() Format Patterns

| Format  | Meaning                   | Example  |
| ------- | ------------------------- | -------- |
| `DD`    | Day                       | 09       |
| `MM`    | Month number              | 11       |
| `YYYY`  | Four-digit year           | 2026     |
| `YY`    | Two-digit year            | 26       |
| `Month` | Full month name, padded   | November |
| `Mon`   | Short month name          | Nov      |
| `Day`   | Full weekday name, padded | Monday   |
| `Dy`    | Short weekday name        | Mon      |
| `HH24`  | Hour in 24-hour format    | 16       |
| `HH12`  | Hour in 12-hour format    | 04       |
| `MI`    | Minute                    | 30       |
| `SS`    | Second                    | 25       |

## 15. TO_DATE() Function

The `TO_DATE()` function converts a text value into a DATE value using a specified format.

### Syntax

```
TO_DATE(text_value, 'format');
```

### Example 1

```
SELECT TO_DATE('09-11-2026', 'DD-MM-YYYY');
```

Expected output:

```
2026-11-09
```

### Example 2

```
SELECT TO_DATE('15/08/2025', 'DD/MM/YYYY');
```

Expected output:

```
2025-08-15
```

Important: `TO_DATE()` is used for converting text into dates. It does not simply change the display format of an existing DATE value.

## 16. TO_TIMESTAMP() Function

The `TO_TIMESTAMP()` function converts text into a timestamp with time zone information.

### Syntax

```
TO_TIMESTAMP(text_value, 'format');
```

### Example

```
SELECT TO_TIMESTAMP(
    '09-11-2026 16:30:00',
    'DD-MM-YYYY HH24:MI:SS'
);
```

This converts the supplied text into a timestamp value.

## 17. DATE_TRUNC() Function

`DATE_TRUNC()` removes smaller parts of a timestamp and keeps the specified date or time level.

It is useful when grouping or reporting data by year, month, or day.

### Syntax

```
DATE_TRUNC('field', timestamp_value);
```

### Example 1: Start of Year

```
SELECT DATE_TRUNC(
    'year',
    TIMESTAMP '2026-11-09 16:30:45'
);
```

Result:

```
2026-01-01 00:00:00
```

### Example 2: Start of Month

```
SELECT DATE_TRUNC(
    'month',
    TIMESTAMP '2026-11-09 16:30:45'
);
```

Result:

```
2026-11-01 00:00:00
```

### Example 3: Start of Day

```
SELECT DATE_TRUNC(
    'day',
    TIMESTAMP '2026-11-09 16:30:45'
);
```

Result:

```
2026-11-09 00:00:00
```

### Common DATE_TRUNC Fields

| Field     | Purpose              |
| --------- | -------------------- |
| `year`    | Beginning of year    |
| `quarter` | Beginning of quarter |
| `month`   | Beginning of month   |
| `week`    | Beginning of week    |
| `day`     | Beginning of day     |
| `hour`    | Beginning of hour    |
| `minute`  | Beginning of minute  |
| `second`  | Beginning of second  |

## 18. EXTRACT() with WHERE Clause

We can use date functions with the WHERE clause to filter records.

### Example 1: Find Students Admitted in 2024

```
SELECT *
FROM students
WHERE EXTRACT(YEAR FROM admission_date) = 2024;
```

### Example 2: Find Students Admitted in September

```
SELECT *
FROM students
WHERE EXTRACT(MONTH FROM admission_date) = 9;
```

### Example 3: Find Students Born After 2005

```
SELECT *
FROM students
WHERE date_of_birth >= DATE '2006-01-01';
```

Performance tip: For filtering a date range, direct comparisons are often more efficient than applying a function to the date column.

For example, to find admissions during 2024:

```
SELECT *
FROM students
WHERE admission_date >= DATE '2024-01-01'
  AND admission_date < DATE '2025-01-01';
```

## 19. Generate a Series of Dates

PostgreSQL provides `GENERATE_SERIES()` to generate a sequence of values.

We can use it to generate a list of dates.

### Example: Generate Seven Consecutive Dates

```
SELECT GENERATE_SERIES(
    DATE '2026-11-01',
    DATE '2026-11-07',
    INTERVAL '1 day'
)::DATE AS calendar_date;
```

Expected output:

| calendar_date |
| ------------- |
| 2026-11-01    |
| 2026-11-02    |
| 2026-11-03    |
| 2026-11-04    |
| 2026-11-05    |
| 2026-11-06    |
| 2026-11-07    |

This function is useful for creating calendars, attendance reports, and date-based reports.

## 20. Date Functions with GROUP BY

We can combine date functions with GROUP BY to prepare reports.

Suppose we want to count students admitted in each year.

```
SELECT
    EXTRACT(YEAR FROM admission_date) AS admission_year,
    COUNT(*) AS total_students
FROM students
GROUP BY EXTRACT(YEAR FROM admission_date)
ORDER BY admission_year;
```

Similarly, we can calculate monthly admissions:

```
SELECT
    EXTRACT(YEAR FROM admission_date) AS admission_year,
    EXTRACT(MONTH FROM admission_date) AS admission_month,
    COUNT(*) AS total_students
FROM students
GROUP BY
    EXTRACT(YEAR FROM admission_date),
    EXTRACT(MONTH FROM admission_date)
ORDER BY admission_year, admission_month;
```

## 21. Important Points to Remember

1. `DATE` stores date values.
2. `TIME` stores time values.
3. `TIMESTAMP` stores date and time without time zone.
4. `TIMESTAMPTZ` stores an instant with time zone handling.
5. `CURRENT_DATE` returns the current date.
6. `NOW()` returns the current transaction timestamp.
7. `EXTRACT()` retrieves a specific part of a date or timestamp.
8. `AGE()` calculates the difference between dates as an interval.
9. Subtracting two DATE values returns the number of days between them.
10. `INTERVAL` represents a duration.
11. `TO_CHAR()` formats a date or timestamp as text.
12. `TO_DATE()` converts text into a date.
13. `TO_TIMESTAMP()` converts text into a timestamp.
14. `DATE_TRUNC()` reduces a date or timestamp to a specified level.
15. `GENERATE_SERIES()` can generate a sequence of dates.

## 22. Practice Exercises

### Beginner Level

1. Display the current date using PostgreSQL.
2. Display the current time.
3. Display the current date and time.
4. Extract the year from each student's admission date.
5. Extract the month from each student's date of birth.
6. Display student names and admission dates in DD-MM-YYYY format.

### Intermediate Level

7. Find students admitted in 2024.
8. Find students admitted in September.
9. Calculate the number of days since each student's admission.
10. Add 30 days to every student's admission date.
11. Calculate the age of each student using `AGE()`.
12. Calculate department-wise admissions using GROUP BY and EXTRACT().
13. Find students born after 1 January 2005.

### Advanced Level

14. Display the first day of the admission month for each student using DATE_TRUNC().
15. Generate all dates for the month of November 2026.
16. Calculate monthly student admissions.
17. Calculate the number of years between two given dates.
18. Find students admitted within the last 365 days.
19. Convert the text `'25/12/2026'` into a DATE value.
20. Generate a calendar of all dates between two given dates.

## 23. Review Questions

1. What is the difference between DATE and TIMESTAMP?
2. What is the purpose of CURRENT_DATE?
3. What does NOW() return?
4. What is the purpose of EXTRACT()?
5. What is the difference between EXTRACT() and DATE_PART()?
6. What does AGE() calculate?
7. What is the purpose of INTERVAL?
8. What is the difference between TO_CHAR() and TO_DATE()?
9. What does DATE_TRUNC() do?
10. What is the purpose of GENERATE_SERIES()?
11. How can we calculate the number of days between two dates?
12. How can we count monthly admissions using GROUP BY?

## 24. Quick Revision

| Function / Keyword  | Purpose                                   |
| ------------------- | ----------------------------------------- |
| `CURRENT_DATE`      | Returns current date                      |
| `CURRENT_TIME`      | Returns current time                      |
| `NOW()`             | Returns current transaction timestamp     |
| `CURRENT_TIMESTAMP` | Returns current transaction timestamp     |
| `LOCALTIMESTAMP`    | Returns timestamp without time zone       |
| `EXTRACT()`         | Extracts date/time components             |
| `DATE_PART()`       | Extracts date/time components             |
| `AGE()`             | Calculates date difference as an interval |
| `INTERVAL`          | Represents a duration                     |
| `TO_CHAR()`         | Converts date/time into formatted text    |
| `TO_DATE()`         | Converts text into DATE                   |
| `TO_TIMESTAMP()`    | Converts text into TIMESTAMPTZ            |
| `DATE_TRUNC()`      | Truncates date/time to a specified level  |
| `GENERATE_SERIES()` | Generates a sequence of values            |

## 25. Next Lesson

Next Topic: String Functions in PostgreSQL

Students will learn how to manipulate text using `UPPER()`, `LOWER()`, `LENGTH()`, `CONCAT()`, `SUBSTRING()`, `TRIM()`, `REPLACE()`, and other useful string functions.