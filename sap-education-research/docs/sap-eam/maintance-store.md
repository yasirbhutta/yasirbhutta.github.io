---
layout: page
title: "SAP EAM Maintenance Store Setup and Usage Guide for Universities"
description: Learn how to set up and manage a maintenance store in SAP EAM for universities. Includes step-by-step order processing, material reservation, and inventory integration using MM module.
keywords: SAP EAM maintenance store, SAP PM for universities, maintenance order process SAP, SAP EAM tutorial, SAP storage location, SAP IW31 example, university maintenance SAP, SAP MM integration, SAP spare parts management, SAP MIGO 261, SAP material reservation, SAP PM work order process
author: Muhammad Yasir Bhutta
course: sap-education-reasearch
topic: sap-eam
toc: toc/sap-education-research.html
show_toc: yes
prev: /sap-education-research/
next: /sap-education-research/docs/sap-fico/
breadcrumb:
  - title: Home
    url: /
  - title: SAP
    url: /sap-education-research/
  - title: EAM
    url: /sap-education-research/docs/sap-eam/
---

## Table of Contents

1. [Maintenance Store in SAP EAM](#1-️-maintenance-store-in-sap-eam)
2. [SAP Integration (EAM + MM)](#2--sap-integration-eam--mm)
3. [Example Flow (Maintenance Store Usage)](#3--example-flow-maintenance-store-usage)
4. [Example Flow: Maintenance Store Usage in SAP EAM](#4--example-flow-maintenance-store-usage-in-sap-eam)

## 1. 🛠️ **Maintenance Store in SAP EAM**

In SAP EAM, a **Maintenance Store** refers to the **storage location** or **warehouse** from which spare parts, tools, and materials are issued for maintenance work (e.g., corrective, preventive, or shutdown maintenance).

### 🔑 Key Concepts:

| Concept                     | Description                                                                         |
| --------------------------- | ----------------------------------------------------------------------------------- |
| **Plant**                   | Organizational unit for production/maintenance                                      |
| **Storage Location (Sloc)** | Subdivision of a plant that contains inventory (e.g., a physical maintenance store) |
| **Material Master**         | Includes data for spare parts, tools, etc.                                          |
| **Bill of Material (BOM)**  | List of components required for equipment                                           |
| **Reservation**             | Created to block materials for work orders                                          |
| **Goods Issue (GI)**        | Posting to reduce inventory when materials are used                                 |

---

## 2. 🔄 **SAP Integration (EAM + MM)**

SAP EAM integrates with **Materials Management (MM)** to handle inventory processes:

| Activity                     | SAP Transaction                                         |
| ---------------------------- | ------------------------------------------------------- |
| Create Maintenance Order     | `IW31`                                                  |
| Add Components (Spare Parts) | In order components tab                                 |
| Create Material Reservation  | Auto or manual (via `MB21`)                             |
| Goods Issue from Store       | `MB1A`, `MIGO`, or via order release                    |
| Stock Overview               | `MMBE`                                                  |
| Material Master Display      | `MM03`                                                  |
| Storage Location Creation    | `OMJJ`, `SPRO` config under MM > Inventory Management > |

---

## 3. 🧾 **Example Flow (Maintenance Store Usage)**

1. **Engineer creates Work Order** (`IW31`)
2. **Planner adds spare parts** to the components tab (materials stored in a specific storage location)
3. System **automatically creates a reservation**
4. Storekeeper views reservations (`MB25`) and issues materials (`MIGO`, movement type 261)
5. **Material consumption is posted** against the order

---

## 4. 🧾 Example Flow: Maintenance Store Usage in SAP EAM

**Context**: A university's Engineering Department reports a broken lab projector. The Maintenance Department uses SAP EAM to plan, execute, and track the repair using materials from the university maintenance store.

---

### 🧱 Step 1: Create a Maintenance Notification

* **T-Code**: `IW21`
* **Purpose**: Record the issue (e.g., "Projector in Lab 204 is not working.")
* **Notification Type**: Breakdown / Corrective

🖊️ *Note: Can be created by lab staff, facility coordinator, or helpdesk.*

---

### 🛠️ Step 2: Create a Maintenance Order

* **T-Code**: `IW31`
* **Order Type**: PM01 (Corrective Maintenance)
* **Functional Location**: LAB-ENGG-BLOCK/LAB204
* **Equipment**: LAB-PROJECTOR-204
* **Planner Group**: Facilities Maintenance
* **Work Center**: Electricians or IT Services

---

### 🧩 Step 3: Add Components (Materials Required)

In the Components tab:

* Material 1: **HDMI Cable** – 10 meters
* Material 2: **Projector Lamp** – 1 unit
* Set the **Storage Location**: `MT01` (University Main Maintenance Store)

📌 *SAP creates a reservation automatically for these materials.*

---

### 📦 Step 4: Reservation & Goods Issue

* **T-Code for Reservation Display**: `MB25`
* **T-Code for Goods Issue**: `MIGO` or `MB1A`

  * Movement Type: `261` (Goods Issue to Order)
  * Reference: Maintenance Order number
* Storekeeper issues materials from the store (`MT01`) and hands them to the technician.

---

### 🔧 Step 5: Perform the Maintenance Work

* Technician repairs the projector using the parts
* Order status updated (e.g., from "REL" to "TECO" – technically complete)

---

### 📊 Step 6: Close and Analyze

* **Cost Tracking**: Material & labor costs are posted to internal cost centers (e.g., "Maintenance - Science Block")
* **Reports**: `IW39`, `IW38` for order status and analysis
* **Stock Analysis**: `MMBE` for inventory overview

---

## ✅ Benefits for the University

* Transparency in material usage
* Better inventory control for maintenance items
* Historical maintenance data for campus assets
* Integration with budgeting and procurement

---
### ✅ Tips for Maintenance Store Setup

* **Define separate storage locations** for maintenance departments (e.g., `MT01`, `MT02`)
* Keep **non-stock and consumable materials** managed via `NLAG` material type
* Ensure **accurate Material Master data** (e.g., base unit, valuation class)
* **Link storage location** to maintenance plant in config (`SPRO` > Plant Maintenance and Customer Service > Maintenance and Service Processing > Maintenance and Service Orders > Functions and Settings...)

---

