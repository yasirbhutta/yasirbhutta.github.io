---
layout: page
title: "Python Loop Control Statements – Break, Continue & Pass"
description: Explore Python loop control statements—break, continue. Learn how to manage loop flow for more efficient and readable code.
keywords: Python loop control statements, break continue else, Python loops tutorial, loop flow control in Python, Python programming guide, Python break example, Python continue usage, Python loop else
author: Muhammad Yasir Bhutta
course: python
topic: loop-control-statements
show_toc: true
toc: toc/python.html
show_practice_progress: true
show_mini_project: true
prev: /python/docs/loops-for/
next: /python/docs/loop-control-statements/
breadcrumb:
  - title: Home
    url: /
  - title: Control Flow
    url: /python/docs/control-flow/
---

## Table of Contents

1. [break Statement](#1-break)
2. [continue Statement](#2-continue)
3. [pass Statement](#3-pass)
4. [Tasks](#4-tasks)

These statements modify the behavior of loops.

**break:** Terminates the loop entirely.
**continue:** Skips the current iteration and moves to the next one.
**pass:** Does nothing, often used as a placeholder.

## 1. `break` Statement

Exits the loop prematurely.

```python
for item in sequence:
    if some_condition:
        break  # exit the loop
```

### Example 1: Using Break Statement in a Loop with Range

```python
for x in range(3):
    if x == 1:
        break
    print(x)
```
### Example 2: Exit a loop when a number is found
```python
# Search for the number 5 and exit the loop when found
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    print(f"Checking {num}...")
    if num == 5:
        print("Number 5 found! Exiting the loop.")
        break  # Exit the loop
```

**Output**:
```
Checking 1...
Checking 2...
Checking 3...
Checking 4...
Checking 5...
Number 5 found! Exiting the loop.
```

### **📺 Python Tutorial in Urdu: Using Python break statement with a while loop**  

{% assign video_type = "video" %}
{% assign video_id = "KWuyQ7HQUBE" %}
{% include youtube-video.html video_type=video_type video_id=video_id %}


### Example 3: Password validation with `while` loop
```python
# Keep asking for a password until the correct one is entered
correct_password = "python123"

while True:
    user_input = input("Enter the password: ")
    if user_input == correct_password:
        print("Access granted!")
        break  # Exit the loop
    else:
        print("Wrong password. Try again!")
```

### Example 4: **Temperature Monitoring**  
Stop monitoring if temperature exceeds a safe limit.
```python
temperatures = [25, 30, 32, 28, 45, 29, 33]  # Sensor readings

for temp in temperatures:
    if temp > 40:
        print(f"ALERT: Temperature {temp}°C is unsafe! Shutting down.")
        break  # Exit immediately
    print(f"Temperature {temp}°C is safe.")
```

**Output**:
```
Temperature 25°C is safe.
Temperature 30°C is safe.
Temperature 32°C is safe.
Temperature 28°C is safe.
ALERT: Temperature 45°C is unsafe! Shutting down.
```

---

### Example 5: **Login system with limited attempts.** 

**Use Case:** 
```python
max_attempts = 3
correct_password = "secret123"

for attempt in range(1, max_attempts + 1):
    password = input(f"Attempt {attempt}: Enter password: ")
    if password != correct_password:
        print("Wrong password. Try again.")
        continue  # Skip to next attempt
    else:
        print("Login successful!")
        break  # Exit loop on success
else:
    print("Account locked. Too many failed attempts.")
```

**Output** (if user fails 3 times):
```
Attempt 1: Enter password: hello
Wrong password. Try again.
Attempt 2: Enter password: test
Wrong password. Try again.
Attempt 3: Enter password: 123
Wrong password. Try again.
Account locked. Too many failed attempts.
```

## 2. `continue` Statement

Skips the current iteration and proceeds to the next iteration of the loop.

```python
for item in sequence:
    if some_condition:
        continue  # skip the rest of the code in this iteration
    # code to execute if some_condition is False
```

### **📺 Video Tutorial: How to Effectively Use Break and Continue Statements**  

{% assign video_type = "video" %}
{% assign video_id = "LfF9CsyVRgU" %}
{% include youtube-video.html video_type=video_type video_id=video_id %}
 
### Example 6: Skip even numbers using `continue` Statement

Skips the **current iteration** and moves to the next loop cycle.

```python
# Print only odd numbers (skip even numbers)
for num in range(1, 11):
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num)
```

**Output**:
```
1
3
5
7
9
```

### Example 7: **Data Cleaning using `continue` Statement**  
Skip invalid entries when processing a dataset.
```python
user_ages = [20, 15, "unknown", 30, -5, 25]  # Some invalid data

print("Valid ages:")
for age in user_ages:
    if not isinstance(age, int) or age < 0 or age > 120:
        continue  # Skip invalid entries
    print(f"- {age} years old")
```

**Output**:
```
Valid ages:
- 20 years old
- 15 years old
- 30 years old
- 25 years old
```

---

## 3. `pass` Statement

A null statement, used as a placeholder.

```python
if condition:
    pass  # do nothing
```

The `pass` statement is often used in loops as a placeholder or to intentionally skip certain conditions without any action. Here are practical examples demonstrating `pass` in different loop scenarios.  

---

### **Example 8: Basic `pass` in a `for` Loop**  
**Use Case:** Skip specific items without any action.  

```python
fruits = ["apple", "banana", "cherry", "kiwi"]  

for fruit in fruits:  
    if fruit == "banana":  
        pass  # Do nothing for banana  
    else:  
        print(fruit)  
```

**Output:**  
```
apple  
cherry  
kiwi  
```  

**Explanation:**  
- The loop checks if the fruit is `"banana"`.  
- If yes, `pass` does nothing and moves to the next iteration.  
- Otherwise, it prints the fruit.  

---

### **Example 9: `pass` vs `continue` in a Loop**  
**Key Difference:**  
- `pass` → Does nothing, continues execution.  
- `continue` → Skips the rest of the loop body and moves to the next iteration.  

#### **Example with `pass`**  
```python
numbers = [1, 2, 3, 4, 5]  

for num in numbers:  
    if num == 3:  
        pass  # Just a placeholder, no action  
    print(num)  # This line still runs  
```

**Output:**  
```
1  
2  
3  
4  
5  
```  

#### **Example with `continue`**  
```python
for num in numbers:  
    if num == 3:  
        continue  # Skips printing for 3  
    print(num)  
```

**Output:**  
```
1  
2  
4  
5  
```  

---

### **Example 10: `pass` in a `while` Loop (Placeholder Logic)**  
**Use Case:** Temporarily ignore a condition while developing.  

```python
count = 0  

while count < 5:  
    if count == 2:  
        pass  # Will handle this case later  
    else:  
        print(f"Count: {count}")  
    count += 1  
```

**Output:**  
```
Count: 0  
Count: 1  
Count: 3  
Count: 4  
```  

**Explanation:**  
- When `count == 2`, `pass` does nothing, but the loop continues.  
- All other values are printed normally.  

---

### **Example 11: Using `pass` in Nested Loops**  
**Use Case:** Skip certain combinations in a nested loop.  

```python
for i in range(3):  
    for j in range(3):  
        if i == j:  
            pass  # Skip when i and j are equal  
        else:  
            print(f"i={i}, j={j}")  
```

**Output:**  
```
i=0, j=1  
i=0, j=2  
i=1, j=0  
i=1, j=2  
i=2, j=0  
i=2, j=1  
```  

**Explanation:**  
- When `i == j`, `pass` ignores the case.  
- Otherwise, it prints the combination.  

---

## **When to Use `pass`?**  
✅ **Placeholder for future code**  
✅ **Intentionally doing nothing in a condition**  
✅ **Silently ignoring exceptions**  

🚫 **Don’t use when:**  
- You want to skip iterations (use `continue`).  
- You want to exit a loop (use `break`).  

---

## 4. Tasks

### **Task 1: Coffee Machine Stock Check using `break` Statement**  
   Simulate a coffee machine that stops serving when a drink is out of stock.  
   - **Input List**: `["latte", "cappuccino", "espresso", "mocha", "out_of_stock", "latte"]`  
   - **Goal**: Loop through the list and stop when "out_of_stock" is found.  
   - **Example Output**:  
     ```
     Serving latte...  
     Serving cappuccino...  
     Serving espresso...  
     Serving mocha...  
     Out of stock! Machine stopping.  
     ```
     
### **Task 2: Skip Negative Numbers**  
   Calculate the sum of positive numbers in a list, ignoring negatives.  
   - **Input**: `[5, -2, 10, -8, 3]`  
   - **Goal**: Use `continue` to skip negative values.  
   - **Output**: `Sum of positive numbers: 18`

### **Task 3: Simple Calculator with Exit using `continue` and `break`**  
   Create a loop that:  
   - Lets users type numbers to add.  
   - Skips non-numeric inputs (use `continue`).  
   - Exits when the user types "quit" (use `break`).  
   - **Example Output**:  
     ```
     Enter a number (or 'quit'): 5  
     Enter a number (or 'quit'): ten  
     Invalid input!  
     Enter a number (or 'quit'): 3  
     Enter a number (or 'quit'): quit  
     Total: 8  
     ```

### **Task 4: Movie Ticket Checker**  
   Loop through a list of ages and:  
   - Skip ages < 0 (invalid).  
   - Stop if a "VIP" (age 100+) is found.  
   - **Input**: `[25, -5, 30, 105, 40]`  
   - **Output**:  
     ```
     Valid age: 25  
     Skipped invalid age.  
     Valid age: 30  
     VIP detected! Stopping sales.  
     ```

### **Task 5: Flight Booking System**  
   Check seat availability in a list. Stop when a seat is found, or skip "reserved" seats.  
   - **Input**: `["reserved", "reserved", "available", "reserved"]`  
   - **Output**:  
     ```
     Seat 1: Reserved.  
     Seat 2: Reserved.  
     Seat 3: Available! Booked successfully.  
     ```

## 📘 **Related Topics**

* **Python FOR Loops** – A `for` loop in Python is a programming statement that repeats a block of code a fixed number of times.
  👉 [Learn more](../loops-for/)
* **Python while Loops** – A `while` loop in python is a control flow statement that repeatedly executes a block of code until a specified condition is met.
  👉 [Learn more](../loops-while/)
* **Python else Clause in Loops** – In Python, the `else` clause can be used with loops (`for` and `while`).
  👉 [Learn more](../else-clauses-on-loops/)
* **Match Statement (Python 3.10+)** – Introduced in Python 3.10, **`match-case`** is a modern way to handle data-driven decision-making.
  👉 [Learn more](../match-statement/)
