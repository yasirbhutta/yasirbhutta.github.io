---
layout: page
title: "Python String Tutorial: Learn String Methods & Formatting" 
description: Master Python strings with this guide. Learn string manipulations, methods, slicing, and formatting with examples to improve your Python coding skills fast.  
keywords: ​Python strings, string manipulation, string formatting, Python tutorial, string methods, Python basics, string operations, beginner Python, Python string examples, Python string functions, learn with yasir
toc: toc/python-toc.html
topic: "strings"
course: "python"
prev: /python/docs/control-flow.html
next: /python/docs/functions.html
---

## String Manipulations

### What is a String?
- A **string** is a sequence of characters enclosed in quotes.
  - Examples: `"hello"`, `'Python'`, `"1234"`

### Creating Strings:
```python
name = "Alice"
greeting = 'Hello'
```

### Common String Operations:
1. **Concatenation (joining strings):**
   ```python
   first = "Hello"
   second = "World"
   result = first + " " + second  # Output: "Hello World"
   ```

2. **Repetition:**
   ```python
   word = "Hi"
   print(word * 3)  # Output: "HiHiHi"
   ```

3. **Indexing:**
   ```python
   text = "Python"
   print(text[0])  # Output: "P"
   print(text[-1]) # Output: "n"
   ```

4. **Slicing:**
   ```python
   text = "Python"
   print(text[0:3])  # Output: "Pyt"
   print(text[2:])   # Output: "thon"
   ```

---

## Formatting Strings

### Formatting Strings – Adjusting Case

#### 1. **Convert to Uppercase:**
```python
text = "hello"
print(text.upper())  # Output: "HELLO"
```

#### 2. **Convert to Lowercase:**
```python
text = "HELLO"
print(text.lower())  # Output: "hello"
```

#### 3. **Capitalize First Letter:**
```python
text = "python is fun"
print(text.capitalize())  # Output: "Python is fun"
```

#### 4. **Title Case (First letter of each word capitalized):**
```python
text = "hello world"
print(text.title())  # Output: "Hello World"
```

#### 5. **Swap Case:**
```python
text = "PyTHon"
print(text.swapcase())  # Output: "pYthON"
```

---

### Formatting Strings – Adding and Removing Spaces**

#### 1. **Removing Extra Spaces:**
- **Remove leading and trailing spaces:**
```python
text = "   hello world   "
print(text.strip())  # Output: "hello world"
```

- **Remove only leading spaces:**
```python
text = "   hello"
print(text.lstrip())  # Output: "hello"
```

- **Remove only trailing spaces:**
```python
text = "hello   "
print(text.rstrip())  # Output: "hello"
```

#### 2. **Adding Spaces or Padding:**
- **Center-align with padding:**
```python
text = "Python"
print(text.center(10))  # Output: "  Python  "
```

- **Left-align:**
```python
print(text.ljust(10))  # Output: "Python    "
```

- **Right-align:**
```python
print(text.rjust(10))  # Output: "    Python"
```

## **Mini Quiz: String Basics**



---

## **Practice Tasks**

### Task 1: String Info
Write a program that asks the user for their name and prints:
- The name in all uppercase
- The name in all lowercase
- The number of characters in the name

**Example:**
```python
# Sample output for name "Alice"
Uppercase: ALICE  
Lowercase: alice  
Length: 5
```

---

### Task 2: Remove Extra Spaces
Given a string with extra spaces:
```python
sentence = "   Python is fun!   "
```
Write code to:
- Remove the spaces
- Print the cleaned-up sentence

---

### Task 3: Align a String
Print the word `"Code"`:
- Centered in a 20-character space
- Left-aligned in a 20-character space
- Right-aligned in a 20-character space

---

