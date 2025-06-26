---
layout: page
title: "Python Basics: Find and Fix Mistakes"
description: "Sharpen your Python basics by identifying and fixing common coding errors. Perfect for beginners to enhance problem-solving skills and reinforce programming fundamentals."
toc: toc/python.html
course: python
topic: basics
show_toc: true
show_practice_progress: true
show_mini_project: false
breadcrumb:
  - title: Home
    url: /
  - title: Python
    url: /python/
  - title: Basics
    url: /python/docs/basics/
---

## Question 1: Fix the Parenthesis Error
**Task**: Identify and fix the syntax error in the following code snippet.

```python
print("Hello World!"
```

**Error**: SyntaxError: The closing parenthesis is missing.

**Corrected Code**:
```python
print("Hello World!")
```

---

## Question 2: Fix the Indentation Error [Python Quiz #67]
**Task**: Fix the indentation error in the following code snippet.

```python
if True:
  print("Hello")
    print("World")
```

**Error**: `IndentationError: unexpected indent` at the second print statement.

---

## Question 3: Fix the Incorrect Variable Usage Error [Python Quiz 68]
**Task**: Fix the error where the variable name is incorrectly used.

```python
name = "Ahmad"
print(f"My name is {namee} and I am 30 years old.")
```

**Error**: `NameError: name 'namee' is not defined` because `namee` is not the correct variable name.

---

## Question 3: Fix the Missing Import Error
**Task**: Correct the following code by adding the necessary module import.

```python
print(os.getcwd())
```

**Error**: `NameError: name 'os' is not defined` because the `os` module was not imported.

**Corrected Code**:
```python
import os
print(os.getcwd())
```

---

## Question 5: Fix the File Output Error
**Task**: Fix the syntax issue in printing to a file.

```python
with open("output.txt", "w") as file:
print("Hello, file!", file=file)
```

**Error**: `IndentationError: expected an indented block` because the print statement is not indented.

**Corrected Code**:
```python
with open("output.txt", "w") as file:
    print("Hello, file!", file=file)
```

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1602443888929206"
     crossorigin="anonymous"></script>
<ins class="adsbygoogle"
     style="display:block"
     data-ad-format="autorelaxed"
     data-ad-client="ca-pub-1602443888929206"
     data-ad-slot="7879511511"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>