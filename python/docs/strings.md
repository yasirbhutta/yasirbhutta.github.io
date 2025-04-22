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

Here's a beginner-friendly Python tutorial covering the topics you've listed, organized into three lectures with clear explanations and examples.

---

## Formatting Strings – Finding and Replacing Substrings**

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

## Formatting Strings – Splitting**

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

## Formatting Strings – Partitioning Strings**

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

---

Sure! Here’s a set of beginner-friendly **student tasks and exercises** related to the three lectures you’ve covered: `find()`, `replace()`, `split()`, and `partition()`.

---

## Tasks

### ✅ Tasks: `find()` and `replace()`**

#### **Task 1: Find the Word**
Ask the user to enter a sentence and a word. Use `.find()` to print the position of that word.

```python
# Example input: "Python is easy", word: "easy"
# Expected output: Word found at position 10
```

#### **Task 2: Replace Bad Words**
Write a program that replaces words like `"bad"` or `"ugly"` with `"***"` in a sentence.

```python
# Input: "This food is bad and ugly"
# Output: "This food is *** and ***"
```

#### **Task 3: Count Substring Occurrence**
Use `.find()` inside a loop to count how many times a word appears.

---

### ✅ Tasks: `split()`**

#### **Task 4: Split a Sentence into Words**
Write a program to split a user-provided sentence into words and print them one per line.

```python
# Input: "Python is fun"
# Output:
# Python
# is
# fun
```

#### **Task 5: CSV Splitter**
Split this string: `"Alice,Math,85"` and print each part labeled (e.g., Name, Subject, Marks).

```python
# Output:
# Name: Alice
# Subject: Math
# Marks: 85
```

#### **Task 6: Word Count**
Ask the user for a sentence and print the number of words in it using `split()`.

---

### ✅ **Lecture #3 Tasks: `partition()`**

#### **Task 7: Email Parser**
Ask the user for an email and extract the username and domain using `partition("@")`.

```python
# Input: "user123@gmail.com"
# Output:
# Username: user123
# Domain: gmail.com
```

#### **Task 8: Separate Front and Back**
Partition a string at a given word and print what's before and after.

```python
# Input: "The quick brown fox", partition word: "brown"
# Output:
# Before: The quick
# After: fox
```

#### **Task 9: Handle Missing Separator**
Use `partition()` on a string that **doesn't** contain the separator and show the output tuple.

---

