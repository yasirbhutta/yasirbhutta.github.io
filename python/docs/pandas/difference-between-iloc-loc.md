# **Difference Between Pandas `loc` vs `iloc` – Key Comparisons**  

Pandas provides two primary methods for data selection: **`loc`** and **`iloc`**. While both are used for indexing, they work differently.  

| Feature          | **`loc`** | **`iloc`** |
|-----------------|----------|----------|
| **Selection Type** | Label-based | Integer position-based |
| **Syntax** | `df.loc[row_label, column_label]` | `df.iloc[row_idx, column_idx]` |
| **Includes Last Index?** | Yes (inclusive) | No (exclusive, like Python slicing) |
| **Works With** | Row/column names (labels) | Row/column integer positions |
| **Supports Boolean Masks?** | Yes | Yes |
| **Example** | `df.loc[2:5, 'Name']` | `df.iloc[2:5, 0]` |

### **When to Use `loc` vs `iloc`?**  
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

