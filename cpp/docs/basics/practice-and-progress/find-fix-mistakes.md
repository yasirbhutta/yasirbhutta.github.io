---
layout: page
title: "C++ Basics: Fix the Mistake"
description: "Practice identifying and correcting common C++ beginner mistakes in syntax, variables, operators, and output with simple debugging exercises."
keywords: C++ debugging exercises, fix C++ mistakes, common C++ errors, beginner C++ practice, C++ syntax errors, variable mistakes in C++, output mistakes in C++, C++ programming exercises, learning C++ by debugging, C++ basics practice
---

## Instructions

For each question:

1. Read the problem statement.
2. Examine the given code carefully.
3. Identify the mistake or mistakes.
4. Explain why the code is incorrect.
5. Correct the code.
6. Compile and run the corrected program.
7. Explain how your correction solves the problem.

**Important:** Try to find the mistake yourself before checking the solution.

---

<!-- # Section 1: Basic Syntax Errors -->

## Question 1: Missing Semicolon

**Task:** Find and fix the mistake in the following program.

### Incorrect Code

```cpp
#include <iostream>
using namespace std;

int main()
{
    cout << "Hello World"

    return 0;
}
```
## Question 2: Incorrect Data Type

**Task:** The program should store and display a student's age.

### Incorrect Code

```cpp
#include <iostream>
using namespace std;

int main()
{
    string age = 20;

    cout << "Age: " << age << endl;

    return 0;
}
```
## Question 3: Incorrect Variable Assignment

**Task:** The program should store a student's marks as a decimal value.

### Incorrect Code

```cpp
#include <iostream>
using namespace std;

int main()
{
    float marks;
    marks = "85.5";

    cout << "Marks: " << marks << endl;

    return 0;
}
```
## Question 4: Incorrect Character Declaration

**Task:** The program should store and display a student's grade.

### Incorrect Code

```cpp
#include <iostream>
using namespace std;

int main()
{
    char grade = "A";

    cout << "Grade: " << grade << endl;

    return 0;
}
```
## Question 5: Incorrect Integer Declaration

**Task:** The program should store the number of students in a classroom.

### Incorrect Code

```cpp
#include <iostream>
using namespace std;

int main()
{
    float students = 45.5;

    cout << "Total Students: " << students << endl;

    return 0;
}
```
## Question 6: Missing Header File

**Task:** The program should store and display a student's name.

### Incorrect Code

```cpp
#include <iostream>
using namespace std;

int main()
{
    string name = "Ali";

    cout << "Student Name: " << name << endl;

    return 0;
}
```
<!-- ### Intermediate Level -->

## Question 7: Incorrect Data Type for Average

**Task:** The program should calculate the average of three numbers and display the decimal result.

### Incorrect Code

```cpp
#include <iostream>
using namespace std;

int main()
{
    int a = 10;
    int b = 15;
    int c = 20;

    int average = (a + b + c) / 3.0;

    cout << "Average: " << average << endl;

    return 0;
}
```
## Question 8: Incorrect Data Types for Student Information

**Task:** The program should store a student's name, age, and percentage.

### Incorrect Code

```cpp
#include <iostream>
#include <string>
using namespace std;

int main()
{
    int name = "Ahmed";
    string age = "20";
    int percentage = 85.75;

    cout << name << endl;
    cout << age << endl;
    cout << percentage << endl;

    return 0;
}
```
## Question 9: Incorrect Data Type for Distance

**Task:** The program should store the distance between two cities in kilometres, including decimal values.

### Incorrect Code

```cpp
#include <iostream>
using namespace std;

int main()
{
    int distance = 125.75;

    cout << "Distance: " << distance << " km" << endl;

    return 0;
}
```
## Question 10: Incorrect Data Type for Boolean

**Task:** The program should store and display whether a student is enrolled or not.

### Incorrect Code

```cpp
#include <iostream>
using namespace std;

int main()
{
    int isEnrolled = true;

    cout << "Enrollment Status: " << boolalpha
         << isEnrolled << endl;

    return 0;
}
```
## Question 11: Incorrect Data Type in Calculation

**Task:** The program should calculate the total price of three items, where each item costs 45.75.

### Incorrect Code

```cpp
#include <iostream>
using namespace std;

int main()
{
    int price = 45.75;
    int quantity = 3;

    int total = price * quantity;

    cout << "Total Price: " << total << endl;

    return 0;
}
```
<!-- ## Topic 2: Operators (10 Questions) -->

<!-- ### Beginner Level -->

## Question 12: Incorrect Assignment Operator

**Task:** The program should increase the value of a number by 5.

### Incorrect Code

```cpp
#include <iostream>
using namespace std;

int main()
{
    int number = 10;

    number + 5;

    cout << "Number: " << number << endl;

    return 0;
}
```

## Question 13: Incorrect Multiplication Operator

**Task:** The program should calculate the product of two numbers.

### Incorrect Code

```cpp
#include <iostream>
using namespace std;

int main()
{
    int a = 8;
    int b = 5;

    int product = a + b;

    cout << "Product: " << product << endl;

    return 0;
}
```
## Question 14: Incorrect Modulus Operator

**Task:** The program should calculate the remainder when 17 is divided by 5.

### Incorrect Code

```cpp
#include <iostream>
using namespace std;

int main()
{
    int a = 17;
    int b = 5;

    int remainder = a / b;

    cout << "Remainder: " << remainder << endl;

    return 0;
}
```
<!-- ### Intermediate Level -->

## Question 15: Incorrect Increment Operator

**Task:** The program should increase a number by one using the increment operator.

### Incorrect Code

```cpp
#include <iostream>
using namespace std;

int main()
{
    int number = 10;

    number--;

    cout << "Number: " << number << endl;

    return 0;
}
```

<!-- ## Topic 3: Operator Precedence (10 Questions) -->

<!-- ### Beginner Level -->

## Question 16: Incorrect Calculation Order

**Task:** The program should add two numbers first and then multiply the sum by 3.

### Incorrect Code

```cpp
#include <iostream>
using namespace std;

int main()
{
    int a = 5;
    int b = 10;

    int result = a + b * 3;

    cout << "Result: " << result << endl;

    return 0;
}
```
## Question 17: Incorrect Average Calculation

**Task:** The program should calculate the average of three numbers.

### Incorrect Code

```cpp
#include <iostream>
using namespace std;

int main()
{
    int a = 10;
    int b = 20;
    int c = 30;

    int average = a + b + c / 3;

    cout << "Average: " << average << endl;

    return 0;
}
```
## Question 18: Incorrect Multiplication and Addition

**Task:** The program should multiply two numbers first and then add 10 to the result.

### Incorrect Code

```cpp
#include <iostream>
using namespace std;

int main()
{
    int a = 5;
    int b = 4;

    int result = a + b * 10;

    cout << "Result: " << result << endl;

    return 0;
}
```
## Question 19: Incorrect Division and Subtraction

**Task:** The program should subtract 5 from 20 and then divide the result by 3.

### Incorrect Code

```cpp
#include <iostream>
using namespace std;

int main()
{
    int a = 20;
    int b = 5;
    int c = 3;

    int result = a - b / c;

    cout << "Result: " << result << endl;

    return 0;
}
```
<!-- ### Intermediate Level -->

## Question 20: Incorrect Mathematical Expression

**Task:** The program should calculate the product of the sum of `a` and `b` and the difference of `c` and `d`.

### Incorrect Code

```cpp
#include <iostream>
using namespace std;

int main()
{
    int a = 5;
    int b = 3;
    int c = 10;
    int d = 4;

    int result = a + b * c - d;

    cout << "Result: " << result << endl;

    return 0;
}
```

## Question 21: Incorrect Expression with Modulus

**Task:** The program should calculate the remainder of the sum of two numbers divided by 5.

### Incorrect Code

```cpp
#include <iostream>
using namespace std;

int main()
{
    int a = 7;
    int b = 8;

    int result = a + b % 5;

    cout << "Remainder: " << result << endl;

    return 0;
}
```
## Question 22: Incorrect Expression with Multiple Operators

**Task:** The program should calculate:

\\[ (a+b)\times 2-c \\]

### Incorrect Code

```cpp
#include <iostream>
using namespace std;

int main()
{
    int a = 4;
    int b = 6;
    int c = 5;

    int result = a + b * 2 - c;

    cout << "Result: " << result << endl;

    return 0;
}
```
## Question 23: Incorrect Percentage Calculation

**Task:** The program should calculate the percentage obtained by a student.

### Incorrect Code

```cpp
#include <iostream>
using namespace std;

int main()
{
    int obtained = 400;
    int total = 500;

    double percentage = obtained / total * 100;

    cout << "Percentage: " << percentage << "%" << endl;

    return 0;
}
```

<!-- ## Topic 4: Constants (10 Questions) -->

<!-- ### Beginner Level -->

## Question 24: Missing Constant Initialization

**Task:** The program should declare a constant for PI and display its value.

### Incorrect Code

```cpp
#include <iostream>
using namespace std;

int main()
{
    const double PI;

    PI = 3.14159;

    cout << "PI: " << PI << endl;

    return 0;
}
```
## Question 25: Changing a Constant

**Task:** The program should calculate the area of a square using a constant side length.

### Incorrect Code

```cpp
#include <iostream>
using namespace std;

int main()
{
    const int SIDE = 5;

    SIDE = 10;

    int area = SIDE * SIDE;

    cout << "Area: " << area << endl;

    return 0;
}
```
## Question 26:

**Task:** The program should declare the value of a week as a constant and display the number of days.

### Incorrect Code

```cpp
#include <iostream>
using namespace std;

int main()
{
    int DAYS_IN_WEEK = 7;

    cout << "Days in a week: "
         << DAYS_IN_WEEK << endl;

    return 0;
}
```

<!-- ### Intermediate Level -->

## Question 27: Changing Constant During Calculation

**Task:** The program should calculate the total price of five items using a constant item price.

### Incorrect Code

```cpp
#include <iostream>
using namespace std;

int main()
{
    const double PRICE = 150.50;
    int quantity = 5;

    PRICE = PRICE * quantity;

    cout << "Total Price: " << PRICE << endl;

    return 0;
}
```
## Question 28: Incorrect Constant Initialization

**Task:** The program should calculate the circumference of a circle using a constant PI value.

### Incorrect Code

```cpp
#include <iostream>
using namespace std;

int main()
{
    const double PI = 3.14159;
    double radius = 5;

    const double circumference;

    circumference = 2 * PI * radius;

    cout << "Circumference: "
         << circumference << endl;

    return 0;
}
```

<!-- ## Topic 5: Type Casting (10 Questions) -->

<!-- ### Beginner Level -->

## Question 29: Integer Division

**Task:** The program should divide two integer numbers and display the decimal result.

### Incorrect Code

```cpp
#include <iostream>
using namespace std;

int main()
{
    int a = 7;
    int b = 2;

    double result = a / b;

    cout << "Result: " << result << endl;

    return 0;
}
```
## Question 30: Incorrect Type Conversion

**Task:** The program should convert an integer value into a decimal value.

### Incorrect Code

```cpp
#include <iostream>
using namespace std;

int main()
{
    int number = 15;

    double result = int(number / 2);

    cout << "Result: " << result << endl;

    return 0;
}
```
## Question 31: Incorrect Character Conversion

**Task:** The program should convert an integer ASCII code into its corresponding character.

### Incorrect Code

```cpp
#include <iostream>
using namespace std;

int main()
{
    int code = 65;

    int character = char(code);

    cout << "Character: " << character << endl;

    return 0;
}
```

<!-- ### Intermediate Level -->

## Question 32: Missing Type Casting in Average

**Task:** The program should calculate the average of three integers and display the decimal result.

### Incorrect Code

```cpp
#include <iostream>
using namespace std;

int main()
{
    int a = 10;
    int b = 20;
    int c = 25;

    double average = (a + b + c) / 3;

    cout << "Average: " << average << endl;

    return 0;
}
```

## Question 33: Incorrect Type Casting Position

**Task:** The program should calculate the average of three numbers using type casting.

### Incorrect Code

```cpp
#include <iostream>
using namespace std;

int main()
{
    int a = 10;
    int b = 20;
    int c = 25;

    double average = double(a + b + c / 3);

    cout << "Average: " << average << endl;

    return 0;
}
```
