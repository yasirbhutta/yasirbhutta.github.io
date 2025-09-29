---
layout: page
title: "How to Use MAX and MIN Functions in Excel | Excel Guide"
description: Master the Excel MAX and MIN functions with easy examples. Learn how to find the highest and lowest values in your data using simple Excel formulas.
keywords: excel MAX, excel MIN, MAX function in excel, MIN function in excel, how to use MAX and MIN, excel highest value, excel lowest value, excel formulas, excel function guide, MS excel tips
author: Muhammad Yasir Bhutta
course: ms-excel
topic: functions
toc: toc/ms-excel-toc.html
prev: /ms-excel/docs/functions/sumif.html
next: /ms-excel/docs/functions/average.html
breadcrumb:
  - title: Home
    url: /
  - title: Excel
    url: /ms-excel/
  - title: Functions
    url: /ms-excel/docs/functions.html
---

[Download PDF](/downloads/ms-excel/functions/max-min.pdf)

## MAX

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
