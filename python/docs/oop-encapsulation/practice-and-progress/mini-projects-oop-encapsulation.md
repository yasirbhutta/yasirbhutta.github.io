---
layout: page
title: "🧠 Mini Projects on Python Encapsulation – Apply OOP Concepts in Real Code"
description: "Explore hands-on mini projects focused on encapsulation in Python. Apply object-oriented programming concepts like private attributes, access modifiers, and method control through practical coding challenges and real-world examples."
keywords: python encapsulation, mini projects python, oop mini projects, python project-based learning, python encapsulation practice, object-oriented programming, python private variables, python access modifiers, python classes, python coding projects, python oop challenges, yasirbhutta
toc: toc/python.html
topic: "oop-encapsulation"
course: "python"
prev: /python/docs/oop-encapsulation/practice-and-progress/exercises-oop-encapsulation.html
next: /python/docs/oop-encapsulation/practice-and-progress/review-questions-oop-encapsulation.html
---

### **Project: Bank Account Manager with Encapsulation**  
**Objective**: Create a `BankAccount` class that properly encapsulates all account details and provides controlled access through methods.

#### **Features to Implement**:
1. **Private Attributes**:
   - `__account_number` (generated automatically)
   - `__balance` (cannot be accessed directly)
   - `__transaction_history` (list of transactions)

2. **Public Methods**:
   - `deposit(amount)` (with validation for positive amounts)
   - `withdraw(amount)` (prevent overdrafts)
   - `get_balance()` (read-only access)
   - `view_transactions()` (returns a copy of history)

3. **Bonus**:
   - Add a `@property` for `account_number` (read-only).
   - Use a class variable to auto-generate account numbers.

---

### **Starter Code (with Intentional Gaps for Students to Fix)**  
```python
class BankAccount:
    __next_account_number = 1000  # Class variable for auto-generating account numbers

    def __init__(self, initial_balance):
        self.__account_number = BankAccount.__next_account_number
        BankAccount.__next_account_number += 1
        self.__balance = initial_balance
        self.__transaction_history = []

    # TODO: Add deposit() method with validation
    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be positive!")
        else:
            self.__balance += amount
            self.__transaction_history.append(f"Deposited ${amount}")

    # TODO: Add withdraw() method with overdraft protection
    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be positive!")
        elif amount > self.__balance:
            print("Insufficient funds!")
        else:
            self.__balance -= amount
            self.__transaction_history.append(f"Withdrew ${amount}")

    # TODO: Add get_balance() (read-only)
    @property
    def balance(self):
        return self.__balance

    # TODO: Add view_transactions() (returns a copy)
    def view_transactions(self):
        return self.__transaction_history.copy()

    # Bonus: Read-only property for account_number
    @property
    def account_number(self):
        return self.__account_number
```

---

### **Tasks for Students**  
1. **Implement Missing Methods**:  
   - Complete the `deposit()` and `withdraw()` methods with validation.  
   - Add the `get_balance()` method using `@property`.  

2. **Fix Encapsulation Issues**:  
   - Ensure `__balance` and `__transaction_history` cannot be modified directly.  
   - Return a **copy** of `__transaction_history` to prevent external modifications.  

3. **Test the Code**:  
   ```python
   # Test Case
   account = BankAccount(100)
   account.deposit(50)
   account.withdraw(30)
   print(f"Balance: ${account.balance}")  # Should show $120
   print(f"Transactions: {account.view_transactions()}")
   ```

---

### **Expected Output**  
```
Balance: $120
Transactions: ['Deposited $50', 'Withdrew $30']
```

---

### **Key Concepts Practiced**  
✅ **Private Attributes** (`__balance`, `__transaction_history`)  
✅ **Getter Methods** (`@property` for read-only access)  
✅ **Validation** (prevent negative deposits/withdrawals)  
✅ **Immutable Returns** (copy of transaction history)  

**Bonus Challenge**:  
- Add a `transfer(to_account, amount)` method that validates balances before transferring.  

---
