---
layout: page
title: "How to Use CONCAT Function in Excel | Excel Formula Guide"
description: Learn how to use the CONCAT function in Excel to join text from multiple cells. Includes syntax, examples, and tips for efficient text handling.
keywords: excel CONCAT, CONCAT function in excel, how to use CONCAT, combine text in excel, excel text functions, excel formulas, excel function guide, MS excel tips, excel tutorial, text concatenation in excel
author: Muhammad Yasir Bhutta
course: ms-excel
topic: functions
toc: toc/ms-excel-toc.html
prev: /ms-excel/docs/functions/len-lenb.html
next: /ms-excel/docs/functions/if.html
breadcrumb:
  - title: Home
    url: /
  - title: Excel
    url: /ms-excel/
  - title: Functions
    url: /ms-excel/docs/functions.html
---

[Download PDF](/downloads/ms-excel/functions/concat.pdf)

## Concat function - Combine text from two or more cells into one cell

- The CONCAT function combines the text from multiple ranges and/or strings, but it doesn't provide delimiter or IgnoreEmpty arguments.

**Syntax:**

```excel
CONCAT(text1, [text2],…)
```

For example, =CONCAT("The"," ","sun"," ","will"," ","come"," ","up"," ","tomorrow.") will return The sun will come up tomorrow.

[Video Tutorial: Join First Name and Last Name in the Excel - CONCAT function](https://youtu.be/6Puk_HhpFRM?si=NjnKFCa6bBOsMJIH)

**See also:**
  
- [Excel Help & Training - Combine text from two or more cells into one cell](https://support.microsoft.com/en-us/office/combine-text-from-two-or-more-cells-into-one-cell-81ba0946-ce78-42ed-b3c3-21340eb164a6)

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
