---
layout: page
title: Python List Methods 
description: Explore all the essential methods for manipulating Python lists. Learn how to add, remove, sort, and search elements with clear examples..  
keywords: Python, lists, methods, append, insert, remove, sort, index, count, pop, del,
toc: toc/python.html
prev: /python/docs/lists/lists-slicing.html
next: /python/docs/sets/
---

## Table of Contents

- [Common List Methods](#common-list-methods)
- More Methods ...
  - [List Index() Method](index-method.md)

## Common List Methods

- `append(item)` – Adds an item to the end  
- `insert(index, item)` – Adds item at specific index  
- `remove(item)` – Removes the first matching item  
- `pop(index)` – Removes item at given index (default is last)
- `sort()` - Sort the list


### Adding Elements to a List
You can add elements to a list using methods like `append()` or `insert()`.

```python

fruits = ['Apple', 'Banana', 'Mango', 'Orange']

# Append an element to the end of the list
fruits.append("Grape")
print(fruits)  # Output: ['Apple', 'Banana', 'Mango', 'Orange', 'Grape']

# Insert an element at a specific position
fruits.insert(1, "Orange")
print(fruits)  # Output: ['Apple', 'Orange', 'Banana', 'Mango', 'Orange', 'Grape']
```

### Removing Elements from a List
Elements can be removed from a list using methods like `remove()`, `pop()`, or `del`.

```python
# Remove a specific element by value
fruits.remove("Banana")
print(fruits)  # Output: ['Apple', 'Orange', 'Mango', 'Orange', 'Grape']

# Remove last element by using pop
fruits.pop() # Output: ['Apple', 'Orange', 'Mango', 'Orange']

# Remove an element by index using pop
fruits.pop(1)
print(fruits)  # Output:  ['Apple', 'Mango', 'Orange']

```
## **📺 Video Tutorial: Adding and Removing Elements from a Python List**  
**This video covers:**  
* ✔️ Adding elements to a list using the `append` \[[00:22](http://www.youtube.com/watch?v=x98wvk-4MHw&t=22)\] and `insert` \[[00:35](http://www.youtube.com/watch?v=x98wvk-4MHw&t=35)\] methods.
* ✔️ Comparing the performance of `append` and `insert` \[[00:52](http://www.youtube.com/watch?v=x98wvk-4MHw&t=52)\].
* ✔️ Removing elements from a list using the `remove` \[[01:24](http://www.youtube.com/watch?v=x98wvk-4MHw&t=84)\] and `pop` \[[01:45](http://www.youtube.com/watch?v=x98wvk-4MHw&t=105)\] methods.
* ✔️ Demonstrating how `pop` removes and returns elements \[[01:50](http://www.youtube.com/watch?v=x98wvk-4MHw&t=110)\], including the last item when no index is specified \[[02:34](http://www.youtube.com/watch?v=x98wvk-4MHw&t=154)\].

{% assign video_type = "video" %}
{% assign video_id = "x98wvk-4MHw" %}
{% include youtube-video.html video_type=video_type video_id=video_id %}


## **📺 Python Tutorial in Urdu: List pop() Method**  
**This video covers:**  
* ✔️ A list of colors as an example \[[00:00](http://www.youtube.com/watch?v=S6HkdH4Xnog&t=0)\].
* ✔️ The `pop` method removes the last item in a list by default and displays it \[[00:38](http://www.youtube.com/watch?v=S6HkdH4Xnog&t=38)\].
* ✔️ Remove an item at a specific index by specifying it in the `pop` method \[[00:46](http://www.youtube.com/watch?v=S6HkdH4Xnog&t=46)\].

{% assign video_type = "video" %}
{% assign video_id = "S6HkdH4Xnog" %}
{% include youtube-video.html video_type=video_type video_id=video_id %}

### Sorting Elements in a List
You can sort elements in a list using the `sort()` method.

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
fruits = ['Apple', 'banana', 'Mango', 'orange']

# Sort a list in ascending order (modifies the original list)
numbers.sort()
print(numbers)  # Output: [1, 1, 2, 3, 4, 5, 5, 6, 9]

# Sort a list in descending order
numbers.sort(reverse=True)
print(numbers)  # Output: [9, 6, 5, 5, 4, 3, 2, 1, 1]

# Case-sensitive sort (ASCII order: uppercase comes before lowercase)
fruits.sort()
print(fruits)  # Output: ['Apple', 'Mango', 'banana', 'orange']

```

For more details on sorting, see [Sorting Techniques in Python - Sorting How To](../sorting.md)

## Example: Real-World Uses of Python List Common Methods: Managing Tasks & Organizing Data

### 1. **`append(item)` – Adding a new task to a to-do list**  
   - **Scenario:** You have a to-do list, and you want to add a new task at the end.  
   - **Code Example:**  
     ```python
     todo_list = ["Buy groceries", "Finish report"]
     todo_list.append("Call mom")
     print(todo_list)  # Output: ["Buy groceries", "Finish report", "Call mom"]
     ```

### 2. **`insert(index, item)` – Adding an emergency task at a specific position**  
   - **Scenario:** Your to-do list has tasks, but an urgent meeting comes up, so you insert it at the top.  
   - **Code Example:**  
     ```python
     todo_list = ["Buy groceries", "Finish report"]
     todo_list.insert(0, "Attend emergency meeting")
     print(todo_list)  # Output: ["Attend emergency meeting", "Buy groceries", "Finish report"]
     ```

### 3. **`remove(item)` – Removing a completed task**  
   - **Scenario:** You finished "Buy groceries," so you remove it from the list.  
   - **Code Example:**  
     ```python
     todo_list = ["Buy groceries", "Finish report", "Call mom"]
     todo_list.remove("Buy groceries")
     print(todo_list)  # Output: ["Finish report", "Call mom"]
     ```

### 4. **`pop(index)` – Removing the last task (or a specific one)**  
   - **Scenario:** You decide to drop the last task (or a task at a given position).  
   - **Code Example:**  
     ```python
     todo_list = ["Finish report", "Call mom", "Pay bills"]
     last_task = todo_list.pop()  # Removes & returns "Pay bills"
     print(todo_list)  # Output: ["Finish report", "Call mom"]
     
     # Removing a task at index 0
     first_task = todo_list.pop(0)  # Removes & returns "Finish report"
     print(todo_list)  # Output: ["Call mom"]
     ```

### 5. **`sort()` – Sorting a list of names alphabetically**  
   - **Scenario:** You have a list of attendees for an event and want to sort them alphabetically.  
   - **Code Example:**  
     ```python
     attendees = ["Zara", "Alice", "Bob", "Eve"]
     attendees.sort()
     print(attendees)  # Output: ["Alice", "Bob", "Eve", "Zara"]
     ```

## Tasks

### **Task 1: Using List Methods**  
Write a Python program that:  
- Creates a list of **three programming languages**.  
- Adds a new language using `append()`.  
- Inserts another language at the second position using `insert()`.  
- Removes the last language using `pop()`.  
- Prints the final list.  

**Example Output:**  
```
Initial List: ['Python', 'Java', 'C++']
After Append: ['Python', 'Java', 'C++', 'JavaScript']
After Insert: ['Python', 'Ruby', 'Java', 'C++', 'JavaScript']
After Pop: ['Python', 'Ruby', 'Java', 'C++']
```
---

### **Task 2: Adding to a List**  
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

### **Include Error Handling Tips**
- Mention common mistakes (e.g., `IndexError` when accessing out-of-range indices).
- Suggest using `len(list)` to check list length.

**Example Addition:**
```python
colors = ["red", "blue"]
try:
    print(colors[2])  # Raises IndexError
except IndexError:
    print("Index out of range!")
```

## More Methods

### [Index() Method - To find the position of the first occurrence](index-method.md)

## Further reading
- [Python Nested List](https://www.youtube.com/watch?v=BOIn5oW868A&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=111)
- [Check if Data Structure is Empty Using 'not' Operator](https://www.youtube.com/watch?v=K4WUapBO_E0&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=2)
- [Remove duplicate elements from a list](https://www.youtube.com/watch?v=RekQ2j4yzIQ&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=1)

## References

- [1] Python Software Foundation, *The Python Tutorial: Data Structures*. \[Online]. Available: [https://docs.python.org/3/tutorial/datastructures.html](https://docs.python.org/3/tutorial/datastructures.html). \[Accessed: May 5, 2025].

