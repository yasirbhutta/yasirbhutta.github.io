---
layout: page
title: "Excel SUMIF Function Guide with Examples"
description: Learn how to use the Excel SUMIF function with clear examples and syntax. Perfect for beginners and advanced users looking to master conditional summing..
keywords: excel SUMIF, SUMIF function in excel, how to use SUMIF, excel conditional sum, excel formulas, SUMIF examples, MS excel tips, excel function guide, excel tutorial, excel for beginners, sumif tasks, sumif exercises
author: Muhammad Yasir Bhutta
course: ms-excel
topic: functions
toc: toc/ms-excel-toc.html
prev: /ms-excel/docs/functions/sum.html
next: /ms-excel/docs/functions/max-min.html
breadcrumb:
  - title: Home
    url: /
  - title: Excel
    url: /ms-excel/
  - title: Functions
    url: /ms-excel/docs/functions.html
---

[Download PDF](/downloads/ms-excel/functions/sumif.pdf)

# SUMIF function

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
