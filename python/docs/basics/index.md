---
layout: page
title: Python Basics - Beginner-Friendly Tutorials, Examples, and Exercises  
description: Learn Python basics with beginner-friendly tutorials, examples, and exercises. Master Python programming concepts like print function, variables, comments, indentation and more. Perfect for students and professionals starting their Python journey.  
keywords: Python basics, Python tutorials for beginners, Python examples, Python exercises, Python print function, python comments Python variables, Python data types, Python programming for beginners, learn Python, Python coding exercises
toc: toc/python.html
topic: basics
breadcrumb:
  - title: Home
    url: /
  - title: Python
    url: /python/
---

## Table of Contents

- What is Python
- 
## What is Python

- Python is a high-level, general-purpose programming language.
- It is known for its clear syntax, readability, and versatility.
- Python is widely used for `web development`, `data science`, `machine learning`, and `automation`.

## Getting Started

- Install Python: Download and install it from <https://www.python.org/downloads/>.
- Choose a text editor: A program to write code, like [Visual Studio Code](https://code.visualstudio.com/docs/python/python-tutorial), [Jupyter Notebook](https://jupyter.org/install), `PyCharm`, or even a simple text editor like `Notepad`.
- Text editor for Android: [Pydroid 3 - IDE for Python 3](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3)
  - [Video: How to: Install Jupyter Notebook on an Android device](https://youtu.be/b2XNfD3xEwY?si=JFQsMiVj5xqkTgGv)
- Interactive mode: Experiment with Python directly in your terminal or command prompt using the python command.
- [Python IDE Installation](python-ide-installation.md)

> **Important:** Python source code files always use the `.py` extension.

## Comments

- Comments are important for making code more readable and understandable, especially for other programmers who may need to read or modify the code.
- Comments in Python are non-executable lines of code and ignored by the Python interpreter when the code is executed. 

There are two main types of comments in Python:

- **Single-line comments:** These comments start with the hash symbol (#) and extend to the end of the line.

```python
# This is a single-line comment
print("Hello, World!")
```

- **Multi-line comments:** These comments are enclosed in triple quotes (""" or ''').

```python
"""
This is a multi-line comment.
It can span multiple lines of code.
"""
print("Hello, World!")
```

**See also:**

- [Video: A Comprehensive Guide to Single Line & Multi-Line Comments](https://www.youtube.com/watch?v=W7ixMGE2exc&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=73)

## Indentation

In Python, indentation refers to the use of whitespace (spaces or tabs) to denote block-level structure in the code. Python uses indentation to define the scope of code blocks, such as:

- Function definitions
- Loops (for, while)
- Conditional statements (if, elif, else)
- Exception handling (try, except)

In Python, indentation is mandatory and is used to determine the grouping of statements. The number of spaces used for indentation is not fixed, but it's standard to use 4 spaces for each level of indentation. Read more: [Indentation - PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/#indentation)

Here's an example:
```python
if True:
    print("Hello")  # This line is indented with 4 spaces
    print("World")  # This line is also indented with 4 spaces
```
In this example, the two print statements are indented with 4 spaces, indicating that they are part of the if block.

Python's indentation system has several benefits, including:

- Improved readability: Indentation makes the code structure clear and easy to read.
- Reduced errors: Indentation helps avoid errors caused by mismatched braces or parentheses.
- Simplified syntax: Python's indentation system eliminates the need for explicit block delimiters like braces or keywords.

Another example, consider the following code snippet:

```python
if True:
    print("True")
else:
    print("False")
```

**Task: 15** Please correct the following Python code:

```python
if True:
  print("True")
    print("False")
```
Error message: `IndentationError: unexpected indent`"

**See also:**

- [Indentation in Python - geeksforgeeks.org](https://www.geeksforgeeks.org/indentation-in-python/)
- [Indentation in Python (With Examples) - askpython.com](https://www.askpython.com/python/python-indentation)

### **Task 16: Code Together, Lead Together**  

**Title:** "Teach Your Team"  
**Instructions:**  
1. **Each student picks one basic Python topic** (e.g., print function,Basic Printing, Printing Different Data Types,  Using sep and end Parameters, Print Variables, String Formatting with f-Strings, Printing Special Characters, Syntax Error, Comments, Indentation).  
2. **Prepare a 2-minute explanation** for the group (using examples).  
3. **Deliver their explanation** to the team.  
4. **Peers ask questions** and give feedback.  

**💡 Key Learning Points:**  
✔ Leadership through teaching.  
✔ Confidence in public speaking.  
✔ Understanding Python better by explaining it.  

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
   
## Practice & Progress

- [True or False](basics/practice-and-progress/true-false-python-basics.md)
- [Fill in the Blanks](basics/practice-and-progress/fill-blanks-python-basics.md)

---

### Multiple-Choice Questions (MCQs)

- [Python Basics MCQs: Test Your Knowledge](basics/practice-and-progress/mcqs-python-basics.md)

---

### Find and Fix Mistakes

- [Find and Fix Mistakes](basics/practice-and-progress/find-fix-mistakes-computer-basics.md)

✅ **Online Quizzes for Python Basics**

- [Python Basics Quiz](../quizzes/python-basics-quiz.md)

---

### Coding Exercises

- [Python Exercises for Basics](basics/practice-and-progress/coding-exercises-python-basics.md)

---

### Mini Projects

- [Python Basics Mini Project: Build a Simple Expense Tracker](basics/practice-and-progress/mini-project-python-basics.md)

---

### [Review Questions](basics/practice-and-progress/review-questions-python-basics.md)

--- 

## References and Bibliography

- [1] “Guido van Rossum,” Wikipedia, May 24, 2021. https://en.wikipedia.org/wiki/Guido_van_Rossum
- [Indentation in Python - geeksforgeeks.org](https://www.geeksforgeeks.org/indentation-in-python/)
- [Indentation in Python (With Examples) - askpython.com](https://www.askpython.com/python/python-indentation)

