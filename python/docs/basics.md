# Python: Language Basics

Connect with me: [Youtube](https://www.youtube.com/yasirbhutta) \| [LinkedIn](https://www.linkedin.com/in/yasirbhutta/) \| [WhatsApp Channel](https://whatsapp.com/channel/0029VaC3BC160eBZZSs3CW0c) \| [Web](https://yasirbhutta.github.io/) \| [Facebook](https://www.facebook.com/yasirbhutta786) \| [Twitter](https://twitter.com/yasirbhutta)

- [Download PDF](https://yasirbhutta.github.io/python/docs/basics.pdf)
- To access the updated handouts, please click on the following link:
[https://yasirbhutta.github.io/ms-excel/docs/basics.html](https://yasirbhutta.github.io/ms-excel/docs/basics.html)

- [Python Playlist on Youtube](https://www.youtube.com/playlist?list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja)
- [Download Example Code](https://github.com/yasirbhutta/python-examples)
- [Pyton Resources: Books, Websites, Tutorials](resources.md)
- [Python Tools](tools.md)
- [Python - Quick Guide for Ultimate Python Beginner's](docs/quick-guide.md)

[**Want to Learn Python, Join our WhatsApp Channel ✨:**](https://whatsapp.com/channel/0029VaeGV0517En4iyZGWn2P)

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
### Task 5: String Formatting

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

Regarding file closure, when you use the `with` statement to open a file, Python automatically takes care of closing the file for you once the block of code under the `with` statement is executed. There is no need to explicitly close the file; it is done automatically when the block is exited. This is one of the benefits of using the with statement for file operations. for more details, see [Appendix A](#appendix-a-osgetcwd)

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

### Practice Exercises

#### Exercise 1: Print Your Favorite Quote
Print your favorite quote, ensuring proper formatting.

#### Exercise 2: Create a Simple Receipt
Print a simple receipt with items and prices, properly aligned using tab characters.

#### Exercise 3: Use Variables in Print Statements
Create variables for your name, age, and favorite hobby, then print a sentence using these variables.

#### Exercise 4: Output to a File
Write a program that prints a summary of your week (e.g., tasks completed, hours worked) to a text file.

#### Exercise 5: 100 times "hello world" without loop

[related video: 100 times "hello world" without loop](https://www.youtube.com/watch?v=QpqnHtD76BI&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=7)

#### Exercise 6: How to print multiple lines

[Related Video: How to print multiple lines](https://www.youtube.com/watch?v=Y13CX7-zzcQ&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=51)

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

**Task:** Please correct the following Python code:

```python
if True:
  print("True")
    print("False")
```
Error message: `IndentationError: unexpected indent`"

**See also:**

- [Indentation in Python - geeksforgeeks.org](https://www.geeksforgeeks.org/indentation-in-python/)
- [Indentation in Python (With Examples) - askpython.com](https://www.askpython.com/python/python-indentation)

## Fix the Error

## True/False (Mark T for True and F for False)

1. An indentation error in Python is considered a syntax error.

**Answer Key (True/False):**

1. True
   
## Multiple Choice (Select the best answer)

**Python**

1. **What is Python?**
      - A) A type of snake
      - B) A high-level programming language
      - C) A web browser
      - D) An operating system

   **Answer: B) A high-level programming language**

2. **Which of the following is a popular Integrated Development Environment (IDE) for Python?**
      - A) Visual Studio Code
      - B) Microsoft Word
      - C) Adobe Photoshop
      - D) Google Chrome

   **Answer: A) Visual Studio Code**

3. **Which tool is used for managing and installing Python packages?** [Python Quiz #53]
      - A) pip
      - B) npm
      - C) yarn
      - D) gem

   **Answer: A) pip**

4. **What does IDE stand for in the context of Python programming?**
      - A) Integrated Development Environment
      - B) Integrated Data Environment
      - C) Internal Development Engine
      - D) Internet Development Environment

   **Answer: A) Integrated Development Environment**

5. **What is the purpose of virtual environments in Python?**
      - A) To provide a web-based interface for Python development
      - B) To create isolated environments for different Python projects
      - C) To compile Python code into machine code
      - D) To improve the speed of Python code execution

   **Answer: B) To create isolated environments for different Python projects**

6. **Which tool is used for version control in Python projects?**
      - A) Git
      - B) Docker
      - C) Kubernetes
      - D) Jenkins

   **Answer: A) Git**

7. **Which of the following is the correct extension of the Python file?** [Python Quiz #51]

      - A) .python
      - B) .pl
      - C) .p
      - D)  .py

8. **What is Jupyter Notebook primarily used for in the Python ecosystem?** [Python Quiz #54]
      - A) Web development
      - B) Writing and sharing code, visualizations, and text
      - C) Game development
      - D) Mobile app development

   **Answer: B) Writing and sharing code, visualizations, and text**

9. **Who created Python and in which year?** [1]
      - A) James Gosling in 1995
      - B) Guido van Rossum in 1991
      - C) Bjarne Stroustrup in 1983
      - D) Dennis Ritchie in 1972

   **Answer: B) Guido van Rossum in 1991**

10. **Which of the following features is a key characteristic of Python?** [Python Quiz #52]
      - A) Statically typed
      - B) Compiled language
      - C) Interpreted language
      - D) Requires manual memory management

11. **What is the purpose of the virtual environment tool in Python?**
      - A) To create virtual machines
      - B) To manage and isolate project-specific dependencies
      - C) To design virtual reality experiences
      - D) To develop mobile applications
   
   **Answer: B) To manage and isolate project-specific dependencies**

12. **What is the Python Package Index (PyPI)?**
      - A) A text editor for Python
      - B) A library for machine learning
      - C) A repository of software for the Python programming language
      - D) An IDE for Python development
   
   **Answer: C) A repository of software for the Python programming language**

13. **What is `pip` in Python?**
      - A) A text editor
      - B) A package installer
      - C) A version control system
      - D) A web framework

   **Answer: B) A package installer**

14. **Which tool is commonly used for creating virtual environments in Python?**
      - A) npm
      - B) pip
      - C) venv
      - D) docker

   **Answer: C) venv**

15. **Which Integrated Development Environment (IDE) is specifically designed for Python development?** [Python Quiz #54]
      - A) Visual Studio
      - B) IntelliJ IDEA
      - C) PyCharm
      - D) Eclipse

   **Answer: C) PyCharm**

16. **Which of the following is true about Python?**
      - A) Python is a compiled language
      - B) Python is a low-level programming language
      - C) Python supports object-oriented programming
      - D) Python does not support modules
   
   **Answer: C) Python supports object-oriented programming**

17. **Which of the following is NOT a feature of Python?**
      - A) Interpreted language
      - B) Compiled language
      - C) High-level language
      - D) Object-oriented language

   **Answer: B) Compiled language**

**print function**

[video:Can You Guess the Output of this Python Code? | print Quiz](https://youtu.be/WD92M8WXRZM?si=1FgSE-5Vr1aFCVR-)

**What is the output of the following code?** [Python Quiz #28]

**Code:**

```python
print("I", "love", "Python", sep="-")
```

**Options:**

- A) I-love-Python
- B) I love Python
* C) I, love, Python
* D) Syntax error

**Watch the video for the answer:** [https://youtube.com/shorts/WD92M8WXRZM?si=kJ5jbIAaIlJ_63ia](https://youtube.com/shorts/WD92M8WXRZM?si=kJ5jbIAaIlJ_63ia)

**What will be the output of the following code?** [Python Quiz #29]

```python
x = 5
y = 3
print("The value of x is", x, "and the value of y is", y)
```

   - A) Syntax error
   - B) The value of x is {} and the value of y is {}
   - C) The value of x is 3 and the value of y is 5
   - D) The value of x is 5 and the value of y is 3

**Watch the video for the answer:** [https://youtube.com/shorts/ZE2yfAJsCxk?si=6UvXfKLmR56c-Qu9](https://youtube.com/shorts/ZE2yfAJsCxk?si=6UvXfKLmR56c-Qu9)


> **Which of the following is the correct syntax for the print statement in Python?**

- A) print ("text")
- B) println ("text")
- C) echo ("text")
- D) None

> **What will be the output of the following code?**

```python
print("Hello, world!")
```
1. [ ] Hello
2. [ ] world
3. [ ] Hello, world!
4. [ ] There will be no output.

> How can you print multiple values on a single line in Python?

1. [ ] Use commas to separate the values within the print statement.
2. [ ] Use semicolons to separate the values within the print statement.
3. [ ] Use the + operator to concatenate the values before printing.
4. [ ] Create a list of the values and print the list.

> Which of the following statements will print the value of the variable x?

1. [ ] print(x)
2. [ ] print "x"
3. [ ] println(x)
4. [ ] echo x

> What is the purpose of the sep argument in the print function?

1. [ ] To specify the separator between multiple values printed on the same line.
2. [ ] To specify the end character for the printed line.
3. [ ] To specify the file to which the output should be printed.
4. [ ] To specify the format of the output.

> What is the purpose of the end argument in the print function?

1. [ ] To specify the separator between multiple values printed on the same line.
2. [ ] To specify the end character for the printed line.
3. [ ] To specify the file to which the output should be printed.
4. [ ] To specify the format of the output.

> How can you print a string without a newline character?

1. [ ] print(string, end="")
2. [ ] print(string, sep="")
3. [ ] print(string + "")
4. [ ] print(string; "")

What is the output of the following code?

name = "Alice"
age = 30
print("My name is", name, "and I am", age, "years old.")

- a) My name is Alice and I am 30 years old. (Correct)
- b) My name is Aliceand I am 30years old. (No separation)
- c) Alice 30 (Values printed without labels)
- d) An error (Incorrect syntax)

3. How can you format a string in Python to insert variables directly within it?

- a) Using string concatenation with the + operator (Limited control)
- b) Using the format method (Less readable for complex formatting)
- c) Using f-strings (Correct)
- d) All of the above (f-strings are generally preferred)

Which of the following statements is NOT valid for the print function in Python?

- a) print("Hello, world!")
- b) print(5 + 3) (prints the result of the expression)
- c) print() (prints an empty line)
- d) print(x, y, sep=",") (prints x and y with a comma separator)

How can you prevent a newline character from being printed at the end of the output in Python?

- a) By using a semicolon at the end of the print statement (this is not valid Python syntax)
- b) Using the end argument within the print function and setting it to an empty string ("")
- c) Specifying a special flag in the function call
- d) There's no way to suppress the newline character

**What is a syntax error in Python?**

- A) An error caused by incorrect logic in the code.
- B) An error detected when the code violates the rules of the Python language.
- C) An error that occurs during runtime.
- D) An error caused by a variable not being defined.

**Identify the error in the following code snippet:**

```python
prin("Hello World!")
```

- A) Incorrect variable name
- B) Missing colon
- C) Misspelled keyword
- D) Missing parenthesis


**Hint** NameError: name 'prin' is not defined.


**What should be done to correct the syntax error in the following code?**

```python
print("Hello World!"
```

- A) Add a closing quotation mark.
- B) Add a closing parenthesis.
- C) Add a colon at the end.
- D) Indent the line correctly.

**Comments:**

> What is the primary purpose of comments in Python code?

1. [ ] To execute instructions for the computer
2. [ ] To temporarily disable lines of code
3. [ ] To make the code more readable and understandable for humans
4. [ ] To create errors for debugging

> Which of the following is the correct syntax for a single-line comment in Python?

1. [ ] // This is a comment
2. [ ] /* This is a comment */
3. [ ] # This is a comment
4. [ ] { This is a comment }

> How can you create a multi-line comment in Python?

1. [ ] Using triple single quotes (''')
2. [ ] Using triple double quotes (""")
3. [ ] Using backslash () at the end of each line
4. [ ] Using the comment keyword

> What happens when you run code that includes comments?

1. [ ] The comments are executed along with the code.
2. [ ] The comments are ignored by the Python interpreter.
3. [ ] The comments are displayed as output.
4. [ ] The comments are converted into machine code.

**Indentation:**

> What is the purpose of indentation in Python?
1. [ ] To define code blocks
2. [ ] To define functions
3. [ ] To define variables
4. [ ] To print output

Answer: a) To define code blocks

> Which of the following is a correct way to indent code in Python?
- a) Using tabs
- b) Using spaces
- c) Using both tabs and spaces
- d) Using neither tabs nor spaces

Answer: b) Using spaces (Python recommends using 4 spaces for indentation)

> What happens if you don't indent your code in Python?
- a) It will run correctly
- b) It will throw a syntax error
- c) It will print an error message
- d) It will ignore the code
  
Answer: b) In Python, improper indentation specifically results in an IndentationError. While a syntax error is a broad category for any error in the syntax, an IndentationError is a specific type of syntax error related to incorrect indentation.

1. What is the indentation error in the following code?
```
if True:
  print("True")
    print("False")
```
- a) Missing indentation
- b) Extra indentation
- c) Incorrect indentation
- d) No error

Answer: b) Extra indentation (the second print statement has extra indentation)

> What is the standard number of spaces used for indentation in Python?
a) 2 spaces
b) 4 spaces
c) 6 spaces
d) 8 spaces

Answer: b) 4 spaces 

> Which of the following code snippets is correctly indented?

```
a) if True:
  print("True")
    print("False")

b) if True:
    print("True")
    print("False")

c) if True:
     print("True")
  print("False")

d) if True:
  print("True")
      print("False")
```
Answer: b) 

```python
 if True:
    print("True")
    print("False")
```

> In Python, indentation is used to define __________ in the code.

- A) Loops
- B) Functions
- C) Classes
- D) Blocks of code

## Exercises

Sure, here are some exercises about print functions, indentation, and comments in Python:

### Print Functions

1. **Basic Printing**
   - Write a Python program to print the following:
     ```
     Hello, World!
     ```
   
   **Solution:**
   ```python
   print("Hello, World!")
   ```

2. **Printing Variables**
   - Create two variables, `name` and `age`, and print them using the `print` function. Use the variables to print the following:
     ```
     My name is John and I am 25 years old.
     ```

   **Solution:**
   ```python
   name = "John"
   age = 25
   print("My name is", name, "and I am", age, "years old.")
   ```

3. **Formatted Strings**
   - Use an f-string to print the following using the variables `name` and `age`:
     ```
     My name is John and I am 25 years old.
     ```

   **Solution:**
   ```python
   name = "John"
   age = 25
   print(f"My name is {name} and I am {age} years old.")
   ```

### Indentation

4. **Correct Indentation**
   - The following code has incorrect indentation. Fix it so that it runs correctly:
     ```python
     def greet(name):
     print(f"Hello, {name}!")

     greet("Alice")
     ```

   **Solution:**
   ```python
   def greet(name):
       print(f"Hello, {name}!")

   greet("Alice")
   ```

5. **Conditional Indentation**
   - Write a Python program that checks if a number is positive, negative, or zero and prints the result. Ensure proper indentation is used.
   
   **Solution:**
   ```python
   number = int(input("Enter a number: "))

   if number > 0:
       print("The number is positive.")
   elif number < 0:
       print("The number is negative.")
   else:
       print("The number is zero.")
   ```

### Comments

6. **Single-Line Comments**
   - Add comments to the following code explaining each line:
     ```python
     name = "Alice"
     age = 30
     print(f"{name} is {age} years old.")
     ```

   **Solution:**
   ```python
   # Assign the string "Alice" to the variable 'name'
   name = "Alice"
   
   # Assign the integer 30 to the variable 'age'
   age = 30
   
   # Print the name and age using an f-string
   print(f"{name} is {age} years old.")
   ```

7. **Multi-Line Comments**
   - Use a multi-line comment to describe what the following code does:
     ```python
     def add(a, b):
         return a + b

     result = add(3, 5)
     print(result)
     ```

   **Solution:**
   ```python
   """
   This program defines a function 'add' that takes two arguments 'a' and 'b'
   and returns their sum. It then calls this function with the arguments 3
   and 5, stores the result in the variable 'result', and prints the result.
   """

   def add(a, b):
       return a + b

   result = add(3, 5)
   print(result)
   ```

## Review Questions

## References and Bibliography

[1] “Guido van Rossum,” Wikipedia, May 24, 2021. https://en.wikipedia.org/wiki/Guido_van_Rossum
‌
- [Indentation in Python - geeksforgeeks.org](https://www.geeksforgeeks.org/indentation-in-python/)
- [Indentation in Python (With Examples) - askpython.com](https://www.askpython.com/python/python-indentation)

## **Appendices**

### **Appendix A: os.getcwd()**
`os.getcwd()` is a function in Python that returns the current working directory (CWD) of the script. The "current working directory" is the folder from which your Python script is running. It is useful for figuring out the exact location of the script during execution.

**Explanation:**
- **`os`**: This is the module in Python that provides a way to interact with the operating system.
- **`getcwd()`**: This function within the `os` module returns a string representing the current working directory.

**Example:**

```python
import os

# Get the current working directory
current_directory = os.getcwd()

# Print the current working directory
print("Current Working Directory:", current_directory)
```

**Output:**
If you run this script, you might get an output like this (depending on where the script is being executed):

```
Current Working Directory: /Users/yourusername/Documents/my_project
```

This tells you that the script is being run from the `/Users/yourusername/Documents/my_project` directory.

**Use Case:**
Imagine you are writing a script that needs to read or write files. Knowing the current working directory will help ensure you reference the correct paths to those files.

