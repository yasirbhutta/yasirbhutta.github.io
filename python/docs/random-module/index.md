---
layout: page
title: "The `random` Module in Python"
description: Learn how to use the Pandas module in Python for data analysis. Explore functions, examples, and best practices for efficient data manipulation.
keywords: Python Pandas, Pandas module, Pandas tutorial, Python data analysis, Pandas DataFrame, Python data manipulation, Pandas functions, Python library, Pandas examples
author: Muhammad Yasir Bhutta
course: python
topic: pandas
toc: toc/python.html
prev: /python/docs/modules/numpy.html
next: /python/docs/modules/scipy.html
breadcrumb:
  - title: Home
    url: /
  - title: Python
    url: /python/
---

The `random` module in Python is used to generate pseudo-random numbers for various probability distributions. It's commonly used in games, simulations, testing, security, and any application that requires randomness.

## Common Methods with Syntax and Examples

### 1. `random.random()`
Returns a random float number between 0.0 and 1.0 (excluding 1.0).

```python
import random
print(random.random())
# Example output: 0.5488135039273248
```

### 2. `random.randint(a, b)`
Returns a random integer between a and b (inclusive).

```python
print(random.randint(1, 10))
# Example output: 7
```

### 3. `random.choice(sequence)`
Returns a randomly selected element from a non-empty sequence.

```python
colors = ['red', 'green', 'blue']
print(random.choice(colors))
# Example output: 'green'
```

### 4. `random.shuffle(sequence)`
Shuffles the elements of a sequence in place.

```python
cards = ['Ace', 'King', 'Queen', 'Jack']
random.shuffle(cards)
print(cards)
# Example output: ['Queen', 'Ace', 'Jack', 'King']
```

### 5. `random.uniform(a, b)`
Returns a random float number between a and b.

```python
print(random.uniform(1.5, 3.5))
# Example output: 2.783439510426392
```

### 6. `random.sample(population, k)`
Returns a k-length list of unique elements chosen from the population.

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(random.sample(numbers, 3))
# Example output: [5, 9, 2]
```

### 7. `random.randrange(start, stop, step)`
Returns a randomly selected element from range(start, stop, step).

```python
print(random.randrange(0, 100, 5))
# Example output: 65 (which is in 0, 5, 10, ..., 95)
```

## Real-Life Examples of the Random Module

### 1. Dice Rolling Simulator
```python
import random

def roll_dice():
    return random.randint(1, 6)

print("You rolled:", roll_dice())
```

### 2. Password Generator
```python
import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

print("Your new password:", generate_password(12))
```

### 3. Lottery Number Picker
```python
import random

def lottery_numbers(pool_size=49, numbers_to_pick=6):
    return random.sample(range(1, pool_size+1), numbers_to_pick)

print("Lottery numbers:", lottery_numbers())
```

### 4. Random Team Generator
```python
import random

players = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank']
random.shuffle(players)
team1 = players[:len(players)//2]
team2 = players[len(players)//2:]

print("Team 1:", team1)
print("Team 2:", team2)
```

### 5. Random Quiz Question Selector
```python
import random

questions = [
    "What is the capital of France?",
    "Who painted the Mona Lisa?",
    "What is the largest planet in our solar system?",
    "In what year did World War II end?"
]

current_question = random.choice(questions)
print("Your question:", current_question)
```

### 6. Random Discount Generator
```python
import random

def generate_discount():
    return f"{random.randint(5, 50)}% off"

print("Today's special offer:", generate_discount())
```

Remember that the `random` module generates pseudo-random numbers, which are sufficient for most applications but shouldn't be used for cryptographic purposes (for that, use the `secrets` module in Python).

## Multiple Choice (Select the best answer)
 
1. **Assuming that the random module has already been imported. Identify the statement that will not lead to ValueError**
   - A) random.randint(50,10)
   - B) random.randint(5.0,10.0)
   - C) random.randint(5.0,10.01)
   - D) random.randint(5.5,10.5)

**Watch this video for the answer:**

**Answer key (Mutiple Choice):**

## Fill in the Blanks

**Answer Key (Fill in the Blanks):**

## Exercises

## Review Questions

## References and Bibliography
