---
layout: page
title: "How to Upload Biometric Data Using CSV in SAP HCM | Step-by-Step Guide"
description: Learn how to upload biometric data in SAP HCM using a CSV file. Follow this step-by-step guide to prepare, validate, and import employee attendance data efficiently in your SAP system.
keywords: SAP HCM, upload biometric data, CSV upload SAP HCM, SAP HCM attendance, SAP HCM time management, import biometric data, employee attendance SAP, SAP HCM tutorial, HRMS biometric upload, SAP HCM data import
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


## **Step 1: Prepare the CSV File**

1. Collect data from the biometric device.
2. Ensure the CSV contains **mandatory fields**, typically:

   * Employee ID (Personnel Number / PA ID)
   * Date (YYYY-MM-DD)
   * Time (HH:MM)
   * Device ID (if multiple devices)
   * Event type (Check-in / Check-out)
3. Example CSV format:

   ```
   EmployeeID,Date,Time,DeviceID,Event
   1001,2025-11-30,08:30,01,IN
   1002,2025-11-30,08:32,01,IN
   1001,2025-11-30,17:00,01,OUT
   ```
4. Save the file with `.csv` extension and ensure no extra spaces or formatting issues.

---

## **Step 2: Log in to SAP HCM**

1. Open your SAP HCM portal or SAP GUI.
2. Enter your **HR/Admin credentials**.
3. Navigate to **Time Management → Attendance/Work Schedule → Data Upload** (menu paths may vary depending on system configuration).

---

## **Step 3: Access the Upload Tool**

1. Go to the **“Upload Biometric/Attendance Data”** section.
2. Some systems call it:

   * **CATS (Cross-Application Time Sheet) Data Upload**
   * **PA30/PA61 → Attendance Data Upload**
   * **Time Management → Data Transfer → Upload**

ZHCM_TIME_UPLOAD 
ZHCM_ATTR

---

## **Step 4: Upload the CSV File**

1. Click **“Import”** or **“Upload File”**.
2. Browse and select your CSV file.
3. Choose **mapping options**:

   * Map CSV columns to SAP HCM fields (Employee ID → Personnel Number, Date → Date, etc.)
4. Preview the data if your system allows it.

---

## **Step 5: Validate the Data**

1. SAP will perform **validation checks**:

   * Correct employee IDs
   * Valid dates/times
   * Duplicate entries
2. Correct any errors reported by SAP before proceeding.

---

## **Step 6: Import/Confirm**

1. Once validation passes, click **“Submit”** or **“Import”**.
2. SAP will process the records and update the **Time/Attendance database**.

---

## **Step 7: Verify**

1. Randomly check employee records to ensure the biometric data has been correctly uploaded.
2. Generate **attendance or time reports** to confirm accuracy.

---

### **Tips & Best Practices**

* Always **backup the CSV file** before uploading.
* Ensure **employee IDs in CSV match exactly** with SAP Personnel Numbers.
* If uploading large datasets, split the file to avoid system timeout.
* Keep a **log of upload operations** for audit purposes.

---
