---
layout: page
title: "PHP Project: Personal Blog System in PHP"
description: Learn PHP basics with this beginner-friendly guide. Understand PHP syntax, variables, functions, and more to start building dynamic web applications.
keywords: PHP basics, PHP tutorial, PHP for beginners, PHP syntax, PHP variables, PHP functions, learn PHP, PHP fundamentals, PHP programming
toc: toc/php.html
course: php
topic: "basics"
mini_project: true
next: /php/docs/basics/what-is-php.html
---

## **Project Title:** Simple Personal Blog System  

## **Objective:**  
To create a basic personal blog system where users can view blog posts, and an admin can add, edit, or delete posts. This project will integrate the following PHP concepts:  
- Introduction to PHP  
- How to Use PHP (Embedding PHP in HTML)  
- Case Sensitivity  
- Variables in PHP  
- Functions in PHP  
- Variable Scope  
- Constants  
- String Functions  
- Comments  

---

## **Features:**  
1. **User Side (Frontend):**  
   - Display a list of blog posts.  
   - View individual blog posts.  

2. **Admin Side (Backend):**  
   - Add a new blog post.  
   - Edit an existing blog post.  
   - Delete a blog post.  

---

## **Implementation Steps:**  

### **1. Setup Database (MySQL)**
Create a database `blog_db` with a table `posts`:  
```sql
CREATE TABLE posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### **2. Create `config.php` (Constants & Database Connection)**
```php
<?php
// Constants
define("DB_HOST", "localhost");
define("DB_USER", "root");
define("DB_PASS", "");
define("DB_NAME", "blog_db");

// Database connection (Variable Scope)
$conn = mysqli_connect(DB_HOST, DB_USER, DB_PASS, DB_NAME);

if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
?>
```

### **3. Create `functions.php` (Functions in PHP)**
```php
<?php
// Function to get all posts (Variable Scope)
function getAllPosts() {
    global $conn;
    $query = "SELECT * FROM posts ORDER BY created_at DESC";
    $result = mysqli_query($conn, $query);
    return mysqli_fetch_all($result, MYSQLI_ASSOC);
}

// Function to get a single post by ID
function getPostById($id) {
    global $conn;
    $query = "SELECT * FROM posts WHERE id = $id";
    $result = mysqli_query($conn, $query);
    return mysqli_fetch_assoc($result);
}

// Function to add a new post (String Functions - sanitization)
function addPost($title, $content) {
    global $conn;
    $title = mysqli_real_escape_string($conn, $title);
    $content = mysqli_real_escape_string($conn, $content);
    $query = "INSERT INTO posts (title, content) VALUES ('$title', '$content')";
    return mysqli_query($conn, $query);
}

// Function to delete a post
function deletePost($id) {
    global $conn;
    $query = "DELETE FROM posts WHERE id = $id";
    return mysqli_query($conn, $query);
}
?>
```

### **4. Create `index.php` (Display Posts - Introduction to PHP)**
```php
<?php include 'config.php'; ?>
<?php include 'functions.php'; ?>

<!DOCTYPE html>
<html>
<head>
    <title>My Personal Blog</title>
</head>
<body>
    <h1>Welcome to My Blog</h1>
    <?php
    // Case Sensitivity Example (variables are case-sensitive)
    $posts = getAllPosts();
    foreach ($posts as $post) {
        echo "<h2>" . htmlspecialchars($post['title']) . "</h2>";
        echo "<p>" . substr(htmlspecialchars($post['content']), 0, 100) . "...</p>"; // String Functions
        echo "<a href='post.php?id=" . $post['id'] . "'>Read More</a>";
        echo "<hr>";
    }
    ?>
</body>
</html>
```

### **5. Create `post.php` (Single Post View)**
```php
<?php include 'config.php'; ?>
<?php include 'functions.php'; ?>

<?php
// Check if 'id' is set in URL
if (isset($_GET['id'])) {
    $id = $_GET['id'];
    $post = getPostById($id);
    if (!$post) {
        die("Post not found!");
    }
} else {
    die("Invalid request!");
}
?>

<!DOCTYPE html>
<html>
<head>
    <title><?php echo htmlspecialchars($post['title']); ?></title>
</head>
<body>
    <h1><?php echo htmlspecialchars($post['title']); ?></h1>
    <p><?php echo nl2br(htmlspecialchars($post['content'])); ?></p>
    <a href="index.php">Back to Home</a>
</body>
</html>
```

### **6. Create `admin.php` (Admin Panel - Variables & Forms)**
```php
<?php include 'config.php'; ?>
<?php include 'functions.php'; ?>

<?php
// Handle form submission (Variables in PHP)
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    if (isset($_POST['add_post'])) {
        $title = $_POST['title'];
        $content = $_POST['content'];
        addPost($title, $content);
        header("Location: admin.php");
    } elseif (isset($_POST['delete_post'])) {
        $id = $_POST['post_id'];
        deletePost($id);
        header("Location: admin.php");
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Admin Panel</title>
</head>
<body>
    <h1>Admin Panel</h1>
    
    <!-- Add New Post Form -->
    <form method="POST">
        <h2>Add New Post</h2>
        <input type="text" name="title" placeholder="Post Title" required>
        <textarea name="content" placeholder="Post Content" required></textarea>
        <button type="submit" name="add_post">Add Post</button>
    </form>

    <!-- List Posts with Delete Option -->
    <h2>Manage Posts</h2>
    <?php
    $posts = getAllPosts();
    foreach ($posts as $post) {
        echo "<div>";
        echo "<h3>" . htmlspecialchars($post['title']) . "</h3>";
        echo "<form method='POST' style='display:inline;'>";
        echo "<input type='hidden' name='post_id' value='" . $post['id'] . "'>";
        echo "<button type='submit' name='delete_post'>Delete</button>";
        echo "</form>";
        echo "</div>";
    }
    ?>
</body>
</html>
```

---

## **Concepts Covered:**  
✅ **Introduction to PHP** – Basic PHP file structure.  
✅ **How to Use PHP** – Embedding PHP in HTML.  
✅ **Case Sensitivity** – Variable naming (`$Post` vs `$post`).  
✅ **Variables in PHP** – `$posts`, `$title`, `$content`.  
✅ **Functions in PHP** – `getAllPosts()`, `addPost()`, etc.  
✅ **Variable Scope** – Using `global $conn` inside functions.  
✅ **Constants** – `define("DB_HOST", "localhost")`.  
✅ **String Functions** – `substr()`, `htmlspecialchars()`, `nl2br()`.  
✅ **Comments** – Single-line (`//`) and multi-line (`/* */`).  

---

## **How to Run?**  
1. Set up XAMPP/WAMP.  
2. Place files in `htdocs/blog`.  
3. Import the SQL database.  
4. Open `http://localhost/blog/index.php`.  
5. Admin panel: `http://localhost/blog/admin.php`.  

---

### **Enhancements (Optional):**  
- User authentication (Login/Logout).  
- Categories & Tags.  
- Image upload for blog posts.  
