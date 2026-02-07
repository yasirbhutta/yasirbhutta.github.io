---
layout: page
title: "Python Basics Mini Project: Build a Simple Expense Tracker"
description: Test your Python skills with this mini project! Learn to build a simple expense tracker using variables, loops, string formatting, and file handling. Perfect for beginners.
keywords: "expenses, expense, enter, file, cost, name, program, using"
toc: toc/python.html
course: python
topic: basics
show_toc: true
show_practice_progress: true
show_mini_project: false
breadcrumb: 
- title: Basics
url: /python/docs/basics/
---

### Mini Project: Build a Simple Expense Tracker

**Objective:**  
Create a Python program that allows users to track their daily expenses. This project will test your understanding of Python basics, including variables, `print` statements, string formatting, and file handling.

---

#### **Project Requirements:**

1. **Input Expenses:**
   - Prompt the user to enter the name of an expense (e.g., "Groceries") and its cost.
   - Allow the user to enter multiple expenses.

2. **Display Expenses:**
   - Print a neatly formatted list of all expenses using the `print` function.
   - Use `\t` (tab character) to align the expense names and their costs.

3. **Calculate Total:**
   - Calculate and display the total cost of all expenses.

4. **Save to File:**
   - Save the list of expenses and the total cost to a text file named `expenses.txt`.

5. **Error Handling:**
   - Handle invalid inputs (e.g., non-numeric values for costs) gracefully.

---

#### **Example Output:**

```output
Welcome to the Expense Tracker!

Enter the name of the expense (or type 'done' to finish): Groceries Enter the cost of Groceries: 50

Enter the name of the expense (or type 'done' to finish): Rent Enter the cost of Rent: 500

Enter the name of the expense (or type 'done' to finish): Utilities Enter the cost of Utilities: 100

Enter the name of the expense (or type 'done' to finish): done

Here is your expense summary: Expense Name Cost
Groceries $50 Rent $500 Utilities $100
Total: $650

Your expenses have been saved to 'expenses.txt'.
```


---

#### **Steps to Complete the Project:**

1. **Plan the Program:**
   - Identify the variables needed (e.g., `expenses`, `total_cost`).
   - Decide on the structure of the program (e.g., input loop, calculations, output).

2. **Write the Code:**
   - Use a loop to collect expense data from the user.
   - Store the expenses in a list or dictionary.
   - Use string formatting to display the expenses neatly.
   - Write the data to a file using the `with open()` statement.

3. **Test the Program:**
   - Test with different inputs, including invalid ones (e.g., entering text instead of numbers for costs).
   - Verify that the output is correct and the file is saved properly.

---

#### **Coding Challenge:**
- Add a feature to categorize expenses (e.g., "Food", "Rent", "Utilities").
- Allow the user to view expenses from a previous session by reading from the `expenses.txt` file.
- Add a date and time stamp to each expense entry using the `datetime` module.

---

#### **Learning Outcomes:**
- Practice using variables, loops, and conditionals.
- Learn how to format output using `print` and escape characters.
- Understand basic file handling in Python.
- Develop problem-solving and debugging skills.

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1602443888929206"
     crossorigin="anonymous"></script>
<ins class="adsbygoogle"
     style="display:block"
     data-ad-format="autorelaxed"
     data-ad-client="ca-pub-1602443888929206"
     data-ad-slot="7879511511"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>