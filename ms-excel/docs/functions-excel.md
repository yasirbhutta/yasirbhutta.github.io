# Microsoft Excel - Microsoft 365

## Functions in Excel

### Cell References

- A cell reference refers to a cell or a range of cells on a worksheet. 
- It identifies a cell by referring to the row and column headings. When referring to a cell, enter the column letter followed by the row number Example
- **A10** refers to the cell at the intersection of column A and row 10 

### Copying Formulae

- When you copy a formula, Excel adjusts each cell reference in the formula relative to the position of the formula
- That is, by default a copy operation maintains the same relationship relative to the new cell

### Cell Reference

1. Relative
2. Absolute
3. Mixed

#### Relative Cell Reference

- In Excel, a relative cell reference identifies the location of a cell or group of cell.
- By default, a spreadsheet cell reference is relative.
- If copy the formula ,the reference automatically adjusts.  

#### Absolute Cell References

- A reference to a particular cell or group of cells that does not change, even copy the reference to another cell.
- An absolute cell reference consists of the column letter and row number surrounded by dollar sign($).
- To place a $ sign before a Column letter and Row number of a Cell click on the cell that contains the absolute value and press F4 Key 

EXAMPLE: ABSOLUTE REFERENCE

EXAMPLE: ABSOLUTE REFERENCE

#### Mixed Cell Reference

- You create a mixed cell reference when you set either the column or row reference fixed instead of both being absolute
- Absolute row reference -If a dollar sign were to precede only the row number, Example
- **A$1**, then only the column reference changes relatively when the formula is copied
- Absolute column reference -If a dollar sign precedes only the column letter, e.g. $A1, Excel will change only the row reference relative to the change in the formula location

### Named Cell Reference

- A name is a meaningful shorthand that makes it easier to understand the purpose of a cell reference, constant, formula or table.
- You can create a name that describes a cell or range. 
- You can also use the labels of columns and rows on a worksheet to refer to the cells within those columns and rows.

Defined Names

- **Formulas > Defined Names > Create from Selection**

### Functions

- Excel has hundreds of predefined formulae known as Functions
- Functions use specific arguments in a particular order or structure
- The arguments of functions can be anything from numbers, text, logical values, or cell references
- You can also have formulae or other functions as arguments in a function that are called nested functions.

Functions ….
The normal order for a function is:-

- Function Name,
- The opening parenthesis
- Arguments for the function separated by commas and closing parenthesis. 

#### 10 Most popluar functions

##### SUM

The SUM function adds values. You can add individual values, cell references or ranges or a mix of all three.

>For example:  
=SUM(A2:A10) Adds the values in cells A2:10.  
=SUM(A2:A10, C2:C10) Adds the values in cells A2:10, as well as cells C2:C10.  

**Note:** You can also type “ALT + =” into a cell, and Excel automatically inserts the SUM function. (windows)

Use AutoSum to sum numbers

Further reading:

- [SUM function - Microsoft Support](https://support.microsoft.com/en-us/office/sum-function-043e1c7d-7726-4e80-8f32-07b23e057f89)
- [Use AutoSum to sum numbers - Microsoft Support](#)

##### MAX

Returns the largest value in a set of values.

>Syntax  
MAX(number1, [number2], ...)

The MAX function syntax has the following arguments:
Number1, number2, ...    Number1 is required, subsequent numbers are optional. 1 to 255 numbers for which you want to find the maximum value.

##### MIN

Returns the smallest number in a set of values.

>**Syntax**  
MIN(number1, [number2], ...)

The MIN function syntax has the following arguments:
Number1, number2, ...    Number1 is optional, subsequent numbers are optional. 1 to 255 numbers for which you want to find the minimum value.

further reading:

- [MAX function - Microsoft Support](#)
- [MIN function - Microsoft Support](#)

#### COUNT

- The COUNT function counts the number of cells that contain numbers, and counts numbers within the list of arguments. 
- Use the COUNT function to get the number of entries in a number field that is in a range or array of numbers.

For example, you can enter the following formula to count the numbers in the range A1:A20: =COUNT(A1:A20). In this example, if five of the cells in the range contain numbers, the result is 5.

further reading:

- [COUNT function - Microsoft Support](#)

##### POWER

Returns the result of a number raised to a power.

>Syntax  
POWER(number, power)

The POWER function syntax has the following arguments:

Number Required. The base number. It can be any real number.
Power Required. The exponent to which the base number is raised.

=POWER(5,2)
Number
Power

further reading:

- POWER function - Microsoft Support

##### PRODUCT function

- The PRODUCT function multiplies all the numbers given as arguments and returns the product.
- The PRODUCT function is useful when you need to multiply many cells together.

For example, the formula =PRODUCT(A1:A3, C1:C3) is equivalent to =A1 * A2 * A3 * C1 * C2 * C3.

=Product(5,2)
=Product(C6:E6)

further reading: 

- [PRODUCT function - Microsoft Support]()

##### Average function

- Returns the average (arithmetic mean) of the arguments.

For example, if the range A1:A20 contains numbers, the formula =AVERAGE(A1:A20) returns the average of those numbers.

further reading:

- [AVERAGE function - Microsoft Support]

##### IF function

- The IF function is one of the most popular functions in Excel, and it allows you to make logical comparisons between a value and what you expect.
- So an IF statement can have two results. The first result is if your comparison is True, the second if your comparison is False.

For example, =IF(C2=”Yes”,1,2) says IF(C2 = Yes, then return a 1, otherwise return a 2).

further reading:

- [IF function - Microsoft Support](https://support.microsoft.com/en-us/office/if-function-69aed7c9-4e8a-4755-a9bc-aa8bbff73be2)

##### NOW function

The NOW function is useful when you need to display the current date and time on a worksheet or calculate a value based on the current date and time, and have that value updated each time you open the worksheet.

further reading:
[NOW function - Microsoft Support](#)

##### TODAY

The TODAY function is useful when you need to have the current date displayed on a worksheet, regardless of when you open the workbook. 

For example, if you know that someone was born in 1963, you might use the following formula to find that person's age as of this year's birthday:

= YEAR( TODAY())-1963

further reading:

- [TODAY function - Microsoft Support](#)

#### Change the case of Text

**LOWER function:** Converts all uppercase letters in a text string to lowercase.

>Syntax  
LOWER(text)

The LOWER function syntax has the following arguments:

Text Required. The text you want to convert to lowercase. LOWER does not change characters in text that are not letters.

**UPPER function:** Converts text to uppercase.

>Syntax  
UPPER(text)

The UPPER function syntax has the following arguments:

Text    Required. The text you want converted to uppercase. Text can be a reference or text string.

**PROPER function:**

further reading: 

- [LOWER function - Microsoft Support](#)
- [UPPER function - Microsoft Support](#)

#### LEN function

LEN returns the number of characters in a text string.

>Syntax  
LEN(text)

LENB(text)

Text Required. The text whose length you want to find. Spaces count as characters.

further reading: 

- [LEN, LENB functions - Microsoft Support]

#### COUNTIF function

Use COUNTIF, to count the number of cells that meet a criterion; for example, to count the number of times a particular city appears in a customer list.

For example:

=COUNTIF(A2:A5,"London")
=COUNTIF(A2:A5,A4)

further reading:

- [COUNTIF function - Microsoft Support](https://support.microsoft.com/en-us/office/countif-function-e0de10c6-f885-4e71-abb4-1f464816df34)

#### SUMIF function

use the SUMIF function to sum the values in a range that meet criteria that you specify.

For example, suppose that in a column that contains numbers, you want to sum only the values that are larger than 5. You can use the following formula: =SUMIF(B2:B25,">5")

>Syntax  
SUMIF(range, criteria, [sum_range])

further reading: 

- [SUMIF function - Microsoft Support](https://support.microsoft.com/en-us/office/sumif-c44b60c3-c9f4-4789-80fe-28a07f9b75b1)

### Formula Errors

- "######"
This error occurs when a column is not wide enough, or a negative date or time is used.
- "# DIV / O!"
A division by zero has occurred in the formula
- "# N / A"
A value is not available to the formula
- "# Name"
An unrecognizable range name is used in the formula
"# Value!"
An incorrect argument or operator is used in the formula
- "# Ref"
An invalid cell is referenced in the formula

- #N/A
 
Note    You can enter #N/A in those cells where data is not yet available. Formulas that refer to those cells will then return #N/A instead of attempting to calculate a value.


### Excercises

**Exercise 6:**

* Create a new Excel worksheet.
* In cells A1 to A10, enter the following numbers: 10, 20, 30, 40, 50, 60, 70, 80, 90, and 100.
* In cell A11, enter the following formula: `=SUM(A1:A10)`
* Press Enter.

The result, 550, should appear in cell A11.

**Exercise 7:**

* Create a new Excel worksheet.
* In cells A1 to A10, enter the following numbers: 10, 20, 30, 40, 50, 60, 70, 80, 90, and 100.
* In cell A11, enter the following formula: `=AVERAGE(A1:A10)`
* Press Enter.

The result, 55, should appear in cell A11.

**Exercise 8:**

* Create a new Excel worksheet.
* In cells A1 to A10, enter the following numbers: 10, 20, 30, 40, 50, 60, 70, 80, 90, and 100.
* In cell A11, enter the following formula: `=MAX(A1:A10)`
* Press Enter.

The result, 100, should appear in cell A11.

**Exercise 9:**

* Create a new Excel worksheet.
* In cells A1 to A10, enter the following numbers: 10, 20, 30, 40, 50, 60, 70, 80, 90, and 100.
* In cell A11, enter the following formula: `=MIN(A1:A10)`
* Press Enter.

The result, 10, should appear in cell A11.

**Exercise 10:**

* Create a new Excel worksheet.
* In cells A1 to A10, enter the following numbers: 10, 20, 30, 40, 50, 60, 70, 80, 90, and 100.
* In cell A11, enter the following formula: `=IF(A1>A2,"A1 is greater than A2","A1 is not greater than A2")`
* Press Enter.

The result, "A1 is greater than A2", should appear in cell A11.

These are just a few examples of Excel exercises to perform arithmetic operators. You can find many other exercises online and


Power and Square Root:

In cell A1, enter a number, e.g., 4.
In cell B1, calculate the square of the number using the formula =A1^2.
In cell B2, calculate the square root of the number using the formula =SQRT(A1).

Rounding:

In cell A1, enter a decimal number, e.g., 7.85.
In cell B1, round the number to the nearest whole number using the formula =ROUND(A1, 0).
In cell B2, round the number to one decimal place using the formula =ROUND(A1, 1).

Random Numbers:

In cell A1, enter the formula =RAND(). This will generate a random number between 0 and 1.
Drag the fill handle (the small square at the bottom-right corner of the cell) down to generate multiple random numbers.



