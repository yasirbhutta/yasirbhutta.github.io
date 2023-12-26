# Python: Language Basics

Connect with me: [Youtube](https://www.youtube.com/yasirbhutta) \| [LinkedIn](https://www.linkedin.com/in/yasirbhutta/) \| [WhatsApp Channel](https://whatsapp.com/channel/0029VaC3BC160eBZZSs3CW0c) \| [Web](https://yasirbhutta.github.io/) \| [Facebook](https://www.facebook.com/yasirbhutta786) \| [Twitter](https://twitter.com/yasirbhutta)

- [Download PDF](https://yasirbhutta.github.io/python/docs/basics.pdf)
- To access the updated handouts, please click on the following link:
[https://yasirbhutta.github.io/ms-excel/docs/basics.html](https://yasirbhutta.github.io/ms-excel/docs/basics.html)

## [Language Introduction]

- Python is a high-level, general-purpose programming language.
- It is known for its clear syntax, readability, and versatility.
- Python is widely used for `web development`, `data science`, `machine learning`, and `automation`.

### Python source code

### How To Use Print() Function in Python

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

#### Example 1

```python
message = 'Python is fun'

# print the string message
print(message)

```

**Output:**

```code
Python is fun
```

#### Example 2

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

- [Python Tutorial: How to print multiple lines](https://www.youtube.com/watch?v=Y13CX7-zzcQ&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=51)
- [Python Tutorial: 100 times "hello world" without loop](https://www.youtube.com/watch?v=QpqnHtD76BI&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=7)

### Comments

- Comments in Python are non-executable lines of code that are used to explain or document the code.
- They are ignored by the Python interpreter when the code is executed. 
- Comments are important for making code more readable and understandable, especially for other programmers who may need to read or modify the code.

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

- [Python Tutorial: A Comprehensive Guide to Single Line & Multi-Line Comments](https://www.youtube.com/watch?v=W7ixMGE2exc&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=73)

### Indentation

### [Variables and Assignments]

Tuple [example1,](https://yasirbhutta.blogspot.com/2022/09/python-variables-and-assignment-tuple.html) [example2](https://yasirbhutta.blogspot.com/2022/09/python-variables-and-assignment-tuple_22.html)

### User-defined Functions

### Code Checked at Runtime

### Variable Names

### More on Modules and their Namespaces

### Online help, help(), and dir()

## True/False (Mark T for True and F for False)

## Multiple Choice (Select the best answer)

1. Which of the following is the correct syntax for the print statement in Python?

a) print text
b) println text
c) echo text

What will be the output of the following code?

```python
print("Hello, world!")
```
a) Hello
b) world
c) Hello, world!
d) There will be no output.

How can you print multiple values on a single line in Python?

a) Use commas to separate the values within the print statement.
b) Use semicolons to separate the values within the print statement.
c) Use the + operator to concatenate the values before printing.
d) Create a list of the values and print the list.

Which of the following statements will print the value of the variable x?

a) print(x)
b) print "x"
c) println(x)
d) echo x

What is the purpose of the sep argument in the print function?

a) To specify the separator between multiple values printed on the same line.
b) To specify the end character for the printed line.
c) To specify the file to which the output should be printed.
d) To specify the format of the output.

 What is the purpose of the end argument in the print function?

a) To specify the separator between multiple values printed on the same line.
b) To specify the end character for the printed line.
c) To specify the file to which the output should be printed.
d) To specify the format of the output.

How can you print a string without a newline character?

a) print(string, end="")
b) print(string, sep="")
c) print(string + "")
d) print(string; "")

**Comments:**

What is the primary purpose of comments in Python code?
a) To execute instructions for the computer
b) To temporarily disable lines of code
c) To make the code more readable and understandable for humans
d) To create errors for debugging

Which of the following is the correct syntax for a single-line comment in Python?
a) // This is a comment
b) /* This is a comment */
c) # This is a comment
d) { This is a comment }

How can you create a multi-line comment in Python?

a) Using triple single quotes (''')
b) Using triple double quotes (""")
c) Using backslash () at the end of each line
d) Using the comment keyword

What happens when you run code that includes comments?
a) The comments are executed along with the code.
b) The comments are ignored by the Python interpreter.
c) The comments are displayed as output.
d) The comments are converted into machine code.



## Exercises

## Review Questions

## References and Bibliography