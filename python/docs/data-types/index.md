---
layout: page
title: Python Data Types - Comprehensive Guide with Examples and Exercises
description: Master Python data types with this comprehensive guide. Learn about numeric, string, boolean, and collection data types with examples, exercises, and tasks. Perfect for beginners and professionals to enhance their Python programming skills.
keywords: Python data types, Python numeric types, Python string type, Python boolean type, Python collection types, Python data type examples, Python data type exercises, Python programming for beginners, learn Python data types, Python coding tasks
toc: toc/python.html
---

## Table of the Contents:

1. [Basic Data Types](basic-data-types.md)
   - [Numeric Types (int, float, complex)](#1-numeric-types-int-float-complex)
   - [Text Type (str)](#2-text-type-str)
   - [Boolean Type (bool)](#3-boolean-type-bool)
2. [Type Casting](type-casting.md)
3. [Immutable vs. Mutable](immutable-mutable.md#immutable-vs-mutable)
   - [Common Mutable Data Types](immutable-mutable.md#common-immutable-data-types)  
   - [Common Immutable Data Types](immutable-mutable.md#common-mutable-data-types) 
4. [Why Data Types Matter in Python](why-use-data-types.md)
5. [Type Hints](type-hints.md)


## Key Terms

## ..

## Fix the error

**Incorrect Input Conversion** [Python Quiz #64]

```python
age = input("Enter your age: ")  
result = age * 2
```


## True/False (Mark T for True and F for False)

1. In Python, the type of a variable is determined at runtime.

**Answer Key (True/False):**

1. True

## Multiple Choice (Select the best answer)

**What is the output of the following code? [Python Quiz #22]**

```python
age = 25
print("I am " + str(age) + " years old.")
```

- A) I am 25 years old.
- B) I am "25" years old.
- C) Syntax error
- D) I am years old. (with quotes)

**Watch this video for the answer:**[https://youtube.com/shorts/DBC5-ZYoGXI?si=PXk-CPGymx2Q6X2p](https://youtube.com/shorts/DBC5-ZYoGXI?si=PXk-CPGymx2Q6X2p)


```python
age = 25
message = "You are " + str(age) + " years old."
message += " Welcome!"
print(message)
```

1. **Which function would you use to determine the type of a variable in Python?**
   - A) id()
   - B) type()
   - C) str()
   - D) isinstance()

2. **Which of the following is not a scalar data type in Python?**
   - A) bool
   - B) int
   - C) float
   - D) list
      
3. Which data type is used to represent decimal numbers in Python?
    - A) int
    - B) float
    - C) complex
    - D) str

4. Which of the following is an example of a boolean value in Python?
   - a. "True"
   - b. 1
   - c. 3.14
   - d. False

5. Which scalar data type is used to represent textual data in Python?
- a. str
- b. char
- c. text
- d. string
  
1. What is the default type of a numerical literal without a decimal point in Python?
- a. int
- b. float
- c. complex
- d. bool

1. **What is the result of the expression type("Hello, World!") in Python?**
    - A) <class 'str'>
    - B) <class 'bool'>
    - C) <class 'int'>
    - D) <class 'float'>

2.  What is the output of type(42)?
    - A) <class 'str'>
    - B) <class 'bool'>
    - C) <class 'int'>
    - D) <class 'float'>

3. What is the result of 3 + 4.5?
- a. 7
- b. 7.5
- c. Error
- d. None of the above

1.  How do you create a string in Python?
    - A) Using single quotes (')
    - B) Using double quotes (")
    - C) Both a and b
    - D) None of the above

2.  Which of the following is a valid boolean value in Python?
- a. True
- b. False
- c. 0
- d. All of the above

1.   What is the output of str(3.14)?
- a. 3.14
- b. '3.14'
- c. Error
- d. None of the above

1.  What is the result of the following expression? [Python Quiz #79]

```python
type(3 + 4.0)
```
    - A) <class 'str'>
    - B) <class 'bool'>
    - C) <class 'int'>
    - D) <class 'float'>

14. Which of the following is a correct way to declare a complex number in Python?
    - A) a = 3 + 4j
    - B) a = 3.4j
    - C) a = 3 + 4i
    - D) a = 3 + 4

15. Which function can be used to convert a float to an integer in Python?
    - A) float()
    - B) int()
    - C) str()
    - D) bool()

16. Which of the following statements is true regarding dynamic typing in Python?
    - A) Variables can only be assigned values of the same type.
    - B) The data type of a variable is determined at runtime based on the value it holds.
    - C) Variables must be declared with a specific type.
    - D) Once a variable is assigned a type, it cannot be changed.

17. In Python, what happens if you assign a new value of a different type to a variable?
    - A) Python will raise a type error.
    - B) Python will change the variable's type to match the new value.
    - C) Python will ignore the new value.
    - D) Python will convert the value to the original type.

18. What is the output of the following code? [Python Quiz #80]

```python
x = 10
x = "Hello"
print(type(x))
```
    - A) <class 'int'>
    - B) <class 'str'>
    - C) <class 'bool'>
    - D) <class 'float'>

19. What is the result of the following code?

```python
x = 5
x = 5.0
x = True
x = "Python"
print(x)
```
    - A) 5
    - B) 5.0
    - C) True
    - D) Python

20. What is the main advantage of dynamic typing in Python?
    - A) Faster execution time.
    - B) More flexibility in code.
    - C) Improved error detection at compile-time.
    - D) Reduced memory usage.

21. Which of the following best describes a dynamically typed language?
    - A) Type checking is performed during code compilation.
    - B) Type checking is deferred until program execution.
    - C) Type checking is not performed at all.
    - D) Types are always explicitly declared by the programmer.

22. In Python, which of the following is true about variable assignment?
    - A) The type of the variable is determined when the variable is first assigned a value.
    - B) The type of the variable is determined at compile-time.
    - C) Variables must be explicitly typed before assignment.
    - D) Variables cannot change type once assigned.

23. What is the output of the following code? [Python Quiz #81]

```python
x = "10"
x = int(x) + 2
print(x)
```
    - A) "102"
    - B) 102
    - C) 12
    - D) "12"

## Fill in the Blanks

**Answer Key (Fill in the Blanks):**

## Exercises

### Exercise 1: Variable Assignment and Basic Operations
1. Assign the value `5` to a variable named `x`.
2. Assign the value `10` to a variable named `y`.
3. Assign the sum of `x` and `y` to a variable named `sum_xy`.
4. Print the value of `sum_xy`.

**Solution:**
```python
x = 5
y = 10
sum_xy = x + y
print("Sum of x and y:", sum_xy)
```

### Exercise 2: Working with Different Data Types
1. Assign a floating-point number to a variable named `pi`.
2. Assign a string to a variable named `greeting`.
3. Assign a boolean value to a variable named `is_active`.
4. Print the types and values of `pi`, `greeting`, and `is_active`.

**Solution:**
```python
pi = 3.14
greeting = "Hello, World!"
is_active = True

print("Type of pi:", type(pi), "Value:", pi)
print("Type of greeting:", type(greeting), "Value:", greeting)
print("Type of is_active:", type(is_active), "Value:", is_active)
```

### Exercise 3: String Concatenation
1. Assign your first name to a variable named `first_name`.
2. Assign your last name to a variable named `last_name`.
3. Concatenate `first_name` and `last_name` with a space in between and assign the result to a variable named `full_name`.
4. Print the value of `full_name`.

**Solution:**
```python
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print("Full name:", full_name)
```

### Exercise 4: Boolean Operations
1. Assign the value `True` to a variable named `is_sunny`.
2. Assign the value `False` to a variable named `is_raining`.
3. Create a new variable named `can_go_outside` that is `True` if `is_sunny` is `True` and `is_raining` is `False`.
4. Print the value of `can_go_outside`.

**Solution:**
```python
is_sunny = True
is_raining = False
can_go_outside = is_sunny and not is_raining
print("Can go outside:", can_go_outside)
```

### Exercise 5: Type Conversion
1. Assign the string `"123"` to a variable named `num_str`.
2. Convert `num_str` to an integer and assign it to a variable named `num_int`.
3. Print the type and value of `num_int`.

**Solution:**
```python
num_str = "123"
num_int = int(num_str)
print("Type of num_int:", type(num_int), "Value:", num_int)
```

## Review Questions

**Basic Data Types**

1. What are the basic data types in Python?
   - **Answer:** Python's basic data types include:
     1. **Numbers:** Integers (`int`), floating-point numbers (`float`), and complex numbers (`complex`).
     2. **Text:** Strings (`str`) to represent sequences of characters.
     3. **Logical Values:** Booleans (`bool`) for True or False.

2. How do you create a string in Python? Give an example.
3. What is the difference between an integer and a float in Python?
4. How do you convert a string to an integer in Python?
5. How can you convert a string to an integer and an integer to a string in Python? Provide examples.
6. What function would you use to find the type of a variable in Python?
7.  What is the purpose of the type() function in Python?

**Boolean and None**

6. What are the Boolean values in Python?
7. What does the None type represent in Python?
   - **Answer:** In Python, the None type represents the absence of a value or a null value. It is a built-in constant that is used to denote a lack of value or a null reference.
   - ### Characteristics of `None`
     1. **Singleton**: `None` is a singleton in Python, meaning there is only one instance of `None` in a Python runtime. All occurrences of `None` point to the same object.
    ```python
    a = None
    b = None
    print(a is b)  # Output: True
    ```

     2. **Type**: The type of `None` is `NoneType`.
    ```python
    print(type(None))  # Output: <class 'NoneType'>
    ```
     3. **Boolean Context**: `None` is treated as `False` in a boolean context.
    ```python
    if not None:
        print("None is considered False")  # Output: None is considered False
    ```
    - ### Checking for `None`
    - To check if a variable is `None`, use the `is` operator, as it checks for identity.
        ```python
        variable = None
        if variable is None:
            print("Variable is None")  # Output: Variable is None
        ```
8. How do you check if a variable is None?

   - **Answer:** To check if a variable is None in Python, you should use the is operator. The is operator checks for identity, meaning it checks whether two references point to the same object. Since None is a singleton in Python (there is only one instance of None in a Python runtime), using is is the correct and most efficient way to check for None.

```python
variable = None

if variable is None:
    print("Variable is None")
```

**Type Casting**

1.  How do you convert an integer to a string in Python?
2.  What is the result of int('123.45')?
3.  What does the str() function do?
4.  How do you safely convert a string to a float, considering the possibility of invalid input?

## References and Bibliography

[1]R. Python, “Dynamic vs Static – Real Python,” realpython.com. https://realpython.com/lessons/dynamic-vs-static/
[2]Python Software Foundation, “Built-in Types — Python 3.12.1 documentation,” Python.org, 2019. https://docs.python.org/3/library/stdtypes.html
[3]“PEP 526 – Syntax for Variable Annotations | peps.python.org,” peps.python.org. https://peps.python.org/pep-0526/
‌
‌
‌