# Formulas in Excel

## Formula

- A formula is an equation that performs operations on a worksheet data.

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

### Arithmetic Operator

|  Operation | Operator | Example |
| --- | --- | --- |
| Addition | + | =10+2 |
| Subtraction | - | =6-2|
| Negation | - | =-9|
| Multiplication | * | =5*8|
| Division | / | =27/9|
| Percent | % | =550*3%|
| Exponentiation | ^ | =5^2 (same 5*5)|

### Comparision Operators

### Reference Operators

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

## Creating a formula

1. By placing an equal sign in the cell that is to hold the result and then pointing and clicking those cells that contain the operands.
2. By writing the cell addresses of cells that you want to use for your calculation in your result cell

[Video Tutorial: How to Create a simple formula in Excel](https://youtu.be/mKNp8MgTS70?si=v_zE08edCBRU9Hsh)

## Review Questions

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

## Muhammad Yasir Bhutta

- [Web](https://yasirbhutta.github.io/)
- [Youtube](https://www.youtube.com/yasirbhutta)
- [Facebook](https://www.facebook.com/yasirbhutta786)
- [Twitter](https://twitter.com/yasirbhutta)
