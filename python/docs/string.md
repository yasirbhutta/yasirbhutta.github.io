---
layout: page
title: String in Python  
description: Learn inheritance in Python with this beginner-friendly guide. Understand parent and child classes, method overriding, `super()`, and multilevel inheritance with examples. Perfect for Python learners to master object-oriented programming.  
keywords: Python inheritance tutorial, Python OOP inheritance, parent and child classes in Python, method overriding in Python, Python `super()` example, multilevel inheritance Python, Python OOP basics, Python programming for beginners, Python class inheritance examples
toc: toc/python-toc.html
topic: "string"
subject: "python"
---
# String in Python
## **Lecture #1: String Manipulations**

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

## **Lecture #2: Formatting Strings – Adjusting Case**

### 1. **Convert to Uppercase:**
```python
text = "hello"
print(text.upper())  # Output: "HELLO"
```

### 2. **Convert to Lowercase:**
```python
text = "HELLO"
print(text.lower())  # Output: "hello"
```

### 3. **Capitalize First Letter:**
```python
text = "python is fun"
print(text.capitalize())  # Output: "Python is fun"
```

### 4. **Title Case (First letter of each word capitalized):**
```python
text = "hello world"
print(text.title())  # Output: "Hello World"
```

### 5. **Swap Case:**
```python
text = "PyTHon"
print(text.swapcase())  # Output: "pYthON"
```

---

## **Lecture #3: Formatting Strings – Adding and Removing Spaces**

### 1. **Removing Extra Spaces:**
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

### 2. **Adding Spaces or Padding:**
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

---

Great! Here’s a mini quiz with multiple-choice questions and a few practice tasks based on the three lectures:

---

## **Mini Quiz: String Basics**

### **1. What will be the output of the following code?**
```python
name = "Alice"
print(name[1])
```
a) A  
b) l  
c) i  
d) e  
**Answer:** c) i

---

### **2. Which method converts a string to all uppercase letters?**  
a) `capitalize()`  
b) `upper()`  
c) `title()`  
d) `swapcase()`  
**Answer:** b) `upper()`

---

### **3. What does the `strip()` method do?**  
a) Removes only leading spaces  
b) Removes only trailing spaces  
c) Removes both leading and trailing spaces  
d) Removes all spaces inside the string  
**Answer:** c) Removes both leading and trailing spaces

---

### **4. What is the output of the following code?**
```python
word = "HELLO"
print(word.lower())
```
a) Hello  
b) hello  
c) HELLO  
d) error  
**Answer:** b) hello

---

### **5. What is the output of this code?**
```python
text = "python"
print(text.title())
```
a) Python  
b) PYTHON  
c) python  
d) P y t h o n  
**Answer:** a) Python

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

