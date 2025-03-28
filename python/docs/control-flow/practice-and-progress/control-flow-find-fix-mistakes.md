# Control Flow Statements: Find and Fix the Mistakes

To learn about Common Errors in Python, see [Common Errors in Python](../posts/common-mistakes-in-python.md)

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
