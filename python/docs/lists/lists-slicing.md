---
layout: page
title: "List Slicing in Python: Syntax and Examples"
description: Learn how to use Python list slicing to extract and manipulate parts of lists. This guide provides clear explanations and examples for efficient coding.  
keywords: Python, List, Slicing, Syntax, Examples, Tutorial, Guide, Coding, list slicing in python, list slicing tasks, list slicing exercises, list slicing syntax, list tasks.
toc: toc/python-toc.html
prev: /python/docs/lists/lists-basics.html
next: /python/docs/lists/lists-methods.html

---

**Slicing** a list in Python means extracting a portion (or subsequence) of the list using a specific syntax:

## **Syntax:**

```python
list[start:stop:step]
```

* `start`: index to begin slicing (inclusive)
* `stop`: index to end slicing (exclusive)
* `step`: how many elements to skip (default is 1)

---

## **Examples:**

```python
numbers = [10, 20, 30, 40, 50, 60, 70]
```

### 1. Get elements from index 1 to 4:

```python
numbers[1:5]   # [20, 30, 40, 50]
```

### 2. Get every second element:

```python
numbers[::2]   # [10, 30, 50, 70]
```

### 3. Reverse the list:

```python
numbers[::-1]  # [70, 60, 50, 40, 30, 20, 10]
```

### 4. From index 3 to end:

```python
numbers[3:]    # [40, 50, 60, 70]
```

### 5. From start to index 4:

```python
numbers[:5]    # [10, 20, 30, 40, 50]
```


## **Tasks**

1. **Positive Index Slicing**
   - Given `numbers = [10, 20, 30, 40, 50, 60]`, extract:
     - First 3 elements
     - Elements from index 2 to 4
     - Last 2 elements (using positive indices)

2. **Negative Index Practice**
   - For `letters = ['a', 'b', 'c', 'd', 'e', 'f']`:
     - Get all elements except the last one using negative indexing
     - Extract ['c', 'd'] using negative indices
     - Get the last element using negative index

3. **Step Value Exercises**
   - Using `data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`:
     - Extract all even-indexed items (0, 2, 4...)
     - Get every 3rd item starting from index 1
     - Reverse the list using step value


