---
layout: page
title: "Python `print` Function"
description: Learn how to handle Python errors and exceptions effectively. Fix common Python errors like SyntaxError, TypeError, and NameError with practical examples.
keywords: Python errors, Python exceptions, fix Python errors, SyntaxError Python, TypeError Python, NameError Python, Python error handling, Python debugging, Python try-except, Python exception handling
toc: toc/python.html
---

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
