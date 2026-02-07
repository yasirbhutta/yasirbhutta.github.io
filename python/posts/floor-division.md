---
layout: page
title: **What is the `//` Operator in Python?**
description: The `//` operator in Python is the floor division operator. It divides two numbers and returns the quotient, rounded down to the nearest whole number...
keywords: print, output, down, full, script
---
# **What is the `//` Operator in Python?**

The `//` operator in Python is the **floor division** operator. It divides two numbers and **returns the quotient, rounded down to the nearest whole number (integer if both operands are integers, or a float if at least one operand is a float).**  

## **Difference Between `/` and `//` Operator**
| Operator | Description | Example |
|----------|------------|---------|
| `/` (Division) | Returns the exact quotient (floating-point result). | `7 / 2 = 3.5` |
| `//` (Floor Division) | Returns the quotient rounded down to the nearest whole number. | `7 // 2 = 3` |

## **Examples in Python**
```python
# Using / operator (Division)
print(7 / 2)   # Output: 3.5
print(9 / 4)   # Output: 2.25

# Using // operator (Floor Division)
print(7 // 2)  # Output: 3
print(9 // 4)  # Output: 2

# Works with negative numbers too
print(-7 // 2)  # Output: -4  (because -3.5 rounds down to -4)
```

---

## **Real-World Use Cases of `//` Operator**
1. **Splitting People into Groups:**  
   Suppose you have 100 students and want to divide them into groups of 7.
   ```python
   students = 100
   group_size = 7
   num_groups = students // group_size  # 100 // 7 = 14
   print(num_groups)  # Output: 14
   ```
   This tells us that we can form 14 full groups of 7 students.

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

2. **Calculating Days from Hours:**  
   You have 50 hours and want to find out how many full days (24 hours) are in it.
   ```python
   hours = 50
   days = hours // 24  # 50 // 24 = 2
   print(days)  # Output: 2
   ```
   It tells us we have 2 full days in 50 hours.

3. **Pagination in Web Applications:**  
   If you have 500 comments and each page shows 20 comments, how many full pages will you get?
   ```python
   total_comments = 500
   comments_per_page = 20
   total_pages = total_comments // comments_per_page  # 500 // 20 = 25
   print(total_pages)  # Output: 25
   ```
   This ensures 25 full pages of comments.

4. **Distributing Tasks Among Workers:**  
   If there are 120 tasks and 5 workers, how many full tasks does each worker get?
   ```python
   tasks = 120
   workers = 5
   tasks_per_worker = tasks // workers  # 120 // 5 = 24
   print(tasks_per_worker)  # Output: 24
   ```
   Each worker gets 24 full tasks.

## **What Does "Rounded Down" Mean in Floor Division (`//`)?**  

When we say **"rounded down"**, it means the quotient is always **reduced to the nearest smaller whole number** (or integer). This happens even if the result is negative.

For example:  
- `7 // 2 = 3` → The exact result is `3.5`, but it rounds down to `3`.  
- `9 // 4 = 2` → The exact result is `2.25`, but it rounds down to `2`.  
- `-7 // 2 = -4` → The exact result is `-3.5`, but rounding down moves it to `-4` (towards more negative).  

## **Key Rule:**  
- **For positive numbers**, it behaves like normal integer division.  
- **For negative numbers**, it rounds down to the lower integer (more negative).  

For detailed information on operators, see [Use of Operators in Python](../docs/operators.md)

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1602443888929206"
     crossorigin="anonymous"></script>
<!-- display square -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-1602443888929206"
     data-ad-slot="9845543342"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>