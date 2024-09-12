# Python Code Examples with Errors (Learning Purposes)

Connect with me: [Youtube](https://www.youtube.com/yasirbhutta) \| [LinkedIn](https://www.linkedin.com/in/yasirbhutta/) \| [WhatsApp Channel](https://whatsapp.com/channel/0029VaC3BC160eBZZSs3CW0c) \| [Web](https://yasirbhutta.github.io/) \| [Facebook](https://www.facebook.com/yasirbhutta786) \| [Twitter](https://twitter.com/yasirbhutta)

- [Python Playlist on Youtube](https://www.youtube.com/playlist?list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja)

Here are a few Python code examples with errors to help you understand common mistakes and debugging:

## Syntax Error

**1. Missing closing parenthesis**

```python
print("Hello World!"
```


**Syntax Errors (Incorrect Punctuation and Structure)**

```python
# Missing colon after if statement
if x > 5
    print("X is greater than 5")  # Indentation error here

# Incorrect use of parentheses in print statement
print "This is a string"  # Missing parentheses





## Indentation Error

**1. Indentation Error** [python quiz #58]

```python
for item in list:
    print(item)
      print("Loop finished")
```

**Error:** This code will result in an `IndentationError: expected indent` because the `print` statement inside the loop is not indented correctly.

**Fix:** Indent the line inside the loop by four spaces.

```python
for item in list:
    print(item)  # Correct indentation
print("Loop finished")
```

## Name Error

**1. Name Error: Using a Variable Before Definition** [Python Quiz #59]

```python
name = "Ahmad"
print(greeting + name)  # Using greeting before definition
greeting = "Hello, "
```

**Error:** This code will cause a `NameError: name 'greeting' is not defined` because the code tries to use `greeting` before it's assigned a value.

**Fix:** Define `greeting` before using it.

```python
greeting = "Hello, "
name = "Ahmad"
print(greeting + name)
```

**Name Error: Using a Variable Before Definition** [python quiz #60]

```python
age = 25
print(f"You are {age} years old")

name = "Alice"
greet(name)  # NameError: greet is not defined yet

def greet(name):
  print(f"Hello, {name}")
```
**Name Errors (Using Undefied Variables or Functions)**


Here are more "Fix the Error" questions:

---

### Question 6: Fix the NameError
**Task**: Correct the variable name error in the following code.

```python
message = "Python is fun"
print(messages)
```

**Error**: `NameError: name 'messages' is not defined` because the variable is named `message`, not `messages`.

**Corrected Code**:
```python
message = "Python is fun"
print(message)
```

---

### Question 7: Fix the TypeError with Print Function
**Task**: Fix the `TypeError` in the following code.

```python
print("The answer is: " + 42)
```

**Error**: `TypeError: can only concatenate str (not "int") to str` because you cannot concatenate a string and an integer directly.

**Corrected Code**:
```python
print("The answer is: " + str(42))
# Or using commas
print("The answer is:", 42)
```

---

### Question 8: Fix the SyntaxError with Multi-Line Strings
**Task**: Identify and correct the syntax error in this multi-line string.

```python
print("""
This is a multi-line string.
It doesn't have a proper closing.
```

**Error**: `SyntaxError: EOF while scanning triple-quoted string literal` because the multi-line string is not properly closed.

**Corrected Code**:
```python
print("""
This is a multi-line string.
It has a proper closing.
""")
```

---

### Question 9: Fix the ZeroDivisionError
**Task**: Correct the code to prevent a division by zero error.

```python
x = 10
y = 0
print(x / y)
```

**Error**: `ZeroDivisionError: division by zero` because division by zero is mathematically undefined.

**Corrected Code**:
```python
x = 10
y = 0
if y != 0:
    print(x / y)
else:
    print("Cannot divide by zero")
```

---

### Question 10: Fix the FileNotFoundError
**Task**: Correct the error in opening a file that does not exist.

```python
with open("nonexistentfile.txt", "r") as file:
    content = file.read()
```

**Error**: `FileNotFoundError: [Errno 2] No such file or directory` because the file does not exist.

**Corrected Code**:
```python
try:
    with open("nonexistentfile.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found. Please check the file path.")
```

---

### Question 11: Fix the Indentation Error in Loop
**Task**: Fix the indentation error in the following for loop.

```python
for i in range(5):
print(i)
```

**Error**: `IndentationError: expected an indented block` because the print statement is not indented.

**Corrected Code**:
```python
for i in range(5):
    print(i)
```

---

### Question 12: Fix the ValueError in Integer Conversion
**Task**: Correct the error when trying to convert an invalid string to an integer.

```python
num = int("abc")
```

**Error**: `ValueError: invalid literal for int() with base 10: 'abc'` because "abc" is not a valid integer.

**Corrected Code**:
```python
try:
    num = int("abc")
except ValueError:
    print("Cannot convert 'abc' to an integer")
```

---

These additional questions focus on common Python runtime errors and logic issues.

Here are additional "Fix the Error" questions:

---

### Question 13: Fix the TypeError in String Formatting
**Task**: Fix the error when using incorrect string formatting.

```python
name = "Alice"
age = 25
print("My name is {} and I am {} years old.".format(name))
```

**Error**: `IndexError: tuple index out of range` because there are two placeholders but only one argument is provided.

**Corrected Code**:
```python
name = "Alice"
age = 25
print("My name is {} and I am {} years old.".format(name, age))
```

---

### Question 14: Fix the KeyError in Dictionary Access
**Task**: Fix the error when accessing a key that does not exist in the dictionary.

```python
person = {"name": "John", "age": 30}
print(person["address"])
```

**Error**: `KeyError: 'address'` because the key "address" does not exist in the dictionary.

**Corrected Code**:
```python
person = {"name": "John", "age": 30}
print(person.get("address", "Address not found"))
```

---

### Question 15: Fix the AttributeError in Method Call
**Task**: Fix the error when trying to call a non-existent method.

```python
my_list = [1, 2, 3]
my_list.append(4)
my_list.add(5)
```

**Error**: `AttributeError: 'list' object has no attribute 'add'` because the `list` object does not have an `add` method.

**Corrected Code**:
```python
my_list = [1, 2, 3]
my_list.append(4)
my_list.append(5)
```

---

### Question 16: Fix the UnboundLocalError in Function
**Task**: Fix the error where a variable is used before it is assigned in a function.

```python
def my_function():
    print(x)
    x = 10

my_function()
```

**Error**: `UnboundLocalError: local variable 'x' referenced before assignment` because the variable `x` is used before it is defined within the function.

**Corrected Code**:
```python
def my_function():
    x = 10
    print(x)

my_function()
```

---

### Question 17: Fix the IndexError in List Access
**Task**: Correct the code to prevent accessing an out-of-range list index.

```python
my_list = [1, 2, 3]
print(my_list[5])
```

**Error**: `IndexError: list index out of range` because index 5 does not exist in the list.

**Corrected Code**:
```python
my_list = [1, 2, 3]
if len(my_list) > 5:
    print(my_list[5])
else:
    print("Index out of range")
```

---

### Question 18: Fix the SyntaxError in Function Definition
**Task**: Fix the syntax error in defining a function.

```python
def greet(name
    print(f"Hello, {name}!")
```

**Error**: `SyntaxError: invalid syntax` because the closing parenthesis is missing in the function definition.

**Corrected Code**:
```python
def greet(name):
    print(f"Hello, {name}!")
```

---

### Question 19: Fix the RecursionError
**Task**: Correct the code to prevent infinite recursion.

```python
def factorial(n):
    return n * factorial(n-1)

print(factorial(5))
```

**Error**: `RecursionError: maximum recursion depth exceeded` because there is no base case to stop the recursion.

**Corrected Code**:
```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))
```

---

### Question 20: Fix the TypeError in List Sorting
**Task**: Fix the error when trying to sort a list of mixed data types.

```python
my_list = [1, "two", 3, "four"]
my_list.sort()
```

**Error**: `TypeError: '<' not supported between instances of 'str' and 'int'` because you cannot directly compare integers and strings.

**Corrected Code**:
```python
my_list = [1, "two", 3, "four"]
my_list_str = sorted([str(i) for i in my_list])
print(my_list_str)
```

---

These additional questions cover more diverse and practical Python errors to deepen your understanding of error correction in Python code.

Here are additional "Fix the Error" questions for various Python concepts:

---

### Question 21: Fix the ZeroDivisionError
**Task**: Prevent the code from crashing when dividing by zero.

```python
x = 10
y = 0
result = x / y
print(result)
```

**Error**: `ZeroDivisionError: division by zero`

**Corrected Code**:
```python
x = 10
y = 0
if y != 0:
    result = x / y
else:
    print("Cannot divide by zero")
```

---

### Question 22: Fix the NameError in Variable Access
**Task**: Fix the error caused by using a variable that has not been defined.

```python
print(my_var)
```

**Error**: `NameError: name 'my_var' is not defined` because `my_var` is used without being assigned.

**Corrected Code**:
```python
my_var = "Hello"
print(my_var)
```

---

### Question 23: Fix the TypeError in Function Arguments
**Task**: Fix the error caused by providing an incorrect number of arguments to a function.

```python
def greet(name, age):
    print(f"Hello, {name}. You are {age} years old.")

greet("Alice")
```

**Error**: `TypeError: greet() missing 1 required positional argument: 'age'`

**Corrected Code**:
```python
def greet(name, age):
    print(f"Hello, {name}. You are {age} years old.")

greet("Alice", 25)
```

---

### Question 24: Fix the ValueError in Type Conversion
**Task**: Prevent the code from crashing when converting an invalid string to an integer.

```python
user_input = "abc"
num = int(user_input)
print(num)
```

**Error**: `ValueError: invalid literal for int() with base 10: 'abc'`

**Corrected Code**:
```python
user_input = "abc"
try:
    num = int(user_input)
    print(num)
except ValueError:
    print("Invalid input: cannot convert to an integer")
```

---

### Question 25: Fix the IndentationError in Loops
**Task**: Correct the code to fix inconsistent indentation.

```python
for i in range(5):
  print(i)
    print(i * 2)
```

**Error**: `IndentationError: unexpected indent`

**Corrected Code**:
```python
for i in range(5):
    print(i)
    print(i * 2)
```

---

### Question 26: Fix the SyntaxError in Conditional Statements
**Task**: Fix the syntax error in the `if` statement.

```python
if x > 5
    print("x is greater than 5")
```

**Error**: `SyntaxError: invalid syntax` because there is no colon `:` after the `if` condition.

**Corrected Code**:
```python
if x > 5:
    print("x is greater than 5")
```

---

### Question 27: Fix the TypeError in List Concatenation
**Task**: Fix the error caused by trying to concatenate a list with an integer.

```python
my_list = [1, 2, 3]
my_list += 4
```

**Error**: `TypeError: 'int' object is not iterable` because you cannot concatenate a list with a single integer.

**Corrected Code**:
```python
my_list = [1, 2, 3]
my_list.append(4)
```

---

### Question 28: Fix the ModuleNotFoundError
**Task**: Fix the error caused by trying to import a non-existent module.

```python
import my_custom_module
```

**Error**: `ModuleNotFoundError: No module named 'my_custom_module'`

**Corrected Code**:
```python
# Ensure the module exists or install it if it's a third-party library
# Example: Using the correct built-in module
import math
```

---

### Question 29: Fix the TypeError in Function Return Value
**Task**: Correct the error caused by returning a wrong type from a function.

```python
def add_numbers(a, b):
    return a + " " + b

result = add_numbers(10, 20)
print(result)
```

**Error**: `TypeError: unsupported operand type(s) for +: 'int' and 'str'`

**Corrected Code**:
```python
def add_numbers(a, b):
    return str(a) + " " + str(b)

result = add_numbers(10, 20)
print(result)
```

---

### Question 30: Fix the ImportError in Module Import
**Task**: Fix the error caused by an incorrect import statement.

```python
from math import squareroot
print(squareroot(16))
```

**Error**: `ImportError: cannot import name 'squareroot' from 'math'` because the correct function name is `sqrt`.

**Corrected Code**:
```python
from math import sqrt
print(sqrt(16))
```

---

These additional questions cover more errors in common Python tasks, helping to practice and understand how to identify and fix various coding issues.

Here are **30 more "Fix the Error" questions** to help practice identifying and correcting common Python errors:

---

### Question 31: Fix the SyntaxError in Defining a Function
**Task**: Correct the function definition.

```python
def my_function(param1, param2
    return param1 + param2
```

**Error**: `SyntaxError: invalid syntax` due to missing closing parenthesis in the function definition.

**Corrected Code**:
```python
def my_function(param1, param2):
    return param1 + param2
```

---

### Question 32: Fix the KeyError in Dictionary Access
**Task**: Fix the error when trying to access a key that does not exist in the dictionary.

```python
my_dict = {"name": "Alice", "age": 30}
print(my_dict["address"])
```

**Error**: `KeyError: 'address'`

**Corrected Code**:
```python
print(my_dict.get("address", "Address not found"))
```

---

### Question 33: Fix the AttributeError in Using a Non-Existent Method
**Task**: Fix the error caused by trying to call a non-existent method.

```python
my_list = [1, 2, 3]
my_list.push(4)
```

**Error**: `AttributeError: 'list' object has no attribute 'push'`

**Corrected Code**:
```python
my_list.append(4)
```

---

### Question 34: Fix the IndexError in List Indexing
**Task**: Prevent the code from crashing when accessing an out-of-range index in a list.

```python
my_list = [1, 2, 3]
print(my_list[5])
```

**Error**: `IndexError: list index out of range`

**Corrected Code**:
```python
if len(my_list) > 5:
    print(my_list[5])
else:
    print("Index out of range")
```

---

### Question 35: Fix the TypeError in String and Integer Concatenation
**Task**: Correct the error caused by trying to concatenate a string and an integer.

```python
age = 25
message = "I am " + age + " years old"
```

**Error**: `TypeError: can only concatenate str (not "int") to str`

**Corrected Code**:
```python
message = "I am " + str(age) + " years old"
```

---

### Question 36: Fix the ValueError in List Sorting
**Task**: Fix the error caused by trying to sort a list with mixed data types.

```python
my_list = [1, "two", 3]
my_list.sort()
```

**Error**: `TypeError: '<' not supported between instances of 'str' and 'int'`

**Corrected Code**:
```python
# Remove strings or convert them to numbers before sorting
my_list = [1, 3]
my_list.sort()
```

---

### Question 37: Fix the OverflowError in Exponential Calculations
**Task**: Prevent the overflow error in large exponent calculations.

```python
result = 10 ** 10000
print(result)
```

**Error**: `OverflowError: integer pow() too large to convert to float`

**Corrected Code**:
```python
import math
result = math.pow(10, 100)
print(result)
```

---

### Question 38: Fix the FileNotFoundError in File Handling
**Task**: Fix the error when trying to open a non-existent file.

```python
with open("nonexistent_file.txt", "r") as file:
    content = file.read()
```

**Error**: `FileNotFoundError: [Errno 2] No such file or directory: 'nonexistent_file.txt'`

**Corrected Code**:
```python
try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found")
```

---

### Question 39: Fix the SyntaxError in Dictionary Comprehension
**Task**: Correct the syntax in a dictionary comprehension.

```python
squares = {x: x**2 for x in range(1, 6]
```

**Error**: `SyntaxError: invalid syntax` due to missing closing bracket.

**Corrected Code**:
```python
squares = {x: x**2 for x in range(1, 6)}
```

---

### Question 40: Fix the UnboundLocalError in Function Variables
**Task**: Fix the error caused by using a local variable before it is assigned.

```python
def increment():
    count += 1
    return count

increment()
```

**Error**: `UnboundLocalError: local variable 'count' referenced before assignment`

**Corrected Code**:
```python
count = 0
def increment():
    global count
    count += 1
    return count

increment()
```

---

### Question 41: Fix the RecursionError in Recursive Function
**Task**: Fix the error caused by exceeding the recursion limit.

```python
def factorial(n):
    return n * factorial(n - 1)

print(factorial(1000))
```

**Error**: `RecursionError: maximum recursion depth exceeded in comparison`

**Corrected Code**:
```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(10))
```

---

### Question 42: Fix the NameError in Function Call
**Task**: Fix the error caused by calling a function that does not exist.

```python
greet_user()
```

**Error**: `NameError: name 'greet_user' is not defined`

**Corrected Code**:
```python
def greet_user():
    print("Hello!")

greet_user()
```

---

### Question 43: Fix the SyntaxError in For Loop
**Task**: Correct the syntax in the `for` loop.

```python
for i in range(10)
    print(i)
```

**Error**: `SyntaxError: invalid syntax` due to missing colon `:` at the end of the `for` loop.

**Corrected Code**:
```python
for i in range(10):
    print(i)
```

---

### Question 44: Fix the TypeError in List Append
**Task**: Fix the error caused by trying to append a list with another list using incorrect syntax.

```python
my_list = [1, 2, 3]
my_list.append([4, 5])
```

**Error**: No error, but the list will have a nested list.

**Corrected Code**:
```python
my_list = [1, 2, 3]
my_list.extend([4, 5])
```

---

### Question 45: Fix the IndentationError in Conditional Statements
**Task**: Correct the indentation in the following code.

```python
if True:
  print("True")
    print("False")
```

**Error**: `IndentationError: unexpected indent`

**Corrected Code**:
```python
if True:
    print("True")
    print("False")
```

---

### Question 46: Fix the TypeError in Map Function
**Task**: Fix the error caused by using `map` with a function that expects multiple arguments.

```python
def multiply(a, b):
    return a * b

nums = [1, 2, 3]
result = map(multiply, nums)
print(list(result))
```

**Error**: `TypeError: multiply() missing 1 required positional argument: 'b'`

**Corrected Code**:
```python
def multiply(a):
    return a * 2

nums = [1, 2, 3]
result = map(multiply, nums)
print(list(result))
```

---

### Question 47: Fix the ImportError in Using Random Library
**Task**: Fix the error caused by trying to use a non-existent function in the `random` module.

```python
import random
print(random.choice_int(10))
```

**Error**: `AttributeError: module 'random' has no attribute 'choice_int'`

**Corrected Code**:
```python
import random
print(random.randint(1, 10))
```

---

### Question 48: Fix the IndentationError in While Loop
**Task**: Correct the indentation error in the while loop.

```python
while True:
  print("Hello")
   print("World")
```

**Error**: `IndentationError: unexpected indent`

**Corrected Code**:
```python
while True:
    print("Hello")
    print("World")
```

---

### Question 49: Fix the SyntaxError in Lambda Expression
**Task**: Fix the syntax in the lambda expression.

```python
double = lambda x: x*2
print(double(5))
```

**Error**: No error, but let's modify it to use multiple arguments.

**Corrected Code**:
```python
multiply = lambda x, y: x * y
print(multiply(5, 3))
```

---

### Question 50: Fix the TypeError in String Formatting
**Task**: Correct the error in string formatting using the `format()` method.

```python
name = "Alice"
age = 30
print("My name is {} and I am {} years old.".format(name))
```

**Error**: `IndexError: tuple index out of range`

**Corrected Code**:
```python

Here are **30 additional "Fix the Error" questions** to further practice identifying and correcting common Python errors:

---

### Question 51: Fix the TypeError in Division
**Task**: Correct the error caused by dividing an integer by a string.

```python
result = 10 / "2"
```

**Error**: `TypeError: unsupported operand type(s) for /: 'int' and 'str'`

**Corrected Code**:
```python
result = 10 / int("2")
```

---

### Question 52: Fix the NameError in Variable Scope
**Task**: Fix the error caused by using a variable outside its scope.

```python
def my_function():
    x = 10

my_function()
print(x)
```

**Error**: `NameError: name 'x' is not defined`

**Corrected Code**:
```python
def my_function():
    global x
    x = 10

my_function()
print(x)
```

---

### Question 53: Fix the ValueError in Tuple Unpacking
**Task**: Correct the error caused by incorrect tuple unpacking.

```python
x, y = (1, 2, 3)
```

**Error**: `ValueError: too many values to unpack (expected 2)`

**Corrected Code**:
```python
x, y, z = (1, 2, 3)
```

---

### Question 54: Fix the IndexError in List Slicing
**Task**: Prevent the code from crashing when slicing a list with an incorrect index.

```python
my_list = [1, 2, 3]
print(my_list[1:5])
```

**Error**: No error, but slicing beyond the length of the list returns an empty list.

**Corrected Code**:
```python
print(my_list[1:len(my_list)])
```

---

### Question 55: Fix the KeyError in Dictionary Deletion
**Task**: Fix the error caused by trying to delete a non-existent key in a dictionary.

```python
my_dict = {"name": "Alice", "age": 30}
del my_dict["address"]
```

**Error**: `KeyError: 'address'`

**Corrected Code**:
```python
my_dict.pop("address", None)
```

---

### Question 56: Fix the AttributeError in Object Method
**Task**: Fix the error caused by calling a non-existent method on an object.

```python
class Person:
    def __init__(self, name):
        self.name = name

p = Person("John")
p.say_hello()
```

**Error**: `AttributeError: 'Person' object has no attribute 'say_hello'`

**Corrected Code**:
```python
class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, my name is {self.name}")

p = Person("John")
p.say_hello()
```

---

### Question 57: Fix the OverflowError in Large Integers
**Task**: Fix the overflow error when performing operations with large integers.

```python
result = 2 ** 10000
```

**Error**: `OverflowError: (34, 'Result too large')`

**Corrected Code**:
```python
import math
result = math.exp(10000)
```

---

### Question 58: Fix the SyntaxError in Function Arguments
**Task**: Fix the syntax error in function arguments.

```python
def add_numbers(a, b):
    return a + b

print(add_numbers(5, 10, 15))
```

**Error**: `TypeError: add_numbers() takes 2 positional arguments but 3 were given`

**Corrected Code**:
```python
def add_numbers(a, b, c=0):
    return a + b + c

print(add_numbers(5, 10, 15))
```

---

### Question 59: Fix the ImportError in Module Usage
**Task**: Fix the error caused by using an incorrect import statement.

```python
import mathlib

print(mathlib.sqrt(16))
```

**Error**: `ModuleNotFoundError: No module named 'mathlib'`

**Corrected Code**:
```python
import math

print(math.sqrt(16))
```

---

### Question 60: Fix the TypeError in List Comprehension
**Task**: Fix the error in a list comprehension with mixed types.

```python
my_list = [x + 1 for x in [1, 2, "3"]]
```

**Error**: `TypeError: can only concatenate int (not "str") to int`

**Corrected Code**:
```python
my_list = [x + 1 for x in [1, 2] if isinstance(x, int)]
```

---

### Question 61: Fix the SyntaxError in Lambda Function
**Task**: Correct the syntax in a lambda function with multiple statements.

```python
add = lambda x, y: x + y
print(add(2, 3))
```

**Error**: No error, but lambda functions should be single expressions.

**Corrected Code**:
```python
add = lambda x, y: x + y
print(add(2, 3))
```

---

### Question 62: Fix the ValueError in Float Conversion
**Task**: Fix the error caused by trying to convert an invalid string to float.

```python
value = float("123.45.67")
```

**Error**: `ValueError: too many decimal points`

**Corrected Code**:
```python
value = float("123.45")
```

---

### Question 63: Fix the SyntaxError in String Formatting
**Task**: Fix the syntax error in string formatting.

```python
name = "Alice"
age = 30
print("My name is {name} and I am {age} years old.")
```

**Error**: `KeyError: 'name'`

**Corrected Code**:
```python
print(f"My name is {name} and I am {age} years old.")
```

---

### Question 64: Fix the UnboundLocalError in List Modification
**Task**: Fix the error caused by modifying a list inside a function.

```python
numbers = [1, 2, 3]

def add_number():
    numbers.append(4)

add_number()
print(numbers)
```

**Error**: No error, but if the list is used as a global variable.

**Corrected Code**:
```python
numbers = [1, 2, 3]

def add_number():
    global numbers
    numbers.append(4)

add_number()
print(numbers)
```

---

### Question 65: Fix the FileNotFoundError in File Reading
**Task**: Fix the error when reading from a file that does not exist.

```python
with open("data.csv", "r") as file:
    content = file.read()
```

**Error**: `FileNotFoundError: [Errno 2] No such file or directory: 'data.csv'`

**Corrected Code**:
```python
try:
    with open("data.csv", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found")
```

---

### Question 66: Fix the SyntaxError in Import Statement
**Task**: Fix the syntax error in an import statement.

```python
from math import sqrt, pow
```

**Error**: No error, but let's correct a common mistake in imports.

**Corrected Code**:
```python
from math import sqrt, pow

print(sqrt(16))
print(pow(2, 3))
```

---

### Question 67: Fix the NameError in Global Variable
**Task**: Fix the error caused by accessing a global variable inside a function.

```python
value = 10

def print_value():
    print(value)

print_value()
```

**Error**: No error, but ensure global access.

**Corrected Code**:
```python
value = 10

def print_value():
    global value
    print(value)

print_value()
```

---

### Question 68: Fix the TypeError in Dictionary Update
**Task**: Fix the error when trying to update a dictionary with invalid key-value pairs.

```python
my_dict = {"name": "Alice"}
my_dict.update("age": 30)
```

**Error**: `TypeError: update() argument 1 must be a mapping or iterable`

**Corrected Code**:
```python
my_dict.update({"age": 30})
```

---

### Question 69: Fix the IndentationError in Nested If Statements
**Task**: Correct the indentation in nested `if` statements.

```python
age = 20

if age > 18:
print("Adult")
else:
print("Minor")
```

**Error**: `IndentationError: expected an indented block`

**Corrected Code**:
```python
age = 20

if age > 18:
    print("Adult")
else:
    print("Minor")
```

---

### Question 70: Fix the OverflowError in Exponential Operations
**Task**: Fix the error when performing large exponent operations.

```python
result = 10 ** 1000
```

**Error**: `OverflowError: (34, 'Result too large')`

**Corrected Code**:
```python
import decimal
result = decimal.Decimal(10) ** 1000
```

---

### Question 71: Fix the SyntaxError in Nested Lists
**Task**: Fix

Here are **30 additional "Fix the Error" questions** to further practice identifying and correcting common Python errors:

---

### Question 51: Fix the TypeError in Division
**Task**: Correct the error caused by dividing an integer by a string.

```python
result = 10 / "2"
```

**Error**: `TypeError: unsupported operand type(s) for /: 'int' and 'str'`

**Corrected Code**:
```python
result = 10 / int("2")
```

---

### Question 52: Fix the NameError in Variable Scope
**Task**: Fix the error caused by using a variable outside its scope.

```python
def my_function():
    x = 10

my_function()
print(x)
```

**Error**: `NameError: name 'x' is not defined`

**Corrected Code**:
```python
def my_function():
    global x
    x = 10

my_function()
print(x)
```

---

### Question 53: Fix the ValueError in Tuple Unpacking
**Task**: Correct the error caused by incorrect tuple unpacking.

```python
x, y = (1, 2, 3)
```

**Error**: `ValueError: too many values to unpack (expected 2)`

**Corrected Code**:
```python
x, y, z = (1, 2, 3)
```

---

### Question 54: Fix the IndexError in List Slicing
**Task**: Prevent the code from crashing when slicing a list with an incorrect index.

```python
my_list = [1, 2, 3]
print(my_list[1:5])
```

**Error**: No error, but slicing beyond the length of the list returns an empty list.

**Corrected Code**:
```python
print(my_list[1:len(my_list)])
```

---

### Question 55: Fix the KeyError in Dictionary Deletion
**Task**: Fix the error caused by trying to delete a non-existent key in a dictionary.

```python
my_dict = {"name": "Alice", "age": 30}
del my_dict["address"]
```

**Error**: `KeyError: 'address'`

**Corrected Code**:
```python
my_dict.pop("address", None)
```

---

### Question 56: Fix the AttributeError in Object Method
**Task**: Fix the error caused by calling a non-existent method on an object.

```python
class Person:
    def __init__(self, name):
        self.name = name

p = Person("John")
p.say_hello()
```

**Error**: `AttributeError: 'Person' object has no attribute 'say_hello'`

**Corrected Code**:
```python
class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, my name is {self.name}")

p = Person("John")
p.say_hello()
```

---

### Question 57: Fix the OverflowError in Large Integers
**Task**: Fix the overflow error when performing operations with large integers.

```python
result = 2 ** 10000
```

**Error**: `OverflowError: (34, 'Result too large')`

**Corrected Code**:
```python
import math
result = math.exp(10000)
```

---

### Question 58: Fix the SyntaxError in Function Arguments
**Task**: Fix the syntax error in function arguments.

```python
def add_numbers(a, b):
    return a + b

print(add_numbers(5, 10, 15))
```

**Error**: `TypeError: add_numbers() takes 2 positional arguments but 3 were given`

**Corrected Code**:
```python
def add_numbers(a, b, c=0):
    return a + b + c

print(add_numbers(5, 10, 15))
```

---

### Question 59: Fix the ImportError in Module Usage
**Task**: Fix the error caused by using an incorrect import statement.

```python
import mathlib

print(mathlib.sqrt(16))
```

**Error**: `ModuleNotFoundError: No module named 'mathlib'`

**Corrected Code**:
```python
import math

print(math.sqrt(16))
```

---

### Question 60: Fix the TypeError in List Comprehension
**Task**: Fix the error in a list comprehension with mixed types.

```python
my_list = [x + 1 for x in [1, 2, "3"]]
```

**Error**: `TypeError: can only concatenate int (not "str") to int`

**Corrected Code**:
```python
my_list = [x + 1 for x in [1, 2] if isinstance(x, int)]
```

---

### Question 61: Fix the SyntaxError in Lambda Function
**Task**: Correct the syntax in a lambda function with multiple statements.

```python
add = lambda x, y: x + y
print(add(2, 3))
```

**Error**: No error, but lambda functions should be single expressions.

**Corrected Code**:
```python
add = lambda x, y: x + y
print(add(2, 3))
```

---

### Question 62: Fix the ValueError in Float Conversion
**Task**: Fix the error caused by trying to convert an invalid string to float.

```python
value = float("123.45.67")
```

**Error**: `ValueError: too many decimal points`

**Corrected Code**:
```python
value = float("123.45")
```

---

### Question 63: Fix the SyntaxError in String Formatting
**Task**: Fix the syntax error in string formatting.

```python
name = "Alice"
age = 30
print("My name is {name} and I am {age} years old.")
```

**Error**: `KeyError: 'name'`

**Corrected Code**:
```python
print(f"My name is {name} and I am {age} years old.")
```

---

### Question 64: Fix the UnboundLocalError in List Modification
**Task**: Fix the error caused by modifying a list inside a function.

```python
numbers = [1, 2, 3]

def add_number():
    numbers.append(4)

add_number()
print(numbers)
```

**Error**: No error, but if the list is used as a global variable.

**Corrected Code**:
```python
numbers = [1, 2, 3]

def add_number():
    global numbers
    numbers.append(4)

add_number()
print(numbers)
```

---

### Question 65: Fix the FileNotFoundError in File Reading
**Task**: Fix the error when reading from a file that does not exist.

```python
with open("data.csv", "r") as file:
    content = file.read()
```

**Error**: `FileNotFoundError: [Errno 2] No such file or directory: 'data.csv'`

**Corrected Code**:
```python
try:
    with open("data.csv", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found")
```

---

### Question 66: Fix the SyntaxError in Import Statement
**Task**: Fix the syntax error in an import statement.

```python
from math import sqrt, pow
```

**Error**: No error, but let's correct a common mistake in imports.

**Corrected Code**:
```python
from math import sqrt, pow

print(sqrt(16))
print(pow(2, 3))
```

---

### Question 67: Fix the NameError in Global Variable
**Task**: Fix the error caused by accessing a global variable inside a function.

```python
value = 10

def print_value():
    print(value)

print_value()
```

**Error**: No error, but ensure global access.

**Corrected Code**:
```python
value = 10

def print_value():
    global value
    print(value)

print_value()
```

---

### Question 68: Fix the TypeError in Dictionary Update
**Task**: Fix the error when trying to update a dictionary with invalid key-value pairs.

```python
my_dict = {"name": "Alice"}
my_dict.update("age": 30)
```

**Error**: `TypeError: update() argument 1 must be a mapping or iterable`

**Corrected Code**:
```python
my_dict.update({"age": 30})
```

---

### Question 69: Fix the IndentationError in Nested If Statements
**Task**: Correct the indentation in nested `if` statements.

```python
age = 20

if age > 18:
print("Adult")
else:
print("Minor")
```

**Error**: `IndentationError: expected an indented block`

**Corrected Code**:
```python
age = 20

if age > 18:
    print("Adult")
else:
    print("Minor")
```

---

### Question 70: Fix the OverflowError in Exponential Operations
**Task**: Fix the error when performing large exponent operations.

```python
result = 10 ** 1000
```

**Error**: `OverflowError: (34, 'Result too large')`

**Corrected Code**:
```python
import decimal
result = decimal.Decimal(10) ** 1000
```

---

### Question 71: Fix the SyntaxError in Nested Lists
**Task**: Fix

 the syntax error in nested lists.

```python
nested_list = [[1, 2, 3], [4, 5, 6]]
print(nested_list[1][2])
```

**Error**: No error, but ensure correct indexing.

**Corrected Code**:
```python
nested_list = [[1, 2, 3], [4, 5, 6]]
print(nested_list[1][2])
```

---

### Question 72: Fix the AttributeError in Using a Method
**Task**: Fix the error when using a method that doesn’t exist on a list.

```python
my_list = [1, 2, 3]
my_list.reverse_list()
```

**Error**: `AttributeError: 'list' object has no attribute 'reverse_list'`

**Corrected Code**:
```python
my_list.reverse()
```

---

### Question 73: Fix the ValueError in Unpacking
**Task**: Fix the error caused by incorrect unpacking of a tuple.

```python
a, b = (1, 2, 3)
```

**Error**: `ValueError: too many values to unpack (expected 2)`

**Corrected Code**:
```python
a, b, c = (1, 2, 3)
```

---

### Question 74: Fix the NameError in Local Variable
**Task**: Fix the error when using a local variable before assignment.

```python
def calculate():
    total += 5
    return total

total = 10
print(calculate())
```

**Error**: `UnboundLocalError: local variable 'total' referenced before assignment`

**Corrected Code**:
```python
def calculate():
    global total
    total += 5
    return total

total = 10
print(calculate())
```

---

### Question 75: Fix the TypeError in List Extend
**Task**: Fix the error when extending a list with an integer.

```python
my_list = [1, 2]
my_list.extend(3)
```

**Error**: `TypeError: extend() argument must be an iterable`

**Corrected Code**:
```python
my_list.extend([3])
```

---

### Question 76: Fix the IndexError in String Slicing
**Task**: Fix the error caused by incorrect string slicing.

```python
text = "Python"
print(text[10:])
```

**Error**: No error, but slicing beyond length returns an empty string.

**Corrected Code**:
```python
print(text[:len(text)])
```

---

### Question 77: Fix the SyntaxError in Lambda Function
**Task**: Fix the syntax error in a lambda function with an incorrect expression.

```python
add = lambda x, y: x + y
print(add(10, 20))
```

**Error**: No error, but ensure single expression.

**Corrected Code**:
```python
add = lambda x, y: x + y
print(add(10, 20))
```

---

### Question 78: Fix the ValueError in Integer Conversion
**Task**: Fix the error when converting an invalid string to an integer.

```python
num = int("123abc")
```

**Error**: `ValueError: invalid literal for int() with base 10: '123abc'`

**Corrected Code**:
```python
num = int("123")
```

---

### Question 79: Fix the FileNotFoundError in CSV Reading
**Task**: Fix the error when reading a non-existent CSV file.

```python
import csv
with open("data.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

**Error**: `FileNotFoundError: [Errno 2] No such file or directory: 'data.csv'`

**Corrected Code**:
```python
import csv
try:
    with open("data.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("CSV file not found")
```

---

### Question 80: Fix the AttributeError in Importing
**Task**: Fix the error caused by importing a non-existent function.

```python
from math import sqrt, square

print(sqrt(16))
```

**Error**: `ImportError: cannot import name 'square' from 'math'`

**Corrected Code**:
```python
from math import sqrt

print(sqrt(16))
```

---

### Question 81: Fix the SyntaxError in Function Definition
**Task**: Fix the syntax error in a function definition with a missing colon.

```python
def multiply(a, b)
    return a * b
```

**Error**: `SyntaxError: invalid syntax` due to missing colon.

**Corrected Code**:
```python
def multiply(a, b):
    return a * b
```

---

### Question 82: Fix the ValueError in List Indexing
**Task**: Fix the error when accessing an invalid index in a list.

```python
my_list = [1, 2, 3]
print(my_list[3])
```

**Error**: `IndexError: list index out of range`

**Corrected Code**:
```python
print(my_list[2])  # Last valid index
```

---

### Question 83: Fix the NameError in Function Call
**Task**: Fix the error caused by calling an undefined function.

```python
result = add(5, 3)
```

**Error**: `NameError: name 'add' is not defined`

**Corrected Code**:
```python
def add(a, b):
    return a + b

result = add(5, 3)
```

---

### Question 84: Fix the TypeError in String Replacement
**Task**: Fix the error caused by incorrect replacement arguments.

```python
text = "Hello World"
text.replace("World", 123)
```

**Error**: `TypeError: replace() argument 2 must be str, not int`

**Corrected Code**:
```python
text = "Hello World"
text = text.replace("World", "123")
```

---

### Question 85: Fix the SyntaxError in Class Definition
**Task**: Fix the syntax error in class definition.

```python
class MyClass:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1
```

**Error**: No error, but ensure correct syntax.

**Corrected Code**:
```python
class MyClass:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

obj = MyClass()
obj.increment()
print(obj.value)
```

---

### Question 86: Fix the TypeError in String Concatenation
**Task**: Fix the error caused by concatenating strings and integers.

```python
age = 25
message = "I am " + age + " years old"
```

**Error**: `TypeError: can only concatenate str (not "int") to str`

**Corrected Code**:
```python
message = "I am " + str(age) + " years old"
```

---

### Question 87: Fix the NameError in Local vs Global Variable
**Task**: Fix the error caused by using a local variable that shadows a global variable.

```python
value = 5

def set_value():
    value = 10
    return value

print(set_value())
print(value)
```

**Error**: No error, but ensure clarity between local and global.

**Corrected Code**:
```python
value = 5

def set_value():
    global value
    value = 10
    return value

print(set_value())
print(value)
```

---

### Question 88: Fix the IndexError in List Deletion
**Task**: Fix the error when deleting an invalid index from a list.

```python
my_list = [1, 2, 3]
del my_list[5]
```

**Error**: `IndexError: list assignment index out of range`

**Corrected Code**:
```python
del my_list[2]  # Delete the last valid index
```

---

### Question 89: Fix the OverflowError in Large Numbers
**Task**: Fix the error when working with very large numbers.

```python
result = 1e+1000
```

**Error**: `OverflowError: (34, 'Result too large')`

**Corrected Code**:
```python
import decimal
result = decimal.Decimal(1e+100)
```

---

### Question 90: Fix the SyntaxError in Tuple Definition
**Task**: Fix the syntax error in a tuple definition.

```python
my_tuple = (1, 2, 3, 4
```

**Error**: `SyntaxError: unexpected EOF while parsing`

**Corrected Code**:
```python
my_tuple = (1, 2, 3, 4)
```

---

### Question 91: Fix the ValueError in Float Conversion
**Task**: Fix the error when converting an invalid string to a float.

```python
value = float("12.34.56")
```

**Error**: `ValueError: too many decimal points`

**Corrected Code**:
```python
value = float("12.34")
```

---

### Question 92: Fix the FileNotFoundError in Reading CSV
**Task**: Fix the error when reading a non-existent CSV file.

```python
