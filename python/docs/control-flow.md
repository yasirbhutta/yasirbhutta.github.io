# 5. Python: Flow Control Statements

Connect with me: [Youtube](https://www.youtube.com/yasirbhutta) \| [LinkedIn](https://www.linkedin.com/in/yasirbhutta/) \| [WhatsApp Channel](https://whatsapp.com/channel/0029VaC3BC160eBZZSs3CW0c) \| [Web](https://yasirbhutta.github.io/) \| [Facebook](https://www.facebook.com/yasirbhutta786) \| [Twitter](https://twitter.com/yasirbhutta)

- [Download PDF](https://yasirbhutta.github.io/python/docs/control-flow.pdf)  
- To access the updated handouts, please click on the following link:
[https://yasirbhutta.github.io/python/docs/control-flow.html](https://yasirbhutta.github.io/python/docs/control-flow.html)

[**Want to Learn Python, Join our WhatsApp Channel ✨:**](https://whatsapp.com/channel/0029VaeGV0517En4iyZGWn2P)

- [5. Python: Flow Control Statements](#5-python-flow-control-statements)
  - [5.1 Flow control statements](#51-flow-control-statements)
  - [5.2 Conditional Statements (if, else, elif)](#52-conditional-statements-if-else-elif)
    - [Example #5.1:](#example-51)
    - [Example #5.2: Basic If-Else](#example-52-basic-if-else)
    - [Example #5.3: Checking Even or Odd](#example-53-checking-even-or-odd)
    - [Example #5.4: Age Group Classification](#example-54-age-group-classification)
    - [Example #5.5: Grade Assignment](#example-55-grade-assignment)
    - [Example #5.6: Voting Eligibility \[video\]](#example-56-voting-eligibility-video)
    - [Example #5.7: Nested If-Else](#example-57-nested-if-else)
    - [Example #5.8: Temperature Check](#example-58-temperature-check)
    - [Example #5.9: Checking String Length](#example-59-checking-string-length)
    - [Task #5.1: Password Check](#task-51-password-check)
    - [Task #5.2: Compare Two Numbers in Python](#task-52-compare-two-numbers-in-python)
    - [Task #5.3: Determine if a Number is Negative, Zero, or Positive](#task-53-determine-if-a-number-is-negative-zero-or-positive)
    - [Task #5.4: Compare Two Input Numbers](#task-54-compare-two-input-numbers)
    - [Task #5.5: Age Checker](#task-55-age-checker)
    - [Task #5.6: Divisibility Check](#task-56-divisibility-check)
    - [Task #5.7: Voting Eligibility Check](#task-57-voting-eligibility-check)
  - [5.3 loops](#53-loops)
    - [5.3.1 for loop](#531-for-loop)
      - [Example #5.8](#example-58)
      - [**Example #5.9:** Print Numbers from 1 to 5](#example-59-print-numbers-from-1-to-5)
      - [Example #5.10: Printing "Building the future, one line at a time." 5 Times Using a for Loop](#example-510-printing-building-the-future-one-line-at-a-time-5-times-using-a-for-loop)
      - [Example #5.11: Sum of Numbers from 1 to N](#example-511-sum-of-numbers-from-1-to-n)
      - [Task #5.8: Sum of Numbers in a Range](#task-58-sum-of-numbers-in-a-range)
      - [Task #5.9: Display Even Numbers in a Range](#task-59-display-even-numbers-in-a-range)
      - [Example #5.11: Print Even Numbers from 2 to 10 and sum of even numbers](#example-511-print-even-numbers-from-2-to-10-and-sum-of-even-numbers)
      - [Task #5.11: Display Multiplication Tables\*\*](#task-511-display-multiplication-tables)
      - [Example #5.12: String as an iterable](#example-512-string-as-an-iterable)
      - [Example #5.13: Lists as an iterable](#example-513-lists-as-an-iterable)
      - [Example #5.14: Loop over Lists of lists](#example-514-loop-over-lists-of-lists)
      - [Example #5.15 Nested Loops - Multiplication Tables](#example-515-nested-loops---multiplication-tables)
      - [Why We Use Variables in For Loops](#why-we-use-variables-in-for-loops)
      - [Example #5.16: Loop Through a List of Fruits in Python](#example-516-loop-through-a-list-of-fruits-in-python)
      - [Use of underscore in 'For Loop'](#use-of-underscore-in-for-loop)
        - [Example #5.17: Using an Underscore in a Loop to Print "Hello" Multiple Times](#example-517-using-an-underscore-in-a-loop-to-print-hello-multiple-times)
    - [5.3.2 while loop](#532-while-loop)
      - [Example #5.18: Print numbers from 1 to 10 using while loop](#example-518-print-numbers-from-1-to-10-using-while-loop)
      - [Example #5.19: Print "Hello, world!" 5 times using while loop](#example-519-print-hello-world-5-times-using-while-loop)
      - [Task #5.12: Display Multiplication Tables\*\*](#task-512-display-multiplication-tables)
      - [Task #5.13: Sum Integers from 1 to 100 Using While Loop](#task-513-sum-integers-from-1-to-100-using-while-loop)
      - [Example #5.20: Sum of even numbers from 2 to 20 using while loop](#example-520-sum-of-even-numbers-from-2-to-20-using-while-loop)
      - [Task #5.14: Calculate Squares of Numbers from 1 to 4 Using While Loop](#task-514-calculate-squares-of-numbers-from-1-to-4-using-while-loop)
      - [Example #5.21: Prompt User for Input Until Blank Line is Entered](#example-521-prompt-user-for-input-until-blank-line-is-entered)
      - [Example #5.22: Sum User-Entered Numbers Until Zero is Entered](#example-522-sum-user-entered-numbers-until-zero-is-entered)
      - [Task #5.15: Sum User-Entered Numbers Until a Negative Number is Entered](#task-515-sum-user-entered-numbers-until-a-negative-number-is-entered)
      - [Task #14: Number Guessing Game](#task-14-number-guessing-game)
      - [Example #24: Infinite Loop Printing Messages with Counter](#example-24-infinite-loop-printing-messages-with-counter)
    - [Loop Control Statements (break, continue, pass)](#loop-control-statements-break-continue-pass)
      - [`break`](#break)
      - [`continue`](#continue)
      - [`pass`](#pass)
  - [Example #: Using Break Statement in a Loop with Range](#example--using-break-statement-in-a-loop-with-range)
      - [Example 1: Exit a loop when a number is found](#example-1-exit-a-loop-when-a-number-is-found)
      - [Example 2: Password validation with `while` loop](#example-2-password-validation-with-while-loop)
    - [Example 1: Skip even numbers using `continue` Statement](#example-1-skip-even-numbers-using-continue-statement)
      - [Example 2: **Temperature Monitoring**](#example-2-temperature-monitoring)
    - [Example 1: **Data Cleaning using `continue` Statement**](#example-1-data-cleaning-using-continue-statement)
    - [**Task: Coffee Machine Stock Check using `break` Statement**](#task-coffee-machine-stock-check-using-break-statement)
    - [The else Clauses on Loops](#the-else-clauses-on-loops)
      - [Example with a `for` loop](#example-with-a-for-loop)
    - [**3. Combined Example**](#3-combined-example)
      - [Example with a `while` loop](#example-with-a-while-loop)
      - [Why Use the `else` Clause with Loops?](#why-use-the-else-clause-with-loops)
      - [Example #: for..else](#example--forelse)
  - [Match Statement (Python 3.10+)](#match-statement-python-310)
  - [Key Terms](#key-terms)
  - [Fix the errors in Python](#fix-the-errors-in-python)
    - [Question:](#question)
    - [Answer:](#answer)
    - [Fixed Code:](#fixed-code)
    - [Explanation:](#explanation)
  - [True/False (Mark T for True and F for False)](#truefalse-mark-t-for-true-and-f-for-false)
  - [Multiple Choice (Select the best answer)](#multiple-choice-select-the-best-answer)
    - [if statement (MCQs)](#if-statement-mcqs)
    - [for loop (MCQs)](#for-loop-mcqs)
    - [Question 4](#question-4)
    - [Question 6](#question-6)
    - [while loop (MCQs)](#while-loop-mcqs)
    - [Loop Control Statements (break, continue, pass) (MCQs)](#loop-control-statements-break-continue-pass-mcqs)
  - [Exercises](#exercises)
    - [For loop Exercises](#for-loop-exercises)
    - [While loop Exercises](#while-loop-exercises)
    - [Loop Control Statements (break, continue, pass) Exercises](#loop-control-statements-break-continue-pass-exercises)
  - [Mini Projects](#mini-projects)
    - [Project #1: Simple Calculator](#project-1-simple-calculator)
  - [Review Questions](#review-questions)
  - [References and Bibliography](#references-and-bibliography)
  - [**Appendices**](#appendices)
    - [\*\*Appendix A:](#appendix-a)

## 5.1 Flow control statements

Flow control statements in Python determine the order in which your code is executed. They allow you to make decisions, repeat actions, and control the program's flow based on specific conditions.

**Python has three types of control structures:**

1. Sequential: Default mode
2. Selection: Used for decisions and branching
3. Repetition: Used for looping, i.e., repeating a code multiple times.

for more details, see [Understanding Control Structures in Python](../posts/control-structures-python.md)

**Flow control statements in Python**

1. Conditional Statements (if, else, elif)
2. Looping Statements (for, while)
3. Loop Control Statements (break, continue, pass)
4. Match Statement (Python 3.10+)

## 5.2 Conditional Statements (if, else, elif)

- The `if` statement in Python is a conditional statement that allows you to execute a block of code only if a certain condition is met.
- Make decisions using `if`, `elif`, and `else` statements.

The general **syntax** of the if statement is as follows:

```python
if condition:
    # code to execute if condition is True
```

The `condition` can be any logical expression. If the condition is evaluated to `true`, the block of `statements` is executed. Otherwise, the block of `statements` is skipped.

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1602443888929206"
     crossorigin="anonymous"></script>
<ins class="adsbygoogle"
     style="display:block"
     data-ad-format="fluid"
     data-ad-layout-key="-gw-3+1f-3d+2z"
     data-ad-client="ca-pub-1602443888929206"
     data-ad-slot="6771715491"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

Here is a simple example of an if statement in PYTHON:

### Example #5.1:

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

### Example #5.2: Basic If-Else

```python
number = 10

if number > 0:
    print("The number is positive")
else:
    print("The number is not positive")
```
**Explanation**: This code checks if the variable `number` is greater than 0. If true, it prints "The number is positive", otherwise it prints "The number is not positive".

### Example #5.3: Checking Even or Odd 

[related video:](https://youtube.com/shorts/za0rSiA33j0)

```python
number = 7

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
```
**Explanation**: This code checks if the variable `number` is even or odd. If `number % 2` equals 0, it is even; otherwise, it is odd.

### Example #5.4: Age Group Classification

```python
age = 25

if age < 18:
    print("Minor")
else:
    print("Adult")
```
**Explanation**: This code classifies a person as a "Minor" if their age is less than 18, and as an "Adult" otherwise.

### Example #5.5: Grade Assignment 

[realted video](https://youtu.be/oEZzg0cUNw8)

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

### Example #5.6: Voting Eligibility [[video]](https://youtu.be/yxS0A5G1MCs)

```python
age = 17

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
```
**Explanation**: This code checks if a person is eligible to vote based on their age. If `age` is 18 or more, it prints "You are eligible to vote"; otherwise, it prints "You are not eligible to vote".

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1602443888929206"
     crossorigin="anonymous"></script>
<ins class="adsbygoogle"
     style="display:block"
     data-ad-format="fluid"
     data-ad-layout-key="-gw-3+1f-3d+2z"
     data-ad-client="ca-pub-1602443888929206"
     data-ad-slot="6771715491"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

### Example #5.7: Nested If-Else

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

### Example #5.8: Temperature Check

```python
temperature = 30

if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")
```
**Explanation**: This code checks if the temperature is greater than 30. If true, it prints "It's a hot day"; otherwise, it prints "It's not a hot day".

### Example #5.9: Checking String Length

```python
string = "Hello, World!"

if len(string) > 10:
    print("The string is long")
else:
    print("The string is short")
```

**Explanation**: This code checks if the length of the `string` is greater than 10. If true, it prints "The string is long"; otherwise, it prints "The string is short".

### Task #5.1: Password Check

**Objective**: Write a Python program that checks if the provided password matches 
the correct password and prints an appropriate message.

**Instructions:**
1. Define a variable `password` and set it to a string value.
2. Create an if-else condition to compare the `password` with the correct password `"password123"`.
3. If the password matches `"password123"`, print `"Access granted"`.
4. If the password does not match, print `"Access denied"`.

**Example Input/Output:**

**Input 1:**
```python
password = "password123"
```

**Output 1:**
```
Access granted
```

**Input 2:**
```python
password = "wrongpassword"
```

**Output 2:**
```
Access denied
```

**Explanation:**
- The program compares the variable `password` with the correct password `"password123"`. 
- In **Example 1**, since the password is correct, the output is `"Access granted"`.
- In **Example 2**, since the password is incorrect, the output is `"Access denied"`.

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1602443888929206"
     crossorigin="anonymous"></script>
<ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-1602443888929206"
     data-ad-slot="6296238623"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
  
### Task #5.2: Compare Two Numbers in Python

Write a Python program that compares two numbers `a` and `b`. If `a` is greater than `b`, the program should print the message "a is greater than b". Otherwise, it should print "a is not greater than b".

**Input**:
- The program sets two variables `a` and `b` to specific values (15 and 20 in this case).
- The comparison is then made based on these values.

**Expected Output**:
- The program will print one of the following outputs depending on the values of `a` and `b`:
  1. If `a` is greater than `b`:  
     **Output**:  
     `"a is greater than b"`
  
  2. If `a` is less than or equal to `b`:  
     **Output**:  
     `"a is not greater than b"`

**Example**:

1. **Input**:  
   `a = 15, b = 20`

   **Output**:  
   `"a is not greater than b"`

2. **Input**:  
   `a = 25, b = 20`

   **Output**:  
   `"a is greater than b"`

**Explanation**:
This code checks the relationship between `a` and `b`. If `a` is greater than `b`, it prints a message saying so; otherwise, it prints a different message.

### Task #5.3: Determine if a Number is Negative, Zero, or Positive

Write a Python program that checks whether a number `x` is negative, zero, or positive. The program should print:
- "Negative" if `x` is less than 0,
- "Zero" if `x` is equal to 0, and
- "Positive" if `x` is greater than 0.

**Input**:
- The program sets a variable `x` to a specific value (10 in this case).

**Expected Output**:
- The program will print one of the following outputs based on the value of `x`:
  1. If `x` is less than 0:  
     **Output**:  
     `"Negative"`
  
  2. If `x` is equal to 0:  
     **Output**:  
     `"Zero"`

  3. If `x` is greater than 0:  
     **Output**:  
     `"Positive"`

**Example**:

1. **Input**:  
   `x = 10`

   **Output**:  
   `"Positive"`

2. **Input**:  
   `x = -5`

   **Output**:  
   `"Negative"`

3. **Input**:  
   `x = 0`

   **Output**:  
   `"Zero"`

---

**Explanation**:
This code checks whether the value of `x` is less than 0, equal to 0, or greater than 0, and prints the corresponding message based on the comparison.

- [Video: Use Walrus Operator with if-else (New)](https://www.youtube.com/watch?v=vhEz75XZlJI&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja)
- [Video: How to Write Single-Line Code Instead of If-Else Statements](https://www.youtube.com/watch?v=8qOyRklMr-I&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja)

- [Python Quiz -IF](https://forms.gle/C71fbbFnDfigs4Dt8)

### Task #5.4: Compare Two Input Numbers

Write a program that takes two numbers as input and prints 
whether the first number is greater than, less than, or equal to the second number.

**Input:**
```
Enter the first number: 10
Enter the second number: 5
```

**Sample Output:**
```
10 is greater than 5
```

**Another Sample Input:**
```
Enter the first number: 4
Enter the second number: 4
```

**Output:**
```
4 is equal to 4
```

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1602443888929206"
     crossorigin="anonymous"></script>
<ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-1602443888929206"
     data-ad-slot="6296238623"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

### Task #5.5: Age Checker 

Write a simple program that asks for the user’s age and checks if the user is older than 18.

**Sample Input:**
```
Enter your age: 20
```

**Sample Output:**
```
You are older than 18.
```

**Another Sample Input:**
```
Enter your age: 16
```

**Output:**
```
You are younger than 18.
```

### Task #5.6: Divisibility Check
- Write a program that checks if a given number is divisible by both 2 and 3.

**Input:**
- A single integer, `n`.

**Output:**
- Print "Yes" if the number is divisible by both 2 and 3.
- Print "No" otherwise.

**Example:**

- **Input:**  
  `6`  
- **Output:**  
  `Yes`  

- **Input:**  
  `10`  
- **Output:**  
  `No`  

### Task #5.7: Voting Eligibility Check
- Create a program that takes the age and country of a person as input 
  and checks if they are eligible to vote in that country 
  (consider the voting age as 18 and the country as "USA").

**Input:**
- An integer `age`, representing the person's age.
- A string `country`, representing the person's country.

**Output:**
- Print "Eligible to vote" if the person is 18 years or older and from the USA.
- Print "Not eligible to vote" otherwise.

**Example:**

- **Input:**  
  `age = 20`  
  `country = USA`  
- **Output:**  
  `Eligible to vote`  

- **Input:**  
  `age = 17`  
  `country = USA`  
- **Output:**  
  `Not eligible to vote`  

- **Input:**  
  `age = 25`  
  `country = Canada`  
- **Output:**  
  `Not eligible to vote`  

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1602443888929206"
     crossorigin="anonymous"></script>
<ins class="adsbygoogle"
     style="display:block"
     data-ad-format="fluid"
     data-ad-layout-key="-gw-3+1f-3d+2z"
     data-ad-client="ca-pub-1602443888929206"
     data-ad-slot="6771715491"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

## 5.3 loops

- There are two ways to create loops in Python: with the for-loop and the while-loop.

- Repeat actions using `for` and `while` loops.

### 5.3.1 for loop

- A for loop in Python is a programming statement that repeats a block of code a fixed number of times.
- The for-loop is always used in combination with an iterable object[^1], like a list or a range. 
- The Python for statement iterates over the members of a sequence in order, executing the block each time. 

[video: What is it and Why do we Use it? \| Python For loop Tutorial](https://youtu.be/2mhrDgBEp10)

**Syntax:**

```python
for item in iterable:
    # code block
```

`iterable` is a sequence of elements such as a list, tuple, dictionary, set, or string. item is a variable that takes on the value of each element in the sequence, one at a time. The code block is executed once for each element in the sequence.

**range() function:**

- We can use the `range()` function as an iterable in a for loop in Python. The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number. 
- We can also specify the starting value and the increment value of the sequence using the range() function. For example, range(2, 10, 2) returns a sequence of numbers starting from 2, incrementing by 2, and ending at 8. [read more ...](https://www.w3schools.com/python/gloss_python_for_range.asp)

Here are the common usages:

#### Example #5.8

1. **Single Argument (`stop`)**:
   ```python
   range(stop)
   ```
   - Generates numbers from `0` up to, but not including, `stop`.

   ```python
   range(5)  # Output: 0, 1, 2, 3, 4
   ```

2. **Two Arguments (`start`, `stop`)**:
   ```python
   range(start, stop)
   ```
   - Generates numbers from `start` up to, but not including, `stop`.

   ```python
   range(2, 5)  # Output: 2, 3, 4
   ```

3. **Three Arguments (`start`, `stop`, `step`)**:
   ```python
   range(start, stop, step)
   ```
   - Generates numbers from `start` up to, but not including, `stop`, incrementing by `step`. The `step` can be positive or negative.

   ```python
   range(1, 10, 2)  # Output: 1, 3, 5, 7, 9
   range(10, 1, -2) # Output: 10, 8, 6, 4, 2
   ```

**Note:** `range()` produces an immutable sequence type, which is often used in loops. To get a list of numbers, you can convert the `range` object to a list:

```python
list(range(5))  # Output: [0, 1, 2, 3, 4]
```

- [Video: The range() Function](https://www.youtube.com/watch?v=cRa_nnO6L00&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=87)
- [Video: Use of range() in for loop](https://www.youtube.com/watch?v=ZEVsokTGbwA&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=88)

#### **Example #5.9:** Print Numbers from 1 to 5 

[video](https://youtu.be/2mhrDgBEp10)

Question: Write a Python program to print the numbers from 1 to 5, using a for loop.

```python
for i in range(6):
    print(i)
```

#### Example #5.10: Printing "Building the future, one line at a time." 5 Times Using a for Loop

**Question:** Write a Python program to print the string "Building the future, one line at a time." 5 times, using a for loop.

```python
for i in range(5):
    print("Building the future, one line at a time.")
```

#### Example #5.11: Sum of Numbers from 1 to N

Question: Write a python program to calculate the sum of the first N natural numbers using a for loop.

[video: Calculate the sum of the first N natural numbers \| Python for loop example](https://youtu.be/FgMHDLRi_G4)

#### Task #5.8: Sum of Numbers in a Range

**Description:**

Write a Python program that asks the user to input two numbers, a start and an end value, and calculates the sum of all the numbers in that range (inclusive) using a `for` loop.

**Input:**
- The program should prompt the user to enter two integers:
  1. The start of the range.
  2. The end of the range.

**Output:**
- The program should display the sum of all the numbers in the given range.

**Example:**

**Input:**
```
Enter the start of the range: 1
Enter the end of the range: 5
```

**Output:**
```
The sum of numbers from 1 to 5 is: 15
```

**Requirements:**
- Use a `for` loop to iterate through the range.
- Accumulate the sum of numbers using a variable inside the loop.


#### Task #5.9: Display Even Numbers in a Range

**Description:**

Write a Python program that asks the user to input two numbers, a start and an end value, and displays all the even numbers between the two values (inclusive) using a `for` loop.

**Input:**
- The program should prompt the user to enter two integers:
  1. The start of the range.
  2. The end of the range.

**Output:**
- The program should display all the even numbers in the range in ascending order, one number per line.

**Example:**

**Input:**
```
Enter the start of the range: 2
Enter the end of the range: 10
```

**Output:**
```
2
4
6
8
10
```

**Requirements:**
- Use a `for` loop to iterate through the range.
- Check if a number is even using the modulus (`%`) operator.
  
#### Example #5.11: Print Even Numbers from 2 to 10 and sum of even numbers

**Question:** Write a Python program to display the even numbers from 2 to 10 and sum of even numbers, inclusive, using a for loop.

```python
sum = 0
for i in range(2,11):
    if i%2 == 0:
        sum +=i
        print(i)
print(f"Sum of even numbers: {sum}")
```

#### Task #5.11: Display Multiplication Tables**

**Description:**

Write a Python program that asks the user to input a number and displays its multiplication table up to 10 using a `for` loop.

**Input:**
- The program should prompt the user to enter an integer value.

**Output:**
- The program should display the multiplication table for the entered number in the following format:

```
n x 1 = n
n x 2 = 2n
...
n x 10 = 10n
```

**Example:**

**Input:**
```
Enter a number: 5
```

**Output:**
```
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```

**Requirements:**
- Use a `for` loop to generate and display the multiplication table.

#### Example #5.12: String as an iterable

[video: String as an iterable](https://www.youtube.com/watch?v=uC0bbj08d4A)

#### Example #5.13: Lists as an iterable

```python
collection = ['python', 5, 'd']
for x in collection:
    print(x)
```

#### Example #5.14: Loop over Lists of lists

```python
list_of_lists = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]
for list in list_of_lists:
    for x in list:
        print(x)
```

- A **nested loop** is a loop inside another loop. It is a powerful programming technique that can be used to solve a wide variety of problems.

#### Example #5.15 Nested Loops - Multiplication Tables

```python
for i in range(1, 11):
    print(f"Multiplication table of {i}")
    for j in range(1, 11):
        print('%d * %d = %d' % (i, j, i*j))
```

#### Why We Use Variables in For Loops

In Python, a variable in a `for` loop is used to iterate over a sequence (like a list, tuple, string, or range) and access each element in that sequence one at a time. This variable is often called the "loop variable" or "iterator variable." 

**Understanding the Role of the Variable:**

1. **Accessing Elements**: The loop variable allows you to access each element in the sequence during each iteration of the loop. This makes it possible to perform operations on each element.

2. **Dynamic Assignment**: The loop variable automatically takes the value of the next element in the sequence during each iteration. This saves you from having to manually update the variable's value.

3. **Readability and Simplicity**: Using a loop variable makes the code more readable and easier to understand. You can name the variable in a way that reflects the data it represents, making the code more self-explanatory.

4. **Control Over Iteration**: The loop variable gives you control over the loop’s execution. You can use it to control the flow, such as skipping certain elements, breaking out of the loop early, or performing specific actions based on the variable's value.

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1602443888929206"
     crossorigin="anonymous"></script>
<ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-1602443888929206"
     data-ad-slot="6296238623"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

#### Example #5.16: Loop Through a List of Fruits in Python

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

In this example, the loop variable `fruit` takes on the value of each element in the list `fruits` during each iteration. The output will be:

```
apple
banana
cherry
```

The variable `fruit` is used to access and print each element in the `fruits` list.

#### Use of underscore in 'For Loop'

- In Python, an underscore (`_`) is often used as a variable name in a for loop (or any other context) when the value of the variable is not needed. 
- This is a common convention to indicate that the value is intentionally being ignored or discarded.

For example, if you want to repeat an action a certain number of times but don't need to use the loop variable, you can use `_`:

##### Example #5.17: Using an Underscore in a Loop to Print "Hello" Multiple Times

```python
for _ in range(5):
    print("Hello")
```

Here, `_` is used instead of a variable name like `i` or `j` because the value is not important. The loop will simply print "Hello" five times without using the loop index. This helps to make the code more readable by signaling to other programmers that the loop variable is not used in the loop's body.

- [video: Underscore to Ignore Values in for loop](https://www.youtube.com/watch?v=bZOgrIHCHbQ&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=2)
  

### 5.3.2 while loop

- A while loop in python is a control flow statement that repeatedly executes a block of code until a specified condition is met.

**Syntax:**

```python
while condition:
    # code block
```

Here, condition is a boolean expression that is evaluated before each iteration of the loop. If the condition is `True`, the code block is executed. The loop continues to execute as long as the condition remains True.

[video: Python while loop example - Learn how to use while loop](https://youtu.be/zF-x4JBgn4A?si=P_IAHHTwg9Yk9nSD)

#### Example #5.18: Print numbers from 1 to 10 using while loop

Question: Write a Python program to print the numbers from 1 to 10, using a while loop?

```python
count = 1  # Start counting at 1
while count <= 10:  # Keep counting as long as we're less than or equal to 10
    print(count)  # Print the current number
    count += 1  # Add 1 to the count for the next round
```

#### Example #5.19: Print "Hello, world!" 5 times using while loop

Question: Write a Python program to print the string "Hello, world!" 5 times, using a while loop?

```python
i = 1
while i <= 10:
    print('Hello, world!')
    i += 1
```

#### Task #5.12: Display Multiplication Tables**

**Description:**

Write a Python program that asks the user to input a number and displays its multiplication table up to 10 using a `while` loop.

**Input:**
- The program should prompt the user to enter an integer value.

**Output:**
- The program should display the multiplication table for the entered number in the following format:

```
n x 1 = n
n x 2 = 2n
...
n x 10 = 10n
```

**Example:**

**Input:**
```
Enter a number: 5
```

**Output:**
```
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```

**Requirements:**
- Use a `while` loop to generate and display the multiplication table.

#### Task #5.13: Sum Integers from 1 to 100 Using While Loop

Write a Python program that calculates the sum of all integers from 1 to 100. The program should use a `while` loop to iterate through these integers and accumulate their sum.

**Input**:
- The program initializes a variable `i` to 1 and a variable `sum` to 0. 
- The loop continues while `i` is less than or equal to 100.

**Expected Output**:
- The program will print the total sum of integers from 1 to 100 in the following format:  
  `Sum = {sum}`

**Example Output**:

```
Sum = 5050
```

**Explanation**:
This code uses a `while` loop to iterate through the integers from 1 to 100.
In each iteration, the current value of `i` is added to the variable `sum`, and `i` is incremented by 1.
After the loop completes, the total sum is printed.

#### Example #5.20: Sum of even numbers from 2 to 20 using while loop

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

#### Task #5.14: Calculate Squares of Numbers from 1 to 4 Using While Loop

Write a Python program that calculates and prints the square of the numbers from 1 to 4. The program should use a `while` loop to iterate through these numbers.

**Input**:
- The program initializes a variable `i` to 1 and continues looping while `i` is less than 5.

**Expected Output**:
- The program will print the square of each number from 1 to 4 in the following format:  
  `Square of {i} is {square}`

**Example Output**:

```
Square of 1 is 1
Square of 2 is 4
Square of 3 is 9
Square of 4 is 16
```

**Explanation**:
This code uses a `while` loop to calculate the square of the variable `i`, 
which starts at 1 and increments by 1 in each iteration until it reaches 5. 
The squares of the numbers 1 through 4 are printed during each iteration.

#### Example #5.21: Prompt User for Input Until Blank Line is Entered

Question: Write a Python program to prompt the user to enter lines of text until the user enters a blank line. The program should then display the message "You entered a blank line.".

```python
inputStr = 'Start'

while inputStr != "":
  inputStr = input("Enter a line of text:")

print('You entered a blank line.')
```

#### Example #5.22: Sum User-Entered Numbers Until Zero is Entered

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

#### Task #5.15: Sum User-Entered Numbers Until a Negative Number is Entered

Write a Python program that prompts the user to enter numbers. The program should keep accepting numbers until the user enters a negative number. Once a negative number is entered, the program should stop and display the sum of all the numbers entered (excluding the negative number).

**Sample Input:**
```
Enter a number (negative number to stop): 10
Enter another number (negative number to stop): 20
Enter another number (negative number to stop): 5
Enter another number (negative number to stop): -1
```

**Sample Output:**
```
The sum of all numbers is: 35
```

#### Task #14: Number Guessing Game

**Instructions:**
- Write a Python program where the computer picks a random number between 1 and 10, and the user has to guess it.
- The program should continue asking the user for a guess until they guess the correct number.
- After each incorrect guess, the program should give a hint whether the guess is too low or too high.

**Example Code:**

```python
import random

# Step 1: Computer picks a random number between 1 and 10
secret_number = random.randint(1, 10)

# Step 2: Initialize the guess variable to None
guess = None

# Step 3: Use a while loop to keep asking the user for input

# write your code here

```

**Sample Input and Output:**

```
Guess a number between 1 and 10: 4
Too low! Try again.
Guess a number between 1 and 10: 9
Too high! Try again.
Guess a number between 1 and 10: 7
Too low! Try again.
Guess a number between 1 and 10: 8
Congratulations! You guessed the correct number.
```

This sample demonstrates:
- How the user is prompted repeatedly.
- Feedback on whether their guess is too low or too high.
- A congratulatory message when the correct guess is made.
- 
#### Example #24: Infinite Loop Printing Messages with Counter

[Video: Learn how to use INFINITE while loop](https://www.youtube.com/watch?v=4qZyBEKSfaA&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=49))

```python
x = 1
while True:
    print("To infinity and beyond! We're getting close, on %d now!" % (x))
    x += 1
```

**while loop examples:**
  
**See also:**

- [Video: Learn how to use while loops](https://www.youtube.com/watch?v=zF-x4JBgn4A&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=50)

- [Video: Python while loop](https://www.youtube.com/watch?v=ieU3ZRSZVf8&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=86)

[video: Python Loops Performance Comparison: For vs. While | Which is Faster?](https://youtu.be/6JNeo6TVQN8)

### Loop Control Statements (break, continue, pass)

These statements modify the behavior of loops.

**break:** Terminates the loop entirely.
**continue:** Skips the current iteration and moves to the next one.
**pass:** Does nothing, often used as a placeholder.

#### `break`

Exits the loop prematurely.

```python
for item in sequence:
    if some_condition:
        break  # exit the loop
```

#### `continue`

Skips the current iteration and proceeds to the next iteration of the loop.

```python
for item in sequence:
    if some_condition:
        continue  # skip the rest of the code in this iteration
    # code to execute if some_condition is False
```

#### `pass`

A null statement, used as a placeholder.

```python
if condition:
    pass  # do nothing
```

- [Video: How to Effectively Use Break and Continue Statements](https://www.youtube.com/watch?v=LfF9CsyVRgU&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=68)
- [Video: Using Python break statement with a while loop](https://www.youtube.com/watch?v=KWuyQ7HQUBE&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=85)

## Example #: Using Break Statement in a Loop with Range

```python
for x in range(3):
    if x == 1:
        break
```
#### Example 1: Exit a loop when a number is found
```python
# Search for the number 5 and exit the loop when found
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    print(f"Checking {num}...")
    if num == 5:
        print("Number 5 found! Exiting the loop.")
        break  # Exit the loop
```

**Output**:
```
Checking 1...
Checking 2...
Checking 3...
Checking 4...
Checking 5...
Number 5 found! Exiting the loop.
```

---

#### Example 2: Password validation with `while` loop
```python
# Keep asking for a password until the correct one is entered
correct_password = "python123"

while True:
    user_input = input("Enter the password: ")
    if user_input == correct_password:
        print("Access granted!")
        break  # Exit the loop
    else:
        print("Wrong password. Try again!")
```

---

### Example 1: Skip even numbers using `continue` Statement

Skips the **current iteration** and moves to the next loop cycle.

```python
# Print only odd numbers (skip even numbers)
for num in range(1, 11):
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num)
```

**Output**:
```
1
3
5
7
9
```

---

#### Example 2: **Temperature Monitoring**  
Stop monitoring if temperature exceeds a safe limit.
```python
temperatures = [25, 30, 32, 28, 45, 29, 33]  # Sensor readings

for temp in temperatures:
    if temp > 40:
        print(f"ALERT: Temperature {temp}°C is unsafe! Shutting down.")
        break  # Exit immediately
    print(f"Temperature {temp}°C is safe.")
```

**Output**:
```
Temperature 25°C is safe.
Temperature 30°C is safe.
Temperature 32°C is safe.
Temperature 28°C is safe.
ALERT: Temperature 45°C is unsafe! Shutting down.
```

---

### Example 1: **Data Cleaning using `continue` Statement**  
Skip invalid entries when processing a dataset.
```python
user_ages = [20, 15, "unknown", 30, -5, 25]  # Some invalid data

print("Valid ages:")
for age in user_ages:
    if not isinstance(age, int) or age < 0 or age > 120:
        continue  # Skip invalid entries
    print(f"- {age} years old")
```

**Output**:
```
Valid ages:
- 20 years old
- 15 years old
- 30 years old
- 25 years old
```

---

### **Task: Coffee Machine Stock Check using `break` Statement**  
   Simulate a coffee machine that stops serving when a drink is out of stock.  
   - **Input List**: `["latte", "cappuccino", "espresso", "mocha", "out_of_stock", "latte"]`  
   - **Goal**: Loop through the list and stop when "out_of_stock" is found.  
   - **Example Output**:  
     ```
     Serving latte...  
     Serving cappuccino...  
     Serving espresso...  
     Serving mocha...  
     Out of stock! Machine stopping.  
     ```
     
**Task: Skip Negative Numbers**  
   Calculate the sum of positive numbers in a list, ignoring negatives.  
   - **Input**: `[5, -2, 10, -8, 3]`  
   - **Goal**: Use `continue` to skip negative values.  
   - **Output**: `Sum of positive numbers: 18`

**Task: Simple Calculator with Exit using `continue` and `break`**  
   Create a loop that:  
   - Lets users type numbers to add.  
   - Skips non-numeric inputs (use `continue`).  
   - Exits when the user types "quit" (use `break`).  
   - **Example Output**:  
     ```
     Enter a number (or 'quit'): 5  
     Enter a number (or 'quit'): ten  
     Invalid input!  
     Enter a number (or 'quit'): 3  
     Enter a number (or 'quit'): quit  
     Total: 8  
     ```

 7. **Task: Movie Ticket Checker**  
   Loop through a list of ages and:  
   - Skip ages < 0 (invalid).  
   - Stop if a "VIP" (age 100+) is found.  
   - **Input**: `[25, -5, 30, 105, 40]`  
   - **Output**:  
     ```
     Valid age: 25  
     Skipped invalid age.  
     Valid age: 30  
     VIP detected! Stopping sales.  
     ```

8. **Task: Flight Booking System**  
   Check seat availability in a list. Stop when a seat is found, or skip "reserved" seats.  
   - **Input**: `["reserved", "reserved", "available", "reserved"]`  
   - **Output**:  
     ```
     Seat 1: Reserved.  
     Seat 2: Reserved.  
     Seat 3: Available! Booked successfully.  
     ```
### The else Clauses on Loops

In Python, the `else` clause can be used with loops (`for` and `while`). This may be surprising at first since most people associate `else` with `if` statements. However, in loops, the `else` clause has a unique behavior:

- The `else` block is executed **only if the loop completes all its iterations without encountering a `break` statement**.
- If the loop is exited early because of a `break`, the `else` block is skipped.

The `else` clause in loops (`for` and `while`) in Python is a bit unusual because most people associate `else` with `if` statements. In the context of loops, the `else` clause is executed only when the loop finishes normally, meaning it wasn’t interrupted by a `break` statement.

**How It Works:**

1. **With a `for` loop**:
   - The `else` block runs if the loop completes all its iterations without hitting a `break`.
   - If the loop is terminated by a `break`, the `else` block is skipped.

2. **With a `while` loop**:
   - The `else` block runs if the `while` loop condition becomes `False` naturally.
   - If the loop is terminated by a `break`, the `else` block is skipped.

#### Example with a `for` loop

Let’s say we’re searching for a specific number in a list.

```python
# List of numbers
numbers = [1, 2, 3, 4, 5]

# Number we want to find
target = 6

# Iterate over the list
for num in numbers:
    if num == target:
        print("Found the target!")
        break
else:
    print("Target not found in the list.")
```

**Explanation:**
- The loop checks each number to see if it matches the `target`.
- If the number is found, the loop breaks, and the `else` clause is skipped.
- If the loop finishes without finding the target (i.e., without a `break`), the `else` block runs, printing "Target not found in the list."

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1602443888929206"
     crossorigin="anonymous"></script>
<ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-1602443888929206"
     data-ad-slot="6296238623"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

### **3. Combined Example**  
**Use Case:** Login system with limited attempts.
```python
max_attempts = 3
correct_password = "secret123"

for attempt in range(1, max_attempts + 1):
    password = input(f"Attempt {attempt}: Enter password: ")
    if password != correct_password:
        print("Wrong password. Try again.")
        continue  # Skip to next attempt
    else:
        print("Login successful!")
        break  # Exit loop on success
else:
    print("Account locked. Too many failed attempts.")
```

**Output** (if user fails 3 times):
```
Attempt 1: Enter password: hello
Wrong password. Try again.
Attempt 2: Enter password: test
Wrong password. Try again.
Attempt 3: Enter password: 123
Wrong password. Try again.
Account locked. Too many failed attempts.
```


#### Example with a `while` loop

```python
# Counter
i = 1

# Loop condition
while i <= 5:
    if i == 3:
        print("Breaking the loop")
        break
    print(i)
    i += 1
else:
    print("Loop finished without breaking.")
```

**Explanation:**
- The loop runs while `i` is less than or equal to 5.
- If `i` equals 3, the loop breaks.
- Since the loop is broken before it naturally ends, the `else` block is skipped.

#### Why Use the `else` Clause with Loops?

Using `else` with loops can be helpful when you're performing a search or some operation where you want to know if the loop completed successfully or was interrupted by a `break`. It’s a clean way to handle scenarios where the loop might end early.
  

#### Example #: for..else

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

## Fix the errors in Python

To learn about Common Errors in Python, see [Appendix A](#appendix-a-common-errors-in-python).

1. **Mistaken Use of `elif` Instead of `if`** [Python Quiz #43]

**Code:**
```python
x = 7

if x > 5:
    print("x is greater than 5")
elif x > 0:
    print("x is positive")
```

- **Watch the Solution Now ✨:**[https://youtu.be/oQAvH8N1uPk](https://youtu.be/oQAvH8N1uPk)

2. **Infinite `while` Loop Due to Missing Update Statement** [Python Quiz #44]

**Problem Statement:**
Write a program that starts with a given positive integer and repeatedly prints its value, decreasing it by 1 in each iteration until it reaches 0. However, the initial code runs into an issue: the loop does not terminate because the value of the integer is never updated, leading to an infinite loop.

**Code:**
```python
n = 10

while n > 0:
    print(n)
```

**Mistake:**  
The loop will run infinitely because `n` is never updated, so `n > 0` is always true.

  - [**Watch the Solution Now ✨**](https://youtu.be/LVHCsgRo-54) 

3. **`continue` Misused in `while` Loop** [Python Quiz #45]

**Scenario:**
You are tasked with debugging a piece of Python code that uses a `while` loop. The goal of the loop is to print numbers from `0` to `4`, skipping the number `2`. However, the code as written enters an infinite loop when the value of `i` becomes `2`.

**Given Code:**
```python
i = 0

while i < 5:
    if i == 2:
        continue
    print(i)
    i += 1
```

**Problem:**
The `continue` statement is misused in this code. When `i == 2`, the `continue` statement is executed, causing the loop to skip the `i += 1` statement. As a result, `i` remains `2` indefinitely, leading to an infinite loop.

**Task:**
1. Identify the mistake in the code that causes the infinite loop.
2. Correct the code so that it successfully prints all numbers from `0` to `4`, except for `2`.

**Expected Output:**
```
0
1
3
4
```
  - [**Watch the Solution Now ✨**](https://youtu.be/2yabb2TJ7a0) 

4. **Incorrect Use of Multiple `elif` Conditions**

**Code:**
```python
score = 75

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
elif score < 70:
    print("F")
```

**Mistake:**  
The last `elif` block (`elif score < 70`) is redundant because the `elif score >= 70` block already covers it.

**Improved Code:**
```python
score = 75

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
```
- The `else` block now correctly handles any score below `60`.

5. Syntax Error: Missing Colon [Python Quiz #49]

```python
if x > 5  # Missing colon here
  print("X is greater than 5")
```

Here’s another question:

### Question:
The following code is intended to print the even numbers from 0 to 10, but it contains an error. Identify and fix the error.

```python
for i in range(0, 11):
if i % 2 == 0:
    print(i)
```

### Answer:
The code has an indentation error. The `if` statement needs to be indented to be part of the `for` loop.

### Fixed Code:
```python
for i in range(0, 11):
    if i % 2 == 0:
        print(i)
```

### Explanation:
In Python, all statements inside a `for` loop and any nested statements (like `if`) need to be indented consistently. This indicates that they are part of the respective block.

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

E) None


6. **Incorrect `if` Statement Syntax**

**Code:**
```python
x = 10

if x > 5
    print("x is greater than 5")
```

**Mistake:**  
The `if` statement is missing a colon (`:`) at the end.

**Corrected Code:**
```python
x = 10

if x > 5:
    print("x is greater than 5")
```

7. **Incorrect Indentation in `if-else` Statement**

**Code:**
```python
y = -3

if y > 0:
    print("y is positive")
    print("This is always printed")
else:
print("y is not positive")
```

**Mistake:**  
The `else` block is not properly indented.

**Corrected Code:**
```python
y = -3

if y > 0:
    print("y is positive")
    print("This is always printed")
else:
    print("y is not positive")
```

8. **`while` Loop with Incorrect Condition**

**Code:**
```python
count = 10

while count > 10:
    print("This will never print")
    count -= 1
```

**Mistake:**  
The loop condition `count > 10` is false at the start, so the loop will never run.

**Corrected Code:**
```python
count = 10

while count >= 0:
    print("Count:", count)
    count -= 1
```

9. **`for` Loop with Incorrect Range**

**Code:**
```python
for i in range(1, 10, -1):
    print(i)
```

**Mistake:**  
The step value in `range(1, 10, -1)` is negative, but the start value is less than the stop value, so this loop will not run.

**Corrected Code:**
```python
for i in range(10, 0, -1):
    print(i)
```
- This prints numbers from 10 to 1.

10. **Using `break` Incorrectly in a Loop**

**Code:**
```python
for i in range(5):
    if i == 2:
        break
    else:
        print(i)
```

**Mistake:**  
The `else` block is not correctly used here. It runs as part of each iteration, not after the loop.

**Corrected Code:**
```python
for i in range(5):
    if i == 2:
        break
    print(i)
else:
    print("Loop completed without a break")
```
- The `else` block will only run if the loop completes without a `break`.

11. **`try` Block with Unhandled Exception**

**Code:**
```python
try:
    print(5 / 0)
except TypeError:
    print("A TypeError occurred")
```

**Mistake:**  
The code raises a `ZeroDivisionError`, but the `except` block is only catching a `TypeError`.

**Corrected Code:**
```python
try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```

12. **Misuse of `continue` Statement**

**Code:**
```python
for i in range(5):
    if i == 3:
        continue
        print("This will never be printed")
    print(i)
```

**Mistake:**  
The `print` statement after `continue` will never be executed.

**Corrected Code:**
```python
for i in range(5):
    if i == 3:
        continue
    print(i)
```
- The code correctly skips printing `3` and continues with the next iteration.

13. **Logical Error with `if-elif` Statements**

**Code:**
```python
z = 20

if z > 30:
    print("z is greater than 30")
elif z > 10:
    print("z is greater than 10")
else:
    print("z is less than 10")
```

**Mistake:**  
The code will print `"z is greater than 10"` even though `z` is also greater than 30. This is logically correct, but not what might be intended if you want to check for ranges.

**Corrected Code:**
```python
z = 20

if z > 30:
    print("z is greater than 30")
elif z > 20:
    print("z is greater than 20 but less than 30")
elif z > 10:
    print("z is greater than 10")
else:
    print("z is less than or equal to 10")
```
- Now, this checks for more specific conditions.

14. **What will be the output of the following code?**

```python
for i in range(5):
    print(i)
else:
    break
```

15. **Incorrect Usage of `pass` in Control Flow**

**Code:**
```python
for i in range(5):
    if i == 2:
        pass
        print("This should not print")
    print(i)
```

**Mistake:**  
The `pass` statement does nothing, but the `print("This should not print")` will still run.

**Corrected Code:**
```python
for i in range(5):
    if i == 2:
        pass
    print(i)
```
- Now, the loop will simply skip doing anything when `i` is `2`, without any unintended behavior.

16. **Improper Use of `finally` in Exception Handling**

**Code:**
```python
try:
    result = 10 / 0
finally:
    print("This will run no matter what.")
except ZeroDivisionError:
    print("You can't divide by zero!")
```

**Mistake:**  
The `finally` block must come after `except`, not before.

**Corrected Code:**
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
finally:
    print("This will run no matter what.")
```

These challenges are designed to highlight common mistakes that occur when working with control flow statements in Python. Working through these examples will help reinforce proper syntax and logical structure.

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1602443888929206"
     crossorigin="anonymous"></script>
<ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-1602443888929206"
     data-ad-slot="6296238623"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

## True/False (Mark T for True and F for False)

## Multiple Choice (Select the best answer)

- [Python if elif else Quiz](../quizzes/python-if-elif-else-quiz.md)
- [Python For Loop Quiz](../quizzes/python-for-loop-quiz.md)
- [Python While Loop Quiz](../quizzes/python-while-loop-quiz.md)
- [ Python Quiz: `break`, `continue` Statements, and `else` Clauses in Loops](../quizzes/python-break-continue-else-loop-quiz.md)

### if statement (MCQs)

**What is the syntax for a simple if statement in Python?** [Python Quiz #50]
    - A) if x == 10:
    - B) for x in range(10):
    - C) while x < 10:
    - D) if (x == 10) then:

1. **What is the output of the following code** [Python Quiz #16](https://youtube.com/shorts/ExDu2lwjd3c?si=VVq47sCNgRWd7l_i)

```python
x = 10
y = 5

if x == y * 2:
    print("True")
else:
    print("False")
```
    - A) True
    - B) False
    - C) Error
    - D) Nothing

**Watch this video for the answer:** [https://youtube.com/shorts/ExDu2lwjd3c?si=VVq47sCNgRWd7l_i](https://youtube.com/shorts/ExDu2lwjd3c?si=VVq47sCNgRWd7l_i)

2. **What is the output of the following code?** [Python Quiz #31](https://youtube.com/shorts/7uAgT3_P4Oc?si=evBHSymYx2kVaEEk)

```python
x = 3
y = 5

if x == 3 and y != 5:
    print("True")
else:
    print("False")
```
    - A) True
    - B) False
    - C) Syntax error
    - D) Name error
  
**Watch the video for the answer:** [https://youtube.com/shorts/7uAgT3_P4Oc?si=evBHSymYx2kVaEEk](https://youtube.com/shorts/7uAgT3_P4Oc?si=evBHSymYx2kVaEEk)

3. **What will be the output of the following code?** [Python Quiz #39](https://youtu.be/TkmqlDK8oCg)
```python
x = 10
if  5 < x < 15:
    print("x is between 5 and 15")
else:
    print("x is not between 5 and 15")
```
    - A) x is between 5 and 15
    - B) x is not between 5 and 15
    - C) Error
    - D) No output
**Watch the video for the answer:**[https://youtu.be/TkmqlDK8oCg](https://youtu.be/TkmqlDK8oCg)

4. **Which of the following correctly fixes the syntax error in the code below?** [Python Quiz #40](https://youtu.be/3010E1WuHd8)

```python
# fixes the error
x = 10
if x == 10
    print("x is 10")
```

    - A) Remove the comment.
    - B) Add a colon after `if x == 10`.
    - C) Add parentheses around `x == 10`.
    - D) Indent the print statement correctly.

**Watch the video for the answer:** [https://youtu.be/3010E1WuHd8](https://youtu.be/3010E1WuHd8)

1. **Which of the following correctly represents the syntax of an if statement in Python?**
    - A) if condition { block of code }
    - B) if(condition) { block of code }
    - C) if condition: block of code
    - D) None


3. **What is the purpose of the else block in an if statement?**

    - A) To execute a code block when the if condition is True
    - B) To execute a code block when the if condition is False
    - C) To create an infinite loop
    - D) To define a function

4. **What happens when none of the conditions in an if-elif-else chain are True, and there is no else block?**

    - A) The program raises an error.
    - B) The program executes the first if block.
    - C) The program executes the last elif block.
    - D) The program does nothing and continues to the next statement.

5. **What will be the output of the following code?**

```python
x = 10
y = 5
if x < y:
    print("x is greater than y")
```
    - A) "x is greater than y"
    - B) "x is less than y"
    - C) Nothing will be printed
    - D) An error will occur

6. **What happens if none of the conditions in an if-elif chain are True, and there is no else block?**

    - A) The program raises an error
    - B) The program executes the first if block
    - C) The program does nothing and continues to the next statement
    - D) The program executes the last elif block

7. **What will be the output of the following code?**

```python
number = 10
if number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")
```
    - A) Number is odd
    - B) Number is even
    - C) Nothing
    - D) Error

8. **Which of the following is the correct way to compare if two variables are equal in an if statement?**
    - A) if x equals 5:
    - B) if x == 5:
    - C) if x = 5:
    - D) if x := 5:

9. **How can you check if a value is NOT equal to 10 in an if statement?**
    - A) if x != 10:
    - B) if x <> 10:
    - C) if x =! 10:
    - D) if x not 10:

10. **What does the following code snippet do?**
```python
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")

```
    - A) Prints "Positive" if x is greater than 0, "Negative" if x is less than 0, and "Zero" if x is 0.
    - B) Prints "Positive" if x is less than 0, "Negative" if x is greater than 0, and "Zero" if x is 0.
    - C) Prints "Positive" if x is 0, "Negative" if x is greater than 0, and "Zero" if x is less than 0.
    - D) Causes an error because the conditions are conflicting.

11. **What is the correct syntax for an if-else statement?**
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

12. **What happens if none of the conditions in an if-elif-else block are true?**
    - A) The program terminates
    - B) The else block is executed
    - C) An error occurs
    - D) The program continues without executing any block

14. **What will be the output of the following code?**
   ```python
   num = 7
   if num % 2 == 0:
       print("Even")
   else:
       print("Odd")
   ```
    - A) Even
    - B) Odd
    - C) Error
    - D) No output

15. **What will be the output of the following code?**

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

    - A) Grade: A  
    - B) Grade: B  
    - C) Grade: C  
    - D) Grade: F

  
16. **What is the output of the following code?**

```python
x = 5
if x > 10:
    print("Greater than 10")
elif x > 5:
    print("Greater than 5 but not greater than 10")
else:
    print("5 or less")
```

    - A) Greater than 10  
    - B) Greater than 5 but not greater than 10  
    - C) 5 or less  
    - D) No output

**Answer:** C

17. **Which of the following is true about the `elif` statement?**

    - A) `elif` stands for "else if" and is used to check additional conditions after the `if` statement  
    - B) `elif` is the same as `else`  
    - C) `elif` must be followed by an `else` statement  
    - D) You can have multiple `elif` statements in one block

**Answer:** A, D

18. **What will be the output of the following code?**

```python
y = 20
if y < 20:
    print("Less than 20")
elif y == 20:
    print("Equal to 20")
else:
    print("Greater than 20")
```

    - A) Less than 20  
    - B) Equal to 20  
    - C) Greater than 20  
    - D) None of the above

**Answer:** B

19. **What will be the output of the following code snippet?**

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

    - A) a is positive  
    - B) a is non-positive  
    - C) a is less than or equal to b  
    - D) No output

**Answer:** A

20. **Which of the following statements is false about `if-elif-else` statements in Python?**

    - A) `elif` statements are optional in an `if-elif-else` construct  
    - B) An `if` statement can be followed by multiple `elif` statements  
    - C) An `else` statement is mandatory in an `if-elif-else` construct  
    - D) An `if` statement can exist without `elif` or `else`

**Answer:** C

21. **What will be the output of the following code?**

```python
x = 0
if x:
    print("True")
else:
    print("False")
```

    - A) True  
    - B) False  
    - C) No output  
    - D) Error

**Answer:** B

**Truthy and Falsy Values in Python**
In Python, certain values are considered False when evaluated in a boolean context (like in an if statement). These values include:

- None
- False
- 0 (zero of any numeric type, including 0.0)
- Empty sequences and collections (e.g., '', (), [], {})
- Any object that implements __bool__ or __len__ to return False or 0, respectively

22. **Which of the following expressions can be used in an `if` condition to check if a number `n` is between 1 and 100 inclusive?**

    - A) `if n > 1 and n < 100:`  
    - B) `if n >= 1 and n <= 100:`  
    - C) `if 1 <= n <= 100:`  
    - D) `if n == 1 or n == 100:`

**Answer:** B, C

23. **What will be the output of the following code?**

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

    - A) Less than 5  
    - B) Equal to 10  
    - C) Greater than 5 but not 10  
    - D) Something else

**Answer:** C

24. **What is the purpose of the `else` statement in an `if-elif-else` structure?**

    - A) To check another condition if the previous ones were false  
    - B) To execute a block of code if none of the previous conditions were true  
    - C) To execute a block of code if the previous conditions were true  
    - D) To end the `if-elif-else` structure

**Answer:** B

25. **What will be the output of the following code?**

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

    - A) x is 10  
    - B) x is greater than 5 but not 10  
    - C) x is 5 or less  
    - D) No output

**Answer:** A

26. **Which of the following is correct syntax for an `if-elif-else` statement in Python?**

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

27. **What will be the output of the following code?**

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
    - A) a is greater  
    - B) a and b are equal  
    - C) b is greater  
    - D) No output

**Answer:** C

28. **Which of the following statements will execute if `n = 7`?**

```python
if n < 5:
    print("n is less than 5")
elif n < 10:
    print("n is less than 10")
else:
    print("n is 10 or more")
```

    - A) n is less than 5  
    - B) n is less than 10  
    - C) n is 10 or more  
    - D) None of the above

**Answer:** B


29. **Which keyword is used to check an additional condition if the initial `if` statement is `False`?**

    - A) else  
    - B) elif  
    - C) elseif  
    - D) if

**Answer:** B

30. **What is the result of the following code?**

```python
x = 0
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
```

    - A) Positive  
    - B) Zero  
    - C) Negative  
    - D) No output

**Answer:** B

31. **How many `elif` clauses can be included in an `if-elif-else` statement?**

    - A) One  
    - B) Two  
    - C) Unlimited  
    - D) None

**Answer:** C

32. **What will be the output of the following code?**

```python
age = 20
if age < 18:
    print("Minor")
elif age >= 18 and age < 65:
    print("Adult")
else:
    print("Senior")
```

    - A) Minor  
    - B) Adult  
    - C) Senior  
    - D) No output

**Answer:** B


### for loop (MCQs)

1. **What is the output of the following code snippet in Python?** [Python Quiz #3](https://bit.ly/3WKH9wE)

```python
for i in range(10):
    if i % 2 == 0:
        print(i)
```

A) 0 1 2 3 4 5 6 7 8 9
B) 0 2 4 6 8
C) 2 4 6 8
D) IndentationError: expected an indented block

**Watch the video for answer:** [https://bit.ly/3WKH9wE](https://bit.ly/3WKH9wE)

2. **What is the correct syntax for a for loop in Python?**

- A) for (int i = 0; i < 10; i++):
- B) for i in range(10):
- C) for i = 0 to 9:
- D) for i in 10:

**watch the video for the answer:** [https://youtu.be/2mhrDgBEp10](https://youtu.be/2mhrDgBEp10)

3. **What will be the output of the following code?** [Python Quiz #36](https://bit.ly/3WqjjEP)

```python
for i in range(5):
  print(i * 2)
```

    - A) 0 1 2 3 4
    - B) 2 4 6 8 10
    - C) 10 8 6 4 2
    - D) 0 2 4 6 8

**Watch this video for the answer:** [https://bit.ly/3WqjjEP](https://bit.ly/3WqjjEP)

4. **How many times is the print statement executed?** [Python Quiz #37](https://youtu.be/CYeZI3uCiTI)
```python
for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")
```

    - A) 3 times
    - B) 5 times
    - C) 6 times
    - D) 9 times

**Watch this video for the answer:** [https://youtu.be/CYeZI3uCiTI](https://youtu.be/CYeZI3uCiTI) 

1. **What will the program output if the `number` variable is set to `5`?**
```python
# Get user input
number = int(input("Enter non-negative number:"))

if number < 0:
    print("Factorial is not defined for negative numbers.")
    result = None
elif number == 0 or number ==1:
    result = 1
else:
    result = 1
    for i in range(2, number + 1):
        result *= i

if result is not None:
    print("Factorial of", number, "is", result)
```

- A) Factorial is not defined for negative numbers.
- B) Factorial of 5 is 5
- C) Factorial of 5 is 120
- D) Factorial of 5 is 24

**Watch this video for the answer:** [https://youtu.be/K5LV5I2hFg4](https://youtu.be/K5LV5I2hFg4)

6. **What will happen if the `number` variable is set to `0`?**

```python
# Get user input
number = int(input("Enter non-negative number:"))

if number < 0:
    print("Factorial is not defined for negative numbers.")
    result = None
elif number == 0 or number ==1:
    result = 1
else:
    result = 1
    for i in range(2, number + 1):
        result *= i

if result is not None:
    print("Factorial of", number, "is", result)
```

- A) The program will raise an error.
- B) The program will print "Factorial of 0 is 1".
- C) The program will print "Factorial is not defined for negative numbers."
- D) The program will print "Factorial of 0 is 0".

**Watch this video for the answer:** [https://youtu.be/K5LV5I2hFg4](https://youtu.be/K5LV5I2hFg4)

**What is the primary purpose of a for loop in Python?**

    - A) To define a function
    - B) To iterate over a sequence
    - C) To create a conditional statement
    - D) To perform mathematical operations

**In Python, what does the range() function do when used in a for loop?**
    - A) Generates a sequence of numbers
    - B) Defines a list
    - C) Calculates the average
    - D) Determines the length of a string

**How can you create a nested loop in Python?**

    - A) by using a loop inside another loop with proper indentation
    - B) by using a loop inside another loop with parentheses
    - C) by using a nested keyword before the inner loop
    - D) by using a colon after the outer loop and before the inner loop

**Answer:** A

### Question 4
**Consider the following code:**
```python
total = 0
for i in range(1, 6):
    total += i
print(total)
```
**What does this code accomplish?**

A) It prints numbers from 1 to 5.
B) It calculates the sum of numbers from 1 to 5.
C) It prints the sum of numbers from 1 to 6.
D) It calculates the sum of numbers from 0 to 5.

*Explanation:* The loop iterates over the range from 0 to 5 (inclusive), summing up the values. The `total` variable accumulates this sum.

### Question 6

**How can a `for` loop be used in a real-life scenario involving data processing?**

A) To count the number of words in a large document.
B) To open a web browser.
C) To create a new file on the desktop.
D) To turn off a computer.

*Explanation:* A `for` loop can be used to iterate through the words in a document to count them, making it useful for data analysis tasks.

**Answer:** A

**Why might you use a `for` loop instead of manually performing repeated tasks?**

    - A) To reduce the chance of human error.
    - B) To make the program run slower.
    - C) To avoid using variables.
    - D) To limit the program to one iteration.

*Explanation:* Using a `for` loop automates repetitive tasks, which helps prevent errors and saves time, especially when processing large datasets or performing repetitive calculations.

**Answer:** A

**What does the following code print?**
```python
for x in range(5, 8):
    print(x)
```
    - A) 5 6 7
    - B) 5 6 7 8
    - C) 4 5 6 7
    - D) 5 6 7 8 9

*Explanation:* The `range(5, 8)` function generates numbers starting from 5 up to, but not including, 8.

**Answer:** A

**What does the following code output?**
```python
for i in range(1, 4):
    for j in range(1, 3):
        print(i, j)
```
A) 1 1 1 2 2 1 2 2 3 1 3 2
B) 1 2 2 3 3 4
C) 1 3 2 3 3 3
D) 1 1 2 2 3 3

*Explanation:* This is a nested loop, where the outer loop runs from 1 to 3 (inclusive) and the inner loop runs from 1 to 2 (inclusive). It prints all combinations of `i` and `j`.

**Answer:** A

**What will be the output of this code?**
```python
for i in range(3):
    print(i * i)
```
A) 0 1 4
B) 0 1 2
C) 1 4 9
D) 0 2 4

*Explanation:* The loop iterates over the range 0, 1, 2. For each iteration, it prints the square of the current index `i`.

**Answer:** A

**What will the following code output?**
```python
for i in range(5, 10, 2):
    print(i)
```
A) 5 7 9

B) 5 6 7 8 9

C) 5 7 9 11

D) 5 7 8

*Explanation:* The `range(5, 10, 2)` generates numbers starting from 5 up to, but not including, 10 with a step of 2, resulting in 5, 7, and 9.

**Answer:** A

### while loop (MCQs)

1. **What is the output of the following code snippet in Python?** [Python Quiz #7](https://youtube.com/shorts/zdLNmwO1u8Y)
   
```python
i = 1
while i < 10:
    print(i)
    i += 2
```

    - A) 1 2 3 4 5 6 7 8 9
    - B) 1 3 5 7 9
    - C) 0
    - D) IndentationError: expected an indented block

**Watch the video for answer:** [https://youtube.com/shorts/zdLNmwO1u8Y](https://youtube.com/shorts/zdLNmwO1u8Y)

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1602443888929206"
     crossorigin="anonymous"></script>
<ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-1602443888929206"
     data-ad-slot="6296238623"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

1. **What is the output of the following code snippet in Python?** [Python Quiz #4](https://youtube.com/shorts/9Zw-LuNX9h0)

```python
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Done")
```

    - A) 0 1 2 3 4 Done
    - B) 0 1 2 3 Done
    - C) SyntaxError: invalid syntax
    - D) IndentationError: expected an indented block

**Watch this video for the answer:** [https://youtube.com/shorts/9Zw-LuNX9h0](https://youtube.com/shorts/9Zw-LuNX9h0)

3. **What is the output of the following code?** [Python Quzi #38](https://bit.ly/3AdTqka)

```python
x = 10
while x > 0:
    print(x)
    x -= 2
```

    - A) 9 7 5 3 1
    - B) 10 8 6 4 2
    - C) 10 9 8 7 6
    - D) The code will run indefinitely.

**Watch this video for the answer:** [https://bit.ly/3AdTqka](https://bit.ly/3AdTqka)

**What is the output of the following code?**

```python
count = 0
while count < 3:
    print(count)
    count += 1
```
    - A) 0 1 2
    - B) 0 1
    - C) 1 2 3
    - D) The code will run indefinitely.

### Loop Control Statements (break, continue, pass) (MCQs)

1. **What is the output of the following code snippet in Python?** [Python Quiz #5]
```python
for i in range(5):
    if i == 3:
        continue
    print(i)
```

    - A) 0 1 2 3
    - B) 0 1 2 4
    - C) SyntaxError: invalid syntax
    - D) IndentationError: expected an indented block

**Watch this video for answer:** [https://youtube.com/shorts/x7CIxqoqccY](https://youtube.com/shorts/x7CIxqoqccY)

2. **What is the output of the following code snippet in Python?** [Python Quiz #6]
```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

    - A) 0 1 2
    - B) 0 1 2 3
    - C) 1 2 3
    - D) 0 1 2 3 4

**Watch this video for answer:** [https://youtube.com/shorts/XNLL6j-P61A](https://youtube.com/shorts/XNLL6j-P61A)

**youtube@yasirbhutta**
3. **What is the output of the following code?**

```python
i = 0
while i < 5:
    i += 1
    if i == 3:
        break
    print(i)
else:
    print("Loop completed")
```

    - A) 1 2
    - B) 1 2 Loop completed
    - C) 1 2 3
    - D) 1 2 3 Loop completed

   - **Watch the Video Tutorial for the Answer:** [https://youtu.be/LfF9CsyVRgU](https://youtu.be/LfF9CsyVRgU)

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1602443888929206"
     crossorigin="anonymous"></script>
<ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-1602443888929206"
     data-ad-slot="6296238623"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

## Exercises

**if elif else statement Exercises**

**Problem 1: FizzBuzz**

**Problem Statement:**
Write a program that prints the numbers from 1 to `n`. But for multiples of 3, print "Fizz" instead of the number, and for the multiples of 5, print "Buzz". For numbers which are multiples of both 3 and 5, print "FizzBuzz".

**Input:**
- The first and only line contains the integer `n`.

**Output:**
- Print numbers from 1 to `n`, replacing multiples of 3 with "Fizz", multiples of 5 with "Buzz", and multiples of both with "FizzBuzz".

**Example:**

**Input:**
```
15
```

**Output:**
```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
```

  - [Watch the Solution Now ✨](https://youtu.be/7mnZxCf8-XA) 

1. **Check Positive, Negative, or Zero**
   ```python
   # Write a program to check if a number is positive, negative, or zero.
   number = int(input("Enter a number: "))
   ```

2. **Even or Odd**
   ```python
   # Write a program to check if a number is even or odd.
   number = int(input("Enter a number: "))
   ```

3. **Largest of Three Numbers**
   ```python
   # Write a program to find the largest of three numbers.
   a = int(input("Enter first number: "))
   b = int(input("Enter second number: "))
   c = int(input("Enter third number: "))
   ```

4. **Grade Assignment**
   ```python
   # Write a program to assign grades based on the score.
   score = int(input("Enter your score: "))
   ```

5. **Leap Year Check**
   ```python
   # Write a program to check if a year is a leap year or not.
   year = int(input("Enter a year: "))
   ```

6. **Age Group Classification**
   ```python
   # Write a program to classify age into child, teenager, adult, and senior.
   age = int(input("Enter your age: "))
   ```

7. **Temperature Description**
   ```python
   # Write a program to describe the temperature (hot, warm, cold).
   temperature = float(input("Enter the temperature: "))
   ```

8. **Voter Eligibility**
   ```python
   # Write a program to check if a person is eligible to vote.
   age = int(input("Enter your age: "))
   ```

9. **Password Strength Checker**
   ```python
   # Write a program to check the strength of a password.
   password = input("Enter your password: ")
   ```

10. **Simple Calculator**
    ```python
    # Write a simple calculator program using if-elif-else.
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")
    ```

11. **BMI Calculator**
    ```python
    # Write a program to calculate BMI and categorize it (underweight, normal, overweight, obese).
    height = float(input("Enter your height in meters: "))
    weight = float(input("Enter your weight in kilograms: "))
    ```

12. **Triangle Type Checker**
    ```python
    # Write a program to check the type of a triangle (equilateral, isosceles, scalene).
    a = float(input("Enter first side: "))
    b = float(input("Enter second side: "))
    c = float(input("Enter third side: "))
    ```

13. **Day of the Week**
    ```python
    # Write a program to print the day of the week based on a number (1 for Monday, 7 for Sunday).
    day_number = int(input("Enter a number (1-7): "))
    ```

14. **Letter Grade Assignment**
    ```python
    # Write a program to convert a numerical score into a letter grade.
    score = int(input("Enter your score: "))
    ```

15. **Month Days**
    ```python
    # Write a program to print the number of days in a given month.
    month = int(input("Enter the month number (1-12): "))
    ```

16. **Discount Calculator**
    ```python
    # Write a program to calculate the discount on a product based on the price.
    price = float(input("Enter the price of the product: "))
    ```

17. **Character Checker**
    ```python
    # Write a program to check if a character is a vowel or consonant.
    char = input("Enter a character: ").lower()
    ```

18. **Valid Triangle Checker**
    ```python
    # Write a program to check if three given lengths can form a triangle.
    a = float(input("Enter first side: "))
    b = float(input("Enter second side: "))
    c = float(input("Enter third side: "))
    ```

19. **Multiples of Five**
    ```python
    # Write a program to check if a number is a multiple of five.
    number = int(input("Enter a number: "))
    ```

20. **Alphabet Case Checker**
    ```python
    # Write a program to check if an alphabet is uppercase or lowercase.
    char = input("Enter a character: ")
    ```

21. **Login System**
    ```python
    # Write a simple login system that checks username and password.
    username = input("Enter username: ")
    password = input("Enter password: ")
    ```

22. **Divisibility Check**
    ```python
    # Write a program to check if a number is divisible by 3 and 5.
    number = int(input("Enter a number: "))
    ```

23. **Prime Number Checker**
    ```python
    # Write a program to check if a number is prime.
    number = int(input("Enter a number: "))
    ```

24. **Digit or Alphabet Checker**
    ```python
    # Write a program to check if a character is a digit or an alphabet.
    char = input("Enter a character: ")
    ```

25. **Fuel Efficiency**
    ```python
    # Write a program to categorize fuel efficiency (excellent, good, average, poor).
    mpg = float(input("Enter miles per gallon: "))
    ```

26. **Odd or Even List**
    ```python
    # Write a program to classify numbers in a list as odd or even.
    numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
    ```

27. **Quadratic Equation Solver**
    ```python
    # Write a program to solve a quadratic equation and determine the nature of the roots.
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    ```

28. **User Age Validator**
    ```python
    # Write a program to validate the age input by the user (must be between 0 and 120).
    age = int(input("Enter your age: "))
    ```

29. **Student Result System**
    ```python
    # Write a program to check if a student passed or failed based on marks in three subjects.
    marks1 = int(input("Enter marks in subject 1: "))
    marks2 = int(input("Enter marks in subject 2: "))
    marks3 = int(input("Enter marks in subject 3: "))
    ```

30. **Shopping Cart Total**
    ```python
    # Write a program to calculate the total cost of items in a shopping cart and apply discount if applicable.
    item1 = float(input("Enter price of item 1: "))
    item2 = float(input("Enter price of item 2: "))
    item3 = float(input("Enter price of item 3: "))
    ```

### For loop Exercises

**Basic Exercises**

1. **Print "Python" 5 times**: Write a `for` loop to print the word "Python" five times. 
   - [**Watch the Solution Now ✨**](https://youtu.be/LDULv7B9QdQ) 
2. **Print numbers 0 to 9**: Write a `for` loop to print numbers from 1 to 10. 
   - [**Watch the Solution Now ✨**](https://youtube.com/shorts/zIU3X59TcBE)
3. **Print even numbers 2 to 20**: Write a `for` loop to print all even numbers from 2 to 20.
4. **Print each character in a string**: Write a `for` loop to iterate through the string "Hello, World!" and print each character.
   - [**Watch the Solution Now ✨**](https://youtu.be/FgMHDLRi_G4)
5. **Find the factorial of a number**: Write a `for` loop to calculate the factorial of a given number, e.g., 5! = 5 × 4 × 3 × 2 × 1.
   - [**Watch the Solution Now ✨**](https://youtu.be/K5LV5I2hFg4)
6. **Squares of numbers 1 to 5**: Write a Python for loop that prints the square of each number from 1 to 5. 
   - [**Watch the Solution Now ✨**](https://youtu.be/ecGCXSxHjsw)
7. **Count down from 10 to 1**: Use a `for` loop to print numbers from 10 down to 1. 
   - [**Watch the Solution Now ✨**](https://bit.ly/3yrTe0e)
8. **Calculate the sum of the first N natural numbers**
   - [**Watch the Solution Now ✨**](https://youtu.be/FgMHDLRi_G4)

**Intermediate Exercises**

9.  **Print the multiplication table for 5**: Write a `for` loop to print the multiplication table for the number 5. 
    - [**Watch the Solution Now ✨**](https://www.youtube.com/watch?v=wqtVGYn7NpQ&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=41)
2.  **Print the first 10 Fibonacci numbers**: Write a `for` loop to generate the first 10 numbers in the Fibonacci sequence.
3.  **Check if a number is prime**: Write a `for` loop to check if a given number is prime.
4.  **Sum of digits of a number**: Write a `for` loop to calculate the sum of the digits of a given number, e.g., 1234.
5.  **Print a pattern of stars**: Use nested `for` loops to print the following pattern:
    ```
    *
    **
    ***
    ****
    *****
    ```
6.  **Print odd numbers between 1 and 20**: Write a `for` loop to print all odd numbers between 1 and 20.
7.  **Count vowels in a string**: Use a `for` loop to count the number of vowels in the string "Hello, World!".

**Advanced Exercises**

18. **Generate a list of even numbers**: Use a `for` loop to generate a list of even numbers between 1 and 20.
22. **Print numbers divisible by 3 and 5 between 1 and 50**: Use a `for` loop to print all numbers between 1 and 50 that are divisible by both 3 and 5.
23. **Print a right-angle triangle of numbers**: Use nested `for` loops to print the following pattern:
    ```
    1
    12
    123
    1234
    12345
    ```
24. **Print numbers that are multiples of 3 up to 30**: Use a `for` loop to print all multiples of 3 up to 30.
25. **Find numbers divisible by 7 and 11 between 1 and 100**: Use a `for` loop to print all numbers between 1 and 100 that are divisible by both 7 and 11.
26. **Calculate the harmonic sum of n numbers**: Write a

### While loop Exercises

1. How to Count Digits in a Positive Integer using Python 
   - [**Watch the Solution Now ✨**](https://www.youtube.com/watch?v=33n-lb1Ujp4&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=48)
2. How to Count Occurrence of a Specific Digit in a Number using Python.  
   - [**Watch the Solution Now ✨**](https://www.youtube.com/watch?v=MXWbTdvSBVs&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=47)

### Loop Control Statements (break, continue, pass) Exercises

1. Write a Python program that runs an infinite loop using a while statement. Include a way to exit the loop by using the break statement.
   - [**Watch the Solution Now ✨**](https://youtube.com/shorts/4qZyBEKSfaA)
2. Write a Python program using the continue statement in a loop to skip specific iterations, such as skipping over the numbers 0, 1, 2, and 4?
   - [**Watch the Solution Now ✨**](https://youtube.com/shorts/lf6SYOMIJv8)

## Mini Projects

### Project #1: Simple Calculator

Write a Python program that allows the user to perform basic arithmetic operations (addition, subtraction, multiplication, and division) until they choose to exit. The program should take two numbers and an operation from the user, perform the calculation, and display the result.

**Requirements:**
- The program should continuously prompt the user for two numbers and an operation.
- If the user enters an invalid operation, display an error message and ask for input again.
- The user should be able to exit the program by entering 'exit'.
- Handle division by zero gracefully.

**Example:**

```python
# Function to perform calculations
def calculate(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operation."

# Start the calculator loop
while True:
    user_input = input("Enter 'exit' to quit or press Enter to continue: ")
    
    if user_input.lower() == 'exit':
        print("Exiting the calculator. Goodbye!")
        break
    
    # Get user input for numbers and operation
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (add, subtract, multiply, divide): ").lower()
        
        # Perform calculation
        result = calculate(num1, num2, operation)
        print(f"The result is: {result}")
    
    except ValueError:
        print("Error: Please enter valid numbers.")
```

**Sample Output:**

```
Enter 'exit' to quit or press Enter to continue: 
Enter the first number: 10
Enter the second number: 5
Enter the operation (add, subtract, multiply, divide): add
The result is: 15.0
Enter 'exit' to quit or press Enter to continue: 
Enter the first number: 10
Enter the second number: 0
Enter the operation (add, subtract, multiply, divide): divide
The result is: Error: Division by zero is not allowed.
Enter 'exit' to quit or press Enter to continue: exit
Exiting the calculator. Goodbye!
```

This task helps users practice using `while` loops for continuous input and performing basic arithmetic operations in Python.

## Review Questions

**for loop:**
- What is the difference between a for loop and a while loop in Python?
- Can you use a for loop to iterate over a string?

**if statement:**

- Can you have multiple elif blocks in an if-elif-else statement?
- What is the purpose of nesting if statements?
- 
## References and Bibliography

- [1] In Python, an iterable object is an object that you can loop over using a "for" loop. It's any object that can return its elements one at a time.
- [2] “ForLoop - Python Wiki,” Python.org, 2017. https://wiki.python.org/moin/ForLoop
- [3] “4. More Control Flow Tools — Python 3.13.2 documentation,” docs.python.org. <https://docs.python.org/3/tutorial/controlflow.html>
‌

## **Appendices**

### **Appendix A: 