---
layout: page
title: "What is Structured Service Procurement in SAP"
description: Learn about Structured Service Procurement in SAP
keywords: structure service procurement, procurement, service in sap, material in sap
author: Muhammad Yasir Bhutta
course: sap-education-reasearch
topic: sap-mm
toc: toc/sap-education-research.html
prev: /sap-education-research/docs/sap-mm/
next: /sap-education-research/docs/sap-ps/
breadcrumb:
  - title: Home
    url: /
  - title: SAP
    url: /sap-education-research/
  - title: MM
    url: /sap-education-research/docs/sap-mm/
  - title: Material Types
    url: /sap-education-research/docs/sap-mm/material-types.html
---

## 🏗️ What is **Structured Service Procurement** in SAP?

**Structured service procurement** refers to the **organized and detailed way** of purchasing external services in SAP. Instead of just buying a service as a single line item (like "Consulting – 10 hours"), structured procurement uses a **hierarchical service specification** to define **what exactly is being done**, **how much**, and **at what rate**.

---

### ✅ Key Features of Structured Service Procurement:

| Feature                    | Description                                                                        |
| -------------------------- | ---------------------------------------------------------------------------------- |
| **Service Specifications** | A **detailed breakdown** of services into tasks, quantities, units, and prices.    |
| **Outline Structure**      | Uses a **hierarchical structure** (outline levels) to organize services logically. |
| **Service Master Records** | Reusable service definitions (e.g., "Installation per hour", "Wiring per meter").  |
| **Service Entry Sheets**   | Actual performed services are confirmed using `ML81N` based on service specs.      |
| **Item Category "D"**      | In Purchase Orders, item category **D = Service** is used to trigger this process. |

---

### 🛠 Example:

Instead of:

* **"Construction Work – \$10,000"**

You define:

1. Earthwork – 50 m³ – \$15/m³
2. Foundation – 20 m³ – \$100/m³
3. Wall construction – 30 m² – \$50/m²

This allows:

* Transparent billing
* Easier verification
* Better control and audit

![structure service](/assets/images/sap/structured-service.png)

---

### 🔄 Difference From Unstructured (Simple) Service Procurement:

| Feature                | **Structured**              | **Unstructured**         |
| ---------------------- | --------------------------- | ------------------------ |
| Service Detail         | Detailed line items (specs) | Single general line item |
| Reusability            | Uses service master records | Ad-hoc descriptions      |
| Entry Sheet Validation | Based on service specs      | Manual validation        |
| SAP Material Type Used | `SERV`                      | `DIEN`                   |

---

