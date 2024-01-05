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


## How To Use Print() Function in Python

- It is used to display text to the console, or to a file. The print() function can take one or more arguments, and it can be used to format text in a variety of ways.

Here is the basic syntax of the print() function:

```pthon
print(object1, object2, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
```

object1, object2, ...: The objects to be printed. These can be strings, numbers, variables, or any other Python object.
sep: The separator to use between objects. The default separator is a space.
end: The character or string to print at the end of the output. The default is a newline character (\n).
file: The file to write the output to. The default is the console.
flush: Whether to flush the output buffer immediately. The default is False.

[Video: Use of print() function in python](https://youtu.be/RSSSyqw79_M)

**Example #1:**

```python
message = 'Python is fun'

# print the string message
print(message)

```

**Output:**

```code
Python is fun
```

**Example #2:**

```python
# Print a string:
print("Hello, World!")

# Print a number:
print(10)

# Print a variable:
x = 5
print(x)

# Print multiple objects on the same line:
print("Hello", "World")

# Print multiple objects on separate lines:
print("Hello")
print("World")

# Print with a custom separator:
print("Hello", "World", sep=", ")

# Print with a custom ending character:
print("Hello", "World", end="!")

# Print to a file:
with open("output.txt", "w") as f:
    print("Hello, World!", file=f)

```

**See also:**

- [Video: How to print multiple lines](https://www.youtube.com/watch?v=Y13CX7-zzcQ&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=51)
- [Video: 100 times "hello world" without loop](https://www.youtube.com/watch?v=QpqnHtD76BI&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=7)

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

Indentation is a very important concept in Python. It refers to adding white space before a statement to a particular block of code. In another word, all the statements with the same space to the right, belong to the same code block.

For example, consider the following code snippet:

```python
if True:
    print("True")
else:
    print("False")
```

**See also:**

- [Indentation in Python - geeksforgeeks.org](https://www.geeksforgeeks.org/indentation-in-python/)
- [Indentation in Python (With Examples) - askpython.com](https://www.askpython.com/python/python-indentation)

## True/False (Mark T for True and F for False)

## Multiple Choice (Select the best answer)


> Which of the following is the correct syntax for the print statement in Python?

1. [ ] print ("text")
2. [ ] println ("text")
3. [ ] echo ("text")

> What will be the output of the following code?

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

## Exercises

## Review Questions

## References and Bibliography

- [Indentation in Python - geeksforgeeks.org](https://www.geeksforgeeks.org/indentation-in-python/)
- [Indentation in Python (With Examples) - askpython.com](https://www.askpython.com/python/python-indentation)