---
layout: page
title: **Mini Project: Personal Task Manager with PHP & MySQL**
description: Build a web-based task manager where users can: - Create, view, edit, and delete tasks - Mark tasks as complete - Organize tasks by categories (Work,...
keywords: task, php, category, title, tasks
---
# **Mini Project: Personal Task Manager with PHP & MySQL**

## **Project Title:** Simple Task Management System  

## **Objective:**  
Build a web-based task manager where users can:  
- Create, view, edit, and delete tasks  
- Mark tasks as complete  
- Organize tasks by categories (Work, Personal, Study)  

**Perfect for beginners** to learn:  
✅ PHP form handling  
✅ MySQL database operations  
✅ Basic CRUD functionality  
✅ Session management (for user login in extended version)  

---

## **Features**  
### **Core Features**  
1. **Add New Tasks** (Title, Description, Due Date, Category)  
2. **View All Tasks** (List view with filtering options)  
3. **Mark Tasks as Complete**  
4. **Edit/Delete Tasks**  

### **Optional Enhancements**  
- User registration/login system  
- Priority levels (High/Medium/Low)  
- Search functionality  

---

## **Step-by-Step Implementation**  

### **1. Database Setup (`task_manager_db`)**  
```sql
CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    due_date DATE,
    category ENUM('Work', 'Personal', 'Study') NOT NULL,
    is_completed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Sample data
INSERT INTO tasks (title, description, due_date, category) VALUES
('Complete PHP project', 'Build a task manager app', '2023-12-15', 'Work'),
('Buy groceries', 'Milk, eggs, bread', '2023-12-10', 'Personal');
```

### **2. `config.php` (Database Connection)**  
```php
<?php
$host = "localhost";
$user = "root";
$pass = "";
$db = "task_manager_db";

$conn = new mysqli($host, $user, $pass, $db);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>
```

### **3. `index.php` (Main Task Dashboard)**  
```php
<?php include 'config.php'; ?>
<!DOCTYPE html>
<html>
<head>
    <title>My Task Manager</title>
    <style>
        body { font-family: Arial; max-width: 800px; margin: 0 auto; padding: 20px; }
        .task { background: #f9f9f9; padding: 15px; margin-bottom: 10px; border-radius: 5px; }
        .completed { opacity: 0.6; text-decoration: line-through; }
        .task-actions a { margin-right: 10px; }
        .category-work { border-left: 4px solid #3498db; }
        .category-personal { border-left: 4px solid #2ecc71; }
        .category-study { border-left: 4px solid #9b59b6; }
    </style>
</head>
<body>
    <h1>My Tasks</h1>
    
    <!-- Add New Task Form -->
    <form method="POST" action="add_task.php">
        <h2>Add New Task</h2>
        <input type="text" name="title" placeholder="Task title" required>
        <textarea name="description" placeholder="Description"></textarea>
        <input type="date" name="due_date">
        <select name="category" required>
            <option value="Work">Work</option>
            <option value="Personal">Personal</option>
            <option value="Study">Study</option>
        </select>
        <button type="submit">Add Task</button>
    </form>

    <!-- Task List -->
    <h2>My Task List</h2>
    <?php
    $sql = "SELECT * FROM tasks ORDER BY is_completed, due_date ASC";
    $result = $conn->query($sql);
    
    if ($result->num_rows > 0) {
        while ($task = $result->fetch_assoc()) {
            $completed = $task['is_completed'] ? 'completed' : '';
            echo "<div class='task category-{$task['category']} {$completed}'>
                <h3>{$task['title']}</h3>
                <p>{$task['description']}</p>
                <p>Due: {$task['due_date']} | Category: {$task['category']}</p>
                <div class='task-actions'>
                    <a href='toggle_complete.php?id={$task['id']}'>" . 
                        ($task['is_completed'] ? 'Mark Incomplete' : 'Mark Complete') . 
                    "</a>
                    <a href='edit_task.php?id={$task['id']}'>Edit</a>
                    <a href='delete_task.php?id={$task['id']}'>Delete</a>
                </div>
            </div>";
        }
    } else {
        echo "<p>No tasks found. Add your first task above!</p>";
    }
    ?>
</body>
</html>
```

### **4. `add_task.php` (Process New Task)**  
```php
<?php
include 'config.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $title = $_POST['title'];
    $description = $_POST['description'];
    $due_date = $_POST['due_date'];
    $category = $_POST['category'];
    
    $sql = "INSERT INTO tasks (title, description, due_date, category) 
            VALUES ('$title', '$description', '$due_date', '$category')";
    
    if ($conn->query($sql)) {
        header("Location: index.php");
    } else {
        echo "Error: " . $conn->error;
    }
}
?>
```

### **5. `toggle_complete.php` (Mark Complete/Incomplete)**  
```php
<?php
include 'config.php';

$id = $_GET['id'];
$task = $conn->query("SELECT is_completed FROM tasks WHERE id=$id")->fetch_assoc();
$new_status = $task['is_completed'] ? 0 : 1;

$conn->query("UPDATE tasks SET is_completed=$new_status WHERE id=$id");
header("Location: index.php");
?>
```

### **6. `edit_task.php` (Edit Existing Task)**  
```php
<?php
include 'config.php';

// Handle form submission
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $id = $_POST['id'];
    $title = $_POST['title'];
    $description = $_POST['description'];
    $due_date = $_POST['due_date'];
    $category = $_POST['category'];
    
    $sql = "UPDATE tasks SET 
            title='$title', 
            description='$description', 
            due_date='$due_date', 
            category='$category' 
            WHERE id=$id";
    
    $conn->query($sql);
    header("Location: index.php");
}

// Get task to edit
$id = $_GET['id'];
$task = $conn->query("SELECT * FROM tasks WHERE id=$id")->fetch_assoc();
?>

<!DOCTYPE html>
<html>
<head>
    <title>Edit Task</title>
    <style>
        /* Same as index.php styles */
    </style>
</head>
<body>
    <h1>Edit Task</h1>
    <form method="POST" action="edit_task.php">
        <input type="hidden" name="id" value="<?php echo $task['id']; ?>">
        <input type="text" name="title" value="<?php echo $task['title']; ?>" required>
        <textarea name="description"><?php echo $task['description']; ?></textarea>
        <input type="date" name="due_date" value="<?php echo $task['due_date']; ?>">
        <select name="category" required>
            <option value="Work" <?php if ($task['category'] == 'Work') echo 'selected'; ?>>Work</option>
            <option value="Personal" <?php if ($task['category'] == 'Personal') echo 'selected'; ?>>Personal</option>
            <option value="Study" <?php if ($task['category'] == 'Study') echo 'selected'; ?>>Study</option>
        </select>
        <button type="submit">Update Task</button>
    </form>
</body>
</html>
```

### **7. `delete_task.php` (Delete Task)**  
```php
<?php
include 'config.php';

$id = $_GET['id'];
$conn->query("DELETE FROM tasks WHERE id=$id");
header("Location: index.php");
?>
```

---

## **How to Run?**  
1. Set up XAMPP/WAMP  
2. Import the SQL database  
3. Place files in `htdocs/task_manager`  
4. Access: `http://localhost/task_manager/index.php`  

---

## **Key Learnings**  
🔹 **PHP Forms** – Handling user input  
🔹 **MySQL CRUD** – Creating, reading, updating, deleting data  
🔹 **Basic UI** – Clean task display with CSS  
🔹 **Practical Application** – Building something useful  

---

## **Enhancement Ideas**  
1. **User System**  
   - Registration/login  
   - User-specific tasks  

2. **Advanced Features**  
   - Task priorities  
   - Search/filter options  
   - Due date reminders  

3. **UI Improvements**  
   - Drag-and-drop sorting  
   - Calendar view  

This project gives beginners hands-on experience building a **real-world application** while learning fundamental PHP/MySQL concepts! 🚀