---
layout: page
title: Usage
description: In Python, type hints allow you to specify the expected data types of variables, function parameters, and return values. They make the code more reada...
keywords: type, str, hints, return, alice
---
## Type Hints

In Python, **type hints** allow you to specify the expected data types of variables, function parameters, and return values. They make the code more readable and help developers understand what kind of values are expected.

Here’s how you can use type hints in Python:

### 1. **Type Hinting for Variables**
You can add type hints to variables by using a colon `:` after the variable name, followed by the type:

#### Example: Type Hinting for Variables

```python
age: int = 25
name: str = "Alice"
height: float = 5.7
is_student: bool = True
```

### 2. Type Hinting in Functions
For functions, type hints are added after the parameter names and before the return type with `->`.

#### Example: Type Hinting in Functions

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Usage
print(greet("Alice"))  # Output: Hello, Alice!
```

This code specifies that the `name` parameter should be a `str`, and the function should return a `str`.

### 3. **Type Hints for Collections** 

For more complex types like lists, dictionaries, sets, and tuples.

#### Lists
To specify that a list contains elements of a certain type, use `list`.

```python

# A list of integers
numbers: list[int] = [1, 2, 3, 4, 5]

# A list of strings
names: list[str] = ["Alice", "Bob", "Charlie"]
```

#### Dictionaries
For dictionaries, you can specify the types of both keys and values using `dict`.

##### Example:

```python
# A dictionary with string keys and integer values
age_map: dict[str, int] = {"Alice": 30, "Bob": 25, "Charlie": 35}
```

#### Sets
To specify the type of elements in a set, use `Set`.

##### Example:

```python
# A set of strings
unique_names: set[str] = {"Alice", "Bob", "Charlie"}
```

#### Functions with Collection Type Hints
You can also use type hints in function definitions to specify the types of parameters and return values.

##### Example:

```python
# Function that processes a list of integers and returns a dictionary
def process_data(numbers: list[int]) -> dict[str, int]:
    result = {
        'sum': sum(numbers),
        'count': len(numbers)
    }
    return result

data = [1, 2, 3, 4, 5]
processed_data = process_data(data)
print(processed_data)  # Output: {'sum': 15, 'count': 5}
```

Using type hints doesn’t enforce types at runtime but can improve code readability and help detect type-related issues with tools like **mypy**.
