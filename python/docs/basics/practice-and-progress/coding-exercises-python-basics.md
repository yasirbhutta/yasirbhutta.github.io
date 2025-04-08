---
layout: default
title: Python Basics: Coding Exercises
description: "Learn Python basics with coding exercises focused on input, print statements, comments, f-strings, and indentation. Improve your coding skills by mastering essential Python concepts for clean, readable code and efficient programming practices."
---

# Python Basics: Coding Exercises


###Print Functions

1. **Basic Printing**
   - Write a Python program to print the following:
     ```
     Hello, World!
     ```
   
   **Solution:**
   ```python
   print("Hello, World!")
   ```

2. **Printing Variables**
   - Create two variables, `name` and `age`, and print them using the `print` function. Use the variables to print the following:
     ```
     My name is John and I am 25 years old.
     ```

   **Solution:**
   ```python
   name = "John"
   age = 25
   print("My name is", name, "and I am", age, "years old.")
   ```

3. **Formatted Strings**
   - Use an f-string to print the following using the variables `name` and `age`:
     ```
     My name is John and I am 25 years old.
     ```

   **Solution:**
   ```python
   name = "John"
   age = 25
   print(f"My name is {name} and I am {age} years old.")
   ```

### Indentation

4. **Correct Indentation**
   - The following code has incorrect indentation. Fix it so that it runs correctly:
     ```python
     def greet(name):
     print(f"Hello, {name}!")

     greet("Alice")
     ```

   **Solution:**
   ```python
   def greet(name):
       print(f"Hello, {name}!")

   greet("Alice")
   ```

5. **Conditional Indentation**
   - Write a Python program that checks if a number is positive, negative, or zero and prints the result. Ensure proper indentation is used.
   
   **Solution:**
   ```python
   number = int(input("Enter a number: "))

   if number > 0:
       print("The number is positive.")
   elif number < 0:
       print("The number is negative.")
   else:
       print("The number is zero.")
   ```

### Comments

6. **Single-Line Comments**
   - Add comments to the following code explaining each line:
     ```python
     name = "Alice"
     age = 30
     print(f"{name} is {age} years old.")
     ```

   **Solution:**
   ```python
   # Assign the string "Alice" to the variable 'name'
   name = "Alice"
   
   # Assign the integer 30 to the variable 'age'
   age = 30
   
   # Print the name and age using an f-string
   print(f"{name} is {age} years old.")
   ```

7. **Multi-Line Comments**
   - Use a multi-line comment to describe what the following code does:
     ```python
     def add(a, b):
         return a + b

     result = add(3, 5)
     print(result)
     ```

   **Solution:**
   ```python
   """
   This program defines a function 'add' that takes two arguments 'a' and 'b'
   and returns their sum. It then calls this function with the arguments 3
   and 5, stores the result in the variable 'result', and prints the result.
   """

   def add(a, b):
       return a + b

   result = add(3, 5)
   print(result)
   ```
   
