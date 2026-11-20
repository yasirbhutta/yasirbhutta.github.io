# Module 1: Introduction to Databases and PostgreSQL

# Lesson 1.1: Introduction to Databases

## 1. What Is Data?

Data refers to raw facts and figures that can be collected, stored, and processed.

Examples of data include:

- Student names
- Roll numbers
- Phone numbers
- Examination marks
- Employee salaries
- Product prices
- Customer addresses

For example:

| Name | Age | Marks |
|---|---:|---:|
| Ali | 20 | 85 |
| Ahmed | 21 | 78 |
| Sara | 19 | 92 |

The names, ages, and marks in this table are examples of data.

## 2. What Is Information?

Information is data that has been processed or organized to make it meaningful and useful.

**Example:**

- Data: 85, 78, 92
- Information: The average marks of three students are 85.

Information helps people understand facts and make decisions.

## 3. Why Do We Need Databases?

Imagine a university with 10,000 students.

The university needs to maintain:

- Student admission records
- Student personal information
- Course details
- Examination results
- Fee records
- Attendance records
- Teacher information

Managing this information manually using paper registers can be difficult.

A database provides an organized way to store, manage, retrieve, and update information.

## 4. Real-Life Examples of Databases

| Organization | Database Usage |
|---|---|
| University | Student and examination records |
| Bank | Customer accounts and transactions |
| Hospital | Patient and medical records |
| Library | Books and member records |
| Shopping Website | Products and customer orders |
| Airline | Flights and passenger reservations |

## 5. Benefits of Using Databases

1. **Organization:** Stores data in an organized way.
2. **Easy Searching:** Helps find required information quickly.
3. **Data Updating:** Allows users to update existing information.
4. **Data Security:** Controls who can access information.
5. **Data Sharing:** Allows authorized users to access shared data.
6. **Data Accuracy:** Constraints can help maintain correct data.
7. **Backup and Recovery:** Helps protect information against data loss.

## 6. Quick Summary

- Data means raw facts and figures.
- Information is meaningful, processed data.
- A database organizes and stores data.
- Databases are used in universities, banks, hospitals, businesses, and many other organizations.

## Practice Questions

1. What is data?
2. What is information?
3. Why do organizations need databases?
4. Give five real-life examples of databases.
5. Write four benefits of using databases.

---








# Lesson 1.10: Introduction to the `dvdrental` Sample Database

## 1. Introduction

The `dvdrental` database is a sample database commonly used for learning and practising PostgreSQL.

It represents a DVD rental business where customers rent films.

It contains sample information about:

- Films
- Actors
- Customers
- Stores
- Staff
- Rentals
- Payments
- Categories

Students can use this database to practise SQL queries with realistic business data.

## 2. Why Do We Use the DVD Rental Database?

Learning SQL requires practical examples.

Instead of working only with small tables containing a few records, students can use `dvdrental` to practise queries involving multiple related tables.

It helps students understand:

1. Database structure.
2. Tables and columns.
3. Primary and foreign keys.
4. Relationships between tables.
5. SQL queries.
6. Data filtering.
7. Sorting and grouping.
8. Aggregate functions.
9. JOIN operations.
10. Reporting and analysis.

## 3. Important Tables in the DVD Rental Database

Some important tables include:

| Table Name | Description |
|---|---|
| actor | Stores actor information |
| film | Stores film information |
| category | Stores film categories |
| customer | Stores customer information |
| rental | Stores rental transactions |
| payment | Stores payment information |
| staff | Stores staff information |
| store | Stores store information |
| inventory | Stores film inventory |
| language | Stores language information |

## 4. Understanding the Database Structure

The `dvdrental` database contains related tables.

For example:

- The `film` table stores information about films.
- The `actor` table stores information about actors.
- The `customer` table stores information about customers.
- The `rental` table stores rental transactions.
- The `payment` table stores payment transactions.

These tables are connected through relationships.

For example, a rental record identifies the customer and the inventory item involved in a rental.



---

# Module 1: Final Review

## A. Short Questions

1. What is data?
2. Differentiate between data and information.
3. Define a database.
4. What is a DBMS?
5. What is an RDBMS?
6. What is PostgreSQL?
7. What is SQL?
8. What is pgAdmin?
9. What is psql?
10. What is a relational database?
11. What is a primary key?
12. What is a foreign key?
13. What is a table?
14. What is a row?
15. What is a column?
16. What is a record?
17. What is the purpose of the `dvdrental` database?
18. Name five tables from the DVD Rental database.

## B. Multiple Choice Questions

**1. What does DBMS stand for?**

A. Database Management System  
B. Data Backup Management System  
C. Database Monitoring Software  
D. Data Management Service

**2. Which of the following is an open-source relational DBMS?**

A. Microsoft Word  
B. PostgreSQL  
C. PowerPoint  
D. Notepad

**3. Which language is used to communicate with relational databases?**

A. HTML  
B. CSS  
C. SQL  
D. XML

**4. A table consists of:**

A. Rows and columns  
B. Images and videos  
C. Files and folders  
D. Programs and functions

**5. What is another name for a row?**

A. Field  
B. Record  
C. Database  
D. Schema

**6. Which PostgreSQL tool provides a graphical interface?**

A. psql  
B. pgAdmin  
C. pg_dump  
D. pg_restore

**7. Which key uniquely identifies a row in a table?**

A. Foreign Key  
B. Primary Key  
C. Default Key  
D. Secondary Key

**8. Which table stores film information in the DVD Rental database?**

A. customer  
B. rental  
C. film  
D. payment

**9. Which SQL command retrieves data from a table?**

A. INSERT  
B. DELETE  
C. SELECT  
D. UPDATE

**10. Which of the following is a database management system?**

A. PostgreSQL  
B. Google Chrome  
C. Microsoft Paint  
D. Windows Explorer

## C. Practical Activities

**Activity 1: Explore PostgreSQL**

1. Open pgAdmin.
2. Connect to your PostgreSQL server.
3. Explore the available databases.
4. Identify the `postgres` database.
5. Open the Query Tool.
6. Execute:

```sql
SELECT version();
```

**Activity 2: Explore DVD Rental**

1. Open the `dvdrental` database.
2. Explore the `public` schema.
3. Identify at least five tables.
4. Open the `film` table.
5. View the first 10 records.

**Activity 3: Identify Database Components**

Choose any three tables from `dvdrental` and identify:

- Table name
- Column names
- Number of columns
- Primary key
- Foreign keys, where applicable

---

# Module 1: Key Takeaways

By completing this module, students should understand:

- What data and information mean.
- Why databases are important.
- What a DBMS and RDBMS are.
- How relational databases organize data.
- What PostgreSQL is and why it is used.
- The basic features and advantages of PostgreSQL.
- Common database tasks.
- How to use pgAdmin and psql.
- The difference between tables, rows, columns, and records.
- How to explore the `dvdrental` sample database.

**Next Module:** Module 2 – Database Management

In the next module, students will learn how to create, connect to, view, rename, and delete databases in PostgreSQL.
