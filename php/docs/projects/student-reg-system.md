---
layout: page
title: "PHP Projects for Beginners: Student Registration System"
description: Learn PHP basics with this beginner-friendly guide. Understand PHP syntax, variables, functions, and more to start building dynamic web applications.
keywords: PHP basics, PHP tutorial, PHP for beginners, PHP syntax, PHP variables, PHP functions, learn PHP, PHP fundamentals, PHP programming
toc: toc/php.html
course: php
topic: "basics"
mini_project: true
next: /php/docs/basics/what-is-php.html
---

## **Project Title:** Student Registration System  

## **Objective:**  
To create a student registration system where students can register, and admins can view, edit, or delete student records. This project will integrate:  
- **PHP** (Form handling, database operations)  
- **HTML** (Registration form, display page)  
- **CSS** (Styling the forms and tables)  
- **MySQL** (Database storage)  

---

## **Features:**  
1. **Student Registration Form**  
   - Input fields: Name, Email, Phone, Course, Password  
   - Form validation (client-side & server-side)  
   - Success/error messages  

2. **Admin Dashboard**  
   - View all registered students  
   - Edit student details  
   - Delete a student  

3. **Responsive Design (CSS)**  
   - Clean, modern UI  
   - Mobile-friendly layout  

---

## **Implementation Steps:**  

### **1. Database Setup (MySQL)**
```sql
CREATE DATABASE student_db;
USE student_db;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15),
    course VARCHAR(50),
    password VARCHAR(255) NOT NULL,
    reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### **2. `config.php` (Database Connection)**
```php
<?php
$host = "localhost";
$user = "root";
$pass = "";
$db = "student_db";

$conn = new mysqli($host, $user, $pass, $db);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>
```

### **3. `register.php` (Student Registration Form - HTML & PHP)**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Registration</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f4f9;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 500px;
            margin: 0 auto;
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            text-align: center;
            color: #333;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input, select {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        button {
            background: #28a745;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 4px;
            cursor: pointer;
            width: 100%;
        }
        button:hover {
            background: #218838;
        }
        .error {
            color: red;
            font-size: 14px;
        }
        .success {
            color: green;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Student Registration</h1>
        <?php
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            include 'config.php';
            
            $name = $_POST['name'];
            $email = $_POST['email'];
            $phone = $_POST['phone'];
            $course = $_POST['course'];
            $password = password_hash($_POST['password'], PASSWORD_DEFAULT);

            $sql = "INSERT INTO students (name, email, phone, course, password) 
                    VALUES ('$name', '$email', '$phone', '$course', '$password')";
            
            if ($conn->query($sql) {
                echo "<p class='success'>Registration successful!</p>";
            } else {
                echo "<p class='error'>Error: " . $conn->error . "</p>";
            }
        }
        ?>
        <form method="POST" action="">
            <div class="form-group">
                <label for="name">Full Name</label>
                <input type="text" name="name" required>
            </div>
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="phone">Phone</label>
                <input type="text" name="phone">
            </div>
            <div class="form-group">
                <label for="course">Course</label>
                <select name="course" required>
                    <option value="Computer Science">Computer Science</option>
                    <option value="Engineering">Engineering</option>
                    <option value="Business">Business</option>
                </select>
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" name="password" required>
            </div>
            <button type="submit">Register</button>
        </form>
    </div>
</body>
</html>
```

### **4. `students.php` (Admin Dashboard - View/Edit/Delete)**
```php
<?php include 'config.php'; ?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Manage Students</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background: #f4f4f9;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }
        th, td {
            padding: 10px;
            border: 1px solid #ddd;
            text-align: left;
        }
        th {
            background: #007bff;
            color: white;
        }
        tr:nth-child(even) {
            background: #f2f2f2;
        }
        .action-buttons a {
            padding: 5px 10px;
            text-decoration: none;
            margin-right: 5px;
            border-radius: 3px;
        }
        .edit-btn {
            background: #ffc107;
            color: black;
        }
        .delete-btn {
            background: #dc3545;
            color: white;
        }
    </style>
</head>
<body>
    <h1>Registered Students</h1>
    <table>
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Phone</th>
            <th>Course</th>
            <th>Actions</th>
        </tr>
        <?php
        $sql = "SELECT * FROM students";
        $result = $conn->query($sql);
        
        if ($result->num_rows > 0) {
            while ($row = $result->fetch_assoc()) {
                echo "<tr>
                    <td>{$row['id']}</td>
                    <td>{$row['name']}</td>
                    <td>{$row['email']}</td>
                    <td>{$row['phone']}</td>
                    <td>{$row['course']}</td>
                    <td class='action-buttons'>
                        <a href='edit.php?id={$row['id']}' class='edit-btn'>Edit</a>
                        <a href='delete.php?id={$row['id']}' class='delete-btn'>Delete</a>
                    </td>
                </tr>";
            }
        } else {
            echo "<tr><td colspan='6'>No students registered yet.</td></tr>";
        }
        ?>
    </table>
</body>
</html>
```

### **5. `edit.php` (Edit Student Details)**
```php
<?php
include 'config.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $id = $_POST['id'];
    $name = $_POST['name'];
    $email = $_POST['email'];
    $phone = $_POST['phone'];
    $course = $_POST['course'];

    $sql = "UPDATE students SET name='$name', email='$email', phone='$phone', course='$course' WHERE id=$id";
    $conn->query($sql);
    header("Location: students.php");
}

$id = $_GET['id'];
$sql = "SELECT * FROM students WHERE id=$id";
$result = $conn->query($sql);
$student = $result->fetch_assoc();
?>

<!DOCTYPE html>
<html>
<head>
    <title>Edit Student</title>
    <style>
        /* Same as register.php styles */
    </style>
</head>
<body>
    <div class="container">
        <h1>Edit Student</h1>
        <form method="POST" action="">
            <input type="hidden" name="id" value="<?php echo $student['id']; ?>">
            <div class="form-group">
                <label>Name</label>
                <input type="text" name="name" value="<?php echo $student['name']; ?>" required>
            </div>
            <div class="form-group">
                <label>Email</label>
                <input type="email" name="email" value="<?php echo $student['email']; ?>" required>
            </div>
            <div class="form-group">
                <label>Phone</label>
                <input type="text" name="phone" value="<?php echo $student['phone']; ?>">
            </div>
            <div class="form-group">
                <label>Course</label>
                <select name="course" required>
                    <option value="Computer Science" <?php if ($student['course'] == 'Computer Science') echo 'selected'; ?>>Computer Science</option>
                    <option value="Engineering" <?php if ($student['course'] == 'Engineering') echo 'selected'; ?>>Engineering</option>
                    <option value="Business" <?php if ($student['course'] == 'Business') echo 'selected'; ?>>Business</option>
                </select>
            </div>
            <button type="submit">Update</button>
        </form>
    </div>
</body>
</html>
```

### **6. `delete.php` (Delete Student)**
```php
<?php
include 'config.php';

$id = $_GET['id'];
$sql = "DELETE FROM students WHERE id=$id";
$conn->query($sql);
header("Location: students.php");
?>
```

---

## **Concepts Covered:**  
✅ **PHP** – Form handling, MySQL operations, sessions (optional).  
✅ **HTML** – Forms, tables, semantic structure.  
✅ **CSS** – Styling forms, tables, buttons, responsive design.  
✅ **MySQL** – CRUD operations (Create, Read, Update, Delete).  

---

## **How to Run?**  
1. Set up XAMPP/WAMP.  
2. Import the SQL database.  
3. Place files in `htdocs/student_registration`.  
4. Access:  
   - Registration: `http://localhost/student_registration/register.php`  
   - Admin Dashboard: `http://localhost/student_registration/students.php`  

---

### **Enhancements (Optional):**  
🔹 **User Login System** (Admin vs Student).  
🔹 **Search & Pagination** for the student list.  
🔹 **Email Verification** after registration.  

