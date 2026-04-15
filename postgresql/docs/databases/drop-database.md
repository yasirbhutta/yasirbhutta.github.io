## 3. Dropping a Database
The `DROP DATABASE` command permanently removes a database, its schemas, and all its data. **This action is irreversible.**

**Syntax:**
```sql
DROP DATABASE database_name;
```

**Safety Features:**
* **IF EXISTS:** To prevent an error if the database doesn't exist, use:
    `DROP DATABASE IF EXISTS database_name;`
* **Force Disconnection:** In modern PostgreSQL versions, you can add `WITH (FORCE)` to kick out active users and proceed with the deletion:
    `DROP DATABASE database_name WITH (FORCE);`

---