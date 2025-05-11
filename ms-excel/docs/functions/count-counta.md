---
layout: page
title: "Excel COUNT vs COUNTA Function Explained | Excel Formula Guide"
description: Understand the difference between COUNT and COUNTA functions in Excel. Learn syntax, use cases, and examples to improve your data counting skills.
keywords: excel COUNT, excel COUNTA, COUNT vs COUNTA, COUNT function in excel, COUNTA function in excel, how to use COUNT, how to use COUNTA, excel formulas, excel data functions, MS excel tips, count a examples, counta examples
author: Muhammad Yasir Bhutta
course: ms-excel
topic: functions
toc: toc/ms-excel-toc.html
prev: /ms-excel/docs/functions/average.html
next: /ms-excel/docs/functions/countif.html
breadcrumb:
  - title: Home
    url: /
  - title: Excel
    url: /ms-excel/
  - title: Functions
    url: /ms-excel/docs/functions.html
---
## COUNT

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
