# **Mini Project: Online Recipe Sharing Platform**

## **Project Title:** Simple Recipe Book

### **Perfect for Beginners Learning:**
✅ User authentication (registration/login)  
✅ Database relationships (recipes ↔ users)  
✅ File uploads (recipe images)  
✅ Search functionality  
✅ Responsive design  

---

## **Features**
### **User Features**
1. **Browse Recipes** - View all recipes or by category
2. **Search Recipes** - Find recipes by name/ingredients
3. **View Recipe Details** - Full instructions, ingredients, prep time
4. **User Accounts** - Register/login to submit recipes

### **Admin Features**
1. **Manage All Recipes** - Edit/delete any recipe
2. **Category Management** - Add/remove food categories

---

## **Database Schema (`recipe_db`)**
```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE recipes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    category_id INT NOT NULL,
    title VARCHAR(100) NOT NULL,
    ingredients TEXT NOT NULL,
    instructions TEXT NOT NULL,
    prep_time INT COMMENT 'in minutes',
    image VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

-- Sample categories
INSERT INTO categories (name) VALUES 
('Breakfast'), ('Lunch'), ('Dinner'), 
('Dessert'), ('Vegetarian'), ('Vegan');
```

---

## **Implementation Highlights**

### **1. User Registration**
```php
// register.php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = trim($_POST['username']);
    $email = trim($_POST['email']);
    $password = password_hash($_POST['password'], PASSWORD_DEFAULT);
    
    // Validate input
    // Check if username/email exists
    // Insert new user
}
```

### **2. Recipe Submission with Image Upload**
```php
// submit_recipe.php
if (isset($_FILES['image'])) {
    $targetDir = "uploads/";
    $fileName = uniqid() . '_' . basename($_FILES['image']['name']);
    $targetFile = $targetDir . $fileName;
    
    if (move_uploaded_file($_FILES['image']['tmp_name'], $targetFile)) {
        // Save recipe with image path
    }
}
```

### **3. Recipe Search**
```php
// search.php
$search = $_GET['q'] ?? '';
$sql = "SELECT * FROM recipes WHERE 
        title LIKE ? OR 
        ingredients LIKE ?";
$stmt = $conn->prepare($sql);
$searchTerm = "%$search%";
$stmt->bind_param("ss", $searchTerm, $searchTerm);
```

### **4. Responsive Recipe Card (CSS)**
```css
.recipe-card {
    border: 1px solid #ddd;
    border-radius: 8px;
    overflow: hidden;
    transition: transform 0.3s;
}
.recipe-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
}
.recipe-image {
    width: 100%;
    height: 200px;
    object-fit: cover;
}
@media (max-width: 768px) {
    .recipe-grid {
        grid-template-columns: 1fr;
    }
}
```

---

## **How to Run**
1. Create database and tables
2. Configure database connection in `config.php`
3. Create `uploads/` directory with write permissions
4. Implement basic user authentication
5. Start adding recipes!

---

## **Learning Outcomes**
1. **User Authentication** - Secure registration/login system
2. **File Handling** - Uploading and managing images
3. **Database Relations** - Connecting recipes to users/categories
4. **Search Implementation** - Basic search functionality
5. **Responsive Design** - Mobile-friendly layout

---

## **Enhancement Ideas**
1. **Rating System** - Let users rate recipes
2. **Meal Planner** - Weekly meal planning feature
3. **Print Option** - Printable recipe cards
4. **Social Sharing** - Share recipes on social media
5. **Admin Dashboard** - Advanced management tools
