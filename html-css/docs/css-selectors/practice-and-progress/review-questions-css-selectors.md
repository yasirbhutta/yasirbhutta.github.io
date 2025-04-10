---
layout: default
title: --.
description: --.
---

### Review Questions: CSS Selectors

1. What is the purpose of a class selector in CSS?  
   **Answer:** A class selector is used to apply styles to one or more elements with the same class name.

2. How do you define a class selector in CSS?  
   **Answer:** Use a period (`.`) followed by the class name. Example: `.example { color: red; }`

3. Explain the difference between a class selector and a generic class selector in CSS. Provide one example of each.
   **Answer:**
   [Difference Between a Class Selector and a Generic Class Selector in CSS](/html-css/posts/class-generic-selectors.md)
4. What is the difference between an ID selector and a class selector?  
   **Answer:**  
   - An ID selector (`#id`) is unique and applies to a single element.  
   - A class selector (`.class`) can be reused for multiple elements.

5. How do you apply a generic class selector to multiple elements?  
   **Answer:** Assign the same class name to multiple elements and define the styles in CSS using the class selector.

6. What is the purpose of the `hover` pseudo-class in CSS?  
   **Answer:** It applies styles to an element when the user hovers over it with a mouse.

7. How do you style an element using an ID selector in CSS?  
   **Answer:** Use a hash (`#`) followed by the ID name. Example: `#example { color: blue; }`

8. What is the difference between a pseudo-class and a pseudo-element in CSS?  
   **Answer:**  
   - A pseudo-class defines the special state of an element (e.g., `:hover`).  
   - A pseudo-element allows you to style specific parts of an element (e.g., `::before`).

9.  How do you apply a hover effect to a button in CSS?  
   **Answer:** Use the `button:hover` pseudo-class. Example:  
   ```css
   button:hover {
       background-color: darkorange;
   }