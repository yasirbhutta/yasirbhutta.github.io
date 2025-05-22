---
layout: page
title: "How to Use the SUM Function and AutoSum in Excel – Complete Guide"
description: Learn how to use the SUM function and AutoSum in Microsoft Excel to quickly add values across cells, columns, or rows. Includes syntax, examples, and tips for efficient usage.
keywords: Excel SUM function, how to use SUM in Excel, Excel functions guide, Excel SUM formula, Excel add cells, Excel basics, Excel tutorials, Microsoft Excel functions, SUM formula examples
author: Muhammad Yasir Bhutta
course: ms-excel
topic: functions
toc: toc/ms-excel-toc.html
prev: /ms-excel/docs/functions/what-is-functions.html
next: /ms-excel/docs/functions/sumif.html
breadcrumb:
  - title: Home
    url: /
  - title: Excel
    url: /ms-excel/
  - title: Functions
    url: /ms-excel/docs/functions.html
---

## 📘 What is **SAP FM (Funds Management)?**

**SAP Funds Management (FM)** is a module in SAP Public Sector Management (PSM) used by **governments, universities, and nonprofit organizations** to **plan, allocate, monitor, and control budgets and funds**. It's especially crucial in **education and research institutions** where spending is tightly monitored against grants and government allocations.

---

## 🎓 SAP FM for **Education and Research Institutions**

In universities or research centers, SAP FM ensures that:

* Budgets from various sources (e.g., government, donors, grants) are allocated correctly.
* Expenditures stay within allocated limits.
* Financial accountability and compliance requirements are met.
* Real-time tracking of fund availability supports decision-making.

---

## 🔑 Key Features of SAP Funds Management (FM)

### 1. **Fund and Fund Center Management**

* Create and manage **funds** (sources of money) and **fund centers** (budget holders like departments).
* Example: A research department may have separate funds for government grants, private donations, and internal funding.

### 2. **Budgeting**

* **Create, release, and modify budgets** (transactions: FR51, FR52, FR58).
* Budget distributed to fund centers and commitment items.
* Annual or multi-year budget control.

### 3. **Availability Control**

* Automatic **budget checks** before expenses are posted.
* Prevent overspending using tolerance profiles.

### 4. **Integration with Other Modules**

* Works closely with:

  * **FI** (Financial Accounting) – actual postings
  * **MM** (Materials Management) – purchase orders, goods receipts
  * **GM** (Grants Management) – grant-based budgets
  * **CO/PS** – internal orders or projects

### 5. **Commitment and Actual Management**

* Tracks **commitments** (planned expenses) and **actuals** (real expenses).
* Ensures full visibility of financial status.

### 6. **Reporting and Analysis**

* Standard reports (e.g., **S\_ALR\_87013558** – Budget/Actual/Commitment/Remaining).
* Tracks how much budget is available, used, or encumbered.

---

## 🧪 Sample Practical Tasks (Education/Research Context)

| Task                            | Description                                                                                            |
| ------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **1. Create a Fund**            | Define a new fund for a research project (FMME).                                                       |
| **2. Create a Fund Center**     | Set up a fund center for a department (FMSA).                                                          |
| **3. Enter Budget**             | Allocate \$500,000 to a science department for the fiscal year (FR51).                                 |
| **4. Simulate Expense Posting** | Create a purchase order for lab equipment and check budget availability (ME21N with fund/fund center). |
| **5. Run a Report**             | Display remaining budget for a department (S\_ALR\_87013558).                                          |
| **6. Budget Transfer**          | Transfer budget from one fund center to another (FR58).                                                |
| **7. Release Budget**           | Use workflow to release a blocked budget to a department (FR52).                                       |

---

## 🧾 Example Use Case in a University

A university receives a **\$1 million research grant**:

* A **fund** is created for the grant.
* **Fund centers** are assigned to research departments.
* Budget is allocated and released.
* Purchases (equipment, services) are made against that fund.
* FM ensures **budget is not overspent**, and generates reports for audit and compliance.

---
