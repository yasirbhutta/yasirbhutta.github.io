---
layout: page
title: "SAP Logistics – General (LO) Overview: Key Functions, T-Codes, and Use in Universities"
description: Learn about SAP Logistics – General (LO), its core functionalities, integration with MM, SD, PM, and its practical use in universities and non-manufacturing sectors. Includes common T-Codes and examples..
keywords: SAP LO module, SAP Logistics General, SAP LO T-Codes, SAP LO functionalities, SAP LO for universities, SAP LO integration MM SD PM, SAP LO document management, SAP classification system, SAP enterprise structure, SAP batch management, SAP LO non-manufacturing, SAP LO material master
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

1. [What is SAP Logistics – General (LO)?](#1--what-is-sap-logistics--general-lo)
2. [Key Functionalities of SAP LO](#2--key-functionalities-of-sap-lo)
3. [Integration with Other SAP Modules](#3--integration-with-other-sap-modules)
4. [Common LO T-Codes](#4-️-common-lo-t-codes)
5. [Why SAP LO Matters in a University or Non-Manufacturing Setup](#5-️-why-sap-lo-matters-in-a-university-or-non-manufacturing-setup)
   
## 1. 📦 **What is **SAP Logistics – General (LO)?**

**SAP Logistics – General (LO)** is a **core component of SAP ERP** that provides **foundational logistics functions** used by other SAP logistics modules like:

* **[MM (Materials Management)](../sap-mm/**
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

* **What is Plant** – In **SAP ERP**, a **Plant** is a **central organizational unit** within logistics used to manage operations such as **procurement**, **production**, **maintenance**, **inventory**, and **services**.
  👉 [Learn more](plants.md)
