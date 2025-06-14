---
layout: page
title: "Python Input & Output: F-Strings in Python"
description: Master Python f-strings with this definitive guide! Learn syntax, formatting tricks, multiline f-strings, expressions, and advanced use cases with clear examples.
keywords: Python f-strings, f-string Python, Python string formatting, Python 3.6 f-strings, Python formatted string literals, f-string syntax, Python string interpolation, f-string expressions, f-string formatting numbers, f-string multiline, f-string datetime, f-string dictionary, f-string alignment, f-string padding, f-string precision, f-string vs format(), f-string vs % formatting, f-string debug, f-string special characters, f-string best practices
toc: toc/python.html
---

## What are F-Strings?

F-strings (formatted string literals) are a feature introduced in Python 3.6 that provide a concise and readable way to embed expressions inside string literals. The "f" stands for "formatted" - these strings are evaluated at runtime.

## Why Use F-Strings?

1. **Readability**: Much cleaner syntax compared to older formatting methods
2. **Performance**: Faster than %-formatting and str.format()
3. **Expressiveness**: Can include any valid Python expression
4. **Less Error-Prone**: Fewer moving parts than other formatting methods

## Syntax

The basic syntax is simple - prefix your string with 'f' or 'F' and include expressions in curly braces `{}`:

```python
f"string text {expression} more text"
```

## Basic Examples for Beginners

### 1. Simple variable insertion
```python
name = "Alice"
age = 25
print(f"My name is {name} and I'm {age} years old.")
```

### 2. Simple calculations
```python
a = 5
b = 10
print(f"The sum of {a} and {b} is {a + b}.")
```

### 3. Calling functions
```python
def greet(name):
    return f"Hello, {name}!"

print(f"{greet('Bob')} How are you today?")
```

### 4. Formatting numbers
```python
price = 19.99
quantity = 3
print(f"Total: ${price * quantity:.2f}")
```

### Task 1: String Formatting with f-Strings

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

## Real-Life Examples

### 1. Database query results
```python
user = {"name": "John", "last_login": "2023-04-15"}
print(f"User {user['name']} last logged in on {user['last_login']}")
```

### 2. File processing
```python
filename = "report.pdf"
size = 2.5  # in MB
print(f"File '{filename}' is {size:.1f} MB ({size*1024:.0f} KB)")
```

### 3. API responses
```python
response = {"status": "success", "data_count": 42, "time": 0.45}
print(f"API call {response['status']}. Returned {response['data_count']} items in {response['time']}s")
```

### 4. Scientific calculations
```python
radius = 5.5
area = 3.14159 * radius**2
print(f"A circle with radius {radius} has area {area:.2f}")
```

### 5. Debugging
```python
x = 10
y = 20
print(f"DEBUG: x={x}, y={y}, x*y={x*y}")
```

## Advanced Features

### 1. Formatting options
```python
value = 123.456789
print(f"Default: {value}")
print(f"2 decimal places: {value:.2f}")
print(f"Scientific notation: {value:.2e}")
print(f"Percentage: {0.25:.1%}")
```

### 2. Alignment and padding
```python
item = "Apple"
price = 0.99
print(f"{item:10} - ${price:5.2f}")  # Left-aligned
print(f"{item:>10} - ${price:5.2f}") # Right-aligned
```

### 3. Date formatting
```python
from datetime import datetime
today = datetime.now()
print(f"Today is {today:%B %d, %Y}")
```

F-strings have become the preferred string formatting method in modern Python due to their clarity and efficiency. They're widely used in logging, debugging, report generation, and anywhere you need to combine variables with text.



