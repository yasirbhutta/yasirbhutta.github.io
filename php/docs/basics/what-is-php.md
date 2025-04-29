---
layout: page
title: "Introduction to PHP: Basics, Features, and Examples"
description: Learn what PHP is, how it works, and what it can do. This beginner-friendly guide covers PHP basics, file structure, practical uses, and example scripts..
keywords: What is PHP, PHP tutorial, PHP file, PHP examples, PHP code, PHP for beginners, server-side scripting, dynamic web pages, PHPinfo, PHP script, PHP functions
toc: toc/php.html
course: php
topic: "basics"
mini_project: true
---

## What is PHP
- **PHP** (Hypertext Preprocessor) is a widely-used open-source server-side scripting language designed for web development. It can also be used as a general-purpose language.
- It is embedded into HTML to make dynamic web pages. It can interact with databases, handle forms, and much more.

[Learn More About PHP](https://www.php.net/manual/en/intro-whatis.php)

## What is a PHP File?

- PHP files can contain text, HTML, CSS, JavaScript, and PHP code.
- PHP code are executed on the server, and the result is returned to the browser as plain HTML.
- PHP files have extension ".php".

## What Can PHP Do?

- PHP can generate dynamic page content
- PHP can create, open, read, write, delete, and close files on the server
- PHP can collect form data
- PHP can send and receive cookies
- PHP can add, delete, modify data in your database
- PHP can be used to control user-access
- PHP can encrypt data

With PHP you are not limited to output HTML. You can output images, PDF files, and even Flash movies. You can also output any text, such as XHTML and XML.

## Why PHP?

- PHP runs on various platforms (Windows, Linux, Unix, Mac OS X, etc.)
- PHP is compatible with almost all servers used today (Apache, IIS, etc.)
- PHP supports a wide range of databases
- PHP is free. Download it from the official PHP resource: www.php.net
- PHP is easy to learn and runs efficiently on the server side

## **2. PHP Syntax**

### **Basic PHP Syntax**
- PHP code is written between `<?php` and `?>` tags.
- PHP commands end with a semicolon (`;`).
  
### Example: Basic Syntax

```php
<?php
  echo "Hello, World!";  // Output: Hello, World!
?>
```

### **HTML with PHP**
- You can mix PHP and HTML in a webpage. PHP is executed on the server, and the result is sent to the browser.

```php
<!DOCTYPE html>
<html>
<body>
  <?php
    echo "Hello from PHP!";
  ?>
</body>
</html>
```

