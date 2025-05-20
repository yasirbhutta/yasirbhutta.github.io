---
layout: page
title: Python Sets - Comprehensive Guide with Examples and Exercises  
description: Master Python data types with this comprehensive guide. Learn about numeric, string, boolean, and collection data types with examples, exercises, and tasks. Perfect for beginners and professionals to enhance their Python programming skills.  
keywords: Python data types, Python numeric types, Python string type, Python boolean type, Python collection types, Python data type examples, Python data type exercises, Python programming for beginners, learn Python data types, Python coding tasks
toc: toc/python.html
---

## Sets

In Python, a **set** is an unordered collection of unique elements, meaning no duplicates are allowed. Sets are useful when you want to store multiple items but don't need to keep them in a particular order, and you want to ensure that each item only appears once.

### Key Points about Sets:
- **Unordered:** The elements in a set do not have a specific order. For more details, see [Appendix A](#appendix-a-unordered-nature-of-sets-in-python)
- **Unique:** Sets automatically remove any duplicate items.
- **Mutable:** You can add or remove elements from a set.
- **Immutable Elements:** The items in a set must be immutable (e.g., numbers, strings, or tuples).

### Creating a Set
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

### Common Operations with Sets

1. **Adding Elements:**
   Use the `add()` method to add an item to a set.

   ```python
   fruits = {"apple", "banana"}
   fruits.add("cherry")
   print(fruits)  # Output: {'apple', 'banana', 'cherry'}
   ```

2. **Removing Elements:**
   Use `remove()` or `discard()` to remove an item.

   ```python
   fruits.remove("banana")
   print(fruits)  # Output: {'apple', 'cherry'}
   ```

3. **Set Operations:**
   Sets support mathematical operations like **union**, **intersection**, and **difference**.

   - **Union (`|`)**: Combines elements from both sets.
   - **Intersection (`&`)**: Finds common elements between sets.
   - **Difference (`-`)**: Finds elements in one set but not the other.

   ```python
   set1 = {1, 2, 3}
   set2 = {3, 4, 5}
   
   # Union
   print(set1 | set2)  # Output: {1, 2, 3, 4, 5}

   # Intersection
   print(set1 & set2)  # Output: {3}

   # Difference
   print(set1 - set2)  # Output: {1, 2}
   ```

### When to Use Sets?
- When you want to eliminate duplicates from a list.
- When you need to perform operations like union and intersection.
- When the order of elements doesn't matter.

- [How to: Add or Remove Elements in a Set](https://www.youtube.com/watch?v=96f2SKK_QZk&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=98)
- [How to: Create Empty Set in Python](https://www.youtube.com/watch?v=nmI7BGXPA4I&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=77)
- [Find the Union of Two Sets in Python](https://www.youtube.com/watch?v=YDyCNYCUK9A&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=72)
  

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
