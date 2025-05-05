---
layout: page
title: "Introduction to Python Dictionaries: Concepts, Usage, and Examples"

description: Master Python data types with this comprehensive guide. Learn about numeric, string, boolean, and collection data types with examples, exercises, and tasks. Perfect for beginners and professionals to enhance their Python programming skills.  
keywords: Python data types, Python numeric types, Python string type, Python boolean type, Python collection types, Python data type examples, Python data type exercises, Python programming for beginners, learn Python data types, Python coding tasks
toc: toc/python-toc.html
---

In Python, a **dictionary** is a collection of key-value pairs. Each key in a dictionary is unique, and it is associated with a value. Dictionaries are used to store data values like a map or a real-life dictionary where each word (key) has a definition (value). They are mutable, meaning you can change, add, or remove items after the dictionary is created.

**Creating a Dictionary**

You create a dictionary using curly braces `{}` with keys and values separated by a colon `:`. Multiple key-value pairs are separated by commas.

```python
# Example of a dictionary
student = {
    "name": "John",
    "age": 20,
    "courses": ["Math", "Science"]
}
```

**Accessing Values**

You can access the value associated with a specific key by using square brackets `[]` or the `get()` method.

```python
# Accessing values
print(student["name"])  # Output: John
print(student.get("age"))  # Output: 20
```

**Adding or Updating Elements**

You can add a new key-value pair or update an existing one by assigning a value to the key.

```python
# Adding a new key-value pair
student["grade"] = "A"

# Updating an existing value
student["age"] = 21
```

### **Task 12: Creating a Dictionary**  
Write a Python program that:  
- Creates a dictionary with **two items** (name and age).  
- Prints the dictionary.  
- Prints only the **name** from the dictionary.  

**Example Output:**  
```
Person: {'name': 'Alice', 'age': 25}
Name: Alice
```

---

### **Task 13: Adding to a Dictionary**  
Write a Python program that:  
- Creates a dictionary with **name and country**.  
- Adds a new key **"hobby"** with a value.  
- Prints the updated dictionary.  

**Example Output:**  
```
Original Dictionary: {'name': 'John', 'country': 'USA'}
Updated Dictionary: {'name': 'John', 'country': 'USA', 'hobby': 'Reading'}
```

---
