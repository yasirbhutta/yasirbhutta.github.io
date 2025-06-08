# Reading and Writing Files in Python: A Beginner's Guide

Working with files is a fundamental skill in Python programming. Whether you're saving user data, reading configuration files, or processing large datasets, file operations are essential. Let's break down the basics with clear examples.

## Basic Syntax for File Operations

### Opening a File

Python uses the `open()` function to work with files. The basic syntax is:

```python
file_object = open('filename', 'mode')
```

Common modes:
- `'r'` - Read (default)
- `'w'` - Write (overwrites existing file)
- `'a'` - Append (adds to existing file)
- `'r+'` - Read and write
- `'b'` - Binary mode (for non-text files)

### Closing a File

Always close files when done to free system resources:

```python
file_object.close()
```

### The Better Way: `with` Statement

Using `with` automatically closes the file, even if an error occurs:

```python
with open('filename', 'mode') as file_object:
    # work with the file here
# file is automatically closed here
```

## Reading Files

### Example 1: Reading an Entire File

```python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

**Real-world use**: Reading a configuration file for your application settings.

### Example 2: Reading Line by Line

```python
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())  # strip() removes extra whitespace and newlines
```

**Real-world use**: Processing a log file line by line to find errors.

### Example 3: Reading All Lines into a List

```python
with open('example.txt', 'r') as file:
    lines = file.readlines()
    print(lines)  # List where each element is a line from the file
```

**Real-world use**: Reading a CSV file where each line represents a data record.

## Writing Files

### Example 4: Writing to a File (Overwrites)

```python
with open('output.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a second line.\n")
```

**Real-world use**: Saving program results or user data to a file.

### Example 5: Appending to a File

```python
with open('log.txt', 'a') as file:
    file.write("New log entry at: 2023-11-15 14:30\n")
```

**Real-world use**: Adding entries to a log file without deleting previous ones.

## Practical Examples

### Example 6: Simple To-Do List Application

```python
# Add a task
def add_task(task):
    with open('todo.txt', 'a') as file:
        file.write(f"{task}\n")

# View all tasks
def view_tasks():
    try:
        with open('todo.txt', 'r') as file:
            tasks = file.readlines()
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks yet!")

# Usage
add_task("Buy groceries")
add_task("Finish Python project")
view_tasks()
```

### Example 8: Configuration File Handling

```python
def read_config(config_file='config.ini'):
    config = {}
    with open(config_file, 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.strip().split('=', 1)
                config[key] = value
    return config

# Sample config.ini:
# username=admin
# timeout=30
# theme=dark
```

## Handling Exceptions

Always handle potential errors when working with files:

```python
try:
    with open('nonexistent.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found!")
except PermissionError:
    print("Error: Permission denied!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

## Best Practices

1. Always use the `with` statement for automatic file closing
2. Handle exceptions to make your program robust
3. For large files, read line by line instead of loading everything into memory
4. Specify the encoding if working with non-ASCII text: `open('file.txt', 'r', encoding='utf-8')`
5. When writing, consider adding newline characters (`\n`) explicitly
