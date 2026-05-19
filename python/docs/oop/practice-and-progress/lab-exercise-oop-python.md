Here is a **complete lab assignment with clear requirements, structure, and expected output** for your University Portal OOP task.

---

# 🧪 Lab Task: University Portal System (OOP in Python)

## 🎯 Objective

To design a simple **University Portal System** using Object-Oriented Programming concepts in Python, demonstrating:

* Constructor usage
* Inheritance
* Encapsulation
* Method Overriding
* Polymorphism

---

# 📌 Problem Statement

You are required to build a **University Portal System** where different types of users (Students and Teachers) can log in and access their information.

The system should be designed using a **base class `User`** and two derived classes:

* `Student`
* `Teacher`

Each user type should have its own login behavior and protected data.

---

# 🏗️ Requirements

## 🔷 1. Base Class: User

Create a class `User` with the following:

### Attributes:

* `name`
* `email` (private → encapsulation)
* `password` (private → encapsulation)

### Constructor:

Initialize all attributes using `__init__()`

### Methods:

* `login(email, password)` → default login method
* `show_info()` → display user information (except password)

---

## 🔷 2. Subclass: Student

### Inherits from:

* `User`

### Additional Attributes:

* `roll_no`
* `program`

### Methods:

* Override `login()` method:

  * Show message: `"Student login successful"`
  * Validate email and password
* Override `show_info()`:

  * Display student details

---

## 🔷 3. Subclass: Teacher

### Inherits from:

* `User`

### Additional Attributes:

* `teacher_id`
* `department`

### Methods:

* Override `login()` method:

  * Show message: `"Teacher login successful"`
  * Validate email and password
* Override `show_info()`:

  * Display teacher details

---

# 🔐 Encapsulation Requirement

* Email and password must be **private attributes**
* Access them only through:

  * Getter methods (optional)
  * Internal class methods

👉 Students should NOT access `email` or `password` directly.

---

# 🔁 Polymorphism Requirement

Create a function:

```python
def portal_login(user, email, password):
    user.login(email, password)
```

👉 This function should work for both:

* Student object
* Teacher object

✔ Same method name (`login()`)
✔ Different behavior depending on object type

---

# 🧾 Sample Input/Output

## Example 1: Student Login

```
Student login successful
Welcome: Ali Ahmed
Roll No: 23
Program: BSCS
```

---

## Example 2: Teacher Login

```
Teacher login successful
Welcome: Dr. Khan
Department: Computer Science
Teacher ID: T-102
```

---

# 💻 Expected Implementation Structure

Students should use:

* `__init__()` constructor
* `super()` to call parent constructor
* Method overriding in both subclasses
* Private variables for encapsulation
* Polymorphism through function call

---

# ⭐ Bonus Features (Optional for Extra Marks)

* Add login validation:

  * If email/password is wrong → show `"Invalid credentials"`
* Add `logout()` method
* Store multiple users in a list and loop login attempts

---

# 🧪 Evaluation Criteria (Marks Distribution)

| Concept             | Marks        |
| ------------------- | ------------ |
| Class & Constructor | 5            |
| Inheritance         | 5            |
| Encapsulation       | 5            |
| Method Overriding   | 5            |
| Polymorphism        | 5            |
| Output & Logic      | 5            |
| **Total**           | **30 Marks** |

---

