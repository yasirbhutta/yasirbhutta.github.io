---
layout: page
title: "Functions in Python Modules : A Beginner's Guide | Python for Beginners"
description: Learn how to define and use functions inside Python modules. This guide covers creating a module, importing it, and organizing your Python code for better reusability and clarity.
keywords: Python modules, Python functions, custom modules in Python, import module Python, how to use functions in modules, Python programming, Python beginner guide, reusable Python code, Python for Beginners, python tutorial for beginners
toc: toc/python.html
course: python
topic: "lambda"
mini_project: false
---

## Table of Contents
- [What is a Module in Python?](#-what-is-a-module-in-python)
- [Types of Modules](#types-of-modules)
- [How to Import a Module?](#how-to-import-a-module)
- Creating and Using a Custom Python Module
  - [Example #1: `math_utils.py` Module](#-example-1-creating-and-using-a-custom-python-module)
  - [Example #2: `greetings.py` Module](#-example-2-creating-and-using-a-custom-python-module)
- [Special Module Variable: `__name__`](#special-module-variable-__name__)

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

## 🔷 Example #1: Creating and Using a Custom Python Module

1. **Create a module (`math_utils.py`)****
   Save functions in a `.py` file, e.g., `math_utils.py`:
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

   print(math_utils.add(3, 4))       # Output: 7
   print(math_utils.subtract(10, 5)) # Output: 5
   ```

   Or **import specific functions:**
   
   ```python
   from math_utils import add

   print(add(2, 2))  # Output: 4
   ```

   or **Import with Alias ('calc'):**
   
   ```python
    import math_utils as calc

    result= calc.add(5, 3)
    print(result)

    result2 = calc.subtract(10, 4)
    print(result2)
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

In Python, the `__name__` variable is a special built-in variable that helps determine whether a script is being run **directly** or being **imported** as a module into another script.  

### **How `__name__` Works:**
- When a Python file is **run directly**, `__name__` is set to `"__main__"`.
- When it is **imported** as a module, `__name__` is set to the **module's name**.


## Example

```python
def add(a, b):
      return a + b

def subtract(a, b):
    return a - b

if __name__ == "__main__":
    # Test the functions in this module
    print("Testing math_utils.py")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
    print("All tests passed!")
```

**This construct allows you to:**

1. Test your module when run directly
2. Prevent test execution when imported as a module
3. Separate reusable functions from test/demo code

---

### **Example: Using `__name__` Across Two Files**

#### **1. Create a Module (`module.py`)**

```python
# module.py
def greet(name):
    return f"Hello, {name}!"

print(f"Module's __name__: {__name__}")  # Check __name__

if __name__ == "__main__":
    print("This runs only when module.py is executed directly.")
```

**- If you run `module.py` directly, it prints:**

  ```
  Module's __name__: __main__
  This runs only when module.py is executed directly.
  ```
- If imported, the `if __name__ == "__main__":` block **does not run**.

---

#### **2. Import `module.py` in Another Script (`main_script.py`)**
```python
# main_script.py
import module  # Imports module.py

print(f"Main script's __name__: {__name__}")  # Check __name__ in main file
print(module.greet("Alice"))
```

**Output when running `main_script.py`:**

```
Module's __name__: module  # (Because it was imported)
Main script's __name__: __main__  # (Because main_script.py is run directly)
Hello, Alice!
```
- The `if __name__ == "__main__":` block in `module.py` **does not execute** because it was imported.

---

## **Key Use Cases of `__name__`**
1. **Preventing Code Execution on Import**  
   - Use `if __name__ == "__main__":` to ensure certain code (like tests) runs only when the script is executed directly, not when imported.

2. **Module Testing**  
   - You can include test cases inside `if __name__ == "__main__":` to test functions without affecting imports.

3. **Controlling Script Behavior**  
   - Example: A script can behave differently when run standalone vs. when used as a module.

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

