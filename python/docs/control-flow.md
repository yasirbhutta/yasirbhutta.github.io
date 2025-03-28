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

## [5.2 Conditional Statements (if, else, elif)](control-flow/python-if-elif-else.md)

## 5.3 Looping Statements (for, while)
- There are two ways to create loops in Python: with the for-loop and the while-loop.
- Repeat actions using `for` and `while` loops.

### [5.3.1 for loop](control-flow/python-loops-for.md)

### [5.3.2 while loop](control-flow/python-loops-while.md)

## [5.4 Loop Control Statements (break, continue, pass)](control-flow/python-loop-control-statements.md)

## [5.5 The else Clauses on Loops](control-flow/python-else-clauses-on-loops.md)

## [5.6 Match Statement (Python 3.10+)](control-flow/python-match-statement.md)

## Practice & Progress

- [True or False](control-flow/practice-and-progress/control-flow-true-false.md)
- [Fill in the Blanks](control-flow/practice-and-progress/control-flow-fill-blanks.md)

### Multiple-Choice Questions (MCQs)

- [if statement (MCQs)](control-flow/practice-and-progress/python-if-statement-mcqs.md)
- [for loop (MCQs)](control-flow/practice-and-progress/python-loops-for-mcqs.md)
- [while loop (MCQs)](control-flow/practice-and-progress/python-loops-while-mcqs.md)
- [Loop Control Statements (break, continue, pass) (MCQs)](control-flow/practice-and-progress/python-loop-control-statements-mcqs.md)

---

### Find and Fix Mistakes

- [Find and Fix Mistakes](control-flow/practice-and-progress/control-flow-find-fix-mistakes.md)

✅ **Online Quizzes for Python Control Flow Statements**

- [Python if elif else Quiz](../quizzes/python-if-elif-else-quiz.md)
- [Python For Loop Quiz](../quizzes/python-for-loop-quiz.md)
- [Python While Loop Quiz](../quizzes/python-while-loop-quiz.md)
- [ Python Quiz: `break`, `continue` Statements, and `else` Clauses in Loops](../quizzes/python-break-continue-else-loop-quiz.md)

---

### Coding Exercises

- [Python Exercise for if elif else statement](../exercises/python-exercises-if-elif-else.md)
- [Python Exercises for Loops (for,while)](../exercises/python-exercises-loops.md)
- [Loop Control Statements (break, continue, pass) Exercises](../exercises/python-exercises-loop-control.md)

---

### Mini Projects

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

---

### [Review Questions](control-flow/practice-and-progress/control-flow-review-questions.md)

--- 

## References and Bibliography

- [1] In Python, an iterable object is an object that you can loop over using a "for" loop. It's any object that can return its elements one at a time.
- [2] “ForLoop - Python Wiki,” Python.org, 2017. https://wiki.python.org/moin/ForLoop
- [3] “4. More Control Flow Tools — Python 3.13.2 documentation,” docs.python.org. <https://docs.python.org/3/tutorial/controlflow.html>
‌
