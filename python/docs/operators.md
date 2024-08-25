# Python: Operators


[**Want to Learn Python, Join our WhatsApp Channel ✨:**](https://whatsapp.com/channel/0029VaeGV0517En4iyZGWn2P)

## What is Operators

- Operators in Python are special symbols that perform specific operations on values and variables.
- They are essential for calculations, comparisons, assignments, and logical operations within your code.

## Major operator categories

**1. Arithmetic Operators:**

- Used for performing basic mathematical calculations.
- Operators: `+` (addition), `-` (subtraction), `*` (multiplication), `/` (division), `//` (floor division), `%` (modulo), `**` (exponentiation)

[video: Basic Mathematical Operations with Examples](https://youtu.be/fDul88llyHM)

- Examples:

```python
result = 10 + 5  # Addition
difference = 15 - 7  # Subtraction
product = 4 * 6  # Multiplication
quotient = 12 / 3  # Division
integer_quotient = 17 // 4  # Floor division
remainder = 25 % 4  # Modulo
square = 5 ** 2  # Exponentiation
```

**2. Comparison Operators:**

- Used to compare values and return a Boolean result (True or False).
- Operators: `==` (equal to), `!=` (not equal to), `>` (greater than), `<` (less than), `>=` (greater than or equal to), `<=` (less than or equal to)

- Examples:

```python
is_equal = 7 == 7  # True
is_greater = 12 > 9  # True
is_less_or_equal = 5 <= 5  # True
```

**3. Assignment Operators:**

- Used to assign values to variables.
- Operators: `=` (simple assignment), `+=` (add and assign), `-=` (subtract and assign), `*=` (multiply and assign), `/=` (divide and assign), etc.

- Examples:

```python
x = 10  # Simple assignment
x += 5  # Add 5 to x
x *= 2  # Multiply x by 2
```

**4. Logical Operators:**

- Used to combine Boolean expressions.
- Operators: `and`, `or`, `not`

- Examples:

```python
is_valid = (age >= 18) and (has_license == True)
is_allowed = (is_member) or (has_ticket)
```

**5. Identity Operators:**

- In Python, the `is` operator is used to compare the identities of two objects. It checks whether two references point to the same object in memory, not whether the values of the two objects are equal. 
- Operators: `is`, `is not`

Here's a simple example to illustrate the difference between `is` and `==`:

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # Output: True, because the lists have the same content
print(a is b)  # Output: False, because they are different objects in memory
print(a is c)  # Output: True, because both references point to the same object
```

In this example:
- `a == b` is `True` because the values in both lists are the same.
- `a is b` is `False` because they are two different objects in memory, even though their contents are identical.
- `a is c` is `True` because `c` is assigned to the same object as `a`, so they reference the same memory location.
  
**Example 2**

```python
x = 5
y = 5
result = x is y  # True (they refer to the same integer object)
```

**Important:** In Python, small integers (typically between -5 and 256) are cached and reused. This means that when you assign x = 5 and y = 5, both variables reference the same integer object in memory. This behavior is part of Python's optimization to save memory and improve performance, as small integers are frequently used. [1]

**6. Membership Operators:**

- Used to check if a value is present in a sequence (like a list or string).
- Operators: `in`, `not in`

- Examples:

```python
numbers = [1, 3, 5, 7]
is_present = 5 in numbers  # True
is_missing = 2 not in numbers  # True
```

**7. Bitwise Operators:**

- Used to perform operations on the binary representation of numbers.
- Operators: `&` (bitwise AND), `|` (bitwise OR), `^` (bitwise XOR), `~` (bitwise NOT), `<<` (left shift), `>>` (right shift)
- These are less common in general-purpose programming, but useful in certain domains like low-level programming or cryptography.

## `id()` function

In Python, the `id()` function returns the "identity" of an object, which is a unique integer that serves as a constant for the object during its lifetime. The `id` is often the memory address of the object. Here's a simple example:

```python
x = 10
print(id(x))

y = "hello"
print(id(y))
```

This code will print the unique identifiers for the variables `x` and `y`. If you have specific objects or variables in mind that you would like to see the `id` for, please let me know!

**Python operators examples:**
- [Walrus Operator in Python](https://youtube.com/shorts/vhEz75XZlJI)


## Key Terms

## True/False (Mark T for True and F for False)

**Answer Key (True/False):**

## Multiple Choice (Select the best answer)

1. **Arithmetic Operators:**

**What is the output of the following Python code?** [Python Quiz #2](https://youtube.com/shorts/gz4YuXmZvYo?si=VK50ZYFnvh5WljmT)

```python
x = 10
y = 5

x = x + y
y = x - y
x = x - y

print(x, y)

```
  - A) 5 0
  - B) 5 -5
  - C) 10 5
  - D) 5 10

**Watch this video for answers:** [https://youtube.com/shorts/gz4YuXmZvYo?si=VK50ZYFnvh5WljmT](https://youtube.com/shorts/gz4YuXmZvYo?si=VK50ZYFnvh5WljmT)

**What is the output of the following expression?** [Python Quiz #12](https://youtube.com/shorts/_cHsABqmmcM)

```python
2 ** 3 + 4 // 2 - 1
```
    - A) 8 
    - B) 9 
    - C) 10 
    - D) 11

**Watch this video for the answer:** [https://youtube.com/shorts/_cHsABqmmcM](https://youtube.com/shorts/_cHsABqmmcM)

**What is the output of the following expression?** [Python Quiz #24](https://youtube.com/shorts/-mPZMfg_uJ8?si=F6Hk4m4C_HVmHZ9A)

```python
x = 10
y = 5
print(x % y)
```

- A) 2
- B) 5
- C) 0
- D) 1
  
**Watch this video for the answer:** [https://youtube.com/shorts/-mPZMfg_uJ8?si=F6Hk4m4C_HVmHZ9A](https://youtube.com/shorts/-mPZMfg_uJ8?si=F6Hk4m4C_HVmHZ9A)

**What is the output of the following code?** [Python Quiz #33](https://youtube.com/shorts/weXLcIrx2Ko?si=JlDU0qMLPgYedatJ)

```python
print(11 % 3 == (11 - 3 * (11 // 3)))
```

  - A) True
  - B) False

**Watch the video for the answer:** [https://youtube.com/shorts/weXLcIrx2Ko?si=JlDU0qMLPgYedatJ](https://youtube.com/shorts/weXLcIrx2Ko?si=JlDU0qMLPgYedatJ)

2. **Comparison Operators:**

**What is the output of the following Python code?** [Python Quiz #10](https://youtube.com/shorts/FRa0r4UxyXM)
```python
x = 5
y = 10

result = x > 3 or y < 5
print(result)
```
**A)** True
**B)** False
**C)** SyntaxError
**D)** None of these

**Watch video for the answer:** [https://youtube.com/shorts/FRa0r4UxyXM](https://youtube.com/shorts/FRa0r4UxyXM)


**3. Assignment Operators:**
**4. Logical Operators:**
**5. Identity Operators:**
**6. Membership Operators:**
**7. Bitwise Operators:**

1. **What is the difference between and and or operators in Python?**

   - A) and returns True if both operands are True and or returns True if either operand is True
   - B) and returns True if either operand is True and or returns True if both operands are True
   - C) and returns False if both operands are False and or returns False if either operand is False
   - D) both A and C are correct

Answer: D
  
What is the difference between == and = in Python?

a) == is the comparison operator, = is the assignment operator
b) == is the assignment operator, = is the comparison operator
c) They are the same operator
d) There is no difference

Which operator is used to raise a number to a power?
a. **
b. ^
c. pow()
d. ** and ^ are both correct

What is the result of the expression 3 + 5 * 2 in Python?
a. 16
b. 13
c. 11
d. 26

What is the purpose of the % operator in Python?
a. Exponential
b. Modulus
c. Floor Division
d. Addition

What is the output of 45 // 7?
a. 5.0
b. 6
c. 5
d. 6.428571428571429

Which operator adds a value to a variable?
a. +=
b. -=
c. *=
d. /=

What is the output of x = 10; x //= 3?
a. 3
b. 3.33
c. 3.5
d. 4

Which operator checks if two values are greater than or equal to each other?
a. >
b. <=
c. >=
d. <

What is the result of 5 <= 5?
a. True
b. False
c. 5
d. None of the above

Which operator returns True if both operands are True?
a. and
b. or
c. not
d. xor

What is the output of not (True and False)?
a. True
b. False
c. None
d. Error

Which operator checks if a value is present in a sequence?
a. in
b. not in
c. Both in and not in
d. None of the above

What is the output of 4 in [1, 3, 4]?
a. True
b. False
c. 4
d. Error

Which operator checks if two objects refer to the same memory location?
a. ==
b. is
c. is not
d. Both is and is not

What is the result of x = [1, 2]; y = x; x is y?
a. True
b. False
c. [1, 2]
d. None of the above


Which of these operators can be used to perform bitwise operations on integers in Python? a) & | ^ ~ << >> b) && || ! << >> c) * / % ** // d) + - * /
Answer: a) & | ^ ~ << >>


What is the correct way to use the exponentiation operator in Python?

a) x ^ y b) x ** y c) pow(x, y) d) either b or c

Answer: d) either b or c


#60 In Python, What is the output of this code?

x = 10
y = 5
x = x + y
y = x - y
x = x - y
print(x, y)


a) 10, 5 
b) 5, 10 
c) 15, -5 
d) -5, 15

Answer: b) 5, 10


**Answer key (Mutiple Choice):**

## Fill in the Blanks

**Answer Key (Fill in the Blanks):**

## Exercises

## Review Questions

## References and Bibliography

[1] “Python memory management,” Discussions on Python.org, Apr. 02, 2023. https://discuss.python.org/t/python-memory-management/25391 (accessed Jul. 27, 2024).
‌