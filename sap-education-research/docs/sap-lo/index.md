---
layout: page
title: "SAP EAM Work Center Guide – Definition, Attributes, T-Codes, and IT Support Example"
description: Explore a complete guide on SAP EAM Work Centers including definitions, key attributes, usage in maintenance orders, related transaction codes, and a real-world IT support center example for universities.
keywords: SAP EAM work center, SAP maintenance work center, SAP CR01 CR02 CR03, SAP work center example, SAP work center attributes, IT support in SAP EAM, SAP maintenance order work center, SAP PM functional location, SAP EAM university example, SAP work center cost planning, SAP PM training content
author: Muhammad Yasir Bhutta
course: sap-education-reasearch
topic: sap-eam
toc: toc/sap-education-research.html
prev: /sap-education-research/
next: /sap-education-research/docs/sap-fico/
breadcrumb:
  - title: Home
    url: /
  - title: SAP
    url: /sap-education-research/
  - title: LO
    url: /sap-education-research/docs/sap-lo/
---

## Table of Contents

1. 📦 **What is **SAP Logistics – General (LO)?
2. 2. 🧱 Key Functionalities of SAP LO
3. 🔗 Integration with Other SAP Modules
4. 4. 🛠️ Common LO T-Codes
5. 5. 🏛️ Why SAP LO Matters in a University or Non-Manufacturing Setup
   
## 1. 📦 **What is **SAP Logistics – General (LO)?**

**SAP Logistics – General (LO)** is a **core component of SAP ERP** that provides **foundational logistics functions** used by other SAP logistics modules like:

* **MM (Materials Management)**
* **SD (Sales and Distribution)**
* **PP (Production Planning)**
* **PM (Plant Maintenance)**
* **QM (Quality Management)**
* **WM/EWM (Warehouse Management)**

It contains **cross-application tools** and **basic structures** that ensure consistent data and integration across the entire logistics chain.

---

## 2. 🧱 Key Functionalities of SAP LO

| Area                                    | Description                                                                           |
| --------------------------------------- | ------------------------------------------------------------------------------------- |
| **Enterprise Structure**                | Define and manage plants, storage locations, company codes, and organizational units. |
| **Material Master Data**                | Centralized data management for all materials across MM, PP, SD, and PM.              |
| **Batch Management**                    | Track material batches (e.g., for pharmaceuticals, food, or chemicals).               |
| **Classification System**               | Categorize materials, equipment, or documents using classes and characteristics.      |
| **Document Management System (DMS)**    | Manage engineering drawings, blueprints, and technical files.                         |
| **Units of Measure**                    | Set up base and alternative units (e.g., box, carton, dozen).                         |
| **Conversion Factors**                  | Unit and currency conversions for global logistics.                                   |
| **Engineering Change Management (ECM)** | Control changes in product structure or specs over time.                              |

---

## 3. 🔗 Integration with Other SAP Modules

| SAP Module | Example of LO Integration              |
| ---------- | -------------------------------------- |
| **MM**     | Material master and plant setup        |
| **SD**     | Sales unit and product classification  |
| **PP**     | BOM classification and routing         |
| **PM**     | Equipment classification and documents |
| **QM**     | Batch characteristics and tracking     |
| **WM/EWM** | Storage units and logistics structure  |

---

## 4. 🛠️ Common LO T-Codes

| T-Code  | Description                       |
| ------- | --------------------------------- |
| `OX10`  | Create/define Plant               |
| `OX03`  | Create Company Code               |
| `MM01`  | Create Material Master            |
| `CL01`  | Create Class                      |
| `CT04`  | Create Characteristic             |
| `CU50`  | Configuration Simulation          |
| `CC01`  | Create Change Master (ECM)        |
| `CV01N` | Create Document Info Record (DMS) |

---

## 5. 🏛️ Why SAP LO Matters in a University or Non-Manufacturing Setup

In universities, hospitals, or public sector organizations, **SAP LO** helps manage:

* The foundational structure (plants, stores, departments)
* Master data for consumables, equipment, and assets
* Classifications of materials (e.g., lab chemicals, IT equipment)
* Centralized control for multiple campuses or facilities

---

## 📘 **Related Topics**

* **Plants** – Learn how to convert fractions into decimals and percentages, and apply them in everyday situations.
  👉 [Learn more](#)
