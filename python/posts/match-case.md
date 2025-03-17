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