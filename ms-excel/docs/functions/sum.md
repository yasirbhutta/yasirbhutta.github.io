---
layout: page
title: "How to Use the SUM Function in Excel – Complete Guide"
description: Learn how to use the SUM function in Microsoft Excel to quickly add values across cells, columns, or rows. Includes syntax, examples, and tips for efficient usage.
keywords: Excel SUM function, how to use SUM in Excel, Excel functions guide, Excel SUM formula, Excel add cells, Excel basics, Excel tutorials, Microsoft Excel functions, SUM formula examples
author: Muhammad Yasir Bhutta
course: ms-excel
topic: functions
toc: toc/ms-excel-toc.html
prev: /ms-excel/docs/functions/what-is-functions.html
next: /ms-excel/docs/functions/sumif.html
---

## Contents

- [Sum function](#sum-function)
- [Use AutoSum to sum numbers](#use-autosum-to-sum-numbers)

## SUM function

- The SUM function adds values. 
- You can add individual values, cell references or ranges or a mix of all three.

### **Syntax**:
```excel
=SUM(number1, [number2], [number3], ...)
```
- **`number1`** (required): The first number or range to add.
- **`number2, number3, ...`** (optional): Additional numbers or ranges (up to 255 total arguments).

---

### **Examples**:

1. **Sum individual numbers**:
   ```excel
   =SUM(5, 10, 15)  // Returns 30
   ```

2. **Sum a range of cells**:
   ```excel
   =SUM(A1:A10)  // Adds all numbers in cells A1 to A10
   ```

3. **Sum multiple ranges**:
   ```excel
   =SUM(A1:A5, B1:B5)  // Adds numbers in A1:A5 and B1:B5
   ```

4. **Sum with mixed references**:
   ```excel
   =SUM(A1, B2, C3:C10)  // Adds A1, B2, and the range C3:C10
   ```

---

### 🛠️ Related Functions

- [SUMIF function](sumif.md)

### **Tips**:

- Ignores **text**, **logical values (TRUE/FALSE)**, and **empty cells**.
- If a cell contains an **error**, the entire SUM function will return that error.
- Use **SUMIF** or **SUMIFS** for conditional summing.

## Use AutoSum to sum numbers

### **What is AutoSum in Excel?**  
**AutoSum** is a quick and easy way to add up numbers in Excel automatically. It uses the **SUM function** to calculate the total of a selected range of cells with just a click or a keyboard shortcut.  

---

### **How to Use AutoSum**  
#### **Method 1: Using the Ribbon**  
1. Select the cell **below** (for columns) or **beside** (for rows) the numbers you want to sum.  
2. Go to the **Home** tab → Click **AutoSum (Σ)** in the **Editing** group.  
   - Or go to the **Formulas** tab → Click **AutoSum (Σ)**.  
3. Excel will automatically detect the range and insert the `SUM` formula.  
4. Press **Enter** to confirm.  

#### **Method 2: Keyboard Shortcut**  
- Select the target cell and press **`Alt+Equal sign ( = )`** (Windows).  

---

### **Examples of AutoSum**  
1. **Sum a Column**  
   - If you have numbers in **A1:A10**, select **A11** and click **AutoSum (Σ)**.  
   - Excel will insert:  
     ```excel
     =SUM(A1:A10)
     ```  

2. **Sum a Row**  
   - If numbers are in **A1:E1**, select **F1** and press **`Alt + =`**.  
   - Excel will insert:  
     ```excel
     =SUM(A1:E1)
     ```  

3. **Sum Multiple Ranges**  
   - Select a cell where you want the total, click **AutoSum**, then adjust the range manually if needed.  

---

### **What Else Can AutoSum Do?**  
AutoSum can also insert other functions automatically, such as:  
- **Average (`AVERAGE`)**  
- **Count Numbers (`COUNT`)**  
- **Maximum (`MAX`)**  
- **Minimum (`MIN`)**  

To use these:  
1. Click the **drop-down arrow (▼)** next to the **AutoSum (Σ)** button.  
2. Select the desired function.  

---

### **AutoSum Tips**  
✅ **Detects adjacent data** by default (but you can manually adjust the range).  
❌ **Ignores text and empty cells** (only sums numbers).  
⚠ **If AutoSum selects the wrong range**, drag to correct it before pressing **Enter**.  

## **📺 Excel Tutorial in Urdu: Use of Sum function and AutoSum to sum numbers**  
**This video covers:**  
* ✔️  How to use the SUM function by typing it out \[[00:29](http://www.youtube.com/watch?v=o8aBs1Qr_8s&t=29)\]
* ✔️ How to use cell references in the SUM function \[[01:31](http://www.youtube.com/watch?v=o8aBs1Qr_8s&t=91)\]
* ✔️ How to use range operators with the SUM function \[[02:45](http://www.youtube.com/watch?v=o8aBs1Qr_8s&t=165)\]
* ✔️ How to use AutoSum \[[03:57](http://www.youtube.com/watch?v=o8aBs1Qr_8s&t=237)\]
* ✔️ How to use the shortcut key for AutoSum, which is Alt + Equals sign \[[04:30](http://www.youtube.com/watch?v=o8aBs1Qr_8s&t=270)\]
* How to copy the formula to multiple cells \[[04:50](http://www.youtube.com/watch?v=o8aBs1Qr_8s&t=290)\]

{% assign video_type = "video" %}
{% assign video_id = "o8aBs1Qr_8s" %}
{% include youtube-video.html video_type=video_type video_id=video_id %}

## **📺 Excel Tutorial in Urdu: Copy values quickly from the status bar**

{% assign video_type = "video" %}
{% assign video_id = "beDE-DM3e2k" %}
{% include youtube-video.html video_type=video_type video_id=video_id %}

## Tasks

### **Tasks 1: Calculating the Sum of values in Excel**

- Create a new Excel worksheet.
- In cells A1 to A10, enter the following numbers: 10, 20, 30, 40, 50, 60, 70, 80, 90, and 100.
- In cell A11, enter the following formula: `=SUM(A1:A10)`
- Press Enter.

The result, 550, should appear in cell A11.

### **Task 2:** Calculate the total marks for each students.

Sample Date:

| Student | Math | Science | History |
|---------|------|---------|---------|
| Alice   | 85   | 90      | 75      |
| Bob     | 70   | 88      | 80      |
| Carol   | 92   | 76      | 85      |
| David   | 78   | 82      | 70      |
| Emma    | 90   | 85      | 92      |


### **Task 3:** Use the SUM function to calculate the total sales in the following table:

| Month    | Sales |
| -------- | ----- |
| January  | 100   |
| February | 120   |
| March    | 150   |
| April    | 180   |
| May      | 210   |

**See also:**

- [Sum Function - Excel Exercises](https://excelexercises.com/practice.html?lesson=1)
- [SUM function - Microsoft Support](https://support.microsoft.com/en-us/office/sum-function-043e1c7d-7726-4e80-8f32-07b23e057f89)
- Use AutoSum to sum numbers - Microsoft Support [[Windows]](https://support.microsoft.com/en-us/office/use-autosum-to-sum-numbers-543941e7-e783-44ef-8317-7d1bb85fe706) [[Android]](https://support.microsoft.com/en-us/office/use-autosum-to-sum-numbers-543941e7-e783-44ef-8317-7d1bb85fe706#ID0EBBF=Android)