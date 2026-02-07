---
layout: page
title: "Standard Naming Convention for Business Event Type in SAP SLCM – Format, Examples, and Best Practices"
description: Learn the standardized naming convention for courses in SAP SLCM. Discover the correct format, detailed component explanations, and practical examples for course codes, sections, semesters, and shifts. Follow best practices to ensure consistency and clarity across university departments.
keywords: SAP SLCM naming convention, SAP course naming, SAP standard naming, SAP course code format, SAP section code, SAP semester code, SAP shift code, SAP best practices, SAP education, SAP university course management, SAP user guide
author: Muhammad Yasir Bhutta
course: sap-education-reasearch
show_practice_progress: false
toc: toc/sap-education-research.html
show_toc: yes
prev: /sap-education-research/
breadcrumb: 
- title: SAP User Guides
url: /sap-education-research/user-guide/
---

## 🔹 Standardized Naming Convention for Business Event Type in SAP SLCM

**Format:**

```
<COURSECODE>-<SECTION>-<SEMESTER>-<SHIFT>
```

---

## 🔹 Components Explained

* **COURSECODE** → Course number (e.g., CHEM-403, CSC-101, ENG-205)
* **SECTION** → A, B, C … (sequential per semester)
* **SEMESTER** →

  * `F25` = Fall 2025
  * `S25` = Spring 2025
  * `Su25` = Summer 2025
* **SHIFT** →

  * `M` = Morning
  * `E` = Evening
  * `WE` = Weekend

---

## 🔹 Standard Examples

### Chemistry – CHEM-403 (Fall 2025)

* **Morning Sections**

  * `CHEM-403-F25-M` → Morning
  * `CHEM-403-A-F25-M` → Section A, Morning
  * `CHEM-403-B-F25-M` → Section B, Morning

* **Evening Sections**

  * `CHEM-403-F25-E` → Evening
  * `CHEM-403-A-F25-E` → Section A, Evening
  * `CHEM-403-B-F25-E` → Section B, Evening


---

## ✅ Best Practices

1. **Consistency is key** — same format across all faculties.
2. **Uppercase** for `Course Code`, `SECTION`, and `SHIFT` → avoids confusion in reports.
3. **Semester codes fixed** → `F`, `S`, `Su` (no variations like FA, SP, SUM).
4. **Shift codes fixed** → `M`, `E`, `WE`.
5. Always **document and circulate** the naming standard for departmental compliance.

## 📘 **Related Topics**

* [Difference Between Business Event Type and Business Event in SAP SLCM](../../sap-slcm/difference-bet-business-event-type.md)






