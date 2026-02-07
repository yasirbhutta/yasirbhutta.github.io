---
layout: page
title: "Python Lists: Basics, Operations, and Examples"
description: Learn the fundamentals of Python lists, including creation, manipulation, indexing, and common operations. Explore practical examples and best practices.
keywords: Python, lists, basics, tutorial, examples, operations, indexing, programming
toc: toc/python.html
prev: /python/docs/tuples/
next: /python/docs/lists/lists-slicing.html
course: python
topic: lists
show_toc: true
show_practice_progress: true
show_mini_project: false
breadcrumb: 
- title: Lists
url: /python/docs/lists/
---

## Table of Contents
1. [Introduction to Lists](#introduction)
2. [Characteristics of Lists](#key-characteristics-of-lists)
3. [Creating a List](#creating-a-list)
4. [Accessing Elements](#creating-a-list)
5. [Modifying Elements](#modifying-elements-in-a-list-using-index)
6. [Iterating Through a List](#iterating-through-a-list)
7. [Practice Tasks](#-tasks)


## Introduction

- A **list** in Python is one of the most commonly used data structures. It allows you to store a collection of items (which can be of different types) in a single variable. Lists are very flexible and easy to use, making them a great tool for beginners to understand.

### Key Characteristics of Lists:
1. **Ordered**: The items in a list have a specific order, and this order will not change unless explicitly modified.
2. **[Mutable](../data-types/immutable-mutable.md)**: You can change, add, or remove items after the list has been created.
3. **Heterogeneous**: A list can contain different data types, such as integers, strings, and even other lists.
4. **Indexed**: Each item in a list has an index, starting from `0` for the first item.

## Creating a List
You can create a list by placing items inside square brackets `[]`, separated by commas.

```python
# A list of integers
numbers = [1, 2, 3, 4, 5]

# A list of strings
fruits = ["apple", "banana", "cherry"]

# A list of mixed data types
mixed_list = [1, "hello", 3.14, True]

# An empty list
empty_list = []
```

## Accessing Elements in a List using Index
You can access individual elements in a list using their index.

```python
# Access the first element (index 0)
print(fruits[0])  # Output: apple

# Access the second element (index 1)
print(fruits[1])  # Output: banana

# Access the last element (index -1)
print(fruits[-1])  # Output: cherry
```

## Modifying Elements in a List using Index
Since lists are mutable, you can change an element in a list by assigning a new value to a specific index.

```python
# Change the first element of the list
fruits[0] = "orange"
print(fruits)  # Output: ['orange', 'banana', 'cherry']
```

## List Operations

```python
# Concatenation
new_list = [1, 2] + [3, 4]  # [1, 2, 3, 4]

# Repetition
repeated = [0] * 3          # [0, 0, 0]

# Membership testing
if 'a' in my_list:
    print("Found!")

# Length
length = len(my_list)       # Number of elements
```

## Iterating Through a List
You can use a loop to iterate through all the elements in a list.

```python
# Print each fruit in the list
for fruit in fruits:
    print(fruit)

# Output:
# mango
# grape
```

## **📺 Video Tutorial: Lists in Python**  
**This video covers:**  
- ✔️ How to **create** lists.  
- ✔️ Accessing List Elements
  - Positive indexing (list[0] for the first item)
  - Negative indexing (list[-1] for the last item) 
- ✔️ length of the list.  


{% assign video_type = "video" %}
{% assign video_id = "LKZmCAL92pI" %}
{% include youtube-video.html video_type=video_type video_id=video_id %}

---

## **📺 Video Tutorial: 6 Ways to use List in For loop in Python**  
**This video covers:**  
* ✔️ The basic method for printing the values of a list \[[00:08](http://www.youtube.com/watch?v=-FErgsl9njQ&t=8)\].
* ✔️ Accessing the index and values of a list \[[00:50](http://www.youtube.com/watch?v=-FErgsl9njQ&t=50)\].
* ✔️ Modifying elements within a list \[[01:29](http://www.youtube.com/watch?v=-FErgsl9njQ&t=89)\].
* ✔️ Creating a new list using list comprehension \[[02:28](http://www.youtube.com/watch?v=-FErgsl9njQ&t=148)\].
* ✔️ Filtering items in a list based on a condition \[[03:09](http://www.youtube.com/watch?v=-FErgsl9njQ&t=189)\].
* ✔️ Using nested for loops with lists \[[03:56](http://www.youtube.com/watch?v=-FErgsl9njQ&t=236)\].

{% assign video_type = "video" %}
{% assign video_id = "-FErgsl9njQ" %}
{% include youtube-video.html video_type=video_type video_id=video_id %}

---

## ✅ Tasks

### **Task 1: Creating a List**  
Write a Python program that:  
- Creates a list of **four favorite foods**.  
- Prints the **entire list**.  
- Prints the **second food** from the list.  

**Example Output:**  
```
Favorite Foods: ['Pizza', 'Burger', 'Pasta', 'Ice Cream']
Second food: Burger
```

---

### **Task 2: Changing an Item in a List**  
Write a Python program that:  
- Creates a list with **three colors**.  
- Changes the **first color** to a new one.  
- Prints the updated list.  

**Example Output:**  
```
Original List: ['Red', 'Blue', 'Green']
Updated List: ['Yellow', 'Blue', 'Green']
```

### **Task 3: Creating and Accessing a List**

Write a Python program that:

* Creates a list of **five Islamic boys' names**.
* Prints the **entire list**.
* Accesses and prints the **third name** in the list using indexing.
* Changes the **last name** in the list to a new name.
* Prints the updated list.

**Example Output:**

```
Original List: ['Ahmed', 'Hassan', 'Omar', 'Yusuf', 'Zayd']
Third name: Omar
Updated List: ['Ahmed', 'Hassan', 'Omar', 'Yusuf', 'Bilal']
```

