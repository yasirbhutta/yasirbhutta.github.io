---
layout: page
title: "*args and **kwargs in Python" 
description: Learn Python variables with this beginner-friendly guide. Understand variable naming rules, assignments, and operations with examples and exercises. Perfect for students and professionals starting their Python journey.  
keywords: Python variables, Python variable examples, Python variable exercises, Python variable naming rules, Python variable assignment, Python beginner tutorials, Python programming basics, learn Python variables, Python coding exercises
toc: toc/python.html
---

## **`*args` and `**kwargs`**

## Arbitrary Positional Arguments (`*args`)
   
These allow a function to take any number of positional arguments. Inside the function, `*args` collects all the positional arguments as a tuple.

- [Video: How to Use *args in Python Functions](https://www.youtube.com/watch?v=7ejTzBybkw4&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=5)
- [Video: Understanding *args in Functions - How to Add Any Number of Arguments with *args](https://www.youtube.com/watch?v=0noa3Sgxmg8&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=6)

**Example:**
```python
def greet(*names):
    for name in names:
        print(f"Hello, {name}!")

greet("Ali", "Hamza", "Ahmad")
```
**Output:**
```
Hello, Ali!
Hello, Hamza!
Hello, Ahmad!
```

In this example, the `greet` function can take any number of names. The `*names` collects them into a tuple (`names`), which can be iterated over.

1. Arbitrary Keyword Arguments (`**kwargs`)

These allow a function to accept any number of keyword arguments (arguments passed as key-value pairs). Inside the function, `**kwargs` collects these as a dictionary.

- [Video: How to use **kwargs in Python](https://www.youtube.com/watch?v=_NMaZ9EO0zI&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=2)

**Example:**
```python
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Ali", age=25, city="Multan")
```
**Output:**
```
name: Ali
age: 25
city: Multan
```

In this case, the function accepts any number of keyword arguments and collects them into a dictionary (`info`), which you can then work with inside the function.

##### Combined Use

You can also use both `*args` and `**kwargs` in the same function to handle a combination of positional and keyword arguments.

**Example:**
```python
def display_data(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

display_data(1, 2, 3, name="Ali", age=25)
```
**Output:**
```
Positional arguments: (1, 2, 3)
Keyword arguments: {'name': 'Ali', 'age': 25}
```

**Key Points:**
- `*args` collects all positional arguments into a tuple.
- `**kwargs` collects all keyword arguments into a dictionary.
- You can use both `*args` and `**kwargs` together to handle any type of arguments passed to a function.
