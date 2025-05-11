---
layout: page
title: "How to Use COUNTIF Function in Excel | Excel Formula Guide"
description: Learn how to use the COUNTIF function in Excel to count cells based on criteria. Includes syntax, examples, and tips for accurate data filtering.
keywords: excel COUNTIF, COUNTIF function in excel, how to use COUNTIF, count with condition in excel, excel criteria-based count, excel formulas, MS excel tips, excel function guide, excel data analysis, excel tutorial
author: Muhammad Yasir Bhutta
course: ms-excel
topic: functions
toc: toc/ms-excel-toc.html
prev: /ms-excel/docs/functions/count-counta.html
next: /ms-excel/docs/functions/power.html
breadcrumb:
  - title: Home
    url: /
  - title: Excel
    url: /ms-excel/
  - title: Functions
    url: /ms-excel/docs/functions.html
---

## COUNTIF function

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
