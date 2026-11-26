---
layout: page
title: "Numeric Data Types in PostgreSQL"
description: Learn how to use PostgreSQL numeric data types, including SMALLINT, INTEGER, BIGINT, NUMERIC, DECIMAL, REAL, and DOUBLE PRECISION, with practical SQL examples.
keywords: PostgreSQL numeric data types, SMALLINT, INTEGER, BIGINT, NUMERIC, DECIMAL, REAL, DOUBLE PRECISION, integer vs decimal, PostgreSQL numbers
---

## **1. What are Numeric Data Types?**

Numeric data types are used to store numbers in a database. These numbers may be whole numbers or decimal numbers.

For example:

- Student age: 20
- Total students: 1500
- Semester fee: 45000.50
- Temperature: 36.5
- Percentage: 85.75

PostgreSQL provides different numeric data types depending on the size, accuracy, and type of numbers we want to store.

**Simple definition:**

A numeric data type specifies how PostgreSQL stores and processes numerical values.

## **2. Types of Numeric Data Types in PostgreSQL**

PostgreSQL numeric data types are divided into three main groups.

**1. Whole Number Types (Integer Types)**

- SMALLINT
- INTEGER (INT)
- BIGINT

**2. Exact Decimal Types**

- NUMERIC
- DECIMAL

**3. Approximate Decimal Types**

- REAL
- DOUBLE PRECISION

## **3. Integer Data Types**

Integer data types are used to store whole numbers without decimal points.

For example:

- 10
- 250
- 1500
- -50

PostgreSQL provides three integer data types.

| Data type | Storage | Range                                                |
| --------- | ------- | ---------------------------------------------------- |
| SMALLINT  | 2 bytes | -32,768 to 32,767                                    |
| INTEGER   | 4 bytes | -2,147,483,648 to 2,147,483,647                      |
| BIGINT    | 8 bytes | Approximately -9.22 quintillion to +9.22 quintillion |

**Understanding the differences**

- SMALLINT: Stores relatively small whole numbers.
- INTEGER: Stores medium-sized whole numbers.
- BIGINT: Stores very large whole numbers.

### **Real-life examples**

| Information               | Suitable data type |
| ------------------------- | ------------------ |
| Student age               | SMALLINT           |
| Number of students        | INTEGER            |
| Large transaction counter | BIGINT             |

### **SQL Example**

```
CREATE TABLE students (
    student_id INTEGER,
    age SMALLINT,
    total_marks INTEGER,
    registration_number BIGINT
);
```

**Important:** INTEGER cannot store a decimal fraction.

For example, if we try:

```
INSERT INTO students (student_id, age)
VALUES (1, 20.5);
```

PostgreSQL will return an error because 20.5 is not an integer value.

## **4. NUMERIC and DECIMAL Data Types**

NUMERIC and DECIMAL are used to store exact decimal numbers.

For example:

- 45000.50
- 85.75
- 125.25
- 99.99

They are particularly useful when accuracy is important, such as financial calculations.

### **Syntax**

```
NUMERIC(precision, scale)
```

Here:

- **Precision:** Total number of digits.
- **Scale:** Number of digits after the decimal point.

### **Example: NUMERIC(10,2)**

```
semester_fee NUMERIC(10,2)
```

It means:

- Total digits allowed: 10
- Digits after decimal: 2
- Digits before decimal: 8

**Understanding NUMERIC(10,2)**

# **12345678.90**

# **8**

Digits before decimal

# **2**

Digits after decimal

Total precision = 10 digits

### **SQL Example**

```
CREATE TABLE fee_records (
    student_id INTEGER,
    semester_fee NUMERIC(10,2)
);
```

Insert records:

```
INSERT INTO fee_records
VALUES
(1, 45000.50),
(2, 55000.75),
(3, 60000.00);
```

View records:

```
SELECT * FROM fee_records;
```

**Note:** DECIMAL and NUMERIC are equivalent in PostgreSQL. Both provide exact numeric storage.

## **5. Difference Between INTEGER and NUMERIC**

This is one of the most important differences students should understand.

Consider a university fee record.

- Student age: 22
- Semester fee: 45000.50

Can we use INTEGER for both columns?

No. INTEGER is designed for whole numbers, whereas NUMERIC can store exact decimal values.

### **Comparison**

| Feature               | INTEGER              | NUMERIC                 |
| --------------------- | -------------------- | ----------------------- |
| Stores whole numbers  | Yes                  | Yes                     |
| Stores decimal values | No                   | Yes                     |
| Accuracy              | Exact whole numbers  | Exact decimal numbers   |
| Storage               | Fixed 4 bytes        | Variable                |
| Decimal precision     | Not applicable       | Can be specified        |
| Best use              | Age, count, quantity | Fee, salary, percentage |

### **Practical Example**

**INTEGER vs NUMERIC**

INTEGER

# **45000**

Whole number

NUMERIC(10,2)

# **45000.50**

Decimal number

**Example SQL**

```
CREATE TABLE university_fees (
    student_id INTEGER,
    semester_fee NUMERIC(10,2)
);
```

Here, student_id stores a whole number, while semester_fee stores an exact decimal amount.

### **Can NUMERIC store whole numbers?**

Yes!

NUMERIC can store both whole numbers and decimal numbers.

For example:

```
SELECT
    100::INTEGER AS integer_value,
    100::NUMERIC AS numeric_value;
```

Both values are valid.

**Remember:**

INTEGER = Whole numbers

NUMERIC = Whole numbers + Decimal numbers (with exact precision).

## **6. REAL and DOUBLE PRECISION**

REAL and DOUBLE PRECISION are used to store approximate decimal numbers.

Unlike NUMERIC, these data types do not guarantee exact decimal representation.

| Data type        | Storage | Approximate precision |
| ---------------- | ------- | --------------------- |
| REAL             | 4 bytes | 6 decimal digits      |
| DOUBLE PRECISION | 8 bytes | 15 decimal digits     |

### **Example**

```
CREATE TABLE measurements (
    temperature REAL,
    scientific_value DOUBLE PRECISION
);
```

**When should we use them?**

- REAL: Scientific measurements where moderate precision is sufficient.
- DOUBLE PRECISION: Scientific calculations requiring greater approximate precision.
- NUMERIC: Financial calculations requiring exact decimal values.

## **7. Complete Comparison of Numeric Data Types**

| Data type        | Category            | Example      |
| ---------------- | ------------------- | ------------ |
| SMALLINT         | Integer             | 100          |
| INTEGER          | Integer             | 25000        |
| BIGINT           | Integer             | 9000000000   |
| NUMERIC          | Exact decimal       | 45000.50     |
| DECIMAL          | Exact decimal       | 125.75       |
| REAL             | Approximate decimal | 3.14159      |
| DOUBLE PRECISION | Approximate decimal | 3.1415926535 |

## **8. Practical Exercise**

Create a university student table using appropriate numeric data types.

**Task:** Select suitable data types for these columns.

| Column       | Example value |
| ------------ | ------------- |
| Student ID   | 1001          |
| Age          | 22            |
| Semester Fee | 45000.50      |
| CGPA         | 3.75          |
| Total Marks  | 850           |
| Temperature  | 36.5          |

Suggested SQL solution:

```sql
CREATE TABLE student_records (
    student_id INTEGER,
    age SMALLINT,
    semester_fee NUMERIC(10,2),
    cgpa NUMERIC(3,2),
    total_marks INTEGER,
    temperature REAL
);
```

## **9. Test Your Understanding**

**MCQ Assessment**

6 Questions

**Q1. Which data type stores whole numbers?**

A. NUMERIC

B. INTEGER

C. REAL

D. DOUBLE PRECISION

**Q2. Which data type is best for an exact fee amount of 45000.50?**

A. INTEGER

B. REAL

C. NUMERIC(10,2)

D. SMALLINT

**Q3. How many bytes does INTEGER use?**

A. 2 bytes

B. 4 bytes

C. 8 bytes

D. 16 bytes

**Q4. What does NUMERIC(8,2) mean?**

A. 8 digits after decimal

B. 2 total digits

C. 8 total digits, 2 after decimal

D. 8 bytes

**Q5. Which data type stores approximate decimal values?**

A. INTEGER

B. NUMERIC

C. REAL

D. BIGINT

**Q6. Can NUMERIC store a whole number?**

A. No

B. Yes

C. Only negative numbers

D. Only zero

Submit Answers

## **10. Key Points to Remember**

1. INTEGER stores whole numbers.
2. SMALLINT, INTEGER and BIGINT differ in storage size and range.
3. NUMERIC and DECIMAL store exact decimal values.
4. REAL and DOUBLE PRECISION store approximate decimal values.
5. NUMERIC(10,2) means 10 total digits, including 2 decimal digits.
6. For financial records, NUMERIC is generally preferred over REAL or DOUBLE PRECISION.

**Official documentation:** [PostgreSQL Numeric Types](https://www.postgresql.org/docs/current/datatype-numeric.html)

