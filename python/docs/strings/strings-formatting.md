---
layout: page
title: "Formatting Strings"
description: Master Python strings with this guide. Learn  formatting with examples to improve your Python coding skills fast.
keywords: ​Python strings, string formatting, Python tutorial, string methods, Python basics, string operations, beginner Python, Python string examples, Python string functions, learn with yasir
toc: toc/python.html
topic: "strings"
course: "python"
show_practice_progress: true
show_mini_project: null
show_toc: true
prev: /python/docs/strings/strings-manip.html
next: /python/docs/functions.html
breadcrumb: 
- title: Strings
url: /python/docs/strings/
---

## Table of Contents

1. [Formatting Strings – Adjusting Case](#1-formatting-strings--adjusting-case)
2. [Formatting Strings – Adding and Removing Spaces](#2-formatting-strings--adding-and-removing-spaces)
3. [Formatting Strings – Finding and Replacing Substrings](#3-formatting-strings--finding-and-replacing-substrings)
4. [Formatting Strings – Splitting](#4-formatting-strings--splitting)
5. [Formatting Strings – Partitioning Strings](#5-formatting-strings--partitioning-strings)
6. [Tasks](#6-tasks)

## 1. Formatting Strings – Adjusting Case

### 1.1 **Convert to Uppercase:**
```python
text = "hello"
print(text.upper())  # Output: "HELLO"
```

### 1.2 **Convert to Lowercase:**
```python
text = "HELLO"
print(text.lower())  # Output: "hello"
```

#### 1.3 **Capitalize First Letter:**
```python
text = "python is fun"
print(text.capitalize())  # Output: "Python is fun"
```

#### 1.4 **Title Case (First letter of each word capitalized):**
```python
text = "hello world"
print(text.title())  # Output: "Hello World"
```

#### 1.5 **Swap Case:**
```python
text = "PyTHon"
print(text.swapcase())  # Output: "pYthON"
```

---
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1602443888929206"
     crossorigin="anonymous"></script>
<ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-1602443888929206"
     data-ad-slot="6296238623"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

## 2. Formatting Strings – Adding and Removing Spaces

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

## **Tasks**

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


## 3. Formatting Strings – Finding and Replacing Substrings

### 🔹 `find()` Method
- Returns the index of the first occurrence of a substring.
- Returns `-1` if not found.

```python
text = "Hello, welcome to Python!"
position = text.find("welcome")
print(position)  # Output: 7
```

### 🔹 `replace()` Method
- Replaces all occurrences of a substring with another substring.

```python
text = "I love Python. Python is awesome!"
new_text = text.replace("Python", "coding")
print(new_text)
# Output: I love coding. coding is awesome!
```

### 🔹 Example: Censoring Words

```python
comment = "This product is bad, really bad!"
cleaned = comment.replace("bad", "***")
print(cleaned)
# Output: This product is ***, really ***!
```

---

## 4. Formatting Strings – Splitting

### 🔹 `split()` Method
- Splits a string into a list based on a separator.
- When you use `split()` **without any arguments**, it splits the string using **any whitespace** as the separator. This includes:

  - Spaces (`" "`)
  - Tabs (`"\t"`)
  - Newlines (`"\n"`)

Also, it **automatically removes extra spaces**, so multiple spaces are treated as one.



### 📌 Syntax
```python
string.split()
```

---

### ✅ Examples

#### 1. Basic Usage
```python
sentence = "Python is fun"
words = sentence.split()
print(words)
# Output: ['Python', 'is', 'fun']
```

#### 2. With Extra Spaces
```python
sentence = "   Python    is   powerful   "
words = sentence.split()
print(words)
# Output: ['Python', 'is', 'powerful']
```

#### 3. With Tabs and Newlines
```python
text = "Learn\tPython\nNow"
parts = text.split()
print(parts)
# Output: ['Learn', 'Python', 'Now']
```

#### 🔹 Splitting by a Custom Separator

```python
data = "apple,banana,orange"
fruits = data.split(",")
print(fruits)
# Output: ['apple', 'banana', 'orange']
```

#### 🔹 Example: Extracting Names from a CSV Line

```python
csv_line = "John,Doe,25"
parts = csv_line.split(",")
print("First Name:", parts[0])
print("Last Name:", parts[1])
```

---

## 5. Formatting Strings – Partitioning Strings

### 🔹 `partition()` Method
- Splits the string at the first occurrence of the separator.
- Returns a tuple: `(before, separator, after)`

```python
email = "username@example.com"
result = email.partition("@")
print(result)
# Output: ('username', '@', 'example.com')
```

### 🔹 Handling Missing Separator

```python
text = "hello world"
result = text.partition(":")
print(result)
# Output: ('hello world', '', '')
```

### 🔹 Example: Extracting Domain from an Email

```python
email = "jane.doe@gmail.com"
_, _, domain = email.partition("@")
print("Domain:", domain)
# Output: Domain: gmail.com
```

---

### ✅ Summary Table

| Method       | Purpose                           | Returns                    |
|--------------|-----------------------------------|----------------------------|
| `find()`     | Finds substring position          | Index or -1                |
| `replace()`  | Replaces substrings               | New string                 |
| `split()`    | Splits into list                  | List of strings            |
| `partition()`| Splits once, returns 3-part tuple | Tuple (before, sep, after) |


<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1602443888929206"
     crossorigin="anonymous"></script>
<ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-1602443888929206"
     data-ad-slot="6296238623"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

---

## 6. Tasks

### ✅ Tasks: `find()` and `replace()`

#### **Task 4: Find the Word**
Ask the user to enter a sentence and a word. Use `.find()` to print the position of that word.

```python
# Example input: "Python is easy", word: "easy"
# Expected output: Word found at position 10
```

#### **Task 5: Replace Bad Words**
Write a program that replaces words like `"bad"` or `"ugly"` with `"***"` in a sentence.

```python
# Input: "This food is bad and ugly"
# Output: "This food is *** and ***"
```

#### **Task 6: Count Substring Occurrence**
Use `.find()` inside a loop to count how many times a word appears.

---

### ✅ Tasks: `split()`

#### **Task 7: Split a Sentence into Words**
Write a program to split a user-provided sentence into words and print them one per line.

```python
# Input: "Python is fun"
# Output:
# Python
# is
# fun
```

#### **Task 8: CSV Splitter**
Split this string: `"Alice,Math,85"` and print each part labeled (e.g., Name, Subject, Marks).

```python
# Output:
# Name: Alice
# Subject: Math
# Marks: 85
```

#### **Task 9: Word Count**
Ask the user for a sentence and print the number of words in it using `split()`.

---

### ✅ Tasks: `partition()`

#### **Task 10: Email Parser**
Ask the user for an email and extract the username and domain using `partition("@")`.

```python
# Input: "user123@gmail.com"
# Output:
# Username: user123
# Domain: gmail.com
```

#### **Task 11: Separate Front and Back**
Partition a string at a given word and print what's before and after.

```python
# Input: "The quick brown fox", partition word: "brown"
# Output:
# Before: The quick
# After: fox
```

#### **Task 12: Handle Missing Separator**
Use `partition()` on a string that **doesn't** contain the separator and show the output tuple.

---

