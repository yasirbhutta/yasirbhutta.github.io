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

