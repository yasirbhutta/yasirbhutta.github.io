---

# **Exception Groups & `except*` in Python 3.11+**  
*A Beginner’s Guide to Handling Multiple Errors at Once*  

---

## **What Are Exception Groups and `except*`?**  
In Python 3.11+, **`ExceptionGroup`** and **`except*`** were introduced to simplify handling multiple exceptions raised **concurrently** (e.g., in parallel tasks or asynchronous code).  

- **ExceptionGroup**: A container that holds multiple exceptions.  
- **`except*`**: Catches specific exception types *within* the group, allowing you to handle each type separately.  

This is especially useful in modern Python apps using `asyncio` or multithreading, where multiple errors can occur simultaneously.  

---

## **Why Use `ExceptionGroup` and `except*`?**  
Before Python 3.11, handling multiple exceptions required complex workarounds. Now:  
- 🛠️ **Handle errors granularly**: Process each exception type in the group individually.  
- 🧩 **Structured code**: Avoid nested `try-except` blocks for concurrent tasks.  
- 🔍 **Clarity**: See all errors at once instead of stopping at the first failure.  

---

## **Basic Syntax**  
### Raising an ExceptionGroup  
```python
try:
    # Raise a group of exceptions
    raise ExceptionGroup(
        "error messages",  # Description of the group
        [ValueError("Invalid value"), TypeError("Wrong type")]  # List of exceptions
    )
except* ValueError as eg:  # Catch all ValueErrors in the group
    print(f"Handled ValueError: {eg.exceptions}")
except* TypeError as eg:    # Catch all TypeErrors in the group
    print(f"Handled TypeError: {eg.exceptions}")
```

### Output:  
```
Handled ValueError: (ValueError('Invalid value'),)
Handled TypeError: (TypeError('Wrong type'),)
```

---

## **Real-World Examples**  

### 1. **Handling Async API Requests**  
Imagine fetching data from multiple URLs concurrently. Some requests might fail with different errors:  
```python
import asyncio

async def fetch_data(url):
    # Simulate errors
    if "example.com" in url:
        raise ValueError("Invalid URL")
    else:
        raise TypeError("Data format mismatch")

async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            task1 = tg.create_task(fetch_data("https://example.com"))
            task2 = tg.create_task(fetch_data("https://api.com"))
    except* ValueError as eg:
        print(f"URL errors: {eg.exceptions}")
    except* TypeError as eg:
        print(f"Data errors: {eg.exceptions}")

asyncio.run(main())
```

---

### 2. **Validating User Inputs**  
Process a form where multiple fields might have invalid data:  
```python
def validate_form(data):
    errors = []
    if not data["name"].isalpha():
        errors.append(ValueError("Name must be alphabetic"))
    if not isinstance(data["age"], int):
        errors.append(TypeError("Age must be an integer"))
    if errors:
        raise ExceptionGroup("Form errors", errors)

try:
    validate_form({"name": "Alice123", "age": "30"})
except* ValueError as eg:
    print(f"Validation errors: {eg.exceptions}")
except* TypeError as eg:
    print(f"Type errors: {eg.exceptions}")
```

---

## **Practice Tasks**  

### **Task 1: Process Payment Errors**  
Handle a payment system where transactions can fail with `NetworkError` or `InvalidAmountError`:  
```python
class NetworkError(Exception): pass
class InvalidAmountError(Exception): pass

errors = [
    NetworkError("Connection timeout"),
    InvalidAmountError("Amount must be positive")
]

try:
    raise ExceptionGroup("Payment failed", errors)
except* NetworkError:
    print("Retry payment due to network issues")
except* InvalidAmountError:
    print("Fix the payment amount")
```

---

### **Task 2: Parse Mixed Data**  
Clean a dataset that might have both `ValueError` (invalid numbers) and `KeyError` (missing fields):  
```python
data = [
    {"value": "5"}, 
    {"value": "abc"}, 
    {}  # Missing "value"
]

errors = []
for entry in data:
    try:
        int(entry["value"])
    except Exception as e:
        errors.append(e)

if errors:
    raise ExceptionGroup("Data errors", errors)
```

---

### **Task 3: Handle Remaining Exceptions**  
Use a "catch-all" `except*` to handle unprocessed errors:  
```python
try:
    raise ExceptionGroup(
        "errors",
        [ValueError("bad value"), OSError("file not found")]
    )
except* ValueError:
    print("Handled ValueError")
except* Exception as eg:  # Catch all other exceptions
    print(f"Other errors: {eg.exceptions}")
```

---

## **Key Takeaways**  
1. **Exception Groups** bundle multiple exceptions into one object.  
2. **`except*`** lets you handle each exception type in the group separately.  
3. **Order matters**: Python checks `except*` clauses from top to bottom.  
4. **Unhandled exceptions** will propagate if not caught.  

---

## **When to Use**  
- Parallel task execution (e.g., `asyncio`, multithreading).  
- Batch processing (e.g., validating multiple inputs at once).  
- APIs/services where multiple errors can occur in a single request.  

---

**Note**: Ensure you’re using Python 3.11+! Check your version with:  
```bash
python --version
```

Now go handle those errors like a pro! 🚀