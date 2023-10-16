# Formulas in Excel

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

### PEMDAS

PEMDAS is an acronym that stands for the following order of operations:

- Parentheses
- Exponents
- Multiplication
- Division
- Addition
- Subtraction

Excel follows the PEMDAS order of operations when evaluating formulas. This means that operations within parentheses are performed first, followed by exponents, multiplication and division, and then addition and subtraction.

For example, the following formula will evaluate to 14:

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
=2 + 3^4      # Evaluates to 83 (exponents are performed before addition)
=2 - 3 * 4      # Evaluates to -10 (multiplication is performed before subtraction)
=5 / (6 + 4)     # Evaluates to 0.5 (addition is performed before division)
=2 * (3 + 4)     # Evaluates to 14 (addition is performed before multiplication)
=6/3-2+3*3       # Evaluates to 14 (muliplication and division are performed before subtraction.)
```

You can use parentheses in Excel to override the PEMDAS order of operations and change the order in which operations are performed. This can be useful for creating more complex formulas.

Watch this video on [Operator order in Excel](https://support.microsoft.com/en-us/office/video-operator-order-in-excel-2013-4af9541b-1c79-41cb-a0cf-dbced6c9ae4e) to learn more.

## Creating a formula

1. By placing an equal sign in the cell that is to hold the result and then pointing and clicking those cells that contain the operands.
2. By writing the cell addresses of cells that you want to use for your calculation in your result cell

Watch this video on [Simple formula in excel](https://youtu.be/mKNp8MgTS70?si=v_zE08edCBRU9Hsh)

- [Video Tutorial: Enter formula in multiple cells using array formulas in excel](https://youtu.be/T9kXiBI3Y7c?si=t3oGXL71y0sUua2w)

## Review Questions

1. How can you multiply two numbers in Excel? Which operator do you use?
2. What are the different types of Excel operators?
3. What does the exponentiation operator (^) do in Excel, and how is it used?
4. What is the order of precedence for Excel operators?
5. How do you use parentheses to control the order of operations in a formula?
6. What is Cell Address and explain the purpose of formula bar?
7. What is the difference between arithmetic operators, comparison operators, logical operators, and text operators?
8. How can you combine two or more text strings in Excel using an operator?
9. How do you use the percent operator (%) in Excel to calculate percentages?
10. What is the PEMDAS order of operations?
11. What is the basic structure of a formula in Excel?

## Excercises

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

**Exercise 10: Discount calculation**

- In cell A1, enter the total sales amount, e.g., 5000.
- In cell A2, enter the percentage discount, e.g., 10%.
- In cell B1, calculate the discount amount using the formula `=A1 * A2`.
- In cell B2, calculate the final discounted price using the formula `=A1 - B1`.

**Exercise 11: Discount calculation**

- In cell A12, enter the original price (e.g., 50), and in cell B12, enter the discount percentage (e.g., 20%).
- In cell C12, use the formula `=A12 - (A12 * B12)` to calculate the discounted price.


Which of the following is the correct order of operations in Excel formulas?

(A) Parentheses, Exponents, Multiplication, Division, Addition, Subtraction
(B) Exponents, Multiplication, Division, Addition, Subtraction, Parentheses
(C) Multiplication, Division, Addition, Subtraction, Parentheses, Exponents
(D) Parentheses, Multiplication, Division, Addition, Subtraction, Exponents

Answer: (A)

## References

[^1:] [Calculation operators and precedence in Excel](https://support.microsoft.com/en-us/office/calculation-operators-and-precedence-in-excel-48be406d-4975-4d31-b2b8-7af9e0e2878a)

## Muhammad Yasir Bhutta

- [Web](https://yasirbhutta.github.io/)
- [Youtube](https://www.youtube.com/yasirbhutta)
- [Facebook](https://www.facebook.com/yasirbhutta786)
- [Twitter](https://twitter.com/yasirbhutta)
