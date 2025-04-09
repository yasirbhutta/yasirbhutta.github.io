---
layout: default
title: Coding Exercises for Python Functions: Beginner to Intermediate Challenges.
description: Explore Python function exercises for beginners and intermediates. Practice writing functions, handling inputs, and solving real-world problems with these coding challenges.
---

# Coding Exercises

## Beginner

1. Write a Python program that takes two numbers as input and prints their sum.
  - [**Watch the Solution Now ✨**](https://www.youtube.com/watch?v=CQHXsGnUns0&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=24
2. Write a function `sum3(num1,num3,num3)` that takes three numbers as input and returns the sum.
3. Write a function `SumNum(num1)` that takes a number as input and returns the sum of numbers from 1 to that number (num1).

4. Write a function `sumSquares(x)` that takes a list of numbers as input and returns the sum of their squares.
   
5. Write a function `order_food` that accepts a `main_dish`, an optional `side_dish` with a default value of `"fries"`, and an optional `drink` with a default of `"water"`. Call this function using both positional and keyword arguments.
   
   - **Example:** `order_food("burger")`, `order_food("pizza", drink="soda")`, and `order_food("salad", side_dish="breadsticks", drink="juice")`
  
6. Create a function `introduce` that takes three parameters: `name`, `age`, and `city`. Set default values for `age` to 18 and `city` to "Unknown". Test calling the function with different combinations of arguments.
   
   - **Example:** `introduce("John")`, `introduce("John", 25)`, `introduce("John", 25, "New York")`

7. Define a function `student_profile` that accepts `name`, `grade`, and `subject` with a default value of `"Math"`. Use keyword arguments to call this function in different orders.
   
   - **Example:** `student_profile(grade="A", name="Emma")` and `student_profile("Sophia", "B", subject="History")`

8. Write a function `add_numbers` that takes two numbers and returns their sum.
  
   - **Example:** `add_numbers(3, 5)` should return `8`

9. Write a function `circle_area` that calculates the area of a circle given its radius. Use the formula: area = π * radius² (you can use `3.14` for π).

   - **Example:** `circle_area(3)` should return approximately `28.26`

10.  Write a function `celsius_to_fahrenheit` that takes a temperature in Celsius and converts it to Fahrenheit using the formula: Fahrenheit = Celsius * (9/5) + 32.

   - **Example:** `celsius_to_fahrenheit(25)` should return `77.0`

11. Write a function `is_even` that takes a number and returns `True` if the number is even, and `False` otherwise.

   - **Example:** `is_even(4)` should return `True` and `is_even(7)` should return `False`

12. Write a function `max_of_three` that takes three numbers and returns the largest one.

   - **Example:** `max_of_three(3, 7, 5)` should return `7`

13. Write a function `simple_interest` that calculates simple interest given `principal`, `rate`, and `time` using the formula: interest = (principal * rate * time) / 100.

   - **Example:** `simple_interest(1000, 5, 2)` should return `100.0`

## Intermediate

14. Write a function `is_prime` that checks if a number is prime. A prime number has only two divisors: 1 and itself.

   - **Example:** `is_prime(7)` should return `True` and `is_prime(8)` should return `False`

15. Write a function `factorial` that takes a number and returns its factorial. (Factorial of 5 is `5 * 4 * 3 * 2 * 1 = 120`)
  
   - **Example:** `factorial(5)` should return `120`
  
16. Write a program with three functions:
  
  1. **`isEven(n)`:** This function takes an integer `n` as input and returns `True` if `n` is even and `False` otherwise. You can use the modulo operator (`%`) to check for evenness.
  2. **`printTable(n)`:** This function takes an integer `n` as input and prints its multiplication table. The table should show the product of `n` with each number from 1 to 10, formatted like `n * i = n * i`, where `i` is the current number in the loop.
  3. **`main`:** The main program should:
     - Prompt the user to enter an integer.
     - Use the `isEven(n)` function to check if the entered number is even.
     - If the number is even, call the `printTable(n)` function to print its multiplication table.
     - If the number is odd, print a message indicating the number is odd and not eligible for printing a table.

**Example output:**

```python
Enter an integer: 4
4 is even! Here's its multiplication table:
4 * 1 = 4
4 * 2 = 8
4 * 3 = 12
...
4 * 10 = 40
```

17. Write a function `fibonacci` that takes a number `n` and returns the `n`th number in the Fibonacci sequence.

   - **Example:** `fibonacci(5)` should return `5` (sequence: 0, 1, 1, 2, 3, 5, ...)

