---
layout: page
title: "PostgreSQL Roles & Permissions Lab Exercise | GRANT REVOKE Hands-On Practice"
description: Hands-on lab exercise to learn PostgreSQL role management, GRANT and REVOKE permissions, role-based access control with practical examples using admin, teacher, and student roles.
keywords: PostgreSQL roles lab, GRANT REVOKE permissions, role-based access control, PostgreSQL permissions exercise, CREATE ROLE, SET ROLE, PostgreSQL user permissions, hands-on lab
toc: toc/postgresql.html
topic: postgresql
breadcrumb: 
- title: PostgreSQL
  url: /postgresql/
---

## 🎯 Objective

By the end of this lab, students will be able to:

* Create roles (users)
* Assign permissions
* Use `GRANT` and `REVOKE`
* Understand role-based access control

---

# 🏫 Scenario

You are managing a **University Database System** with:

* Admin
* Teacher
* Students

---

# 🔹 Step 1: Create Database

```sql
CREATE DATABASE university_lab;
```

Connect to it:

```sql
\c university_lab
```

---

# 🔹 Step 2: Create Sample Table

```sql
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    course VARCHAR(50)
);
```

Insert sample data:

```sql
INSERT INTO students (name, course)
VALUES 
('Ali', 'CS'),
('Sara', 'IT'),
('Ahmed', 'SE');
```

---

# 🔹 Step 3: Create Roles

### 👨‍💼 Admin Role

```sql
CREATE ROLE admin_user WITH LOGIN PASSWORD 'admin123' SUPERUSER;
```

### 👨‍🏫 Teacher Role

```sql
CREATE ROLE teacher WITH LOGIN PASSWORD 'teacher123';
```

### 👨‍🎓 Student Role

```sql
CREATE ROLE student WITH LOGIN PASSWORD 'student123';
```

---

# 🔹 Step 4: Grant Permissions

### Teacher Permissions (Read + Insert)

```sql
GRANT SELECT, INSERT ON students TO teacher;
```

### Student Permissions (Read Only)

```sql
GRANT SELECT ON students TO student;
```

---

# 🔹 Step 5: Test Roles

Switch role:

```sql
SET ROLE teacher;
```

Try:

```sql
SELECT * FROM students;
INSERT INTO students (name, course) VALUES ('Zain', 'AI');
```

Now test student:

```sql
SET ROLE student;
```

Try:

```sql
SELECT * FROM students;
INSERT INTO students (name, course) VALUES ('Test', 'CS'); -- Should FAIL
```

---

# 🔹 Step 6: Revoke Permission

```sql
REVOKE INSERT ON students FROM teacher;
```

---

# 📝 Lab Tasks

### ✅ Task 1:

Create a new role:

```text
librarian
```

* Can only **SELECT** data

---

### ✅ Task 2:

Create a new table:

```text
books (id, title, author)
```

Give:

* Teacher → SELECT, INSERT
* Student → SELECT only

---

### ✅ Task 3:

Test access using `SET ROLE`

---

### ✅ Task 4:

Revoke SELECT from student and test again

---

# 🎯 Challenge

* Create a **group role**:

```text
staff_group
```

* Assign teacher to it
* Grant permissions to group instead of individual users

---

