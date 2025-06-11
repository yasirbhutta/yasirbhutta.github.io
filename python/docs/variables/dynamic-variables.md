## 3.6 Understanding Dynamic Variables in Python with Examples

[video: Is Python a Dynamic Language?](https://youtu.be/4qweH-RCfCQ)

- Python is a dynamically typed language. This means that the Python interpreter does type checking only as code runs, and the type of a variable is allowed to change over its lifetime.[1]
- In Python, variables are dynamic, meaning they can change types during the execution of a program. This flexibility allows you to assign a value of any type to a variable and later reassign it to a value of a different type without any issues. This dynamic nature of variables is due to Python being a dynamically typed language.

**Example #:** Dynamic Variables in Python

```python
# Initial assignment of an integer value
x = 10
print(x)  # Output: 10
print(type(x))  # Output: <class 'int'>

# Reassigning a string value to the same variable
x = "Hello, World!"
print(x)  # Output: Hello, World!
print(type(x))  # Output: <class 'str'>

# Reassigning a list to the same variable
x = [1, 2, 3]
print(x)  # Output: [1, 2, 3]
print(type(x))  # Output: <class 'list'>

# Reassigning a float value to the same variable
x = 3.14
print(x)  # Output: 3.14
print(type(x))  # Output: <class 'float'>
```

In this example:

1. `x` is initially assigned an integer value of `10`.
2. `x` is then reassigned a string value `"Hello, World!"`.
3. `x` is later reassigned a list `[1, 2, 3]`.
4. Finally, `x` is reassigned a float value `3.14`.

Each time, the type of `x` changes dynamically to match the type of the value assigned to it. This flexibility is one of the powerful features of Python, allowing for more concise and adaptable code.
