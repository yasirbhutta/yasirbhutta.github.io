---
layout: page
title: "Mini Projects While Loop in Python"
description: Learn how to use the SUM function and AutoSum in Microsoft Excel to quickly add values across cells, columns, or rows. Includes syntax, examples, and tips for efficient usage.
keywords: Excel SUM function, how to use SUM in Excel, Excel functions guide, Excel SUM formula, Excel add cells, Excel basics, Excel tutorials, Microsoft Excel functions, SUM formula examples
author: Muhammad Yasir Bhutta
course: ms-excel
topic: functions
show_toc: false
toc: toc/ms-excel-toc.html
show_practice_progress: false
show_mini_project: false
prev: /ms-excel/docs/functions/what-is-functions.html
next: /ms-excel/docs/functions/sumif.html
breadcrumb:
  - title: Home
    url: /
  - title: Excel
    url: /ms-excel/
  - title: Functions
    url: /ms-excel/docs/functions.html
---

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
