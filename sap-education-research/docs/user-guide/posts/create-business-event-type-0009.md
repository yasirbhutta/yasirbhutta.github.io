---
layout: page
title: How to Create a Business Event Type in SAP SLCM | Step-by-Step User Guide
description: Learn how to create a Business Event Type in SAP Student Lifecycle Management (SLCM) using transaction code PV10. Step-by-step user guide with navigation, fields explanation, and tips for scheduling academic and training events.
keywords: SAP SLCM business event type, create business event type SAP, SAP PV10 guide, SAP training and event management, SAP course scheduling, SAP TEM event type, SAP academic structure, SAP student lifecycle management
author: Muhammad Yasir Bhutta
course: sap-education-reasearch
show_practice_progress: false
toc: toc/sap-education-research.html
show_toc: yes
prev: /sap-education-research/
breadcrumb:
  - title: Home
    url: /
  - title: SAP
    url: /sap-education-research/
  - title: SAP User Guides
    url: /sap-education-research/user-guide/
---



## 📖 User Guide: Creating a Business Event Type in SAP SLCM

---

## 1. Purpose

This guide explains how to create a **Business Event Type** in **SAP Student Lifecycle Management (SLCM)**. A Business Event Type serves as a **template** for training sessions, courses, or seminars. Once defined, you can schedule actual events (instances) based on it.

---

## 2. Transaction Code

* **T-Code:** `PV10`
* **Description:** Create Business Event Type

---

## 3. Navigation

* **SAP Easy Access Path:**

  ```
  SAP Easy Access
     → Student Lifecycle Management
        → Academic Structure
           → Study Planning
              → Program Catalog
  ```

---


Here’s a polished and **user-guide ready version** of your section:

---

## 4. Steps to Create a Business Event Type

### Step 1 – Access the Transaction

1. Log in to **SAP GUI**.
2. In the command field, enter **`PIQ_ACSTRUC`** and press **Enter**.
3. In the **Academic Structure** tree, navigate to and select the **Course** for which you want to create the Business Event Type.
4. Right-click the selected course and choose **Create One Level Lower**.
5. From the options, select **Business Event Type**.

---

### Step 2 – Enter Basic Data

1. Fill in the required fields:

   * **Business Event Type ID** → Unique identifier (e.g., MATH101).
   * **Name** → Event type name (e.g., Mathematics 101 Lecture).
   * **Validity Period (From/To)** → Duration this type is valid.

**Sample Business Event Type Details**

- **Category:** General Course
- **Teaching Method:** Class Room
- **Delivery Mode:** Lecture/Theory
- **Appraisal Type:** Final Grade

2. Press **Enter** to continue.

---

### Step 3 – Maintain Event Type Details

1. On the detail screen, enter:

   * **Description** → Longer text description.
   * **Delivery Type (DType)** → Lecture, Seminar, Lab, Workshop, etc.
   * **Organizational Unit** → Responsible department/unit.
   * **Capacity** → Minimum and maximum number of participants.
   * **Language of Instruction**.
   * **Location/Room** (optional).

2. Save your entries (**Ctrl+S** or Save icon).

---

### Step 4 – Verify the Business Event Type

1. Use transaction **PV12 (Display Business Event Type)** to review the details.
2. Optionally, use **PV11 (Change Business Event Type)** to edit if needed.

---

## 5. Result

✅ A new **Business Event Type** has been created.
It can now be used to schedule actual **Business Events** (instances) using **PV01 (Create Business Event)**.

---

## 6. Notes

* **Event Type = Template**
* **Event = Actual Session** (e.g., Math 101 Lecture → Spring 2025 instance).
* Ensure consistency by linking Event Types with the appropriate **Modules/Courses** in Academic Structure.

---
