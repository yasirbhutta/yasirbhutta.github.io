# Python: Operators

## What is Operators

- Operators in Python are special symbols that perform specific operations on values and variables.
- They are essential for calculations, comparisons, assignments, and logical operations within your code.

## Major operator categories

**1. Arithmetic Operators:**

- Used for performing basic mathematical calculations.
- Operators: `+` (addition), `-` (subtraction), `*` (multiplication), `/` (division), `//` (floor division), `%` (modulo), `**` (exponentiation)

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

- Used to check if two variables refer to the same object in memory.
- Operators: `is`, `is not`

- Examples:

```python
x = 5
y = 5
result = x is y  # True (they refer to the same integer object)
```

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


**Python operators examples:**
- [Walrus Operator in Python](https://youtube.com/shorts/vhEz75XZlJI)

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

## Key Terms

## True/False (Mark T for True and F for False)

**Answer Key (True/False):**

## Multiple Choice (Select the best answer)

1. **What is the difference between and and or operators in Python?**

   - A) and returns True if both operands are True and or returns True if either operand is True
   - B) and returns True if either operand is True and or returns True if both operands are True
   - C) and returns False if both operands are False and or returns False if either operand is False
   - D) both A and C are correct

Answer: D
  
**Watch this video for the answer:**

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
