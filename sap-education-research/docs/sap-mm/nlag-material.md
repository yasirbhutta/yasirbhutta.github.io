---
layout: page
title: "NLAG Material Type in SAP: Non-Stock Material Explained"
description: Understand NLAG material type in SAP. Learn its use, characteristics, examples, and how it's different from stock materials like ROH or FERT.
keywords: NLAG material type SAP, non-stock material SAP, SAP consumable materials, SAP NLAG vs ROH, SAP material types, SAP non-valuated materials
author: Muhammad Yasir Bhutta
course: sap-education-reasearch
topic: sap-mm
toc: toc/sap-education-research.html
prev: /sap-education-research/docs/sap-mm/
next: /sap-education-research/docs/sap-ps/
breadcrumb:
  - title: Home
    url: /
  - title: SAP
    url: /sap-education-research/
  - title: MM
    url: /sap-education-research/docs/sap-mm/
  - title: Material Types
    url: /sap-education-research/docs/sap-mm/material-types.html
---

### ✅ **Definition:**

**NLAG** stands for **"Non-Stock Material"** in SAP. It is used for materials that are **not kept in stock** and are **not managed in inventory**. These are typically **consumables**, like office supplies, small tools, or services — things that are used up quickly and don’t need to be tracked in inventory.

---

### 🧾 **Key Characteristics:**

| Feature                  | Description                                                      |
| ------------------------ | ---------------------------------------------------------------- |
| **Material Type**        | NLAG (Non-stock material)                                        |
| **Inventory Management** | ❌ Not quantity or value managed in inventory                     |
| **Valuation**            | ✅ Can be valuated during procurement (but not tracked afterward) |
| **Typical Use**          | Consumables, spare parts, services, one-time purchases           |
| **Procurement Type**     | External procurement (purchased directly)                        |
| **MRP Views**            | Usually not relevant (not planned by MRP)                        |
| **Stock Management**     | Not applicable                                                   |
| **Posting**              | Expense account directly at goods receipt                        |

---

### 📦 Examples of NLAG Materials:

* Printer cartridges
* Office stationery
* Cleaning supplies
* External consulting services
* Small tools not meant to be inventoried

---

### 🔧 Common SAP Transactions:

| Purpose                   | Transaction Code |
| ------------------------- | ---------------- |
| Create Material           | `MM01`           |
| Change Material           | `MM02`           |
| Display Material          | `MM03`           |
| Purchase Requisition      | `ME51N`          |
| Purchase Order            | `ME21N`          |
| Goods Receipt (non-stock) | `MIGO`           |

---

### 🔄 Difference Between NLAG and ROH:

| Feature              | **NLAG**                    | **ROH**                      |
| -------------------- | --------------------------- | ---------------------------- |
| Stock managed?       | ❌ No                        | ✅ Yes                        |
| Inventory valuation? | ❌ Not tracked in stock      | ✅ Tracked in stock           |
| Used for             | Consumables, services       | Raw materials for production |
| Goods receipt        | Directly to expense account | To inventory stock           |

---

### 🔹 Related Material Types:

* **ROH** – Raw materials
* **FERT** – Finished products
* **[HALB](halb-material.md)** – Semi-finished products
* **SERV** – Services
* **HIBE** – Operating supplies

---

