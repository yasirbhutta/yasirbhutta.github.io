---
layout: page
title: "How to Change User Password in SAP GUI – Step-by-Step Guide"
description: Learn how to change your user password in SAP GUI with this easy, step-by-step guide. Includes instructions for both standard password change and using transaction SU01. Perfect for SAP beginners, users, and administrators in education and research.
keywords: change SAP password, SAP GUI password change, SAP SU01 password, SAP user guide, SAP password reset, SAP login help, SAP for beginners, SAP administration, SAP education, SAP
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

## Table of Contents

1. [Change Password in SAP GUI](#1--change-password-in-sap-gui)
2. [Change Password Using SU01 in SAP GUI](#2--change-password-using-su01-in-sap-gui)
   
---

## 1. 🔧 **Change Password in SAP GUI**

To change your password in **SAP GUI**, follow these steps:

---

### 🔑 Steps to Change Password in SAP GUI:

1. **Open SAP Logon / SAP GUI**

   * Launch the SAP Logon application on your computer.

2. **Select the SAP System**

   * Choose the system you want to log in to (e.g., PRD, DEV) and double-click it.

3. **Log In with Current Credentials**

   * Enter your **User ID** and **current password**.
   * Press **Enter** or click the green checkmark ✅.

4. **Change Password Screen**

   * On the login screen, after entering your user ID and old password, click the **“New Password”** field (if available) or:

   👉 **Go to Menu**: `System` > `User Profile` > `User Data`

   ![sap user data](https://res.cloudinary.com/da0pjikvw/image/upload/v1753961912/change-password1_m9tfef.png)

   👉 Then select **“Password”** button (if inside SAP)

    ![select password](https://res.cloudinary.com/da0pjikvw/image/upload/v1753961912/change-password2_m9kwyh.png)

5. **Enter New Password**

   * Enter the **new password** and **confirm it**.

6. **Save Changes**

   * Click the **Save** icon 💾 or press **Enter**.

---

### 🔒 Password Tips:

* SAP passwords are usually **case-sensitive**.
* Must meet the **minimum length and complexity rules** set by your system administrator (e.g., mix of letters, numbers, symbols).
* You might be forced to change the password at first login if set by admin.

If you have the required **authorizations**, you can change a user's password (including your own) using transaction **SU01** in SAP GUI. Here's how:

---

## 2. 🔧 **Change Password Using SU01 in SAP GUI**

### ✅ **Step-by-Step Guide**:

1. **Open SAP GUI**

   * Log in to your SAP system.

2. **Go to Transaction Code:**

   ```
   SU01
   ```

3. **Enter User ID**

   * In the **User** field, enter the username for which you want to change the password.
   * If changing your own password, enter your user ID or click the **own user** icon.

4. **Click the “Change Password” Button**

   * In the toolbar, click the **Password** icon (🔑 key symbol).
   * Alternatively: Menu bar → **User** → **Change Password**.

5. **Enter New Password**

   * In the popup window:

     * Enter the **new password**.
     * Re-enter it in the **Repeat Password** field.

6. **Save**

   * Click the **green checkmark** ✅ or press **Enter**.

7. **Confirmation**

   * You will see a message like:

     > *Password for user XXXXX has been changed.*

---

### ⚠️ **Important Notes**:

* You need **user administration authorization** to change others' passwords using `SU01`.
* If you do **not** have authorization, you can only change your own password using the regular login method (not SU01).
* SAP password policies (like complexity, reuse rules, expiration) may apply.

---


