---
layout: default
title: --.
description: --.
---

Alright! Here's another Python class example — this time, with **inheritance** — and I'll add mistakes for you to spot and understand. Then I’ll show the corrected version.

---

### **Code with Mistakes (with Inheritance)**
```python
class Animal:
    def __init__(species):
        self.species = species

    def speak():
        print("The animal makes a sound.")

class Dog(Animal):
    def __init__(self, name, species):
        self.name = name
        super().__init__(species)

    def speak(self):
        print("Woof! My name is " + name)

dog1 = Dog("Buddy", "Canine")
dog1.speak()
```

---

### **Mistakes Explained**
1. `__init__(species)` in `Animal` is missing `self`.
2. `speak()` in `Animal` is missing `self`.
3. In `Dog.__init__()`, `self.name = name` is fine, but `super().__init__(species)` is placed **after** it — this is okay, but let's focus on the **next mistake**.
4. In `Dog.speak()`, it uses `name` instead of `self.name`.

---

### **Corrected Version**
```python
class Animal:
    def __init__(self, species):
        self.species = species

    def speak(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def __init__(self, name, species):
        super().__init__(species)
        self.name = name

    def speak(self):
        print("Woof! My name is " + self.name)

dog1 = Dog("Buddy", "Canine")
dog1.speak()
```

---

Would you like a challenge version next? Maybe with class variables, property decorators, or abstract classes?