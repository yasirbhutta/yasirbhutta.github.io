---
layout: page
title: "C++ Basics: Output Practice Questions"
description: "Practice basic C++ output concepts with simple exercises on cout, variables, arithmetic expressions, and predicting console output for beginner programmers."
keywords: C++ output basics, cout in C++, C++ console output, print variable values in C++, arithmetic output in C++, predicting output in C++, beginner C++ exercises, C++ programming practice, output practice questions, C++ basics tutorial
---

## Instructions for Students

1. Read the program carefully.
2. Predict the output without running the code.
3. Write your predicted output.
4. Run the program to verify your answer.
5. Understand why the output appears.
6. Modify the code and predict the new output.

---

<!-- ## Topic 1: Data Types (10 Questions) -->

<!-- ### Beginner Level -->

## Question 1: Displaying Integer Values

**Task:** Predict the output.

### Code

```cpp
int x = 10;
int y = 5;

cout << x << endl;
cout << y << endl;
cout << x + y;
```

## Question 2: Displaying Decimal Values

**Task:** Predict the output.

### Code

```cpp
float price = 25.5;
double tax = 5.25;

cout << price << endl;
cout << tax << endl;
cout << price + tax;
```

## Question 3: Displaying Character Values

**Task:** Predict the output.

### Code

```cpp
char grade = 'A';
char section = 'B';

cout << grade << endl;
cout << section << endl;
cout << grade + 1;
```

## Question 4: Displaying String Values

**Task:** Predict the output.

### Code

```cpp
string firstName = "Ali";
string lastName = "Ahmed";

cout << firstName << endl;
cout << lastName << endl;
cout << firstName + lastName;
```



<!-- ### Intermediate Level -->


## Question 5: Character and Integer Values

**Task:** Predict the output.

### Code

```cpp
char letter = 'A';
int number = 5;

cout << letter << endl;
cout << letter + number << endl;
cout << char(letter + number);
```

## Question 6: Different Data Types in One Program

**Task:** Predict the output.

### Code

```cpp
int age = 20;
float height = 5.6;
char grade = 'A';
bool isStudent = true;

cout << age << endl;
cout << height << endl;
cout << grade << endl;
cout << isStudent;
```

<!-- ## Topic 2: Operators (10 Questions) -->

<!-- ### Beginner Level -->


## Question 7: Multiplication and Division

**Task:** Predict the output.

### Code

```cpp
int a = 20;
int b = 4;

cout << a * b << endl;
cout << a / b;
```

## Question 8: Modulus Operator

**Task:** Predict the output.

### Code

```cpp
int a = 17;
int b = 5;

cout << a % b << endl;
cout << 20 % 3;
```

## Question 9: Increment Operator

**Task:** Predict the output.

### Code

```cpp
int x = 5;

cout << x << endl;

x++;

cout << x << endl;

++x;

cout << x;
```

## Question 10: Decrement Operator

**Task:** Predict the output.

### Code

```cpp
int x = 10;

cout << x-- << endl;
cout << x << endl;
cout << --x;
```

<!-- ### Intermediate Level -->

## Question 11: Compound Assignment Operators

**Task:** Predict the output.

### Code

```cpp
int x = 10;

x += 5;
cout << x << endl;

x *= 2;
cout << x << endl;

x -= 4;
cout << x;
```

## Question 12: Relational Operators

**Task:** Predict the output.

### Code

```cpp
int a = 10;
int b = 20;

cout << (a > b) << endl;
cout << (a < b) << endl;
cout << (a == b) << endl;
cout << (a != b);
```

## Question 13: Logical AND Operator

**Task:** Predict the output.

### Code

```cpp
int age = 20;
int marks = 75;

cout << (age >= 18 && marks >= 50);
```

## Question 14: Logical OR Operator

**Task:** Predict the output.

### Code

```cpp
int marks = 40;
int attendance = 80;

cout << (marks >= 50 || attendance >= 75);
```

## Question 15: Combining Relational and Logical Operators

**Task:** Predict the output.

### Code

```cpp
int age = 22;
int marks = 85;
int attendance = 90;

bool result = (age >= 18 && marks >= 50)
              || attendance >= 95;

cout << boolalpha << result;
```

<!-- ## Topic 3: Operator Precedence (10 Questions) -->

<!-- ### Beginner Level -->

## Question 16: Multiplication Before Addition

**Task:** Predict the output.

### Code

```cpp
int result = 10 + 5 * 2;

cout << result;
```

## Question 17: Division Before Subtraction

**Task:** Predict the output.

### Code

```cpp
int result = 20 - 12 / 3;

cout << result;
```

## Question 18: Multiple Arithmetic Operators

**Task:** Predict the output.

### Code

```cpp
int result = 20 + 10 / 2 * 3;

cout << result;
```

<!-- ### Intermediate Level -->


## Question 19: Modulus and Addition

**Task:** Predict the output.

### Code

```cpp
int a = 17;
int b = 5;

int result = a + b % 3;

cout << result;
```


<!-- ## Topic 4: Constants (5 Questions) -->

<!-- ### Beginner Level -->


## Question 20: Constant in Addition

**Task:** Predict the output.

### Code

```cpp
const int BONUS = 10;
int salary = 50000;

cout << salary + BONUS;
```

## Question 21: Combining Constants and Variables

**Task:** Predict the output.

### Code

```cpp
const int TAX_RATE = 10;
int price = 1000;

int tax = price * TAX_RATE / 100;
int total = price + tax;

cout << tax << endl;
cout << total;
```

<!-- ## Topic 5: Type Casting (10 Questions) -->

<!-- ### Beginner Level -->


## Question 22: Double to Integer Conversion

**Task:** Predict the output.

### Code

```cpp
double price = 99.75;

int result = (int) price;

cout << result;
```

## Question 23: Integer Division Without Casting

**Task:** Predict the output.

### Code

```cpp
int a = 7;
int b = 2;

double result = a / b;

cout << result;
```

## Question 24: Integer Division with Casting

**Task:** Predict the output.

### Code

```cpp
int a = 7;
int b = 2;

double result = (double) a / b;

cout << result;
```

## Question 25: Character Type Casting

**Task:** Predict the output.

### Code

```cpp
int code = 65;

char letter = (char) code;

cout << letter;
```

<!-- ### Intermediate Level -->


## Question 26: Type Casting Before Division

**Task:** Predict the output.

### Code

```cpp
int a = 10;
int b = 3;

double result = (double)(a / b);

cout << result;
```

## Question 27: Multiple Type Conversions

**Task:** Predict the output.

### Code

```cpp
double a = 15.8;
int b = (int) a;

double c = b + 2.5;

cout << b << endl;
cout << c;
```

<!-- ## Topic 6: Comments (5 Questions) -->

<!-- ### Beginner Level -->

## Question 28: Single-Line Comment

**Task:** Predict the output.

### Code

```cpp
int x = 10;

// cout << 20 << endl;

cout << x;
```

## Question 29: Multiple-Line Comments

**Task:** Predict the output.

### Code

```cpp
int a = 5;

/*
cout << 10 << endl;
cout << 20 << endl;
*/

cout << a;
```

## Question 30: Commenting Part of a Statement

**Task:** Predict the output.

### Code

```cpp
int a = 10;
int b = 5;

cout << a /* + b */ * 2;
```

## Question 31: Comments and Variable Updates

**Task:** Predict the output.

### Code

```cpp
int number = 10;

// Increase the number
number += 5;

/*
number = number * 2;
cout << number << endl;
*/

cout << number;
```

