---
layout: page
title: PostgreSQL ROUND() Function Explained with Examples
description: Learn how to use PostgreSQL ROUND() to round numeric values to a specific number of decimal places. Includes examples for AVG(), practical SQL queries, and beginner-friendly explanations.
keywords: PostgreSQL ROUND function, SQL round function, ROUND in PostgreSQL, round decimal values, SQL numeric rounding, AVG with ROUND, SQL tutorial, PostgreSQL examples, database query examples, round to 2 decimals
---

`ROUND()` is used to **round a decimal number to a specific number of decimal places**.

In your query:

```sql
ROUND(AVG(amount), 2)
```

It means:

* `AVG(amount)` → calculates the average payment.
* `2` → keeps **2 digits after the decimal point**.
* `ROUND()` → rounds the result to those 2 decimal places.

### Example

Suppose the average payment is:

```text
4.356789
```

Using:

```sql
ROUND(4.356789, 2)
```

Result:

```text
4.36
```

Another example:

```sql
ROUND(10.124, 2)
```

Result:

```text
10.12
```

```sql
ROUND(10.126, 2)
```

Result:

```text
10.13
```

### In your query

```sql
SELECT
    customer_id,
    ROUND(AVG(amount), 2) AS average_payment
FROM payment
GROUP BY customer_id;
```

**Meaning:**
For each customer, calculate the average payment and display it with **only 2 decimal places**.

> **Remember:** `ROUND(number, 2)` = round the number to **2 decimal places**.
