---
layout: page
title: **Structural Pattern Matching in Python (`match-case`): A Beginner’s Guide**
description: Learn how to simplify complex conditional logic with Python’s powerful `match-case` syntax! Introduced in Python 3.10, `match-case` is a modern way to...
keywords: case, print, match, data, matching
---
# **Structural Pattern Matching in Python (`match-case`): A Beginner’s Guide**  
*Learn how to simplify complex conditional logic with Python’s powerful `match-case` syntax!*

---

## **What is Structural Pattern Matching?**  
Introduced in Python 3.10, **`match-case`** is a modern way to handle data-driven decision-making. It goes beyond simple `if-elif-else` chains by letting you check the **structure** of data (like dictionaries, lists, or objects) and extract values from them. Think of it as a supercharged `switch` statement!

---

## **Why Use `match-case`?**  
- 🎯 **Cleaner code**: Replace messy nested `if` statements with readable patterns.  
- 💡 **Extract data**: Directly pull values from complex structures (e.g., JSON).  
- 🛠️ **Handle multiple cases**: Match data types, values, and even conditions in one block.

---

## **Basic Syntax**  
```python
match variable_to_check:
    case Pattern1:
        # Action for Pattern1
    case Pattern2:
        # Action for Pattern2
    case _:
        # Default action
```

---

## **Breaking Down the Example**  
Let’s dissect the sample code:

```python
def process_data(data):
    match data:
        # Case 1: Match a dictionary with "type": "alert" and extract "message"
        case {"type": "alert", "message": msg}:
            print(f"ALERT: {msg}")
        
        # Case 2: Match a list of 3 elements where the first > second
        case [x, y, z] if x > y:
            print(f"First element {x} is larger than {y}")
        
        # Case 3: Match integers or floats, capture as "num"
        case int() | float() as num:
            print(f"Number: {num}")
        
        # Default case: Handle anything else
        case _:
            print("Unknown format")
```

---

## **Real-World Examples**  

### 1. **Processing API Responses**  
Imagine handling JSON data from a weather API:  
```python
response = {
    "status": "success",
    "data": {"temp": 22, "city": "Paris"}
}

match response:
    case {"status": "success", "data": {"temp": t, "city": c}}:
        print(f"Temperature in {c}: {t}°C")
    case {"status": "error", "code": code}:
        print(f"API Error: Code {code}")
    case _:
        print("Unexpected response")
```

---

### 2. **Handling User Commands in a CLI App**  
Process commands like `add 5 3` or `delete user123`:  
```python
command = input("Enter command: ").split()

match command:
    case ["add", x, y]:
        print(f"Result: {int(x) + int(y)}")
    case ["delete", user_id]:
        print(f"Deleting user {user_id}...")
    case _:
        print("Invalid command")
```

---

### 3. **Game Event Handling**  
Manage events in a game (e.g., player actions):  
```python
event = {"type": "move", "direction": "north", "speed": 5}

match event:
    case {"type": "move", "direction": dir}:
        print(f"Player moved {dir}")
    case {"type": "attack", "damage": d} if d > 0:
        print(f"Dealt {d} damage!")
    case _:
        print("Unknown event")
```

---

## **Practice Tasks**  
Test your understanding with these exercises:

### **Task 1: Process Shapes**  
Given a list of shapes like `["circle", 5]` or `["rectangle", 3, 4]`, calculate their area:  
```python
shape = ["circle", 5]

match shape:
    case ["circle", radius]:
        print(f"Area: {3.14 * radius ** 2}")
    case ["rectangle", l, w]:
        print(f"Area: {l * w}")
    case _:
        print("Invalid shape")
```

---

### **Task 2: Validate User Input**  
Check if user input is a valid email or phone number:  
```python
user_input = "user@example.com"

match user_input.split("@"):
    case [name, domain]:
        print("Valid email!")
    case _ if user_input.isdigit() and len(user_input) == 10:
        print("Valid phone number!")
    case _:
        print("Invalid input")
```

---

### **Task 3: Parse Log Messages**  
Extract error levels and messages from log entries:  
```python
log = "ERROR: Disk full"

match log.split(": "):
    case ["ERROR", msg]:
        print(f"Critical error: {msg}")
    case ["WARNING", msg]:
        print(f"Warning: {msg}")
    case _:
        print("Unknown log type")
```

---

## **Key Takeaways**  
1. **Readability**: `match-case` makes complex logic easier to write and understand.  
2. **Patterns**: Match data structures (dicts, lists), types, and values in one go.  
3. **Extraction**: Pull values directly from patterns (e.g., `{"message": msg}`).  
4. **Guards**: Add conditions with `if` for finer control (e.g., `case [x, y] if x > y`).  

---

## **When to Use `match-case`**  
- Parsing JSON/API responses.  
- Handling commands in CLI apps.  
- Processing events in games or GUIs.  
- Validating structured data (forms, config files).  

---

Now go try `match-case` in your projects! 🚀 Start with Python 3.10+ and simplify your conditional logic today.


Introduction to Structural Pattern Matching (match-case) in Python

Structural Pattern Matching, introduced in Python 3.10, is a powerful way to write cleaner and more readable conditional logic. It is similar to switch-case statements in other languages but far more flexible. It allows you to match complex data structures such as dictionaries, lists, and even custom objects.

In this article, you'll learn:

What Structural Pattern Matching is

How to use match-case in Python

Examples to illustrate different use cases

Real-world applications

Tasks to practice



---

Understanding Structural Pattern Matching (match-case)

In simple terms, Structural Pattern Matching lets you compare a variable against multiple patterns and execute code based on which pattern matches.

Syntax:

match variable:
    case pattern1:
        # Execute code for pattern1
    case pattern2:
        # Execute code for pattern2
    case _:
        # Default case (if nothing matches)

Basic Example: Handling Different Data Types

def check_value(value):
    match value:
        case 1:
            print("You entered one!")
        case "hello":
            print("You said hello!")
        case _:
            print("Unknown input")

check_value(1)       # Output: You entered one!
check_value("hello") # Output: You said hello!
check_value(42)      # Output: Unknown input

In this example, different cases handle different input values, and _ acts as the default case.


---

Advanced Examples of match-case

Matching Dictionaries (JSON-like data)

You can match dictionaries by their structure and extract values.

def process_data(data):
    match data:
        case {"type": "alert", "message": msg}:
            print(f"ALERT: {msg}")
        case {"type": "info", "details": details}:
            print(f"INFO: {details}")
        case _:
            print("Unknown format")

process_data({"type": "alert", "message": "Low battery!"})
# Output: ALERT: Low battery!

Here, match checks if data is a dictionary with specific keys.


---

Matching Lists and Tuples

def check_sequence(seq):
    match seq:
        case [x, y, z] if x > y:
            print(f"First element {x} is greater than {y}")
        case [x, y, z]:
            print(f"Three elements found: {x}, {y}, {z}")
        case _:
            print("Unknown sequence")

check_sequence([10, 5, 2])  # Output: First element 10 is greater than 5
check_sequence([1, 2, 3])   # Output: Three elements found: 1, 2, 3

This allows structured unpacking and conditional matching.


---

Matching Data Types

def identify_value(value):
    match value:
        case int() | float() as num:
            print(f"Number: {num}")
        case str() as text:
            print(f"String: {text}")
        case _:
            print("Unknown type")

identify_value(3.14)   # Output: Number: 3.14
identify_value("Hey")  # Output: String: Hey

This case matches data types and assigns them to variables.


---

Real-World Applications of Structural Pattern Matching

1. Parsing JSON Data (API Responses)

APIs often return JSON data with different structures. match-case helps process them effectively.

def api_response_handler(response):
    match response:
        case {"status": "error", "message": msg}:
            print(f"Error: {msg}")
        case {"status": "success", "data": data}:
            print(f"Success! Data: {data}")
        case _:
            print("Unexpected response format")

api_response_handler({"status": "success", "data": {"user": "Alice"}})
# Output: Success! Data: {'user': 'Alice'}


---

2. Command Processing (Chatbots, CLI)

def process_command(command):
    match command.split():
        case ["add", x, y]:
            print(f"Adding {x} and {y}")
        case ["exit"]:
            print("Goodbye!")
        case _:
            print("Invalid command")

process_command("add 5 10")  # Output: Adding 5 and 10
process_command("exit")      # Output: Goodbye!

This is useful for chatbots and command-line applications.


---

3. Event Handling in GUI Applications

def handle_event(event):
    match event:
        case {"type": "click", "x": x, "y": y}:
            print(f"Click at ({x}, {y})")
        case {"type": "keypress", "key": key}:
            print(f"Key pressed: {key}")
        case _:
            print("Unknown event")

handle_event({"type": "click", "x": 50, "y": 100})
# Output: Click at (50, 100)

This helps in GUI programming for event handling.


---

Tasks for Practice

Try solving these problems using match-case:

1. Student Grading System:
Write a function that takes a student's marks and matches it to a grade:

marks >= 90 → "Grade: A"

marks >= 80 → "Grade: B"

marks >= 70 → "Grade: C"

Else → "Fail"



2. E-commerce Order Processing:
Match an order dictionary with:

{"status": "shipped", "tracking": "XYZ123"} → Print tracking number

{"status": "delivered"} → Print "Order delivered"

Default → "Invalid order"



3. Weather Alerts:
Match different weather conditions ({"temp": temp, "condition": "rainy"}) and print appropriate messages.




---

Conclusion

Structural Pattern Matching (match-case) makes Python code cleaner, more readable, and powerful for handling structured data. It's especially useful for JSON processing, event handling, and command processing.

Would you like to try implementing one of the tasks above? Let me know if you need help!

