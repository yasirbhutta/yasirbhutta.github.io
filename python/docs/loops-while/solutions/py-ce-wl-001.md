---
layout: page
title: "Python While Loop Exercise - Age and Input Validation | Code Example"
description: "Step-by-step solution for Python while loop exercise age and input validation. Learn how to solve this problem efficiently with clear explanations and example code. Perfect for beginners!"
keywords: Python while loop solution, Python exercise py-ce-wl-001, while loop code example, Python programming solution, learn Python loops, while loop problem answer, Python practice exercises solved
author: Muhammad Yasir Bhutta
course: python
topic: loops-while
show_toc: true
toc: toc/python.html
show_practice_progress: true
show_mini_project: true
prev: /python/docs/loops-for/
next: /python/docs/loop-control-statements/
breadcrumb: 
- title: Control Flow
url: /python/docs/control-flow/
---

[Click here to view problem statement](https://yasirbhutta.github.io/python/docs/loops-while/practice-and-progress/exercises-loops-while.html)

## Solution

```python
while True:
    age_input = input("Enter your age: ")
    if not age_input.isdigit():
        print("Please enter a valid number.")
        continue

    age = int(age_input)
    if age <= 0:
        print("You haven't been born yet!")
        continue
    break

print()
name = input("Enter your name: ")
print(f"Your name is {name} and you are {age} years old.")
print()

exercise = input("Do you like to exercise? (Y/N) only: ").strip().upper()
while exercise != "N":
    print("Choose either Yes (Y) or No (N) only!")
    exercise = input("Do you like to exercise? (Y/N): ").strip().upper()

print()
print("Nice")
```
## Explanation

Here's a line-by-line explanation of the provided code:

### **1. Infinite Loop for Age Input**
```python
while True:
```
- Starts an infinite loop that will keep running until explicitly broken (`break`).

### **2. Prompt User for Age Input**
```python
    age_input = input("Enter your age: ")
```
- Asks the user to enter their age and stores it in `age_input`.

### **3. Check if Input is a Valid Number**
```python
    if not age_input.isdigit():
        print("Please enter a valid number.")
        continue
```
- Checks if `age_input` is not a digit (i.e., not a valid number).
  - If not, it prints an error message and `continue` restarts the loop.

### **4. Convert Input to Integer and Validate Age**
```python
    age = int(age_input)
    if age <= 0:
        print("You haven't been born yet!")
        continue
```
- Converts `age_input` to an integer (`age`).
- Checks if `age` is ≤ 0 (invalid age).
  - If so, it prints a message and `continue` restarts the loop.

### **5. Exit the Loop if Age is Valid**
```python
    break
```
- If the input passes all checks, `break` exits the loop.

### **6. Print a Blank Line for Readability**
```python
print()
```
- Prints a newline for better formatting.

### **7. Prompt User for Name and Display**
```python
name = input("Enter your name: ")
print(f"Your name is {name} and you are {age} years old.")
print()
```
- Asks for the user's name and stores it in `name`.
- Prints the name and age in a formatted string.
- Prints another blank line.

### **8. Ask if User Likes Exercise (Initial Prompt)**
```python
exercise = input("Do you like to exercise? (Y/N) only: ").strip().upper()
```
- Asks the user if they like exercise (expecting `Y` or `N`).
- `.strip()` removes extra whitespace.
- `.upper()` converts input to uppercase for case-insensitive comparison.

### **9. Validate Exercise Input (Must be 'N')**
```python
while exercise == "Y":
    print("Choose either Yes (Y) or No (N) only!")
    exercise = input("Do you like to exercise? (Y/N): ").strip().upper()
```
- If the user enters `"Y"`, the loop forces them to re-enter until they provide `"N"`.
  - (Note: This logic is **backwards**—it should check for invalid inputs instead.)

### **10. Print Final Message**
```python
print()
print("Nice")
```
- Prints a blank line followed by `"Nice"`.

---

## 📘 **Related Topics**

* **Python While Loops: Syntax, Examples & Best Practices** – Learn how to use Python while loops with clear examples, syntax rules, and best practices.
  👉 [Learn more](https://yasirbhutta.github.io/python/docs/loops-while/)
