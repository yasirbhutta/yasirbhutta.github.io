---
layout: page
title: Python Dictionary Methods – Beginner-Friendly Guide with Examples  
description: Discover the most important Python dictionary methods with clear explanations and real-world examples. Learn how to use get, keys, values, items, update, pop, setdefault, copy, and more to master dictionary operations in Python. Perfect for beginners and students.  
keywords: Python dictionary methods, Python dictionaries tutorial, Python get method, Python update dictionary, Python pop method, Python setdefault, Python copy dictionary, beginner Python dictionaries, Python dictionary examples, learn Python dictionaries
course: python
topic: dictionaries
toc: toc/python.html
show_toc: true
show_practice_progress: true
show_mini_project: false
prev: /python/docs/dictionaries/dict-basics.md
next: /python/docs/list-comprehension/
breadcrumb:
  - title: Home
    url: /
  - title: Python
    url: /python/
---

## Table of Contents

1. [Dictionaries Common Methods](#1-common-methods)
2. [Tasks](#2-tasks)
3. 
Dictionaries in Python are versatile data structures that store key-value pairs. Here are some essential dictionary methods with beginner-friendly explanations and real-world examples:

## 1. Common Methods

### 1.1 `get(key[, default])`
**Purpose:** Safely retrieve a value for a given key without raising an error if the key doesn't exist.

**Example:**
```python
user = {'name': 'Alice', 'age': 30, 'email': 'alice@example.com'}

# Get existing key
print(user.get('name'))  # Output: Alice

# Get non-existent key
print(user.get('address'))  # Output: None
print(user.get('address', 'Not provided'))  # Output: Not provided
```

**Real-world use:** Looking up product prices in an e-commerce system where some products might not have prices defined.

### 1.2 `keys()`
**Purpose:** Get all keys in the dictionary.

**Example:**
```python
car = {'make': 'Toyota', 'model': 'Camry', 'year': 2022}

print(car.keys())  # Output: dict_keys(['make', 'model', 'year'])
```

**Real-world use:** Getting all field names from a database record before processing them.

### 1.3 `values()`
**Purpose:** Get all values in the dictionary.

**Example:**
```python
grades = {'math': 90, 'science': 85, 'history': 88}

print(grades.values())  # Output: dict_values([90, 85, 88])
```

**Real-world use:** Calculating the average of all values in a gradebook or survey results.

### 1.4 `items()`
**Purpose:** Get all key-value pairs as tuples.

**Example:**
```python
inventory = {'apples': 10, 'bananas': 5, 'oranges': 8}

for item, quantity in inventory.items():
    print(f"We have {quantity} {item}")
```

**Real-world use:** Displaying all items in a shopping cart with their quantities.

### 1.5 `update([other])`
**Purpose:** Update the dictionary with key-value pairs from another dictionary.

**Example:**
```python
profile = {'name': 'Bob', 'age': 25}
additional_info = {'occupation': 'developer', 'city': 'New York'}

profile.update(additional_info)
print(profile)
# Output: {'name': 'Bob', 'age': 25, 'occupation': 'developer', 'city': 'New York'}
```

**Real-world use:** Merging user profile information from multiple sources.

### 1.6 `pop(key[, default])`
**Purpose:** Remove and return the value for a key.

**Example:**
```python
config = {'theme': 'dark', 'font_size': 14, 'language': 'en'}

removed_value = config.pop('theme')
print(removed_value)  # Output: dark
print(config)  # Output: {'font_size': 14, 'language': 'en'}
```

**Real-world use:** Removing and processing items from a task queue.

### 1.7 `popitem()`
**Purpose:** Remove and return the last inserted key-value pair.

**Example:**
```python
settings = {'volume': 80, 'brightness': 70, 'contrast': 50}

last_setting = settings.popitem()
print(last_setting)  # Output: ('contrast', 50)
```

**Real-world use:** Processing items in LIFO (last-in, first-out) order.

### 1.8 `clear()`
**Purpose:** Remove all items from the dictionary.

**Example:**
```python
shopping_cart = {'shirt': 2, 'pants': 1, 'shoes': 1}

shopping_cart.clear()
print(shopping_cart)  # Output: {}
```

**Real-world use:** Emptying a shopping cart after checkout.

### 1.9 `setdefault(key[, default])`
**Purpose:** Get a value for a key, setting it to a default if the key doesn't exist.

**Example:**
```python
employee = {'name': 'John', 'position': 'manager'}

salary = employee.setdefault('salary', 50000)
print(salary)  # Output: 50000
print(employee)  # Output: {'name': 'John', 'position': 'manager', 'salary': 50000}
```

**Real-world use:** Initializing default values in configuration settings.

### 1.10 `copy()`
**Purpose:** Create a shallow copy of the dictionary.

**Example:**
```python
original = {'a': 1, 'b': 2, 'c': 3}
duplicate = original.copy()

duplicate['d'] = 4
print(original)  # Output: {'a': 1, 'b': 2, 'c': 3}
print(duplicate)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

**Real-world use:** Creating a backup of configuration before making changes.

Here are three beginner-friendly tasks to practice working with Python dictionaries, along with sample solutions:

## 2. Tasks

### **Task 1: Student Grade Tracker**
**Objective:** Create a program that stores student names and their grades, then calculates the average grade.

**Requirements:**
- Use a dictionary to store student names (keys) and their grades (values).
- Allow adding new students and updating grades.
- Calculate and display the average grade.

**Example Output:**
```
Students: {'Alice': 85, 'Bob': 90, 'Charlie': 78}
Average grade: 84.33
```

<details>
<summary>🔹 Solution</summary>

```python
grades = {}

# Add students
grades["Alice"] = 85
grades["Bob"] = 90
grades["Charlie"] = 78

# Calculate average
average = sum(grades.values()) / len(grades)

print(f"Students: {grades}")
print(f"Average grade: {average:.2f}")
```
</details>

---

### **Task 2: Inventory Management System**
**Objective:** Build a simple inventory system that tracks product stock and allows restocking.

**Requirements:**
- Use a dictionary to store product names (keys) and quantities (values).
- Allow checking stock, adding new products, and updating quantities.
- Print a warning if stock is low (< 5 items).

**Example Output:**
```
Current Inventory: {'apples': 10, 'bananas': 3, 'oranges': 7}
Warning: bananas stock is low (3 left)!
```

---

### **Task 3: Contact Book**
**Objective:** Create a simple contact book where users can add, search, and delete contacts.

**Requirements:**
- Store contacts as `{name: phone_number}`.
- Allow adding, searching, and deleting contacts.
- Print all contacts in a formatted way.

**Example Output:**
```
Contacts:
- Alice: 123-456-7890
- Bob: 987-654-3210
Search for 'Alice': 123-456-7890
```

---
