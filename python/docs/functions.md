# Python for Beginners: Functions in Python

Connect with me: [Youtube](https://www.youtube.com/yasirbhutta) \| [LinkedIn](https://www.linkedin.com/in/yasirbhutta/) \| [WhatsApp Channel](https://whatsapp.com/channel/0029VaC3BC160eBZZSs3CW0c) \| [Web](https://yasirbhutta.github.io/) \| [Facebook](https://www.facebook.com/yasirbhutta786) \| [Twitter](https://twitter.com/yasirbhutta)

- [Download PDF](https://yasirbhutta.github.io/python/docs/functions.pdf)
- To access the updated lecture notes, please click on the following link:
[https://yasirbhutta.github.io/python/docs/functions.html](https://yasirbhutta.github.io/python/docs/functions.html)

## What is a Function?

In Python, a function is a block of code designed to perform a specific task. It's reusable, which means you can call it multiple times in your program. This helps to organize your code, make it more readable, and avoid repetition.

## How to Write a Function

To define a function, you use the `def` keyword followed by the function name, parentheses for parameters, and a colon. The code block that defines the function is indented.

```python
def function_name(parameters):
  # Function body
  # Code to be executed
```

**Example:**

```python
def greet(name):
  print("Hello,", name + "!")

# Calling the function
greet("Ahmad")  # Output: Hello, Ahmad!
```

**Explanation:**

- `def greet(name):` defines a function named `greet` that takes one parameter, `name`.
- `print("Hello,", name + "!")` is the function body, which prints a greeting message using the provided name.
- `greet("Ahmad")` calls the function with the argument "Ahmad".

**Key Points:**

- **Parameters:** These are variables passed to the function when it's called.
- **Return Value:** A function can optionally return a value using the `return` statement.
- **Docstrings:** It's good practice to include a docstring (a string that explains the function's purpose) after the function definition.

**Function with a Return Value:**

```python
def add(x, y):
  return x + y

result = add(3, 5)
print(result)  # Output: 8
```


- [Video: How to Write a Python Function to Find the Length of a Word](https://www.youtube.com/watch?v=wKuKX8-at5E&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=22)
- [Video: Learn How to Use Default Parameters in Function Definition](https://www.youtube.com/watch?v=2z_K1YChX1A&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=21)
- [Video: Understanding *args in Functions - How to Add Any Number of Arguments with *args](https://www.youtube.com/watch?v=0noa3Sgxmg8&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=6)
- [Video: How to Use *args in Python Functions](https://www.youtube.com/watch?v=7ejTzBybkw4&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=5)
- [Video: How to use **kwargs in Python](https://www.youtube.com/watch?v=_NMaZ9EO0zI&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=2)

### Parameters and Arguments

Parameters are defined by the names that appear in a function definition, whereas arguments are the values actually passed to a function when calling it. Parameters define what kind of arguments a function can accept. 

### Parameters
* **Definition:** Variables declared in a function's definition.
* **Purpose:** Act as placeholders for values that will be passed to the function when it's called.
* **Location:** Inside the function's parentheses.

### Arguments
* **Definition:** Actual values passed to a function when it's called.
* **Purpose:** Provide data for the function to work with.
* **Location:** Inside the function call parentheses.

See also the `FAQ` question of `Python Documentation` on [the difference between arguments and parameters](https://docs.python.org/3/faq/programming.html#faq-argument-vs-parameter).

**Example:**

```python
def greet(name):  # 'name' is a parameter
    print("Hello,", name + "!")

greet("Alice")  # "Alice" is an argument
```

In this example:
* `name` is a parameter in the function `greet`.
* `"Alice"` is an argument passed to the function when it's called.

**To summarize:**
* Parameters are defined *before* the function is called.
* Arguments are provided *when* the function is called.

**Think of it like this:**
* A parameter is like an empty box that expects a value.
* An argument is the value you put into the box.

## More on Defining Functions
### Default Argument Values

**Example:** Function with Default Parameters:**

```python
def greet(name="World"):
  print("Hello,", name + "!")

greet()  # Output: Hello, World!
greet("Alice")  # Output: Hello, Alice!
```
### Keyword Arguments
### Special parameters
#### Positional-or-Keyword Arguments
#### Positional-Only Parameters
#### Keyword-Only Arguments
#### Arbitrary Argument Lists

In Python, Arbitrary Argument Lists allow a function to accept a varying number of arguments. This is useful when you don't know beforehand how many arguments might be passed to the function. There are two types of arbitrary arguments:

1. **Arbitrary Positional Arguments (`*args`)**
2. **Arbitrary Keyword Arguments (`**kwargs`)**

1. Arbitrary Positional Arguments (`*args`)
   
These allow a function to take any number of positional arguments. Inside the function, `*args` collects all the positional arguments as a tuple.

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

[video: How to Use *args in Python Functions](https://youtu.be/7ejTzBybkw4)

2. Arbitrary Keyword Arguments (`**kwargs`)

These allow a function to accept any number of keyword arguments (arguments passed as key-value pairs). Inside the function, `**kwargs` collects these as a dictionary.

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

[video: How to use  **kwargs in Python](https://youtu.be/_NMaZ9EO0zI)

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
- 

### Unpacking Argument Lists
### Lambda Expressions
### Documentation Strings
### Function Annotations

**See also:**

- [Python Quiz - Functions](https://forms.gle/ZxyA5p98T9f8CZsA6)

## True/False (Mark T for True and F for False)

## Multiple Choice (Select the best answer)

1. What is the output of the following code?

```Python
def myfunction(val):
	return val % 4 == 0
print(myfunction (13) or myfunction (8))
```

  - A) 0
  - B) 13
  - C) False
  - D) True
  - E) 3.5

   - **Watch the Video Tutorial for the Answer:** [https://youtu.be/laKpsLlq60I](https://youtu.be/laKpsLlq60I)

2. **What is the output of the following code?** [Python Quiz #2]

```python
def foo(x):
  if x == 1:
    return 1
  else:
    return x * foo(x - 1)

print(foo(5))
```
- A) 5
- B) 15
- C) 120
- D) None
  
**Watch this video for answer:** [https://www.youtube.com/shorts/k50czTu7vao](https://www.youtube.com/shorts/k50czTu7vao) 

3. **What is the output of the following code?** [Python Quiz #30]
```python
def calculate_sum(n):
    if n == 0:
        return 0
    else:
        return n + calculate_sum(n-1)

print(calculate_sum(4))
```

  - A) 4
  - B) 6
  - C) 10
  - D) 15

**Watch the video for the answer:** [https://youtube.com/shorts/LQEfGgJYlT4?si=MDvSvVHiBc6hCJ0W](https://youtube.com/shorts/LQEfGgJYlT4?si=MDvSvVHiBc6hCJ0W)

# Youtube@yasirbhutta
4. **What is the output of the following expression?** [Python Quiz #13]
```python
def add(a,b,*parm):
    total = 0
    print(a+b)
    for n in parm:
        total += n
    return total

print(add(1, 2))
```

  - A) 3 0
  - B) 3
  - C) 0
  - D) Error

**Watch this video for answer:** [https://youtube.com/shorts/k4KVCxU5oMg](https://youtube.com/shorts/k4KVCxU5oMg)

5. **What is the output of the following  code?** [Python Quiz #14]

```python
def add(*args):
     print(type(args))

add(1, 2,8,9)
```

  - A) set
  - B) tuple
  - C) list
  - D) None

**Watch this video for answer:** [https://youtube.com/shorts/VQT4Cllpf9M](https://youtube.com/shorts/VQT4Cllpf9M)

6. **What is the output of the following  code?**

```python
def display_data(**kwargs):
    print(type(kwargs))

display_data(name="Ali", age=25)
```

  - A) <class 'set'>
  - B) <class 'tuple'>
  - C) <class 'list'>
  - D) <class 'dict'>
  
7. **What is the main purpose of a function in Python?**  

  - A) To group a set of related code into a single unit
  - B) To create a new type of data
  - C) To write a program in a single line
  - D) To change the value of global variables

8. **What is the purpose of the return statement in a function in Python?**

  - A) To print the output of the function
  - B) To exit the function and return a value
  - C) To execute the function without returning anything
  - D) To stop the function and start a new one

9. **What is the correct way to define a function in Python?**

  - A) function my_function():
  - B) def my_function():
  - C) define my_function():
  - D) my_function() {


How can you pass parameters to a function in Python?
a) By listing the parameters after the function name, separated by commas
b) By enclosing the parameters in square brackets
c) By using the global keyword
d) By using the input() function

Answer: a) By listing the parameters after the function name, separated by commas


## Exercises

1. Write a Python program that takes two numbers as input and prints their sum.
  - [**Watch the Solution Now ✨**](https://www.youtube.com/watch?v=CQHXsGnUns0&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=24)
2. **Exercise: Find the Maximum Value**

**Task:** Write a Python program that finds and prints the maximum value from a given list of numbers.

**Sample Input:**
```python
numbers = [3, 7, 1, 9, 5]
```

**Sample Output:**
```
9
```

**Instruction:** please don't use the `max()` function to find the maximum value in a list.

- [**Watch the Solution Now ✨**](https://www.youtube.com/watch?v=AcC4ykPRYhc&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=23)
   
3. Write a function `sum3(num1,num3,num3)` that takes three numbers as input and returns the sum.
4. Write a function `SumNum(num1)` that takes a number as input and returns the sum of numbers from 1 to that number (num1).
5. Write a function `sumSquares(x)` that takes a vector of numbers as input and returns the sum of their squares.
6. Write a function `isEven(x)` that takes a number as input and returns true if it is even, and false otherwise.
7. Write a program with three functions:
  
  1. **`isEven(n)`:** This function takes an integer `n` as input and returns `True` if `n` is even and `False` otherwise. You can use the modulo operator (`%`) to check for evenness.
  2. **`printTable(n)`:** This function takes an integer `n` as input and prints its multiplication table. The table should show the product of `n` with each number from 1 to 10, formatted like `n * i = n * i`, where `i` is the current number in the loop.
  3. **`main`:** The main program should:
     - Prompt the user to enter an integer.
     - Use the `isEven(n)` function to check if the entered number is even.
     - If the number is even, call the `printTable(n)` function to print its multiplication table.
     - If the number is odd, print a message indicating the number is odd and not eligible for printing a table.

**Example output:**

```python
Enter an integer: 4
4 is even! Here's its multiplication table:
4 * 1 = 4
4 * 2 = 8
4 * 3 = 12
...
4 * 10 = 40
```

9. Write a function `avgPositive(data)` that takes a list of numbers as input and returns the average of all positive numbers in the list.

## Review Questions

## References and Bibliography

**Which of the following will cause a syntax error due to incorrect indentation in Python?**

A)
```python
print("Hello World!")
```

B)
```python
def my_function():
print("Hello World!")
```

C)
```python
if x == 10:
    print("x is 10")
```

D)
```python
x = 10
```

*Answer:* B
