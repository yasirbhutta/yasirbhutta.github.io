---
layout: page
title: "Python Mini-Project: Guess the Number Game"
description: Build a simple calculator using Python in this beginner-friendly mini project. Learn how to implement basic arithmetic operations like addition, subtraction, multiplication, and division.
keywords: Python calculator project, simple calculator Python, Python mini project for beginners, basic arithmetic in Python, Python calculator code, Python project with source code, calculator app Python, beginner Python coding project
author: Muhammad Yasir Bhutta
course: python
topic: mini-projects
show_toc: true
toc: toc/python.html
show_practice_progress: false
show_mini_project: false
breadcrumb: 
- title: Mini Projects
url: /python/mini-projects/
---


## Python Mini-Project: Guess the Number Game

**Objective:** To create a simple "Guess the Number" game in Python using a `while` loop, demonstrating core programming concepts such as random number generation, user input, conditional statements (`if-elif-else`), and iteration.

**Target Audience:** Students learning introductory Python programming.

**Estimated Time:** 1-2 hours (can be extended with enhancements)

-----

### Project Description:

Students will write a Python program where the computer "thinks" of a secret number within a specified range. The player then tries to guess this number. The program will provide helpful hints (e.g., "Too high\!" or "Too low\!") after each guess, guiding the player until they guess correctly. A `while` loop will be the key to keeping the game running until the correct guess is made.

### Learning Objectives:

Upon completion of this project, students will be able to:

  * Import and use the `random` module to generate random integers.
  * Get and convert user input using `input()` and `int()`.
  * Implement `while` loops for repetitive tasks.
  * Apply `if-elif-else` statements for decision-making.
  * Provide clear and informative output to the user using `print()`.
  * Track and display the number of attempts.
  * Understand basic error handling (optional, but good for discussion).
  * Use f-strings for easy string formatting.

### Project Steps:

**Step 1: The Computer Chooses a Secret Number**

1.  **Import the `random` module:** This module provides functions for generating random numbers.

2.  **Generate a secret number:** Use `random.randint(low, high)` to pick a random integer within a desired range (e.g., between 1 and 100, inclusive). Store this number in a variable (e.g., `secret_number`).

    ```python
    import random

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    # Optional: For testing purposes, you can uncomment the line below to see the secret number
    # print(f"DEBUG: The secret number is {secret_number}")
    ```

**Step 2: Set Up the Game Variables**

1.  **Initialize `num_guesses`:** This variable will keep track of how many attempts the player makes. Start it at `0`.

2.  **Initialize `player_guess`:** This variable will store the player's current guess. Initialize it to a value that *cannot* be the secret number (e.g., `0` or `None`) to ensure the `while` loop starts correctly.

    ```python
    num_guesses = 0
    player_guess = 0 # Initialize to a value that won't match secret_number initially
    ```

**Step 3: Implement the Game Loop (`while` loop)**

1.  **Create the `while` loop:** The loop should continue executing as long as `player_guess` is *not* equal to `secret_number`.

2.  **Inside the loop, get user input:**

      * Prompt the user to enter their guess using `input()`.
      * **Convert the input to an integer:** User input from `input()` is always a string. Use `int()` to convert it to a number so you can compare it with `secret_number`.
      * **Error Handling (Basic):** What if the user types "hello" instead of a number? The `int()` conversion will cause an error (`ValueError`). For now, just have them re-run, or introduce `try-except` (see enhancements).

3.  **Increment `num_guesses`:** After each valid guess, increase the `num_guesses` counter.

4.  **Provide hints using `if-elif-else`:**

      * If `player_guess` is greater than `secret_number`, print "Too high\! Try again."
      * If `player_guess` is less than `secret_number`, print "Too low\! Try again."
      * **Important:** The `while` loop condition (`player_guess != secret_number`) takes care of the "correct guess" scenario. When the guess is correct, the loop will simply terminate.

    <!-- end list -->

    ```python
    while player_guess != secret_number:
        try:
            player_guess_str = input("Guess the number (between 1 and 100): ")
            player_guess = int(player_guess_str)
            num_guesses += 1 # Increment guess count only for valid number input

            if player_guess > secret_number:
                print("Too high! Try again.")
            elif player_guess < secret_number:
                print("Too low! Try again.")
            # If player_guess == secret_number, the loop condition becomes false and the loop exits.

        except ValueError:
            print("Invalid input. Please enter a whole number.")
            # Do NOT increment num_guesses here as it wasn't a valid attempt
    ```

**Step 4: Winning Message**

1.  **Outside the loop:** Once the `while` loop condition (`player_guess != secret_number`) becomes `False` (meaning `player_guess` *is* equal to `secret_number`), the code will continue directly after the loop.

2.  **Congratulate the player:** Print a message announcing their victory.

3.  **Display total guesses:** Use an f-string to clearly show how many attempts it took.

    ```python
    print(f"Congratulations! You guessed the number {secret_number} in {num_guesses} guesses!")
    ```

### Complete Code Example (for reference, students build it step-by-step):

```python
import random

# Step 1: The Computer Chooses a Secret Number
secret_number = random.randint(1, 100)
# print(f"DEBUG: The secret number is {secret_number}") # For testing

# Step 2: Set Up the Game Variables
num_guesses = 0
player_guess = 0 # Initialize to a value that won't match secret_number initially

print("Welcome to the Guess the Number Game!")
print("I'm thinking of a number between 1 and 100.")

# Step 3: Implement the Game Loop (while loop)
while player_guess != secret_number:
    try:
        player_guess_str = input("Enter your guess: ")
        player_guess = int(player_guess_str)
        num_guesses += 1 # Increment guess count for valid number input

        if player_guess > secret_number:
            print("Too high! Try again.")
        elif player_guess < secret_number:
            print("Too low! Try again.")
        # No 'else' needed here, as if it's not high or low, it must be correct,
        # and the loop condition will then be false, causing it to terminate.

    except ValueError:
        print("Invalid input. Please enter a whole number.")
        # If input is not a number, we don't count it as a guess and the loop continues.

# Step 4: Winning Message (This code runs AFTER the loop finishes)
print(f"Congratulations! You guessed the number {secret_number} in {num_guesses} guesses!")
print("Thanks for playing!")
```

### Optional Enhancements:

  * **Robust Input Validation:**
      * Improve the `try-except ValueError` to handle non-integer input gracefully, perhaps in a small helper function.
      * Add a check to ensure the guess is within the valid range (1-100). If not, print a message like "Your guess is out of range\!"
  * **Limiting Guesses:**
      * Introduce a `max_guesses` variable (e.g., 7).
      * Modify the `while` loop condition to also check `num_guesses < max_guesses`.
      * If the player runs out of guesses, print a "Game Over" message and reveal the `secret_number`.
  * **Difficulty Levels:**
      * At the start, ask the player to choose a difficulty (e.g., "Easy", "Medium", "Hard").
      * Based on their choice, set different ranges for `random.randint()` or different `max_guesses`.
  * **Play Again Feature:**
      * Wrap the entire game logic (from Step 1 to Step 4) inside another `while` loop.
      * After the congratulatory message, ask the player `input("Do you want to play again? (yes/no): ")`.
      * If they type "yes", the outer loop continues; otherwise, it breaks.
  * **High Score Tracking (Advanced):**
      * Store the `num_guesses` in a list or even save it to a text file.
      * Read from the file to display the "Best Score" (fewest guesses) at the start of each new game.

### Assessment Ideas:

  * **Code Demo:** Students run their program and explain their code step-by-step.
  * **Explain Concepts:** Ask students to explain:
      * "Why is a `while` loop suitable for this game?"
      * "What does `random.randint()` do?"
      * "Why do we need `int(input(...))`?"
      * "How does the `if-elif-else` structure help the player?"
  * **Debugging Challenge:** Provide them with a version of the code that has a small bug and ask them to find and fix it.
  * **Documentation:** Have students add comments to their code explaining what each section does.

