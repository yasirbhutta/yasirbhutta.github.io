---
layout: page
title: "HTML Basics: Comprehensive Guide to Elements, Tags, and Structure."
description: Master the fundamentals of HTML with this comprehensive guide. Learn about elements, tags, attributes, and structure to build well-structured web pages for beginners and aspiring web developers.
keywords: html basics structure, html elements, html tags, html structure, learn with yasir, yasirbhutta
author: Muhammad Yasir Bhutta
course: html-css
topic: html-basics
show_toc: false
toc: toc/html-toc.html
show_practice_progress: false
show_mini_project: false
prev: /it-324/
breadcrumb: 
- title: Web Development
url: /it-324/
---

## HTML Basics: Table of Contents

1. **What is HTML?**
   - Introduction and purpose of HTML
   - Basic structure of an HTML document

2. **HTML Elements and Tags**
   - `<html>`, `<head>`, `<body>`
   - Paragraphs (`<p>`), headings (`<h1>` to `<h6>`)
   - Line breaks (`<br>`), horizontal lines (`<hr>`)

3. **Text Formatting Tags**
   - Bold (`<b>`), italic (`<i>`), underline (`<u>`)
   - Superscript (`<sup>`) and subscript (`<sub>`)

4. **Links and Anchors**
   - `<a href="URL">Link text</a>`
   - Opening links in a new tab

5. **Images**
   - `<img src="image.jpg" alt="description">`
   - Setting width, height, and alignment

6. **Lists**
   - Ordered lists (`<ol>`), unordered lists (`<ul>`), and list items (`<li>`)

7. **Tables**
   - `<table>`, `<tr>`, `<td>`, `<th>`
   - Table borders, rowspan, colspan

## Example #1: HTML Comments

```html
    <!-- This is a comment -->
  

    <!-- The next line displays a paragraph -->
  
    <!-- 
        Multi-line comments are also possible.
        You can use this to explain code in detail or temporarily disable code.
    -->
```

The `<meta>` tag is used in HTML to provide metadata about the web page. The `viewport` and `content` attributes are commonly used for controlling the page's layout on different devices, especially mobile devices. See For more details, see [Appendix A](#appendix-a-meta-tags-for-responsive-design)

## Example #2: Standard HTML Document Structure

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Hello world</title>
</head>

<body>
    <!-- This is a comment -->
    <p> "You only live once, 
        but if you do it right, once is enough."
        - Mae West
    </p>
</body>
</html>
```

## Task #1: Create a Simple Webpage with Line Breaks

**Objective**: Learn how to use the `<br>` tag in HTML to create line breaks in a webpage.

**Steps**:

1. Open your text editor (like Notepad, Visual Studio Code, etc.) and create a new HTML file named `index.html`.
   
2. Add the basic HTML structure to your file:
   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Line Breaks Example</title>
   </head>
   <body>
       <h1>Welcome to My Webpage!</h1>
   </body>
   </html>
   ```

3. Inside the `<body>` tag, add a short paragraph about your favorite hobby. After each sentence, use the `<br>` tag to create a line break.

   Example:
   ```html
   <p>My favorite hobby is painting.<br>
   I love using watercolors.<br>
   It helps me relax and express myself creatively.<br></p>
   ```

4. Save the file and open it in a web browser to see the result. You should see the sentences appear on different lines.

## Task #2: Create a Webpage with Blockquotes

**Objective**: Learn how to use the `<blockquote>` tag to highlight and format quotations in HTML.

**Steps**:

1. Open your text editor (like Notepad, Visual Studio Code, etc.) and create a new HTML file named `blockquote_example.html`.

2. Add the basic HTML structure to your file:
   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Blockquote Example</title>
   </head>
   <body>
       <h1>Famous Quotes</h1>
   </body>
   </html>
   ```

3. Inside the `<body>` tag, add a famous quote using the `<blockquote>` tag. A blockquote is used to display a quote from an external source, usually with indentation or styling applied by the browser.

   Example:
   ```html
   <h2>Albert Einstein</h2>
   <blockquote>
       "Life is like riding a bicycle. To keep your balance, you must keep moving."
   </blockquote>

   <h2>Isaac Newton</h2>
   <blockquote>
       "If I have seen further, it is by standing on the shoulders of giants."
   </blockquote>
   ```

4. Optionally, you can add a `<footer>` tag inside the blockquote to specify the source or author of the quote:
   ```html
   <blockquote>
       "The only way to do great work is to love what you do."
       <footer>- Steve Jobs</footer>
   </blockquote>
   ```

5. Save the file and open it in a web browser. You should see the quotes formatted with indentation and any additional styles applied by the browser.

## Task #3: Create a Structured Webpage Using Different Heading Levels

**Objective**: Understand how to use different heading levels in HTML to organize content into sections and subsections.

**Steps**:

1. Open your text editor (like Notepad, Visual Studio Code, etc.) and create a new HTML file named `structured_headings.html`.

2. Add the basic HTML structure to your file:
   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Structured Webpage Example</title>
   </head>
   <body>
       <h1>My Personal Blog</h1>
   </body>
   </html>
   ```

3. Inside the `<body>` tag, create sections for different categories of content using appropriate heading tags. Each section will have a main heading, a subsection, and some content below it. Example:

   ```html
   <h1>My Personal Blog</h1>

   <h2>Introduction</h2>
   <p>Welcome to my blog! Here, I share my thoughts on various topics including technology, lifestyle, and art.</p>

   <h2>Technology</h2>
   <h3>Latest Gadgets</h3>
   <p>Technology is evolving rapidly, and new gadgets are being released every year. In this section, I will review the latest gadgets and provide my opinion.</p>
   <h4>Smartphones</h4>
   <p>The new smartphones are faster and more powerful than ever before. In my latest post, I will compare the top models of the year.</p>
   <h4>Laptops</h4>
   <p>Laptops continue to be essential for both work and play. I will explore which laptops are the best for productivity and gaming.</p>

   <h3>Tech Tutorials</h3>
   <p>In this section, I provide easy-to-follow guides on various tech topics. From building a website to learning how to code, you’ll find it all here.</p>

   <h2>Lifestyle</h2>
   <h3>Health & Fitness</h3>
   <p>Maintaining a healthy lifestyle is key. Here, I discuss exercise routines, healthy eating, and mental well-being.</p>
   <h4>Yoga</h4>
   <p>Yoga is great for both mental and physical health. I’ll share some basic routines you can do at home.</p>
   <h4>Nutrition</h4>
   <p>A balanced diet is important for overall health. I’ll provide tips on what foods to include in your daily diet.</p>

   <h3>Travel</h3>
   <p>Explore new places and cultures! I share travel tips, stories, and recommendations for your next adventure.</p>

   <h2>Art</h2>
   <h3>Painting</h3>
   <p>Art has always been a passion of mine. In this section, I share my painting projects and techniques.</p>
   <h4>Watercolors</h4>
   <p>Watercolor painting is both challenging and rewarding. I’ll guide you through creating your own beautiful watercolor pieces.</p>
   <h4>Digital Art</h4>
   <p>Digital art allows for endless creativity. I explore various software tools and techniques for creating digital masterpieces.</p>
   ```

4. Save the file and open it in a web browser. You will see that the content is now organized with different heading levels, giving the webpage a clear structure.

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

## Task: HTML Entities

**Basic Entities**

1. Create a new HTML file.
2. In the `<body>` section, write a sentence that includes:
   * An ampersand (&)
   * The less than symbol (<)
   * The greater than symbol (>)
   * A double quote (")
   * A single quote (')
3. Use the correct HTML entities to display these characters. 
4. View the file in your web browser to check if the characters are displayed correctly.

**Quotations and Special Symbols**

1. Create a paragraph element (`<p>`).
2. Inside the paragraph, write a short quote. 
3. Use the appropriate entity for the opening and closing double quotes.
4. Add the copyright symbol (©) at the end of the quote.
5. Add the Euro symbol (€) in a separate sentence.

**Non-Breaking Space**

1. Write a sentence that includes the phrase "100 meters".
2. Use a non-breaking space entity (`&nbsp;`) between "100" and "meters".

**Degree Symbol**

1. Write a sentence that mentions a temperature, for example, "The temperature is 25 degrees Celsius."
2. Use the correct HTML entity to display the degree symbol (°).

**Example (First Few Lines):**

```html
<!DOCTYPE html>
<html>
<head>
  <title>HTML Entity Practice</title>
</head>
<body>

<p>This is a sentence with an ampersand (&amp;), 
less than (&lt;), greater than (&gt;), 
double quotes (&quot;), and single quotes (&apos;).</p>

</body>
</html>
```
## Font Styles and Sizes

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTML Formatting Tags Example</title>
</head>
<body>

    <p>This is an <em>emphasized</em> text.</p>
    <p>This is a <strong>strong and important</strong> text.</p>
    <p>Here is a <code>code snippet</code> inside a paragraph.</p>
    <p>This is a <mark>highlighted</mark> text.</p>
    <p>This is a superscript example: x<sup>2</sup> + y<sup>2</sup> = z<sup>2</sup></p>
    <p>This is a subscript example: H<sub>2</sub>O (water).</p>

</body>
</html>
```

## Example: Images

```html
<!DOCTYPE html>
<!–– image.html An example to illustrate an image ––>
    <html lang="en">

    <head>
        <title> Images </title>
        <meta charset="utf-8" />
    </head>

    <body>
        <h1> Aidan's Airplanes </h1>
        <h2> The best in used airplanes </h2>
        <h3> "We've got them by the hangarful" </h3>
        <h2> Special of the month </h2>
        <!-- ******** -->
        <!-- add Image - image source (freepik) -->
        <!-- ******** -->

        <img src="flowers.jpg" width="400" height="200" alt="alternate text"/>
       
        <p>
            1960 Cessna 210 <br />
            577 hours since major engine overhaul<br />
            1022 hours since prop overhaul <br /><br />
        <img src="images/marketing-strategy-planning-strategy-concept.jpg"  alt="Picture of a Cessna 210" width="800" height="600"/>
            <br />
            Buy this fine airplane today at a remarkably low price
            <br />
            Call 999-555-1111 today!
        </p>
        <img src="https://placehold.co/600x400" alt="placeholder image" />
    </body>

    </html>
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

## Example: Links

```html
    <!DOCTYPE html>
<!–– link.html An example to illustrate a link ––>
    <html lang="en">

    <head>
        <title> A link </title>
        <meta charset="utf-8" />
    </head>

    <body>
        <h1> Aidan's Airplanes </h1>
        <h2> The best in used airplanes </h2>
        <h3> "We've got them by the hangarful" </h3>
        <h2> Special of the month </h2>
        <h2><a href="link2.html#css5"> Intro. to CSS</a></h2>
        <p>
            1960 Cessna 210 <br />
            <a href="mypag1.html"> My Page 1 </a>
        </p>
        <a href="pdf/html-slides.pdf">Download - All Slides of HTML</a><br>

        <a href="https://www.urdupoint.com/names/boys-names/meem.html">
            Urdu Point
        </a>
        <br>
        <a href="https://www.urdupoint.com/names/boys-names/meem.html">
            <img src="images/com.jpg" alt="An image of a small airplane" width="800" height="600" />
        </a>
    </body>

    </html>
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1 id="top">Contents</h1>
    <h2>Web Basics </h2>
    <h2>Intro to Visual Studio Code </h2>
    <h2>Intro to HTML </h2>
    <h2>Intro to JavaScript </h2>

    <h2><a href="#css5"> Intro to CSS </a> </h2>

    <h1>Web Basics </h1>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptate esse, quod deserunt voluptates, culpa dolores tenetur quam quasi molestiae illum neque quo error ratione, at fuga repudiandae. Itaque, quae dolorum.</p>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Consequuntur, dicta dolorum numquam dolore quo laborum? Nam repellat, saepe corporis dolorum facilis enim, tenetur laboriosam provident omnis fuga ex temporibus aspernatur.</p>
    <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Tempora vel cumque debitis quod deleniti iste soluta dolorem similique molestiae, fugit sequi ratione! Magni odit eius maiores libero ut consequuntur facere.</p>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptate esse, quod deserunt voluptates, culpa dolores tenetur quam quasi molestiae illum neque quo error ratione, at fuga repudiandae. Itaque, quae dolorum.</p>
    <h1>Intro to Visual Studio Code </h1>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Consequuntur, dicta dolorum numquam dolore quo laborum? Nam repellat, saepe corporis dolorum facilis enim, tenetur laboriosam provident omnis fuga ex temporibus aspernatur.</p>
    <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Tempora vel cumque debitis quod deleniti iste soluta dolorem similique molestiae, fugit sequi ratione! Magni odit eius maiores libero ut consequuntur facere.</p>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptate esse, quod deserunt voluptates, culpa dolores tenetur quam quasi molestiae illum neque quo error ratione, at fuga repudiandae. Itaque, quae dolorum.</p>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Consequuntur, dicta dolorum numquam dolore quo laborum? Nam repellat, saepe corporis dolorum facilis enim, tenetur laboriosam provident omnis fuga ex temporibus aspernatur.</p>
    <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Tempora vel cumque debitis quod deleniti iste soluta dolorem similique molestiae, fugit sequi ratione! Magni odit eius maiores libero ut consequuntur facere.</p>
    <h1>Intro to HTML </h1>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptate esse, quod deserunt voluptates, culpa dolores tenetur quam quasi molestiae illum neque quo error ratione, at fuga repudiandae. Itaque, quae dolorum.</p>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Consequuntur, dicta dolorum numquam dolore quo laborum? Nam repellat, saepe corporis dolorum facilis enim, tenetur laboriosam provident omnis fuga ex temporibus aspernatur.</p>
    <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Tempora vel cumque debitis quod deleniti iste soluta dolorem similique molestiae, fugit sequi ratione! Magni odit eius maiores libero ut consequuntur facere.</p>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptate esse, quod deserunt voluptates, culpa dolores tenetur quam quasi molestiae illum neque quo error ratione, at fuga repudiandae. Itaque, quae dolorum.</p>
    <h1>Intro to JavaScript </h1>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Consequuntur, dicta dolorum numquam dolore quo laborum? Nam repellat, saepe corporis dolorum facilis enim, tenetur laboriosam provident omnis fuga ex temporibus aspernatur.</p>
    <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Tempora vel cumque debitis quod deleniti iste soluta dolorem similique molestiae, fugit sequi ratione! Magni odit eius maiores libero ut consequuntur facere.</p>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptate esse, quod deserunt voluptates, culpa dolores tenetur quam quasi molestiae illum neque quo error ratione, at fuga repudiandae. Itaque, quae dolorum.</p>
    
    <h1 id="css5">Intro to CSS <a href="#top">Top</a> </h1> 
    
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Consequuntur, dicta dolorum numquam dolore quo laborum? Nam repellat, saepe corporis dolorum facilis enim, tenetur laboriosam provident omnis fuga ex temporibus aspernatur.</p>
    <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Tempora vel cumque debitis quod deleniti iste soluta dolorem similique molestiae, fugit sequi ratione! Magni odit eius maiores libero ut consequuntur facere.</p>
    
</body>
</html>
```

content generated using [https://www.lipsum.com/](https://www.lipsum.com/)

**Task: Create a Blog Post with Styled Text**

1. **Create a new HTML file** and name it `blog_post.html`.
2. Inside the `blog_post.html` file, do the following:
    - Create the basic HTML structure (`<!DOCTYPE html>`, `<html>`, `<head>`, and `<body>`).
    - Add a title to the webpage in the `<head>` section.
    - Inside the `<body>`, add the following elements:
        - A main heading (`<h1>`) with the title of your blog post.
        - A subheading (`<h2>`) for the post subtitle.
        - Add a paragraph (`<p>`) with a brief introduction to your blog post.
        - Add another paragraph that describes a topic, and use:
            - `<strong>` to highlight important text.
            - `<em>` to emphasize some text.
            - `<mark>` to highlight text that is important.
        - Add a blockquote (`<blockquote>`) to include a quote.
        - Add a list (`<ul>` or `<ol>`) of key points related to your blog topic.
        - Add a link (`<a>`) to a related website.

**Example structure:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>My Blog Post</title>
</head>
<body>
    <h1>My First Blog Post</h1>
    <h2>Exploring HTML Text Elements</h2>
    <p>Welcome to my blog post! In this post, I'll be discussing various HTML text elements and how to style them.</p>
    <p><strong>HTML</strong> is the foundation of web pages, and knowing how to format text is essential for building content-rich pages.</p>
    <p>Here are some ways to style text in HTML:</p>
    <ul>
        <li>Use <em>emphasis</em> for words you want to stress.</li>
        <li>Highlight <mark>important points</mark> with <mark>mark</mark>.</li>
        <li><strong>Strong</strong> is used for key terms.</li>
    </ul>
    <blockquote>
        "The best way to predict the future is to create it." – Abraham Lincoln
    </blockquote>
    <p>For more on HTML, visit <a href="https://www.w3schools.com/html/">W3Schools</a>.</p>
</body>
</html>
```

## Task #2: Create a Personal Webpage

1. **Create a new HTML file** and name it `index.html`.
2. Inside the `index.html` file, do the following:
    - Create the basic structure of an HTML document with `<!DOCTYPE html>`, `<html>`, `<head>`, and `<body>`.
    - Add a title to the webpage in the `<head>` section.
    - In the `<body>`, create a heading (`<h1>`) with your name.
    - Add a short paragraph (`<p>`) about yourself.
    - Insert an image of yourself (or anything you'd like) using the `<img>` tag.
    - Add a link (`<a>`) to your favorite website (e.g., Google, Wikipedia).
    - Create a simple list (`<ul>` or `<ol>`) of your favorite hobbies or things you like.

**Example structure:**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Personal Webpage</title>
</head>
<body>
    <h1>John Doe</h1>
    <p>Hello! My name is John, and I love learning about web development.</p>
    <img src="path_to_image.jpg" alt="A picture of me">
    <h2>My Hobbies:</h2>
    <ul>
        <li>Coding</li>
        <li>Reading books</li>
        <li>Traveling</li>
    </ul>
    <p>Check out my favorite website: <a href="https://www.example.com">Click here</a></p>
</body>
</html>
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

# **HTML Lists: Ordered, Unordered, and Definition Lists**

## **1. Ordered List (`<ol>`)**
An **Ordered List** is used when the order of the items matters. It is displayed with numbers or other sequence indicators (e.g., Roman numerals, letters).

### **Syntax:**
```html
<ol>
    <li>Wake up</li>
    <li>Brush your teeth</li>
    <li>Eat breakfast</li>
</ol>
```
### **Output:**
1. Wake up  
2. Brush your teeth  
3. Eat breakfast  

### **Types of Ordered Lists:**
You can change the numbering style using the `type` attribute.
```html
<ol type="A"> <!-- Uppercase Letters -->
    <li>Apple</li>
    <li>Banana</li>
    <li>Cherry</li>
</ol>
```
#### **Other types:**
- `type="1"` → Default (1, 2, 3, ...)  
- `type="A"` → Uppercase letters (A, B, C, ...)  
- `type="a"` → Lowercase letters (a, b, c, ...)  
- `type="I"` → Uppercase Roman numerals (I, II, III, ...)  
- `type="i"` → Lowercase Roman numerals (i, ii, iii, ...)  

---

## **2. Unordered List (`<ul>`)**
An **Unordered List** is used when the order of the items does not matter. It is displayed with bullet points.

### **Syntax:**
```html
<ul>
    <li>Milk</li>
    <li>Bread</li>
    <li>Eggs</li>
</ul>
```
### **Output:**
- Milk  
- Bread  
- Eggs  

### **Types of Bullets:**
You can change the bullet style using the `type` attribute.
```html
<ul type="square">
    <li>Apple</li>
    <li>Banana</li>
    <li>Cherry</li>
</ul>
```
#### **Other types:**
- `type="disc"` → Default (●)  
- `type="square"` → Square bullets (■)  
- `type="circle"` → Hollow circle (○)  

---

## **3. Definition List (`<dl>`)**
A **Definition List** is used for defining terms with their descriptions.

### **Syntax:**
```html
<dl>
    <dt>HTML</dt>
    <dd>HyperText Markup Language - used for creating web pages.</dd>

    <dt>CSS</dt>
    <dd>Cascading Style Sheets - used for styling web pages.</dd>
</dl>
```
### **Output:**
**HTML**  
&nbsp;&nbsp;&nbsp;&nbsp;HyperText Markup Language - used for creating web pages.  

**CSS**  
&nbsp;&nbsp;&nbsp;&nbsp;Cascading Style Sheets - used for styling web pages.  

### **Elements in a Definition List:**
- `<dl>` → Definition List container  
- `<dt>` → Term (word or phrase)  
- `<dd>` → Description (explanation of the term)  

---

## **Key Differences**
| List Type      | Purpose | Example |
|---------------|---------|---------|
| Ordered List (`<ol>`) | Sequence matters | Steps to follow in a recipe |
| Unordered List (`<ul>`) | Order doesn't matter | Grocery shopping list |
| Definition List (`<dl>`) | Provides definitions | Glossary of terms |

---

### Example: Ordered List

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Document</title>
</head>

<body>

    <!-- Read more: https://html.com/lists/ -->

    <ol>
        <li>Step 1</li>
        <li>Step 2</li>
        <li>Step 3</li>
    </ol>

    <ol reversed>
        <li>Item 3</li>
        <li>Item 2</li>
        <li>Item 1</li>
    </ol>
    <ol>
        <li>Step 1</li>
        <li>Step 2</li>
    </ol>

    <p>A few short sentences about Item 2 that we don't want to appear appended to the list item. A second sentence of
        additional details</p>

    <ol start="3">
        <li>Step 3</li>
        <li>Step 4</li>
    </ol>
    <p>Notice that we used the <code>start</code> attribute on the <code>ol</code> tag to restart the numbering at "3"
        following the break in the list above. We'll use the same technique to properly number Step 5 below.</p>
    <ol start="5">
        <li>Step 5</li>
    </ol>
</body>

</html>
```

### **Beginner Tasks for HTML Lists**

#### **Task 1: Create an Ordered List**
- Create an HTML file and write an ordered list of **your daily routine**.
- Use different numbering types (`1`, `A`, `a`, `I`, `i`).
- Try using the `start` and `reversed` attributes.

#### **Task 2: Create an Unordered List**
- Make an unordered list of **your favorite foods**.
- Change the bullet style using `type="disc"`, `type="square"`, and `type="circle"`.

#### **Task 3: Create a Definition List**
- Write a definition list explaining at least **three web technologies** (e.g., HTML, CSS, JavaScript).
- Add short descriptions for each term.

#### **Task 4: Combine Lists**
- Create a webpage that includes:
  1. An ordered list of **steps to cook your favorite dish**.
  2. An unordered list of **ingredients needed**.
  3. A definition list explaining **at least two cooking terms**.

#### **Task 5: Experiment with Nested Lists**
- Create a nested list where:
  - The main list is an **ordered list** of different countries.
  - Each country has an **unordered list** of at least **three famous cities**.


### **HTML Tables Explained for Beginners**

An **HTML table** is used to display data in rows and columns. It is created using the `<table>` tag, and each row is defined using the `<tr>` (table row) tag. Inside rows, data is placed within `<td>` (table data) tags, and headings are defined with `<th>` (table header) tags.

---

### **Basic Structure of an HTML Table**
```html
<table>
    <tr>
        <th>Heading 1</th>
        <th>Heading 2</th>
        <th>Heading 3</th>
    </tr>
    <tr>
        <td>Row 1, Data 1</td>
        <td>Row 1, Data 2</td>
        <td>Row 1, Data 3</td>
    </tr>
    <tr>
        <td>Row 2, Data 1</td>
        <td>Row 2, Data 2</td>
        <td>Row 2, Data 3</td>
    </tr>
</table>
```

### **Explanation:**
- `<table>` → Defines the table.
- `<tr>` → Represents a row in the table.
- `<th>` → Creates a **header cell** (bold text by default).
- `<td>` → Creates a **regular data cell**.

---

### **Example: A Simple Student Marks Table**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Student Marks Table</title>
</head>
<body>

    <h2>Student Marks</h2>

    <table border="1">
        <tr>
            <th>Student Name</th>
            <th>Subject</th>
            <th>Marks</th>
        </tr>
        <tr>
            <td>Hamza</td>
            <td>Math</td>
            <td>85</td>
        </tr>
        <tr>
            <td>Muhammmad</td>
            <td>Science</td>
            <td>90</td>
        </tr>
        <tr>
            <td>Ali</td>
            <td>English</td>
            <td>88</td>
        </tr>
    </table>

</body>
</html>
```

### **Beginner HTML Table Tasks**  

#### **Task 1: Create a Basic Table**  
- Create an HTML table with **three columns**: `Product Name`, `Price`, and `Quantity`.  
- Add at least **three rows of data**.  

---

#### **Task 2: Add a Table Header**  
- Modify your previous table by adding **bold headers** (`<th>`).  
- Example headers: `Name`, `Age`, `City`.  

---

#### **Task 3: Add a Table Border**  
- Apply the `border="1"` attribute to make the table **visible with borders**.  

---

#### **Task 4: Create a Student Report Card**  
- Make an HTML table with the following columns:  
  - `Student Name`
  - `Math`
  - `Science`
  - `English`
  - `Total Marks`  
- Add at least **three students’ scores** in rows.  

---

### **Example of `colspan` and `rowspan` in an HTML Table**  

#### **1. Using `colspan` (Merging Columns)**
The `colspan` attribute is used to merge multiple columns into one.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Colspan Example</title>
</head>
<body>

    <h2>Colspan Example</h2>
    
    <table border="1">
        <tr>
            <th colspan="3">Student Information</th>
        </tr>
        <tr>
            <th>Name</th>
            <th>Age</th>
            <th>Grade</th>
        </tr>
        <tr>
            <td>John</td>
            <td>15</td>
            <td>A</td>
        </tr>
        <tr>
            <td>Emma</td>
            <td>14</td>
            <td>B</td>
        </tr>
    </table>

</body>
</html>
```

### **Explanation of `colspan`:**
- The first row has a **single merged header** spanning **three columns** using `colspan="3"`.
- Below it, the normal table structure is followed.

---

#### **2. Using `rowspan` (Merging Rows)**
The `rowspan` attribute is used to merge multiple rows into one.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Rowspan Example</title>
</head>
<body>

    <h2>Rowspan Example</h2>
    
    <table border="1">
        <tr>
            <th>Name</th>
            <th rowspan="2">Subject</th>
            <th>Marks</th>
        </tr>
        <tr>
            <td>John</td>
            <td>85</td>
        </tr>
        <tr>
            <td>Emma</td>
            <td>Science</td>
            <td>90</td>
        </tr>
    </table>

</body>
</html>
```

### **Explanation of `rowspan`:**
- The **"Subject" header spans two rows** using `rowspan="2"`.
- This means **John’s row does not have a separate "Subject" cell** as it is merged with the one above.

---

### **When to Use `colspan` and `rowspan`**
- **Use `colspan`** when you want a **single cell to stretch across multiple columns**.
- **Use `rowspan`** when you want a **single cell to stretch across multiple rows**.


### **Task 5: Create a Table with Merged Cells**  

#### **Objective:**  
- Use `colspan` to merge multiple **columns** into one.  
- Use `rowspan` to merge multiple **rows** into one.  
- Create a **school timetable** where a subject spans multiple time slots.  

### **Sample Output:**
#### **School Timetable**
| Day       | Start   | End     | Subject  |
|-----------|--------|--------|-----------|
| **Monday**  | 9:00 AM | 10:00 AM | Math     |
|            | 10:00 AM | 11:00 AM | Science  |
| **Tuesday** | 9:00 AM | 10:00 AM | **English** (Merged for 2 Rows) |
|            | 10:00 AM | 11:00 AM | |
| **Break Time (Spanning all columns)** |
| **Wednesday** | 9:00 AM | 10:00 AM | History  |

---

### **Explanation of `colspan` and `rowspan` Usage:**
1. **Using `rowspan`:**  
   - The **"Day" column** merges rows for Monday and Tuesday (`rowspan="2"`).  
   - The **English subject** spans **two rows** (`rowspan="2"`) since it takes up **two time slots**.  

2. **Using `colspan`:**  
   - The **header row** has `colspan="2"` for the time slot (Start & End).  
   - The **Break Time row** spans **all four columns** using `colspan="4"`.  


---

### **Key Points in This Example:**
- The `border="1"` attribute adds a border to the table for better visibility.
- The first row contains **header cells** (`<th>`) for column titles.
- Each following row contains **data cells** (`<td>`) with student names, subjects, and marks.

{% assign topic = "html-basics" %}
{% include practice-and-progress.html topic=topic %}

## References and Bibliography

[1] MDN Web Docs, “HTML: HyperText Markup Language,” MDN Web Docs, Dec. 10, 2018. <https://developer.mozilla.org/en-US/docs/Web/HTML>
[2] “HTML elements reference,” MDN Web Docs, Jun. 06, 2019. <https://developer.mozilla.org/en-US/docs/Web/HTML/Element>
‌
‌

For more details, see Appendix A.

## **Appendices**

### **Appendix A: Meta Tags for Responsive Design**

The `<meta>` tag is used in HTML to provide metadata about the web page. The `viewport` and `content` attributes are commonly used for controlling the page's layout on different devices, especially mobile devices.

Here’s an example of how to use the `viewport` meta tag:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Viewport Meta Tag Example</title>
</head>
<body>

    <h1>Responsive Web Page</h1>
    <p>This page will adapt to different screen sizes.</p>

</body>
</html>
```

**Breakdown of the `meta` tag:**

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

- **`name="viewport"`**: Specifies that this meta tag is for controlling the viewport settings.
- **`content="width=device-width, initial-scale=1.0"`**:
  - **`width=device-width`**: The width of the viewport will match the width of the device's screen.
  - **`initial-scale=1.0`**: This sets the initial zoom level when the page is first loaded. `1.0` means no zoom.

**Why it's important:**

- It helps ensure your page is responsive, meaning it will adjust to different screen sizes, such as on desktops, tablets, and smartphones.
- Without this tag, mobile devices might display the page zoomed out or not properly scaled, making the content hard to read.

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

