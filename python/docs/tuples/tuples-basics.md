---
layout: page
title: Tuple in Python
description: Master Python data types with this comprehensive guide. Learn about numeric, string, boolean, and collection data types with examples, exercises, and tasks. Perfect for beginners and professionals to enhance their Python programming skills.  
keywords: Python data types, Python numeric types, Python string type, Python boolean type, Python collection types, Python data type examples, Python data type exercises, Python programming for beginners, learn Python data types, Python coding tasks
toc: toc/python-toc.html
---

### 3.4.1 Tuple in Python

- In python, a tuple is an immutable sequence of elements. it is similar to a list, but the elements of a tuple cannot be modified once they are created.
- Tuple is a collection data type in python. It is useful for storing multiple related values as a single unit.
- Sequence types in python - list, tuple and range

**Creating a Tuple in Python**

**A tuple is created by enclosing elements within parentheses () and separating them with commas.** While parentheses are technically optional, it's generally considered best practice to use them for clarity and consistency.

**Python Tutorial:How to create a tuple in Python**

{% assign video_type = "video" %}
{% assign video_id = "QpRiHuQycXg" %}

{% include youtube-video.html video_type=video_type video_id=video_id %}


**Example**

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

- [Example: How to create an Empty tuple and Single value tuple](https://www.youtube.com/watch?v=nGIWcYXj580&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=83)

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
