---
layout: page
title: "Python Input & Output: `input()` Function"
description: Learn how to use Python's input() function effectively! Get user input, handle data types (int, float, string), add prompts, and validate input with practical examples.
keywords: Python input function, Python user input, input() in Python, Python keyboard input, Python input examples, Python input string, Python input integer, Python input validation, Python input prompt, Python raw_input vs input, Python read user input, Python input conversion, Python input loop, Python input timeout, Python multiline input, Python input EOFError, Python input best practices, Python CLI input, Python input security, Python input stripping whitespace
course: python
topic: input-output
show_toc: true
toc: toc/python.html
show_practice_progress: true
show_mini_project: false
prev: /python/docs/input-output/f-string.html
next: /python/docs/data-types/type-casting.html
breadcrumb: 
- title: Input - Output
url: /python/docs/input-output/
---

#### **What is `input()`?**  

The `input()` function in Python is used to take user input from the keyboard. It allows a program to interact with users by asking for information.  

#### **Syntax:**  
```python
variable_name = input("Prompt message")
```
- `Prompt message`: A string displayed to the user before they enter input.
- `variable_name`: The variable where the user’s input is stored.

---

**Basic Example**

```python
name = input("Enter your name: ")
print("Hello, " + name + "!")
```
#### **Explanation:**

1. `input("Enter your name: ")` displays the message **"Enter your name: "** and waits for the user to type something.
2. The user types their name and presses Enter.
3. The input is stored in the variable `name`.
4. `print("Hello, " + name + "!")` displays a greeting message with the user's name.

---

### **Taking Numerical Input**
By default, `input()` returns a string. If you need a number, you must convert it using `int()` or `float()`.  

#### **Example:**
```python
age = int(input("Enter your age: "))
print("In 5 years, you will be", age + 5)
```
#### **Explanation:**
1. The user enters their age as a string.
2. `int(input(...))` converts it into an integer.
3. The program calculates the age after 5 years and prints it.

## 📘 **Related Topics**

* **F-Strings in Python** – F-strings (formatted string literals) are a feature introduced in Python 3.6 that provide a concise and readable way to embed expressions inside string literals. 
  👉 [Learn more](f-string.md)
* [**Python `print` Function**](print.md)