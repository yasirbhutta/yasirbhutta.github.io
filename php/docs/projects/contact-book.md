Absolutely! Here's a complete **Contact Book PHP project** using **MySQL** with **HTML and CSS**. This project is perfect for beginners and covers full **CRUD operations** (Create, Read, Update, Delete).

---

# 📘 Project: **Contact Book**

---

## ✅ Project Features

| Feature        | Description                                   |
|----------------|-----------------------------------------------|
| Add Contact    | Create a new contact with name, email, phone |
| View Contacts  | Display a list of contacts                   |
| Edit Contact   | Update a contact’s info                      |
| Delete Contact | Remove a contact from the list               |

---

## 🛠️ Technologies Used

- **Frontend**: HTML + CSS
- **Backend**: PHP
- **Database**: MySQL

---

## 📁 Folder Structure

```
contact-book/
│
├── db.php               # DB connection
├── index.php            # Contact list
├── add.php              # Add contact form
├── edit.php             # Edit contact
├── delete.php           # Delete logic
├── styles.css           # CSS file
└── README.md            # (optional) instructions
```

---

## ⚙️ STEP 1: MySQL Database Setup

### ✅ 1. Create the Database and Table

```sql
CREATE DATABASE contact_book;

USE contact_book;

CREATE TABLE contacts (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100),
  phone VARCHAR(20)
);
```

---

## 💻 STEP 2: Create PHP Files

### 📄 `db.php` – Database Connection

```php
<?php
$host = 'localhost';
$user = 'root';
$password = ''; // Change if needed
$database = 'contact_book';

$conn = new mysqli($host, $user, $password, $database);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>
```

---

### 📄 `index.php` – Show All Contacts

```php
<?php include 'db.php'; ?>
<!DOCTYPE html>
<html>
<head>
    <title>Contact Book</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
<div class="container">
    <h1>Contact Book</h1>
    <a class="button" href="add.php">+ Add New Contact</a>
    <table>
        <tr>
            <th>Name</th><th>Email</th><th>Phone</th><th>Actions</th>
        </tr>
        <?php
        $result = $conn->query("SELECT * FROM contacts");
        while ($row = $result->fetch_assoc()) {
            echo "<tr>
                    <td>".htmlspecialchars($row['name'])."</td>
                    <td>".htmlspecialchars($row['email'])."</td>
                    <td>".htmlspecialchars($row['phone'])."</td>
                    <td>
                        <a href='edit.php?id={$row['id']}'>Edit</a> |
                        <a href='delete.php?id={$row['id']}' onclick='return confirm(\"Delete this contact?\");'>Delete</a>
                    </td>
                  </tr>";
        }
        ?>
    </table>
</div>
</body>
</html>
```

---

### 📄 `add.php` – Add New Contact

```php
<?php include 'db.php';

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $name = $_POST['name'] ?? '';
    $email = $_POST['email'] ?? '';
    $phone = $_POST['phone'] ?? '';

    $stmt = $conn->prepare("INSERT INTO contacts (name, email, phone) VALUES (?, ?, ?)");
    $stmt->bind_param("sss", $name, $email, $phone);
    $stmt->execute();

    header("Location: index.php");
    exit();
}
?>
<!DOCTYPE html>
<html>
<head>
    <title>Add Contact</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
<div class="container">
    <h2>Add New Contact</h2>
    <form method="post">
        <label>Name:</label><br>
        <input type="text" name="name" required><br><br>
        <label>Email:</label><br>
        <input type="email" name="email"><br><br>
        <label>Phone:</label><br>
        <input type="text" name="phone"><br><br>
        <button class="button" type="submit">Add Contact</button>
    </form>
</div>
</body>
</html>
```

---

### 📄 `edit.php` – Edit Contact

```php
<?php
include 'db.php';

$id = $_GET['id'] ?? 0;
if (!$id) header("Location: index.php");

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name = $_POST['name'] ?? '';
    $email = $_POST['email'] ?? '';
    $phone = $_POST['phone'] ?? '';

    $stmt = $conn->prepare("UPDATE contacts SET name=?, email=?, phone=? WHERE id=?");
    $stmt->bind_param("sssi", $name, $email, $phone, $id);
    $stmt->execute();

    header("Location: index.php");
    exit();
} else {
    $stmt = $conn->prepare("SELECT * FROM contacts WHERE id=?");
    $stmt->bind_param("i", $id);
    $stmt->execute();
    $result = $stmt->get_result();
    $contact = $result->fetch_assoc();
}
?>
<!DOCTYPE html>
<html>
<head>
    <title>Edit Contact</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
<div class="container">
    <h2>Edit Contact</h2>
    <form method="post">
        <label>Name:</label><br>
        <input type="text" name="name" value="<?= htmlspecialchars($contact['name']) ?>" required><br><br>
        <label>Email:</label><br>
        <input type="email" name="email" value="<?= htmlspecialchars($contact['email']) ?>"><br><br>
        <label>Phone:</label><br>
        <input type="text" name="phone" value="<?= htmlspecialchars($contact['phone']) ?>"><br><br>
        <button class="button" type="submit">Update Contact</button>
    </form>
</div>
</body>
</html>
```

---

### 📄 `delete.php` – Delete Contact

```php
<?php
include 'db.php';
$id = $_GET['id'] ?? 0;

if ($id) {
    $stmt = $conn->prepare("DELETE FROM contacts WHERE id = ?");
    $stmt->bind_param("i", $id);
    $stmt->execute();
}

header("Location: index.php");
exit();
?>
```

---

### 📄 `styles.css` – Basic CSS

```css
body {
    font-family: Arial, sans-serif;
    background: #f9fafb;
    padding: 20px;
}

.container {
    max-width: 700px;
    margin: auto;
    background: white;
    padding: 20px;
    border-radius: 8px;
}

h1, h2 {
    color: #1e293b;
}

.button {
    background-color: #0284c7;
    color: white;
    padding: 10px 15px;
    text-decoration: none;
    border-radius: 5px;
    display: inline-block;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 15px;
}

th, td {
    padding: 10px;
    border: 1px solid #ccc;
    text-align: left;
}
```

---

## 🚀 How to Run This Project

1. Install [XAMPP](https://www.apachefriends.org/) or similar PHP server.
2. Create a folder `contact-book` in `htdocs/`.
3. Place all files inside this folder.
4. Open **phpMyAdmin** and import the SQL schema shown above.
5. Open your browser and go to:  
   👉 `http://localhost/contact-book/index.php`

---

## 🧠 You Will Learn

- How to use PHP to handle forms
- CRUD operations with MySQL
- How to build a functional UI with HTML and CSS
- Writing secure queries with prepared statements
