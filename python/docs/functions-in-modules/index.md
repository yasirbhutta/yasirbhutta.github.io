---
layout: page
title: "What is a Module in Python"
description: Learn how to use Python lambda functions with this detailed guide. Discover syntax, examples, and use cases to enhance your programming skills.
keywords: Python lambda functions, lambda function tutorial, Python programming, lambda function examples, Python syntax, functional programming in Python
toc: toc/python-toc.html
course: python
topic: "lambda"
mini_project: false
---

## 🔷 What is a Module in Python?

In Python, a **module** is a file containing Python code (functions, classes, variables, or runnable code) that can be imported and used in other Python programs. Modules help in organizing code logically, promoting reusability and maintainability.

### 🔷 Why Use Modules? 

| Reason                  | Benefit                                           |
|-------------------------|----------------------------------------------------|
| Code reusability        | Write once, use many times                        |
| Better organization     | Separate logic into smaller, manageable pieces    |
| Easier debugging        | Errors are easier to isolate in smaller files     |
| Collaboration           | Multiple people can work on different modules     |

---

## **Types of Modules:**
1. **Built-in Modules** (Pre-installed with Python)  
   Example: `math`, `os`, `sys`, `random`
   ```python
   import math
   print(math.sqrt(25))  # Output: 5.0
   ```

2. **User-defined Modules** (Created by users)  
   Example: Save as `mymodule.py`
   ```python
   # mymodule.py
   def greet(name):
       return f"Hello, {name}!"
   ```
   Then import it:
   ```python
   import mymodule
   print(mymodule.greet("Alice"))  # Output: Hello, Alice!
   ```

3. **Third-party Modules** (Installed via `pip`)  
   Example: `numpy`, `requests`, `pandas`
   ```bash
   pip install numpy
   ```
   ```python
   import numpy as np
   arr = np.array([1, 2, 3])
   print(arr)  # Output: [1 2 3]
   ```

---

## **How to Import a Module?**
1. **Basic Import**
   ```python
   import module_name
   module_name.function()
   ```

2. **Import with Alias (Shortcut)**
   ```python
   import module_name as alias
   alias.function()
   ```

3. **Import Specific Functions/Classes**
   ```python
   from module_name import function1, function2
   function1()
   ```

4. **Import Everything (Not Recommended)**
   ```python
   from module_name import *  # Avoid (pollutes namespace)
   function1()
   ```

---

## **Example: Creating & Using a Module**
1. **:
   ```python
   def add(a, b):
       return a + b

   def sub(a, b):
       return a - b
   ```

2. **Import and use it**:
   ```python
   import calc
   print(calc.add(5, 3))  # Output: 8
   print(calc.sub(5, 3))  # Output: 2
   ```

## 🔷 Example #1: Creating and Using a Custom Python Module

1. **Create a module (`calc.py`)****
   Save functions in a `.py` file, e.g., `calc.py`:
   ```python
   # calc.py
   def add(a, b):
       return a + b

   def subtract(a, b):
       return a - b
   ```

2. **Import and Use the Module**
   In another Python file:
   ```python
   import calc

   print(calc.add(3, 4))       # Output: 7
   print(calc.subtract(10, 5)) # Output: 5
   ```

   Or import specific functions:
   ```python
   from calc import add

   print(add(2, 2))  # Output: 4
   ```

---

## 🔷 Example #2: Creating and Using a Custom Python Module

**Create a module file `greetings.py`:**
```python
def hello(name):
    return f"Hello, {name}!"

def goodbye(name):
    return f"Goodbye, {name}!"
```

**Use the module in another script:**
```python
import greetings

print(greetings.hello("Alice"))
print(greetings.goodbye("Alice"))
```

---

## **Special Module Variable: `__name__`**
- When a module is run directly, `__name__ == "__main__"`.
- When imported, `__name__` is the module's name.
- Used to add test code that runs only when executed directly:
  ```python
  # mymodule.py
  def func():
      return "Hello!"

  if __name__ == "__main__":
      print("Testing module...")
      print(func())
  ```

---

### **Summary**
✅ Modules help organize and reuse code.  
✅ Python has built-in, user-defined, and third-party modules.  
✅ Use `import` to include modules in your code.  
✅ `__name__` helps in writing module test cases.  

## 🔷 Tasks for Practice

✅ **Task 1**: Create a module named `calculator.py` with functions `multiply`, `divide`.

✅ **Task 2**: Create a main script `main.py` and use `calculator` functions.

✅ **Task 3**: Create a module `string_utils.py` with a function `is_palindrome(text)` that returns `True` if a word is a palindrome.

✅ **Task 4**: Create a module `geometry.py` with functions like `area_of_circle(r)` and `area_of_square(side)`.

