---
layout: page
title: "The `datetime` Module in Python"
description: Learn about Python's datetime module with common methods, syntax examples, and real-life applications. Perfect for beginners to master date and time manipulation in Python programming.
keywords: Python datetime module, datetime methods, Python date and time, datetime examples, Python datetime tutorial, datetime strftime, datetime strptime, timedelta Python, Python date manipulation, Python time handling, beginner Python datetime, real-world datetime examples
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

The `datetime` module in Python provides classes for manipulating dates and times. It's one of the most commonly used modules for working with dates, times, and time intervals in Python applications.

## Common Classes and Methods with Syntax and Examples

### 1. `datetime.date`
Represents a date (year, month, day).

```python
from datetime import date

# Create a date object
d = date(2023, 5, 15)
print(d)  # Output: 2023-05-15

# Get today's date
today = date.today()
print(today)  # Output: current date (e.g., 2023-11-20)

# Access components
print(today.year, today.month, today.day)
```

### 2. `datetime.time`
Represents a time (hour, minute, second, microsecond).

```python
from datetime import time

# Create a time object
t = time(14, 30, 15)
print(t)  # Output: 14:30:15

# Access components
print(t.hour, t.minute, t.second)
```

### 3. `datetime.datetime`
Combines date and time information.

```python
from datetime import datetime

# Create a datetime object
dt = datetime(2023, 5, 15, 14, 30, 15)
print(dt)  # Output: 2023-05-15 14:30:15

# Get current datetime
now = datetime.now()
print(now)  # Output: current datetime

# Access components
print(now.year, now.month, now.day, now.hour, now.minute)
```

### 4. `datetime.timedelta`
Represents a duration or difference between two dates/times.

```python
from datetime import datetime, timedelta

# Current time
now = datetime.now()

# Add 5 days to current date
future_date = now + timedelta(days=5)
print(future_date)

# Subtract 2 weeks
past_date = now - timedelta(weeks=2)
print(past_date)

# Calculate difference between two dates
delta = future_date - past_date
print(delta.days)  # Output: 19 (5 + 14 days)
```

### 5. Formatting Dates (`strftime`)
Convert datetime to string with custom format.

```python
from datetime import datetime

now = datetime.now()

# Format as string
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)  # Output: "2023-11-20 14:30:15"

# Common format codes:
# %Y - Year (2023)
# %m - Month (01-12)
# %d - Day (01-31)
# %H - Hour (00-23)
# %M - Minute (00-59)
# %S - Second (00-59)
```

### 6. Parsing Dates (`strptime`)
Convert string to datetime object.

```python
from datetime import datetime

date_string = "15 May 2023"
dt = datetime.strptime(date_string, "%d %B %Y")
print(dt)  # Output: 2023-05-15 00:00:00
```

## Real-Life Examples of the datetime Module

### 1. Age Calculator
```python
from datetime import date

def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year
    # Adjust if birthday hasn't occurred yet this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

birthday = date(1990, 7, 15)
print(f"Age: {calculate_age(birthday)} years")
```

### 2. Countdown Timer
```python
from datetime import datetime, timedelta

event_date = datetime(2023, 12, 31)  # New Year's Eve
current_date = datetime.now()
time_left = event_date - current_date

print(f"Days until event: {time_left.days} days")
print(f"Hours until event: {time_left.total_seconds()/3600:.1f} hours")
```

### 3. File Backup with Timestamp
```python
from datetime import datetime

def backup_file(filename):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"{filename}.backup_{timestamp}"
    # Code to copy file would go here
    print(f"Created backup: {backup_name}")

backup_file("important_document.txt")
```

### 4. Workday Calculator
```python
from datetime import datetime, timedelta

def calculate_due_date(start_date, working_days):
    current_date = start_date
    added_days = 0
    
    while added_days < working_days:
        current_date += timedelta(days=1)
        # Skip weekends (5=Saturday, 6=Sunday)
        if current_date.weekday() < 5:
            added_days += 1
            
    return current_date

start = datetime(2023, 11, 20)  # Monday
due_date = calculate_due_date(start, 5)  # 5 working days
print(f"Due date: {due_date.strftime('%A, %B %d, %Y')}")
```

### 5. Logging with Timestamps
```python
from datetime import datetime

def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

log_message("System started")
log_message("Processing data...")
```

### 6. Event Reminder
```python
from datetime import datetime, timedelta

events = {
    "Dentist Appointment": datetime(2023, 11, 25, 14, 0),
    "Team Meeting": datetime(2023, 11, 22, 10, 30)
}

now = datetime.now()
for event, event_time in events.items():
    if now < event_time < now + timedelta(days=7):
        time_left = event_time - now
        days = time_left.days
        hours = time_left.seconds // 3600
        print(f"Reminder: {event} in {days} days and {hours} hours")
```

The datetime module is essential for any Python application that needs to work with dates and times, from simple logging to complex scheduling systems. It provides a robust set of tools for date and time manipulation that can handle most common use cases.
