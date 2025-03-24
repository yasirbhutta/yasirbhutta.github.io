# Building a Responsive Horizontal Navigation Menu with CSS Flexbox

---

### **Task: Create a Horizontal Navigation Menu using CSS**  

#### **Objective:**  
Create a horizontal navigation bar with five menu items using HTML and CSS. The menu should be visually appealing and responsive.  

#### **Requirements:**  
1. Use an unordered list (`<ul>`) to structure the menu.  
2. Each menu item should be inside a `<li>` element.  
3. Style the menu with CSS to ensure:  
   - The items are displayed horizontally.  
   - There is padding and margin to space out the items.  
   - The text color changes when hovered.  
4. The menu should have a background color.  
5. On hovering over a menu item, change the background color and text color.  

---

### **Starter Code**  

#### **HTML (index.html)**  
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Horizontal Menu</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <nav>
        <ul class="menu">
            <li><a href="#">Home</a></li>
            <li><a href="#">About</a></li>
            <li><a href="#">Services</a></li>
            <li><a href="#">Portfolio</a></li>
            <li><a href="#">Contact</a></li>
        </ul>
    </nav>
</body>
</html>
```

#### **CSS (styles.css)**  
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

nav {
    background-color: #333;
    padding: 10px 0;
}

.menu {
    list-style: none;
    display: flex;
    justify-content: center;
    padding: 0;
    margin: 0;
}

.menu li {
    margin: 0 15px;
}

.menu a {
    text-decoration: none;
    color: white;
    font-size: 18px;
    padding: 10px 15px;
    display: block;
    transition: 0.3s;
}

.menu a:hover {
    background-color: #ff6600;
    color: #fff;
    border-radius: 5px;
}
```


