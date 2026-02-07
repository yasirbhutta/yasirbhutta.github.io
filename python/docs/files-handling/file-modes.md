---
layout: page
title: "File Modes in Python: Explained"
description: Learn how to read and write files in Python with beginner-friendly examples! This guide covers file modes (r, w, a, r+), real-world use cases (CSV, logs, configs), and best practices for handling text and binary files.
keywords: Python file handling, read write files Python, file modes Python, open() function Python, with statement Python, read() write() Python, file operations Python, beginner Python file examples, text file CSV Python, binary files Python, file handling tutorial, Python I/O operations, file modes explained, Python readlines() writelines(), append file Python, exception handling files
author: Muhammad Yasir Bhutta
course: python
topic: files-handling
toc: toc/python.html
prev: /python/docs/modules/numpy.html
next: /python/docs/modules/scipy.html
breadcrumb: 
- title: Python
url: /python/
---

Understanding file modes is essential when working with files in Python. File modes determine how you can interact with a file - whether you can read from it, write to it, or both. Let's explore each mode with simple examples.

## Basic File Modes

### 1. Read Mode (`'r'`)
- Opens a file for reading (default mode)
- File must exist
- You cannot modify the file

```python
# Example: Reading a diary entry
with open('diary.txt', 'r') as file:
    content = file.read()
    print("My Diary Entry:")
    print(content)
```

**Real-world analogy**: Like opening a book to read it (you can't write in it).

### 2. Write Mode (`'w'`)
- Opens a file for writing
- Creates the file if it doesn't exist
- **Erases all existing content** if the file exists

```python
# Example: Creating a shopping list (overwrites any existing list)
with open('shopping_list.txt', 'w') as file:
    file.write("1. Milk\n")
    file.write("2. Eggs\n")
    file.write("3. Bread\n")
```

**Real-world analogy**: Like getting a brand new notebook - if one exists with the same name, it gets thrown away first.

### 3. Append Mode (`'a'`)
- Opens a file for writing
- Creates the file if it doesn't exist
- New content is added at the end (preserves existing content)

```python
# Example: Adding to a shopping list
with open('shopping_list.txt', 'a') as file:
    file.write("4. Apples\n")
    file.write("5. Chicken\n")
```

**Real-world analogy**: Like adding new pages to an existing notebook without removing old pages.

## Combined Modes

### 4. Read and Write Mode (`'r+'`)
- Opens a file for both reading and writing
- File must exist
- Writing starts at the beginning (can overwrite existing content)

```python
# Example: Updating a score file
with open('scores.txt', 'r+') as file:
    content = file.read()
    if "High Score: 50" in content:
        # Move back to start to overwrite
        file.seek(0)
        file.write("High Score: 100")
```

**Real-world analogy**: Like having a whiteboard where you can both read what's written and modify it.

### 5. Write and Read Mode (`'w+'`)
- Opens a file for both writing and reading
- Creates the file if it doesn't exist
- **Erases all existing content** if the file exists

```python
# Example: Creating and immediately reading a note
with open('quick_note.txt', 'w+') as file:
    file.write("Remember to call mom!")
    file.seek(0)  # Go back to start to read
    print(file.read())
```

**Real-world analogy**: Like getting a brand new whiteboard where you can write and then immediately read what you wrote.

## Special Modes

### 6. Binary Modes (`'rb'`, `'wb'`, `'ab'`, etc.)
- Used for non-text files (images, executables, etc.)
- Add `'b'` to any mode (like `'rb'` or `'wb'`)

```python
# Example: Copying an image
with open('photo.jpg', 'rb') as source:
    with open('photo_copy.jpg', 'wb') as target:
        target.write(source.read())
```

**Real-world analogy**: Like working with the raw data of a file rather than its text content.

## Common Mistakes to Avoid

1. **Trying to read a file opened in write mode**:
   ```python
   with open('example.txt', 'w') as file:
       print(file.read())  # Error! Can't read in 'w' mode
   ```

2. **Opening a non-existent file in read mode**:
   ```python
   with open('nonexistent.txt', 'r') as file:  # FileNotFoundError
       content = file.read()
   ```

3. **Forgetting that 'w' mode erases the file**:
   ```python
   # This will delete all existing content!
   with open('important_data.txt', 'w') as file:
       file.write("New content")
   ```

## Practical Example: Simple User Database

```python
# Adding a new user (append mode)
def add_user(username, password):
    with open('users.txt', 'a') as file:
        file.write(f"{username},{password}\n")

# Checking user login (read mode)
def check_login(username, password):
    with open('users.txt', 'r') as file:
        for line in file:
            stored_user, stored_pass = line.strip().split(',')
            if stored_user == username and stored_pass == password:
                return True
    return False

# Usage
add_user("alice", "secure123")
add_user("bob", "password456")

print(check_login("alice", "secure123"))  # True
print(check_login("eve", "hacker123"))    # False
```

Remember to always choose the right mode for your task to avoid accidentally losing data or getting errors!