---
layout: page
title: "SAP Material Types Explained: ROH, HALB, FERT, NLAG & More for Effective Inventory Control"
description: Explore common SAP Material Types such as ROH, HALB, FERT, NLAG, and more. Learn their use cases, control functions, and how to manage materials like consumables, IT equipment, packaging, and services effectively in SAP ERP.
keywords: SAP Material Types, SAP ROH HALB FERT, SAP NLAG meaning, SAP consumables, SAP inventory management, SAP ERP materials, SAP non-stock material, SAP material type list, SAP stock vs non-stock, SAP IT equipment material type, SAP material master views, SAP procurement types, SAP valuation class, SAP operating supplies
author: Muhammad Yasir Bhutta
course: sap-education-reasearch
topic: sap-mm
toc: toc/sap-education-research.html
show_toc: yes
prev: /sap-education-research/docs/sap-mm/
next: /sap-education-research/docs/sap-ps/
breadcrumb:
  - title: Home
    url: /
  - title: SAP
    url: /sap-education-research/
  - title: MM
    url: /sap-education-research/docs/sap-mm/
---

In **SAP**, **Material Types** define important controls for how a material is managed, procured, and accounted for. Each material type has specific properties, such as whether it is stock-managed, valuated, or consumed directly. Here’s a breakdown of the most commonly used **Material Types in SAP**:

---

### 🔹 **Common SAP Material Types**

| Material Type | Description                      | Typical Use                                                             |
| ------------- | -------------------------------- | ----------------------------------------------------------------------- |
| **ROH**       | Raw Material                     | Used in production but not sold directly. No sales or purchasing views. |
| **[HALB](halb-material.md)**      | Semi-Finished Goods              | Used in production and assembled into finished products.                |
| **FERT**      | Finished Product                 | Sold to customers. Has sales and distribution views.                    |
| **HIBE**      | Operating Supplies               | Materials used in operations (e.g., lubricants, cleaning materials).    |
| **[NLAG](nlag-material.md)**      | Non-Stock Material (Consumables) | Expensed directly, not managed in inventory (e.g., USB drives, cables). |
| **VERP**      | Packaging Material               | Used to pack goods (e.g., boxes, cartons).                              |
| **[DIEN](dien-material.md)**      | Service                          | Non-material services (e.g., consulting, maintenance). No inventory.    |
| **[SERV](serv-material.md)**      | External Services | External service item for [structured service procurement](structured-service-proc.md). |
| **ERSA**      | Spare Parts                      | Parts used for maintenance of equipment. Stock-managed.                 |
| **LEER**      | Returnable Packaging             | Materials returned by customers (e.g., containers, bottles).            |
| **PROD**      | Product Group                    | Group of materials for planning, not an individual material.            |
| **PIPE**      | Pipeline Material                | Materials like gas, water that flow through pipelines.                  |
| **FHMI**      | Production Resource/Tool         | Tools used in production (e.g., molds, jigs). Not consumed directly.    |
| **TRAD**      | Trading Goods                    | Purchased and sold without modification.                                |

---

### 🧠 **Key Control Functions of Material Type**

Material types control:

* Whether the material is **stocked or not** (inventory managed)
* **Views available** in the material master (e.g., Sales, Purchasing, Accounting)
* The **number range** for material numbers
* **Default valuation class** for accounting
* **Allowed procurement types** (in-house, external)

---

### ✅ **For Consumables / IT Equipment**

Use:

* **NLAG** (Non-Stock Material): For items like mouse, cables, adapters.
* **HIBE** (Operating Supplies): For operational materials used regularly.
* **ERSA** (Spare Parts): If the item is stock-managed and replaceable.

## 📘 **Related Topics**

* **Decimals and Percentages** – Learn how to convert fractions into decimals and percentages, and apply them in everyday situations.
  👉 [Learn more](#)

