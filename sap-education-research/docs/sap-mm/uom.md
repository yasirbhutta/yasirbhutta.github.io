---
layout: page
title: "Understanding Units of Measure (UoM) in SAP: Types, Examples & Usage"
description: Learn what measuring units in SAP are, including base, order, and sales units. See common UoM codes like PC, KG, L, and how they're used in SAP material management.
keywords: SAP unit of measure, SAP UoM types, SAP measuring unit list, base unit of measure in SAP, order unit SAP, SAP material master unit, SAP UoM examples, T006 SAP table, CUNI SAP transaction, alternative unit of measure SAP
author: Muhammad Yasir Bhutta
course: sap-education-reasearch
topic: sap-mm
toc: toc/sap-education-research.html
show_toc: yes
prev: /sap-education-research/docs/sap-mm/
next: /sap-education-research/docs/sap-ps/
breadcrumb: 
- title: MM
url: /sap-education-research/docs/sap-mm/
---

In **SAP**, a **measuring unit** (also called **unit of measure**, or **UoM**) is used to define **how quantities of materials are measured and managed** in business processes such as purchasing, inventory management, sales, and production.

---

### 🔍 What is a Measuring Unit in SAP?

A **measuring unit** (Unit of Measure - UoM) represents the **quantity basis** for transactions involving materials.

For example:

* 1 **PC** (piece)
* 5 **KG** (kilograms)
* 10 **L** (liters)
* 100 **M** (meters)

SAP supports multiple units for a single material (e.g., base unit, alternative units).

---

### 🧾 Types of Units of Measure in SAP:

| UoM Type                        | Description                                            |
| ------------------------------- | ------------------------------------------------------ |
| **Base Unit of Measure (BME)**  | Primary unit used for stockkeeping (e.g., EA, KG, L).  |
| **Alternative Unit of Measure** | Used in different processes (e.g., 1 box = 10 pieces). |
| **Sales Unit**                  | Unit in which the product is sold (e.g., box, carton). |
| **Order Unit**                  | Unit in which product is ordered from supplier.        |
| **Unit of Issue**               | Unit in which the material is issued from storage.     |

---

### 📘 Examples of Common Measuring Units in SAP:

| Code    | Description          |
| ------- | -------------------- |
| **PC**  | Piece                |
| **EA**  | Each (same as piece) |
| **KG**  | Kilogram             |
| **G**   | Gram                 |
| **L**   | Liter                |
| **ML**  | Milliliter           |
| **M**   | Meter                |
| **CM**  | Centimeter           |
| **BOX** | Box                  |
| **ROL** | Roll                 |
| **PAK** | Pack                 |
| **SET** | Set                  |
| **DOZ** | Dozen                |
| **H**   | Hour                 |
| **DAY** | Day                  |

---

### 🔧 SAP Table Reference:

* **T006** – Standard SAP table that stores all units of measure.
* **CUNI** – Transaction code to view/edit units of measure in SAP.

---

### 📝 How to Use/Assign in SAP:

When creating or updating a material master (TCode: **MM01**, **MM02**, **MM03**), you define:

* Base Unit of Measure
* Any additional units (with conversion factors)
