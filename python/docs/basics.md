---
layout: page
title: Python Basics - Beginner-Friendly Tutorials, Examples, and Exercises  
description: Learn Python basics with beginner-friendly tutorials, examples, and exercises. Master Python programming concepts like print function, variables, comments, indentation and more. Perfect for students and professionals starting their Python journey.  
keywords: Python basics, Python tutorials for beginners, Python examples, Python exercises, Python print function, python comments Python variables, Python data types, Python programming for beginners, learn Python, Python coding exercises
toc: toc/python-toc.html
---

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

## Lesson 1: Python `print` Function

### Objectives
- Understand the basic usage of the `print` function.
- Learn how to print different data types.
- Explore advanced `print` function features like formatting and special characters.
- Practice printing in various tasks.

### Introduction to `print`

The `print` function is used to output text or variables to the console. or to a file.

[Video: Use of print() function in python](https://youtu.be/RSSSyqw79_M)

**Syntax:**

```python
print(value1, value2, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
```

**Parameters:**
- `value1, value2, ...`: The values to be printed. Multiple values can be separated by commas.
- `sep`: (Optional) Specifies how to separate multiple values. Default is a space `' '`.
- `end`: (Optional) Specifies what to print at the end. Default is a newline character `'\n'`.
- `file`: (Optional) Specifies the file where to print. Default is `sys.stdout` (console).
- `flush`: (Optional) Specifies whether to forcibly flush the stream. Default is `False`.

### Task 1: Basic Printing

**Instructions:**
1. Print a simple message.
2. Print multiple items separated by commas.

**Examples**
```python
# Task 1.1: Print a simple message
print("Hello, world!")

# Task 1.2: Print multiple items
print("Hello", "world", 2024)
```

### Task 2: Printing Different Data Types

**Instructions**
1. Print integers, floats, and strings.

**Examples**

```python
# Task 2.1: Print different data types
print(42)
print(3.14159)
print("This is a string")

```

### Task 3: Using `sep` and `end` Parameters

**Instructions**
1. Change the separator between printed items.
2. Change the ending character of a print statement.

**Examples**
```python
# Task 3.1: Change the separator
print("apple", "banana", "cherry", sep=", ")

# Task 3.2: Change the ending character
print("Hello", end=" ")
print("world!")

# Task 3.3: Print with a custom ending character:
print("Hello", "World", end="!")

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

### Task 4: Print Variables

**Instructions**
- print variables values using print function

```python

# Task 4.1: print a integer variable
x = 5
print(x)

# Task 4.2: print a string variable
message = 'Python is fun'

# print the string message
print(message)

# Task 4.3: print a string variable
message = "How are you?"
print(message)

```
### Task 5: String Formatting with f-Strings

**Instructions**
1. Use f-strings (formatted string literals) for the same purpose.

**Examples**
```python
# Task 5.1: Use f-strings
name = "Ahmad"
age = 30
print(f"My name is {name} and I am {age} years old.")
```

[Python f-Strings Explained: What Does print(f'{a=}') Do?](https://youtube.com/shorts/a34qr0OfxjQ)

The expression print(f"{a=}") is part of Python's f-string formatting introduced in Python 3.8.

When you use a=, Python prints both the name of the variable and its value. Essentially, it shows what the variable is and its corresponding value.

### Task 6: Printing Special Characters

**Instructions**
1. Print a newline character within a string.
2. Print a tab character within a string.

**Examples**
```python
# Task 6.1: Print a newline character
print("Hello\nWorld")

# Task 6.2: Print a tab character
print("Hello\tWorld")
```

[video: Python line break: How to Print Line Break](https://youtube.com/shorts/Iqb5MQmeksM)

```python
# Task 6.3: Print a tab character

print("Name\tAge\tCity")
print("Alice\t30\tNew York")
print("Bob\t25\tLos Angeles")
```

Output:
```
Name    Age    City
Alice   30     New York
Bob     25     Los Angeles
```
In this example, `\t` is used to align the columns of text.

In Python, the `\t` character is a special escape sequence that represents a horizontal tab. When used in the `print` function or any other string operation, it inserts a tab space in the output. This can be particularly useful for formatting text to make it more readable.

 `\t` can be combined with other string manipulation techniques, such as f-strings

```python



# Task 6.4: Print a tab character with f-strings

name = "Alice"
age = 30
city = "New York"

print(f"{name}\t{age}\t{city}")
```

### Task 7: Printing to a File

**Instructions**
1. Print a message to a text file instead of the console.

**Examples**
```python
# Task 7.1: Print to a file
with open("output.txt", "w") as file:
    print("Hello, file!", file=file)
```
When you use the instruction with open("output.txt", "w") as file in Python, the file is created in the current working directory of your program. On an Android system, this could be different depending on the environment where the code is executed (e.g., a specific app's data directory, a shared storage location, etc.). 

To determine the exact path, you can use the os module to get the current working directory:

```python
import os

print(os.getcwd())
```

Regarding file closure, when you use the `with` statement to open a file, Python automatically takes care of closing the file for you once the block of code under the `with` statement is executed. There is no need to explicitly close the file; it is done automatically when the block is exited. This is one of the benefits of using the with statement for file operations. for more details, see [Understanding Python’s os.getcwd(): Get Current Working Directory with Examples](../posts/getch-python-examples.md)

### Task 8: Understanding Syntax Errors in Python

**Objective:**
Learn about syntax errors in Python by examining and correcting a sample code snippet.

**Instructions:**
1. **Review the Code Snippet**: Look at the provided Python code and identify any syntax errors.
2. **Identify the Error**: Understand what a syntax error is and why it occurs.
3. **Correct the Code**: Fix the syntax error in the code snippet.
4. **Explanation**: Write a brief explanation of what the syntax error was and how you corrected it.

**Code Snippet:**
```python
print("Hello World!"
```

**Steps:**
1. **Review the Code Snippet**: Look carefully at the code snippet above.
2. **Identify the Error**:
   - A syntax error occurs when the Python interpreter finds code that does not conform to the rules of the Python language.
   - The provided code snippet has a syntax error because it has an unmatched parenthesis.
3. **Correct the Code**:
   - To fix the error, ensure all parentheses are properly closed.
   - The corrected code should look like this:
     ```python
     print("Hello World!")
     ```
4. **Explanation**:
   - **Syntax Error**: The error was due to a missing closing parenthesis.
   - **Correction**: Adding the closing parenthesis at the end of the print statement fixes the syntax error.

**Syntax error:**

- A syntax error in programming occurs when the code violates the rules of the programming language's syntax. 
- This means that the code's structure and commands do not conform to the expected format that the interpreter or compiler requires to successfully read and execute the code.

**See also:**

- [Invalid Syntax in Python: Common Reasons for SyntaxError](https://realpython.com/invalid-syntax-python/)
  
### Task 9: Print Your Favorite Quote
- Choose your favorite quote.  
- Use Python’s `print()` function to display it.  
- Ensure the quote is properly formatted (e.g., with quotation marks and correct line breaks if necessary).  

### Task 10: Create a Simple Receipt**  
- Define item names and prices.  
- Use `\t` (tab character) to align item names and prices neatly.  
- Print a simple receipt showing itemized costs.  
- Optionally, include a total cost at the bottom.  

### Task 11: Use Variables in Print Statements**  
- Create three variables: `name`, `age`, and `hobby`.  
- Assign appropriate values to each variable.  
- Use the `print()` function to create a sentence incorporating these variables.  

### Task 12: 100 Times “Hello World” Without Loop**  
- Print "Hello World" 100 times **without using a loop**.  
- Consider string multiplication (`"Hello World\n" * 100`) as a possible solution.  

[related video: 100 times "hello world" without loop](https://www.youtube.com/watch?v=QpqnHtD76BI&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=7)

### Task 13: How to Print Multiple Lines**  
- Print multiple lines of text using different methods:  
  - Using multiple `print()` statements.    
  - Using newline characters (`\n`).  

[Related Video: How to print multiple lines](https://www.youtube.com/watch?v=Y13CX7-zzcQ&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=51)

### Task 14: Output to a File**  
- Write a short summary of your week (tasks completed, hours worked, achievements).  
- Open a text file in write mode (`"w"`).  
- Write the summary to the file using Python’s `write()` method.  
- Close the file properly.  

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

