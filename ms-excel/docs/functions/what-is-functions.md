---
layout: page
title: "What Are Functions in Excel? | Excel Functions Explained for Beginners"
description: Discover what functions in Microsoft Excel are, how they work, and why they’re essential for efficient data analysis. Learn Excel basics with clear examples for beginners..
keywords: Excel functions, what is function in Excel, Excel basics, Excel for beginners, Microsoft Excel tutorial, how to use functions in Excel, Excel formula guide, data analysis in Excel
author: Muhammad Yasir Bhutta
course: ms-excel
topic: functions
toc: toc/ms-excel-toc.html
prev: /ms-excel/docs/functions/cell-references.html
next: /ms-excel/docs/functions/sum.html
breadcrumb:
  - title: Home
    url: /
  - title: Excel
    url: /ms-excel/
  - title: Functions
    url: /ms-excel/docs/functions.html
---

## **What Are Functions?**  

Functions are predefined formulas that perform calculations by using specific values, called arguments, in a particular order, or structure. These functions help you perform calculations, analyze data, and automate tasks quickly. ([Microsoft Support][1])

## **How Do Functions Work?**  
Functions follow a specific structure:  

1. **Function Name** – The type of calculation you want to perform (e.g., `SUM`, `AVERAGE`).  
2. **Opening Parenthesis `(`** – Starts the function’s arguments.  
3. **Arguments** – The inputs the function needs to work. These can be:  
   - Numbers  
   - Text  
   - Cell references (e.g., `A1`, `B2:B10`)  
   - Other functions (called **nested functions**)  
4. **Closing Parenthesis `)`** – Ends the function.  

### **Example:**  
`=SUM(A1:A5)`  
- `SUM` → Function name  
- `(A1:A5)` → Argument (adds values from cells A1 to A5)  

### **Nested Functions**  
You can use a function **inside another function** for more complex calculations.  

**Example:**  
`=AVERAGE(SUM(B2:B5), C2)`  
- First, `SUM(B2:B5)` adds the values in B2 to B5.  
- Then, `AVERAGE` calculates the mean of that sum and cell C2.  

## References and Bibiography

[1]: https://support.microsoft.com/en-us/office/using-functions-and-nested-functions-in-excel-formulas-3f4cf298-ded7-4f91-bc80-607533b65f02 "Using functions and nested functions in Excel formulas - Microsoft Support"
