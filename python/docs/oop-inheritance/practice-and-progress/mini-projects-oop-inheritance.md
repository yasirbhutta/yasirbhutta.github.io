---
layout: page
title: "🧠 Mini Project: School Management System."
description: "Reinforce your Python OOP inheritance knowledge with review questions designed to test your grasp of single, multiple, and multilevel inheritance. Ideal for students and beginners."
keywords: Python OOP review questions, Python inheritance quiz, object-oriented programming questions, Python class inheritance test, OOP MCQs Python, Python inheritance assessment, beginner Python OOP questions, review Python OOP concepts
toc: toc/python.html
topic: "oop-inheritance"
course: "python"
prev: /python/docs/oop-inheritance/practice-and-progress/fill-blanks-oop-inheritance.html
next: /python/docs/oop-inheritance/practice-and-progress/mcqs-oop-inheritance.html
---

## 📌 Objective:
Build a simple School Management System that models **students**, **teachers**, **courses**, and **departments** using **Python classes** and various types of **inheritance**.

---

## 📁 Project Structure:
### 1. **Base Class**
- `Person` – with attributes like `name`, `age`, and `gender`.

### 2. **Single Inheritance**
- `Student(Person)` – add attributes like `student_id`, `grade`, `courses_enrolled`.
- `Teacher(Person)` – add attributes like `teacher_id`, `subjects_taught`.

### 3. **Multilevel Inheritance**
- `GraduateStudent(Student)` – add attributes like `thesis_title`, `advisor_name`.

### 4. **Multiple Inheritance**
- `AdminStaff(Person)`
- `Coordinator(Student, AdminStaff)` – someone who is both a student and staff member.

### 5. **Hierarchical Inheritance**
- `Course` – related to both `Student` and `Teacher`.

---

## ✅ Features to Implement:
- Add and view student and teacher details.
- Enroll a student in a course.
- Assign a teacher to a course.
- Display a list of all courses and their participants.
- Print details using method overriding (e.g., `__str__` or custom methods).

---

## 💡 Concepts Covered:
- Class creation
- Different types of inheritance
- `super()` usage
- Method overriding
- Constructor chaining
- Polymorphism (optional)

## Related resources:
- [Inheritance in Python - Beginner's Guide with Examples](/python/docs/oop-inheritance.html)