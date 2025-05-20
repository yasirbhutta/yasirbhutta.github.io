---
layout: page
title: "Python Pandas Module Guide – Functions, Examples & Usage"
description: Learn how to use the Pandas module in Python for data analysis. Explore functions, examples, and best practices for efficient data manipulation.
keywords: Python Pandas, Pandas module, Pandas tutorial, Python data analysis, Pandas DataFrame, Python data manipulation, Pandas functions, Python library, Pandas examples
author: Muhammad Yasir Bhutta
course: python
topic: pandas
toc: toc/python.html
prev: /python/docs/modules/numpy.html
next: /python/docs/modules/scipy.html
breadcrumb:
  - title: Home
    url: /
  - title: Python
    url: /python/
---

- [Download PDF](https://yasirbhutta.github.io/python/docs/modules/pandas.pdf)  
- To access the updated handouts, please click on the following link:
[https://yasirbhutta.github.io/python/docs/modules/pandas.html]([../yasirbhutta.github.io/index.md](https://yasirbhutta.github.io/python/docs/modules/pandas.html))

### 1. **Introduction to Pandas**
   - What is Pandas?
   - Installing Pandas (`pip install pandas`)
   - Importing Pandas (`import pandas as pd`)

### 2. **Data Structures in Pandas**
   - **Series**: A one-dimensional labeled array.
     - Creating a Series
     - Accessing elements in a Series
   - **DataFrame**: A two-dimensional labeled data structure (like a spreadsheet or SQL table).
     - Creating a DataFrame from:
       - Lists of lists
       - Dictionaries
       - CSV/Excel files

### 3. **Basic Operations with DataFrames**
   - Viewing data:
     - `head()`, `tail()`, `info()`, `describe()`
   - Selecting data:
     - Columns (`df['column']`)
     - Rows (`iloc`, `loc`)
   - Filtering rows based on conditions
   - Adding and deleting columns

### 4. **Data Cleaning**
   - Handling missing values:
     - `dropna()`
     - `fillna()`
   - Renaming columns
   - Changing data types (`astype()`)

### 5. **Data Manipulation**
   - Sorting data (`sort_values()`)
   - Grouping data (`groupby()`)
   - Aggregations (`mean()`, `sum()`, `count()`, etc.)
   - Merging and joining DataFrames (`merge()`, `concat()`)

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1602443888929206"
     crossorigin="anonymous"></script>
<ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-1602443888929206"
     data-ad-slot="6296238623"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

### 6. **Reading and Writing Data**
   - Reading from:
     - CSV (`read_csv()`)
     - Excel (`read_excel()`)
     - JSON (`read_json()`)
   - Writing to:
     - CSV (`to_csv()`)
     - Excel (`to_excel()`)

### 7. **Data Visualization with Pandas**
   - Basic plots with Pandas:
     - Line plot, bar plot, histogram, scatter plot (`df.plot()`)

### 8. **Useful Functions for Analysis**
   - `value_counts()`
   - `unique()`
   - `nunique()`
   - `pivot_table()`

### 9. **Practical Examples**
   - Analyzing real-world datasets
   - Cleaning messy data
   - Simple data analysis projects

## 1. 📌 **Introduction to Pandas**

### 1.1 **What is Pandas?**

  -   **Definition:** pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language. [1]
  
  - **Key Features**:  
    - Data alignment and missing data handling.  
    - Support for importing/exporting data from various file formats (CSV, Excel, SQL, etc.).  
    - Tools for reshaping, pivoting, and aggregating data.  
    - Time series functionality.

For more details on Data alignment, see [Data Alignment in Pandas](data-alignment-in-pandas.md).

### 1.2 **Why Use Pandas?**

   - **Benefits**:
     - Simplifies data analysis tasks.
     - Efficient handling of large datasets.
     - Allows easy data cleaning and preprocessing.
     - Combines flexibility with powerful tools for slicing, filtering, and transforming data.

### 1.3 **Installing Pandas**
   - Install Pandas using `pip`:
     ```bash
     pip install pandas
     ```
   - **Verifying Installation**:
     ```python
     import pandas as pd
     print(pd.__version__)
     ```

### 1.4 **Importing Pandas**
   - Import the Pandas library with a conventional alias:
     ```python
     import pandas as pd
     ```
   - Why `pd`?  
     It’s a commonly used alias to shorten the code and improve readability.

### 2. Basic data structures in pandas

Pandas provides two types of classes for handling data:

   - **Series**:
     - a one-dimensional labeled array holding data of any type such as integers, strings, Python objects etc. similar to a column in a spreadsheet. [2]
   - **DataFrame**:
     - a two-dimensional data structure that holds data like a two-dimension array or a table with rows and columns. [2]

### Creating a Simple Series

Creating a Series by passing a list of values, letting pandas create a default RangeIndex. [2]

```python
import pandas as pd
import numpy as np

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
```

`np.nan` stands for "Not a Number", representing a missing or undefined numerical value (similar to NaN in other contexts).

**Indexing**: Both Series and DataFrames have index labels to identify data.


### **Creating a Simple DataFrame**
   ```python
   import pandas as pd

   # Creating a DataFrame from a dictionary
   data = {
       'Name': ['Alice', 'Bob', 'Charlie'],
       'Age': [25, 30, 35],
       'City': ['New York', 'Los Angeles', 'Chicago']
   }

   df = pd.DataFrame(data)
   print(df)
   ```

   **Output**:  
   ```
        Name  Age         City
   0    Alice   25     New York
   1      Bob   30  Los Angeles
   2  Charlie   35      Chicago
   ```

### Example: [How to Create a Data Frame with Fruits and Colors Example](https://www.youtube.com/watch?v=aR8xiyyLoRk&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=12)

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1602443888929206"
     crossorigin="anonymous"></script>
<ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-1602443888929206"
     data-ad-slot="6296238623"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

### 1. Loading CSV Datasets

You can load CSV files from your local system or directly from a URL into Pandas using pd.read_csv().

#### Example Titanic Dataset (from a URL)

```python
import pandas as pd

# Loading the Titanic dataset from a URL
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic = pd.read_csv(url)
print(titanic.head())
```

for more deta sets, see [Datasets for use in examples](/datasets/)

#### Example: Local CSV File

# Loading a local CSV file

```python
titanic = pd.read_csv("path_to_your_file/titanic.csv")
print(titanic.head())
```

### 2. Loading Excel Files

Pandas can easily read Excel files using pd.read_excel().

#### Example: Tasks Trackers Dataset [download](https://wpreportbuilder.com/examples/task-tracker-generate-excel-xlsx/)

# Loading an Excel file

```python
import pandas as pd

tasks = pd.read_excel("tasks_ds.xlsx")
print(tasks.head())
```
for more details, see [Loading and Handling Datasets in Pandas](loading-handling-datasets-pandas.md)

### 3. **Basic Operations with DataFrames**

#### 3.1 **Viewing Data**

When working with DataFrames in libraries like **pandas**, it's essential to quickly inspect your data to understand its structure. Below are some key functions to view data:

- **`head(n)`**: Displays the first *n* rows (default is 5).
  
```python
import pandas as pd
df = pd.read_csv('titanic.csv')
print(df.head())
```

- **`tail(n)`**: Displays the last *n* rows (default is 5).

  ```python
  df.tail()
  ```

- **`info()`**: Provides a concise summary of the DataFrame, including column names, non-null counts, and data types.

  ```python
  df.info()
  ```

- **`describe()`**: Generates summary statistics for numerical columns, such as mean, standard deviation, and quartiles.

  ```python
  df.describe()
  ```

#### 3.2 **Selecting Data**

Selecting specific parts of a DataFrame is a common operation. You can select **columns** and **rows** using different methods:

- **Selecting Columns**

  - Using the column name in square brackets:

    ```python
    df['column_name']
    ```

  - Selecting multiple columns by providing a list of column names:

    ```python
    df[['col1', 'col2']]
    ```

**Loading the Titanic dataset** (assuming it's available as a CSV file):

   ```python
   import pandas as pd

   # Load the Titanic dataset
   df = pd.read_csv('titanic.csv')
   ```

##### Example: **Selecting a Single Column**

   - For example, to select the **"Age"** column:

     ```python
     df['Age']
     ```

   - This returns a **Series** representing the "Age" column.

##### Example: **Selecting Multiple Columns**

   - To select **"Name"**, **"Age"**, and **"Survived"** columns:

     ```python
     df[['Name', 'Age', 'Survived']]
     ```

   - This returns a **DataFrame** with the specified columns.

- **Selecting Rows**

  - Using **`iloc`** (integer-location based): Select rows by their index position.

    ```python
    df.iloc[0]       # First row
    df.iloc[1:4]     # Rows 2 to 4
    ```

  - Using **`loc`** (label-based): Select rows by their index labels.

    ```python
    df.loc[0]                # Row with index 0
    df.loc[0:3]              # Rows from index 0 to 3 (inclusive)
    df.loc[df['col'] > 10]   # Rows where 'col' > 10
    ```
  
### **Selecting Rows with the Titanic Dataset**

1. **Loading the Titanic Dataset**

Let's load the dataset and inspect its structure:

```python
import pandas as pd

# Load the Titanic dataset (assuming it's available as 'titanic.csv')
df = pd.read_csv('titanic.csv')

# Display the first few rows to understand the data
print(df.head())
```

This might display something like:

| PassengerId | Name                          | Age  | Survived | Pclass |
|-------------|-------------------------------|------|----------|--------|
| 1           | Braund, Mr. Owen Harris      | 22.0 | 0        | 3      |
| 2           | Cumings, Mrs. John Bradley   | 38.0 | 1        | 1      |
| 3           | Heikkinen, Miss. Laina       | 26.0 | 1        | 3      |
| 4           | Futrelle, Mrs. Jacques Heath | 35.0 | 1        | 1      |
| 5           | Allen, Mr. William Henry     | 35.0 | 0        | 3      |

---

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1602443888929206"
     crossorigin="anonymous"></script>
<ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-1602443888929206"
     data-ad-slot="6296238623"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

### **Selecting Rows Using `iloc` (Integer-location Based)**

- **Select the First Row**:

  ```python
  first_row = df.iloc[0]
  print(first_row)
  ```

  **Output**:

  ```
  PassengerId                        1
  Name          Braund, Mr. Owen Harris
  Age                               22.0
  Survived                             0
  Pclass                               3
  Name: 0, dtype: object
  ```

- **Select Rows 2 to 4** (indices 1 to 3):

  ```python
  rows_2_to_4 = df.iloc[1:4]
  print(rows_2_to_4)
  ```

  **Output**:

  ```
     PassengerId                            Name   Age  Survived  Pclass
  1            2      Cumings, Mrs. John Bradley  38.0         1       1
  2            3          Heikkinen, Miss. Laina  26.0         1       3
  3            4  Futrelle, Mrs. Jacques Heath    35.0         1       1
  ```

---

### **Selecting Rows Using `loc` (Label-based)**

- **Select the Row with Index 0**:

  ```python
  row_index_0 = df.loc[0]
  print(row_index_0)
  ```

  **Output**:

  ```
  PassengerId                        1
  Name          Braund, Mr. Owen Harris
  Age                               22.0
  Survived                             0
  Pclass                               3
  Name: 0, dtype: object
  ```

- **Select Rows with Index 0 to 3** (inclusive):

  ```python
  rows_0_to_3 = df.loc[0:3]
  print(rows_0_to_3)
  ```

  **Output**:

  ```
     PassengerId                            Name   Age  Survived  Pclass
  0            1       Braund, Mr. Owen Harris    22.0         0       3
  1            2     Cumings, Mrs. John Bradley   38.0         1       1
  2            3         Heikkinen, Miss. Laina   26.0         1       3
  3            4  Futrelle, Mrs. Jacques Heath    35.0         1       1
  ```

- **Select Rows with index 0 to 3 and columns name and age**

```python
df_name_age = df.loc[0:3, ["Name", "Age"]]
# The above line will raise an error because the loc method is not used correctly.
print(df_name_age)
```

**Output:**

```
Name   Age
0                            Braund, Mr. Owen Harris  22.0
1  Cumings, Mrs. John Bradley (Florence Briggs Th...  38.0
2                             Heikkinen, Miss. Laina  26.0
3       Futrelle, Mrs. Jacques Heath (Lily May Peel)  35.0
```

- **Select Rows Where `Age` > 30**:

  ```python
  rows_age_above_30 = df.loc[df['Age'] > 30]
  print(rows_age_above_30.head())
  ```

  **Output**:

  ```
     PassengerId                            Name   Age  Survived  Pclass
  1            2     Cumings, Mrs. John Bradley   38.0         1       1
  3            4  Futrelle, Mrs. Jacques Heath    35.0         1       1
  5            6        Moran, Mr. James          32.0         0       3
  6            7        McCarthy, Mr. Timothy J   54.0         0       3
  9           10  Nasser, Mrs. Nicholas           14.0         1       2
  ```

for more details, see [Difference Between Pandas loc vs iloc – Key Comparisons](difference-between-iloc-loc.md)

#### 3.3 **Filtering Rows Based on Conditions**

Filtering rows allows you to extract data that meets certain criteria. Conditions can be combined using logical operators:

- **Filter based on a single condition**:

  ```python
  df[df['column_name'] > 50]
  ```

- **Filter based on multiple conditions**:

  - Using **AND (`&`)**:

    ```python
    df[(df['col1'] > 50) & (df['col2'] == 'Value')]
    ```

  - Using **OR (`|`)**:

    ```python
    df[(df['col1'] > 50) | (df['col2'] == 'Value')]
    ```

- **Filter based on text matching**:

  ```python
  df[df['col'].str.contains('keyword')]
  ```

#### 3.4 **Adding and Deleting Columns**

- **Adding a New Column**

  You can create new columns by assigning values or calculations based on existing columns:

  ```python
  df['new_col'] = df['col1'] + df['col2']
  ```

- **Deleting a Column**

  Use the `drop` method to remove a column. Set `axis=1` to specify columns:

  ```python
  df.drop('col_to_delete', axis=1, inplace=True)
  ```

  Alternatively, use the `del` statement:

  ```python
  del df['col_to_delete']
  ```

  

### 1.9 **Key Pandas Terminology**
   - **Index**: The labels for rows in a Series or DataFrame.
   - **Column**: A named set of data within a DataFrame.
   - **Row**: An individual record within a DataFrame.


## Key Terms

## True/False (Mark T for True and F for False)

**Answer Key (True/False):**

## Multiple Choice (Select the best answer)

1. **Which function would you use to determine the type of a variable in Python?**
   - A) id()
   - B) type()
   - C) str()
   - D) isinstance()
  
**Watch this video for the answer:**

**Answer key (Mutiple Choice):**

## Fill in the Blanks

**Answer Key (Fill in the Blanks):**

## Exercises

1. Skill Level Categories
Define clear categories based on skill levels, such as:

Beginner: Basic concepts and syntax.
Intermediate: More complex problems involving data structures and algorithms.
Advanced: Challenging problems that require in-depth understanding and optimization.

## References and Bibliography

[1]: https://pandas.pydata.org/ "Pandas, “Python Data Analysis Library,” Pydata.org, 2018."
[2]: https://pandas.pydata.org/docs/user_guide/index.html "Pandas, “User Guide — pandas 1.0.1 documentation,” Pydata.org, 2014."

