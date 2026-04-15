PostgreSQL is a powerful, open-source object-relational database system. When managing databases, the primary operations involve creating new storage containers, modifying their metadata, or removing them entirely.

---

## 1. Creating a Database
The `CREATE DATABASE` statement is used to initialize a new database. In PostgreSQL, this essentially copies a template database (usually `template1`) into a new namespace.

**Syntax:**
```sql
CREATE DATABASE database_name;
```

**Key Notes:**
* **Permissions:** You must have the `CREATEDB` privilege or be a superuser.
* **Constraints:** Database names must be unique within the PostgreSQL instance.
* **Standard Practice:** Use lowercase letters and underscores (snake_case) to avoid needing double quotes during queries.

---

### Best Practices
1.  **Always use a semicolon:** PostgreSQL requires `;` to terminate a statement.
2.  **Check your connection:** Use `\l` in the psql terminal to list all databases and verify your changes.
3.  **Snake Case:** Teach students to use `student_records` rather than `Student Records` to avoid syntax errors involving spaces and capitalization.