---
layout: page
title: Fix 'psql' is not recognized on Windows
description: Solutions to fix the 'psql' is not recognized error on Windows by adding PostgreSQL to PATH or reinstalling PostgreSQL with psql.
keywords: psql not recognized, PostgreSQL PATH, Windows environment variables, PostgreSQL installation, pgAdmin, psql windows error
---

---

# ✅ Method 1: Using `CREATE DATABASE ... WITH TEMPLATE` (Easiest)

This is the **fastest and recommended way**.

### Syntax:

```sql
CREATE DATABASE new_db_name
WITH TEMPLATE old_db_name
OWNER your_user;
```

### Example:

```sql
CREATE DATABASE school_copy
WITH TEMPLATE school
OWNER postgres;
```

### ⚠️ Important Notes:

* No one should be connected to the **source database**
* You must be a **superuser** or owner
* Works best for small to medium databases

### To disconnect users:

```sql
SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE datname = 'school';
```

---


