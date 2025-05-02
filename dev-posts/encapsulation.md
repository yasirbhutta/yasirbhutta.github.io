# Encapsulation in Python for Beginners

Encapsulation is one of the fundamental concepts in object-oriented programming (OOP) that bundles data (attributes) and methods (functions) that operate on that data into a single unit (class). It also restricts direct access to some of an object's components.

## Why We Use Encapsulation

1. **Data Protection**: Prevents accidental modification of data
2. **Control Access**: Allows controlled access to class members
3. **Implementation Hiding**: Hides internal implementation details
4. **Maintainability**: Makes code easier to maintain and modify
5. **Flexibility**: Allows changing internal implementation without affecting other code

## Encapsulation Syntax in Python

Python doesn't have strict access modifiers like some other languages (Java, C++), but it uses naming conventions to indicate access levels:

1. **Public members**: No underscore prefix (e.g., `variable`, `method()`)
2. **Protected members**: Single underscore prefix (e.g., `_variable`, `_method()`)
   - Convention only - still accessible
3. **Private members**: Double underscore prefix (e.g., `__variable`, `__method()`)
   - Name mangling makes it harder to access outside class

## Example of Encapsulation

```python
class BankAccount:
    def __init__(self, account_holder, initial_balance):
        # Public attribute
        self.account_holder = account_holder
        
        # Private attribute (name mangling applies)
        self.__balance = initial_balance
    
    # Public method to access private attribute
    def get_balance(self):
        return self.__balance
    
    # Public method to modify private attribute with validation
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds")
    
    # Protected method (convention only)
    def _internal_processing(self):
        print("Processing internal bank operations")

# Create an object
account = BankAccount("John Doe", 1000)

# Access public attribute
print(account.account_holder)  # Output: John Doe

# Access public method
print(account.get_balance())  # Output: 1000

# Try to access private attribute directly (not recommended)
# This will raise an AttributeError
# print(account.__balance)

# Access private attribute through name mangling (still possible but discouraged)
print(account._BankAccount__balance)  # Output: 1000

# Use public methods to modify private attribute
account.deposit(500)  # Output: Deposited $500. New balance: $1500
account.withdraw(200)  # Output: Withdrew $200. New balance: $1300

# Try invalid operations
account.deposit(-100)  # Output: Invalid deposit amount
account.withdraw(2000)  # Output: Invalid withdrawal amount or insufficient funds
```

## Key Points

1. We use `__` prefix to make attributes/methods private
2. Public methods provide controlled access to private data
3. We can add validation logic in public methods to protect data integrity
4. While Python doesn't enforce strict encapsulation, following these conventions makes your code more maintainable and secure

Remember that in Python, encapsulation is more about convention than enforcement. Developers are expected to respect these naming conventions rather than having the language enforce them strictly.