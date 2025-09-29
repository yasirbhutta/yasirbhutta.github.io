---
layout: page
title: "Formulas in Excel"
description: Formulas in Excel.
keywords: Excel functions, Excel formulas, Excel tutorial, Excel tips, Excel training, Excel how to, Microsoft Excel, Spreadsheet functions
author: Muhammad Yasir Bhutta
course: ms-excel
topic: functions
toc: toc/ms-excel-toc.html
breadcrumb:
  - title: Home
    url: /
  - title: Excel
    url: /ms-excel/
---

[Download PDF](/downloads/ms-excel/formulas.pdf)

## Table of Contents
- [Formulas in Excel](#formulas-in-excel)
  - [Module 3: Formulas in Excel](#module-3-formulas-in-excel)
  - [Formula](#formula)
    - [See also](#see-also)
    - [Structure of a Formula](#structure-of-a-formula)
      - [Example of Formula](#example-of-formula)
  - [Operators](#operators)
    - [Arithmetic Operators](#arithmetic-operators)
      - [See Also](#see-also-1)
    - [Comparision Operators](#comparision-operators)
    - [Text concatenation operator](#text-concatenation-operator)
    - [Reference Operators](#reference-operators)
      - [Implicit intersection operator: @](#implicit-intersection-operator-)
  - [Operand](#operand)
    - [Order of Operations: Left to Right and Parentheses](#order-of-operations-left-to-right-and-parentheses)
    - [The order in which Excel performs operations in formulas](#the-order-in-which-excel-performs-operations-in-formulas)
  - [Creating a formula](#creating-a-formula)
  - [True/False (Mark T for True and F for False)](#truefalse-mark-t-for-true-and-f-for-false)
  - [Explore More Excel Topics](#explore-more-excel-topics)
  - [Multiple Choice (Select the best answer)](#multiple-choice-select-the-best-answer)
  - [Exercises](#exercises)
  - [Review Questions](#review-questions)
  - [References and Bibliography](#references-and-bibliography)


## Module 3: Formulas in Excel

- Understanding of the formulas
- Using basic arithmetic operators
- Comparision Operators
- Text concatenation operator

## Formula

- A formula is an equation that performs operations on a worksheet data.

### See also

- [Video Tutorial: Create a simple formula in Excel](https://youtu.be/mKNp8MgTS70?si=mpqApcElM6A75MQn)

### Structure of a Formula

- All the formula have to begin with an equal sign [=]
- The = sign is followed by the elements to be calculated [the operands]
- Operands are separated by calculation operators

#### Example of Formula

```excel
= A1 + A2
```

## Operators

- An operator specifies the type of calculation that you intend to perform on the elements of a formula
- Excel offers three main types of operators –

  1. Arithmetic- for basic mathematical operations.
  2. Comparison - compare two values.
  3. Reference -combine ranges of cells.

### Arithmetic Operators

To perform basic mathematical operations such as addition, subtraction, or multiplication—or to combine numbers—and produce numeric results, use the arithmetic operators in this table. [^1]

|  Meaning | Arithmetic Operator | Example |
| --- | --- | --- |
| Addition | + (plus sign)| =10+2 |
| Subtraction | - (minus sign) | =6-2|
| Negation | - (minus sign) | =-9|
| Multiplication | * (asterisk) | =5*8|
| Division | / (forward slash)| =27/9|
| Percent | % (percent sign)| =550*3%|
| Exponentiation | ^ (caret)| =5^2 (same 5*5)|

#### See Also

- [Basic math in Excel](https://support.microsoft.com/en-us/office/video-basic-math-in-excel-2013-e05703f5-7150-44c1-8a52-307738266821#ID0EBBD=Transcript)

### Comparision Operators

With the operators in the table below, you can compare two values. When two values are compared by using these operators, the result is a logical value either TRUE or FALSE. [^1]

|Comparison operator | Meaning | Example|
| --- | --- | --- |
| = (equal sign)| Equal to | =A1=B1|
| > (greater than sign) | Greater than | =A1>B1 |
| < (less than sign) | Less than | =A1<B1 |
| >= (greater than or equal to sign) | Greater than or equal to | =A1>=B1|
| <= (less than or equal to sign) | Less than or equal to | =A1<=B1|
| <> (not equal to sign) | Not equal to | =A1<>B1 |

### Text concatenation operator

Use the ampersand (&) to join, or concatenate, one or more text strings to produce a single piece of text.

| Text operator | Meaning | Example |
|---           |---    |--- |
|& (ampersand) |Connects, or concatenates, two values to produce one continuous text value.| ="Muhammad"&" Ahmad"|

### Reference Operators

Combine ranges of cells for calculations with these operators.

| Reference operator | Meaning | Example |
| --- | --- | --- |
| : (colon) | Range operator, which produces one reference to all the cells between two references, including the two references. | =SUM(B5:B15)|
| , (comma) | Union operator, which combines multiple references into one reference. | =SUM(B5:B15,D5:D15) |
|(space) | Intersection operator, which produces a reference to cells common to the two references. | =SUM(B7:D7 C6:C8) |
| # (pound) | The # symbol is used in several contexts: Used as part of an error name. Used to indicate insufficient space to render. In most cases, you can widen the column until the contents display properly. Spilled range operator, which is used to reference an entire range in a dynamic array formula. | #VALUE!, #####,  =SUM(A2#)|
| @ (at) | Reference operator, which is used to indicate implicit intersection in a formula. | =@A1:A10 | =SUM(Table1[@[January]:[December]])|

#### Implicit intersection operator: @

The implicit intersection operator was introduced as part of substantial upgrade to Excel's formula language to support dynamic arrays. Dynamic arrays bring significant new calculation ability and functionality to Excel. [^2]

| Original formula | As seen in dynamic array Excel | Explanation                                                                                                  |
| ---------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| \=SUM(A1:A10)    | \=SUM(A1:A10)                  | No change - No implicit intersection could occur, as the SUM function expects ranges or arrays.              |
| \=A1+A2          | \=A1+A2                        | No change - No implicit intersection could occur.                                                            |
| \=A1:A10         | \=@A1:A10                      | Implicit intersection will occur, and Excel will return the value associated with the row the formula is in. |

**See Also:**

- [Implicit intersection operator: @](https://support.microsoft.com/en-us/office/implicit-intersection-operator-ce3be07b-0101-4450-a24e-c1c999be2b34)

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1602443888929206"
     crossorigin="anonymous"></script>
<ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-1602443888929206"
     data-ad-slot="6296238623"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

## Operand

A quantity upon which a mathematical operation is performed

- A numerical value
- A cell or range reference
- A label
- A name
- A worksheet function

### Order of Operations: Left to Right and Parentheses

- The operations in a formula are performed from left to right – following the order of operator precedence.
- You can change the of precedence of operators by using parentheses ().

### The order in which Excel performs operations in formulas

In some cases, the order in which a calculation is performed can affect the return value of the formula, so it's important to understand how the order is determined and how you can change the order to obtain the results you want.[3]

In Excel, Remember the order of operations:

1. **Parentheses (P):** Calculate expressions inside parentheses first.
2. **Exponents (E):** Next, handle any powers or roots.
3. **Multiplication (M) and Division (D):** These operations are processed from left to right.
4. **Addition (A) and Subtraction (S):** Finally, these are completed from left to right.


For example, with a formula like

```excel 
= (6 + 4) ^ 2 / 5
```
Excel follows by:

- First calculating (6 + 4), resulting in 10.
- Then raising 10 to the power of 2 (10^2 = 100).
- Lastly, dividing by 5, giving a final result of 20.

Another example formula:

```excel
= (3 + 2) ^ 2 * 4 / 2
```

Excel first calculates the parentheses (3 + 2), resulting in 5, then raises it to the power 2 (5^2 = 25), and finally multiplies by 4 to give 100.


The following formula will evaluate to 14:

```excel
=2 + 3 * 4
```

This is because the multiplication operation is performed before the addition operation. However, if we enclose addition operation in parentheses, the formula will evaluate to 20:

```excel
=(2 + 3) * 4
```

This is because the operation within the parentheses is performed first.

Here are some other examples of the PEMDAS order of operations in Excel:

```excel
=2 + 3 ^ 4          # Evaluates to 83 (exponents are performed before addition)
=2 - 3 * 4          # Evaluates to -10 (multiplication is performed before subtraction)
=5 / (6 + 4)        # Evaluates to 0.5 (addition is performed before division)
=2 * (3 + 4)        # Evaluates to 14 (addition is performed before multiplication)
=6 / 3 - 2 + 3 * 3  # Evaluates to 9 (muliplication and division are performed before subtraction.)
```

To change the order of evaluation, enclose in parentheses the part of the formula to be calculated first. 

Watch this video on [Operator order in Excel](https://support.microsoft.com/en-us/office/video-operator-order-in-excel-2013-4af9541b-1c79-41cb-a0cf-dbced6c9ae4e) to learn more.

**See also:**

- [The order in which Excel performs operations in formulas - Microsoft Support](https://support.microsoft.com/en-us/office/the-order-in-which-excel-performs-operations-in-formulas-28eaf0d7-7058-4eff-a8ea-0a835fafadb8)

## Creating a formula

1. By placing an equal sign in the cell that is to hold the result and then pointing and clicking those cells that contain the operands.
2. By writing the cell addresses of cells that you want to use for your calculation in your result cell

Watch this video on [Simple formula in excel](https://youtu.be/mKNp8MgTS70?si=v_zE08edCBRU9Hsh)

- [Video Tutorial: Enter formula in multiple cells using array formulas in excel](https://youtu.be/T9kXiBI3Y7c?si=t3oGXL71y0sUua2w)

## True/False (Mark T for True and F for False)

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1602443888929206"
     crossorigin="anonymous"></script>
<ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-1602443888929206"
     data-ad-slot="6296238623"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

## Explore More Excel Topics

{% assign show_heading = false %}
{% include toc/ms-excel-toc.html show_heading=show_heading%}

{% assign topic = "formulas" %}
{% include practice-and-progress.html topic=topic %}

## Multiple Choice (Select the best answer)

- [Microsfot Excel Quiz: Formulas](../quizzes/excel-formulas-quiz.md)

> What is a formula in Excel?

1. [x] A rule that tells Excel how to calculate something
2. [ ] A cell in a spreadsheet
3. [ ] The address of a cell
4. [ ] A range of cells

> Which of the following is the correct order of operations in Excel formulas?

1. [x] Parentheses, Exponents, Multiplication, Division, Addition, Subtraction
2. [ ] Exponents, Multiplication, Division, Addition, Subtraction, Parentheses
3. [ ] Multiplication, Division, Addition, Subtraction, Parentheses, Exponents
4. [ ] Parentheses, Multiplication, Division, Addition, Subtraction, Exponents

> Which of the following operators has the highest precedence in Excel?

1. [ ] Addition (+)
2. [ ] Multiplication (*)
3. [x] Exponentiation (^)
4. [ ] Division (/)

> What is the result of the following formula in Excel: 10 + 5 * 2?

1. [x] 20
2. [ ] 30
3. [ ] 40
4. [ ] 50

> What is the purpose of using parentheses in an Excel formula?

1. [x] To change the order of operations
2. [ ] To group cells together
3. [ ] To add comments to a formula
4. [ ] To protect a formula from being changed

> What is the purpose of using the PERCENTAGE (%) operator in Excel?

1. [x] To calculate a percentage of a number
2. [ ] To divide a number by 100
3. [ ] To calculate the square root of a number
4. [ ] To calculate the absolute value of a number

> What is the correct syntax for adding two cells in Excel?

1. [ ] =A1:A2
2. [x] =A1+B2
3. [ ] =A1+B2+C2
4. [ ] =SUM(A1+B2)

> What is the difference between an arithmetic operator and a relational operator?

1. [x] An arithmetic operator performs a mathematical operation on two or more values, while a relational operator compares two values and returns a TRUE or FALSE value
2. [ ] An arithmetic operator performs a mathematical operation on two or more values, while a relational operator compares two values and returns a number.
3. [ ] An arithmetic operator performs a mathematical operation on two or more values, while a relational operator compares two values and returns a string.
4. [ ] An arithmetic operator performs a mathematical operation on two or more values, while a relational operator compares two values and returns a date.

> What is the correct way to enter a negative number in Excel?

1. [x] Type the minus sign (-) before the number.
2. [ ] Type the minus sign (-) after the number.
3. [ ] Enclose the number in parentheses.
4. [ ] Use the negative sign (-) button on the toolbar.

> Which operator is used for division in Excel?

1. [x] /
2. [ ] *
3. [ ] %
4. [ ] ^

> Which operator is used for exponentiation in Excel?

1. [ ] **
2. [x] ^
3. [ ] *
4. [ ] /

> If A1 contains the value 20 and B1 contains the value 5, what is the result of the formula =A1-B1*2?

1. [x] 10
2. [ ] 0
3. [ ] 30
4. [ ] 15

> In Excel, the ampersand (&) operator is used for:

1. [ ] Multiplication
2. [x] Concatenation
3. [ ] Division
4. [ ] Subtraction

> Which of the following Excel formulas will result in the product of cells A1 and B1?

1. [ ] =A1 + B1
2. [x] =A1 * B1
3. [ ] =A1 / B1
4. [ ] =A1 - B1

> If cell A1 contains the value 10 and cell A2 contains the value 3, what is the result of the formula =A1/A2?

1. [ ] 7
2. [x] 3.333
3. [ ] 13
4. [ ] 30

> If cell B1 contains the value 8 and cell B2 contains the value 2, what is the result of the formula =B1^B2?

1. [ ] 16
2. [ ] 10
3. [x] 64
4. [ ] 4

> If cell D1 contains the value 25 and cell D2 contains the value 5, what is the result of the formula =D1-D2?

1. [x] 20
2. [ ] 30
3. [ ] 5
4. [ ] 125

> Which symbol is used for "equal to" in Excel?

1. [x] =
2. [ ] ==
3. [ ] ===
4. [ ] --

> What is the result of the expression "=A1 > B1" if the value in cell A1 is 10 and in cell B1 is 5?

1. [x] True
2. [ ] False
3. [ ] Error
4. [ ] Not applicable

> Which operator is used for "not equal to" in Excel?

1. [ ] !=
2. [x] <>
3. [ ] ><
4. [ ] /=

> If cell C1 contains the formula "=A1<50", what does it mean?

1. [ ] C1 is less than 50.
2. [x] A1 is less than 50.
3. [ ] A1 is equal to 50.
4. [ ] A1 is greater than 50.

> Which of the following is the correct syntax for "greater than or equal to" in Excel?

1. [x] >=
2. [ ] =>
3. [ ] =<
4. [ ] ->

> What is the result of the expression "10 <= 5" in Excel?

1. [ ] True
2. [x] False
3. [ ] Error
4. [ ] Cannot be determined

> What is the correct formula to determine if the value in cell A1 is equal to the text "Hello"?

1. [ ] =A1>"Hello"
2. [ ] =A1<="Hello"
3. [ ] =A1<"Hello"
4. [x] =A1="Hello"

> Which of the following formulas will check if the value in cell A1 is not equal to the value in cell A2?

1. [ ] =A1=A2
2. [x] =A1<>A2
3. [ ] =A1<A2
4. [ ] =A1>A2

> What is the result of the following formula: =A1>B1?

1. [ ] False (if A1 is Not Equal to B1)
2. [ ] Error (if A1 and B1 are equal)
3. [x] True (if A1 is greater than B1)
4. [ ] None of the above

> What is the result of the following formula: =A1>=B1?

1. [x] True (if A1 is greater than or equal to B1)
2. [ ] False (if A1 is less than B1)
3. [ ] Error (if A1 and B1 are equal)
4. [ ] None of the above

## Exercises

Here are some Excel exercises to perform arithmetic operators:

**Exercise 1:**

- Create a new Excel worksheet.
- In cells A1 and A2, enter the numbers 10 and 5, respectively.
- In cell A3, enter the following formula: `=A1+A2`
- Press Enter.

The result, 15, should appear in cell A3.

**Exercise 2:**

- Create a new Excel worksheet.
- In cells A1 and A2, enter the numbers 25 and 20, respectively.
- In cell A3, enter the following formula: `=A1-A2`
- Press Enter.

The result, 5, should appear in cell A3.

**Exercise 3:**

- Create a new Excel worksheet.
- In cells A1 and A2, enter the numbers 2 and 12, respectively.
- In cell A3, enter the following formula: `=A1*A2`
- Press Enter.

The result, 24, should appear in cell A3.

**Exercise 4:**

- Create a new Excel worksheet.
- In cells A1 and A2, enter the numbers 50 and 10, respectively.
- In cell A3, enter the following formula: `=A1/A2`
- Press Enter.

The result, 5, should appear in cell A3.

**Exercise 5:**

- Create a new Excel worksheet.
- In cells A1 and A2, enter the numbers 600 and 25%, respectively.
- In cell A3, enter the following formula: `=A1*A2`
- Press Enter.

The result, 150, should appear in cell A3.

**Exercise 5:*

- In cell A3, type 7.
- In cell B3, type 3.
- In cell C3, type 5.
- In cell D3, use the formula `=(A3+B3)*C3` to add A3 and B3 and then multiply the result by C3.

**Exercise 6:**

1. Open a new Excel spreadsheet.
2. In cell A1, type "Number 1" and in cell B1, type "Number 2."
3. In cell A2, enter a number (e.g., 10), and in cell B2, enter another number (e.g., 5).
4. In cell C2, use the "+" operator to add the values in cells A2 and B2.
5. In cell D2, use the "-" operator to subtract the value in cell B2 from the value in cell A2.
6. In cell E2, use the "*" operator to multiply the values in cells A2 and B2.
7. In cell F2, use the "/" operator to divide the value in cell A2 by the value in cell B2.
8. Observe the results in cells C2, D2, E2, and F2.

**Exercise 7:**

- In cell A3, enter a number (e.g., 2), and in cell B3, enter the exponent (e.g., 3).
- In cell C3, use the formula =A3^B3 to calculate the result of A3 raised to the power of B3.

**Exercise 8:**

- In cell A4, enter a number (e.g., 7), and in cell B4, enter another number (e.g., 3).
- In cell C4, use the formula =A4 * (A4 + B4) / B4 to combine addition, multiplication, and division in a single formula.

**Exercise 9:**

- In cell A5, enter a number (e.g., 15), and in cell B5, enter another number (e.g., 6).
- In cell C5, use the formula `=(A5 + B5) * (A5 - B5)` to perform addition and subtraction inside parentheses before multiplying.

**Exercise 10:** Discount calculation

- In cell A1, enter the total sales amount, e.g., 5000.
- In cell A2, enter the percentage discount, e.g., 10%.
- In cell B1, calculate the discount amount using the formula `=A1 * A2`.
- In cell B2, calculate the final discounted price using the formula `=A1 - B1`.

**Exercise 11:** Discount calculation

- In cell A12, enter the original price (e.g., 50), and in cell B12, enter the discount percentage (e.g., 20%).
- In cell C12, use the formula `=A12 - (A12 * B12)` to calculate the discounted price.

## Review Questions

1. How can you multiply two numbers in Excel? Which operator do you use?
2. What are the different types of Excel operators?
3. What does the exponentiation operator (^) do in Excel, and how is it used?
4. Explain the purpose of the following arithmetic operators in Microsoft Excel and provide examples for each: /, ^, *, %.
5. What is the order of precedence for Excel operators?
6. How do you use parentheses to control the order of operations in a formula?
7. What is Cell Address and explain the purpose of formula bar?
8. What is the difference between arithmetic operators, comparison operators, logical operators, and text operators?
9. How can you combine two or more text strings in Excel using an operator?
10. How do you use the percent operator (%) in Excel to calculate percentages?
11. What is the PEMDAS order of operations?
12. What is the basic structure of a formula in Excel?

## References and Bibliography

- [^1:] [Calculation operators and precedence in Excel](https://support.microsoft.com/en-us/office/calculation-operators-and-precedence-in-excel-48be406d-4975-4d31-b2b8-7af9e0e2878a)
- [^2] [Implicit intersection operator: @](https://support.microsoft.com/en-us/office/implicit-intersection-operator-ce3be07b-0101-4450-a24e-c1c999be2b34)
- [3] “The order in which Excel performs operations in formulas,” [support.microsoft.com.](https://support.microsoft.com/en-us/office/the-order-in-which-excel-performs-operations-in-formulas-28eaf0d7-7058-4eff-a8ea-0a835fafadb8)
‌
