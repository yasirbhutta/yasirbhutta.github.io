---
layout: page
title: "How to Use the SUM Function and AutoSum in Excel – Complete Guide"
description: Learn how to use the SUM function and AutoSum in Microsoft Excel to quickly add values across cells, columns, or rows. Includes syntax, examples, and tips for efficient usage.
keywords: Excel SUM function, how to use SUM in Excel, Excel functions guide, Excel SUM formula, Excel add cells, Excel basics, Excel tutorials, Microsoft Excel functions, SUM formula examples
author: Muhammad Yasir Bhutta
course: ms-excel
topic: functions
toc: toc/python.html
prev: /python/docs/pandas/
next: /ms-excel/docs/functions/sumif.html
breadcrumb:
  - title: Home
    url: /
  - title: Python
    url: /python/
  - title: Pandas
    url: /python/docs/pandas/
---

### **Appendix B: 📌 Data Alignment in Pandas**

**Data alignment** refers to how Pandas handles operations between data structures (such as `Series` or `DataFrames`) with differing indexes. When performing operations like addition, subtraction, or merging, Pandas automatically aligns the data by their index labels to ensure that operations happen between corresponding elements.

This feature helps simplify data operations and avoid errors, especially when dealing with real-world datasets that may not always be perfectly aligned.

---

### 🔹 **Example of Data Alignment with Series**

When performing operations between two `Series` with different indexes, Pandas aligns the data by the index labels and fills any missing values with `NaN` (Not a Number).

```python
import pandas as pd

# First Series
s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])

# Second Series with different index
s2 = pd.Series([4, 5, 6], index=['b', 'c', 'd'])

# Adding the two Series
result = s1 + s2

print(result)
```

**Output**:
```
a    NaN
b    6.0
c    8.0
d    NaN
dtype: float64
```

#### **Explanation**:
- The elements with matching indexes (`b` and `c`) are added together.
- For indexes `a` and `d`, there are no corresponding values in the other Series, so the result is `NaN`.

---

### 🔹 **Data Alignment with DataFrames**

When performing operations on `DataFrames`, Pandas aligns both rows and columns based on their respective indexes.

```python
# First DataFrame
df1 = pd.DataFrame({
    'A': [1, 2],
    'B': [3, 4]
}, index=['row1', 'row2'])

# Second DataFrame with different columns and rows
df2 = pd.DataFrame({
    'B': [5, 6],
    'C': [7, 8]
}, index=['row2', 'row3'])

# Adding the two DataFrames
result = df1 + df2

print(result)
```

**Output**:
```
        A     B    C
row1  NaN   NaN  NaN
row2  NaN   9.0  NaN
row3  NaN   NaN  NaN
```

#### **Explanation**:
- The addition is performed where both rows and columns match (`row2` and `B`).
- Missing rows or columns result in `NaN`.

---

### 🔹 **Handling Missing Data During Alignment**

You can handle missing data resulting from alignment by using methods like:
- **`fillna()`**: Replace `NaN` with a specific value.
- **`add()`, `sub()`, etc. with `fill_value`**: Provide a default value for missing entries.

#### Example using `fill_value`:
```python
result = s1.add(s2, fill_value=0)
print(result)
```

**Output**:
```
a    1.0
b    6.0
c    8.0
d    6.0
dtype: float64
```

---

### ✅ **Summary**

- **Data Alignment** ensures operations occur between matching indexes.
- Non-matching indexes result in `NaN` unless specified otherwise.
- Pandas handles alignment automatically, making data manipulation intuitive and error-free.