# CSS Selectors

## Class Selector

## Example of Class Selector

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Class Selectors </title>
    <style type="text/css">
        /* text-align: left | right | center | justify  */
        p.normal {
            color:blue;
            text-align: right;
        }

        p.warning {
            color:red;
            text-align: center;
        }
    </style>
</head>

<body>
    <p class="normal">
        I've learned that people will forget what you said, people will forget what you did, but people will never
        forget how you
        made them feel.”
        <cite>― Maya Angelou</cite>

    </p>
    <p class="warning">
        “Always forgive your enemies; nothing annoys them so much.” ― Oscar Wilde
    </p>
</body>

</html>
```

## Generic Selectors

### Example of Generic Class Selector

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Generic Selectors </title>
    <style type="text/css">
        /* text-decoration: none | underline | overline | line-through | blink */
        .alert {
            color: red;
            text-decoration: underline;
        }

    </style>
</head>

<body>
    <h1> Selector Forms </h1>
    <h2 class="alert">Generic Class Selector</h2>
    <p class="alert">
        “Always forgive your enemies; nothing annoys them so much.” ― Oscar Wilde
    </p>
</body>
</html>
```

### **Task: Class selector task for Styling Multiple Paragraphs and a Button Using Different CSS Levels**  

#### **Objective:**  
Apply **Inline, Document-Level, and External CSS** to style multiple paragraphs and a button in a webpage.

---

### **Instructions:**  

1. **Create an HTML file (`task.html`)** with the following elements:
   - A heading (`h1`) with the text **"CSS Styling Task"**  
   - Three paragraphs (`p`) with different texts:
     - First paragraph: **"This paragraph is styled using inline CSS."**  
     - Second paragraph: **"This paragraph is styled using document-level CSS."**  
     - Third paragraph: **"This paragraph is styled using external CSS."**  
   - A button (`button`) with the text **"Hover Over Me!"**  

2. **Apply CSS using the three different levels:**  

   - **Inline CSS**:  
     - Apply inline styles to the **first paragraph** (`p`), setting **color to red and font size to 16px**.  
   - **Document-Level (Internal) CSS**:  
     - Inside a `<style>` tag in the `<head>`, style the **second paragraph** to have **blue text and italic font style**.  
   - **External CSS (`task-styles.css`)**:  
     - Create a CSS file and style the **third paragraph** (`.external-text`):
       - Text color: **green**  
       - Font size: **18px**  
     - Style the **button**:
       - Background color: **orange**  
       - Text color: **white**  
       - Padding: **10px 20px**  
       - Border-radius: **5px**  
       - On hover, change the background color to **dark orange**.  

---

### **Expected Code Structure:**  

#### **1. HTML File (`task.html`)**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS Styling Task</title>
    <link rel="stylesheet" href="task-styles.css"> <!-- External CSS Link -->
    <style>
        /* Document-Level CSS */
        .document-text {
            color: blue;
            font-style: italic;
        }
    </style>
</head>
<body>

    <h1>CSS Styling Task</h1>

    <p style="color: red; font-size: 16px;">This paragraph is styled using inline CSS.</p>

    <p class="document-text">This paragraph is styled using document-level CSS.</p>

    <p class="external-text">This paragraph is styled using external CSS.</p>

    <button>Hover Over Me!</button>

</body>
</html>
```

---

#### **2. External CSS File (`task-styles.css`)**
```css
/* External CSS for the third paragraph */
.external-text {
    color: green;
    font-size: 18px;
}

/* External CSS for the button */
button {
    background-color: orange;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

/* Button hover effect */
button:hover {
    background-color: darkorange;
}
```

---

### **Bonus Challenge:**  
- Add a **border and padding** to each paragraph to differentiate them.  
- Add an **active state** to the button that changes its background color when clicked.  

#### **Expected Outcome:**  
- **First paragraph** is styled with **Inline CSS** (red, 16px font).  
- **Second paragraph** is styled with **Document-Level CSS** (blue, italic).  
- **Third paragraph** is styled with **External CSS** (green, 18px font).  
- **Button** is styled with **External CSS** and changes color when hovered.  

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