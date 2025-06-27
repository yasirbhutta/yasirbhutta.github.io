---
layout: page
title: Python Exercises for Beginners - Classes and Objects
description: Practice Python programming with beginner-friendly exercises on classes and objects. Learn to define attributes, methods, and create objects with step-by-step tasks.
toc: toc/python.html
topic: "classes"
course: "python"
prev: /python/docs/classes/practice-and-progress/find-fix-mistakes-classes.html
next: /python/docs/classes/practice-and-progress/mini-projects-classes.html
---

### 🧠 **Exercise: Create a `Book` Class**

**Task**: Write a class called `Book` that represents a book in a library. The class should have:

#### **Attributes**
- `title` (string)
- `author` (string)
- `year` (integer)
- `is_checked_out` (boolean, default is `False`)

#### **Methods**
1. `display_info()`  
   Prints the book's title, author, and year.

2. `check_out()`  
   Sets `is_checked_out` to `True` and prints `"Book has been checked out."`  
   If the book is already checked out, print `"Book is already checked out."`

3. `return_book()`  
   Sets `is_checked_out` to `False` and prints `"Book returned."`  
   If the book wasn't checked out, print `"Book was not checked out."`

---

### ✍️ **Try It Yourself First!**

If you want to check your version, here’s what the output *should* look like when you run this:

```python
book1 = Book("The Alchemist", "Paulo Coelho", 1988)
book1.display_info()

book1.check_out()
book1.check_out()

book1.return_book()
book1.return_book()
```

**Expected Output**:
```
Title: The Alchemist, Author: Paulo Coelho, Year: 1988
Book has been checked out.
Book is already checked out.
Book returned.
Book was not checked out.
```

---
