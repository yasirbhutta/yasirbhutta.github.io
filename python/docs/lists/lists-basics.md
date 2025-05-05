---
layout: page
title: Python List - Comprehensive Guide with Examples and Exercises  
description: Master Python data types with this comprehensive guide. Learn about numeric, string, boolean, and collection data types with examples, exercises, and tasks. Perfect for beginners and professionals to enhance their Python programming skills.  
keywords: Python data types, Python numeric types, Python string type, Python boolean type, Python collection types, Python data type examples, Python data type exercises, Python programming for beginners, learn Python data types, Python coding tasks
toc: toc/python-toc.html
---

- A **list** in Python is one of the most commonly used data structures. It allows you to store a collection of items (which can be of different types) in a single variable. Lists are very flexible and easy to use, making them a great tool for beginners to understand.

**Creating a List**

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

**Accessing Elements in a List**

You can access individual elements in a list using their index.

```python
# Access the first element (index 0)
print(fruits[0])  # Output: apple

# Access the second element (index 1)
print(fruits[1])  # Output: banana

# Access the last element (index -1)
print(fruits[-1])  # Output: cherry
```

**Modifying Elements in a List**

Since lists are mutable, you can change an element in a list by assigning a new value to a specific index.

```python
# Change the first element of the list
fruits[0] = "orange"
print(fruits)  # Output: ['orange', 'banana', 'cherry']
```

### **Task 9: Creating a List**  
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

### **Task 10: Changing an Item in a List**  
Write a Python program that:  
- Creates a list with **three colors**.  
- Changes the **first color** to a new one.  
- Prints the updated list.  

**Example Output:**  
```
Original List: ['Red', 'Blue', 'Green']
Updated List: ['Yellow', 'Blue', 'Green']
```

---

### **Task 11: Adding to a List**  
Write a Python program that:  
- Creates an empty list.  
- Asks the user to enter **three city names** and adds them to the list.  
- Prints the final list.  

**Example Input:**  
```
Enter a city: Paris  
Enter a city: London  
Enter a city: Tokyo  
```

**Example Output:**  
```
Cities: ['Paris', 'London', 'Tokyo']
```

---


### **Task 16: Creating and Accessing a List**  
Write a Python program that:  
- Creates a list of **five favorite movies**.  
- Prints the **entire list**.  
- Accesses and prints the **third movie** in the list using indexing.  
- Changes the **last movie** in the list to a new movie.  
- Prints the updated list.  

**Example Output:**  
```
Original List: ['Inception', 'Titanic', 'Avatar', 'Interstellar', 'Joker']
Third movie: Avatar
Updated List: ['Inception', 'Titanic', 'Avatar', 'Interstellar', 'The Dark Knight']
```
