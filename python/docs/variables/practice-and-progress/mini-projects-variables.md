---
layout: page
title: "Mini Projects Using Python Variables | Practice & Progress"
description: Build practical mini‑projects that reinforce Python variable concepts—covering declaration, assignment, scope, naming, and debugging through real‑world challenges.
keywords: python mini projects variables, python variables projects, python hands-on variable projects, python project practice variables, python variable challenges mini projects, python projects for beginners, python variable coding projects, real world python variables, python practical variable exercises, learn python variables by project
author: Muhammad Yasir Bhutta
course: python
topic: variables
show_toc: null
toc: toc/python.html
show_practice_progress: true
show_mini_project: false
prev: /python/docs/variables/practice-and-progress/fill-blanks-variables.html
next: /python/docs/variables/practice-and-progress/mcqs-variables.html
breadcrumb:
  - title: Home
    url: /
  - title: Python
    url: /python/
  - title: Basics
    url: /python/docs/basics/
  - title: Variables
    url: /python/docs/variables/
---

## **Project: The Dynamic User Profile** 📝

This project simulates creating a simple user profile where the information can change, showcasing the flexibility of variables in Python.

---

### **Project Goal**

Create a Python script that stores user profile information (username, age, and a special status) in variables. You will then update these variables to demonstrate how their types can change (dynamic typing) and how to represent an "empty" or unassigned status using `None`.

---

### **Step-by-Step Guide**

#### **Step 1: Create the Initial Profile**

First, let's create variables to hold the user's information. This covers **variable basics**.

```python
# 1. Create a variable to store a username.
# A string is a good choice for text.
username = "CodeWizard"

# 2. Create a variable for the user's age.
# An integer is used for whole numbers.
age = 16

# 3. Create a variable for a special status.
# Let's start with it being empty.
special_status = None

# Now, print the initial profile information.
print("--- Initial User Profile ---")
print("Username:", username)
print("Age:", age)
print("Special Status:", special_status)
print("Type of 'special_status':", type(special_status))
```

**What's happening here?**
* We created three variables: `username`, `age`, and `special_status`.
* We assigned a string to `username`, an integer to `age`, and the special keyword `None` to `special_status`. `None` is used to signify the absence of a value.

---

#### **Step 2: Update the Profile (Dynamic Typing in Action)**

Now, imagine the user has earned a special badge! We will update the `special_status` variable. This demonstrates **dynamic typing**, where a variable can hold different data types.

```python
# The user just earned a "Gold" status!
# Let's update the 'special_status' variable.
print("\n--- Profile Updated! ---")

# This is where dynamic typing happens!
# The 'special_status' variable is about to change from NoneType to a string.
special_status = "Gold Member"

# The user also had a birthday. Let's update their age.
age = age + 1 # Or you can write age += 1

# Print the updated profile.
print("Username:", username)
print("Age:", age)
print("Special Status:", special_status)
print("New type of 'special_status':", type(special_status))
```

**What's happening here?**
* The `special_status` variable, which was previously `None` (type `NoneType`), now holds the string `"Gold Member"` (type `str`). Python automatically handles this change in data type. This is dynamic typing.
* We also updated the `age` by performing a basic calculation.

---

### **Full Code**

Here is the complete script. You can copy and paste this into a Python file (e.g., `profile.py`) and run it.

```python
# --- Step 1: Create the Initial Profile ---

# Create variables for the user profile.
username = "CodeWizard"
age = 16
special_status = None # Use None for an empty or unassigned value

# Print the initial profile information.
print("--- Initial User Profile ---")
print("Username:", username)
print("Age:", age)
print("Special Status:", special_status)
print("Type of 'special_status':", type(special_status))
print("-" * 20) # A separator line for clarity

# --- Step 2: Update the Profile (Dynamic Typing) ---

print("\n--- Profile Updated! ---")

# The 'special_status' variable changes from NoneType to a string.
special_status = "Gold Member"

# The user's age is updated.
age = age + 1

# Print the new profile details.
print("Username:", username)
print("Age:", age)
print("Special Status:", special_status)
print("New type of 'special_status':", type(special_status))
print("-" * 20)
```