# Control Flow Statements in Python: Mini Projects

## Project #1: Simple Calculator

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
