---
layout: page
title: "PM Notification in SAP EAM | Step-by-Step Guide"
description: Learn how to create PM notifications in SAP EAM using IW21. Step-by-step guide with types, process flow, and key benefits for maintenance management.
keywords: create PM notification in SAP, SAP EAM notification process, SAP IW21 transaction, SAP PM notification types, maintenance request in SAP, malfunction report SAP PM, SAP plant maintenance guide, SAP PM notification tutorial
author: Muhammad Yasir Bhutta
course: sap-education-reasearch
topic: sap-eam
toc: toc/sap-education-research.html
show_toc: yes
prev: /sap-education-research/
next: /sap-education-research/docs/sap-fico/
breadcrumb: 
- title: EAM
url: /sap-education-research/docs/sap-eam/
---

In **SAP EAM (Enterprise Asset Management)**, a **PM Notification** is the formal way to record and communicate an issue, malfunction, or maintenance requirement related to a technical object (like equipment, functional location, or asset).

👉 **Creating a PM Notification** means generating a record in the system that captures details about a maintenance event or request.

### Purpose of PM Notification

* To **report malfunctions** or damage.
* To **request maintenance work** (corrective, preventive, predictive).
* To **document inspection findings**.
* To **track breakdowns** and downtime.
* To **initiate follow-up maintenance orders**.

### Types of PM Notifications

1. **M1 – Maintenance Request**

   * Raised when a user notices a problem and requests maintenance.
2. **M2 – Malfunction Report**

   * Raised to record equipment failure or breakdown.
3. **M3 – Activity Report**

   * Records activities carried out without creating a full work order.
4. **Q1 – Quality Notification**

   * Reports quality-related issues (sometimes integrated with QM).

### Key Steps in **Creating a PM Notification**

1. Go to transaction **IW21** (Create Notification).
2. Select the **notification type** (e.g., M1, M2, M3).
3. Enter:

   * **Technical object** (equipment or functional location).
   * **Description of problem** (symptoms, cause if known).
   * **Damage codes & cause codes** (classification of issue).
   * **Priority** (low, medium, high).
   * **Breakdown details** (start/end times if equipment failed).
4. Save the notification → SAP generates a unique **Notification Number**.

### Outcomes of PM Notification

* Used by planners to **analyze and plan work orders**.
* Can be linked to a **maintenance order** for execution.
* Provides **history and reporting** for asset reliability analysis.

⚙️ **Transactions involved**:

* **IW21** → Create PM Notification
* **IW22** → Change PM Notification
* **IW23** → Display PM Notification


