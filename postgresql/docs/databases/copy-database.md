
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


