# Introduction to HTML


Here’s a task that focuses on text elements and text formatting/style in HTML:

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