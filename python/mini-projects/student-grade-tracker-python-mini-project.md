---
layout: page
title: "Student Grade Tracker – Python Mini‑Project for Beginners"
description: Build a hands‑on Student Grade Tracker using Python. Learn to record, update, and calculate student grades with file handling, average scoring, and interactive console features in this beginner-friendly mini-project.
keywords: Python student grade tracker, Python mini project, grade tracking Python, beginner Python projects, student grades console app, Python file handling project, Python average score calculator, Python practice project, grade management Python tutorial
author: Muhammad Yasir Bhutta
course: python
topic: mini-projects
show_toc: true
toc: toc/python.html
show_practice_progress: false
show_mini_project: false
breadcrumb: 
- title: Mini Projects
url: /python/mini-projects/
---

This project uses **lists** and **tuples** to store and manage student records, including their names and grades.  

## **1. Data Structure**  
- A **list** (`students`) stores all student records.  
- Each student is represented as a **tuple** (`(name, grades)`), where:  
  - `name` → String (student's name)  
  - `grades` → List of numbers (student's grades)  

## **2. Functions**  

### **1. `add_student()`**  
- Takes input for student name and grades.  
- Appends the student record (`(name, grades)`) to the `students` list.  

### **2. `calculate_average(grades)`**  
- Takes a list of grades and returns the average.  
- Handles empty lists (returns `0`).  

### **3. `display_students()`**  
- Prints all student records in a formatted way:  
  ```
  Name: Alice | Grades: [90, 85, 95] | Average: 90.00
  Name: Bob   | Grades: [75, 80, 70]  | Average: 75.00
  ```

### **4. `top_performers()`**  
- Computes averages for all students.  
- Sorts students by average (descending order).  
- Displays the top 3 students.  

### **5. `main()` (Menu-Driven Program)**  
- Displays a menu:  
  ```
  1. Add Student  
  2. View All Students  
  3. View Top Performers  
  4. Exit  
  ```  
- Takes user input and calls the appropriate function.  

## **3. Execution Flow**  
1. Initialize `students = []` (empty list).  
2. Call `main()`, which runs in a loop until the user exits.  

---

## **Full Solution Code**  

If you'd like to see the complete implementation, check out the solution file below:  

📄 **[View Full Solution Code](solutions/student-grade-tracker-solution.md)**

### **Why Review the Solution?**  
✔ **Compare your approach** – Did you implement it differently?  
✔ **Debug faster** – Spot mistakes by cross-checking logic.  
✔ **Learn best practices** – See clean code formatting and efficient list/tuple usage.  

💡 **Pro Tip:** Try building the project yourself first, then compare with the solution for maximum learning!  

---

### **Key Takeaways**  
✅ **Lists** store multiple student records.  
✅ **Tuples** hold individual student data (name + grades).  
✅ Functions perform operations like adding, displaying, and ranking students.  
✅ Menu-driven interaction makes it user-friendly.  

This structure helps beginners understand how to **organize data** using lists and tuples effectively. 🚀