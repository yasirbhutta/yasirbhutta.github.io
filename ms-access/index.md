---
title: Microsoft Access Tutorial – Beginner’s Guide to Databases, Forms & Queries 
description: Learn Microsoft Access with step-by-step tutorials for creating databases, tables, queries, forms, and reports. Includes practical examples, templates, and best practices for data design, relationships, normalization, and automation with macros. Perfect for students and professionals learning Access for data management.  
keywords: Microsoft Access tutorial, Access database tutorial, create Access database, Access queries, Access forms and reports, Access macros, database design, Access normalization, Access templates, learn Microsoft Access, Access for beginners
author: Muhammad Yasir Bhutta
---

## 📅 MS Access Weekly Lesson Plan (Beginner Level – 6 Weeks)

**Duration:** 6 Weeks
**Classes per Week:** 2–3
**Class Duration:** 60–90 minutes

---

## 🟢 **Week 1: Introduction & Basics**

### **Lesson 1**

* What is Data and Database?
* What is MS Access?
* Uses of MS Access (real-world examples)
* Difference between Excel and Access

**Activity:**
Identify daily-life databases (school records, library, hospital)

---

### **Lesson 2**

* MS Access Interface
* Creating a New Database
* Saving and Closing Database
* Understanding Database Objects

**Practice:**
Create a blank database named `StudentDB`

---

## 🟢 **Week 2: Tables & Data Types**

### **Lesson 3**

* What is a Table?
* Fields and Records
* Data Types (Short Text, Number, Date, Yes/No)

**Practice:**
Create a table `Students` using Datasheet View

---

### **Lesson 4**

* Design View
* Primary Key
* Field Properties (Required, Field Size)

**Practice:**
Modify `Students` table using Design View

---

## 🟢 **Week 3: Data Entry & Relationships**

### **Lesson 5**

* Entering Records
* Editing and Deleting Data
* Sorting and Filtering Records

**Practice:**
Add at least 10 student records

---

### **Lesson 6**

* What are Relationships?
* One-to-Many Relationship
* Primary Key vs Foreign Key

**Practice:**
Create `Classes` table and relate it with `Students`

---

## 🟢 **Week 4: Queries (Searching Data)**

### **Lesson 7**

* What is a Query?
* Select Query
* Criteria and Sorting

**Practice:**
Query students from a specific class

---

### **Lesson 8**

* Calculated Fields
* Parameter Queries (basic)
* Saving Queries

**Practice:**
Create a query asking for Class Name as input

---

## 🟢 **Week 5: Forms & Reports**

### **Lesson 9**

* What is a Form?
* Creating Forms using Wizard
* Data Entry through Forms

**Practice:**
Create a student entry form

---

### **Lesson 10**

* What is a Report?
* Report Wizard
* Grouping and Sorting

**Practice:**
Generate a printable student report

---

## 🟢 **Week 6: Import/Export & Mini Project**

### **Lesson 11**

* Importing Data from Excel
* Exporting Reports to PDF/Excel
* Backup of Database

**Practice:**
Import student data from Excel

---

### **Lesson 12**

### **Mini Project**

Choose one:

* Student Management System
* Employee Database
* Library Records System

**Requirements:**
✔ 2–3 Tables
✔ Relationships
✔ Queries
✔ Forms
✔ Reports

**Presentation & Review**

---

## 📝 **Assessment Plan**

* Weekly Practical Tasks
* Final Project Evaluation
* Short Quiz / MCQs (Optional)

---

## 🎯 **Learning Outcomes**

By the end of the course, students will be able to:
✔ Create databases
✔ Design tables properly
✔ Use queries for data analysis
✔ Build forms for data entry
✔ Generate reports

---

## MS Access Practice Task

### 📦 What’s included

* **Students.csv** – student records
* **Classes.csv** – class information
* **Teachers.csv** – teacher details
* **README.txt** – step-by-step instructions + practice tasks

👉 **[Download MS Access Practice Files (ZIP)](https://drive.google.com/file/d/1xQfhz7OCCAyqJbld1mbGct-_0EkKpyZN/view?usp=sharing)**

---

## 🧑‍🏫 How to Use These Files (for Students)

1. Open **Microsoft Access**
2. Click **Blank Database**
3. Name it: `SchoolDB.accdb`
4. Go to **External Data → New Data Source → From File → Text File**
5. Import:

   * `Students.csv`
   * `Classes.csv`
   * `Teachers.csv`
6. Set **Primary Keys**:

   * Students → `StudentID`
   * Classes → `ClassID`
   * Teachers → `TeacherID`
7. Create **Relationship**:

   * `Classes.ClassID` → `Students.ClassID`

---

## 📝 Practice Tasks (Beginner Friendly)

### ✅ Tables

* Modify field data types
* Add new records

### ✅ Queries

* Show students of **Class 6th A**
* Sort students by name
* Filter students by gender

### ✅ Forms

* Create a **Student Entry Form**
* Use Form Wizard

### ✅ Reports

* Create a **Student List Report**
* Export report as PDF

---

## 🎯 Suitable For

✔ School students
✔ College beginners
✔ Short IT courses
✔ Teachers (ready classroom material)

---





1	An Introduction to Databases
1.1.	List the advantages of computerizing data.
1.2.	Identify the need for a DBMS
1.3.	Explain the evolution of databases.
1.4.	Discuss the various database models in brief. (A data model can be described as a ‘description’ of the data container and a methodology for storing and retrieving the data.)  
1.5.	Define as RDBMS
1.6.	Explain the concepts of Tables
1.7.	List the features of an RDBMS
1.7.1.	Control Data Redundancy.
1.7.2.	Data Abstraction.
1.7.3.	Support for Multiple users.
1.7.4.	Multiple ways of interfacing to the systems.
1.7.5.	Restricting Unauthorized Access.
1.7.6.	Enforcing Integrity Constraints.
1.7.7.	Backup and Recovery.
1.8.	Identify the users of an RDBMS
1.8.1.	Database Designers.
1.8.2.	Database Administrator
1.8.3.	Application Developer
1.8.4.	End User.
1.9.	Explain the Concept of a ‘Front End’ and ‘Back End’
2	E-R Model.
Designing of Model begins with the database designer and the end user discussing and deciding on the data that is to be stored in the database.
The ‘Entity Relationship Model’ views the entire system as being composed of entities, which are related to one another.
2.1.	Entities (Entity can be used to denote a person, place, thing, object, event or even a concept, which can be distinctly identified. eg: Student
2.2.	Attributes (Each entity has a set of properties or characteristics that define an entities: Rollno, Name, Address
2.3.	Relationship (A Relationship can be defined as an association among entities.
3	The Entity Relationship Diagram (To develop a database model base on the ‘E-R technique’ involves identifying the entities, their attributes as well as the relationships between the entities.)
The symbols used in the ERD are listed below:

Denotes as Entity

Attributes


Relationship between entities.


4	DBMS (A database management system is software that takes care of maintaining the database.
5	Relations, Tuples, Attributes
 A ‘relation’ is synonymous with a ‘table’. A table consists of columns and rows, which are referred to as fields and records in DBMS terms, and attributes and tuples in RDBMS.

 
4	Insert and Delete Fields in a table
5	Working with Fields Properties
5.1.	Format 
5.2.	Input Mask
5.3.	Field Validation
5.4.	Record-level Validation
5.5.	‘Default’ Constraint
5.6.	Required
6	Deleting Records
7	Copying, Renaming and Deleting Tables
8	Keys
8.1.	Primary Key
8.2.	Composite Key
8.3.	Foreign Key
8.4.	Candidate Key/Alternate Key
8.5.	Secondary Key
9	Introduction to SQL
	Based on IBM’s SEQUEL
	New 4GL – SQL
	Access uses variant of SQL called Access-SQL
	ORACLE introduced the first commercially available RDBMS
Introduction to SQL
	Industry standard 
	SQL is categorized into  
		  DDL  (Data Definition Language)
		  DML (Data Manipulation Language)
		  DCL  (Data Control Language)
		  TCL  (Transaction Control 			     language)
	
Data Definition Language
	It is used to create databases objects like 
	Tables 
	Views or Queries
	Other objects
Data Manipulation Language
	It is used to Manipulate Database objects like tables 
	Select, Insert, Update,Delete . 
Data Control Language
	It is used to define control access objects like tables


	Statements include : 
	Alter user ,grant ,revoke


10	Joins
10.1.	Inner Join
10.2.	Outer Join
10.2.1.	Left Outer Join
10.2.2.	Right Outer Join
10.3.	Self Join
11	Creating the ‘Relationships’ between the tables.
11.1.	Join Type
11.2.	Enforce Referential Integrity
11.3.	Cascade Update Related Record
11.4.	Cascade Delete Related Record
12	Working With Queries
12.1.	The Simple Query Wizard
12.2.	Creating a Query in Design View
12.3.	Queries Using Aggregate Functions
12.4.	Subqueries using SQL
13	Create Table Statement
13.1.	Create Table student(CCode  Integer,Name  text(50))
13.2.	
14	Insert Statement
14.1.	INSERT INTO student (Ccode , Name) Values(1,'Adnan')
14.2.	INSERT INTO student  Values(10,'Akbar')
14.3.	INSERT INTO student(CCode) Values(15)
15	Delete Statement
15.1.	Delete * from Student where CCode=10;
16	Update Statement
16.1.	UPDATE Student SET Name='waqas' WHERE  CCode =5
17	Parameter Queries
17.1.	SELECT * FROM student WHERE CCode=[Enter Student Roll No:]
18	Crosstab Queries




