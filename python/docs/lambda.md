# Python

## Anonymous (Lamdba) Functions

- A lambda function in Python is a small, anonymous function that can be defined without name.
- Lamdba functions are used to write functions consisting of a single statement.
- A lambda function can take any number of arguments, but can only have one expression.
- It is created using the 'lambda' keyword, and it is often used as an argument to a higher-order function (a function that takes another function as an argument).

### Syntax

The syntax of a lambda is

> lambda arguments:express

### Example #1

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

### Example # 2 multiple two numbers

use of lambda function to multiple two numbers

```python
mul = lambda a, b : a * b
print(mul(2,4)) # 8
```

### Example # 3 

```python 
lambda x, y : x + y

_(6,8) # 14
```

**Note:** In the interactive interpreter, the single underscore**(_)** is bound to the last expression evalued. 

### Example # 4 Immediately invoked function expression

```python
(lambda x, y : x + y)(6,8) # 14
```
The lambda function above is defined and then immediately called with two arguments (6,8). it retuns the value **14**, which is the sum of the arguments.

Filter()

- In Python, the 'filter()' function is used to filter a sequence (e.g. list, tuple, etc.) by applying a certain test to each eleent of the sequence and returning only the elements that pass the test.
- The 'filter()' function takes two arguments: function and an iterable. The function is applied to each element of the iterable, and if the function retuns 'True' for that element, the element is included in the resulting iterable.

### Example #5 use of lambda in filter() function

```python

numbers = [1,2,3,4,5,6,7,8,9,10] # list

even_numbers= list(filter(lambda x : x % 2 == 0,numbers))

print(even_numbers)

```
Map()

- In Python, the 'map()' function is used to apply a certain function to each element of an iterable (e.g. list, tuple, etc.) and return an iterable containing the results.
- The 'map()' function takes two arguments: a function and an iterable. The function is applied to each element of the iterable, and the result of the function is included in the resulting iterable. 

### Example #6 use of lambda in map() function

```python

numbers = [1,2,3,4,5,6,7,8,9,10]

squared_numbers = map(lambda x : x **2 ,numbers)

print(list(squared_numbers))

```
[need to add details]

### Example # 6

```python
def multiply(lambda(x,y):
    retun x*y

result = (lambda x,y : multiply(x,y))(5,3) 
print(result) # Output: 15

mult = lambda x,y : multiply(x,y)
result = mult(6,2)
print(result) # Output: 12
```
