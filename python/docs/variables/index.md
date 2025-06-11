---
layout: page
title: "Python Variables Explained: Basics, Naming Rules & Practical Examples" 
description: Learn Python variables with this beginner-friendly guide. Understand variable basics, naming rules (including valid vs invalid names), reserved keywords, and practice with hands-on coding tasks.
keywords: Python variables, variable naming rules Python, valid variable names Python, Python reserved keywords, Python variable assignment, Python programming basics, learn Python variables, Python variable examples, Python variable exercises, Python type() and id(), Python data storage, Python variable types, Python coding for beginners, Python variable declaration, Python variable best practices
toc: toc/python.html
topic: variables
breadcrumb:
  - title: Home
    url: /
  - title: Python
    url: /python/
  - title: Basics
    url: /python/docs/basics/
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
4. [Dynamic Variables](dynamic-variables.md)
5. [None Constant](none-constant.md)


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

# Using an undefined variable 

```python
name = "Ahmad"
print(f"Hello, {lastname}")  # lastname not defined
```

## True/False (Mark T for True and F for False)

1. Variable names in Python are case-sensitive.
2. In Python, variables must be declared with a specific data type before they can be used.
3. The statement x = 5 both creates the variable x and assigns it the value 5.

**Answer Key (True/False):**

1. True
2. False
3. True

## Multiple Choice (Select the best answer)

1. **What is a variable in Python?**
   - A) A reserved word in Python
   - B) A placeholder for storing data values
   - C) A function that prints data
   - D) A built-in library in Python

2. **Which statement best describes a variable in Python?**
   - A) A variable can hold multiple values at once.
   - B) A variable must be declared with a data type.
   - C) A variable is a name that refers to a value.
   - D) A variable is used only in loops.
  
3. **What is the output of the following code?**

   ```python
   x = 10
   print(x)
   ```
   - A) `10`
   - B) `x`
   - C) `Error`
   - D) `None`

4. **Which of the following is not true about variables in Python?**
   - A) Variables can be reassigned to different data types.
   - B) Variables must start with a letter or an underscore.
   - C) Variables are case-sensitive.
   - D) Variables must be declared before use.

5. **What will be the output of the following code?** [Python Quiz #76]

   ```python
   x = 5
   y = x
   x = 7
   print(y)
   ```
      - A) `7`
      - B) `5`
      - C) `0`
      - D) `None`

6. **Why is it important to use meaningful variable names?**
   - A) It is required by the Python interpreter.
   - B) It helps make the code more readable and maintainable.
   - C) It increases the execution speed of the program.
   - D) It is necessary for the code to run without errors.

7. **What will be the output of the following code?** [Python Quiz #77]

   ```python
   a = 1
   b = a
   a = a + 1
   print(a, b)
   ```
      - A) `1 1`
      - B) `2 1`
      - C) `1 2`
      - D) `2 2`

8. **Which of the following is a valid variable name in Python?**
   - A) `2ndValue`
   - B) `value#2`
   - C) `_value2`
   - D) `value-2`

9.  **Which of the following is a correct way to declare a variable in Python?**
   - A) `int x = 5`
   - B) `x = 5`
   - C) `declare x = 5`
   - D) `var x = 5`
   
10. **What is the output of the following code?** [Python Quiz 78]
   ```python
   x = 5
   y = "Hello"
   print(x + y)
   ```
      - A) `5Hello`
      - B) `Hello5`
      - C) `TypeError`
      - D) `Hello 5`
   
11.  **Which of the following is not a valid variable name in Python?**
   - A) `my_var`
   - B) `_var`
   - C) `2var`
   - D) `var2`

12. **Which of the following statements is true about variable assignment in Python?**
   - A) Variables must be declared before they are assigned a value.
   - B) Variables are created when they are first assigned a value.
   - C) Variable names must begin with a number.
   - D) Python variables must be declared with a type.
   

# 38 What is the purpose of declaring a variable in Python?
a) To reserve memory space for the variable
b) To give the variable a name
c) To initialize the variable with a value
d) All of the above
Answer: d


   
**Answer key (Mutiple Choice):**

1. B) A placeholder for storing data values
2. C) A variable is a name that refers to a value.
3. A) `10`
4. D) Variables must be declared before use.
5. B) `5`
6. B) It helps make the code more readable and maintainable.
7. B) `2 1`
8. C) `_value2`
9. B) `x = 5`
10. C) `TypeError`
    - **Explanation:** In Python, the + operator is used for both arithmetic addition and string concatenation. However, it cannot be used to add an integer and a string directly. The code provided attempts to add an integer (x = 5) to a string (y = "Hello"), which is not a valid operation and will result in a TypeError.
11. C) `2var`
    - **Explanation:** In Python, variable names must start with a letter or an underscore and cannot start with a number. Thus, my_var, _var, and var2 are valid, but 2var is not.
12. B) Variables are created when they are first assigned a value.
13. A) `5`   

## Fill in the Blanks

1. Variable names in Python must start with a letter or an __________.
2. Variables in Python are __________, meaning they can change type when assigned a new value.
3. The assignment operator in Python is the __________ symbol.

**Answer Key (Fill in the Blanks):**

1.  underscore (_)
2.  dynamic
3.  equals (=)
   
## Exercises

### Exercise 1: Basic Variable Assignment

1. Create a variable called `name` and assign your name to it.
2. Create a variable called `age` and assign your age to it.
3. Create a variable called `city` and assign the city you live in to it.
4. Print all three variables.

### Exercise 2: Variable Reassignment

1. Create a variable called `favorite_color` and assign your favorite color to it.
2. Print the value of `favorite_color`.
3. Reassign a new color to `favorite_color`.
4. Print the new value of `favorite_color`.

### Exercise 3: Variable Operations

1. Create two variables called `a` and `b` and assign them the values 5 and 10, respectively.
2. Create a new variable called `sum` and assign it the value of `a` plus `b`.
3. Create a new variable called `difference` and assign it the value of `a` minus `b`.
4. Create a new variable called `product` and assign it the value of `a` times `b`.
5. Print the values of `sum`, `difference`, and `product`.

### Exercise 4: String Concatenation

1. Create a variable called `first_name` and assign your first name to it.
2. Create a variable called `last_name` and assign your last name to it.
3. Create a new variable called `full_name` and assign it the value of `first_name` concatenated with `last_name` (with a space in between).
4. Print the value of `full_name`.

**Example Solution:**
```python
first_name = "Alice"
last_name = "Johnson"

full_name = first_name + " " + last_name
print(full_name)
```

### Exercise 5: Input and Variables

1. Use the `input()` function to get the user's name and store it in a variable called `user_name`.
2. Use the `input()` function to get the user's age and store it in a variable called `user_age`.
3. Print a message saying "Hello [user_name], you are [user_age] years old."

**Example Solution:**
```python
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")

print("Hello", user_name + ", you are", user_age, "years old.")
```
6. Calculate the Area of a Circle with Radius [Example Solution](https://www.youtube.com/watch?v=QoECA8v_2tQ)
7. How to Swap Variables Without a Third Variable in Python. [Example Solution](https://youtu.be/CVy3A48WXeE)
8.  How to assign multiple values to multiple variables. [Example Solution](https://youtu.be/ur8rkDPzuSU)

## Review Questions

**1. What is a variable in computer programming?**
**Answer:** A variable is a named storage location in a computer's memory that is used to hold data or values. It allows programmers to store and manipulate data within a program.

**2. What is the purpose of using variables in programming?**
**Answer:** Variables provide a way to store and manage data that can be used and manipulated throughout a program. They make programs more flexible and allow for dynamic data storage.

**3. What is the difference between declaring and initializing a variable?**
**Answer:** Declaring a variable involves specifying its name and data type, while initializing a variable means giving it an initial value. Initialization usually follows declaration but is not always required.

4. What is a variable in computer programming? Give examples of integer, string, float, and Boolean variables.

## References and Bibliography



