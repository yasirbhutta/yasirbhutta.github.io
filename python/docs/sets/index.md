---
layout: page
title: "Python Sets Tutorial: Create, Use, and Perform Set Operations with Examples"
description: "Master Python data types with this comprehensive guide. Learn about numeric, string, boolean, and collection data types with examples, exercises, and tasks. Perfect for beginners and professionals to enhance their Python programming skills."  
keywords: Python data types, Python numeric types, Python string type, Python boolean type, Python collection types, Python data type examples, Python data type exercises, Python programming for beginners, learn Python data types, Python coding tasks
course: python
topic: input-output
show_toc: true
toc: toc/python.html
show_practice_progress: null
show_mini_project: false
prev: /python/docs/sets/
next: /python/docs/dictionaries/
breadcrumb:
  - title: Home
    url: /
  - title: Python
    url: /python/
  - title: Sets
    url: /python/docs/sets/
---

## Table of Contents

1. [What is Sets](#1-what-is-sets)
2. [Key Points about Sets](#2-key-points-about-sets)
3. [Creating Sets](#3-creating-sets)
4. [Common Set Methods](#4-common-set-methods)
5. [Practical Examples](#5-practical-examples)
6. [Tasks](#6-tasks)

## 1. What is Sets

In Python, a **set** is an unordered collection of unique elements, meaning no duplicates are allowed. Sets are useful when you want to store multiple items but don't need to keep them in a particular order, and you want to ensure that each item only appears once.

## 2. Key Points about Sets:

- **Unordered:** The elements in a set do not have a specific order.
- **Unique:** Sets automatically remove any duplicate items.
- **Mutable:** You can add or remove elements from a set.
- **Immutable Elements:** The items in a set must be immutable (e.g., numbers, strings, or tuples).

## 3. Creating Sets

```python
# Create an empty set
empty_set = set()  # Note: {} creates an empty dictionary, not set!

# Create a set with elements
fruits = {'apple', 'banana', 'orange'}
numbers = {1, 2, 3, 4, 5}

# Convert list to set (removes duplicates)
colors = ['red', 'blue', 'green', 'blue', 'red']
unique_colors = set(colors)  # {'red', 'blue', 'green'}
```
[Video Tutorial: How to Create Empty Set in Python](https://www.youtube.com/watch?v=nmI7BGXPA4I&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=77)

### Another Example:

```python
# Creating a set
fruits = {"apple", "banana", "cherry", "apple"}

# Displaying the set
print(fruits)  # Output: {'apple', 'banana', 'cherry'}
```
Notice how `apple` only appears once, even though we tried to add it twice.


## 4. Common Set Methods

### 1. Adding Elements

```python
fruits = {'apple', 'banana'}
fruits.add('orange')  # Adds single element
fruits.update(['kiwi', 'mango'])  # Adds multiple elements
print(fruits)  # {'apple', 'banana', 'orange', 'kiwi', 'mango'}
```

**Real-world use**: Adding new unique tags to a blog post.

### 2. Removing Elements

```python
numbers = {1, 2, 3, 4, 5}
numbers.remove(3)  # Raises error if element doesn't exist
numbers.discard(10)  # No error if element doesn't exist
popped = numbers.pop()  # Removes and returns arbitrary element
numbers.clear()  # Removes all elements
```

[Video Tutorial: How to Add or Remove Elements in a Set](https://www.youtube.com/watch?v=96f2SKK_QZk&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=98)

**Real-world use**: Removing items from a shopping cart while ensuring no duplicates.

### 3. Set Operations

Sets support mathematical operations like **union**, **intersection**, and **difference**.

   - **Union (`|`)**: Combines elements from both sets.
   - **Intersection (`&`)**: Finds common elements between sets.
   - **Difference (`-`)**: Finds elements in one set but not the other.

```python
a = {1, 2, 3}
b = {3, 4, 5}

# Union (elements in either set)
print(a | b)  # {1, 2, 3, 4, 5}

# Intersection (elements in both sets)
print(a & b)  # {3}

# Difference (elements in a but not b)
print(a - b)  # {1, 2}

# Symmetric difference (elements in either set but not both)
print(a ^ b)  # {1, 2, 4, 5}
```

[Video Tutorial: Find the Union of Two Sets in Python](https://www.youtube.com/watch?v=YDyCNYCUK9A&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=72)

**Real-world use**: Finding common friends between two users (intersection).

### 4. Membership Testing

```python
vowels = {'a', 'e', 'i', 'o', 'u'}
print('a' in vowels)  # True
print('z' not in vowels)  # True
```

**Real-world use**: Checking if a username is in a blocked list.

### 5. Set Comparisons

```python
set1 = {1, 2}
set2 = {1, 2, 3}

print(set1 <= set2)  # True (subset)
print(set2 >= set1)  # True (superset)
print(set1.isdisjoint({4, 5}))  # True (no common elements)
```

**Real-world use**: Checking if all required permissions are in a user's permission set.

## 5. Practical Examples

### Example 1: Removing duplicates from a list

```python
names = ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob']
unique_names = list(set(names))
print(unique_names)  # Order not guaranteed: ['Alice', 'Bob', 'Charlie']
```

### Example 2: Finding common interests between users

```python
user1_interests = {'music', 'movies', 'sports'}
user2_interests = {'books', 'music', 'travel'}

common_interests = user1_interests & user2_interests
print(f"You both like: {common_interests}")  # {'music'}
```

### Example 3: Validating survey responses

```python
valid_answers = {'yes', 'no', 'maybe'}
responses = ['yes', 'no', 'sometimes', 'maybe', 'no']

invalid = set(responses) - valid_answers
print(f"Invalid responses: {invalid}")  # {'sometimes'}
```

## When to Use Sets

- When you need to ensure elements are unique
- When you need fast membership testing (faster than lists)
- When mathematical set operations are needed
- When order doesn't matter

---

## 6. Tasks

### **Task 1: Creating a Set**  
Write a Python program that:  
- Creates a set with **four different numbers**.  
- Prints the set.  

**Example Output:**  
```
Numbers: {1, 2, 3, 4}
```

### **Task 2: Removing Duplicates Using a Set**  
Write a Python program that:  
- Takes a list with **duplicate numbers**.  
- Converts it into a set to remove duplicates.  
- Prints the unique numbers.  

**Example Input:**  
```
Original List: [1, 2, 2, 3, 3, 4, 5]
```

**Example Output:**  
```
Unique Numbers: {1, 2, 3, 4, 5}
```

### **Task 3: Creating and Using a Set**  
Write a Python program that:  
- Creates a set of **unique numbers** from a given list (including duplicate values).  
- Prints the unique numbers.  

**Example Input:**  
```
Original List: [1, 2, 2, 3, 4, 4, 5]
```

**Expected Output:**  
```
Unique Numbers: {1, 2, 3, 4, 5}
```

---

### **Task 4: Set Operations**  
Write a Python program that:  
- Creates two sets: one with **even numbers** and one with **prime numbers** (both from 1 to 10).  
- Finds the **union** (all unique numbers from both sets).  
- Finds the **intersection** (numbers that are in both sets).  
- Prints the results.  

**Expected Output:**  
```
Even Numbers: {2, 4, 6, 8, 10}
Prime Numbers: {2, 3, 5, 7}
Union: {2, 3, 4, 5, 6, 7, 8, 10}
Intersection: {2}
```
