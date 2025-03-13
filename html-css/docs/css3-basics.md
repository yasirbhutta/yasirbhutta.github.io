## Inline Styles in CSS

Inline styles in CSS are applied directly to an HTML element using the `style` attribute. Here are some basic examples for beginners:

### 1. **Change Text Color**
```html
<p style="color: blue;">This is a blue paragraph.</p>
```

### 2. **Change Font Size**
```html
<p style="font-size: 20px;">This text has a larger font size.</p>
```

### 3. **Change Background Color**
```html
<div style="background-color: yellow;">This div has a yellow background.</div>
```

### 4. **Add Border to an Element**
```html
<p style="border: 2px solid red;">This paragraph has a red border.</p>
```

### 5. **Center Text and Add Padding**
```html
<div style="text-align: center; padding: 20px;">
    This text is centered with padding.
</div>
```

### 6. **Change Font Family**
```html
<p style="font-family: Arial, sans-serif;">This text is in Arial font.</p>
```

### 7. **Make Text Bold and Italic**
```html
<p style="font-weight: bold; font-style: italic;">Bold and italic text.</p>
```

### 8. **Set Width and Height**
```html
<div style="width: 200px; height: 100px; background-color: lightblue;">
    This div has a fixed width and height.
</div>
```

### 9. **Add a Shadow to Text**
```html
<p style="text-shadow: 2px 2px 5px gray;">This text has a shadow.</p>
```

### 10. **Round the Corners of a Box**
```html
<div style="background-color: lightgreen; padding: 20px; border-radius: 10px;">
    This box has rounded corners.
</div>
```
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1602443888929206"
     crossorigin="anonymous"></script>
<ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-1602443888929206"
     data-ad-slot="6296238623"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

## Document Level in CSS

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Document level - CSS3</title>
    <style type="text/css">
        h1 {
            border-width: 2px;
            border-style: solid;
            border-color: black;
            color: white;
            text-align: center;
            background-color: goldenrod;
            font-size: 28px;
            padding: 10px;
            border-radius: 8px;
        }
        p {
            font-weight: bold;
            font-style: italic;
            color: white;
            background-color: darkblue;
            font-size: 18px;
            padding: 10px;
            border-radius: 5px;
        }
    </style>

</head>

<body>
    <h1>Heading</h1>
    <p>
        I've learned that people will forget what you said, people will forget what you did, but people will never forget how you
        made them feel.” ― Maya Angelou
    </p>
    <h1 style="color:red;">Heading</h1>
    <p>
         “Always forgive your enemies; nothing annoys them so much.” ― Oscar Wilde
    </p>
    <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Placeat, neque nulla, harum ipsum ea quae dolore laborum quis rem voluptates illo non inventore pariatur? Nisi, perspiciatis. Quo, sapiente hic. Dicta!</p>

</body>

</html>
```

---

### **Task: Style a Simple Web Page Using Document-Level CSS**  

#### **Objective:** Learn to apply CSS styles using **document-level CSS** (inside a `<style>` tag in the HTML file).  

#### **Instructions:**  
1. Open a text editor (VS Code, Notepad++, or any preferred editor).  
2. Create a new HTML file and name it `styled_page.html`.  
3. Write the following HTML structure and apply CSS inside the `<style>` tag in the `<head>` section.  

---

### **Starter Code:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Styled Page</title>
    <style>
        /* Document-Level CSS */
        body {
            background-color: lightblue;
            font-family: Arial, sans-serif;
            text-align: center;
        }
        h1 {
            color: darkblue;
            text-transform: uppercase;
        }
        p {
            color: darkgreen;
            font-size: 18px;
        }
        button {
            background-color: orange;
            color: white;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: darkorange;
        }
    </style>
</head>
<body>
    <h1>Welcome to My Styled Page</h1>
    <p>This is a simple paragraph with some styling.</p>
    <button>Click Me</button>
</body>
</html>
```

---

### **Tasks for Students:**
1. **Modify the Background:** Change the `background-color` of the page to another color.  
2. **Change Text Color:** Modify the `h1` and `p` colors to different shades.  
3. **Experiment with Font Styles:** Try using a different font-family.  
4. **Customize the Button:** Change the `background-color`, `padding`, and `hover` effect.  
```css
button:hover {
            background-color: darkblue;
            transform: scale(1.1); /* Slightly increases the size */
        }
```
5. **Add a Border to Paragraphs:** Use the `border` property to give paragraphs a border. 

<script async 
src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1602443888929206"
     crossorigin="anonymous"></script>
<ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-1602443888929206"
     data-ad-slot="6296238623"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>


## External Level CSS

External CSS is a method of applying styles to a webpage by linking an external stylesheet file. This approach keeps the HTML structure clean and makes it easier to maintain and update styles across multiple pages.

### How External CSS Works:
1. **Create a CSS file**  
   - Save the file with a `.css` extension (e.g., `styles.css`).
2. **Link the CSS file to an HTML document**  
   - Use the `<link>` tag inside the `<head>` section of the HTML file.

### Example:

#### 1. HTML File (`index.html`):
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>External CSS Example</title>
    <link rel="stylesheet" href="styles.css">  <!-- Linking the external CSS file -->
</head>
<body>
    <h1>Welcome to My Website</h1>
    <p>This is an example of external CSS.</p>
</body>
</html>
```

#### 2. CSS File (`styles.css`):
```css
/* Styling for the heading */
h1 {
    color: blue;
    text-align: center;
}

/* Styling for the paragraph */
p {
    color: green;
    font-size: 18px;
}
```

### How It Works:
- The browser reads the `index.html` file and sees the `<link>` tag pointing to `styles.css`.
- It loads `styles.css` and applies the styles to the corresponding HTML elements.
- The `<h1>` tag turns blue and is centered, while the `<p>` tag appears green with a font size of 18px.

### Advantages of External CSS:
- **Reusability:** The same CSS file can be used for multiple web pages.
- **Separation of Concerns:** Keeps HTML structure separate from styling, making the code more organized.
- **Easier Maintenance:** Updating the CSS file changes styles across all linked pages.

---

**See also:**

- [CSS Validation Service](https://jigsaw.w3.org/css-validator/)
- [CSS Cheat Sheet](https://htmlcheatsheet.com/css/)

### **Task: Applying External CSS to Style a Webpage**

#### **Objective:**  
Create an HTML file and an external CSS file to style a simple webpage.

#### **Instructions:**  
1. **Create an HTML file (`task.html`)** with the following elements:
   - A heading (`h1`) with the text **"My First Styled Page"**  
   - A paragraph (`p`) with a short description of yourself.  
   - A button (`button`) with the text **"Click Me"**  

2. **Create an external CSS file (`task-styles.css`)** and apply the following styles:
   - Set the background color of the webpage to `lightgray`.  
   - Make the heading (`h1`) **red** and center-aligned.  
   - Style the paragraph (`p`) with **blue text** and a font size of `16px`.  
   - Style the button:
     - Background color: `green`  
     - Text color: `white`  
     - Padding: `10px 20px`  
     - Border-radius: `5px`  

3. **Link the CSS file to the HTML file** using the `<link>` tag in the `<head>` section.

#### **Bonus Challenge:**  
Modify the button style to change its background color to **dark green** when hovered.

#### **Expected Outcome:**  
When you open the `task.html` file in a browser, you should see a well-styled page where the heading is red, the paragraph is blue, and the button is green with a hover effect.

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


