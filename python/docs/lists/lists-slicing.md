---
layout: page
title: Python Lists - Slicing 
description: Master Python data types with this comprehensive guide. Learn about numeric, string, boolean, and collection data types with examples, exercises, and tasks. Perfect for beginners and professionals to enhance their Python programming skills.  
keywords: Python data types, Python numeric types, Python string type, Python boolean type, Python collection types, Python data type examples, Python data type exercises, Python programming for beginners, learn Python data types, Python coding tasks
toc: toc/python-toc.html
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


