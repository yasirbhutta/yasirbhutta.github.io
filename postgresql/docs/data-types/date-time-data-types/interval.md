---
layout: page
title: "PostgreSQL INTERVAL - Syntax, Examples and Practical Use"
description: Learn how to use the PostgreSQL INTERVAL data type to represent time durations and calculate dates and timestamps with NOW().
keywords: PostgreSQL INTERVAL, INTERVAL data type, PostgreSQL interval arithmetic, NOW function, date and time arithmetic, interval multiplication, DELETE cutoff date
---

In PostgreSQL, `INTERVAL '1 day'` represents a time duration of one day (24 hours).

Let's understand this expression:

```sql
INTERVAL '1 day' * p_days
```

### 1. What is INTERVAL?

`INTERVAL` is a PostgreSQL data type used to represent a period of time.

**Examples:**

```sql
INTERVAL '1 day'
INTERVAL '2 days'
INTERVAL '1 month'
INTERVAL '1 year'
INTERVAL '3 hours'
INTERVAL '30 minutes'
```

### 2. Understanding INTERVAL '1 day' \* p_days

Consider this expression:

```sql
NOW() - INTERVAL '1 day' * p_days
```

It calculates a date and time by subtracting the specified number of days from the current date and time.

Suppose:

```sql
p_days = 7;
```

The expression becomes:

```sql
NOW() - INTERVAL '1 day' * 7
```

Which is equivalent to:

```sql
NOW() - INTERVAL '7 days'
```

### 3. Practical Example

Suppose the current date and time is:

`2026-11-19 10:00:00`

If `p_days = 7`, PostgreSQL calculates:

Current date and time

# 19 Nov 2026, 10:00 AM

7 days

Calculated date and time

# 12 Nov 2026, 10:00 AM

### 4. How It Works in DELETE

```sql
DELETE FROM rental
WHERE rental_date < NOW() - INTERVAL '1 day' * p_days;
```

Explanation:

1. `NOW()` gets the current date and time.
2. `INTERVAL '1 day'` represents one day.
3. `* p_days` multiplies one day by the specified number of days.
4. `NOW() - ...` calculates the cutoff date and time.
5. `WHERE` selects rentals older than the calculated cutoff.

Example: If `p_days = 7`, the procedure deletes rentals whose `rental_date` is earlier than seven days ago.

### 5. Try to Understand

If `p_days = 30`, what does this expression represent?

```sql
INTERVAL '1 day' * p_days
```

Remember: `INTERVAL` represents a time duration, while `NOW()` returns the current date and time.