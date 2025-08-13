---
layout: page
title: "DType in SAP SLCM Courses: Meaning, Purpose, and Step-by-Step Creation Guide"
description: Learn what DType (Delivery Type) means in SAP Student Lifecycle Management (SLCM) courses, why it’s important for academic scheduling, and how to create a new DType in SAP GUI with step-by-step instructions.
keywords: SAP SLCM DType, SAP Delivery Type, DType in courses, SAP course delivery type, SAP SLCM tutorial, how to create DType in SAP, SAP academic structure, SAP course scheduling, SAP lecture type, SAP lab type
author: Muhammad Yasir Bhutta
course: sap-education-reasearch
topic: sap-eam
toc: toc/sap-education-research.html
show_toc: yes
prev: /sap-education-research/docs/sap-scm/
next: /sap-education-research/docs/sap-fiori/
breadcrumb:
  - title: Home
    url: /
  - title: SAP
    url: /sap-education-research/
---

## Table of Contents

1. [What is DType in SLCM Courses?](#1-what-is-dtype-in-slcm-courses)
2. [Why we use DType in courses?](#2-why-we-use-dtype-in-courses)


In **SAP SLCM**, **DType** = **Delivery Type** for a course.
It specifies *how* a course is delivered or conducted.

---

## **1. What is DType in SLCM Courses?**

In SAP’s academic structure:

* **Module** = a subject or course unit (e.g., *Mathematics 101*).
* **DType (Delivery Type)** = the *form* or *method* in which that course is delivered.

Examples of Delivery Types (DTypes):

| DType Code | Meaning          |
| ---------- | ---------------- |
| LEC        | Lecture          |
| LAB        | Laboratory       |
| TUT        | Tutorial         |
| SEM        | Seminar          |
| PRJ        | Project Work     |
| EXM        | Examination-only |

---

## **2. Why we use DType in courses?**

We define DType so SAP knows:

1. **Teaching Method** – to distinguish lectures, labs, tutorials, etc.
2. **Scheduling Rules** – e.g., a lab might require equipment and fewer students per group.
3. **Capacity Planning** – different DTypes may have different room size or resource needs.
4. **Reporting & Analytics** – administrators can count hours or sessions by delivery type.

Example:
If "Physics 101" has:

* Lecture (DType = LEC, 3 hours/week)
* Lab (DType = LAB, 2 hours/week)
  then SAP will treat them as separate delivery items under the same module.

---

## **3. How to Create a DType in SAP GUI**

