---
layout: page
title: "Date and Time Data Types in PostgreSQL"
description: Learn how to use PostgreSQL date and time data types, including DATE, TIME, TIMESTAMP, TIMESTAMPTZ, and INTERVAL, with practical SQL examples and date/time calculations.
keywords: PostgreSQL date and time data types, DATE, TIME, TIMESTAMP, TIMESTAMPTZ, INTERVAL, PostgreSQL NOW function, date and time arithmetic, PostgreSQL date examples
---

## **1. What are Date and Time Data Types?**

Date and Time data types are used to store dates, times, and durations in a database.

For example:

- Student Date of Birth: 2002-05-15
- Admission Date: 2026-09-01
- Class Time: 08:30:00
- Examination Date and Time: 2026-11-24 09:00:00
- Course Duration: 16 weeks

**Simple definition:**

Date and Time data types specify how PostgreSQL stores and manages dates, times, timestamps, and time intervals.

## **2. Types of Date and Time Data Types**

PostgreSQL provides five main Date and Time data types.

**1. DATE**

Stores date only.

Example: `2026-11-24`

**2. TIME**

Stores time only.

Example: `09:30:00`

**3. TIMESTAMP**

Stores date and time without time zone information.

Example: `2026-11-24 09:30:00`

**4. TIMESTAMPTZ**

Stores a timestamp with time zone handling.

Example: `2026-11-24 09:30:00+05`

**5. INTERVAL**

Stores a duration or period of time.

Example: `2 days`

## **3. DATE – Stores Date Only**

DATE is used to store a calendar date without storing the time.

The standard PostgreSQL date format is:

```
YYYY-MM-DD
```

Where:

- YYYY = Year
- MM = Month
- DD = Day

### **Examples**

| Date       | Meaning          |
| ---------- | ---------------- |
| 2026-01-05 | 5 January 2026   |
| 2026-08-14 | 14 August 2026   |
| 2026-11-24 | 24 November 2026 |

### **Real-life example**

A university stores the date of birth and admission date of students.

```
CREATE TABLE students (
    student_id INTEGER,
    student_name VARCHAR(100),
    date_of_birth DATE,
    admission_date DATE
);
```

Insert records:

```
INSERT INTO students
VALUES
(1, 'Ali', '2002-05-15', '2026-09-01'),
(2, 'Ahmed', '2001-08-20', '2026-09-01');
```

Retrieve records:

```
SELECT * FROM students;
```

**Important points:**

- DATE stores only year, month, and day.
- It does not store hours, minutes, or seconds.
- It is suitable for birthdays, admission dates, examination dates, and deadlines.

## **4. TIME – Stores Time Only**

TIME is used to store time without storing the date.

The standard time format is:

```
HH:MM:SS
```

Where:

- HH = Hours
- MM = Minutes
- SS = Seconds

### **Examples**

| Time     | Meaning |
| -------- | ------- |
| 08:30:00 | 8:30 AM |
| 13:45:00 | 1:45 PM |
| 17:00:00 | 5:00 PM |

### **Real-life example**

A university stores the starting time of classes.

```
CREATE TABLE class_schedule (
    class_id INTEGER,
    course_name VARCHAR(100),
    start_time TIME,
    end_time TIME
);
```

Insert records:

```
INSERT INTO class_schedule
VALUES
(1, 'Database Systems', '08:30:00', '10:00:00'),
(2, 'Programming Fundamentals', '10:15:00', '11:45:00');
```

**Important points:**

- TIME stores hours, minutes, and seconds.
- It does not store a date.
- It is suitable for class schedules, office timings, and daily routines.

## **5. TIMESTAMP – Stores Date and Time**

TIMESTAMP is used when we need to store both date and time together.

It combines DATE and TIME information.

### **Format**

```
YYYY-MM-DD HH:MM:SS
```

### **Example**

```
2026-11-24 09:30:00
```

This means:

- Date: 24 November 2026
- Time: 9:30 AM

### **Real-life example**

Suppose a university wants to record the exact date and time when a student submits an admission application.

```
CREATE TABLE applications (
    application_id INTEGER,
    student_name VARCHAR(100),
    submission_time TIMESTAMP
);
```

Insert record:

```
INSERT INTO applications
VALUES
(1, 'Muhammad Yasir', '2026-11-24 09:30:00');
```

**Important points:**

- TIMESTAMP stores both date and time.
- It does not store or automatically convert between time zones.
- It is suitable for recording events where local date and time are important.

## **6. TIMESTAMPTZ – Timestamp with Time Zone Handling**

TIMESTAMPTZ stands for Timestamp with Time Zone.

It is used to store a point in time with time zone awareness.

For example, a student submits an online application from Pakistan at 10:00 AM.

The same moment may be 5:00 AM in London.

TIMESTAMPTZ helps PostgreSQL represent the same moment correctly across different time zones.

### **Example**

```
CREATE TABLE online_applications (
    application_id INTEGER,
    submission_time TIMESTAMPTZ
);
```

Insert record:

```
INSERT INTO online_applications
VALUES
(1, '2026-11-24 10:00:00+05');
```

Here:

- Date: 24 November 2026
- Time: 10:00 AM
- Time zone offset: +05:00

**Important points:**

- PostgreSQL converts TIMESTAMPTZ values to UTC internally.
- It displays values according to the current session time zone.
- It does not preserve the original time zone name or offset supplied during insertion.
- It is useful for international applications, online transactions, and event logs.

## **7. INTERVAL – Stores Duration of Time**

INTERVAL is used to store a period or duration of time.

For example:

- 2 days
- 3 hours
- 30 minutes
- 6 months
- 2 years

Unlike DATE and TIME, INTERVAL represents the amount of time rather than a specific date or time.

### **Real-life example**

A university course lasts 16 weeks.

```
CREATE TABLE courses (
    course_id INTEGER,
    course_name VARCHAR(100),
    course_duration INTERVAL
);
```

Insert record:

```
INSERT INTO courses
VALUES
(101, 'Database Systems', INTERVAL '16 weeks');
```

Other examples:

```
SELECT
    INTERVAL '2 days' AS duration1,
    INTERVAL '3 hours' AS duration2,
    INTERVAL '30 minutes' AS duration3,
    INTERVAL '6 months' AS duration4;
```

**Important points:**

- INTERVAL stores a duration.
- It can represent years, months, days, hours, minutes, and seconds.
- It is useful for course duration, project deadlines, and time calculations.

## **8. Difference Between DATE, TIME and TIMESTAMP**

This is one of the most important comparisons for students.

| Feature        | DATE | TIME | TIMESTAMP |
| -------------- | ---- | ---- | --------- |
| Stores date    | Yes  | No   | Yes       |
| Stores time    | No   | Yes  | Yes       |
| Stores year    | Yes  | No   | Yes       |
| Stores month   | Yes  | No   | Yes       |
| Stores day     | Yes  | No   | Yes       |
| Stores hours   | No   | Yes  | Yes       |
| Stores minutes | No   | Yes  | Yes       |
| Stores seconds | No   | Yes  | Yes       |

### **Practical comparison**

**Understanding the differences**

DATE

# **2026-11-24**

Only date information.

TIME

# **09:30:00**

Only time information.

TIMESTAMP

# **2026-11-24 09:30:00**

Both date and time information.

**Remember:**

- DATE = When?
- TIME = At what time?
- TIMESTAMP = On which date and at what time?
- INTERVAL = For how long?

## **9. Practical SQL Examples**

### **Example 1: Get the Current Date**

```
SELECT CURRENT_DATE;
```

### **Example 2: Get the Current Time**

```
SELECT CURRENT_TIME;
```

### **Example 3: Get the Current Date and Time**

```
SELECT CURRENT_TIMESTAMP;
```

### **Example 4: Get the Current Timestamp Without Time Zone**

```
SELECT LOCALTIMESTAMP;
```

### **Example 5: Add Days to a Date**

```
SELECT DATE '2026-11-24' + 7;
```

Result:

```
2026-12-01
```

### **Example 6: Calculate Duration Between Two Dates**

```
SELECT DATE '2026-12-01' - DATE '2026-11-24';
```

Result:

```
7
```

The result is the number of days between the two dates.

### **Example 7: Add an Interval to a Date**

```
SELECT DATE '2026-11-24' + INTERVAL '2 months';
```

Result:

```
2027-01-24 00:00:00
```

## **10. Complete Practical Example: University Attendance System**

Let's create a table for recording student attendance.

```
CREATE TABLE student_attendance (
    attendance_id INTEGER,
    student_name VARCHAR(100),
    attendance_date DATE,
    class_start_time TIME,
    check_in TIMESTAMP,
    check_in_zone TIMESTAMPTZ,
    class_duration INTERVAL
);
```

Insert a record:

```
INSERT INTO student_attendance
VALUES (
    1,
    'Ali',
    '2026-11-24',
    '08:45:00',
    '2026-11-24 08:40:00',
    '2026-11-24 08:40:00+05',
    INTERVAL '1 hour 15 minutes'
);
```

Retrieve records:

```
SELECT * FROM student_attendance;
```

### **Understanding the columns**

| Column           | Data type   | Purpose                      |
| ---------------- | ----------- | ---------------------------- |
| attendance_date  | DATE        | Attendance date              |
| class_start_time | TIME        | Class starting time          |
| check_in         | TIMESTAMP   | Local date and check-in time |
| check_in_zone    | TIMESTAMPTZ | Time-zone-aware check-in     |
| class_duration   | INTERVAL    | Class duration               |

## **11. Student Practice Exercise**

Choose the appropriate data type for each field.

| Database field                            | Example                | Suggested data type |
| ----------------------------------------- | ---------------------- | ------------------- |
| Date of birth                             | 2002-05-15             | DATE                |
| Class starting time                       | 08:45:00               | TIME                |
| Admission submission date and time        | 2026-11-24 10:30:00    | TIMESTAMP           |
| Online transaction time across time zones | 2026-11-24 10:30:00+05 | TIMESTAMPTZ         |
| Course duration                           | 16 weeks               | INTERVAL            |
| Examination date                          | 2026-12-15             | DATE                |

**Task:** Create a table named `university_examinations` with the following columns:

1. exam_id
2. subject_name
3. exam_date
4. start_time
5. end_time
6. exam_duration

Select suitable data types and insert at least three examination records.

## **12. Test Your Understanding – MCQs**

**Date and Time Quiz**

7 MCQs

**Q1. Which data type stores only a date?**

A. TIME

B. DATE

C. TIMESTAMP

D. INTERVAL

**Q2. Which data type stores only time?**

A. DATE

B. TIMESTAMP

C. TIME

D. INTERVAL

**Q3. Which data type stores both date and time without time zone handling?**

A. DATE

B. TIME

C. TIMESTAMP

D. INTERVAL

**Q4. Which data type handles time zones?**

A. DATE

B. TIME

C. TIMESTAMPTZ

D. INTERVAL

**Q5. Which data type is suitable for storing a course duration of 16 weeks?**

A. DATE

B. TIME

C. INTERVAL

D. INTEGER

**Q6. What does CURRENT_DATE return?**

A. Current time

B. Current date

C. Current timestamp

D. Current year only

**Q7. What is the result of subtracting one DATE from another DATE?**

A. A timestamp

B. A time zone

C. Number of days

D. A Boolean value

Submit Answers

## **13. Key Points to Remember**

1. DATE stores only dates.
2. TIME stores only time.
3. TIMESTAMP stores date and time without time zone conversion.
4. TIMESTAMPTZ stores a time-zone-aware point in time.
5. INTERVAL stores a duration or period.
6. CURRENT_DATE returns the current date.
7. CURRENT_TIMESTAMP returns the current date and time.
8. Subtracting two DATE values returns the number of days between them.

**Official PostgreSQL Documentation:** [PostgreSQL – Date/Time Types](https://www.postgresql.org/docs/current/datatype-datetime.html?utm_source=chatgpt.com)
