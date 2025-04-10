---
layout: default
title: Class Selector vs Generic Class Selector in CSS: Key Differences and Examples.
description: Learn the difference between class selectors and generic class selectors in CSS. Explore practical examples to understand how to style specific elements and multiple elements effectively..
---

# Difference Between a Class Selector and a Generic Class Selector in CSS

1. **Class Selector**:  
   - Targets elements with a specific class name.  
   - It applies styles only to elements explicitly assigned that class.  

   **Example of a Class Selector**:  
   ```html
   <p class="highlight">This is a highlighted paragraph.</p>
   ```
   ```css
   p.highlight {
       color: red;
       font-weight: bold;
   }
   ```

2. **Generic Class Selector**:  
   - Targets multiple elements that share the same class name.  
   - It allows you to apply the same styles to multiple elements across the webpage.  

   **Example of a Generic Class Selector**:  
   ```html
   <h1 class="common-style">Heading 1</h1>
   <p class="common-style">This is a paragraph.</p>
   ```
   ```css
   .common-style {
       font-family: Arial, sans-serif;
       color: blue;
   }
   ``` 

### Key Difference:
- A **class selector** is specific to elements assigned a particular class, while a **generic class selector** is used to apply the same styles to multiple elements with the same class name.

{% include toc/css-toc.html %}

