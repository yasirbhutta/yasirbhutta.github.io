---
layout: page
title: "SAP PS (Project System) Guide 2025 - Project Management, WBS & Cost Control"
description: Master SAP PS for end-to-end project management - from WBS creation to profitability analysis. Learn key structures, integration with SAP FICO/MM, and real-world implementation examples.
keywords: SAP PS, SAP Project System, WBS in SAP, SAP project management, SAP PS vs PPM, SAP project costing, SAP PS configuration, SAP PS reports, SAP network activities, SAP PS integration, SAP PS certification, SAP PS training, SAP project budgeting, SAP milestone trend analysis, SAP PS transaction codes 
author: Muhammad Yasir Bhutta
course: sap-education-reasearch
topic: sap-eam
toc: toc/sap-education-research.html
show_toc: yes
prev: /sap-education-research/docs/sap-mm/
next: /sap-education-research/docs/sap-scm/
breadcrumb:
  - title: Home
    url: /
  - title: SAP
    url: /sap-education-research/
---

### 📊 What is **SAP PS (Project System)?**

**SAP PS (Project System)** is a module designed for **planning, executing, and monitoring projects** of any size and complexity. It provides detailed tracking of **costs, resources, timelines, and tasks**, making it essential for **research projects, campus development, and grant-funded initiatives** in education and research institutions.

---

## 🎓 SAP PS in Education and Research

Universities, colleges, and research organizations use SAP PS to:

* **Manage research grants and funding programs**
* **Track costs and progress** of campus infrastructure projects (labs, hostels, IT upgrades)
* **Coordinate collaborative projects** across departments or with external partners
* **Ensure financial control and reporting** for each project

---

## 🔑 Key Features of SAP PS

| Feature                                 | Description                                                                                                          |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Project Structuring (WBS, Networks)** | Create a Work Breakdown Structure (WBS) to represent tasks and phases. Use Networks to manage time and dependencies. |
| **Budgeting & Cost Planning**           | Allocate budgets and plan expected costs. Control overspending via integration with SAP FM/FICO.                     |
| **Project Execution & Monitoring**      | Track project milestones, deadlines, and progress through real-time updates.                                         |
| **Actual Cost Posting**                 | Capture real expenses like salaries, procurement, and services.                                                      |
| **Resource Planning**                   | Assign internal or external resources to project activities.                                                         |
| **Billing & Settlement**                | Settle costs to grants, departments, or external partners.                                                           |
| **Integration**                         | Works with modules like SAP MM (materials), HR (personnel), FI (accounting), and FM (funds).                         |

---

## 🧪 Sample SAP PS Tasks in Education/Research Context

| Task                          | Description                                            | T-Code |
| ----------------------------- | ------------------------------------------------------ | ------ |
| **Create Project Definition** | Define a new research or construction project.         | CJ01   |
| **Create WBS Elements**       | Structure the project into phases or components.       | CJ02   |
| **Plan Project Budget**       | Allocate funds to project tasks.                       | CJ30   |
| **Display Project Plan**      | View the hierarchy and tasks in Gantt chart form.      | CJ20N  |
| **Post Actual Costs**         | Post staff salary, material usage, or service costs.   | KB21N  |
| **Create Network Activities** | Plan activities and dependencies.                      | CN21   |
| **Project Progress Analysis** | Analyze progress and compare planned vs. actual costs. | CNE1   |
| **Settle Project Costs**      | Transfer expenses to a grant or department.            | CJ88   |

---

## 📚 Example Use Case in a University

> The university receives a research grant to build a renewable energy lab.
> A project is created using **CJ01**, with WBS elements for **design, procurement, construction, and testing** using **CJ02**.
> Budgets are assigned (**CJ30**), and purchase orders are linked via **SAP MM**.
> Actual costs like staff time and vendor payments are posted (**KB21N**), and the project is monitored with **CJ20N** and **CNE1**.
> Once complete, costs are settled to the grant (**CJ88**).

---

## 🔄 Integration with Other Modules

* **SAP FM / GM**: For fund control and grant budgeting
* **SAP MM**: For material procurement in projects
* **SAP FICO**: For posting and tracking financial data
* **SAP HCM**: For assigning human resources to project tasks

---