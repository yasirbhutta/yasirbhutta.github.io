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
