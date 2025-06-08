---
layout: page
title: "CSV Handling in Python"
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

Handling CSV (Comma-Separated Values) files is a common task in Python, especially for data analysis, automation, and working with spreadsheets. This guide covers **reading, writing, and manipulating CSV files** with beginner-friendly examples and real-world use cases.

---

## Example Processing CSV Data (Simple Version)

```python
# Read CSV and calculate average
def calculate_average_scores():
    with open('scores.csv', 'r') as file:
        lines = file.readlines()
    
    total = 0
    count = 0
    
    for line in lines:
        name, score = line.strip().split(',')
        total += int(score)
        count += 1
    
    average = total / count
    print(f"Average score: {average:.2f}")

# Sample scores.csv:
# Alice,92
# Bob,85
# Charlie,78
```

## **2. Reading a CSV File**

### **Using `csv.reader()` (Basic Method)**
```python
import csv

with open('employees.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)  # Each row is a list
```
**Output Example:**
```
['Name', 'Age', 'Department']
['Alice', '28', 'HR']
['Bob', '32', 'Engineering']
['Charlie', '45', 'Finance']
```

**Real-Life Use Case:**  
- Reading an exported list of employees from an HR system.

---

### **Using `csv.DictReader()` (Easier for Column Access)**
```python
import csv

with open('employees.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row['Name'], row['Department'])  # Access columns by name
```
**Output Example:**
```
Alice HR
Bob Engineering
Charlie Finance
```

**Real-Life Use Case:**  
- Extracting specific columns (e.g., only names and emails from a contact list).

---

## **2. Writing to a CSV File**
### **Using `csv.writer()` (Basic Method)**
```python
import csv

data = [
    ["Product", "Price", "Stock"],
    ["Laptop", "999", "50"],
    ["Phone", "699", "100"],
    ["Tablet", "299", "30"]
]

with open('inventory.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)
```

**Real-Life Use Case:**  
- Generating an inventory report for an e-commerce store.

---

### **Using `csv.DictWriter()` (Better for Structured Data)**
```python
import csv

employees = [
    {"Name": "Alice", "Age": 28, "Department": "HR"},
    {"Name": "Bob", "Age": 32, "Department": "Engineering"},
    {"Name": "Charlie", "Age": 45, "Department": "Finance"}
]

with open('employees_new.csv', 'w', newline='') as file:
    fieldnames = ["Name", "Age", "Department"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()  # Writes column names
    writer.writerows(employees)
```

**Real-Life Use Case:**  
- Exporting structured data (e.g., employee records) to a CSV file.

---

## **3. Modifying CSV Data (Real-Life Example)**
### **Example: Filtering Data (Only Keep Engineering Dept.)**
```python
import csv

# Read CSV and filter
with open('employees.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    engineering_employees = [row for row in csv_reader if row['Department'] == 'Engineering']

# Write filtered data to a new CSV
with open('engineering_employees.csv', 'w', newline='') as file:
    fieldnames = ["Name", "Age", "Department"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(engineering_employees)
```

**Real-Life Use Case:**  
- Extracting only relevant rows (e.g., employees in a specific department).

---

## **4. Working with CSV & Pandas (For Data Analysis)**
Pandas is a powerful library for handling CSV files efficiently.

### **Install Pandas (if not installed)**
```bash
pip install pandas
```

### **Reading CSV with Pandas**
```python
import pandas as pd

df = pd.read_csv('employees.csv')
print(df.head())  # Shows first 5 rows
```

### **Writing CSV with Pandas**
```python
df.to_csv('updated_employees.csv', index=False)  # index=False avoids extra column
```

**Real-Life Use Case:**  
- Cleaning and analyzing large datasets (e.g., sales records, survey responses).

---

## **5. Common CSV Tasks (Cheat Sheet)**
| **Task** | **Code Example** |
|----------|------------------|
| Read CSV | `csv.reader(file)` or `pd.read_csv()` |
| Write CSV | `csv.writer(file)` or `df.to_csv()` |
| Skip Header | `next(csv_reader)` (before loop) |
| Read as Dictionary | `csv.DictReader(file)` |
| Write with Headers | `csv.DictWriter(file, fieldnames)` |
| Append to CSV | Open in `'a'` (append) mode |

---

## **Real-World CSV Use Cases**
1. **Importing/Exporting Data** (Excel, Google Sheets)
2. **Data Cleaning** (Removing duplicates, fixing errors)
3. **Automating Reports** (Sales, inventory, logs)
4. **Machine Learning Datasets** (Storing training data)
5. **Web Scraping Results** (Saving scraped data to CSV)

---

## **Summary**
- Use `csv.reader()` and `csv.writer()` for basic CSV handling.
- Use `csv.DictReader()` and `csv.DictWriter()` for column-based access.
- Use **Pandas** (`pd.read_csv()`, `df.to_csv()`) for advanced data manipulation.
- **Real-world applications** include HR records, inventory, sales data, and more.


