# Microsoft Excel - Microsoft 365

- [Download PDF](https://yasirbhutta.github.io/ms-excel/docs/functions.pdf)

- To access the updated lecture notes, please click on the following link:
[https://yasirbhutta.github.io/ms-excel/docs/functions.html](https://yasirbhutta.github.io/ms-excel/docs/functions.html)

## Functions in Excel

### Cell References

- A cell reference refers to a cell or a range of cells on a worksheet.
- It identifies a cell by referring to the row and column headings. When referring to a cell, enter the column letter followed by the row number Example
- **A10** refers to the cell at the intersection of column A and row 10.

### Copying Formulae

- When you copy a formula, Excel adjusts each cell reference in the formula relative to the position of the formula
- That is, by default a copy operation maintains the same relationship relative to the new cell

### Cell Reference

1. Relative
2. Absolute
3. Mixed

#### Relative Cell Reference

- A relative cell reference is a cell reference that changes when the formula is copied to a different cell.
- By default, a spreadsheet cell reference is relative.

**For example,** if you enter the formula =A1+B1 into cell C1, and then copy that formula to cell D2, the formula will automatically change to `=A2+B2`. This is because Excel assumes that you want to add the corresponding cells in the new location.

#### Absolute Cell References

- An absolute cell reference is a cell reference that does not change when the formula is copied to a different cell.
- To create an absolute cell reference, you need to prefix the cell reference with a dollar sign ($).
- To place a $ sign before a Column letter and Row number of a Cell click on the cell that contains the absolute value and press **F4 Key**.
  
**For example,** if you enter the formula `=$A1+$B1` into cell C1, and then copy that formula to cell D2, the formula will remain the same. This is because Excel knows that you want to add the specific cells A1 and B1, regardless of where the formula is copied.

- [Video Tutorial: Create an Absolute Reference in Excel](https://youtu.be/NDBp1p6g_4c?si=ULHKKtku6Ts6U_Zz)

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

**Use AutoSum to sum numbers**

- [Video Tutorial: Use of Sum function and AutoSum to sum numbers | Microsoft Excel](https://youtu.be/o8aBs1Qr_8s?si=54T8YseIfXyJt5Fg)

Further reading:

- [SUM function - Microsoft Support](https://support.microsoft.com/en-us/office/sum-function-043e1c7d-7726-4e80-8f32-07b23e057f89)
- Use AutoSum to sum numbers - Microsoft Support [[Windows]](https://support.microsoft.com/en-us/office/use-autosum-to-sum-numbers-543941e7-e783-44ef-8317-7d1bb85fe706) [[Android]](https://support.microsoft.com/en-us/office/use-autosum-to-sum-numbers-543941e7-e783-44ef-8317-7d1bb85fe706#ID0EBBF=Android)

##### Use of cell references in a formula

- [Video Tutorial: Use cell refenences in a formul in Microsoft Excel](https://youtu.be/mdmYAOeGJoQ?si=xGxjvagLaCTQSlBp)
  
##### MAX

Returns the largest value in a set of values.

>Syntax  

```excel
MAX(number1, [number2], ...)
```

The MAX function syntax has the following arguments:
Number1, number2, ...    Number1 is required, subsequent numbers are optional. 1 to 255 numbers for which you want to find the maximum value.

##### MIN

Returns the smallest number in a set of values.

>**Syntax**  

```excel
MIN(number1, [number2], ...)
```

The MIN function syntax has the following arguments:
Number1, number2, ...    Number1 is optional, subsequent numbers are optional. 1 to 255 numbers for which you want to find the minimum value.

- [Video Tutorial: use of MAX() and MIN() functions in excel](https://youtu.be/v-HPGVPpEvE?si=Kah5qhLKiHNyhcW-)

further reading:

- [MAX function - Microsoft Support](https://support.microsoft.com/en-gb/office/max-function-e0012414-9ac8-4b34-9a47-73e662c08098#:~:text=The%20MAX%20function%20syntax%20has,to%20find%20the%20maximum%20value.)
- [MIN function - Microsoft Support](https://support.microsoft.com/en-us/office/min-function-61635d12-920f-4ce2-a70f-96f202dcc152#:~:text=The%20MIN%20function%20syntax%20has,to%20find%20the%20minimum%20value.)

#### COUNT

- The COUNT function counts the number of cells that contain numbers, and counts numbers within the list of arguments. 
- Use the COUNT function to get the number of entries in a number field that is in a range or array of numbers.

For example, you can enter the following formula to count the numbers in the range A1:A20: =COUNT(A1:A20). In this example, if five of the cells in the range contain numbers, the result is 5.

- [Video Tutorial: Count function in excel](https://youtu.be/KHTWvRaorWs?si=DveQ1O9i44SpHvjp)
- [Video Tutorial: Use of COUNTA function](https://youtu.be/0JCfxebwKa4?si=fT9eBy3X1i5qmhER)
further reading:

- [COUNT function - Microsoft Support](https://support.microsoft.com/en-us/office/count-function-a59cd7fc-b623-4d93-87a4-d23bf411294c#:~:text=The%20COUNT%20function%20counts%20the,range%20or%20array%20of%20numbers.)

##### POWER

Returns the result of a number raised to a power.

>Syntax  

```excel
POWER(number, power)
```

The POWER function syntax has the following arguments:

Number Required. The base number. It can be any real number.
Power Required. The exponent to which the base number is raised.

```excel
=POWER(5,2)
```

- [Video Tutorial: Power function in excel](https://youtu.be/Brd7LkDfPXY?si=W8I3vV92mN6WE1Cl)
  
further reading:

- [POWER function - Microsoft Support](https://support.microsoft.com/en-au/office/power-function-d3f2908b-56f4-4c3f-895a-07fb519c362a)

##### PRODUCT function

- The PRODUCT function multiplies all the numbers given as arguments and returns the product.
- The PRODUCT function is useful when you need to multiply many cells together.

For example, the formula =PRODUCT(A1:A3, C1:C3) is equivalent to `=A1 * A2 * A3 * C1 * C2 * C3`.

```excel
=Product(5,2)
=Product(C6:E6)
```

- [Video Tutorial: PRODUCT function in excel](https://youtu.be/G-6sxw5Dvpw?si=oZ4INRYwoIg223lc)
  
further reading:

- [PRODUCT function - Microsoft Support](https://support.microsoft.com/en-gb/office/product-function-8e6b5b24-90ee-4650-aeec-80982a0512ce#:~:text=Description,arguments%20and%20returns%20the%20product.)

##### Average function

- Returns the average (arithmetic mean) of the arguments.

For example, if the range A1:A20 contains numbers, the formula =AVERAGE(A1:A20) returns the average of those numbers.

- [Video Tutorial: Use of AVERAGE() function in excel](https://youtu.be/WtETTSFaWSs?si=acofncokcJ9wtJIr)

further reading:

- [AVERAGE function - Microsoft Support](https://support.microsoft.com/en-gb/office/average-function-047bac88-d466-426c-a32b-8f33eb960cf6)

##### IF function

- The IF function is one of the most popular functions in Excel, and it allows you to make logical comparisons between a value and what you expect.
- So an IF statement can have two results. The first result is if your comparison is True, the second if your comparison is False.

For example, `=IF(C2=”Yes”,1,2)` says IF(C2 = Yes, then return a 1, otherwise return a 2).

- [Video Tutorial:Use of IF function in excel](https://youtu.be/hftoKkdWNRk?si=POM60zBSWg5tZ-i8)

further reading:

- [IF function - Microsoft Support](https://support.microsoft.com/en-us/office/if-function-69aed7c9-4e8a-4755-a9bc-aa8bbff73be2)

##### NOW function

The NOW function is useful when you need to display the current date and time on a worksheet or calculate a value based on the current date and time, and have that value updated each time you open the worksheet.

further reading:

- [NOW function - Microsoft Support](https://support.microsoft.com/en-au/office/now-function-3337fd29-145a-4347-b2e6-20c904739c46)

##### TODAY

The TODAY function is useful when you need to have the current date displayed on a worksheet, regardless of when you open the workbook.

For example, if you know that someone was born in 1963, you might use the following formula to find that person's age as of this year's birthday:

```excel
= YEAR(TODAY())-1963
```

- [Video Tutorial: TODAY and NOW functions in excel](https://youtu.be/9ETguwC7Jnk?si=COwxFgKO5WBe1WKX)

further reading:

- [TODAY function - Microsoft Support](https://support.microsoft.com/en-au/office/today-function-5eb3078d-a82c-4736-8930-2f51a028fdd9)
- [Insert the current date and time in a cell - Microsoft Support](https://support.microsoft.com/en-gb/office/insert-the-current-date-and-time-in-a-cell-b5663451-10b0-40ab-9e71-6b0ce5768138)


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

- [Change the case of text in excel](https://youtu.be/X38NcRn0PhM?si=pCO7K-DuBJKz5G9b)

further reading:

- [LOWER function - Microsoft Support](https://support.microsoft.com/en-us/office/lower-function-3f21df02-a80c-44b2-afaf-81358f9fdeb4#:~:text=The%20LOWER%20function%20syntax%20has,text%20that%20are%20not%20letters.)
- [UPPER function - Microsoft Support](https://support.microsoft.com/en-gb/office/upper-function-c11f29b3-d1a3-4537-8df6-04d0049963d6)
- [Change the case of text - Microsoft Support](https://support.microsoft.com/en-gb/office/change-the-case-of-text-01481046-0fa7-4f3b-a693-496795a7a44d)

#### LEN function

LEN returns the number of characters in a text string.

>Syntax  
LEN(text)

LENB(text)

Text Required. The text whose length you want to find. Spaces count as characters.

further reading:

- [LEN, LENB functions - Microsoft Support](https://support.microsoft.com/en-gb/office/len-lenb-functions-29236f94-cedc-429d-affd-b5e33d2c67cb#:~:text=LEN%20returns%20the%20number%20of,be%20available%20in%20all%20languages.)
  
#### COUNTIF function

Use COUNTIF, to count the number of cells that meet a criterion; for example, to count the number of times a particular city appears in a customer list.

For example:

```excel
=COUNTIF(A2:A5,"London")
=COUNTIF(A2:A5,A4)
```

- [Video Tutorial: Use of COUNTIF function in excel](https://youtu.be/Uv-j-N7wdTo?si=GjA232Ni4UVt0cEv)

further reading:

- [COUNTIF function - Microsoft Support](https://support.microsoft.com/en-us/office/countif-function-e0de10c6-f885-4e71-abb4-1f464816df34)

#### SUMIF function

use the SUMIF function to sum the values in a range that meet criteria that you specify.

For example, suppose that in a column that contains numbers, you want to sum only the values that are larger than 5. You can use the following formula: =SUMIF(B2:B25,">5")

>Syntax  
SUMIF(range, criteria, [sum_range])

- [Video Tutorial: SUMIF function in excel](https://youtu.be/AX7DXRCoaf8?si=iPntuexdimCN7ojw)
  
further reading:

- [SUMIF function - Microsoft Support](https://support.microsoft.com/en-us/office/sumif-c44b60c3-c9f4-4789-80fe-28a07f9b75b1)

#### Concat function

- [Join First Name and Last Name in the Excel | CONCAT function](https://youtu.be/6Puk_HhpFRM?si=NjnKFCa6bBOsMJIH)

### Formula Errors

- [Video Tutorial: Top 4 Most Common Excel Errors](https://youtu.be/Rh0I5B-0uHM?si=nv9OyoivwApx0ssf)

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

**Note:** You can enter #N/A in those cells where data is not yet available. Formulas that refer to those cells will then return #N/A instead of attempting to calculate a value.

### New functions - Microsoft 365

- [Find Employee using XLOOKUP function](https://youtu.be/vUCB2zLwG3g)
- [Generate Serial # using sequence](https://youtu.be/gKds5egFFJI)
- [CHOOSECOL](https://youtu.be/ZzdTxA0Elqk)
- [How to: Filter data by using a formula in excel](https://youtu.be/B1nPF2OGkKI)
- [TEXTSPLIT: split cells / text strings by delimiter](https://youtu.be/hRr9YnZvK6w)

### More Functions

- [Video Tutorial: Insert copyright, registered and trademark symbols | Microsoft Excel](https://youtu.be/Zf-VfFlCMYI?si=sHIXhL5g4aG1w4fi)
- [Video Tutorial: Find unique list of cities using Unique Function](https://youtu.be/dISzLBMgZF0)
- [Video Tutorial: DAYS](https://youtu.be/1CRDkupdYrQ)
- [Video Tutorial: TRANSPOSE function:Vertical range of cells as a horizontal range](https://youtu.be/81Lk7ke7UNw)
- [Video Tutorial: Display formula of cell as string in Excel](https://youtu.be/lUg8zYzisuk)
- [Video Tutorial: Array of text values from range of cells](https://youtu.be/Sa8qdcZ8vXc)
- [Video Tutorial: Date](https://youtu.be/UpJluY3XY74)
- [Video Tutorial: Generate Serial # using sequence in excel](https://youtu.be/gKds5egFFJI?si=JP4kFby1VPxJOb9i)
- [Video Tutorial: Converts a number from one measurement system to another | Microsoft Excel](https://youtu.be/ilEpvXG1NO4?si=mXBMoNtCiPXuvu6j)
- [Video Tutorial: Generate a sequence end with text | Microsoft Excel](https://youtu.be/urzWGZDpGGk?si=WGFdphwk0dSXT6XE)
- [Video Tutorial: Format numbers as TEXT in Microsoft Excel](https://youtu.be/9-ldmZ3Z8Iw?si=q95ulIUXbHdmQxjs)
- [Video Tutorial: Append data from multiple sheets into one sheet | Microsoft Excel](https://youtu.be/RjALEkatPEk?si=Mnsiz78dypUVokJm)


- [Video Tutorial: Excel Mobile | TOP 25 Tips to use Excel Mobile App | Microsoft 365](https://youtu.be/y9m36XLI4v4?si=iRfz-u-Np3SdgE_J)


### Review Questions

Beginner:

1. What is the formula to calculate the sum of a range of cells?
2. What is the formula to calculate the average of a range of cells?
3. What is the formula to count the number of cells in a range that contain a specific value?
4. What is the formula to calculate the minimum or maximum value in a range of cells?
5. What is the formula to round a number to a specific number of decimal places?
6. What is function? Enlist some important functions of Excel?
7. What is the difference between a relative cell reference and an absolute cell reference?
8. How do you use the $ symbol to lock cell references in a formula?
9. What is the use of Conditional Formatting?
10. What is the use of Data Validation?
11. What is the purpose of the comparison operators (e.g., <, >, =) in Excel, and how are they used in formulas?
12. How can you use logical operators (AND, OR, NOT) in Excel formulas to perform conditional calculations?
13. What is the ampersand operator (&) used for when working with cell references in Excel?
14. Explain the use of the range operator (colon, :) in Excel and how it simplifies cell referencing.
15. How can you use the IF function in Excel to perform conditional operations? How does it relate to operators?
16. Explain how to use the CONCATENATE function and the operator for line breaks in Excel to create multi-line text.
17. Describe the use of the CONCATENATE function versus the "&" operator for text manipulation in Excel
18. What are some common functions used in Excel formulas?
19. How would you write a formula to calculate the total sales for each product in a worksheet?
20. How would you write a formula to count the number of cells in a range that contain the text "Apple"?
21. What does the following formula do?

```excel
=IF(A1>B1,"A1 is greater than B1","A1 is less than or equal to B1")
```

What is conditional formatting, and how can you use it to highlight specific data in Excel?

### Excercises

**Exercise 1:**

- Create a new Excel worksheet.
- In cells A1 to A10, enter the following numbers: 10, 20, 30, 40, 50, 60, 70, 80, 90, and 100.
- In cell A11, enter the following formula: `=SUM(A1:A10)`
- Press Enter.

The result, 550, should appear in cell A11.

**Exercise 2:**

- Create a new Excel worksheet.
- In cells A1 to A10, enter the following numbers: 10, 20, 30, 40, 50, 60, 70, 80, 90, and 100.
- In cell A11, enter the following formula: `=AVERAGE(A1:A10)`
- Press Enter.

The result, 55, should appear in cell A11.

**Exercise 3:**

- Create a new Excel worksheet.
- In cells A1 to A10, enter the following numbers: 10, 20, 30, 40, 50, 60, 70, 80, 90, and 100.
- In cell A11, enter the following formula: `=MAX(A1:A10)`
- Press Enter.

The result, 100, should appear in cell A11.

**Exercise 4:**

- Create a new Excel worksheet.
- In cells A1 to A10, enter the following numbers: 10, 20, 30, 40, 50, 60, 70, 80, 90, and 100.
- In cell A11, enter the following formula: `=MIN(A1:A10)`
- Press Enter.

The result, 10, should appear in cell A11.

**Exercise 5:**

- Create a new Excel worksheet.
- In cells A1 to A10, enter the following numbers: 10, 20, 30, 40, 50, 60, 70, 80, 90, and 100.
- In cell A11, enter the following formula: `=IF(A1>A2,"A1 is greater than A2","A1 is not greater than A2")`
- Press Enter.

The result, "A1 is greater than A2", should appear in cell A11.

**Exercise 6: Power and Square Root**:

- In cell A1, enter a number, e.g., 4.
- In cell B1, calculate the square of the number using the formula `=A1^2`.
- In cell B2, calculate the square root of the number using the formula `=SQRT(A1)`.

Rounding:

In cell A1, enter a decimal number, e.g., 7.85.
In cell B1, round the number to the nearest whole number using the formula =ROUND(A1, 0).
In cell B2, round the number to one decimal place using the formula =ROUND(A1, 1).

Random Numbers:

In cell A1, enter the formula =RAND(). This will generate a random number between 0 and 1.
Drag the fill handle (the small square at the bottom-right corner of the cell) down to generate multiple random numbers.


Which of the following is a valid formula?

A. =SUM(A1:B1)/2
B. =SUM(A1:B1) + 2
C. =SUM(A1:B1) * 2
D. All of the above

Which of the following formulas will return the value 10?

(A) =SUM(1, 2, 3, 4)
(B) =AVERAGE(1, 2, 3, 4)
(C) =MAX(1, 2, 3, 4)
(D) =MIN(1, 2, 3, 4)

## Muhammad Yasir Bhutta

- [Web](https://yasirbhutta.github.io/)
- [Youtube](https://www.youtube.com/yasirbhutta)
- [Facebook](https://www.facebook.com/yasirbhutta786)
- [Twitter](https://twitter.com/yasirbhutta)
