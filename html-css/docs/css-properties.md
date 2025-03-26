# CSS Properties

## Box Model Components in CSS

![box-mobile](https://media.geeksforgeeks.org/wp-content/uploads/box-model-1.png)

### **Padding in CSS**  

**Padding** is a CSS property that adds space **inside** an element, between its content and its border. It helps in controlling the spacing inside elements without affecting their border or margin.

---

### **Syntax:**  
```css
element {
    padding: value;  /* Can be in px, %, em, etc. */
}
```

---

### **Different Ways to Use Padding:**

1. **Equal Padding on All Sides**  
   ```css
   div {
       padding: 20px;  /* Adds 20px padding on top, right, bottom, and left */
   }
   ```

2. **Different Padding for Each Side**  
   ```css
   div {
       padding-top: 10px;
       padding-right: 20px;
       padding-bottom: 15px;
       padding-left: 25px;
   }
   ```

3. **Shorthand Notation**  
   ```css
   div {
       padding: 10px 20px 15px 25px;
       /* Order: TOP RIGHT BOTTOM LEFT */
   }
   ```
   - **Two values:** `padding: 10px 20px;` (Top-Bottom 10px, Left-Right 20px)  
   - **Three values:** `padding: 10px 20px 15px;` (Top 10px, Left-Right 20px, Bottom 15px)  
   - **One value:** `padding: 10px;` (Applies 10px padding on all sides)

---

### **Example:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS Padding Example</title>
    <style>
        .box {
            background-color: lightblue;
            padding: 20px; /* Adds space inside the box */
            border: 2px solid blue;
            width: 200px;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="box">This is a padded box</div>
</body>
</html>
```

---

### **Key Points:**
- Padding increases the **inner space** of an element.
- It does not affect the margin (space **outside** the element).
- It can be set in various units like `px`, `%`, `em`, `rem`, etc.
- Negative padding values **are not allowed**.

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1602443888929206"
     crossorigin="anonymous"></script>
<!-- display square -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-1602443888929206"
     data-ad-slot="9845543342"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

