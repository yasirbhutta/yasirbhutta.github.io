# Microsoft Excel - Microsoft 365

Connect with me: [Youtube](https://www.youtube.com/yasirbhutta) | [LinkedIn](https://www.linkedin.com/in/yasirbhutta/) | [WhatsApp Channel](https://whatsapp.com/channel/0029VaC3BC160eBZZSs3CW0c) | [Web](https://yasirbhutta.github.io/) | [Facebook](https://www.facebook.com/yasirbhutta786) | [Twitter](https://twitter.com/yasirbhutta)

- [Download: Handouts PDF](https://yasirbhutta.github.io/ms-excel/docs/functions.pdf)
- To access the updated handouts, please click on the following link:
[https://yasirbhutta.github.io/ms-excel/docs/functions.html](https://yasirbhutta.github.io/ms-excel/docs/functions.html)
- [Youtube Playlist to learn excel](https://youtube.com/playlist?list=PLKYRx0Ibk7Vh3MomITbYSF5I-NGTW5s7f&si=TBb3FDR21BnlJO9r)
- [Slides](https://docs.google.com/presentation/d/1z9o05Mi10xwlSupsi3lWHHxNQSeR56JmKaLw9Z6gB0o/)
  
- [Microsoft Excel - Microsoft 365](#microsoft-excel---microsoft-365)
  - [Modules - Functions](#modules---functions)
    - [Module 1: Functions in Excel - I](#module-1-functions-in-excel---i)
    - [Module 2: Functions in Excel II](#module-2-functions-in-excel-ii)
    - [Module 3: Functions in Excel III](#module-3-functions-in-excel-iii)
  - [Functions in Excel](#functions-in-excel)
    - [Cell References](#cell-references)
    - [Copying Formulae](#copying-formulae)
    - [Cell Reference](#cell-reference)
      - [Relative Cell Reference](#relative-cell-reference)
      - [Absolute Cell References](#absolute-cell-references)
      - [Mixed Cell Reference](#mixed-cell-reference)
    - [Functions](#functions)
      - [10 Most popluar functions](#10-most-popluar-functions)
        - [1. SUM](#1-sum)
      - [SUMIF function](#sumif-function)
        - [MAX](#max)
        - [MIN](#min)
      - [COUNT](#count)
      - [COUNTA](#counta)
      - [COUNTIF function](#countif-function)
        - [POWER](#power)
        - [PRODUCT function](#product-function)
        - [Average function](#average-function)
        - [Use of cell references in a formula](#use-of-cell-references-in-a-formula)
        - [IF function](#if-function)
          - [See also](#see-also)
        - [NOW function](#now-function)
        - [TODAY](#today)
      - [Change the case of Text](#change-the-case-of-text)
      - [LEN function](#len-function)
      - [Concat function - Combine text from two or more cells into one cell](#concat-function---combine-text-from-two-or-more-cells-into-one-cell)
    - [Formula Errors](#formula-errors)
    - [New functions - Microsoft 365](#new-functions---microsoft-365)
    - [More Functions](#more-functions)
  - [Additional topics](#additional-topics)
    - [Named Cell Reference](#named-cell-reference)
  - [True/False (Mark T for True and F for False)](#truefalse-mark-t-for-true-and-f-for-false)
  - [Multiple Choice (Select the best answer)](#multiple-choice-select-the-best-answer)
    - [Review Questions](#review-questions)
    - [Excercises](#excercises)
  - [Multiple Choice Questions](#multiple-choice-questions)
  - [References](#references)
  - [Muhammad Yasir Bhutta](#muhammad-yasir-bhutta)

## Modules - Functions

### Module 1: Functions in Excel - I

- Cell reference type
- Copying formula
- What is Function and Its Structure
- Functions: SUM, SUMIF
- Use AutoSum to sum numbers

### Module 2: Functions in Excel II

- Functions: MIN, MAX, COUNT, COUNTA, COUNTIF, POWER, AVERAGE, PRODUCT

### Module 3: Functions in Excel III

- Referencing cells in formulas
- Functions: IF, TODAY, NOW, LOWER, UPPER, PROPER, LEN

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
  
**For example,** if you enter the formula `=$A$1+$B$1` into cell C1, and then copy that formula to cell D2, the formula will remain the same. This is because Excel knows that you want to add the specific cells A1 and B1, regardless of where the formula is copied.

- [Video Tutorial: Create an Absolute Reference in Excel](https://youtu.be/NDBp1p6g_4c?si=ULHKKtku6Ts6U_Zz)

#### Mixed Cell Reference

- You create a mixed cell reference when you set either the column or row reference fixed instead of both being absolute
- Absolute row reference -If a dollar sign were to precede only the row number, Example
- **A$1**, then only the column reference changes relatively when the formula is copied
- Absolute column reference -If a dollar sign precedes only the column letter, e.g. $A1, Excel will change only the row reference relative to the change in the formula location

### Functions

- Excel has hundreds of predefined formulae known as Functions
- Functions use specific `arguments` in a particular order or structure
  - The arguments of functions can be anything from numbers, text, logical values, or cell references
  - You can also have formulae or other functions as arguments in a function that are called nested functions.

Functions ….
The normal order for a function is:-

- `Function Name`,
- The opening `parenthesis (`
- `Arguments` for the function separated by commas and `closing parenthesis )`.

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

#### 10 Most popluar functions

##### 1. SUM

- The SUM function adds values. 
- You can add individual values, cell references or ranges or a mix of all three.

>For example:  

```
=SUM(A2:A10) Adds the values in cells A2:10.  
=SUM(A2:A10, C2:C10) Adds the values in cells A2:10, as well as cells C2:C10.  
```
**Tip:** You can also type “ALT + =” into a cell, and Excel automatically inserts the SUM function. (windows)

**Use AutoSum to sum numbers:**

- [Video Tutorial: Use of Sum function and AutoSum to sum numbers - Microsoft Excel](https://youtu.be/o8aBs1Qr_8s?si=54T8YseIfXyJt5Fg)

> **Tips:** [Click here to learn  Copy values quickly from the status bar](https://youtu.be/beDE-DM3e2k)

**See also:**

- [Sum Function - Excel Exercises](https://excelexercises.com/practice.html?lesson=1)
- [SUM function - Microsoft Support](https://support.microsoft.com/en-us/office/sum-function-043e1c7d-7726-4e80-8f32-07b23e057f89)
- Use AutoSum to sum numbers - Microsoft Support [[Windows]](https://support.microsoft.com/en-us/office/use-autosum-to-sum-numbers-543941e7-e783-44ef-8317-7d1bb85fe706) [[Android]](https://support.microsoft.com/en-us/office/use-autosum-to-sum-numbers-543941e7-e783-44ef-8317-7d1bb85fe706#ID0EBBF=Android)

#### SUMIF function

use the SUMIF function to sum the values in a range that meet criteria that you specify.

For example, suppose that in a column that contains numbers, you want to sum only the values that are larger than 5. You can use the following formula: =SUMIF(B2:B25,">5")

>Syntax

```excel
SUMIF(range, criteria, [sum_range])
```

- [Video: How to use the SUMIF function in Microsoft Excel](https://youtu.be/AX7DXRCoaf8?si=iPntuexdimCN7ojw)
  
**See also:**

- [SUMIF function - Microsoft Support](https://support.microsoft.com/en-us/office/sumif-function-169b8c99-c05c-4483-a712-1697a653039b)
- [SUMIF function - Excel Help & Training](https://support.microsoft.com/en-us/office/sumif-c44b60c3-c9f4-4789-80fe-28a07f9b75b1)
- [Video: How to use the SUMIF function in Microsoft Excel - Microsoft 365](https://www.youtube.com/watch?v=7395LUP9dsk)

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

further reading:

- [COUNT function - Microsoft Support](https://support.microsoft.com/en-us/office/count-function-a59cd7fc-b623-4d93-87a4-d23bf411294c#:~:text=The%20COUNT%20function%20counts%20the,range%20or%20array%20of%20numbers.)

#### COUNTA

- The COUNTA function counts the number of cells that are not empty in a range.

- [Video Tutorial: Use of COUNTA function](https://youtu.be/0JCfxebwKa4?si=fT9eBy3X1i5qmhER)

See Also

- [COUNTA function - Microsoft Support](https://support.microsoft.com/en-gb/office/counta-function-7dc98875-d5c1-46f1-9a82-53f3219e2509#:~:text=The%20COUNTA%20function%20counts%20cells,does%20not%20count%20empty%20cells.)

#### COUNTIF function

Use COUNTIF, to count the number of cells that meet a criterion; for example, to count the number of times a particular city appears in a customer list.

>Syntax

```excel
COUNTIF(range, criteria)
```

For example:

```excel
=COUNTIF(A2:A5,"London")
=COUNTIF(A2:A5,A4)
```

- [Video Tutorial: Use of COUNTIF function in excel](https://youtu.be/Uv-j-N7wdTo?si=GjA232Ni4UVt0cEv)

**see also:**

- [COUNTIF function - Microsoft Support](https://support.microsoft.com/en-us/office/countif-function-e0de10c6-f885-4e71-abb4-1f464816df34)

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

For example, if the range A1:A20 contains numbers, the formula `=AVERAGE(A1:A20)` returns the average of those numbers.

- [Video Tutorial: Use of AVERAGE() function in excel](https://youtu.be/WtETTSFaWSs?si=acofncokcJ9wtJIr)

**See also:**

- [AVERAGE function - Excel Exercises](https://excelexercises.com/practice.html?lesson=31)
- [AVERAGE function - Microsoft Support](https://support.microsoft.com/en-gb/office/average-function-047bac88-d466-426c-a32b-8f33eb960cf6)

##### Use of cell references in a formula

- [Video Tutorial: Use cell refenences in a formul in Microsoft Excel](https://youtu.be/mdmYAOeGJoQ?si=xGxjvagLaCTQSlBp)

##### IF function

- The IF function is one of the most popular functions in Excel, and it allows you to make logical comparisons between a value and what you expect.
- So an IF statement can have two results. The first result is if your comparison is True, the second if your comparison is False.

**Syntax:**

Use the IF function, one of the [logical functions](https://support.microsoft.com/en-gb/office/logical-functions-reference-e093c192-278b-43f6-8c3a-b6ce299931f5), to return one value if a condition is true and another value if it's false. [^1]

```excel
IF(logical_test, value_if_true, [value_if_false])
```

For example:

```excel
=IF(A2>B2,"Over Budget","OK")
=IF(A2=B2,B4-A4,"")
```

Formula that uses the IF function

**logical_test (required):** The condition you want to test.

**value_if_true (required):** The value that you want returned if the result of logical_test is TRUE.

**value_if_false (optional):** The value that you want returned if the result of logical_test is FALSE.

For example, `=IF(C2=”Yes”,1,2)` says IF(C2 = Yes, then return a 1, otherwise return a 2).

- [Video Tutorial:Use of IF function in excel](https://youtu.be/hftoKkdWNRk?si=POM60zBSWg5tZ-i8)

**Example:**

```excel
=IF(A1>10,"Greater than 10","Less than or equal to 10")
```

This formula checks if the value in cell A1 is greater than 10. If it is, the formula returns the text “Greater than 10”. If it’s not, the formula returns “Less than or equal to 10”.

**Example:**

```excel
=IF(B1="Yes","Paid","Not Paid")
```

This formula checks if the value in cell B1 is “Yes”. If it is, the formula returns “Paid”. If it’s not, the formula returns “Not Paid”.

**Example:**

```excel
=IF(C1>=100,"Pass","Fail")
```

This formula checks if the value in cell C1 is greater than or equal to 100. If it is, the formula returns “Pass”. If it’s not, the formula returns “Fail”.

**Example:**

the following formula will return "Over Budget" if the value in cell A2 is greater than the value in cell B2, otherwise it will return "OK":

```excel
=IF(A2>B2,"Over Budget","OK")
```

**Example:**

the following formula will calculate the difference between the values in cell A2 and cell B2 if the value in cell A2 is greater than the value in cell B2, otherwise it will return 0:

```excel
=IF(A2>B2,A2-B2,0)
```

Here are some more examples of how to use the IF function:

**Check if a cell is empty:**

```excel
=IF(A2="","Empty","Not empty")
```

**Check if a cell contains a specific value:**

```excel
=IF(A2="Apple","Apple found","Apple not found")
```

**Check if a date is before or after a certain date:**

```excel
=IF(A2<B2,"Date is before", "Date is after")
```

**Calculate a discount based on the amount of a purchase:**

```excel
=IF(A2>100,A2*0.1,A2*0.05)
```

###### See also

- [IF function - Excel Help & Training](https://support.microsoft.com/en-us/office/if-function-69aed7c9-4e8a-4755-a9bc-aa8bbff73be2)
- [Create conditional formulas - Microsoft Support](https://support.microsoft.com/en-gb/office/create-conditional-formulas-ca916c57-abd8-4b44-997c-c309b7307831)
- [Using IF with AND, OR and NOT functions - Microsoft Support](https://support.microsoft.com/en-gb/office/using-if-with-and-or-and-not-functions-d895f58c-b36c-419e-b1f2-5c193a236d97)
- [Video Tutorial: IF with AND and OR](https://support.microsoft.com/en-gb/office/video-if-with-and-and-or-2a47066d-85d8-4751-a59d-3c69d2931c3e)

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

##### NOW function

The NOW function is useful when you need to display the current date and time on a worksheet or calculate a value based on the current date and time, and have that value updated each time you open the worksheet.

See also:

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

#### Task: Extracting Day and Month from a Date in Excel

To extract the day and month from a date in Excel, you can use the following functions:

1. **Day Function**: This function extracts the day of the month from a date.

   ```excel
   =DAY(date)
   ```

   Replace `date` with the cell reference that contains the date (e.g., `A1`).

2. **Month Function**: This function extracts the month from a date.

   ```excel
   =MONTH(date)
   ```

   Similarly, replace `date` with the cell reference.

For example, if cell `A1` contains the date `2025-02-06`, you can use the formulas as follows:

- `=DAY(A1)` will return `6`.
- `=MONTH(A1)` will return `2`. 

#### Change the case of Text

**LOWER function:** Converts all uppercase letters in a text string to lowercase.

**Syntax:**

```excel
LOWER(text)
```

The LOWER function syntax has the following arguments:

Text Required. The text you want to convert to lowercase. LOWER does not change characters in text that are not letters.

**UPPER function:** Converts text to uppercase.

**Syntax:**

```excel
UPPER(text)
```

The UPPER function syntax has the following arguments:

Text Required. The text you want converted to uppercase. Text can be a reference or text string.

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

**PROPER function:**

- [Video Tutorial: Change the case of text in excel](https://youtu.be/X38NcRn0PhM?si=pCO7K-DuBJKz5G9b)

**See also:**

- [LOWER function - Microsoft Support](https://support.microsoft.com/en-us/office/lower-function-3f21df02-a80c-44b2-afaf-81358f9fdeb4#:~:text=The%20LOWER%20function%20syntax%20has,text%20that%20are%20not%20letters.)
- [UPPER function - Microsoft Support](https://support.microsoft.com/en-gb/office/upper-function-c11f29b3-d1a3-4537-8df6-04d0049963d6)
- [Change the case of text - Microsoft Support](https://support.microsoft.com/en-gb/office/change-the-case-of-text-01481046-0fa7-4f3b-a693-496795a7a44d)

#### LEN function

LEN returns the number of characters in a text string.

**Syntax:**

```excel
LEN(text)
```

LENB(text)

Text Required. The text whose length you want to find. Spaces count as characters.

**See also:**

- [LEN, LENB functions - Microsoft Support](https://support.microsoft.com/en-gb/office/len-lenb-functions-29236f94-cedc-429d-affd-b5e33d2c67cb#:~:text=LEN%20returns%20the%20number%20of,be%20available%20in%20all%20languages.)

#### Concat function - Combine text from two or more cells into one cell

- The CONCAT function combines the text from multiple ranges and/or strings, but it doesn't provide delimiter or IgnoreEmpty arguments.

**Syntax:**

```excel
CONCAT(text1, [text2],…)
```

For example, =CONCAT("The"," ","sun"," ","will"," ","come"," ","up"," ","tomorrow.") will return The sun will come up tomorrow.

[Video Tutorial: Join First Name and Last Name in the Excel - CONCAT function](https://youtu.be/6Puk_HhpFRM?si=NjnKFCa6bBOsMJIH)

**See also:**
  
- [Excel Help & Training - Combine text from two or more cells into one cell](https://support.microsoft.com/en-us/office/combine-text-from-two-or-more-cells-into-one-cell-81ba0946-ce78-42ed-b3c3-21340eb164a6)

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

### New functions - Microsoft 365

- [Find Employee using XLOOKUP function](https://youtu.be/vUCB2zLwG3g)
- [Generate Serial # using sequence](https://youtu.be/gKds5egFFJI)
- [CHOOSECOL](https://youtu.be/ZzdTxA0Elqk)
- [How to: Filter data by using a formula in excel](https://youtu.be/B1nPF2OGkKI)
- [TEXTSPLIT: split cells / text strings by delimiter](https://youtu.be/hRr9YnZvK6w)

### More Functions

- [Video Tutorial: Insert copyright, registered and trademark symbols - Microsoft Excel](https://youtu.be/Zf-VfFlCMYI?si=sHIXhL5g4aG1w4fi)
- [Video Tutorial: Find unique list of cities using Unique Function](https://youtu.be/dISzLBMgZF0)
- [Video Tutorial: DAYS](https://youtu.be/1CRDkupdYrQ)
- [Video Tutorial: TRANSPOSE function:Vertical range of cells as a horizontal range](https://youtu.be/81Lk7ke7UNw)
- [Video Tutorial: Display formula of cell as string in Excel](https://youtu.be/lUg8zYzisuk)
- [Video Tutorial: Array of text values from range of cells](https://youtu.be/Sa8qdcZ8vXc)
- [Video Tutorial: Date](https://youtu.be/UpJluY3XY74)
- [Video Tutorial: Generate Serial # using sequence in excel](https://youtu.be/gKds5egFFJI?si=JP4kFby1VPxJOb9i)
- [Video Tutorial: Converts a number from one measurement system to another - Microsoft Excel](https://youtu.be/ilEpvXG1NO4?si=mXBMoNtCiPXuvu6j)
- [Video Tutorial: Generate a sequence end with text - Microsoft Excel](https://youtu.be/urzWGZDpGGk?si=WGFdphwk0dSXT6XE)
- [Video Tutorial: Format numbers as TEXT in Microsoft Excel](https://youtu.be/9-ldmZ3Z8Iw?si=q95ulIUXbHdmQxjs)
- [Video Tutorial: Append data from multiple sheets into one sheet - Microsoft Excel](https://youtu.be/RjALEkatPEk?si=Mnsiz78dypUVokJm)

- [Video Tutorial: Excel Mobile | TOP 25 Tips to use Excel Mobile App - Microsoft 365](https://youtu.be/y9m36XLI4v4?si=iRfz-u-Np3SdgE_J)

## Additional topics

### Named Cell Reference

- A name is a meaningful shorthand that makes it easier to understand the purpose of a cell reference, constant, formula or table.
- You can create a name that describes a cell or range.
- You can also use the labels of columns and rows on a worksheet to refer to the cells within those columns and rows.

Defined Names

- **Formulas > Defined Names > Create from Selection**

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

## Multiple Choice (Select the best answer)

What is the symbol for a cell reference in Excel?

(a) @
(b) $
(c) &
(d) %

What is a function?

(a) A predefined formula that performs a specific calculation
(b) A rule that tells Excel how to calculate something
(c) A cell in a spreadsheet
(d) The address of a cell

What is the purpose of a function?

(a) To perform a calculation
(b) To create a chart
(c) To filter data
(d) None of the above

What is a range of cells?

(a) A group of adjacent cells
(b) A single cell
(c) A formula
(d) The address of a cell

### Review Questions

Beginner:

1. What is the formula to calculate the sum of a range of cells?
2. What is the formula to calculate the average of a range of cells?
3. What is the formula to count the number of cells in a range that contain a specific value?
4. What is the formula to calculate the minimum or maximum value in a range of cells?
5. What is the formula to round a number to a specific number of decimal places?
6. What is the function in Microsoft Excel? Enlist some important functions?
7. Explain the purpose, syntax, and provide an example for each of the following Microsoft Excel functions: SUM, COUNT, SUMIF, and POWER.
8. What is the difference between a relative cell reference and an absolute cell reference?
9. How do you use the $ symbol to lock cell references in a formula?
10. What is the use of Conditional Formatting?
11. What is the use of Data Validation?
12. What is the purpose of the comparison operators (e.g., <, >, =) in Excel, and how are they used in formulas?
13. How can you use logical operators (AND, OR, NOT) in Excel formulas to perform conditional calculations?
14. What is the ampersand operator (&) used for when working with cell references in Excel?
15. Explain the use of the range operator ( colon, : ) in Excel and how it simplifies cell referencing.
16. How can you use the IF function in Excel to perform conditional operations? How does it relate to operators?
17. Explain how to use the CONCAT function and the operator for line breaks in Excel to create multi-line text.
18. Describe the use of the CONCAT function versus the "&" operator for text manipulation in Excel
19. What are some common functions used in Excel formulas?
20. How would you write a formula to calculate the total sales for each product in a worksheet?
21. How would you write a formula to count the number of cells in a range that contain the text "Apple"?
22. What does the following formula do?
23. What is the IF function used for?

The IF function is used to perform conditional logic in Excel. It can be used to test a condition and return a different value depending on the outcome of the test.
23. What is the difference between a logical test and a comparison operator?

**Answer:** A logical test is a condition that is evaluated to TRUE or FALSE. A comparison operator is a symbol that is used to compare two values.

```excel
=IF(A1>B1,"A1 is greater than B1","A1 is less than or equal to B1")
```

24. What is conditional formatting, and how can you use it to highlight specific data in Excel? (Windows only)

25. In Excel, write the formulas to calculate the following for the range of cells A1:A10, which contains the values {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}:**  
    1. **Minimum value**  
    2.  **Maximum value**  
    3.  **Sum of all values**  
    4.  **Average value**  
   
### Excercises

**Excercise:**

- Create a login on this website [https://excelexercises.com/](https://excelexercises.com/) and complete the practice exercises for all the Excel functions you have learned.

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

The result, "A1 is not greater than A2", should appear in cell A11.

**Exercise 6:** Power and Square Root

- In cell A1, enter a number, e.g., 4.
- In cell B1, calculate the square of the number using the formula `=A1^2`.
- In cell B2, calculate the square root of the number using the formula `=SQRT(A1)`.

**SUM FUNCTIONS (SUM, SUMIF):**

**Exercise :** Calculate the total marks for each students.

Sample Date:

| Student | Math | Science | History |
|---------|------|---------|---------|
| Alice   | 85   | 90      | 75      |
| Bob     | 70   | 88      | 80      |
| Carol   | 92   | 76      | 85      |
| David   | 78   | 82      | 70      |
| Emma    | 90   | 85      | 92      |


**Exercise:** Use the SUM function to calculate the total sales in the following table:

| Month    | Sales |
| -------- | ----- |
| January  | 100   |
| February | 120   |
| March    | 150   |
| April    | 180   |
| May      | 210   |

**Exercise:**  Use the `SUMIF` function to calculate the total sales for all products sold in the month of `January`.

Sample Date:

| Month    | Product Category | Sales |
| -------- | ---------------- | ----- |
| January  | Food             | 10    |
| January  | Clothing         | 20    |
| January  | Electronics      | 30    |
| February | Food             | 20    |
| February | Clothing         | 30    |
| February | Electronics      | 40    |

**Exercise:**  Use the `SUMIF` function to calculate the total sales of `Food` in the following table:

| Month    | Product Category | Sales |
| -------- | ---------------- | ----- |
| January  | Food             | 10    |
| January  | Clothing         | 20    |
| January  | Electronics      | 30    |
| February | Food             | 20    |
| February | Clothing         | 30    |
| February | Electronics      | 40    |

**Exercise:** In the following table, calculate the total sales for all products sold on March 8th:

| Date      | Product   | Sales |
| --------- | --------- | ----- |
| March 7th | Product A | 100   |
| March 7th | Product B | 200   |
| March 8th | Product C | 300   |
| March 8th | Product D | 400   |

**Exercise :** In the following table, calculate the total sales for all products sold to customers in the Pakistan:

| Customer   | Country        | Sales |
| ---------- | -------------- | ----- |
| Customer A | Pakistan       | 100   |
| Customer B | Canada         | 200   |
| Customer C | United Kingdom | 300   |
| Customer D | Pakistan       | 400   |

**Exercise:** Use the SUM function to calculate the total bonus for employees who have achieved a score of 90 or higher in a test.

| Employee | Test Score | Bonus |
| -------- | ---------- | ----- |
| Ali      | 85         | 100   |
| Ahmad    | 92         | 150   |
| Nasir    | 88         | 120   |
| Hamza    | 95         | 180   |
| Muhammad | 90         | 160   |

**Exercise :** Use the SUMIF function to calculate the total sales for products whose names contain the word "Phone."

| Product         | Sales |
| --------------- | ----- |
| SmartPhone 2020 | 1200  |
| PhoneCase       | 1500  |
| Tablet          | 1800  |
| Basic Phone     | 1400  |
| iPhone X        | 1600  |

**Exercise :** Calculate the total expenses for the "Food" category using the SUMIF function.

| Expense   | Category  | Amount |
|-----------|-----------|--------|
| Rent      | Housing   | 1000   |
| Groceries | Food      | 350    |
| Gas       | Transport | 75     |
| Dining    | Food      | 200    |
| Internet  | Utilities | 60     |

**Exercise :** Calculate the total sales for Product A and Product C using the SUMIF function with multiple criteria. Use the following data:

**Sample Data:**

| Product   | Region | Sales |
| --------- | ------ | ----- |
| Product A | North  | 250   |
| Product B | South  | 300   |
| Product C | North  | 150   |
| Product D | South  | 200   |
| Product A | South  | 300   |
| Product C | South  | 125   |

**Solution:**

```excel
=SUMIF(A2:A7, "Product A", C2:C7) + SUMIF(A2:A7, "Product C", C2:C7)
```

**COUNT FUNCTIONS (COUNT, COUNTIF):**

**Exercise :** Counting Numbers in a Range

1. Open a new Excel worksheet.
2. In column A, enter a list of numbers, including some blank cells and non-numeric values (e.g., A1: 5, A2: 10, A3: "Text," A4: 15, A5: 20, A6: Blank, A7: 25).
3. In cell B1, use the COUNT function to count the number of cells in column A that contain numbers.
4. The formula should be "=COUNT(A1:A7)." The result should be 4, as there are four numeric values in the range.

**Exercise :** Basic COUNT Function

1. Open a new Excel worksheet.
2. In column A, enter a mix of numbers and text (e.g., A1: 5, A2: "Apple," A3: 10, A4: 15, A5: "Orange").
3. In cell B1, use the COUNT function to count the number of numeric values in column A. Your formula should be like this: `=COUNT(A1:A5)`.

**Exercise :** Counting Blank Cells

1. Open a new Excel worksheet.
2. Create a range of cells (e.g., A1:A10) where some cells have values, and others are blank.
3. In cell B1, use the COUNTBLANK function to count the number of blank cells in the range (e.g., "=COUNTBLANK(A1:A10)").

**Exercise :** Counting with Logical Operators

1. Open a new Excel worksheet.
2. Create a list of test scores in column A (e.g., A1: 85, A2: 92, A3: 78, A4: 65, A5: 99).
3. In cell B1, use the COUNTIF function to count the number of scores greater than or equal to 90.
4. The formula should be `=COUNTIF(A1:A5, ">=90")`.

**Exercise :** Use the COUNTIF function to count the number of "Apples" in the list:

| Column A     |
| ------------ |
| Bananas      |
| Apples       |
| Oranges      |
| Apples       |
| Grapes       |
| Strawberries |
| Apples       |

**Exercise :** In the following table, count the number of cells in column B that contain the value "100".

| Column A  | Column B |
| --------- | -------- |
| Product A | 100      |
| Product B | 200      |
| Product C | 300      |
| Product D | 100      |

**Exercise :** In the following table, count the number of cells in column B that contain a value that contains the letter "a":

| Column A  | Column B |
| --------- | -------- |
| Product A | Apple    |
| Product B | Banana   |
| Product C | Carrot   |
| Product D | Orange   |

**Exercise :** In the following table, count the number of cells in column B that contain a value that starts with the letter "a":

| Column A  | Column B |
| --------- | -------- |
| Product A | Apple    |
| Product B | Banana   |
| Product C | Carrot   |
| Product D | Orange   |

**Exercise :** In the following table, count the number of cells in column B that contain a value that ends with the letter "e":

| Column A  | Column B |
| --------- | -------- |
| Product A | Apple    |
| Product B | Banana   |
| Product C | Carrot   |
| Product D | Orange   |

**STATISTICAL FUNCTIONS (AVERAGE, AVERAGEIF, MIN, MAX):**

**Exercise :** Find the highest value in the following range of cells:

```excel
range: A1:A5

values:

10
20
30
40
50
```

**Exercise :** Find the highest value in the following range of cells, ignoring empty cells and text values:

```excel
A1:A5
10
Apple
Bananas
30
50
```

**Exercise 1:** Calculate the average of the following numbers:

1, 2, 3, 4, 5

**Exercise :** Calculate the average of the numbers in the following range:

```excel
A1:A10
```

**Exercise :** Find the minimum value in the following range of cells:

```excel
A1:A10 = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}
```

**Excercise :** Find the minimum value in the following range, but only include the values that are in the column B:

| A | B  |
| - | -- |
| 1 | 2  |
| 3 | 4  |
| 5 | 6  |
| 7 | 8  |
| 9 | 10 |

**Exercise :** Calculate the average of the numbers in the following range, excluding the first and last numbers:

```excel
A1:A10
```

**Exercise 2:** Calculate the average per month sales of the year, using the following data:

A | B
------- | --------
**Month** | **Sales**
January | 1000
February | 1200
March | 1100
April | 1300
May | 1400
June | 1500
July | 1600
August | 1700
September | 1800
October | 1900
November | 2000
December | 2100

**Exercise 3:** Calculate the average of the sales figures for all customers who have spent more than $1000, using the following data:

Customer | Sales
------- | --------
Alice | 1000
Bob | 1200
Carol | 1100
Dave | 1300
Eve | 1400
Frank | 1500
George | 1600
Henry | 1700
Ian | 1800
James | 1900
Kate | 2000
Lily | 2100

**Exercise :** Calculate the average of the positive numbers in the following range:

```excel
A1:A10
```

**Exercise:** Rounding

- In cell A1, enter a decimal number, e.g., 7.85.
- In cell B1, round the number to the nearest whole number using the formula =ROUND(A1, 0).
- In cell B2, round the number to one decimal place using the formula =ROUND(A1, 1).

**Exercise:** Random Numbers

In cell A1, enter the formula =RAND(). This will generate a random number between 0 and 1.
Drag the fill handle (the small square at the bottom-right corner of the cell) down to generate multiple random numbers.

**LOGICIAL FUNCTIONS (IF, True/False, AND/OR):**

**TEXT MANIPULATION FUNCTIONS (CONCATE, TEXTJOIN, UPPER, POWER, PROPER):**

**Exercise :** Lowercase Conversion

1. Create a new worksheet.
2. In cell A1, type "PYTHON PROGRAMMING IS FUN."
3. In cell B1, use the LOWER function to convert the text in cell A1 to lgowercase. The formula should look like this: =LOWER(A1). B1 should display "python programming is fun."

**Exercise :** Proper Case Conversion

1. Open a new Excel worksheet.
2. In cell A1, type "muhammad ahmad."
3. In cell B1, use the PROPER function to convert the text in cell A1 to proper case. The formula should look like this: =PROPER(A1). B1 should display "Muhammad Ahmad."

**Exercise :** Change the following text to uppercase.

```excel
This is a sample text.
```

**Exercise:** Change the following text to lowercase.

```excel
THIS IS A SAMPLE TEXT.
```

**Exercise :** Change the following text to title case.

```excel
this is a sample text.
```

**Exercise :** Create a new column called "Title Case" and use the PROPER function to convert the text in Column A to title case.

Sample Data:

| **Good Habits**|
| ------------ |
| regular exercise|
| healthy eating       |
| adequate sleep      |
| time management|
| mindfulness and meditation|

**Exercise:**

1. In cell D1, type the following formula:

```excel
=CONCAT(A1, " ", B1, " is ", C1, " years old.")
```

Sample Data:

| Column A | Column B |Column C |
| ----     | ----     |----     |
|Muhammad  |Ali       |20       |

**Exercise:** Use the CONCAT function to combine the values in Column A and Column B into a single column, Col3, with a hyphen (-) in between.

Sample Data:

| Column A    | Column B |
| ----        | ----     |
| Muhammad    | Ali      |
| Muhammad    | Hamza    |
| Nasir       | Ahmad    |

Output:

| Column A    | Column B | Column C|
| ----        | ----     | ---     |
| Muhammad    | Ali      | Muhammad Ali|
| Muhammad    | Hamza    | Muhammad Hamza|
| Nasir       | Ahmad    | Nasir Ahmad|

**Exercise:** Write a formula using the CONCAT function to create a new column that contains the product name, quantity, and price, separated by a comma and a space, in the following format:

```excel
Product name, quantity, price
```

Sample Data:

|product Name | quantity | price|
|---- | --- | ---|
|Apple | 100 | 5|
|Banana | 200 | 4|
|Orange | 300 | 3|

**DATE FUNCTIONS (TODAY, NOW, DATE):**

**Exercise:** Calculate Age

1. In cell A1, enter a birthdate (e.g., 01/15/1980).
2. In cell B1, use the TODAY function to calculate the age. Subtract the birthdate in A1 from the current date (TODAY) and divide by 365.25 (accounting for leap years). The formula in B1 should look like this:

```excel
=(TODAY() - A1) / 365.25
```

The result in cell B1 will be the age in years.

**Exercise :** Calculate Days Remaining

1. In cell A1, enter a future date (e.g., 12/31/2023).
2. In cell B1, use the TODAY function to calculate the number of days remaining until the date in A1. The formula in B1 should look like this:

```excel
=A1 - TODAY()
```

The result in cell B1 will be the number of days remaining until the future date.

**Exercise:** Write the formula to find the date of the first day of the previous month.

- Type the following forumula in any cell:
  
```excel
=DATE(YEAR(TODAY()), MONTH(TODAY())-1, 1)
```

This formula calculates the date of the first day of the previous month. The DATE() function takes three arguments: the year, the month, and the day.

In this case, we are using the YEAR() and MONTH() functions to get the current year and month, respectively. We then subtract 1 from the month to get the month of the previous month. Finally, we set the day to 1 to get the date of the first day of the previous month.

**Exercise:** Calculate Elapsed Time

You can use the NOW function to calculate the elapsed time between two events.

1. In cell A5, type "Start Time:".
2. In cell B5, enter a start time (e.g., "9:00 AM").
3. In cell A6, type "End Time:".
4. In cell B6, use the following formula to calculate the elapsed time between the start and end times:

```excel
=TEXT(NOW()-B5, "hh:mm")
```

This formula subtracts the start time in cell B5 from the current time provided by NOW and formats the result as "hh:mm".

## Multiple Choice Questions

> What is the cell reference of the cell located at the intersection of column A and row 9?

1. [ ] A9
2. [ ] 9A
3. [ ] A1
4. [ ] 1A

> What is the cell reference of the range of cells A1 to A10?

1. [ ] A1:A10
2. [ ] A1-A10
3. [ ] 1A:10A
4. [ ] 1A-10A

> What is the cell reference of the cell located two rows below and one column to the right of cell B3?

1. [ ] C5
2. [ ] D5
3. [ ] C4
4. [ ] D4

> Which of the following is a valid cell reference in Excel?

1. [ ] A10
2. [ ] 10A
3. [ ] AA1
4. [ ] 100

> What does the $ symbol do when used in a cell reference in Excel?

1. [ ] It makes the cell reference absolute.
2. [ ] It makes the cell reference relative.
3. [ ] It makes the cell reference mixed.
4. [ ] It does nothing.

> What is the difference between a relative cell reference and an absolute cell reference?

1. [ ] A relative cell reference changes when the formula is copied to a different cell, while an absolute cell reference does not change.
2. [ ] An absolute cell reference changes when the formula is copied to a different cell, while a relative cell reference does not change.
3. [ ] There is no difference between a relative cell reference and an absolute cell reference.
4. [ ] Both relative and absolute cell references change when the formula is copied to a different cell.

> Which of the following is a valid mixed cell reference in Excel?

1. [ ] $A10
2. [ ] A$10
3. [ ] $A$10
4. [ ] 10A$10

> What is the cell reference of the cell two rows down and one column to the right of cell A1?

1. [ ] B3
2. [ ] A3
3. [ ] B2
4. [ ] A2

> What is the cell reference for the range of cells from A1 to B10?

1. [ ] A1:B10
2. [ ] 1:10
3. [ ] A1-B10
4. [ ] A1*B10

> Which of the following is a valid formula?

1. [ ] =SUM(A1:B1)/2
2. [ ] =SUM(A1:B1) , A2
3. [ ] =SUM(A1:B1) : B2
4. [ ] None

> Which of the following formulas will return the value 10?

1. [ ] =SUM(1, 2, 3, 4)
2. [ ] =AVERAGE(1, 2, 3, 4)
3. [ ] =MAX(1, 2, 3, 4)
4. [ ] =MIN(1, 2, 3, 4)

> What is the function for finding the maximum value in a range of cells?

1. [ ] MAX()
2. [ ] MIN()
3. [ ] AVERAGE()
4. [ ] COUNT()

> What is the function for counting the number of cells in a range that contain a specific value?

1. [ ] COUNTIF()
2. [ ] COUNTA()
3. [ ] SUMIF()
4. [ ] VLOOKUP()

> What is the function for rounding a number to a specified number of decimal places?

1. [ ] ROUND()
2. [ ] FLOOR()
3. [ ] CEILING()
4. [ ] TRUNC()

> The COUNTIF function is used to:

1. [ ] Count the number of cells in a range that meet a certain criteria
2. [ ] Calculate the average of values in a range that meet a certain criteria
3. [ ] Find the maximum value in a range that meet a certain criteria
4. [ ] None of the above

> What is the function for calculating the average of a range of cells?

1. [ ] SUM
2. [ ] AVERAGE
3. [ ] MIN
4. [ ] MAX

> What is the function for calculating the minimum value in a range of cells?

1. [ ] SUM
2. [ ] AVERAGE
3. [ ] MIN
4. [ ] MAX

> What is the function for counts the number of cells that are not empty in a range.

1. [ ] COUNTA
2. [ ] COUNTBLANK
3. [ ] COUNTIF
4. [ ] COUNTS

> What is the function for concatenating two or more text strings into a single text string?

1. [ ] MERGE
2. [ ] CONCAT
3. [ ] MIX
4. [ ] All of the above

> What is the syntax of the IF function?

1. [ ] =IF(logical_test, value_if_true, value_if_false)
2. [ ] =IF(condition, value_if_true, value_if_false)
3. [ ] =IF(logical_expression, value_if_true, value_if_false)
4. [ ] All of the above

> What is the logical test in the IF function?

1. [ ] The condition that you want to evaluate.
2. [ ] The value that you want to return if the logical test is true.
3. [ ] The value that you want to return if the logical test is false
4. [ ] None of the above.

> What is the value_if_true in the IF function?

1. [ ] The value that you want to return if the logical test is true.
2. [ ] The condition that you want to evaluate.
3. [ ] The value that you want to return if the logical test is false
4. [ ] None of the above.

> What is the value_if_false in the IF function?

1. [ ] The condition that you want to evaluate.
2. [ ] The value that you want to return if the logical test is true.
3. [ ] The value that you want to return if the logical test is false
4. [ ] None of the above.

> Which of the following is an example of an IF function?

1. [ ] =IF(A1>B1, "Greater", "Less")
2. [ ] =IF(A1=B1, "Equal", "Not Equal")
3. [ ] =IF(A1<>B1, "Not Equal", "Equal")
4. [ ] All of the above

> Which of the following is the correct syntax for the SUMIF function?

1. [ ] =SUMIF(range, criteria, sum_range)
2. [ ] =SUMIF(criteria, range, sum_range)
3. [ ] =SUMIF(sum_range, range, criteria)
4. [ ] =SUMIF(range, criteria)

>What is the purpose of the SUMIF function?

1. [ ] To calculate the sum of all values in a range that meet a specified criterion
2. [ ] To calculate the average of all values in a range that meet a specified criterion
3. [ ] To count the number of values in a range that meet a specified criterion
4. [ ] To find the maximum value in a range that meet a specified criterion

>Which of the following formulas will return the sum of all cells in the range A1:A100 that are greater than $100?

1. [ ] =SUMIF(A1:A100, ">100")
2. [ ] =SUMIF(A1:A100, "100")
3. [ ] =SUMIF(A1:A100, "A1:A100>100")
4. [ ] =SUMIF(A1:A100, "A1:A100", ">100")

>What is the purpose of the criteria argument in the SUMIF function?

1. [ ] It specifies the range of cells to be summed.
2. [ ] It defines the condition that determines which cells to include in the sum.
3. [ ] It is the result of the summation.
4. [ ] It is not required in the SUMIF function.

>What does the COUNTIF function return if no cells meet the specified criteria?

1. [ ] 0
2. [ ] An error message
3. [ ] #N/A
4. [ ] A blank cell

## References

[^1] [IF function - Excel Help & Training](https://support.microsoft.com/en-us/office/if-function-69aed7c9-4e8a-4755-a9bc-aa8bbff73be2)
[^2] [Excel Exercises](https://excelexercises.com/)
[^3] [COUNTIF function - Microsoft Support](https://support.microsoft.com/en-us/office/countif-function-e0de10c6-f885-4e71-abb4-1f464816df34)

## Muhammad Yasir Bhutta

- [Web](https://yasirbhutta.github.io/)
- [Youtube](https://www.youtube.com/yasirbhutta)
- [Facebook](https://www.facebook.com/yasirbhutta786)
- [Twitter](https://twitter.com/yasirbhutta)
