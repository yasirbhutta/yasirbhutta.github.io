---
layout: page
title: Fix 'psql' is not recognized on Windows
description: Solutions to fix the 'psql' is not recognized error on Windows by adding PostgreSQL to PATH or reinstalling PostgreSQL with psql.
keywords: psql not recognized, PostgreSQL PATH, Windows environment variables, PostgreSQL installation, pgAdmin, psql windows error
toc: toc/postgresql.html
topic: postgresql
breadcrumb: 
- title: PostgreSQL
  url: /postgresql/
---

You are getting the error:

```
'psql' is not recognized as an internal or external command,
operable program or batch file.
```

This means **PostgreSQL’s bin folder is not added to the Windows PATH**, or PostgreSQL/psql is not installed.

Let’s fix it.

---

# ✅ **Solution 1: Add PostgreSQL to PATH (Most likely fix)**

![Image](https://i.sstatic.net/VUjXU.png)

![Image](https://i.sstatic.net/35YL6.png)

### **Step-by-Step**

1. Find the PostgreSQL installation folder
   Normally located at:

   ```
   C:\Program Files\PostgreSQL\16\bin
   ```

   (or version 15/14 depending on your install)

2. Copy the **bin** folder path
   Example:

   ```
   C:\Program Files\PostgreSQL\16\bin
   ```

3. Add to Windows PATH

   * Press **Windows Key → type "Environment Variables"**
   * Open **Edit the system environment variables**
   * Click **Environment Variables**
   * Under *System variables*, select **Path → Edit**
   * Click **New** → paste the bin path
     (e.g., `C:\Program Files\PostgreSQL\16\bin`)
   * Click **OK**

4. Restart Command Prompt

5. Test again:

   ```
   psql --version
   ```

You should now see something like:

```
psql (PostgreSQL) 16.x
```

---

# ✅ **Solution 2: PostgreSQL is not installed**

If you cannot find the folder:

* Download the official installer:
  [https://www.postgresql.org/download/windows/](https://www.postgresql.org/download/windows/)

Make sure **psql** is selected during installation.

---

# ✅ **Solution 3: Using pgAdmin but psql not installed**

Many users install **pgAdmin 4 only**, not PostgreSQL itself.
pgAdmin does *not* include psql.

In that case, reinstall PostgreSQL using the official installer.

---


