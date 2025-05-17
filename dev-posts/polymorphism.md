# Polymorphism in Python for Beginners

Polymorphism is a core concept in object-oriented programming (OOP) that allows objects of different classes to be treated as objects of a common superclass. The word "polymorphism" comes from Greek meaning "many forms".

## What is Polymorphism?

Polymorphism lets you:
- Use the same method name across different classes
- Have different implementations of the same method
- Call methods without knowing the exact class of the object

## Types of Polymorphism in Python

1. **Method Overriding**: When a child class provides a different implementation of a method that is already defined in its parent class.

2. **Method Overloading**: Python doesn't support this directly like Java/C++, but we can achieve similar functionality using default arguments or variable-length arguments.

3. **Duck Typing**: "If it walks like a duck and quacks like a duck, it must be a duck" - we don't check types, just behavior.

## Syntax Examples

### 1. Method Overriding Example

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):  # Overriding the speak method
        print("Dog barks")

class Cat(Animal):
    def speak(self):  # Overriding the speak method
        print("Cat meows")

# Polymorphic behavior
animals = [Animal(), Dog(), Cat()]
for animal in animals:
    animal.speak()
```

Output:
```
Animal speaks
Dog barks
Cat meows
```

### 2. Duck Typing Example

```python
class Parrot:
    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:
    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

# Common interface
def flying_test(bird):
    bird.fly()

# Instantiate objects
parrot = Parrot()
penguin = Penguin()

# Polymorphic behavior
flying_test(parrot)
flying_test(penguin)
```

Output:
```
Parrot can fly
Penguin can't fly
```

### 3. Operator Overloading Example

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # Overloading the + operator
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(1, 2)
print(v1 + v2)  # Uses the overloaded + operator
```

Output:
```
Vector(3, 5)
```

## Real-World Example: Payment Processing System

```python
class Payment:
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

class PayPalPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

class BankTransferPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing bank transfer of ${amount}")

def checkout(payment_method, amount):
    payment_method.process_payment(amount)

# Usage
credit_card = CreditCardPayment()
paypal = PayPalPayment()
bank_transfer = BankTransferPayment()

checkout(credit_card, 100)    # Processing credit card payment of $100
checkout(paypal, 50)          # Processing PayPal payment of $50
checkout(bank_transfer, 200)  # Processing bank transfer of $200
```

In this example, the `checkout` function doesn't need to know what specific type of payment method it's using - it just calls `process_payment()`. Each payment type implements this method differently, demonstrating polymorphism.

## Key Benefits of Polymorphism

1. **Code reusability**: Write more generic and reusable code
2. **Flexibility**: Easily extend and modify code
3. **Simplified syntax**: Work with objects at a higher level of abstraction
4. **Maintainability**: Easier to maintain and update code

Polymorphism is a powerful concept that helps make your Python code more flexible and easier to work with as your programs grow in complexity.