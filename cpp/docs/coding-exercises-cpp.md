---
layout: page
title: "C++ Coding Exercises"
description: "Practice C++ programming with coding exercises covering variables, data types, operators, input and output, type casting, conditional statements, loops, functions, arrays, and other C++ fundamentals."
keywords: C++ coding exercises, C++ programming exercises, C++ practice exercises, C++ exercises for beginners, C++ programming practice, C++ problem solving, beginner C++ exercises, C++ coding practice
---

## 1. C++ Basics

### **Problem Statement 1: `const` and `#define`**

Write a C++ program to demonstrate the use of **`const`** and **`#define`** for defining constant values.

The program should:

1. Define the value of `PI` using `#define`.
2. Declare a constant integer `DAYS_IN_WEEK` using `const` and assign it the value `7`.
3. Display the values of `PI` and `DAYS_IN_WEEK`.
4. Declare a floating-point variable `radius` and assign it the value `5.0`.
5. Calculate the area of a circle using `PI` and `radius`.
6. Display the radius and calculated area.
7. Include a commented example showing that a `const` variable cannot be changed after initialization.

**Expected Output:**

```text
Value of PI using #define: 3.14159
Days in a week using const: 7
Area of circle with radius 5 is: 78.5397
```

---

### **Problem Statement 2: Explicit Type Casting**

Write a C++ program that:

1. Declares two integer variables `a = 5` and `b = 2`.
2. Declares a third variable `c` of type `float`.
3. Uses **explicit type casting** to convert one of the integer variables to `float` before performing the division.
4. Stores the division result in variable `c`.
5. Displays the value of `c`.

### Expected Output

```text
2.5
```

---

## 2. Input and Output

### Problem Statement 1: – Student Information

Write a C++ program that takes the student's **name, age, and marks** as input and displays them using `cout`.

---

### Problem Statement 2: – Calculate Total

Write a C++ program that takes the prices of three items from the user, calculates the total, and displays the result.

---

### Problem Statement 3: – Calculate Rectangle Perimeter

Write a C++ program that takes the length and width of a rectangle and calculates:

```text
Perimeter = 2 × (Length + Width)
```

Display the result using `cout`.

---

### Problem Statement 4: – Calculate Average

Write a C++ program that takes marks of three subjects, calculates the average, and displays the result.

---

### Problem Statement 5: – Student Age

Write a C++ program that asks the user to enter their age and displays:

```text
Your age is: 20
```

---

### Problem Statement 6: – Two Numbers

Write a C++ program that takes two integers from the user and displays their:

* Sum
* Difference
* Product

---

### Problem Statement 7: – Student Marks

Write a C++ program that takes marks of three subjects and displays the total marks.

### Problem Statement 8: – Rectangle

Write a C++ program that takes the length and width of a rectangle and calculates its area.

Formula:

```text
Area = Length × Width
```
---

### Problem Statement 9: – Student Information

Write a C++ program that takes the following information from the user:

* Name
* Age
* Department
* Marks

Then display all the information using `cout`.

---

### Problem Statement 10: – `endl`

Write a C++ program that displays your:

* Name
* Department
* Semester

Use `endl` to print each item on a separate line.

---

### Problem Statement 11: – `setw`

Write a C++ program to display the following table using `setw(10)`:

```text
Number    Cube
2         8
3         27
4         64
5         125
```

### Problem Statement 12: – Both Manipulators

Write a C++ program that uses both `endl` and `setw()` to display a simple student information table containing:

* Roll No.
* Name
* Marks

## 3. Conditional Statements

### Problem Statement 1: Positive, Negative or Zero - if statement

Write a C++ program that takes a number as input and checks whether it is positive, negative, or zero. Display the appropriate message based on the entered number.

**Hint:** Use an if-else-if ladder.

### Problem Statement 2:  Check Even or Odd - if statement

Write a C++ program that takes an integer as input and determines whether it is even or odd. Display an appropriate message based on the result.

**Hint:** Use the modulus operator (%) to check the remainder when the number is divided by 2.

### Problem Statement 3:  Check Eligibility Based on Marks - if statement

Write a C++ program that takes a student's marks as input. If the marks are 50 or above, display "Eligible"; otherwise, display "Not Eligible".

**Hint:** Use an if-else statement to check the marks.

### Problem Statement 4: Student Grade Calculator - if statement

Write a C++ program that takes a student's marks as input and displays the corresponding grade according to the following criteria:

- **A:** 80–100 marks
- **B:** 70–79 marks
- **C:** 60–69 marks
- **D:** 50–59 marks
- **Fail:** Below 50 marks

If the entered marks are less than 0 or greater than 100, display **"Invalid Marks"**.

**Hint:** Use an `if-else-if` ladder to check the marks and assign the appropriate grade. First, validate that the marks are between 0 and 100.

### Problem Statement 5: Find the Larger Number - if statement

Write a C++ program that takes two numbers as input and compares them. Display the larger number. If both numbers are equal, display "Both numbers are equal."

**Hint:** Use an if-else-if ladder to compare the two numbers and handle all three possible cases.

### Problem Statement 6: Login Authentication System - if statement

Write a C++ program that takes two inputs: a user verification flag and a password verification flag. Display "Login Successful" only if both flags indicate that the username and password are correct. Otherwise, display "Login Failed".

**Hint:** Use nested if statements to check the user verification flag first and then the password verification flag.

### Problem Statement 7:  Scholarship Eligibility Checker - if statement

Write a C++ program that takes a student's marks and family monthly income as input. The student is eligible for a scholarship only if both of the following conditions are met:

- The student's marks are 80 or above.
- The family's monthly income is below Rs. 60,000.

Display "Scholarship Awarded" if the student meets both conditions. Otherwise, display "Not Eligible for Scholarship".

**Hint:** Use nested if statements to check the marks first and then the family income.

 Course Registration

### Problem Statement 8: Student Registration Eligibility - if statement

Write a C++ program that takes three inputs to check whether a student can register:

- **Admission Status:** Admission is confirmed.
- **Fee Status:** Required fee has been paid.
- **Document Verification Status:** All required documents have been verified.

Display **"Registration Allowed"** only if all three requirements are satisfied. Otherwise, display **"Registration Not Allowed"**.

**Hint:** Use nested `if` statements with appropriate `else` branches to check each requirement one by one.
