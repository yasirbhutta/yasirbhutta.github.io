
### 🔷 What is a Module in Python?
A **module** is simply a file that contains **Python code** — typically functions, variables, and classes — that you can reuse in other programs.

For example:
```python
# This is a module: my_module.py
def greet(name):
    return f"Hello, {name}!"
```

---

### 🔷 Why Use Modules?

| Reason                  | Benefit                                           |
|-------------------------|----------------------------------------------------|
| Code reusability        | Write once, use many times                        |
| Better organization     | Separate logic into smaller, manageable pieces    |
| Easier debugging        | Errors are easier to isolate in smaller files     |
| Collaboration           | Multiple people can work on different modules     |

---

### 🔷 Syntax: Creating and Using a Module

1. **Create a Module**
   Save functions in a `.py` file, e.g., `math_utils.py`:
   ```python
   # math_utils.py
   def add(a, b):
       return a + b

   def subtract(a, b):
       return a - b
   ```

2. **Import and Use the Module**
   In another Python file:
   ```python
   import math_utils

   print(math_utils.add(3, 4))       # Output: 7
   print(math_utils.subtract(10, 5)) # Output: 5
   ```

   Or import specific functions:
   ```python
   from math_utils import add

   print(add(2, 2))  # Output: 4
   ```

---

### 🔷 Example

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

### 🔷 Tasks for Practice

✅ **Task 1**: Create a module named `calculator.py` with functions `multiply`, `divide`.

✅ **Task 2**: Create a main script `main.py` and use `calculator` functions.

✅ **Task 3**: Create a module `string_utils.py` with a function `is_palindrome(text)` that returns `True` if a word is a palindrome.

✅ **Task 4**: Create a module `geometry.py` with functions like `area_of_circle(r)` and `area_of_square(side)`.

