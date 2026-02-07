---
layout: page
title: "Python Variables Explained: Basics, Naming Rules & Practical Examples"
description: Learn Python variables with this beginner-friendly guide. Understand variable basics, naming rules (including valid vs invalid names), reserved keywords, and practice with hands-on coding tasks.
keywords: Python variables, variable naming rules Python, valid variable names Python, Python reserved keywords, Python variable assignment, Python programming basics, learn Python variables, Python variable examples, Python variable exercises, Python type() and id(), Python data storage, Python variable types, Python coding for beginners, Python variable declaration, Python variable best practices
toc: toc/python.html
course: python
topic: variables
prev: /python/docs/variables/
next: /python/docs/variables/dynamic-typing.html
breadcrumb: 
- title: Variables
url: /python/docs/variables/
---

## **📖 Table of Contents**  

1. [What Are Variables?](#1-what-are-variables)  
   - [Variable Basics](#variable-basics)  
   - [Assignment Operator (`=`)](#assignment-operator-)  
2. [Variable Naming Rules](#2-variable-naming-rules)  
   - [Valid vs. Invalid Names](#valid-vs-invalid-names)  
   - [Reserved Keywords](#reserved-keywords)  
3. [Practical Tasks](#3-practical-tasks)  
   - [Task 1: Rectangle Calculator](#task-1-rectangle-calculator)  
   - [Task 2: Exploring `type()` and `id()`](#task-2-exploring-type-and-id) 

## **1. What Are Variables?**

- A variable is a named storage location in a computer's memory that is used to hold data or values. It allows programmers to store and manipulate data within a program.

**Purpose:** Variables provide a way to store and manage data that can be used and manipulated throughout a program. They make programs more flexible and allow for dynamic data storage.

**Assignment statement:** in Python is used to assign a value to a variable. Its primary purpose is to store and manage data within a program.

**Imagine variables as labeled boxes:**

- You have boxes for storing different things (numbers, words, etc.).
- Each box has a name (label) to identify what's inside.
- You can put things in, take them out, and change what's inside.
- 

**Example:**  
```python
name = "Alice"      # Stores text  
age = 25            # Stores a number  
is_student = True   # Stores True/False  
```

### **Assignment Operator (`=`)**  
Use `=` to assign values. No need to declare types!  

**Key Rules:**  
- **Reassignment:** Change a variable’s value anytime.  
  ```python
  x = 10  
  x = "hello"  # Now x is a string!  
  ```  
- **Multiple Assignment:**  
  ```python
  a, b = 1, 2          # a=1, b=2  
  x = y = z = 0        # All set to 0  
  ```  
- **Swapping:**  
  ```python
  x, y = 10, 20  
  x, y = y, x  # Swap! (Now x=20, y=10)  
  ```  

**Common Mistakes:**  
- Using spaces: `user name = "Bob"` ❌  
- Starting with numbers: `2nd_place = "Silver"` ❌  

---

## **2. Variable Naming Rules**

In Python, valid variable names must adhere to the following rules:

- **Begin with a letter or an underscore:** The first character of a variable name must be a letter (a-z, A-Z) or an underscore (_).
- **Followed by letters, digits, or underscores:** After the first character, the variable name can contain letters, digits (0-9), or underscores.
- **Case-sensitive:** Variable names are case-sensitive. For example, myVariable and myvariable would be considered different variables.
- **No reserved keywords:** Variable names cannot be Python reserved keywords (e.g., if, for, while, class, etc.).
  
---

### **Valid vs. Invalid Variable Names in Python**  

#### **✅ Valid Variable Names**  
- Can contain:  
  - Letters (`a-z`, `A-Z`)  
  - Digits (`0-9`) *but not as the first character*  
  - Underscores (`_`)  
- Are **case-sensitive** (`age`, `Age`, and `AGE` are different).  
- Should use `snake_case` (recommended Python style).  

**Examples:**  
```python
name = "Alice"  
user_age = 25  
_total = 100  
item2 = "book"  
```  

---

#### **❌ Invalid Variable Names**  
- Start with a digit.  
- Contain spaces or special symbols (`!`, `@`, `#`, etc.).  
- Match Python's **reserved keywords** (see below).  

**Examples:**  
```python
2name = "Bob"      # Error: Starts with digit  
first-name = "John" # Error: Hyphen not allowed  
user age = 30      # Error: Contains space  
```  

---

### **Reserved Keywords**  
Python has 35 reserved keywords (e.g., `if`, `for`, `while`).  

**Check All Keywords:**  
```python
import keyword  
print(keyword.kwlist)  
```

**⚠️ Never use these as variable names!**  

### **Valid vs. Invalid Names**  
| Valid ✅          | Invalid ❌         |  
|-------------------|--------------------|  
| `user_name`       | `user-name` (hyphen)|  
| `_total`          | `2nd_place` (starts with digit)|  
| `price2`          | `class` (reserved keyword)|  

---


**💡 Tip:**  
If you accidentally use a keyword, Python will raise a `SyntaxError`:  
```python
class = "Biology"  # Error: 'class' is a keyword  
```

---

### **📝 Interactive Task**  
**Which of these are valid?**  
```python
1. user_name  
2. 3rd_place  
3. return  
4. _price  
5. my-var  
```  
<details>  
<summary>📚 <i>Answer</i></summary>  
✅ Valid: 1, 4  
❌ Invalid: 2 (starts with digit), 3 (keyword), 5 (hyphen)  
</details>  

---

### **🌟 Best Practices**  
✔ Use descriptive names (e.g., `student_count` vs. `n`).  
✔ Stick to `snake_case` (e.g., `total_score`).  
✔ Avoid single letters (except in loops like `for i in range(5)`).  

---

## **3. Practical Tasks**  
### **Task 1: Rectangle Calculator**  
**Given:**  
```python
length = 10  
width = 5  
```  
**Your Task:** Calculate and print:  
1. **Area** (`length * width`)  
2. **Perimeter** (`2 * (length + width)`)  

<details>  
<summary>💡 Solution</summary>  

```python  
area = length * width  
perimeter = 2 * (length + width)  
print("Area:", area)  
print("Perimeter:", perimeter)  
```  
</details>  

---

### **Task 2: Exploring `type()` and `id()`**  
**Code:**  
```python
x = 10  
print(type(x))  # Output: <class 'int'>  
print(id(x))    # Output: Memory address  
```  

**Questions:**  
1. What happens if you set `x = "hello"` and check `type(x)`?  
2. Assign `y = 10`. Does `id(y)` match `id(x)`? Why?  

**💡 Hint:** Python reuses memory for small integers!  

--- 

**🔗 Additional Resources:**  
- [Python Variables Video Tutorial](https://youtu.be/ur8rkDPzuSU)  
- [Common Mistakes to Avoid](https://youtube.com/shorts/lQy1Le8fnRs)  

---
