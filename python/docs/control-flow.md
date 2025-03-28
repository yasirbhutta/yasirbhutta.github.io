# 5. Python: Flow Control Statements

Connect with me: [Youtube](https://www.youtube.com/yasirbhutta) \| [LinkedIn](https://www.linkedin.com/in/yasirbhutta/) \| [WhatsApp Channel](https://whatsapp.com/channel/0029VaC3BC160eBZZSs3CW0c) \| [Web](https://yasirbhutta.github.io/) \| [Facebook](https://www.facebook.com/yasirbhutta786) \| [Twitter](https://twitter.com/yasirbhutta)

- [📄 Download PDF](https://yasirbhutta.github.io/python/docs/control-flow.pdf)  
- To access the updated handouts, please click on the following link:
[https://yasirbhutta.github.io/python/docs/control-flow.html](https://yasirbhutta.github.io/python/docs/control-flow.html)

## 5.1 Flow control statements

Flow control statements in Python determine the order in which your code is executed. They allow you to make decisions, repeat actions, and control the program's flow based on specific conditions.

**Python has three types of control structures:**

1. Sequential: Default mode
2. Selection: Used for decisions and branching
3. Repetition: Used for looping, i.e., repeating a code multiple times.

for more details, see [Understanding Control Structures in Python](../posts/control-structures-python.md)

**Flow control statements in Python**

## 5.2 [Conditional Statements (if, else, elif)](control-flow/python-if-elif-else.md)
## 5.3 Looping Statements (for, while)
   - There are two ways to create loops in Python: with the for-loop and the while-loop.
   - Repeat actions using `for` and `while` loops.
    ### [5.3.1 for loop](control-flow/python-loops-for.md)
    ### [5.3.2 while loop](control-flow/python-loops-while.md)
## [5.4 Loop Control Statements (break, continue, pass)](control-flow/python-loop-control-statements.md)
## [5.5 The else Clauses on Loops](control-flow/python-else-clauses-on-loops.md)
## [5.6 Match Statement (Python 3.10+)](control-flow/python-match-statement.md)


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

- [Python Exercise for if elif else statement](../exercises/python-exercises-if-elif-else.md)
- [Python Exercises for Loops (for,while)](../exercises/python-exercises-loops.md)
- [Loop Control Statements (break, continue, pass) Exercises](../exercises/python-exercises-loop-control.md)

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