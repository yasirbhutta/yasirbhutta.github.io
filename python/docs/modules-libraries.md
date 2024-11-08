# Modules and Libraries in Python

Let's practice using some of the concepts we've covered, including **modules**, **functions**, and **working with external libraries**.

Let’s now explore **modules and libraries** in Python, which are essential for organizing and reusing code, as well as leveraging pre-built functionality.

### 1. **Importing Modules**
   - Python comes with a standard library of modules, but you can also install third-party libraries using tools like `pip`.
   - You can import a module or specific functions from it using the `import` keyword.

   - **Importing a whole module**:
     ```python
     import math
     print(math.sqrt(16))  # Output: 4.0
     ```

   - **Importing specific functions**:
     ```python
     from math import sqrt
     print(sqrt(16))  # Output: 4.0
     ```

   - **Alias for modules**:
     Sometimes you might want to give a module a shorter name using `as`:
     ```python
     import numpy as np
     print(np.array([1, 2, 3]))
     ```

### 2. **Standard Library**
   Python comes with many useful built-in modules. Some commonly used ones include:
   - `math`: Provides mathematical functions like `sqrt()`, `pow()`, and constants like `pi`.
   - `datetime`: Useful for handling date and time operations.
   - `random`: For generating random numbers.
   - `os`: For interacting with the operating system (e.g., file manipulation).

   Example with `random`:
   ```python
   import random
   print(random.randint(1, 10))  # Random integer between 1 and 10
   ```

### 3. **Installing External Libraries**
   To install third-party libraries, you can use `pip`. For example, to install the popular `requests` library:
   ```bash
   pip install requests
   ```

   Once installed, you can import it and use it in your code:
   ```python
   import requests
   response = requests.get('https://www.example.com')
   print(response.text)
   ```

### 4. **Creating Your Own Modules**
   You can organize your code into modules by saving your functions or classes in separate Python files. For example, if you have a file `mymodule.py`:
   ```python
   # mymodule.py
   def greet(name):
       return f"Hello, {name}!"
   ```

   You can import and use the module like this:
   ```python
   import mymodule
   print(mymodule.greet("Alice"))
   ```

### Exercise 1: Using the `math` module
1. **Objective**: Use the `math` module to calculate the area of a circle. The formula is `Area = π * r²`, where `r` is the radius.
2. **Steps**:
   - Import the `math` module.
   - Define a function `calculate_area(radius)` that returns the area of the circle.
   - Use the function with different radius values and print the result.

### Exercise 2: Working with the `random` module
1. **Objective**: Write a program that simulates rolling a six-sided die 5 times and prints the results.
2. **Steps**:
   - Import the `random` module.
   - Use the `randint()` function to simulate the die rolls.
   - Print the results of each roll.

### Exercise 3: Creating your own module
1. **Objective**: Create a module that contains a function to check if a number is prime.
2. **Steps**:
   - Create a Python file named `mymodule.py`.
   - In this file, define a function `is_prime(n)` that returns `True` if the number is prime and `False` otherwise.
   - In your main script, import the module and test the `is_prime()` function with a few numbers.
