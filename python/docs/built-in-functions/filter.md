---
layout: page
title: "Python filter() Function - Complete Guide with Examples & Real-World Uses"
description: Learn how to use Python's filter() function with clear syntax, beginner examples, and real-life use cases. Master filtering lists, dictionaries, and more efficiently!
keywords: Python filter function, filter() in Python, Python list filtering, lambda with filter, Python data filtering examples, how to use filter() Python, Python filter list by condition, real-world Python filter examples, Python functional programming, filter vs list comprehension
author: Muhammad Yasir Bhutta
course: python
topic: built-in-functions
show_toc: false
toc: toc/python.html
show_practice_progress: false
show_mini_project: false
prev: /ms-excel/docs/functions/what-is-functions.html
next: /ms-excel/docs/functions/sumif.html
breadcrumb:
  - title: Home
    url: /
  - title: Python
    url: /python/
---

## What is the `filter()` Function?

The `filter()` function is a built-in Python function that allows you to process an iterable (like a list, tuple, etc.) and extract items that meet a specific condition. It "filters out" elements based on whether they satisfy a given criterion.

## Syntax

```python
filter(function, iterable)
```

- **function**: A function that tests if each element of the iterable meets a condition (returns `True` or `False`)
- **iterable**: The sequence you want to filter (list, tuple, etc.)

The function returns a filter object (an iterator), which you can convert to a list or other sequence type.

## Basic Usage

### Example 1: Filtering even numbers

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_even(num):
    return num % 2 == 0

even_numbers = list(filter(is_even, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]
```

### Example 2: Using lambda function

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using lambda instead of a separate function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]
```

## Real-Life Examples

### 1. Filtering Valid Email Addresses

```python
emails = [
    "user@example.com",
    "invalid.email",
    "another.user@domain.org",
    "missing@dotcom",
    "valid@test.co.uk"
]

def is_valid_email(email):
    return '@' in email and '.' in email.split('@')[-1]

valid_emails = list(filter(is_valid_email, emails))
print(valid_emails)
# Output: ['user@example.com', 'another.user@domain.org', 'valid@test.co.uk']
```

### 2. Filtering Products Above a Certain Price

```python
products = [
    {"name": "Laptop", "price": 999.99},
    {"name": "Mouse", "price": 19.99},
    {"name": "Keyboard", "price": 49.99},
    {"name": "Monitor", "price": 199.99},
    {"name": "Headphones", "price": 79.99}
]

expensive_products = list(filter(lambda p: p["price"] > 100, products))
print(expensive_products)
# Output: [{'name': 'Laptop', 'price': 999.99}, {'name': 'Monitor', 'price': 199.99}]
```

### 3. Filtering Active Users

```python
users = [
    {"username": "alice", "active": True},
    {"username": "bob", "active": False},
    {"username": "charlie", "active": True},
    {"username": "dave", "active": False},
    {"username": "eve", "active": True}
]

active_users = list(filter(lambda user: user["active"], users))
print(active_users)
# Output: [{'username': 'alice', 'active': True}, 
#          {'username': 'charlie', 'active': True}, 
#          {'username': 'eve', 'active': True}]
```

## Key Points to Remember

1. `filter()` returns an iterator, so you often need to convert it to a list or other sequence type.
2. The function you pass to `filter()` should return `True` (to keep) or `False` (to remove) for each element.
3. `filter()` is often used with lambda functions for simple conditions.
4. It's more memory efficient than list comprehensions for large datasets since it returns an iterator.

## Alternative: List Comprehension

Many filtering operations can also be done with list comprehensions:

```python
# Using filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Equivalent list comprehension
even_numbers = [x for x in numbers if x % 2 == 0]
```

Choose based on readability and performance needs - `filter()` can be more memory efficient for very large datasets.

## 🧠 Practice & Progress

- [📝 Multiple-Choice Questions (MCQs)](practice-and-progress/mcqs-built-in-functions.md)

## 📘 **Related Topics**

- [Python Built-in Functions](index.md)