---
layout: page
title: "Type Casting in Python: What It Is & Why You Need It"
description: Learn what type casting in Python is, why it's used, and how to convert between data types like int, float, str, and bool with examples. Master explicit & implicit type conversion.
keywords: type casting in Python, Python type conversion, int to string Python, float to int Python, str to int Python, explicit type casting, implicit type conversion, Python data types, type casting examples, Python int(), Python float(), Python str(), Python bool(), convert string to int, convert float to int, why use type casting, Python type handling, dynamic typing Python, user input conversion, string to number Python
author: Muhammad Yasir Bhutta
course: python
topic: data-types
toc: toc/python.html
breadcrumb: 
- title: Data Types
url: /python/docs/data-types.html
---

# Type Casting in Python

Type casting (also called type conversion) is the process of converting a value from one data type to another in Python. Python is dynamically typed, but sometimes you need to explicitly convert between types to perform certain operations or meet function requirements.

## Why We Use Type Casting

1. **Data Compatibility**: To perform operations between different data types
2. **Input Handling**: When receiving user input (which is always a string) that needs to be numeric
3. **Function Requirements**: When a function requires a specific data type
4. **Data Processing**: When preparing data for storage or transmission
5. **Precision Control**: To change between different numeric types (e.g., float to int)

## Common Type Casting Functions

```python
# Integer conversion
x = int(3.7)      # 3 (float to int)
y = int("42")     # 42 (string to int)

# Float conversion
a = float(5)      # 5.0 (int to float)
b = float("3.14") # 3.14 (string to float)

# String conversion
s = str(100)      # "100" (int to string)
t = str(7.5)      # "7.5" (float to string)

# Boolean conversion
bool(0)           # False (int to bool)
bool(1)           # True
bool("")          # False (empty string to bool)
bool("hello")     # True (non-empty string to bool)
```

## Implicit vs Explicit Conversion

- **Implicit**: Python automatically converts types (e.g., `3 + 4.5` becomes `3.0 + 4.5`)
- **Explicit**: Programmer manually converts using functions like `int()`, `float()`, `str()`

## Example Use Cases

```python
# User input (always comes as string)
age = input("Enter your age: ")  # "25" (string)
age_num = int(age)               # 25 (integer)

# Mathematical operations
result = float(5) / 2            # 2.5 instead of 2

# String formatting
price = 19.99
print("The price is $" + str(price))

# Data validation
user_input = "123"
if user_input.isdigit():
    value = int(user_input)
else:
    print("Invalid number")
```

Type casting is essential when you need to ensure your data is in the correct format for operations, storage, or display purposes.

### **Task 2: Convert Integer to String**  
Write a Python program that:  
- Takes an integer as input.  
- Converts it to a string using the `str()` function.  
- Concatenates the string with another message and prints it.  

**Example Input:**  
```
Enter a number: 100  
```

**Expected Output:**  
```
Your number is: 100  
```

---

### **Task 3: Convert String to Integer**  
Write a Python program that:  
- Takes a numeric string as input (e.g., `"123"`).  
- Converts it into an integer using the `int()` function.  
- Multiplies the number by 2 and prints the result.  

**Example Input:**  
```
Enter a number as a string: 50  
```

**Expected Output:**  
```
Double the number: 100  
```

---

### **Task 4: Convert Integer to Octal and Hexadecimal**  
Write a Python program that:  
- Takes an integer as input from the user.  
- Converts it to **octal** using `oct()` and **hexadecimal** using `hex()`.  
- Prints both results.  

**Example Input:**  
```
Enter a number: 255  
```

**Expected Output:**  
```
Octal: 0o377  
Hexadecimal: 0xff  
```

---

### **Task 5: Convert Octal and Hexadecimal to Integer**  
Write a Python program that:  
- Takes an **octal** and a **hexadecimal** number as input (as strings).  
- Converts them back to integers using `int(value, base)`.  
- Prints the decimal values.  

**Example Input:**  
```
Enter an octal number: 0o377  
Enter a hexadecimal number: 0xff  
```

**Expected Output:**  
```
Octal to Integer: 255  
Hexadecimal to Integer: 255  
```
