---
layout: page
title: "Installing & Using External Libraries in Python with `pip`"
description: Learn how to install and use external Python libraries with pip – a beginner-friendly guide with practical examples. Discover essential pip commands, popular libraries like requests, matplotlib, and beautifulsoup4, and best practices for dependency management.
keywords: Python pip tutorial, install Python libraries, pip commands, Python package manager, how to use pip, Python requests, matplotlib tutorial, beautifulsoup web scraping, Python virtual environments, pip install examples, Python for beginners, external libraries Python
author: Muhammad Yasir Bhutta
course: python
topic: pandas
toc: toc/python.html
prev: /python/docs/modules/numpy.html
next: /python/docs/modules/scipy.html
breadcrumb: 
- title: Python
url: /python/
---

## What is `pip`?

`pip` is the standard package manager for Python that allows you to install and manage additional libraries that aren't part of the standard Python library.

## Checking if `pip` is Installed

Before using `pip`, check if it's already installed (it usually comes with Python 3.4+):

```bash
pip --version
```

or 

```bash
pip3 --version
```

## Basic `pip` Commands

### Installing a Package

```bash
pip install package_name
```

Example:
```bash
pip install requests
```

### Installing a Specific Version

```bash
pip install package_name==version_number
```

Example:
```bash
pip install requests==2.25.1
```

### Upgrading a Package

```bash
pip install --upgrade package_name
```

Example:
```bash
pip install --upgrade requests
```

### Uninstalling a Package

```bash
pip uninstall package_name
```

Example:
```bash
pip uninstall requests
```

### Listing Installed Packages

```bash
pip list
```

### Showing Package Information

```bash
pip show package_name
```

Example:
```bash
pip show requests
```

## Practical Examples of Using External Libraries

### Example 1: Making HTTP Requests with `requests`

```python
import requests

# Make a GET request to a website
response = requests.get('https://www.example.com')

# Check if the request was successful
if response.status_code == 200:
    print("Successfully fetched the page!")
    print(f"Page content length: {len(response.text)} characters")
else:
    print(f"Failed to fetch page. Status code: {response.status_code}")
```

### Example 2: Working with Dates using `python-dateutil`

```python
from dateutil import parser
from dateutil.relativedelta import relativedelta

# Parse a date string
date = parser.parse("June 5th 2023 10:30 PM")
print(f"Parsed date: {date}")

# Add 2 months to the date
new_date = date + relativedelta(months=+2)
print(f"Date after adding 2 months: {new_date}")
```

### Example 3: Data Visualization with `matplotlib`

```python
import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a simple line plot
plt.plot(x, y)

# Add labels and title
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Simple Line Plot')

# Display the plot
plt.show()
```

### Example 4: Working with Excel Files using `openpyxl`

```python
from openpyxl import Workbook

# Create a new Excel workbook
wb = Workbook()

# Get the active worksheet
ws = wb.active

# Add some data
ws['A1'] = "Name"
ws['B1'] = "Age"
ws['A2'] = "Alice"
ws['B2'] = 25
ws['A3'] = "Bob"
ws['B3'] = 30

# Save the workbook
wb.save("sample.xlsx")
print("Excel file created successfully!")
```

### Example 5: Web Scraping with `beautifulsoup4`

```python
import requests
from bs4 import BeautifulSoup

# Fetch a webpage
url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Extract and print the page title
title = soup.find('h1').text
print(f"Page title: {title}")

# Extract and print the first paragraph
first_paragraph = soup.find('p').text
print(f"\nFirst paragraph:\n{first_paragraph}")
```

## Virtual Environments (Bonus)

For project-specific dependencies, it's good practice to use virtual environments:

1. Create a virtual environment:
```bash
python -m venv myenv
```

2. Activate it:
- On Windows:
```bash
myenv\Scripts\activate
```
- On macOS/Linux:
```bash
source myenv/bin/activate
```

3. Now install packages within this environment:
```bash
pip install package_name
```

4. Deactivate when done:
```bash
deactivate
```

## Requirements Files

You can save all your project's dependencies to a file:

```bash
pip freeze > requirements.txt
```

And later install them all at once:

```bash
pip install -r requirements.txt
```

## Conclusion

Using external libraries with `pip` greatly expands what you can do with Python. Start with simple libraries like `requests` or `matplotlib`, and gradually explore more specialized ones as you need them for your projects.