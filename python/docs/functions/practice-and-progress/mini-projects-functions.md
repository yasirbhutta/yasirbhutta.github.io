---
layout: default
title: "Mini Projects: Build a Number Guessing Game in Python."
description: Learn how to create a number guessing game in Python with this step-by-step guide. Practice loops, conditionals, and random number generation in this fun mini-project.
---

# Mini Projects: Create a Number Guessing Game in Python

**Function Requirements:**
1. Define a function named `guess_number` that takes no parameters.
2. The function should randomly select a number between 1 and 100.
3. Prompt the user to guess the number, providing feedback on whether their guess is too high, too low, or correct.
4. The game should continue until the user guesses the correct number.
5. Once the user guesses correctly, the function should print a congratulatory message and the number of attempts it took.

**Input:**
- User input (guesses) from the console

**Output:**
- Feedback on each guess and a congratulatory message upon a correct guess

### Expected Output

When the user plays the game, the interaction might look like this:

```
Welcome to the Number Guessing Game!
Guess a number between 1 and 100.
Enter your guess: 50
Too low! Try again.
Enter your guess: 75
Too high! Try again.
Enter your guess: 60
Congratulations! You've guessed the number 60 in 3 attempts.
```

### Notes for Beginners

1. **Random Number Generation:** You can use the `random` module to select a random number.
2. **Input Handling:** Use `input()` to get the user's guess and convert it to an integer.
3. **Loops and Conditionals:** This task will help practice loops for continuous guessing and conditionals for feedback
