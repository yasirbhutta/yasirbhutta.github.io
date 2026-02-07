---
layout: page
title: "Python Lists: Index Method"
description: Master Python data types with this comprehensive guide. Learn about numeric, string, boolean, and collection data types with examples, exercises, and tasks. Perfect for beginners and professionals to enhance their Python programming skills.
keywords: Python data types, Python numeric types, Python string type, Python boolean type, Python collection types, Python data type examples, Python data type exercises, Python programming for beginners, learn Python data types, Python coding tasks
toc: toc/python.html
course: python
topic: lists
show_toc: true
show_practice_progress: true
show_mini_project: false
breadcrumb: 
- title: Lists
url: /python/docs/lists/
---

The `index()` method in Python is used with **lists** (and also works on tuples and strings) to **find the position of the first occurrence** of a given element.

---

### ✅ **Why We Use `index()`**

We use the `index()` method when we want to **find the position (index number)** of an item in a list. This is helpful when:

* You need to know where an item is located in a list.
* You want to modify or remove an item by its position.
* You need to match data from two lists using positions.

---

### 🔤 **Syntax**

```python
list_name.index(element, start, end)
```

* `element`: The item to search for.
* `start` *(optional)*: Start searching from this index.
* `end` *(optional)*: Stop searching at this index (exclusive).

---

### 🧒 **Beginner Example**

```python
fruits = ["apple", "banana", "cherry", "banana"]
print(fruits.index("banana"))  # Output: 1
```

It returns `1` because the first occurrence of `"banana"` is at index 1.

---

### ⛔ **If the item is not found**

```python
print(fruits.index("orange"))  # Error!
```

This will raise a `ValueError` because `"orange"` is not in the list.

---

### 📌 **Using start and end**

```python
print(fruits.index("banana", 2))  # Output: 3
```

This starts searching from index 2 and finds the second `"banana"` at index 3.

---

### 🌍 **Real-World Example**

Suppose you are building a to-do list app and you want to know where a task is located:

```python
tasks = ["Buy groceries", "Do laundry", "Pay bills", "Call mom"]
task_to_find = "Pay bills"

position = tasks.index(task_to_find)
print(f"'{task_to_find}' is at position {position}")
```

🟢 Output:

```
'Pay bills' is at position 2
```

This could help you highlight the task in the app or remove it after completion.

---

- [List Index Method: Find the Index of an Element in a List](https://www.youtube.com/watch?v=thYJRk4huGE&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=41)