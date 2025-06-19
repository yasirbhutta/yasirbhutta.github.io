---
layout: page
title: "Python Tuple Methods - Complete Guide with Examples"
description: Learn Python tuple methods with practical examples. Explore built-in tuple functions like count(), index(), and more for efficient Python programming.
keywords: Python tuple methods, tuple in Python, Python count() method, Python index() method, tuple functions, immutable sequences Python, Python tuples tutorial, tuple operations
author: Muhammad Yasir Bhutta
course: python
topic: tuples
toc: toc/ms-excel-toc.html
show_toc: true
show_practice_progress: true
show_mini_project: false
prev: /python/docs/tuples/tuples-slicing.html
next: /python/docs/sorting.html
breadcrumb:
  - title: Home
    url: /
  - title: Python
    url: /python/
  - title: Tuples
    url: /python/docs/tuples/
---

# Tuple Methods

Tuples are [immutable](../data-types/immutable-mutable.md) sequences in Python, which means they have fewer methods than lists since they can't be modified after creation. Here are the most important tuple methods and operations:

## Common Tuple Methods

### 1. count()
**Definition**: Returns the number of times a specified value appears in the tuple.

**Syntax**: 
```python
tuple.count(value)
```

**Example**:
```python
my_tuple = (1, 2, 3, 2, 4, 2)
print(my_tuple.count(2))  # Output: 3
```

### 2. index()
**Definition**: Searches the tuple for a specified value and returns its position.

**Syntax**:
```python
tuple.index(value, start, end)
```

**Example**:
```python
my_tuple = ('a', 'b', 'c', 'b', 'a')
print(my_tuple.index('b'))      # Output: 1
print(my_tuple.index('b', 2))  # Output: 3 (searches from position 2)
```

### 3. len()
**Definition**: Returns the number of items in a tuple.

**Syntax**:
```python
len(tuple)
```

**Example**:
```python
my_tuple = (10, 20, 30)
print(len(my_tuple))  # Output: 3
```


