# Python for Beginners: Functions

Connect with me: [Youtube](https://www.youtube.com/yasirbhutta) \| [LinkedIn](https://www.linkedin.com/in/yasirbhutta/) \| [WhatsApp Channel](https://whatsapp.com/channel/0029VaC3BC160eBZZSs3CW0c) \| [Web](https://yasirbhutta.github.io/) \| [Facebook](https://www.facebook.com/yasirbhutta786) \| [Twitter](https://twitter.com/yasirbhutta)

- [Download PDF](https://yasirbhutta.github.io/python/docs/functions.pdf)
- To access the updated lecture notes, please click on the following link:
[https://yasirbhutta.github.io/python/docs/functions.html](https://yasirbhutta.github.io/python/docs/functions.html)

## Functions

**Syntax of function:**

- [Video: How to Add Two Numbers and Print the Result](https://www.youtube.com/watch?v=CQHXsGnUns0&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=24)
- [Video: How to Find the Maximum Value in a List of Numbers](https://www.youtube.com/watch?v=AcC4ykPRYhc&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=23)
- [Video: How to Write a Python Function to Find the Length of a Word](https://www.youtube.com/watch?v=wKuKX8-at5E&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=22)
- [Video: Learn How to Use Default Parameters in Function Definition](https://www.youtube.com/watch?v=2z_K1YChX1A&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=21)
- [Video: Understanding *args in Functions - How to Add Any Number of Arguments with *args](https://www.youtube.com/watch?v=0noa3Sgxmg8&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=6)
- [Video: How to Use *args in Python Functions](https://www.youtube.com/watch?v=7ejTzBybkw4&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=5)
- [Video: How to use **kwargs in Python](https://www.youtube.com/watch?v=_NMaZ9EO0zI&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=2)

**See also:**

- [Python Quiz - Functions](https://forms.gle/ZxyA5p98T9f8CZsA6)

**See also:**

- [Built-in Functions - Python 3.12.1 documentation](https://docs.python.org/3/library/stdtypes.html)
  
### Anonymous (Lambda) Functions

- A lambda function in Python is a small, anonymous function that can be defined without name.
- Lamdba functions are used to write functions consisting of a single statement.
- A lambda function can take any number of arguments, but can only have one expression.
- It is created using the 'lambda' keyword, and it is often used as an argument to a higher-order function (a function that takes another function as an argument).

**Syntax:**

The syntax of a lambda is

```python
lambda arguments:express
```

**Example #1:**

Following code is used to write the function to add 10 in given number.

```python
def add_ten(x)
    return x + 10
```

above function can be written by the lamdba function in python.

```python

add_ten = lamdba x: x + 10
print(add_ten(5) # 15

```

**Example #2:** multiple two numbers

use of lambda function to multiple two numbers

```python
mul = lambda a, b : a * b
print(mul(2,4)) # 8
```

**Example #3:**

```python
lambda x, y : x + y

_(6,8) # 14
```

**Note:** In the interactive interpreter, the single underscore**(_)** is bound to the last expression evalued.

**Example #4:** Immediately invoked function expression

```python
(lambda x, y : x + y)(6,8) # 14
```

The lambda function above is defined and then immediately called with two arguments (6,8). it retuns the value **14**, which is the sum of the arguments.

**Example #5:**

```python
def multiply(lambda(x,y):
    retun x*y

result = (lambda x,y : multiply(x,y))(5,3) 
print(result) # Output: 15

mult = lambda x,y : multiply(x,y)
result = mult(6,2)
print(result) # Output: 12
```

- [Video: How to: Use of Lambda function](https://www.youtube.com/watch?v=Z8Zeen4WwJQ&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=83)
- [Video: How to: Use of Lambda function](https://www.youtube.com/watch?v=N3UAUI6cEVA&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=81)

## Built-in Functions

### Filter()

- In Python, the 'filter()' function is used to filter a sequence (e.g. list, tuple, etc.) by applying a certain test to each eleent of the sequence and returning only the elements that pass the test.
- The 'filter()' function takes two arguments: function and an iterable. The function is applied to each element of the iterable, and if the function retuns 'True' for that element, the element is included in the resulting iterable.

### Example #5 use of lambda in filter() function

```python

numbers = [1,2,3,4,5,6,7,8,9,10] # list

even_numbers= list(filter(lambda x : x % 2 == 0,numbers))

print(even_numbers)

```

### Map()

- In Python, the 'map()' function is used to apply a certain function to each element of an iterable (e.g. list, tuple, etc.) and return an iterable containing the results.
- The 'map()' function takes two arguments: a function and an iterable. The function is applied to each element of the iterable, and the result of the function is included in the resulting iterable. 

**Example #6:** use of lambda in map() function

```python

numbers = [1,2,3,4,5,6,7,8,9,10]

squared_numbers = map(lambda x : x **2 ,numbers)

print(list(squared_numbers))

```

[need to add details]

**See also:**

- [Video: How to: use a LAMBDA function as an argument in filter() and map()](https://www.youtube.com/watch?v=xUKmtRJBWuA&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=82)

### Generators

- [Video: How to Use Yield to Generate Values](https://www.youtube.com/watch?v=9p2zcdZD9Jk&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=25)
- [Video: Learn to Generate the Fibonacci Sequence in Python using Generators](https://www.youtube.com/watch?v=oSxiDMrbOV8&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=17)

## True/False (Mark T for True and F for False)

## Multiple Choice (Select the best answer)

What is the output of the following code? [Python Quiz #2]

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

What is the output of the following expression? [Python Quiz #13]

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

What is the output of the following  code? [Python Quiz #14]

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

**What is the output of the following code? [Python Quiz #30]**

**Code:**

```python
def calculate_sum(n):
    if n == 0:
        return 0
    else:
        return n + calculate_sum(n-1)

print(calculate_sum(4))
```

**Options:**

* A) 4
* B) 6
* C) 10
* D) 15


**Watch the video for the answer:** [https://youtube.com/shorts/LQEfGgJYlT4?si=MDvSvVHiBc6hCJ0W](https://youtube.com/shorts/LQEfGgJYlT4?si=MDvSvVHiBc6hCJ0W)

#23 What is the main purpose of a function in Python?

#python #pythonpoll #MCQsTest #yasirbhutta

a) To group a set of related code into a single unit
b) To create a new type of data
c) To write a program in a single line
d) To change the value of global variables
Answer: a) To group a set of related code into a single unit


#22 What is the purpose of the return statement in a function in Python?

#python #pythonpoll #MCQsTest #yasirbhutta

a) To print the output of the function
b) To exit the function and return a value
c) To execute the function without returning anything
d) To stop the function and start a new one

Answer: b) To exit the function and return a value

How can you pass parameters to a function in Python?
a) By listing the parameters after the function name, separated by commas
b) By enclosing the parameters in square brackets
c) By using the global keyword
d) By using the input() function
Answer: a) By listing the parameters after the function name, separated by commas

 #19 What is the output of the following code?

def myfunction(val):
	return val % 4 == 0
print(myfunction (13) or myfunction (8))

Watch the Video Tutorial for the Answer: https://youtu.be/laKpsLlq60I

#python #pythonpoll #MCQsTest #yasirbhutta

0
13
False
True
3.5

What is the correct way to define a function in Python?
a) function my_function():
b) def my_function():
c) define my_function():
d) my_function() {


## Exercises

- Write a function `sum3(num1,num3,num3)` that takes three numbers as input and returns the sum.
- Write a function `SumNum(num1)` that takes a number as input and returns the sum of numbers from 1 to that number (num1).
- Write a function `sumSquares(x)` that takes a vector of numbers as input and returns the sum of their squares.
- Write a function `isEven(x)` that takes a number as input and returns true if it is even, and false otherwise.
- Write a program with three functions:
  
  1. **`isEven(n)`:** This function takes an integer `n` as input and returns `True` if `n` is even and `False` otherwise. You can use the modulo operator (`%`) to check for evenness.
  2. **`printTable(n)`:** This function takes an integer `n` as input and prints its multiplication table. The table should show the product of `n` with each number from 1 to 10, formatted like `n * i = n * i`, where `i` is the current number in the loop.
  3. **`main`:** The main program should:
     - Prompt the user to enter an integer.
     - Use the `isEven(n)` function to check if the entered number is even.
     - If the number is even, call the `printTable(n)` function to print its multiplication table.
     - If the number is odd, print a message indicating the number is odd and not eligible for printing a table.

**Example output:**

```matlab
Enter an integer: 4
4 is even! Here's its multiplication table:
4 * 1 = 4
4 * 2 = 8
4 * 3 = 12
...
4 * 10 = 40
```

- Write a function `avgPositive(data)` that takes a list of numbers as input and returns the average of all positive numbers in the list.

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
