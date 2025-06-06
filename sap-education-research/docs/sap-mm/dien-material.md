---
layout: page
title: "DIEN Material Type in SAP: Complete Service Guide"
description: Learn about the DIEN material type in SAP used for services. Understand its features, usage, differences from NLAG, and how it supports service procurement.
keywords: DIEN material type SAP, SAP service material, SAP DIEN vs NLAG, SAP services procurement, SAP ML81N, service entry sheet SAP, SAP material types
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

**DIEN** stands for **"Dienstleistung"** in German, which translates to **"Service"** in English.
In SAP, the **DIEN material type** is used to represent **services** rather than physical goods. Unlike stock materials, DIEN items are **not managed in inventory** and are typically used in **service procurement** processes.

---

### 🧾 **Key Characteristics:**

| Feature                  | Description                                                          |
| ------------------------ | -------------------------------------------------------------------- |
| **Material Type**        | DIEN (Service Material)                                              |
| **Inventory Management** | ❌ Not managed in stock or inventory                                  |
| **Valuation**            | ✅ Valuated at the time of procurement (posted to expense accounts)   |
| **Used For**             | External services like maintenance, consulting, cleaning, IT support |
| **Procurement Type**     | External procurement (Service PO, Service Entry Sheet)               |
| **MRP Views**            | Usually not used (not stock-related)                                 |
| **Service Entry**        | Required to confirm service delivery (`ML81N`)                       |

---

### 🧰 **Typical Use Cases:**

* Facility maintenance services
* Equipment repair or servicing
* Software development or consulting services
* Security or cleaning contracts

---

### 🔧 Common SAP Transactions:

| Purpose                   | Transaction Code              |
| ------------------------- | ----------------------------- |
| Create Material (Service) | `MM01` (Material type = DIEN) |
| Create Purchase Order     | `ME21N`                       |
| Service Entry Sheet       | `ML81N`                       |
| Display Purchase Order    | `ME23N`                       |

---

### 🔄 Difference Between DIEN and NLAG:

| Feature              | **DIEN** (Service) | **NLAG** (Non-stock item) |
| -------------------- | ------------------ | ------------------------- |
| Stock managed?       | ❌ No               | ❌ No                      |
| Physical material?   | ❌ No (intangible)  | ✅ Yes (consumable)        |
| Needs service entry? | ✅ Yes (`ML81N`)    | ❌ No                      |
| Used for             | Services           | Consumable goods          |

---

### 🔹 Related Material Types:

* **SERV** – External services
* **[NLAG](nlag-material.md)** – Non-stock consumables
* **ROH** – Raw materials
* **FERT** – Finished products

---
