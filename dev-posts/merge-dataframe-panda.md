---
layout: page
title: Merging DataFrames in Pandas: A Beginner's Guide
description: Pandas provides several ways to combine DataFrames, with `merge()` being one of the most powerful and commonly used methods. Here's a comprehensive gu...
keywords: print, data, com, merge, csv
---
# Merging DataFrames in Pandas: A Beginner's Guide

Pandas provides several ways to combine DataFrames, with `merge()` being one of the most powerful and commonly used methods. Here's a comprehensive guide with syntax and examples for beginners.

## Basic Syntax

```python
pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None)
```

### Key Parameters:
- `left`: The left DataFrame
- `right`: The right DataFrame
- `how`: Type of merge ('inner', 'outer', 'left', 'right')
- `on`: Column names to join on (must exist in both DataFrames)
- `left_on`/`right_on`: Columns to join on when they have different names

## Example 1: Basic Inner Join

```python
import pandas as pd

# Create two sample DataFrames
df1 = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['Alice', 'Bob', 'Charlie', 'David']
})

df2 = pd.DataFrame({
    'id': [1, 2, 4, 5],
    'age': [25, 30, 40, 35]
})

# Merge on 'id' column
result = pd.merge(df1, df2, on='id')
print(result)
```

**Output:**
```
   id     name  age
0   1    Alice   25
1   2      Bob   30
2   4    David   40
```

## Example 2: Different Join Types

```python
# Left join (keeps all rows from left DataFrame)
left_join = pd.merge(df1, df2, on='id', how='left')
print("Left join:\n", left_join)

# Right join (keeps all rows from right DataFrame)
right_join = pd.merge(df1, df2, on='id', how='right')
print("\nRight join:\n", right_join)

# Outer join (keeps all rows from both DataFrames)
outer_join = pd.merge(df1, df2, on='id', how='outer')
print("\nOuter join:\n", outer_join)
```

**Output:**
```
Left join:
    id     name   age
0   1    Alice  25.0
1   2      Bob  30.0
2   3  Charlie   NaN
3   4    David  40.0

Right join:
    id    name  age
0   1   Alice   25
1   2     Bob   30
2   4   David   40
3   5     NaN   35

Outer join:
    id     name   age
0   1    Alice  25.0
1   2      Bob  30.0
2   3  Charlie   NaN
3   4    David  40.0
4   5      NaN  35.0
```

## Example 3: Merging on Different Column Names

```python
# Create DataFrames with different column names
df3 = pd.DataFrame({
    'emp_id': [1, 2, 3, 4],
    'position': ['Manager', 'Developer', 'Analyst', 'Designer']
})

# Merge df1 and df3 where 'id' matches 'emp_id'
result = pd.merge(df1, df3, left_on='id', right_on='emp_id')
print(result)
```

**Output:**
```
   id     name  emp_id   position
0   1    Alice       1    Manager
1   2      Bob       2  Developer
2   3  Charlie       3    Analyst
3   4    David       4   Designer
```

## Example 4: Merging on Multiple Columns

```python
# Create DataFrames with multiple key columns
df4 = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'year': [2020, 2020, 2021, 2021],
    'sales': [100, 200, 300, 400]
})

df5 = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'year': [2020, 2020, 2020, 2021],
    'expenses': [50, 150, 250, 350]
})

# Merge on both 'id' and 'year'
result = pd.merge(df4, df5, on=['id', 'year'])
print(result)
```

**Output:**
```
   id  year  sales  expenses
0   1  2020    100        50
1   2  2020    200       150
2   4  2021    400       350
```

## Example 5: Indicator Column

```python
# Add indicator to show source of each row
result = pd.merge(df1, df2, on='id', how='outer', indicator=True)
print(result)
```

**Output:**
```
   id     name   age      _merge
0   1    Alice  25.0        both
1   2      Bob  30.0        both
2   3  Charlie   NaN   left_only
3   4    David  40.0        both
4   5      NaN  35.0  right_only
```

These examples cover the most common merging scenarios in Pandas. Remember that `merge()` is different from `concat()` (which stacks DataFrames vertically or horizontally) and `join()` (which is similar to merge but works on indices).

# Real-World Example: Merging Customer and Order Data

Let's walk through a practical example where we:
1. Read data from CSV files (simulating real datasets)
2. Clean and prepare the data
3. Merge the datasets to gain business insights

## Scenario
We have two datasets:
- `customers.csv`: Customer demographic information
- `orders.csv`: Order transaction records

We want to combine these to analyze customer purchasing behavior.

### Step 1: Read the Data

```python
import pandas as pd

# Read customer data
customers = pd.read_csv('customers.csv')
print("Customers data:")
print(customers.head())

# Read order data
orders = pd.read_csv('orders.csv')
print("\nOrders data:")
print(orders.head())
```

**Sample Data (if you want to create these files):**

`customers.csv`:
```
customer_id,first_name,last_name,email,join_date
1001,John,Smith,john.smith@email.com,2020-01-15
1002,Emily,Davis,emily.davis@email.com,2020-03-22
1003,Michael,Brown,michael.brown@email.com,2020-05-10
1004,Sarah,Wilson,sarah.wilson@email.com,2021-01-05
1005,David,Lee,david.lee@email.com,2021-02-18
```

`orders.csv`:
```
order_id,customer_id,order_date,product_id,quantity,total_amount
5001,1001,2023-01-10,P100,2,199.98
5002,1002,2023-01-12,P105,1,89.99
5003,1001,2023-01-15,P102,3,449.97
5004,1003,2023-01-18,P101,1,129.99
5005,1005,2023-01-20,P104,2,159.98
5006,1002,2023-01-25,P103,1,59.99
5007,1004,2023-02-05,P100,1,99.99
```

### Step 2: Basic Data Exploration

```python
print("\nCustomers info:")
print(customers.info())

print("\nOrders info:")
print(orders.info())

print("\nMissing values in customers:")
print(customers.isnull().sum())

print("\nMissing values in orders:")
print(orders.isnull().sum())
```

### Step 3: Merge the Data

```python
# Merge customers with their orders (left join to keep all customers)
customer_orders = pd.merge(
    customers, 
    orders, 
    on='customer_id', 
    how='left'
)

print("\nMerged data (first 10 rows):")
print(customer_orders.head(10))
```

**Output:**
```
   customer_id first_name last_name                  email   join_date  order_id  order_date product_id  quantity  total_amount
0         1001       John     Smith   john.smith@email.com  2020-01-15    5001.0  2023-01-10       P100       2.0        199.98
1         1001       John     Smith   john.smith@email.com  2020-01-15    5003.0  2023-01-15       P102       3.0        449.97
2         1002      Emily     Davis  emily.davis@email.com  2020-03-22    5002.0  2023-01-12       P105       1.0         89.99
3         1002      Emily     Davis  emily.davis@email.com  2020-03-22    5006.0  2023-01-25       P103       1.0         59.99
4         1003    Michael     Brown  michael.brown@email.com  2020-05-10    5004.0  2023-01-18       P101       1.0        129.99
5         1004      Sarah    Wilson  sarah.wilson@email.com  2021-01-05    5007.0  2023-02-05       P100       1.0         99.99
6         1005      David       Lee     david.lee@email.com  2021-02-18    5005.0  2023-01-20       P104       2.0        159.98
```

### Step 4: Advanced Analysis with Merged Data

```python
# Calculate total spending per customer
customer_spending = customer_orders.groupby(['customer_id', 'first_name', 'last_name'])['total_amount'].sum().reset_index()
customer_spending.columns = ['customer_id', 'first_name', 'last_name', 'total_spending']

print("\nCustomer spending:")
print(customer_spending)

# Find customers with no orders
customers_with_no_orders = customer_orders[customer_orders['order_id'].isna()]
print("\nCustomers with no orders:")
print(customers_with_no_orders[['customer_id', 'first_name', 'last_name']])
```

### Step 5: Saving Merged Results

```python
# Save merged data to a new CSV
customer_orders.to_csv('customer_orders_merged.csv', index=False)
print("\nMerged data saved to 'customer_orders_merged.csv'")

# Save customer spending report
customer_spending.to_csv('customer_spending_report.csv', index=False)
print("Customer spending report saved to 'customer_spending_report.csv'")
```

## Real-World Considerations

1. **Data Quality**: Always check for missing values and duplicates before merging
2. **Join Types**: Choose the appropriate join type based on your analysis needs
   - Use `inner` when you only want matching records
   - Use `left` when you want to keep all customers (even without orders)
   - Use `outer` when you want to keep all records from both tables

3. **Performance**: For large datasets, consider:
   ```python
   # More memory-efficient merge
   pd.merge(customers, orders, on='customer_id', how='left', copy=False)
   ```

4. **Alternative Syntax**: You can also merge using DataFrame methods:
   ```python
   # Equivalent to pd.merge(customers, orders)
   customers.merge(orders, on='customer_id')
   ```

This example demonstrates a common business use case where merging datasets provides valuable insights that wouldn't be possible by looking at the datasets separately.

# Real-World Example: Merging Employee and Department Data

Let's explore another practical scenario where we:
1. Work with HR datasets (employees and departments)
2. Handle common data issues like missing values
3. Perform different types of merges for various analyses

## Scenario
We have two datasets from a company's HR system:
- `employees.csv`: Employee personal and job information
- `departments.csv`: Department details and locations

We want to combine these to analyze workforce distribution and department metrics.

### Step 1: Read the Data

```python
import pandas as pd

# Read employee data
employees = pd.read_csv('employees.csv')
print("Employee data (first 5 rows):")
print(employees.head())

# Read department data
departments = pd.read_csv('departments.csv')
print("\nDepartment data:")
print(departments.head())
```

**Sample Data (create these CSV files to follow along):**

`employees.csv`:
```
employee_id,first_name,last_name,email,phone,hire_date,job_title,salary,department_id,manager_id
101,John,Smith,john.smith@company.com,555-1001,2018-06-15,Software Engineer,85000,3,201
102,Emily,Davis,emily.davis@company.com,555-1002,2019-03-22,Marketing Specialist,72000,2,202
103,Michael,Brown,michael.brown@company.com,555-1003,2020-05-10,Sales Associate,68000,1,203
104,Sarah,Wilson,sarah.wilson@company.com,555-1004,2021-01-05,HR Coordinator,65000,4,204
105,David,Lee,david.lee@company.com,555-1005,2021-02-18,Data Analyst,78000,3,201
106,Jennifer,Clark,jennifer.clark@company.com,555-1006,2022-07-30,Accountant,70000,5,205
107,Robert,Johnson,robert.johnson@company.com,555-1007,2022-11-15,Sales Associate,65000,1,203
108,Lisa,Williams,lisa.williams@company.com,555-1008,2023-01-10,Software Engineer,90000,3,201
```

`departments.csv`:
```
department_id,department_name,location,head_count_budget
1,Sales,New York,15
2,Marketing,Chicago,10
3,Engineering,San Francisco,25
4,Human Resources,Boston,8
5,Finance,New York,12
6,Operations,Chicago,20
```

### Step 2: Data Exploration and Cleaning

```python
# Check for missing values
print("\nMissing values in employees:")
print(employees.isnull().sum())

print("\nMissing values in departments:")
print(departments.isnull().sum())

# Convert hire_date to datetime
employees['hire_date'] = pd.to_datetime(employees['hire_date'])

# Add a tenure column (years with company)
employees['tenure'] = (pd.to_datetime('today') - employees['hire_date']).dt.days / 365
employees['tenure'] = employees['tenure'].round(1)

print("\nEmployees with tenure calculated:")
print(employees[['employee_id', 'first_name', 'last_name', 'tenure']].head())
```

### Step 3: Basic Merge (Inner Join)

```python
# Merge employees with their department info
employee_dept = pd.merge(
    employees,
    departments,
    on='department_id',
    how='inner'  # Default, keeps only matches
)

print("\nEmployees with department info (first 5 rows):")
print(employee_dept.head())
```

**Output:**
```
   employee_id first_name last_name                  email     phone hire_date          job_title  salary  department_id  manager_id  tenure department_name      location  head_count_budget
0          101       John     Smith   john.smith@company.com  555-1001 2018-06-15  Software Engineer   85000              3         201     5.3      Engineering  San Francisco                 25
1          105      David       Lee    david.lee@company.com  555-1005 2021-02-18       Data Analyst   78000              3         201     2.3      Engineering  San Francisco                 25
2          108       Lisa  Williams  lisa.williams@company.com  555-1008 2023-01-10  Software Engineer   90000              3         201     0.4      Engineering  San Francisco                 25
3          102      Emily     Davis  emily.davis@company.com  555-1002 2019-03-22  Marketing Specialist   72000              2         202     4.1        Marketing       Chicago                 10
4          103    Michael     Brown  michael.brown@company.com  555-1003 2020-05-10      Sales Associate   68000              1         203     2.9           Sales     New York                 15
```

### Step 4: Left Join (Keep All Employees)

```python
# Left join to keep all employees (even if department info is missing)
employee_dept_left = pd.merge(
    employees,
    departments,
    on='department_id',
    how='left'
)

print("\nAll employees with department info (left join):")
print(employee_dept_left[['employee_id', 'first_name', 'department_name']])
```

### Step 5: Right Join (Keep All Departments)

```python
# Right join to see all departments (even with no employees)
dept_employee_right = pd.merge(
    employees,
    departments,
    on='department_id',
    how='right'
)

print("\nAll departments with employee info (right join):")
print(dept_employee_right[['department_name', 'first_name', 'last_name']].sort_values('department_name'))
```

### Step 6: Advanced Analysis with Merged Data

```python
# Department salary analysis
dept_stats = employee_dept.groupby('department_name').agg(
    employee_count=('employee_id', 'count'),
    avg_salary=('salary', 'mean'),
    avg_tenure=('tenure', 'mean')
).round(1).reset_index()

print("\nDepartment statistics:")
print(dept_stats)

# Budget utilization
dept_stats = pd.merge(
    dept_stats,
    departments[['department_name', 'head_count_budget']],
    on='department_name'
)

dept_stats['utilization'] = (dept_stats['employee_count'] / dept_stats['head_count_budget']) * 100
dept_stats['utilization'] = dept_stats['utilization'].round(1)

print("\nDepartment budget utilization:")
print(dept_stats[['department_name', 'employee_count', 'head_count_budget', 'utilization']])
```

### Step 7: Handling Complex Merges (Multiple Keys)

```python
# Let's add location-specific salary adjustments
locations = pd.DataFrame({
    'department_name': ['Engineering', 'Marketing', 'Sales', 'Human Resources', 'Finance', 'Operations'],
    'location': ['San Francisco', 'Chicago', 'New York', 'Boston', 'New York', 'Chicago'],
    'cost_of_living_adjustment': [1.3, 1.1, 1.2, 1.15, 1.2, 1.1]
})

# Merge on multiple columns (department_name and location)
employee_dept_location = pd.merge(
    employee_dept,
    locations,
    on=['department_name', 'location'],
    how='left'
)

# Calculate adjusted salary
employee_dept_location['adjusted_salary'] = (
    employee_dept_location['salary'] * 
    employee_dept_location['cost_of_living_adjustment']
).round(2)

print("\nEmployees with cost of living adjustments:")
print(employee_dept_location[['first_name', 'last_name', 'department_name', 'location', 'salary', 'adjusted_salary']])
```

## Key Takeaways from This Example:

1. **Different Merge Types Serve Different Purposes**:
   - Inner join for standard employee-department matching
   - Left join to keep all employees (even without department info)
   - Right join to see all departments (even without employees)

2. **Real-World Data Challenges**:
   - Handling date fields (calculating tenure)
   - Dealing with potential missing department links
   - Multi-key merges for location-based adjustments

3. **Practical Applications**:
   - Workforce distribution analysis
   - Department budget utilization
   - Cost-of-living salary adjustments
   - HR reporting and metrics

This example demonstrates how merging datasets enables comprehensive workforce analytics that wouldn't be possible with separate datasets.

# Real-World Example: Merging COVID-19 and Economic Data

For this example, we'll use two publicly available datasets:
1. COVID-19 case data from Our World in Data
2. Country economic indicators from the World Bank

## Step 1: Import Libraries and Load Data Directly from URLs

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load COVID-19 data from Our World in Data
covid_url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
covid_data = pd.read_csv(covid_url)

# Load economic data from World Bank (simplified example)
# Note: For a real analysis, you might use the World Bank API or a preprocessed dataset
economic_data = pd.read_csv("https://raw.githubusercontent.com/datasets/world-bank-data/main/data/country_indicators.csv")

print("COVID Data Columns:", covid_data.columns.tolist())
print("\nEconomic Data Columns:", economic_data.columns.tolist())
```

## Step 2: Preprocess the Data

```python
# Filter COVID data for recent snapshot
latest_covid = covid_data[covid_data['date'] == covid_data['date'].max()]

# Select specific columns
covid_clean = latest_covid[['location', 'date', 'total_cases_per_million', 
                           'total_deaths_per_million', 'people_fully_vaccinated_per_hundred']]

# Clean economic data (example - would vary based on actual dataset)
economic_clean = economic_data[economic_data['Year'] == 2020][
    ['Country Name', 'GDP per capita (current US$)', 
     'Population, total', 'Life expectancy at birth, total (years)']]
economic_clean.columns = ['location', 'gdp_per_capita', 'population', 'life_expectancy']

print("\nLatest COVID Data:")
print(covid_clean.head())
print("\nEconomic Data:")
print(economic_clean.head())
```

## Step 3: Merge the Datasets

```python
# Merge on country name
merged_data = pd.merge(
    covid_clean,
    economic_clean,
    on='location',
    how='inner'  # Only countries with both COVID and economic data
)

print("\nMerged Dataset Shape:", merged_data.shape)
print("\nMerged Data Sample:")
print(merged_data.head())
```

## Step 4: Analyze the Relationship Between Wealth and COVID Outcomes

```python
# Calculate correlation matrix
correlation_matrix = merged_data[['total_cases_per_million', 
                                'total_deaths_per_million',
                                'people_fully_vaccinated_per_hundred',
                                'gdp_per_capita', 
                                'life_expectancy']].corr()

print("\nCorrelation Matrix:")
print(correlation_matrix)

# Visualization
plt.figure(figsize=(10, 6))
plt.scatter(merged_data['gdp_per_capita'], 
            merged_data['people_fully_vaccinated_per_hundred'],
            alpha=0.6)
plt.title('Vaccination Rates vs GDP per Capita')
plt.xlabel('GDP per Capita (USD)')
plt.ylabel('Fully Vaccinated (%)')
plt.grid(True)
plt.show()
```

## Step 5: Advanced Analysis - Regional Comparison

```python
# Add continent information (from the original COVID dataset)
continent_mapping = covid_data[['location', 'continent']].drop_duplicates()
merged_data = pd.merge(merged_data, continent_mapping, on='location', how='left')

# Group by continent
continent_stats = merged_data.groupby('continent').agg({
    'total_cases_per_million': 'mean',
    'total_deaths_per_million': 'mean',
    'people_fully_vaccinated_per_hundred': 'mean',
    'gdp_per_capita': 'mean'
}).reset_index()

print("\nRegional Statistics:")
print(continent_stats.round(2))

# Visualization
continent_stats.plot(x='continent', 
                    y=['total_cases_per_million', 'total_deaths_per_million'],
                    kind='bar', 
                    figsize=(10, 6),
                    title='COVID Outcomes by Continent')
plt.ylabel('Cases/Deaths per Million')
plt.show()
```

## Step 6: Handling Data Quality Issues

```python
# Check for missing values
print("\nMissing Values in Merged Data:")
print(merged_data.isnull().sum())

# Option 1: Drop rows with missing vaccination data
clean_data = merged_data.dropna(subset=['people_fully_vaccinated_per_hundred'])

# Option 2: Impute missing values (example with median)
merged_data['people_fully_vaccinated_per_hundred'] = merged_data[
    'people_fully_vaccinated_per_hundred'].fillna(
    merged_data['people_fully_vaccinated_per_hundred'].median())

print("\nData after handling missing values:")
print(merged_data.isnull().sum())
```

## Step 7: Export Merged Data for Further Analysis

```python
# Save to CSV
merged_data.to_csv('covid_economic_merged.csv', index=False)

# Save to Excel with multiple sheets
with pd.ExcelWriter('covid_economic_analysis.xlsx') as writer:
    merged_data.to_excel(writer, sheet_name='Merged Data')
    continent_stats.to_excel(writer, sheet_name='Regional Stats')
    correlation_matrix.to_excel(writer, sheet_name='Correlations')

print("\nData exported to CSV and Excel files.")
```

## Key Insights from This Real-World Example:

1. **Data Integration**: Combined health and economic datasets from different sources
2. **Practical Challenges**:
   - Handling different country naming conventions
   - Managing missing data
   - Working with different time periods

3. **Analysis Opportunities**:
   - Examined relationships between wealth and health outcomes
   - Compared regional patterns
   - Visualized complex relationships

4. **Real-World Applications**:
   - Public health policy analysis
   - Resource allocation planning
   - Socioeconomic impact studies

This example demonstrates how merging real-world datasets enables powerful analyses that can inform policy decisions and scientific research. The same approach can be applied to many other domains like:
- Financial market data + news sentiment
- Weather data + agricultural production
- Education statistics + employment outcomes