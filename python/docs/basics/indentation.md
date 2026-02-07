---
layout: page
title: Python Indentation
description: Learn Python Indentation
keywords: Python basics, Python tutorials for beginners, python indentation
toc: toc/python.html
topic: basics
breadcrumb: 
- title: Python
url: /python/
---

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

