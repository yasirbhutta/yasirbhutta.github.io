---
layout: default
title: Microsoft Excel MCQs - Test Your Knowledge of Excel Basics
description: Challenge your understanding of Microsoft Excel with these multiple-choice questions. Covering topics like worksheets, workbooks, formulas, shortcuts, and data entry, this quiz is perfect for beginners to assess and improve their Excel skills.
keywords: "Microsoft Excel MCQs, Excel basics quiz, Excel multiple-choice questions, Excel worksheets and workbooks, Excel formulas quiz, Excel shortcuts test, Excel data entry practice, beginner Excel quiz, Excel fundamentals assessment, Microsoft Excel skills test"
author: Muhammad Yasir Bhutta
toc: toc/python-toc.html
topic: "oop-inheritance"
course: "python"
resources:
  - name: Microsoft Excel Basics
    url: https://yasirbhutta.github.io/ms-excel/docs/basics.html
---

<h1>🐍 Python MCQs</h1>

{% assign mcqs = site.data.python.mcqs %}
{% include pap/mcqs-loop.html mcqs=mcqs %}




<!-- ---

### **4. What will be the output of the following code?**

```python
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        print("Hello from Child")

obj = Child()
obj.greet()
```

- A) `Hello from Parent`  
- B) `Hello from Child`  
- C) `Error: greet() is not defined`  
- D) `None`  

**Answer**: B) `Hello from Child`  

---

### **5. What type of inheritance is demonstrated in the following code?**

```python
class A:
    pass

class B(A):
    pass

class C(B):
    pass
```

- A) Single Inheritance  
- B) Multilevel Inheritance  
- C) Multiple Inheritance  
- D) Hierarchical Inheritance  

**Answer**: B) Multilevel Inheritance  

---

### **6. What will be the output of the following code?**

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, discount):
        self.price -= self.price * (discount / 100)

class DigitalProduct(Product):
    def apply_discount(self, discount):
        super().apply_discount(discount)
        print(f"Discount applied to {self.name}")

ebook = DigitalProduct("E-Book", 50)
ebook.apply_discount(10)
print(ebook.price)
```

- A) `Discount applied to E-Book`  
     `50`  
- B) `Discount applied to E-Book`  
     `45.0`  
- C) `50`  
- D) `45.0`  

**Answer**: B) `Discount applied to E-Book`  
     `45.0`  

---

### **8. What will be the output of the following code?**

```python
class A:
    def display(self):
        print("A's display")

class B(A):
    def display(self):
        print("B's display")
        super().display()

obj = B()
obj.display()
```

- A) `A's display`  
- B) `B's display`  
- C) `B's display`  
     `A's display`  
- D) `Error: display() is not defined`  

**Answer**: C) `B's display`  
     `A's display`  

---

### **9. Which of the following is an example of hierarchical inheritance?**
- A)  
```python
class A:
    pass

class B(A):
    pass

class C(B):
    pass
```
- B)  
```python
class A:
    pass

class B(A):
    pass

class C(A):
    pass
```
- C)  
```python
class A:
    pass

class B:
    pass

class C(A, B):
    pass
```
- D)  
```python
class A:
    pass

class B:
    pass

class C:
    pass
```

**Answer**: B)  
```python
class A:
    pass

class B(A):
    pass

class C(A):
    pass
```
 -->
