---
layout: page
title: Python Sets - Comprehensive Guide with Examples and Exercises  
description: Master Python data types with this comprehensive guide. Learn about numeric, string, boolean, and collection data types with examples, exercises, and tasks. Perfect for beginners and professionals to enhance their Python programming skills.  
keywords: Python data types, Python numeric types, Python string type, Python boolean type, Python collection types, Python data type examples, Python data type exercises, Python programming for beginners, learn Python data types, Python coding tasks
toc: toc/python-toc.html
---

In Python, a **set** is an unordered collection of unique elements, meaning no duplicates are allowed. Sets are useful when you want to store multiple items but don't need to keep them in a particular order, and you want to ensure that each item only appears once.

**Creating a Set**

You can create a set using curly braces `{}` or the `set()` function.

```python
# Creating a set using curly braces
my_set = {1, 2, 3, 4, 5}

# Creating a set using the set() function
my_set = set([1, 2, 3, 4, 5])
```

### Example:

```python
# Creating a set
fruits = {"apple", "banana", "cherry", "apple"}

# Displaying the set
print(fruits)  # Output: {'apple', 'banana', 'cherry'}
```
Notice how `apple` only appears once, even though we tried to add it twice.

### **Task 14: Creating a Set**  
Write a Python program that:  
- Creates a set with **four different numbers**.  
- Prints the set.  

**Example Output:**  
```
Numbers: {1, 2, 3, 4}
```

---

### **Task 15: Removing Duplicates Using a Set**  
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

### **Task 17: Creating and Using a Set**  
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

### **Task 18: Set Operations**  
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
