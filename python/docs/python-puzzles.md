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

**1. Indentation Error**

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

**1. Name Error: Using a Variable Before Definition**

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

**Name Error: Using a Variable Before Definition**

```python
age = 25
print(f"You are {age} years old")

name = "Alice"
greet(name)  # NameError: greet is not defined yet

def greet(name):
  print(f"Hello, {name}")
```
**Name Errors (Using Undefied Variables or Functions)**
```python
# Trying to use a variable before it's defined
age = 30
print(name)  # Name error: name is not defined

# Calling a function that hasn't been defined yet
def calculate_area(length, width):
    return length * width

result = calculate_area(5, 3)  # This line would cause a name error if calculate_area is defined after this point

# Using a typo in a variable name
my_list = [1, 2, 3]
print(mylist)  # Name error: mylist is not defined (use my_list instead)
```

## Type Error

```python
number = "ten"
number = number + 5
```

This code assigns the string "ten" to the variable "number". 
The error occurs when it tries to add 5 (an integer) to "number", which is a string. Python cannot perform these operations on different data types.

**1. Type Error: Trying to Add Strings and Numbers**

```python
age = 25
message = "You are " + str(age) + " years old."
message += " Welcome!"  # Trying to add string and int
```

**Error:** This code will result in a `TypeError: can only concatenate str (not "int") to str` because you're trying to add an integer (`age`) to a string (`message`).

**Fix:** Convert `age` to a string before adding.

```python
age = 25
message = "You are " + str(age) + " years old."
message += " Welcome!"
```

**Type Error: Trying to Perform an Operation on Incompatible Data Types**

```python
number = 10
greeting = "Hello"

# Trying to add an integer and a string
combined = number + greeting
print(combined)  # This will cause a TypeError
```
Here, the code attempts to add an integer (number) and a string (greeting), which is not allowed in Python. You can only perform operations on compatible data types.

**Incorrect Input Conversion**

```python
age = input("Enter your age: ")  # Input is a string, needs conversion
result = age * 2  # Error: cannot multiply string by number
```

## Index Error

**1. Index Out of Range**

```python
numbers = [1, 2, 3]
print(numbers[4])  # Trying to access non-existent index
```

**Error:** This code will throw an `IndexError: list index out of range` because you're trying to access the element at index 4, which doesn't exist in a list of size 3.

**Fix:** Make sure you're accessing elements within the valid range of the list (0 to length-1).


```python
fruits = ["apple", "banana", "orange"]
print(fruits[3])
```

```python
# Trying to access an element that doesn't exist
my_list = [1, 2, 3]
element = my_list[5]  # IndexError: list index out of range

# Trying to access a character beyond the string's length
name = "Alice"
first_letter = name[6]  # IndexError: string index out of range
```

## KeyError

```python
my_dict = {"name": "Alice", "age": 30}
print(my_dict["city"])  
Error: key 'city' not found in the dictionary
```

```python
# Trying to access a non-existent key in a dictionary
my_dict = {"name": "Alice", "age": 30}
value = my_dict["city"]  # KeyError: 'city'

# Using a typo in a key
ages = {"Alice": 30, "Bob": 25}
bobs_age = ages["Bobs"]  # KeyError: 'Bobs' (should be 'Bob')

```
## Logical Error

## Incorrect Loop Termination

```python
while x < 10:  
  print(x)
```

```python
x = 0
while x < 10:  # Missing increment in the loop condition
  print(x)
```

```python
if password = "secret":  # Should be '==' for equality check
  print("Access granted")
else:
  print("Wrong password")
```

## Zero Division Error:

```python
def divide(a, b):
  return a / b

result = divide(10, 0)  # Dividing by zero
```

This code defines a function to divide two numbers. 
The error occurs when it calls the function with 0 as the second argument (divisor). Dividing by zero is not allowed in Python.



