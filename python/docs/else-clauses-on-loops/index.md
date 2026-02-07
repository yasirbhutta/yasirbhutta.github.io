---
layout: page
title: Python else Clause in Loops - Master for and while else with Examples
description: Learn how to use the else clause with Python loops. Explore for and while else with examples, syntax, and practical use cases for better control flow understanding..
keywords: Python for loop, Python loop examples, for loop syntax Python, iteration in Python, loop control Python, beginner Python loops, Python range loop, Python programming basics
toc: toc/python.html
prev: /python/docs/control-flow/
next: /python/docs/match-statement/
course: python
topic: else-clauses-on-loops
show_toc: true
show_practice_progress: true
show_mini_project: false
breadcrumb: 
- title: Control Flow Statements
url: /python/docs/python/docs/control-flow/
---
## Table of Contents

1. [The else Clauses on Loops](#1-the-else-clauses-on-loops)
2. [Syntax for Python `else` Clause in Loops](#2-syntax-for-python-else-clause-in-loops)
3. [Example with a `for` loop](#3-example-with-a-for-loop)
4. [Example with a `while` loop](#4-example-with-a-while-loop)

## 1. The else Clauses on Loops

In Python, the `else` clause can be used with loops (`for` and `while`). This may be surprising at first since most people associate `else` with `if` statements. However, in loops, the `else` clause has a unique behavior:

- The `else` block is executed **only if the loop completes all its iterations without encountering a `break` statement**.
- If the loop is exited early because of a `break`, the `else` block is skipped.

The `else` clause in loops (`for` and `while`) in Python is a bit unusual because most people associate `else` with `if` statements. In the context of loops, the `else` clause is executed only when the loop finishes normally, meaning it wasn’t interrupted by a `break` statement.

## 2. Syntax for Python `else` Clause in Loops

The `else` clause can be used with both `for` and `while` loops in Python. Here's the general syntax:

### **For Loop with else**
```python
for item in iterable:
    # Code block to execute for each item
    if condition:
        break  # Exit the loop early
else:
    # Code block to execute if the loop completes without a break
```

### **While Loop with else**

```python
while condition:
    # Code block to execute while the condition is True
    if condition_to_break:
        break  # Exit the loop early
else:
    # Code block to execute if the loop completes without a break
```


**How It Works:**

1. **With a `for` loop**:
   - The `else` block runs if the loop completes all its iterations without hitting a `break`.
   - If the loop is terminated by a `break`, the `else` block is skipped.

2. **With a `while` loop**:
   - The `else` block runs if the `while` loop condition becomes `False` naturally.
   - If the loop is terminated by a `break`, the `else` block is skipped.


### 3. Example with a `for` loop

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

### 4. Example with a `while` loop

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

## 📘 **Related Topics**

* **Python FOR Loops** – A `for` loop in Python is a programming statement that repeats a block of code a fixed number of times.
  👉 [Learn more](../loops-for/)
* **Python while Loops** – A `while` loop in python is a control flow statement that repeatedly executes a block of code until a specified condition is met.
  👉 [Learn more](../loops-while/)
* **Python Loop Control Statements** – Learn about Break, Continue & Pass. 
  👉 [Learn more](../loop-control-statements/)
* **Match Statement (Python 3.10+)** – Introduced in Python 3.10, **`match-case`** is a modern way to handle data-driven decision-making.
  👉 [Learn more](../match-statement/)