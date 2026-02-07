---
layout: page
title: "HALB Material Type in SAP: Semi-Finished Product Guide"
description: Learn what HALB material type means in SAP. Understand its use, configuration, transactions, and how it fits in BOM and production planning.
keywords: HALB material type SAP, semi-finished product SAP, SAP material types, SAP HALB vs FERT, HALB configuration in SAP, SAP BOM HALB, SAP MRP HALB
author: Muhammad Yasir Bhutta
course: sap-education-reasearch
topic: sap-mm
toc: toc/sap-education-research.html
show_toc: yes
prev: /sap-education-research/docs/sap-mm/
next: /sap-education-research/docs/sap-ps/
breadcrumb: 
- title: Material Types
url: /sap-education-research/docs/sap-mm/material-types.html
---

In SAP, **HALB** stands for **"Halbfertigprodukt"** in German, which translates to **"semi-finished product"** in English.

### ✅ Definition:

**HALB (Semi-Finished Product)** is a **material type** used in SAP to represent materials that are:

* Produced internally or externally
* Not sold directly to customers
* Used as components in the **production of finished goods (FERT)**

---

### 🔧 Typical Use Cases:

* Components that go through one or more production steps.
* Intermediate assemblies in a manufacturing process.
* Used in **Bills of Materials (BOMs)** for final products.

---

### 🧾 Key Configuration & Features:

| Feature              | Description                                                                 |
| -------------------- | --------------------------------------------------------------------------- |
| **Material Type**    | HALB                                                                        |
| **Valuation**        | Can be valuated (price, costing, etc.)                                      |
| **Procurement Type** | Can be **in-house production (E)** or **external procurement (F)**          |
| **MRP Views**        | MRP 1, 2, 3, and 4 views are important for planning and production settings |
| **BOM Usage**        | Can appear as components in BOMs for FERT materials                         |

---

### 📌 Common Transactions:

| Purpose                    | Transaction Code |
| -------------------------- | ---------------- |
| Create Material            | `MM01`           |
| Change Material            | `MM02`           |
| Display Material           | `MM03`           |
| BOM Maintenance            | `CS01`/`CS02`    |
| Routing/Recipe Maintenance | `CA01`/`CA02`    |

---

### 🔄 Related Material Types:

| Material Type | Description             |
| ------------- | ----------------------- |
| **FERT**      | Finished product        |
| **ROH**       | Raw material            |
| **VERP**      | Packaging material      |
| **HIBE**      | Operating supplies      |
| **NLAG**      | Non-stock (consumables) |


