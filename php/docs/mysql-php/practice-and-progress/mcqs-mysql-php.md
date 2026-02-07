---
layout: page
title: "MCQs – PHP and MySQL Integration"
description: MCQs – PHP and MySQL Integration
keywords: MCQs – PHP and MySQL Integration, php, mcqs, mysql
author: Muhammad Yasir Bhutta
course: php
topic: mysql-php
show_toc: false
toc: toc/ms-excel-toc.html
show_practice_progress: false
show_mini_project: false
prev: /ms-excel/docs/functions/what-is-functions.html
next: /ms-excel/docs/functions/sumif.html
breadcrumb: 
- title: Functions
url: /ms-excel/docs/functions.html
---

1. **Which PHP extensions can be used to connect to a MySQL database?**
   a) MySQLi (object-oriented)
   b) MySQLi (procedural)
   c) PDO (PHP Data Objects)
   d) All of the above
   ✅ **Answer:** d) All of the above

2. **Which PHP extension supports multiple database systems besides MySQL?**
   a) MySQLi
   b) PDO
   c) mysql\_connect
   d) mysqli\_connect
   ✅ **Answer:** b) PDO

3. **In PHP, what function is used to terminate the script and output a message upon a connection failure?**
   a) exit()
   b) stop()
   c) die()
   d) terminate()
   ✅ **Answer:** c) die()

4. **What does the `mysqli::connect_error` property return?**
   a) The last executed SQL query
   b) The error message from the last connection attempt
   c) The number of affected rows
   d) The current database name
   ✅ **Answer:** b) The error message from the last connection attempt

5. **Which function is used to perform a query on the database using MySQLi?**
   a) mysqli\_execute()
   b) mysqli\_query()
   c) mysqli\_run()
   d) mysqli\_fetch()
   ✅ **Answer:** b) mysqli\_query()

6. **What does the `mysqli::close` function do?**
   a) Closes the PHP script
   b) Ends the MySQL server process
   c) Closes a previously opened database connection
   d) Deletes the database
   ✅ **Answer:** c) Closes a previously opened database connection

7. **Which of the following is a correct way to create a new MySQLi connection in PHP?**
   a) `new mysqli("localhost", "user", "password");`
   b) `mysqli_connect("localhost", "user", "password");`
   c) Both a and b
   d) None of the above
   ✅ **Answer:** c) Both a and b

8. **What is the default port number for MySQL server connections?**
   a) 3306
   b) 8080
   c) 1433
   d) 1521
   ✅ **Answer:** a) 3306

9. **Which function returns the last error message for the most recent MySQLi function call?**
   a) mysqli::error
   b) mysqli::get\_error
   c) mysqli::last\_error
   d) mysqli::error\_message
   ✅ **Answer:** a) mysqli::error

10. **Which PHP function is used to fetch a result row as an associative array?**
    a) mysqli\_fetch\_row()
    b) mysqli\_fetch\_array()
    c) mysqli\_fetch\_assoc()
    d) mysqli\_fetch\_object()
    ✅ **Answer:** c) mysqli\_fetch\_assoc()

Here are multiple-choice questions (MCQs) based on the content you provided from the “MySQL with PHP: Database Connection Guide & Examples”:

---

### **MCQs: PHP and MySQL Integration**

**1. Which PHP extension supports both object-oriented and procedural styles for MySQL interaction?**
A. PDO
B. MySQL
C. MySQLi
D. SQLite
✅ **Answer: C. MySQLi**

---

**2. Which of the following is a correct function to connect to a MySQL database using MySQLi (object-oriented)?**
A. `mysql_connect()`
B. `mysqli_connect()`
C. `new mysqli()`
D. `pdo_connect()`
✅ **Answer: C. `new mysqli()`**

---

**3. What does the `die()` function do in PHP?**
A. Closes database connection
B. Terminates script execution with an optional message
C. Starts a session
D. Hides PHP errors
✅ **Answer: B. Terminates script execution with an optional message**

---

**4. Which method is used to execute SQL queries using a MySQLi object?**
A. `run()`
B. `query()`
C. `execute()`
D. `fire()`
✅ **Answer: B. `query()`**

---

**5. What does `$conn->connect_error` return?**
A. Error code
B. Last executed query
C. Last connection error message
D. Number of failed queries
✅ **Answer: C. Last connection error message**

---

**6. What is the main difference between `include` and `require` in PHP?**
A. `include` is for HTML, `require` is for PHP
B. `include` gives a fatal error on failure
C. `require` halts script on failure, `include` does not
D. No difference
✅ **Answer: C. `require` halts script on failure, `include` does not**

---

**7. What does `===` do in PHP that `==` does not?**
A. Compares string length
B. Checks both value and data type
C. Compares two arrays
D. Compares the memory address
✅ **Answer: B. Checks both value and data type**

---

**8. Which SQL statement is used to create a new table in MySQL?**
A. `MAKE TABLE`
B. `ADD TABLE`
C. `CREATE TABLE`
D. `NEW TABLE`
✅ **Answer: C. `CREATE TABLE`**

---

**9. Which PHP function is used to execute multiple queries at once?**
A. `mysqli::query()`
B. `mysqli::multi_query()`
C. `mysqli::run()`
D. `mysqli::execute_many()`
✅ **Answer: B. `mysqli::multi_query()`**

---

**10. What does `fetch_assoc()` return?**
A. Indexed array
B. JSON string
C. Associative array
D. Number of rows
✅ **Answer: C. Associative array**

---

