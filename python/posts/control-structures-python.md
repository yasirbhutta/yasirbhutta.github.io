---
layout: page
title: Understanding Control Structures in Python
description: Control structures are the building blocks of any programming language, helping developers control the flow of execution. Python has three fundamental...
keywords: count, control, python, print, structures
---
# Understanding Control Structures in Python

Control structures are the building blocks of any programming language, helping developers control the flow of execution. Python has three fundamental types of control structures: **Sequence, Selection, and Repetition (Looping)**. Let’s explore each with examples. [1]

## 1. Sequence Structure

The sequence structure is the simplest control structure where statements execute one after another in the order they are written.

### Example:
```python
print("Step 1: Start the program")
print("Step 2: Process data")
print("Step 3: End the program")
```
**Output:**
```
Step 1: Start the program
Step 2: Process data
Step 3: End the program
```
In this example, each statement executes sequentially from top to bottom.

## 2. Selection (Decision-Making) Structure

The selection structure allows the program to make decisions based on conditions. In Python, we use `if`, `if-else`, and `if-elif-else` statements for decision-making.

### Example:
```python
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
```
**Output (if input is 20):**
```
You are eligible to vote.
```
**Output (if input is 15):**
```
You are not eligible to vote.
```
The program checks the condition and selects a path accordingly.

## 3. Repetition (Looping) Structure

Repetition structures allow executing a block of code multiple times. Python supports two types of loops: `for` and `while`.

### Example 1: Using `for` loop
```python
for i in range(1, 6):
    print("Iteration", i)
```
**Output:**
```
Iteration 1
Iteration 2
Iteration 3
Iteration 4
Iteration 5
```

### Example 2: Using `while` loop
```python
count = 1
while count <= 5:
    print("Count is", count)
    count += 1
```
**Output:**
```
Count is 1
Count is 2
Count is 3
Count is 4
Count is 5
```
The `while` loop continues executing until the condition `count <= 5` becomes false.

## Conclusion

Understanding control structures is crucial for writing efficient programs. Python provides three main types of control structures:
1. **Sequence** – Executes statements in order.
2. **Selection** – Makes decisions using `if` statements.
3. **Repetition** – Repeats code using loops (`for` and `while`).

## Further Learning

- [Flow Control Statements in Python](../docs/control-flow.md)

## References

- [1] [What are control flow statements in Python? - educative.io](https://www.educative.io/answers/what-are-control-flow-statements-in-python)

