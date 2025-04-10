# CSS Properties

# **CSS `background` Property – Syntax & Examples**  

The `background` property in CSS is used to set the background styles of an element, including color, image, position, size, and more.

---

## **1. Basic Syntax**  
```css
selector {
    background: value;
}
```
You can also use **individual background properties**:  

```css
selector {
    background-color: value;
    background-image: url('image.jpg');
    background-repeat: repeat | no-repeat;
    background-position: top | center | bottom left;
    background-size: cover | contain;
    background-attachment: fixed | scroll;
}
```

---

## **2. Examples**
### **Example 1: Setting a Solid Background Color**
```css
body {
    background-color: lightblue;
}
```
This sets the background color of the entire page to **light blue**.

---

### **Example 2: Adding a Background Image**
```css
body {
    background-image: url('background.jpg');
    background-repeat: no-repeat;
    background-size: cover;
}
```
- `background-image`: Sets an image as the background.  
- `background-repeat: no-repeat`: Prevents the image from repeating.  
- `background-size: cover`: Ensures the image covers the full area.

---

### **Example 3: Fixed Background Image**
```css
body {
    background-image: url('background.jpg');
    background-attachment: fixed;
    background-size: cover;
}
```
- `background-attachment: fixed;` keeps the image fixed when scrolling.

---

### **Example 4: Using Shorthand Background Property**
```css
body {
    background: lightblue url('background.jpg') no-repeat center/cover fixed;
}
```
This is equivalent to:
```css
body {
    background-color: lightblue;
    background-image: url('background.jpg');
    background-repeat: no-repeat;
    background-position: center;
    background-size: cover;
    background-attachment: fixed;
}
```

---

### **Conclusion**
The `background` property in CSS helps style elements with colors, images, and positioning. Learning how to use it properly can make your web design visually appealing! 🚀


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

{% assign topic = "css-properties" %}
{% include practice-and-progress.html topic=topic %}