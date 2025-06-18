---
layout: page
title: "String Manipulations" 
description: Master Python strings with this guide. Learn string manipulations, methods, slicing with examples to improve your Python coding skills fast.  
keywords: ​Python strings, string manipulation, Python tutorial, string methods, Python basics, string operations, beginner Python, Python string examples, Python string functions, learn with yasir
toc: toc/python.html
topic: "strings"
course: "python"
prev: /python/docs/strings.html
next: /python/docs/strings/strings-formatting.html
show_practice_progress: true
show_mini_project: null
show_toc: true
breadcrumb:
  - title: Home
    url: /
  - title: python
    url: /python/
  - title: Strings
    url: /python/docs/strings/
---

## Table of Contents

1. [What is a String?](#1-what-is-a-string)
2. [Common String Operations](#2-common-string-operations)
3. [Tasks](#tasks)

## 1. What is a String?
- A **string** is a sequence of characters enclosed in quotes.
  - Examples: `"hello"`, `'Python'`, `"1234"`

### Creating Strings:
```python
name = "Alice"
greeting = 'Hello'
```

## 2. Common String Operations:
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

## Tasks

### 🔹 Task 1: Concatenate Two Strings  
**Instruction**:  
Take two words like `"Hello"` and `"World"` and combine them into one sentence with a space in between.

**Concept**: String concatenation using the `+` operator.

---

### 🔹 Task 2: Access Characters by Index  
**Instruction**:  
Given the word `"Python"`, find out what the first character and the last character are.

**Concept**: Accessing characters using index numbers (positive and negative indexing).

---

### 🔹 Task 3: Slice a Substring  
**Instruction**:  
From the word `"Python"`, extract only the first three letters.

**Concept**: String slicing (extracting parts of a string using index ranges).

---

### 🔹 Task 4: Measure String Length  
**Instruction**:  
Enter any word or sentence and find out how many characters it contains.

**Concept**: Using the `len()` function to count characters.

---




