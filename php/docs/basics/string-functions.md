---
layout: page
title: "PHP Basics Tutorial – String Functions"
description: Explore common PHP string functions like strlen(), str_word_count(), strrev(), strpos(), and str_replace(). Learn how to use these functions with examples to manipulate strings effectively.
keywords: PHP string functions, PHP strlen(), PHP str_word_count(), PHP strrev(), PHP strpos(), PHP str_replace(), string manipulation in PHP, PHP string examples
toc: toc/php.html
course: php
topic: "basics"
mini_project: true
prev: /php/docs/basics/constants.html
next: /php/docs/basics/comments.html
---

## **Common String Functions**:

- **`strlen()`**: Get the length of a string.
- **`str_word_count()`**: Count the number of words in a string.
- **`strrev()`**: Reverse a string.
- **`strpos()`**: Find the position of a substring.
- **`str_replace()`**: Replace a substring with another.

## Example: String Functions

```php
<?php
echo strlen("Hello World!");  // Output: 12
echo str_word_count("Hello World!");  // Output: 2
echo strrev("Hello World!");  // Output: !dlroW olleH
echo strpos("Hello World!", "World");  // Output: 6
echo str_replace("World", "PHP", "Hello World!");  // Output: Hello PHP!
?>
```
