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
next: /phthon/docs/functions/sumif.html
breadcrumb:
  - title: Home
    url: /
  - title: Python
    url: /python/
  - title: Tuples
    url: /python/docs/tuples/
---

## Tuple in Python

- In python, a tuple is an immutable sequence of elements. it is similar to a list, but the elements of a tuple cannot be modified once they are created.
- Tuple is a collection data type in python. It is useful for storing multiple related values as a single unit.
- Sequence types in python - list, tuple and range

**Creating a Tuple in Python**

**A tuple is created by enclosing elements within parentheses () and separating them with commas.** While parentheses are technically optional, it's generally considered best practice to use them for clarity and consistency.

## **📺 Python Tutorial: Learn 5 Easy Ways to Create Tuples in Python**  
This video explains how to create tuples in Python.

**This video covers:**  
* ✔️ **Using Parentheses:** Tuples can be created by enclosing comma-separated items within parentheses \[[00:05](http://www.youtube.com/watch?v=QpRiHuQycXg&t=5)\].
* ✔️ **Without Parentheses:** You can also create a tuple by simply separating items with commas \[[00:46](http://www.youtube.com/watch?v=QpRiHuQycXg&t=46)\].
* ✔️ **Nested Tuples:** Tuples can contain other tuples as elements \[[00:56](http://www.youtube.com/watch?v=QpRiHuQycXg&t=56)\].
* ✔️ **Different Data Types:** Tuples can store multiple items of different data types \[[01:20](http://www.youtube.com/watch?v=QpRiHuQycXg&t=80)\].
* ✔️ **Tuple Function:** The `tuple` function can create a tuple from a list or other iterable, like converting a string into a tuple of characters \[[01:35](http://www.youtube.com/watch?v=QpRiHuQycXg&t=95)\].

{% assign video_type = "video" %}
{% assign video_id = "QpRiHuQycXg" %}
{% include youtube-video.html video_type=video_type video_id=video_id %}

## Example

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

tup4 = tuple('string')
print(tup4) # Output: ('s','t','r','i','n','g')

```

A nested tuple is a tuple that contains one or more tuples as element.

## Empty and single item tuple

- A special problem is the construction of tuples containing 0 or 1 item.
- Empty tuples are constructed by an empty pair of parentheses
- A tuple with one item is constructed by following a value with a comma (it is not sufficient to enclose a single value in parentheses.

- [Python tuples example: How to create an Empty tuple and Single value tuple](/python/videos/tuples-empty-single-value.md)

## Accessing the elements of Tuple

- [Example #1: Learn how to print elements of a tuple in Python using while loop](https://www.youtube.com/watch?v=MGgazFPSrS4&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=32)

- [Example #2: How to: Access Tuple Items in Python](https://www.youtube.com/watch?v=6dZUdvI8V_Q&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=81)

- [Example #3: How to Calculate the Sum of a Tuple Using a For Loop](https://www.youtube.com/watch?v=PFNJl8i4y1c&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=33)

## Unpacking tuples

**Tuple unpacking allows you to assign the values of a tuple to multiple variables in a single step.** Each element of the tuple is assigned to a corresponding variable.

- [Example #1: Unpacking a Tuple in Python](https://www.youtube.com/watch?v=fi-nvcQukRc&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=105)
- [Example #2: How to Swap Variables in One Line of Code using Tuple Unpacking](https://www.youtube.com/watch?v=MCeTYJVktmU&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=45)

**Example:**

```python
my_tuple = (1, 2, 3)
a, b, c = my_tuple

print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3
```

- The number of variables on the left side must match the number of elements in the tuple, or you’ll get a `ValueError`.
  
## Example #2

```python
# Tuples are immutable
# but they can contain mutable objects
```



### **Task 6: Creating a Tuple**  
Write a Python program that:  
- Creates a tuple with **three** different items (e.g., a number, a word, and a decimal).  
- Prints the **entire tuple**.  
- Prints the **first item** in the tuple.  

**Example Output:**  
```
Tuple: (10, 'Apple', 3.5)
First item: 10
```

### **Task 7: Tuple Unpacking**  
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

### **Task 8: Accessing Tuple Elements**  
Write a Python program that:  
- Creates a tuple with **five numbers**.  
- Prints the **last number** using negative indexing.  

**Example Output:**  
```
Numbers: (5, 10, 15, 20, 25)
Last number: 25
```
