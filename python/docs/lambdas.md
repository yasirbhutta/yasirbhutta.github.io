# Python Anonymous (Lambda) Functions

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

## Key Terms

## True/False (Mark T for True and F for False)

**Answer Key (True/False):**

## Multiple Choice (Select the best answer)

1. **Which function would you use to determine the type of a variable in Python?**
   - A) id()
   - B) type()
   - C) str()
   - D) isinstance()
  
**Watch this video for the answer:**

#10 Python supports the creation of anonymous functions at runtime, using a construct called 

Python YouTube Playlist: https://www.youtube.com/playlist?list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja

a) pi
b) anonymous
c) lambda
d) none of the mentioned

What is the syntax for defining a lambda function in Python?
A) lambda x: x + 1
B) def x(lambda): return x + 1
C) func x = lambda: x + 1
D) x lambda x + 1
Answer: A) lambda x: x + 1

Related video 
https://youtu.be/Z8Zeen4WwJQ

What is the output of the following code?
f = lambda x, y: x * y
print(f(3, 4))

related video: https://youtu.be/Z8Zeen4WwJQ

A) 12
B) 7
C) '34'
D) None
Answer: A) 12

Related video: https://youtu.be/Z8Zeen4WwJQ

What is the output of the following code?
g = lambda x: x ** 2
print(g(5))
A) 25
B) 5
C) '5'
D) None
Answer: A) 25
related video 
https://youtu.be/Z8Zeen4WwJQ


**Answer key (Mutiple Choice):**

## Fill in the Blanks

**Answer Key (Fill in the Blanks):**

## Exercises

## Review Questions

## References and Bibliography
