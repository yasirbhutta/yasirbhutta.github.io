---
layout: page
title: "loc vs iloc in Pandas: Key Differences and When to Use Each"
description: Learn the key differences between loc and iloc in Pandas. Understand when to use label-based (loc) vs integer-based (iloc) indexing for efficient data manipulation.
keywords: loc vs iloc, Pandas loc and iloc difference, label-based indexing Pandas, integer-based indexing Pandas, Pandas DataFrame indexing, Python Pandas tutorial, data selection in Pandas, iloc vs loc examples
author: Muhammad Yasir Bhutta
course: python
topic: pandas
toc: toc/python.html
prev: /python/docs/pandas/
next: /python/
breadcrumb:
  - title: Home
    url: /
  - title: Python
    url: /python/
  - title: Pandas
    url: /python/docs/pandas/
---



## What is iloc in Pandas?

**`iloc` (Integer-Based Indexing)** selects rows and columns using **integer positions** (like Python list indexing). It is **position-based** and ignores the actual index labels.  

### **Key Features:**  
- Uses zero-based indexing (`0` for the first row).  
- Slicing follows Python’s `[start:end]` (exclusive of `end`).  
- Ideal for positional data access.  

### **Example:**  
```python
df.iloc[0]      # First row (position 0)  
df.iloc[1:4]    # Rows 2, 3, and 4 (positions 1 to 3, end-exclusive)  
df.iloc[:, 2]   # All rows, third column (position 2)  
```

---

## What is loc in Pandas?

**`loc` (Label-Based Indexing)** selects rows and columns using **explicit labels** (index names or boolean conditions). It is **label-based** and includes the end of slices.  

### **Key Features:**  
- Uses actual index labels (not positions).  
- Slicing is **inclusive** (`df.loc[0:3]` includes index `3`).  
- Supports boolean masking for filtering.  

### **Example:**  
```python
df.loc[0]                 # Row with index label `0`  
df.loc[0:3]               # Rows from label `0` to `3` (inclusive)  
df.loc[df['col'] > 10]    # Filter rows where 'col' > 10  
df.loc[:, 'column_name']  # All rows, specific column by name  
```
---

## Difference Between Pandas `loc` vs `iloc` – Key Comparisons*  

Pandas provides two primary methods for data selection: **`loc`** and **`iloc`**. While both are used for indexing, they work differently.  

| Feature          | **`loc`** | **`iloc`** |
|-----------------|----------|----------|
| **Selection Type** | Label-based | Integer position-based |
| **Syntax** | `df.loc[row_label, column_label]` | `df.iloc[row_idx, column_idx]` |
| **Includes Last Index?** | Yes (inclusive) | No (exclusive, like Python slicing) |
| **Works With** | Row/column names (labels) | Row/column integer positions |
| **Supports Boolean Masks?** | Yes | Yes |
| **Example** | `df.loc[2:5, 'Name']` | `df.iloc[2:5, 0]` |

## **When to Use `loc` vs `iloc`?**  
✔ **Use `loc`** when selecting data by **labels** (e.g., column names, index labels).  
✔ **Use `iloc`** when selecting data by **numeric positions** (like list/array indexing).  

### **Example Code**  
```python
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40]}
df = pd.DataFrame(data, index=['a', 'b', 'c', 'd'])

# Using loc (label-based)
print(df.loc['a':'c', 'Name'])  # Includes 'c'

# Using iloc (position-based)
print(df.iloc[0:3, 0])  # Excludes index 3 (like Python slicing)
```

### **Key Takeaway**  
- **`loc`** is **label-based** (inclusive of the end range).  
- **`iloc`** is **position-based** (exclusive, like Python slicing).  

