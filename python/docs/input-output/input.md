---
layout: page
title: Python `input()` Function
description: Learn how to handle Python errors and exceptions effectively. Fix common Python errors like SyntaxError, TypeError, and NameError with practical examples.
keywords: Python errors, Python exceptions, fix Python errors, SyntaxError Python, TypeError Python, NameError Python, Python error handling, Python debugging, Python try-except, Python exception handling
toc: toc/python.html
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
