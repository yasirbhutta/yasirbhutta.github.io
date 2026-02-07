---
layout: page
title: 🛠️ Project Title: **Mini Job Portal in PHP with MySQL**
description: Sure! Here's a fully regenerated and detailed beginner PHP project using MySQL as the storage method, with step-by-step instructions, code for every f...
keywords: job, php, title, html, mysql
---
Sure! Here's a fully **regenerated and detailed beginner PHP project using MySQL as the storage method**, with **step-by-step instructions**, **code for every file**, and **project structure**. This is a mini **Job Portal** that includes:

- Job listings from a MySQL database  
- Job detail view  
- A form to apply for a job  
- Storage of submitted applications in MySQL  

---

# 🛠️ Project Title: **Mini Job Portal in PHP with MySQL**

---

## 📦 Project Features

| Feature               | Description                                      |
|----------------------|--------------------------------------------------|
| Job Listings Page     | Lists all jobs from the database                |
| Job Details Page      | Shows full description of selected job         |
| Application Form      | Users can submit their name and email to apply |
| Data Storage          | All jobs and applications stored in MySQL       |

---

## 📁 Folder Structure

```
mini-job-portal/
│
├── db.php              # MySQL database connection
├── index.php           # Job listings
├── job.php             # Job detail view
├── apply.php           # Application form
├── styles.css          # Basic styling
└── README.md           # (optional) project notes
```

---

## 🧰 Prerequisites

- **XAMPP** or any PHP server with MySQL
- Basic knowledge of HTML, CSS, and PHP
- A text editor (VS Code recommended)

---

## ⚙️ Step-by-Step Setup

### ✅ Step 1: Create the MySQL Database

1. Open **phpMyAdmin** (usually at http://localhost/phpmyadmin)
2. Create a new database:
```sql
CREATE DATABASE job_portal;
```

3. Create the **jobs** table:
```sql
USE job_portal;

CREATE TABLE jobs (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(100) NOT NULL,
  company VARCHAR(100) NOT NULL,
  description TEXT NOT NULL
);
```

4. Create the **applications** table:
```sql
CREATE TABLE applications (
  id INT AUTO_INCREMENT PRIMARY KEY,
  job_id INT NOT NULL,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL,
  FOREIGN KEY (job_id) REFERENCES jobs(id)
);
```

5. Insert sample job listings:
```sql
INSERT INTO jobs (title, company, description) VALUES
('Frontend Developer', 'TechNova', 'Create user interfaces using HTML/CSS/JavaScript.'),
('PHP Developer', 'DevForge', 'Develop backend logic using PHP and MySQL.');
```

---

## 💾 Step 2: Create `db.php` (Database Connection)

```php
<?php
$host = 'localhost';
$user = 'root';
$password = ''; // change if needed
$database = 'job_portal';

$conn = new mysqli($host, $user, $password, $database);

if ($conn->connect_error) {
  die("Database connection failed: " . $conn->connect_error);
}
?>
```

---

## 🏠 Step 3: Create `index.php` (Job Listings Page)

```php
<?php include 'db.php'; ?>
<!DOCTYPE html>
<html>
<head>
  <title>Job Listings</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
<div class="container">
  <h1>Available Jobs</h1>
  <?php
    $query = "SELECT * FROM jobs";
    $result = $conn->query($query);

    while ($job = $result->fetch_assoc()) {
      echo "<div class='job'>";
      echo "<h2>{$job['title']} at {$job['company']}</h2>";
      echo "<a class='button' href='job.php?id={$job['id']}'>View Details</a>";
      echo "</div>";
    }
  ?>
</div>
</body>
</html>
```

---

## 🗂️ Step 4: Create `job.php` (Job Detail Page)

```php
<?php include 'db.php'; ?>
<?php
$job_id = $_GET['id'] ?? 0;
$stmt = $conn->prepare("SELECT * FROM jobs WHERE id = ?");
$stmt->bind_param("i", $job_id);
$stmt->execute();
$result = $stmt->get_result();
$job = $result->fetch_assoc();
?>
<!DOCTYPE html>
<html>
<head>
  <title>Job Details</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
<div class="container">
  <?php if ($job): ?>
    <h1><?= htmlspecialchars($job['title']) ?></h1>
    <p><strong>Company:</strong> <?= htmlspecialchars($job['company']) ?></p>
    <p><?= nl2br(htmlspecialchars($job['description'])) ?></p>
    <a class="button" href="apply.php?id=<?= $job['id'] ?>">Apply Now</a>
  <?php else: ?>
    <p>Job not found.</p>
  <?php endif; ?>
</div>
</body>
</html>
```

---

## 📝 Step 5: Create `apply.php` (Application Form)

```php
<?php include 'db.php'; ?>
<?php
$job_id = $_GET['id'] ?? 0;
$success = false;

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  $name = $_POST['name'] ?? '';
  $email = $_POST['email'] ?? '';

  $stmt = $conn->prepare("INSERT INTO applications (job_id, name, email) VALUES (?, ?, ?)");
  $stmt->bind_param("iss", $job_id, $name, $email);
  $success = $stmt->execute();
}
?>
<!DOCTYPE html>
<html>
<head>
  <title>Apply for Job</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
<div class="container">
  <?php if ($success): ?>
    <p class="success">✅ Your application has been submitted!</p>
  <?php else: ?>
    <h2>Apply for Job #<?= htmlspecialchars($job_id) ?></h2>
    <form method="POST">
      <label>Name:</label><br>
      <input type="text" name="name" required><br><br>

      <label>Email:</label><br>
      <input type="email" name="email" required><br><br>

      <button type="submit" class="button">Submit Application</button>
    </form>
  <?php endif; ?>
</div>
</body>
</html>
```

---

## 🎨 Step 6: Create `styles.css`

```css
body {
  font-family: Arial, sans-serif;
  background: #f2f2f2;
  margin: 0;
  padding: 0;
}

.container {
  max-width: 600px;
  margin: 30px auto;
  background: white;
  padding: 25px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

h1, h2 {
  color: #333;
}

.job {
  border-bottom: 1px solid #ddd;
  padding-bottom: 15px;
  margin-bottom: 15px;
}

.button {
  background-color: #0284c7;
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 5px;
  text-decoration: none;
  display: inline-block;
}

.success {
  background-color: #d1fae5;
  padding: 10px;
  border: 1px solid #10b981;
  color: #065f46;
  border-radius: 5px;
}
```

---

## 🚀 How to Run the Project

1. **Place the files** in a folder like `htdocs/mini-job-portal/` (if using XAMPP).
2. **Start Apache and MySQL** in the XAMPP control panel.
3. Open `phpMyAdmin` and import the database setup SQL.
4. Open your browser and go to:
```
http://localhost/mini-job-portal/index.php
```

---

## 🧠 Learning Outcomes

- How to connect PHP with MySQL
- How to use prepared statements (`mysqli`)
- Form submission and handling
- Styling with CSS
- Structuring real-world PHP projects
