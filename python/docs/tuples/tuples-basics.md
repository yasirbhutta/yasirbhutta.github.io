---
layout: page
title: "Python Tuples Tutorial for Beginners | Learn Tuple Basics with Examples"
description: Explore the basics of Python tuples in this beginner-friendly tutorial. Learn tuple creation, properties, and usage with clear examples to enhance your Python skills.
keywords: Python tuples, Python tuple tutorial, Python tuple basics, tuples in Python, learn Python tuples, tuple examples Python, Python data structures, Python tutorial for beginners, immutable data types Python, how to use tuples in Python
author: Muhammad Yasir Bhutta
course: python
topic: tuples
toc: toc/ms-excel-toc.html
prev: /python/docs/tuples/
next: /python/docs/tuples/tuples-slicing.html
breadcrumb:
  - title: Home
    url: /
  - title: Python
    url: /python/
  - title: Tuples
    url: /python/docs/tuples/
---

## Tuple in Python

- In python, a tuple is an [immutable](../data-types/immutable-mutable.md) sequence of elements. it is similar to a list, but the elements of a tuple cannot be modified once they are created.
- Tuple is a collection data type in python. It is useful for storing multiple related values as a single unit.
- Sequence types in python - list, tuple and range

## Basic Operations

### 1. Creating Tuples

**A tuple is created by enclosing elements within parentheses () and separating them with commas.** While parentheses are technically optional, it's generally considered best practice to use them for clarity and consistency.

## Example 1

Some common ways to create tuples in Python include:

```python
tup = (1,2,3)
print(tup) # Output: (1, 2, 3)
# check the type of variable
print(type(tup)) # Output: <class 'tuple'>

# another example to create tuple
tup1 = 4,5,6
print(tup1) # Output: (4, 5, 6)

# tuple with mixed datatypes
tup_mixed = (7, "String", 7.8)
print(tup_mixed)

```

## **📺 Python Tutorial: Learn 5 Easy Ways to Create Tuples in Python**  
This video explains how to create tuples in Python.

{% assign video_type = "video" %}
{% assign video_id = "QpRiHuQycXg" %}
{% include youtube-video.html video_type=video_type video_id=video_id %}

### 2. Conversion
```python
# List to tuple
list_data = [1, 2, 3]
tuple_data = tuple(list_data)  # (1, 2, 3)

# String to tuple
str_data = "hello"
tuple_chars = tuple(str_data)  # ('h', 'e', 'l', 'l', 'o')
```

A **nested tuple** is a tuple that contains one or more tuples as element.

**Empty and single item tuple:**

- A special problem is the construction of tuples containing 0 or 1 item.
- Empty tuples are constructed by an empty pair of parentheses
- A tuple with one item is constructed by following a value with a comma (it is not sufficient to enclose a single value in parentheses).

- [Python tuples example : How to create an Empty tuple and Single value tuple](../../videos/tuples-empty-single-value.md)

### 2. Accessing Elements

```python
my_tuple = ('a', 'b', 'c', 'd', 'e')

# Indexing
print(my_tuple[0])    # 'a' (first element)
print(my_tuple[-1])   # 'e' (last element)

# Slicing
print(my_tuple[1:3])  # ('b', 'c')
print(my_tuple[:2])   # ('a', 'b')
print(my_tuple[2:])   # ('c', 'd', 'e')
print(my_tuple[::-1]) # ('e', 'd', 'c', 'b', 'a') (reverse)
```

for more details, see [Tuples Slicing in Python](tuples-slicing.md)

### Python tuple example 2: How to Access Tuple Items in Python

{% assign video_type = "video" %}
{% assign video_id = "6dZUdvI8V_Q" %}
{% include youtube-video.html video_type=video_type video_id=video_id %}

## Tuple Operations

### 3. Concatenation (+)
```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5)
combined = tuple1 + tuple2  # (1, 2, 3, 4, 5)
```

### 4. Repetition (*)
```python
repeated = ('hi',) * 3  # ('hi', 'hi', 'hi')
```

### 5. Membership Testing
```python
colors = ('red', 'green', 'blue')
print('green' in colors)    # True
print('yellow' not in colors)  # True
```

### 6. Iteration
```python
for item in ('a', 'b', 'c'):
    print(item)
```

### 7. Unpacking tuples
**Tuple unpacking allows you to assign the values of a tuple to multiple variables in a single step.** Each element of the tuple is assigned to a corresponding variable.

```python
point = (10, 20)
x, y = point  # x=10, y=20

# Extended unpacking
values = (1, 2, 3, 4, 5)
a, b, *rest = values  # a=1, b=2, rest=[3, 4, 5]
```

### Python tuple example 4: Unpacking a Tuple in Python

{% assign video_type = "video" %}
{% assign video_id = "fi-nvcQukRc" %}
{% include youtube-video.html video_type=video_type video_id=video_id %}


- The number of variables on the left side must match the number of elements in the tuple, or you’ll get a `ValueError`.
  
```python
# Correct unpacking - number of variables matches tuple elements
point = (3, 5)
x, y = point
print(f"x: {x}, y: {y}")  # Output: x: 3, y: 5

# Incorrect unpacking - will raise ValueError
colors = ('red', 'green', 'blue')
# color1, color2 = colors  # This would raise ValueError
# Correct way would be:
color1, color2, color3 = colors
print(color1, color2, color3)  # Output: red green blue
```

---

**Tuples are [immutable](../data-types/immutable-mutable.md)**, meaning once created, their elements cannot be changed, added, or removed. However, **they can store mutable objects** (like lists or dictionaries), which *can* be modified.

for more details, see [Immutable vs. Mutable](../data-types/immutable-mutable.md)

### Example:
```python
my_tuple = (1, 2, [3, 4])  # Tuple with an immutable list inside

# my_tuple[0] = 10  ❌ Fails (can't modify tuple)
my_tuple[2].append(5)      # ✅ Works (modifying the inner list)

print(my_tuple)  # Output: (1, 2, [3, 4, 5])
```

## Tasks

### **Task 1: Creating a Tuple**  
Write a Python program that:  
- Creates a tuple with **three** different items (e.g., a number, a word, and a decimal).  
- Prints the **entire tuple**.  
- Prints the **first item** in the tuple.  

**Example Output:**  
```
Tuple: (10, 'Apple', 3.5)
First item: 10
```

### **Task 2: Tuple Unpacking**  
Write a Python program that:  
- Creates a tuple with three values: name, age, and country.  
- Uses **tuple unpacking** to assign each value to separate variables.  
- Prints the extracted values.  

**Example Output:**  
```
Name: Alice
Age: 25
Country: USA
```

---

### **Task 3: Accessing Tuple Elements**  
Write a Python program that:  
- Creates a tuple with **five numbers**.  
- Prints the **last number** using negative indexing.  

**Example Output:**  
```
Numbers: (5, 10, 15, 20, 25)
Last number: 25
```
### Task 4: Calculate the Sum of a Tuple Using a For Loop
Write a Python function called `sum_tuple` that takes one argument: a tuple of numbers. The function should return the sum of all the numbers in the tuple using a `for` loop (not the built-in `sum()` function).

**Input:**

A tuple containing numerical values (integers or floats).
Example:

```python
(1, 2, 3, 4)
```

**Expected Output:**

A single numerical value representing the sum of the numbers in the tuple.
For the input above, the output would be:

```python
10
```

[Click here to see the solution ✨](/python/videos/tuples-sum-using-for-loop.md)

### Task 5: Printing Tuple Elements with a While Loop
Write a Python function called `print_tuple_while` that takes a tuple of strings as input. This function should iterate through the tuple using a `while` loop and print each element of the tuple on a separate line.

**Input:**

A tuple of strings, for example:
```python
my_tuple = ("apple", "banana", "cherry")
```

**Expected Output:**

```
apple
banana
cherry
```

**Here's a starting point for the function:**

```python
def print_tuple_while(input_tuple):
    index = 0
    # Complete the while loop to print each element
    # of the input_tuple
    pass

# Example usage:
my_tuple = ("apple", "banana", "cherry")
print_tuple_while(my_tuple)
```

[Click here to see the solution ✨](../../videos/tuples-elements-using-while.md)

### Task 6: How to Swap Variables in One Line of Code using Tuple Unpacking

Write a Python function called `swap_variables` that takes two variables, `a` and `b`, as input. The function should swap the values of these two variables using the one-line tuple unpacking technique and then return the new values of `a` and `b` as a tuple.

**Input:**

Two variables of any data type. For example:
```python
x = 10
y = 5
```

**Expected Output:**

A tuple containing the swapped values. For the example input above:
```
(5, 10)
```

**Here's a starting point for the function:**

```python
def swap_variables(a, b):
    # Write your one-line swap using tuple unpacking here
    return a, b

# Example usage:
x = 10
y = 5
swapped_x, swapped_y = swap_variables(x, y)
print(f"Original x: {x}, y: {y}")
print(f"Swapped x: {swapped_x}, y: {swapped_y}")
```

[Click here to see the solution ✨](../../videos/tuples-swap-variables.md)
