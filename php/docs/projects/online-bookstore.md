---
layout: page
title: "PHP Projects for Beginners: Online Bookstore"
description: Learn PHP basics with this beginner-friendly guide. Understand PHP syntax, variables, functions, and more to start building dynamic web applications.
keywords: PHP basics, PHP tutorial, PHP for beginners, PHP syntax, PHP variables, PHP functions, learn PHP, PHP fundamentals, PHP programming
toc: toc/php.html
course: php
topic: "basics"
mini_project: true
next: /php/docs/basics/what-is-php.html
---

# **Mini Project: **

## **Project Title:** Online Bookstore  

## **Objective:**  
Build a simple online bookstore where users can:  
- Browse books  
- Add books to a cart  
- "Checkout" (simulated)  
- Admins can add/edit/delete books  

**Perfect for beginners** to learn:  
✅ PHP forms & sessions  
✅ MySQL database operations  
✅ Basic HTML/CSS styling  
✅ CRUD (Create, Read, Update, Delete)  

---

## **Features**  
### **User Side**  
1. **Homepage** – Display all books  
2. **Book Details** – View single book  
3. **Cart System** – Add/remove books (using sessions)  

### **Admin Side**  
1. **Add New Book** (Title, Author, Price, Image)  
2. **Edit/Delete Books**  

---

## **Step-by-Step Implementation**  

### **1. Database Setup (`bookstore_db`)**  
```sql
CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    image VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Sample data
INSERT INTO books (title, author, price, image) VALUES
('PHP for Beginners', 'John Doe', 19.99, 'php-book.jpg'),
('Learn MySQL', 'Jane Smith', 24.99, 'mysql-book.jpg');
```

### **2. `config.php` (Database Connection)**  
```php
<?php
$host = "localhost";
$user = "root";
$pass = "";
$db = "bookstore_db";

$conn = new mysqli($host, $user, $pass, $db);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>
```

### **3. `index.php` (Homepage - List All Books)**  
```php
<?php include 'config.php'; ?>
<!DOCTYPE html>
<html>
<head>
    <title>Online Bookstore</title>
    <style>
        body { font-family: Arial; padding: 20px; }
        .books { display: flex; flex-wrap: wrap; gap: 20px; }
        .book { border: 1px solid #ddd; padding: 15px; width: 200px; }
        .book img { max-width: 100%; height: auto; }
        .price { color: green; font-weight: bold; }
    </style>
</head>
<body>
    <h1>Welcome to Our Bookstore</h1>
    <div class="books">
        <?php
        $sql = "SELECT * FROM books";
        $result = $conn->query($sql);
        
        while ($book = $result->fetch_assoc()) {
            echo "<div class='book'>
                <img src='images/{$book['image']}' alt='{$book['title']}'>
                <h3>{$book['title']}</h3>
                <p>By {$book['author']}</p>
                <p class='price'>${$book['price']}</p>
                <a href='view.php?id={$book['id']}'>View Details</a>
                <a href='add_to_cart.php?id={$book['id']}'>Add to Cart</a>
            </div>";
        }
        ?>
    </div>
    <a href="admin.php">Admin Panel</a>
</body>
</html>
```

### **4. `view.php` (Single Book Details)**  
```php
<?php 
include 'config.php';
$id = $_GET['id'];
$book = $conn->query("SELECT * FROM books WHERE id=$id")->fetch_assoc();
?>
<!DOCTYPE html>
<html>
<head>
    <title><?php echo $book['title']; ?></title>
    <style>
        .book-detail { max-width: 600px; margin: auto; }
        .book-detail img { max-width: 200px; }
    </style>
</head>
<body>
    <div class="book-detail">
        <img src="images/<?php echo $book['image']; ?>">
        <h1><?php echo $book['title']; ?></h1>
        <p><strong>Author:</strong> <?php echo $book['author']; ?></p>
        <p><strong>Price:</strong> $<?php echo $book['price']; ?></p>
        <a href="add_to_cart.php?id=<?php echo $book['id']; ?>">Add to Cart</a>
        <a href="index.php">Back to Store</a>
    </div>
</body>
</html>
```

### **5. `add_to_cart.php` (Cart System with Sessions)**  
```php
<?php
session_start();
include 'config.php';

$book_id = $_GET['id'];
if (!isset($_SESSION['cart'])) {
    $_SESSION['cart'] = [];
}

// Add book to cart if not already present
if (!in_array($book_id, $_SESSION['cart'])) {
    $_SESSION['cart'][] = $book_id;
    echo "<script>alert('Book added to cart!'); window.location.href='index.php';</script>";
} else {
    echo "<script>alert('Book already in cart!'); window.location.href='index.php';</script>";
}
?>
```

### **6. `cart.php` (View Cart)**  
```php
<?php 
session_start();
include 'config.php';
?>
<!DOCTYPE html>
<html>
<head>
    <title>Your Cart</title>
    <style>
        .cart-item { display: flex; margin-bottom: 15px; }
        .cart-item img { width: 80px; margin-right: 15px; }
    </style>
</head>
<body>
    <h1>Your Shopping Cart</h1>
    <?php
    if (empty($_SESSION['cart'])) {
        echo "<p>Your cart is empty.</p>";
    } else {
        foreach ($_SESSION['cart'] as $book_id) {
            $book = $conn->query("SELECT * FROM books WHERE id=$book_id")->fetch_assoc();
            echo "<div class='cart-item'>
                <img src='images/{$book['image']}'>
                <div>
                    <h3>{$book['title']}</h3>
                    <p>${$book['price']}</p>
                    <a href='remove_from_cart.php?id={$book['id']}'>Remove</a>
                </div>
            </div>";
        }
        echo "<a href='checkout.php'>Proceed to Checkout</a>";
    }
    ?>
    <a href="index.php">Continue Shopping</a>
</body>
</html>
```

### **7. `admin.php` (Admin Dashboard - Add/Edit Books)**  
```php
<?php include 'config.php'; ?>
<!DOCTYPE html>
<html>
<head>
    <title>Admin Panel</title>
    <style>
        form { max-width: 500px; margin: auto; }
        input, textarea { width: 100%; padding: 8px; margin: 5px 0; }
    </style>
</head>
<body>
    <h1>Admin Panel</h1>
    
    <h2>Add New Book</h2>
    <form action="save_book.php" method="POST" enctype="multipart/form-data">
        <input type="text" name="title" placeholder="Title" required>
        <input type="text" name="author" placeholder="Author" required>
        <input type="number" step="0.01" name="price" placeholder="Price" required>
        <input type="file" name="image" accept="image/*">
        <button type="submit">Save Book</button>
    </form>

    <h2>Manage Books</h2>
    <?php
    $books = $conn->query("SELECT * FROM books");
    while ($book = $books->fetch_assoc()) {
        echo "<div>
            <h3>{$book['title']}</h3>
            <a href='edit_book.php?id={$book['id']}'>Edit</a>
            <a href='delete_book.php?id={$book['id']}'>Delete</a>
        </div>";
    }
    ?>
</body>
</html>
```

---

## **How to Run?**  
1. Set up XAMPP/WAMP.  
2. Import the SQL database.  
3. Place files in `htdocs/bookstore`.  
4. Create an `images` folder for book covers.  
5. Access:  
   - User: `http://localhost/bookstore/index.php`  
   - Admin: `http://localhost/bookstore/admin.php`  

---

## **Key Learnings**  
🔹 **PHP & MySQL Integration** – Fetching/displaying data  
🔹 **Sessions** – Simple cart system  
🔹 **File Uploads** – Handling book images  
🔹 **CRUD Operations** – Admin book management  
