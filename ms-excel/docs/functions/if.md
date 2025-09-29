---
layout: page
title: "How to Use IF Function in Excel | Excel Formula Guide"
description: Learn the IF function in Excel to perform conditional logic in your formulas. Learn syntax, examples, and tips for decision-making in your spreadsheets.
keywords: excel IF function, how to use IF in excel, excel conditional logic, excel IF formula, excel formulas, MS excel tips, excel function guide, excel tutorial, decision-making in excel
author: Muhammad Yasir Bhutta
course: ms-excel
topic: functions
toc: toc/ms-excel-toc.html
prev: /ms-excel/docs/functions/concat.html
next: /ms-excel/docs/functions/formula-errors.html
breadcrumb:
  - title: Home
    url: /
  - title: Excel
    url: /ms-excel/
  - title: Functions
    url: /ms-excel/docs/functions.html
---

[Download PDF](/downloads/ms-excel/functions/if.pdf)

## IF function

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

**Exercise 5:**

- Create a new Excel worksheet.
- In cells A1 to A10, enter the following numbers: 10, 20, 30, 40, 50, 60, 70, 80, 90, and 100.
- In cell A11, enter the following formula: `=IF(A1>A2,"A1 is greater than A2","A1 is not greater than A2")`
- Press Enter.

The result, "A1 is not greater than A2", should appear in cell A11.

