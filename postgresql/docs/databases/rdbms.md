# Lesson 1.4: Introduction to Relational Databases

## 1. What Is a Relational Database?

A relational database is a type of database that organizes data into tables.

These tables can be connected through relationships using common columns, such as IDs.

In simple words:

**A relational database stores data in tables and allows related tables to be connected.**

## 2. Understanding Tables

Consider a university database with a table named `students`.

### Students Table

| student_id | student_name | department_id |
|---:|---|---:|
| 101 | Ali | 1 |
| 102 | Ahmed | 2 |
| 103 | Sara | 1 |
| 104 | Ayesha | 3 |

Another table stores department information.

### Departments Table

| department_id | department_name |
|---:|---|
| 1 | Computer Science |
| 2 | Mathematics |
| 3 | English |

## 3. Understanding Relationships

The `department_id` column is used to connect the two tables.

For example:

- Ali belongs to Computer Science.
- Ahmed belongs to Mathematics.
- Sara belongs to Computer Science.
- Ayesha belongs to English.

Instead of repeating the complete department name in every student record, the database stores the department ID.

This makes it easier to organize related information.

## 4. Primary Key

A primary key is a column or combination of columns that uniquely identifies each row in a table.

Example:

In the `students` table, `student_id` can be the primary key.

Each student must have a unique ID.

## 5. Foreign Key

A foreign key is a column or combination of columns that refers to a primary key or other unique key in another table.

Example:

The `department_id` column in the `students` table can be a foreign key referencing `department_id` in the `departments` table.

## 6. Common Types of Relationships

### One-to-One

One record in one table is associated with one record in another table.

Example: One person and one passport record.

### One-to-Many

One record in one table can be associated with multiple records in another table.

Example: One department can have many students.

### Many-to-Many

Multiple records in one table can be associated with multiple records in another table.

Example: Many students can enroll in many courses.

A junction table is commonly used to represent a many-to-many relationship.

## 7. Advantages of Relational Databases

- Organizes information into tables.
- Reduces unnecessary data duplication.
- Supports relationships between tables.
- Maintains data integrity using constraints.
- Supports SQL queries.
- Makes reporting and data analysis easier.

## 8. Quick Summary

- A relational database stores information in tables.
- Tables contain rows and columns.
- Primary keys uniquely identify records.
- Foreign keys establish relationships between tables.
- Common relationships include one-to-one, one-to-many, and many-to-many.

## Practice Questions

1. What is a relational database?
2. What is a table?
3. Define primary key.
4. Define foreign key.
5. Explain one-to-one, one-to-many, and many-to-many relationships.
6. Identify the primary and foreign keys in the given example.

---
