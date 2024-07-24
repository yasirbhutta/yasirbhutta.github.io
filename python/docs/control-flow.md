# Python: Flow Control Statements

Connect with me: [Youtube](https://www.youtube.com/yasirbhutta) \| [LinkedIn](https://www.linkedin.com/in/yasirbhutta/) \| [WhatsApp Channel](https://whatsapp.com/channel/0029VaC3BC160eBZZSs3CW0c) \| [Web](https://yasirbhutta.github.io/) \| [Facebook](https://www.facebook.com/yasirbhutta786) \| [Twitter](https://twitter.com/yasirbhutta)

- [Download PDF](https://yasirbhutta.github.io/python/docs/control-flow.pdf)  
- To access the updated handouts, please click on the following link:
[https://yasirbhutta.github.io/python/docs/control-flow.html](https://yasirbhutta.github.io/python/docs/control-flow.html)

## Flow control statements

Flow control statements in Python determine the order in which your code is executed. They allow you to make decisions, repeat actions, and control the program's flow based on specific conditions.

1. Conditional Statements (if, else, elif)
2. Looping Statements (for, while)
3. Loop Control Statements (break, continue, pass)
4. Match Statement (Python 3.10+)

## Conditional Statements (if, else, elif)

- The `if` statement in Python is a conditional statement that allows you to execute a block of code only if a certain condition is met.
- Make decisions using `if`, `elif`, and `else` statements.

The general **syntax** of the if statement is as follows:

```python
if condition:
    # code to execute if condition is True
```

The `condition` can be any logical expression. If the condition is evaluated to `true`, the block of `statements` is executed. Otherwise, the block of `statements` is skipped.

Here is a simple example of an if statement in MATLAB:

**Example #:**

```python
x = 10

if x > 5:
    print('x is greater than 5.')
```

This code will print the message `x is greater than 5.` to the console.

You can also use `elif` statements to check for multiple conditions. The general **syntax** of the **elif statement** is as follows:

```python
if condition1:
    # code to execute if condition1 is True
elif condition2:
    # code to execute if condition2 is True
```

If the `condition` for the if statement is evaluated to `false`, the python interpreter will check the `condition` for the first elif statement. If the condition for the elif statement is evaluated to `true`, the corresponding block of `statements` is executed. Otherwise, the python interpreter will check the `condition` for the next elif statement, and so on.

Here is an example of an if statement with an elif statement:

**Example #1:**

```python
x = 3

if x > 5:
    print('x is greater than 5.')
elif x < 5:
    print('x is less than 5.')
```

This code will print the message "x is less than 5." to the console.

You can also use an else statement to check for all other conditions. The general syntax of the else statement is as follows:

```python
if condition1:
    # code to execute if condition1 is True
elif condition2:
    # code to execute if condition2 is True
else:
    # code to execute if none of the conditions are True
```

If all of the conditions for the if and elseif statements are evaluated to `false`, the block of `statements` in the `else` statement is executed.

Here is an example of an if statement with an `elif` statement and an `else` statement:

```python
x = 2

if x > 5:
    print('x is greater than 5.')
elif x == 5:
    print('x is equal to 5.')
else:
    print('x is less than 5.')
```

**Output:**
This code will print the message "x is less than 5." to the console.

### Example 2: Basic If-Else
```python
number = 10

if number > 0:
    print("The number is positive")
else:
    print("The number is not positive")
```
**Explanation**: This code checks if the variable `number` is greater than 0. If true, it prints "The number is positive", otherwise it prints "The number is not positive".

### Example 3: Checking Even or Odd [related video:](https://youtube.com/shorts/za0rSiA33j0)
```python
number = 7

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
```
**Explanation**: This code checks if the variable `number` is even or odd. If `number % 2` equals 0, it is even; otherwise, it is odd.

### Example 4: Age Group Classification
```python
age = 25

if age < 18:
    print("Minor")
else:
    print("Adult")
```
**Explanation**: This code classifies a person as a "Minor" if their age is less than 18, and as an "Adult" otherwise.

### Example 5: Grade Assignment [[video]](https://youtu.be/oEZzg0cUNw8)
```python
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
```
**Explanation**: This code assigns a grade based on the `score`. It uses multiple `elif` statements to check for different score ranges.

### Example 6: Nested If-Else
```python
number = -5

if number >= 0:
    if number == 0:
        print("The number is zero")
    else:
        print("The number is positive")
else:
    print("The number is negative")
```
**Explanation**: This code uses nested `if-else` statements to check if the number is zero, positive, or negative.

### Example 7: Temperature Check
```python
temperature = 30

if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")
```
**Explanation**: This code checks if the temperature is greater than 30. If true, it prints "It's a hot day"; otherwise, it prints "It's not a hot day".

### Example 8: Voting Eligibility [[video]](https://youtu.be/yxS0A5G1MCs)
```python
age = 17

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
```
**Explanation**: This code checks if a person is eligible to vote based on their age. If `age` is 18 or more, it prints "You are eligible to vote"; otherwise, it prints "You are not eligible to vote".

### Example 9: Password Check
```python
password = "password123"

if password == "password123":
    print("Access granted")
else:
    print("Access denied")
```
**Explanation**: This code checks if the `password` is correct. If it matches "password123", it prints "Access granted"; otherwise, it prints "Access denied".

### Example 10: Maximum of Two Numbers
```python
a = 15
b = 20

if a > b:
    print("a is greater than b")
else:
    print("a is not greater than b")
```
**Explanation**: This code checks which number is greater between `a` and `b`. If `a` is greater than `b`, it prints "a is greater than b"; otherwise, it prints "a is not greater than b".

### Example 11: Checking String Length
```python
string = "Hello, World!"

if len(string) > 10:
    print("The string is long")
else:
    print("The string is short")
```
**Explanation**: This code checks if the length of the `string` is greater than 10. If true, it prints "The string is long"; otherwise, it prints "The string is short".

**Example #12:** Using if-elif-else

```python
x = 10

if x < 0:
    print("Negative")
elif x == 0:
    print("Zero")
else:
    print("Positive")
```

- [Video: Use Walrus Operator with if-else (New)](https://www.youtube.com/watch?v=vhEz75XZlJI&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja)
- [Video: How to Write Single-Line Code Instead of If-Else Statements](https://www.youtube.com/watch?v=8qOyRklMr-I&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja)

**Example #:**

- [Python Quiz -IF](https://forms.gle/C71fbbFnDfigs4Dt8)
  
## loops

- There are two ways to create loops in Python: with the for-loop and the while-loop.

- Repeat actions using `for` and `while` loops.

### for loop

- A for loop in Python is a programming statement that repeats a block of code a fixed number of times.
- The for-loop is always used in combination with an iterable object[^1], like a list or a range. 
- The Python for statement iterates over the members of a sequence in order, executing the block each time. 

- [Video: For loops in Python](https://www.youtube.com/watch?v=GIG0SudpPLI&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=89)
  

**Syntax:**

```python
for item in iterable:
    # code block
```

`iterable` is a sequence of elements such as a list, tuple, dictionary, set, or string. item is a variable that takes on the value of each element in the sequence, one at a time. The code block is executed once for each element in the sequence.

**range() function:** 

- We can use the `range()` function as an iterable in a for loop in Python. The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number. 
- We can also specify the starting value and the increment value of the sequence using the range() function. For example, range(2, 10, 2) returns a sequence of numbers starting from 2, incrementing by 2, and ending at 8. [read more ...](https://www.w3schools.com/python/gloss_python_for_range.asp)

**Example #:** Print Numbers from 1 to 5

Question: Write a MATLAB program to print the numbers from 1 to 5, using a for loop.

**Example #:**

```python
for i in range(6):
    print(i)
```

**Example #:** Printing "Building the future, one line at a time." 5 Times Using a for Loop

**Question:** Write a Python program to print the string "Building the future, one line at a time." 5 times, using a for loop.

**Example #:**

```python
for i in range(5):
    print("Building the future, one line at a time.")
```

**Example #:** Sum of Numbers from 1 to N

Question: Write a python program to calculate the sum of the first N natural numbers using a for loop.

```python
N = 10
sum = 0
for i in range(1,N+1):
    sum = sum + i
print(f"Sum = {sum}")
```

**Example #:** Print Even Numbers from 2 to 10

**Question:** Write a Python program to display the even numbers from 2 to 10, inclusive, using a for loop.

```python
sum = 0
for i in range(2,11):
    if i%2 == 0:
        sum +=i
        print(i)
print(f"Sum of even numbers: {sum}")
```

**Example #:** Strings as an iterable

```python
string = "python is versatile"
for x in string:
    print(x)
```

**Example #:** Lists as an iterable

```python
collection = ['python', 5, 'd']
for x in collection:
    print(x)
```

**Example #:** Loop over Lists of lists

```python
list_of_lists = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]
for list in list_of_lists:
    for x in list:
        print(x)
```

- A **nested loop** is a loop inside another loop. It is a powerful programming technique that can be used to solve a wide variety of problems.

**Example #:** Nested Loops - Multiplication Tables

```python
for i in range(1, 11):
    print(f"Multiplication table of {i}")
    for j in range(1, 11):
        print('%d * %d = %d' % (i, j, i*j))
```

**for loop examples:**

- [Video: String as an iterable](https://www.youtube.com/watch?v=uC0bbj08d4A)
- [Video: 6 Ways to use List in For loop in Python](https://www.youtube.com/watch?v=-FErgsl9njQ)
- [Video: Underscore to Ignore Values in for loop](https://www.youtube.com/watch?v=bZOgrIHCHbQ&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=2)
- [How to Print Multiplication Tables in Python](https://www.youtube.com/watch?v=wqtVGYn7NpQ&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=41)
- [String as an iterable using for loop](https://youtu.be/uC0bbj08d4A)
- [Calculate the sum of the first N natural numbers](https://youtu.be/FgMHDLRi_G4)
  
**Further reading:**
 
- [For loop - Python wiki](https://wiki.python.org/moin/ForLoop)

#### while loop

- A while loop in python is a control flow statement that repeatedly executes a block of code until a specified condition is met.

**Syntax:**

```python
while condition:
    # code block
```

Here, condition is a boolean expression that is evaluated before each iteration of the loop. If the condition is `True`, the code block is executed. The loop continues to execute as long as the condition remains True.

**Example #:** Print numbers from 1 to 10 using while loop

Question: Write a Python program to print the numbers from 1 to 10, using a while loop?

```python
count = 1  # Start counting at 1
while count <= 10:  # Keep counting as long as we're less than or equal to 10
    print(count)  # Print the current number
    count += 1  # Add 1 to the count for the next round
```

**Example #:** Print "Hello, world!" 5 times using while loop

Question: Write a Python program to print the string "Hello, world!" 5 times, using a while loop?

```python
i = 1
while i <= 10:
    print('Hello, world!')
    i += 1
```

**Example #:** Sum of numbers from 1 to 100 using while loop

Question: Write a MATLAB program to calculates the sum of the numbers from 1 to 100 using a while loop.

```python
i = 1
sum = 0

while i <= 100:
    sum += i
    i += 1 

print(f'Sum = {sum}');
```

**Example #:** Sum of even numbers from 2 to 20 using while loop

Question: Write a Python program to calculate the sum of the even numbers from 2 to 20 using a while loop.

```python
sum = 0  # Initialize a variable to store the sum
number = 1  

while number <= 20:
    if number%2 == 0:
      sum += number  # Add the current number to the sum
    number += 1

print(f'The sum of even numbers from 1 to 20 is: {sum}')

```

**Example:** Square of numbers less than 5 using while loop

Question : Write a program that prints the sum of the squares of all the numbers from 1 to 4, using a while loop.

```python
i = 1
while i < 5:
    square = i ** 2
    print(f'Square of {i} is {square}')
    i += 1
```

**Output:**

```python
Square of 1 is 1
Square of 2 is 4
Square of 3 is 9
Square of 4 is 16
```

**Example #:**

Question: Write a Python program to prompt the user to enter lines of text until the user enters a blank line. The program should then display the message "You entered a blank line.".

```python
inputStr = 'Start';

while inputStr != "":
  inputStr = input("Enter a line of text:")

print('You entered a blank line.')
```

**Example:** Sum of given numbers till the number entered is zero

Question: Write a Python program to add all the numbers entered by the user until the user enters zero. The program should display the sum of the numbers.

```python
sum = 0; # Initialize the sum

# Prompt the user to enter a number
number = int(input('Enter a number: ')) # int() Convert string input to integer

# While the number entered is not zero, add the number to the sum and prompt the user to enter another number
while number != 0:
    sum += number
    number = int(input('Enter another number: ')) # int() Convert string input to integer
    
# Display the sum of the numbers
print(f'The sum of the numbers is: {sum}')
```

**Example :** While loop from 1 to infinity, therefore running forever.

```python
x = 1
while True:
    print("To infinity and beyond! We're getting close, on %d now!" % (x))
    x += 1
```

**while loop examples:**

- [How to Count Digits in a Positive Integer using Python](https://www.youtube.com/watch?v=33n-lb1Ujp4&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=48)
- [How to Count Occurrence of a Specific Digit in a Number using Python](https://www.youtube.com/watch?v=MXWbTdvSBVs&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=47)
  
**See also:**

- [Video: Learn how to use while loops](https://www.youtube.com/watch?v=zF-x4JBgn4A&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=50)
- [Video: Learn how to use INFINITE while loop](https://www.youtube.com/watch?v=4qZyBEKSfaA&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=49)
- [Video: Python while loop](https://www.youtube.com/watch?v=ieU3ZRSZVf8&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=86)

## The Range() function

- [Video: The range() Function](https://www.youtube.com/watch?v=cRa_nnO6L00&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=87)
- [Video: Use of range() in for loop](https://www.youtube.com/watch?v=ZEVsokTGbwA&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=88)

## Loop Control Statements (break, continue, pass)
These statements modify the behavior of loops.

**break:** Terminates the loop entirely.
**continue:** Skips the current iteration and moves to the next one.
**pass:** Does nothing, often used as a placeholder.

`break`

Exits the loop prematurely.

```python
for item in sequence:
    if some_condition:
        break  # exit the loop
```

`continue`

Skips the current iteration and proceeds to the next iteration of the loop.

```python
for item in sequence:
    if some_condition:
        continue  # skip the rest of the code in this iteration
    # code to execute if some_condition is False
```

`pass`

A null statement, used as a placeholder.

```python
if condition:
    pass  # do nothing
```

**Example #:**

```python
for x in range(3):
    if x == 1:
        break
```

**Example #:**

```python
for i in range(10):
    if i == 5:
        break  # exit the loop when i is 5
    if i % 2 == 0:
        continue  # skip even numbers
    print(i)  # print only odd numbers less than 5
```

- [Video: How to Effectively Use Break and Continue Statements](https://www.youtube.com/watch?v=LfF9CsyVRgU&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=68)
- [Video: Using Python break statement with a while loop](https://www.youtube.com/watch?v=KWuyQ7HQUBE&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=85)
  

## The else Clauses on Loops

**Example #:** for..else

```python
for x in range(3):
    print(x)
else:
    print('Final x = %d' % (x))
```

## Match Statement (Python 3.10+)

The match statement offers a more concise way to handle multiple comparison cases.

```python
def get_fruit_color(fruit):
    match fruit:
        case "apple":
            return "red"
        case "banana":
            return "yellow"
        case _:
            return "unknown"
```

**Python Challenge to test your knowledge:** [Quiz1](https://www.youtube.com/watch?v=9Zw-LuNX9h0&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=25) \| [Quiz2](https://www.youtube.com/watch?v=x7CIxqoqccY&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=24) \| [Quiz3](https://www.youtube.com/watch?v=XNLL6j-P61A&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=23) \| [Quiz4](https://www.youtube.com/watch?v=zdLNmwO1u8Y&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=22) \| [Quiz5](https://www.youtube.com/watch?v=ExDu2lwjd3c&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=7)

## Key Terms

- for 
- while
- range
- pass
- else
- match
- break
- continue
- f-string

## True/False (Mark T for True and F for False)

## Multiple Choice (Select the best answer)

**if statement:**

1. **Which of the following correctly represents the syntax of an if statement in Python?**
    - A) if condition { block of code }
    - B) if(condition) { block of code }
    - C) if condition: block of code
    - D) None

2. **What is the syntax for a simple if statement in Python?**
    - A) if x == 10:
    - B) for x in range(10):
    - C) while x < 10:
    - D) if (x == 10) then:

3. **What is the purpose of the else block in an if statement?**

A) To execute a code block when the if condition is True
B) To execute a code block when the if condition is False
C) To create an infinite loop
D) To define a function

4. **What happens when none of the conditions in an if-elif-else chain are True, and there is no else block?**

A) The program raises an error.
B) The program executes the first if block.
C) The program executes the last elif block.
D) The program does nothing and continues to the next statement.

5. **What will be the output of the following code?**

```python
x = 10
y = 5
if x < y:
    print("x is greater than y")
```
A) "x is greater than y"
B) "x is less than y"
C) Nothing will be printed
D) An error will occur

6. **What happens if none of the conditions in an if-elif chain are True, and there is no else block?**

A) The program raises an error
B) The program executes the first if block
C) The program does nothing and continues to the next statement
D) The program executes the last elif block

7. **What will be the output of the following code?**

```python
number = 10
if number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")
```
A) Number is odd
B) Number is even
C) Nothing
D) Error

8. **Which of the following is the correct way to compare if two variables are equal in an if statement?**
A) if x equals 5:
B) if x == 5:
C) if x = 5:
D) if x := 5:

9. **How can you check if a value is NOT equal to 10 in an if statement?**
A) if x != 10:
B) if x <> 10:
C) if x =! 10:
D) if x not 10:

10. **What does the following code snippet do?**
```python
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")

```
A) Prints "Positive" if x is greater than 0, "Negative" if x is less than 0, and "Zero" if x is 0.
B) Prints "Positive" if x is less than 0, "Negative" if x is greater than 0, and "Zero" if x is 0.
C) Prints "Positive" if x is 0, "Negative" if x is greater than 0, and "Zero" if x is less than 0.
D) Causes an error because the conditions are conflicting.

2. **What is the correct syntax for an if-else statement?**
   - A) if condition:
            code block
   - B) if condition:
            code block
        else:
            code block
   - C) if condition:
            code block
        elif condition:
            code block
   - D) if condition:
            code block
        else:
            code block
        elif condition:
            code block

4. **What happens if none of the conditions in an if-elif-else block are true?**
   * a) The program terminates
   * b) The else block is executed
   * c) An error occurs
   * d) The program continues without executing any block

8. **What will be the output of the following code?**
   ```python
   x = 10
   if x > 5 and x < 15:
       print("x is between 5 and 15")
   else:
       print("x is not between 5 and 15")
   ```
   * a) x is between 5 and 15
   * b) x is not between 5 and 15
   * c) Error
   * d) No output

9. **What will be the output of the following code?**
   ```python
   num = 7
   if num % 2 == 0:
       print("Even")
   else:
       print("Odd")
   ```
   * a) Even
   * b) Odd
   * c) Error
   * d) No output

10. **What will be the output of the following code?**
   ```python
   score = 85
   if score >= 90:
       print("A")
   elif score >= 80:
       print("B")
   else:
       print("C")
   ```

What is the output of the following code?

```python
x = 5
if x > 10:
    print("Greater than 10")
elif x > 5:
    print("Greater than 5 but not greater than 10")
else:
    print("5 or less")
```

A) Greater than 10  
B) Greater than 5 but not greater than 10  
C) 5 or less  
D) No output

**Answer:** C

Which of the following is true about the `elif` statement?

A) `elif` stands for "else if" and is used to check additional conditions after the `if` statement  
B) `elif` is the same as `else`  
C) `elif` must be followed by an `else` statement  
D) You can have multiple `elif` statements in one block

**Answer:** A, D

What will be the output of the following code?

```python
y = 20
if y < 20:
    print("Less than 20")
elif y == 20:
    print("Equal to 20")
else:
    print("Greater than 20")
```

A) Less than 20  
B) Equal to 20  
C) Greater than 20  
D) None of the above

**Answer:** B

What will be the output of the following code snippet?

```python
a = 10
b = 5
if a > b:
    if a > 0:
        print("a is positive")
    else:
        print("a is non-positive")
else:
    print("a is less than or equal to b")
```

A) a is positive  
B) a is non-positive  
C) a is less than or equal to b  
D) No output

**Answer:** A

Which of the following statements is false about `if-elif-else` statements in Python?

A) `elif` statements are optional in an `if-elif-else` construct  
B) An `if` statement can be followed by multiple `elif` statements  
C) An `else` statement is mandatory in an `if-elif-else` construct  
D) An `if` statement can exist without `elif` or `else`

**Answer:** C

What will be the output of the following code?

```python
x = 0
if x:
    print("True")
else:
    print("False")
```

A) True  
B) False  
C) No output  
D) Error

**Answer:** B

**Truthy and Falsy Values in Python**
In Python, certain values are considered False when evaluated in a boolean context (like in an if statement). These values include:

- None
- False
- 0 (zero of any numeric type, including 0.0)
- Empty sequences and collections (e.g., '', (), [], {})
- Any object that implements __bool__ or __len__ to return False or 0, respectively

Which of the following expressions can be used in an `if` condition to check if a number `n` is between 1 and 100 inclusive?

A) `if n > 1 and n < 100:`  
B) `if n >= 1 and n <= 100:`  
C) `if 1 <= n <= 100:`  
D) `if n == 1 or n == 100:`

**Answer:** B, C

What will be the output of the following code?

```python
z = 7
if z < 5:
    print("Less than 5")
elif z == 10:
    print("Equal to 10")
elif z > 5:
    print("Greater than 5 but not 10")
else:
    print("Something else")
```

A) Less than 5  
B) Equal to 10  
C) Greater than 5 but not 10  
D) Something else

**Answer:** C

What is the purpose of the `else` statement in an `if-elif-else` structure?

A) To check another condition if the previous ones were false  
B) To execute a block of code if none of the previous conditions were true  
C) To execute a block of code if the previous conditions were true  
D) To end the `if-elif-else` structure

**Answer:** B

What will be the output of the following code?

```python
x = 10
if x > 5:
    if x == 10:
        print("x is 10")
    else:
        print("x is greater than 5 but not 10")
else:
    print("x is 5 or less")
```

A) x is 10  
B) x is greater than 5 but not 10  
C) x is 5 or less  
D) No output

**Answer:** A

Which of the following is correct syntax for an `if-elif-else` statement in Python?

A) 
```python
if x > y:
print("x is greater")
elif x == y:
print("x is equal to y")
else:
print("x is less")
```
B) 
```python
if x > y:
    print("x is greater")
elif x == y:
    print("x is equal to y")
else:
    print("x is less")
```
C) 
```python
if (x > y):
    print("x is greater")
elif (x == y):
    print("x is equal to y")
else:
    print("x is less")
```
D) 
```python
if x > y:
    print("x is greater")
elif x == y
    print("x is equal to y")
else
    print("x is less")
```

**Answer:** B, C

What will be the output of the following code?

```python
a = 3
b = 4
if a > b:
    print("a is greater")
elif a == b:
    print("a and b are equal")
else:
    print("b is greater")
```
A) a is greater  
B) a and b are equal  
C) b is greater  
D) No output

**Answer:** C

Which of the following statements will execute if `n = 7`?

```python
if n < 5:
    print("n is less than 5")
elif n < 10:
    print("n is less than 10")
else:
    print("n is 10 or more")
```

A) n is less than 5  
B) n is less than 10  
C) n is 10 or more  
D) None of the above

**Answer:** B

### Question 5
Which keyword is used to check an additional condition if the initial `if` statement is `False`?

A) else  
B) elif  
C) elseif  
D) if

**Answer:** B

What will be the output of the following code?

```python
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
```

A) Grade: A  
B) Grade: B  
C) Grade: C  
D) Grade: F

What is the result of the following code?

```python
x = 0
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
```

A) Positive  
B) Zero  
C) Negative  
D) No output

**Answer:** B


How many `elif` clauses can be included in an `if-elif-else` statement?

A) One  
B) Two  
C) Unlimited  
D) None

**Answer:** C


What will be the output of the following code?

```python
age = 20
if age < 18:
    print("Minor")
elif age >= 18 and age < 65:
    print("Adult")
else:
    print("Senior")
```

A) Minor  
B) Adult  
C) Senior  
D) No output

**Answer:** B


**for loop:**

> What is the output of the following code?

```python
fruits = ["Apple", "Banana", "Cherry"]
for i, fruit in enumerate(fruits):
    if i == 1:
        print(fruit)
```
1. [ ] Apple
2. [ ] Banana
3. [ ] Cherry
4. [ ] Error

related video: [https://youtu.be/-FErgsl9njQ](https://youtu.be/-FErgsl9njQ)

> What is the correct syntax for a for loop in Python?

1. [ ] for (int i = 0; i < 10; i++):
2. [ ] for i in range(10):
3. [ ] for i = 0 to 9:
4. [ ] for i in 10:

What will be the output of the following code?

```python
for i in range(5):
  print(i * 2)
```

a) 0 1 2 3 4
b) 2 4 6 8 10
c) 10 8 6 4 2
d) 0 2 4 6 8

How many times will the following loop execute?

for i in [1, 2, 3, 3]:
  print("Hello")

a) 3
b) 4
c) 1
d) Infinitely

What is the primary purpose of a for loop in Python?
a. To define a function
b. To iterate over a sequence
c. To create a conditional statement
d. To perform mathematical operations

In Python, what does the range() function do when used in a for loop?
a. Generates a sequence of numbers
b. Defines a list
c. Calculates the average
d. Determines the length of a string

How is the syntax for a for loop in Python?
a. for x in range(10):
b. while x < 10:
c. loop for x in 10:
d. for x = 0; x < 10; x++:

In a for loop, what is the role of the loop variable?
a. It is used to define the loop
b. It holds the result of the loop
c. It is the counter for the loop iterations
d. It is optional and can be omitted

Which of the following is the correct way to iterate over elements in a list using a for loop?
a. for item in my_list:
b. for i = 0; i < len(my_list):
c. for element = my_list:
d. for (i, item) in enumerate(my_list):

How can you iterate over both the index and elements of a list using a for loop?
a. for i in my_list:
b. for (i, element) in enumerate(my_list):
c. for element in range(my_list):
d. for index, element in my_list:

What is the output of the following code?

```python
numbers = [1, 2, 3, 4, 5]
for x in numbers:
    print(x * 2)
```

a. 2 4 6 8 10
b. 1 2 3 4 5
c. 1 4 9 16 25
d. 2 4 8 16 32

**while loop**

What is the output of the following code?

```python
count = 0
while count < 3:
    print(count)
    count += 1
```
(a) 0 1 2
(b) 0 1
(c) 1 2 3
(d) The code will run indefinitely.

What will happen if you try to modify the loop variable within the body of a while loop?

(a) The loop will continue as normal.
(b) The loop will terminate immediately.
(c) The loop may behave unexpectedly, depending on how the variable is modified.
(d) The loop will always run indefinitely.

What is the correct syntax for a while loop in Python?

(a) while (condition):
(b) while condition {}
(c) while condition:
(d) while (condition) {}

What is the output of the following code?

```python
x = 10
while x > 0:
    print(x)
    x -= 2
```

(a) 10 8 6 4 2
(b) 9 7 5 3 1
(c) 10 9 8 7 6
(d) The code will run indefinitely.

What is the purpose of the else clause in a while loop?

(a) To execute a block of code if the loop condition is never true.
(b) To execute a block of code if the loop completes without being terminated by a break statement.
(c) To execute a block of code if the loop encounters an error.
(d) The else clause cannot be used with a while loop.

## Exercises

**if statement**


## Review Questions

**for loop:**
- What is the difference between a for loop and a while loop in Python?
- Can you use a for loop to iterate over a string?

**if statement:**

- Can you have multiple elif blocks in an if-elif-else statement?
- What is the purpose of nesting if statements?
- 
## References and Bibliography

[^1]: In Python, an iterable object is an object that you can loop over using a "for" loop. It's any object that can return its elements one at a time.


**Which of the following correctly fixes the syntax error in the code below?**

```python
if x == 10  # Missing colon
    print("x is 10")
```

A) Remove the comment.
B) Add a colon after `if x == 10`.
C) Add parentheses around `x == 10`.
D) Indent the print statement correctly.

**Which of the following will NOT cause a syntax error in Python?**

A)
```python
1st_variable = 10
```

B)
```python
if x == 10:
print("x is 10")
```

C)
```python
print("Hello World!"
```

D)
```python
print "Hello World!)
```