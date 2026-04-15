## 2. Renaming a Database
To change the name of an existing database, use the `ALTER DATABASE` command. 

**Syntax:**
```sql
ALTER DATABASE old_name RENAME TO new_name;
```

**Important Restrictions:**
* **No Active Connections:** You cannot rename a database while you or anyone else is currently connected to it. You must connect to a different database (like the default `postgres` DB) first.
* **Ownership:** Usually, only the owner of the database or a superuser can rename it.
