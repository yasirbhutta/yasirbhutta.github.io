---
layout: page
title: "Student Grade Tracker Solution – Python Mini Project with Code"
description: Explore the complete Python solution for the Student Grade Tracker mini project. Learn how to implement grade entry, calculation, and file-based data management with clean and beginner-friendly code.
keywords: Python student grade tracker solution, Python mini project code, grade tracker Python example, student grade management Python, Python file handling project, beginner Python project solution, Python grading system, Python student record program
author: Muhammad Yasir Bhutta
course: python
topic: mini-projects
show_toc: true
toc: toc/python.html
show_practice_progress: false
show_mini_project: false
breadcrumb:
  - title: Home
    url: /
  - title: Python
    url: /python/
  - title: Mini Projects
    url: /python/mini-projects/
---

[Project Details](../student-grade-tracker-python-mini-project.md)

This beginner-friendly Python project focuses on using lists and tuples to create a simple student grade tracking system. It will help you practice basic operations with these data structures.

## Project Description
Create a program that allows users to:
1. Add student records (name and grades)
2. Calculate average grades
3. Find top-performing students
4. Display all student records

## Implementation Steps

### Step 1: Initialize Data Structures
```python
# List to store student records (each record is a tuple)
students = []
```

### Step 2: Add Student Function
```python
def add_student():
    name = input("Enter student name: ")
    grades = []
    print("Enter grades (enter 'done' when finished):")
    while True:
        grade = input("Grade: ")
        if grade.lower() == 'done':
            break
        try:
            grades.append(float(grade))
        except ValueError:
            print("Please enter a valid number or 'done'")
    
    # Store as a tuple (name, list of grades)
    students.append((name, grades))
    print(f"Student {name} added successfully!")
```

### Step 3: Calculate Average Grade
```python
def calculate_average(grades):
    return sum(grades) / len(grades) if grades else 0
```

### Step 4: Display All Students
```python
def display_students():
    if not students:
        print("No students in the system.")
        return
    
    print("\nStudent Records:")
    print("-" * 30)
    for student in students:
        name, grades = student
        avg = calculate_average(grades)
        print(f"Name: {name} | Grades: {grades} | Average: {avg:.2f}")
    print("-" * 30)
```

### Step 5: Find Top Performers
```python
def top_performers():
    if not students:
        print("No students in the system.")
        return
    
    # Create a list of tuples (average, name) for sorting
    averages = [(calculate_average(grades), name) for name, grades in students]
    averages.sort(reverse=True)
    
    print("\nTop Performers:")
    print("-" * 30)
    for avg, name in averages[:3]:  # Display top 3
        print(f"{name}: {avg:.2f}")
    print("-" * 30)
```

### Step 6: Main Menu
```python
def main():
    while True:
        print("\nStudent Grade Tracker")
        print("1. Add Student")
        print("2. View All Students")
        print("3. View Top Performers")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            top_performers()
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

