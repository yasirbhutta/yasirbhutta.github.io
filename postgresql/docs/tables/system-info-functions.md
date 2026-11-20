# Student Notes: System and Information Functions in PostgreSQL

## 1. Introduction

In PostgreSQL, we sometimes need information about the database system rather than the records stored in tables.

For example, a database administrator may need to know:

- Which database is currently connected?
- Which user is currently logged in?
- Which schema is being used?
- What is the PostgreSQL server version?
- What is the current date and time?
- Which session is currently active?

PostgreSQL provides built-in system and information functions to retrieve this information.

## 2. What Are System and Information Functions?

System and information functions are built-in PostgreSQL functions that provide information about the database, server, users, sessions, and current environment.

Example:

```
SELECT CURRENT_DATABASE();
```

This query returns the name of the currently connected database.

## 3. CURRENT_DATABASE()

The `CURRENT_DATABASE()` function returns the name of the database to which the current session is connected.

Example:

```
SELECT CURRENT_DATABASE();
```

Possible output:

```
dvdrental
```

The result depends on your current database connection.

Practical use: Check whether you are connected to the correct database before running queries.

## 4. CURRENT_USER

`CURRENT_USER` returns the name of the current database user.

Example:

```
SELECT CURRENT_USER;
```

Possible output:

```
postgres
```

The result depends on the account used to connect to PostgreSQL.

You can also use:

```
SELECT CURRENT_USER AS logged_in_user;
```

## 5. SESSION_USER

`SESSION_USER` returns the database user who originally established the current session.

Example:

```
SELECT SESSION_USER;
```

### Difference Between CURRENT_USER and SESSION_USER

| Expression     | Purpose                         |
| -------------- | ------------------------------- |
| `CURRENT_USER` | Current effective database user |
| `SESSION_USER` | User who originally connected   |

Usually, both return the same value. They can differ when PostgreSQL changes the effective role, for example through `SET ROLE`.

## 6. CURRENT_SCHEMA()

The `CURRENT_SCHEMA()` function returns the name of the first schema in the current search path.

Example:

```
SELECT CURRENT_SCHEMA();
```

Possible output:

```
public
```

The result depends on your search path.

Practical use: Check which schema PostgreSQL will search first when resolving unqualified table names.

## 7. CURRENT_SCHEMAS()

The `CURRENT_SCHEMAS()` function returns the schemas included in the current search path.

Example:

```
SELECT CURRENT_SCHEMAS(TRUE);
```

The argument `TRUE` includes implicit schemas such as `pg_catalog` and `pg_temp` when applicable.

Another example:

```
SELECT CURRENT_SCHEMAS(FALSE);
```

This excludes implicit schemas.

## 8. VERSION()

The `VERSION()` function returns information about the PostgreSQL server version and build.

Example:

```
SELECT VERSION();
```

Possible output:

```
PostgreSQL 17.x ...
```

The exact output depends on the installed PostgreSQL version and operating environment.

Practical use: Check which PostgreSQL version is running on the server.

## 9. CURRENT_DATE

`CURRENT_DATE` returns the current date.

Example:

```
SELECT CURRENT_DATE;
```

Possible output:

```
2026-11-09
```

The output depends on the current date.

You can also use an alias:

```
SELECT CURRENT_DATE AS today;
```

## 10. CURRENT_TIME

`CURRENT_TIME` returns the current time, including the time zone offset.

Example:

```
SELECT CURRENT_TIME;
```

You can also specify the number of fractional seconds:

```
SELECT CURRENT_TIME(0);
```

Here, `0` means that fractional seconds are omitted.

## 11. CURRENT_TIMESTAMP

`CURRENT_TIMESTAMP` returns the date and time at the start of the current transaction, including the time zone offset.

Example:

```
SELECT CURRENT_TIMESTAMP;
```

You can also use:

```
SELECT CURRENT_TIMESTAMP(0);
```

This returns the timestamp without fractional seconds.

Important: `CURRENT_TIMESTAMP` remains the same throughout a transaction. It does not continuously update with the clock.

## 12. NOW()

The `NOW()` function also returns the date and time at the start of the current transaction.

Example:

```
SELECT NOW();
```

`NOW()` and `CURRENT_TIMESTAMP` provide equivalent transaction-start timestamps.

## 13. LOCALTIME and LOCALTIMESTAMP

These expressions return the current time or timestamp without a time zone.

### LOCALTIME

```
SELECT LOCALTIME;
```

Returns the current local time without a time zone.

### LOCALTIMESTAMP

```
SELECT LOCALTIMESTAMP;
```

Returns the current date and time without a time zone.

Comparison:

| Expression          | Returns                             |
| ------------------- | ----------------------------------- |
| `CURRENT_DATE`      | Current date                        |
| `CURRENT_TIME`      | Current time with time zone         |
| `LOCALTIME`         | Current time without time zone      |
| `CURRENT_TIMESTAMP` | Current timestamp with time zone    |
| `LOCALTIMESTAMP`    | Current timestamp without time zone |
| `NOW()`             | Current transaction timestamp       |

## 14. PG_BACKEND_PID()

The `PG_BACKEND_PID()` function returns the process ID of the PostgreSQL server process handling the current session.

Example:

```
SELECT PG_BACKEND_PID();
```

Possible output:

```
12345
```

The number is an example; the actual process ID will be different.

Practical use: Identify the server process associated with your current database connection.

## 15. PG_POSTMASTER_START_TIME()

The `PG_POSTMASTER_START_TIME()` function returns the date and time when the PostgreSQL server was started.

Example:

```
SELECT PG_POSTMASTER_START_TIME();
```

This can help database administrators check when the server was last started.

## 16. PG_CONF_LOAD_TIME()

The `PG_CONF_LOAD_TIME()` function returns the time when the server configuration files were last loaded.

Example:

```
SELECT PG_CONF_LOAD_TIME();
```

This is useful when checking whether configuration changes have been reloaded.

## 17. PG_IS_IN_RECOVERY()

The `PG_IS_IN_RECOVERY()` function checks whether the PostgreSQL server is currently operating in recovery mode.

Example:

```
SELECT PG_IS_IN_RECOVERY();
```

Possible results:

- `TRUE`: The server is in recovery or standby mode.
- `FALSE`: The server is not in recovery mode.

This function is mainly useful for database administration and replication environments.

## 18. CURRENT_SETTING()

The `CURRENT_SETTING()` function retrieves the current value of a PostgreSQL configuration parameter.

Syntax:

```
CURRENT_SETTING('parameter_name')
```

Example 1:

```
SELECT CURRENT_SETTING('server_version');
```

This returns the PostgreSQL server version setting.

Example 2:

```
SELECT CURRENT_SETTING('TimeZone');
```

This returns the current session time zone setting.

Example 3:

```
SELECT CURRENT_SETTING('search_path');
```

This returns the current schema search path.

## 19. SHOW Command

PostgreSQL also provides the `SHOW` command to display configuration settings.

Example:

```
SHOW server_version;
```

Display the current time zone:

```
SHOW TimeZone;
```

Display the search path:

```
SHOW search_path;
```

Difference:

- `CURRENT_SETTING()` is a function that retrieves a setting.
- `SHOW` is a SQL command that displays a setting.

## 20. PG_TABLE_SIZE()

The `PG_TABLE_SIZE()` function returns the disk space used by a table, excluding its indexes.

Syntax:

```
PG_TABLE_SIZE('table_name')
```

Example:

```
SELECT PG_TABLE_SIZE('film');
```

The result is returned in bytes.

For a more readable result, use `PG_SIZE_PRETTY()`:

```
SELECT PG_SIZE_PRETTY(
    PG_TABLE_SIZE('film')
);
```

Possible output:

```
96 kB
```

The actual result depends on the table contents and storage.

## 21. PG_TOTAL_RELATION_SIZE()

The `PG_TOTAL_RELATION_SIZE()` function returns the total disk space used by a table, including its indexes and associated storage.

Example:

```
SELECT PG_TOTAL_RELATION_SIZE('film');
```

Display the size in a readable format:

```
SELECT PG_SIZE_PRETTY(
    PG_TOTAL_RELATION_SIZE('film')
);
```

## 22. PG_DATABASE_SIZE()

The `PG_DATABASE_SIZE()` function returns the total disk space used by a database.

Example:

```
SELECT PG_DATABASE_SIZE(CURRENT_DATABASE());
```

Display the size in a readable format:

```
SELECT PG_SIZE_PRETTY(
    PG_DATABASE_SIZE(CURRENT_DATABASE())
);
```

Practical use: Database administrators can monitor database storage requirements.

## 23. PG_SIZE_PRETTY()

The `PG_SIZE_PRETTY()` function converts a size in bytes into a human-readable format.

Example:

```
SELECT PG_SIZE_PRETTY(1024);
```

Possible output:

```
1 kB
```

Another example:

```
SELECT PG_SIZE_PRETTY(1048576);
```

Possible output:

```
1 MB
```

## 24. Combining System Functions in One Query

We can use several system functions in a single SQL query.

Example:

```
SELECT
    CURRENT_DATABASE() AS database_name,
    CURRENT_USER AS current_user,
    CURRENT_SCHEMA() AS current_schema,
    VERSION() AS server_version,
    CURRENT_DATE AS today,
    CURRENT_TIMESTAMP AS current_timestamp;
```

This query displays useful information about the current PostgreSQL environment.

## 25. Practical Examples Using dvdrental

If you are using the PostgreSQL `dvdrental` sample database, try these queries.

### Example 1: Check the Current Database

```
SELECT CURRENT_DATABASE();
```

### Example 2: Check the Current User

```
SELECT CURRENT_USER;
```

### Example 3: Check the Current Schema

```
SELECT CURRENT_SCHEMA();
```

### Example 4: Find the Size of the Film Table

```
SELECT
    PG_SIZE_PRETTY(
        PG_TOTAL_RELATION_SIZE('public.film')
    ) AS film_table_size;
```

### Example 5: Find the Size of the Current Database

```
SELECT
    PG_SIZE_PRETTY(
        PG_DATABASE_SIZE(CURRENT_DATABASE())
    ) AS database_size;
```

## 26. Important Points to Remember

1. `CURRENT_DATABASE()` returns the connected database name.
2. `CURRENT_USER` returns the effective current user.
3. `SESSION_USER` returns the original session user.
4. `CURRENT_SCHEMA()` returns the first schema in the search path.
5. `VERSION()` returns PostgreSQL server version information.
6. `CURRENT_DATE` returns the current date.
7. `NOW()` returns the transaction-start timestamp.
8. `PG_BACKEND_PID()` returns the current session's server process ID.
9. `CURRENT_SETTING()` retrieves a configuration setting.
10. `PG_DATABASE_SIZE()` returns database size in bytes.
11. `PG_SIZE_PRETTY()` converts bytes into a readable size.
12. `SHOW` displays PostgreSQL configuration settings.

## 27. Practice Exercises

### Beginner Level

Exercise 1: Write a query to display the current database name.

Exercise 2: Display the currently logged-in database user.

Exercise 3: Display the current schema.

Exercise 4: Display the PostgreSQL server version.

Exercise 5: Display the current date and time.

### Intermediate Level

Exercise 6: Display the current database, user, and schema in one query.

Exercise 7: Display the current PostgreSQL time zone.

Exercise 8: Display the current search path.

Exercise 9: Find the size of the `film` table in the `dvdrental` database.

Exercise 10: Display the total size of the current database in a readable format.

### Advanced Level

Exercise 11: Display the current session's PostgreSQL process ID.

Exercise 12: Display the time when the PostgreSQL server was started.

Exercise 13: Check whether the PostgreSQL server is in recovery mode.

Exercise 14: Display the current configuration reload time.

Exercise 15: Write one query that displays the database name, current user, schema, server version, date, timestamp, and database size.

## 28. Review Questions

1. What are system and information functions?
2. What is the purpose of `CURRENT_DATABASE()`?
3. What is the difference between `CURRENT_USER` and `SESSION_USER`?
4. What does `VERSION()` return?
5. What is the difference between `CURRENT_DATE` and `CURRENT_TIMESTAMP`?
6. What is the purpose of `PG_BACKEND_PID()`?
7. What does `CURRENT_SETTING()` do?
8. What is the difference between `PG_TABLE_SIZE()` and `PG_TOTAL_RELATION_SIZE()`?
9. Why do we use `PG_SIZE_PRETTY()`?
10. What is the purpose of the `SHOW` command?

## 29. Quick Revision

| Function / Expression        | Purpose                        |
| ---------------------------- | ------------------------------ |
| `CURRENT_DATABASE()`         | Current database name          |
| `CURRENT_USER`               | Current effective user         |
| `SESSION_USER`               | Original session user          |
| `CURRENT_SCHEMA()`           | Current schema                 |
| `CURRENT_SCHEMAS()`          | Schemas in search path         |
| `VERSION()`                  | PostgreSQL version information |
| `CURRENT_DATE`               | Current date                   |
| `CURRENT_TIME`               | Current time with time zone    |
| `CURRENT_TIMESTAMP`          | Transaction-start timestamp    |
| `NOW()`                      | Transaction-start timestamp    |
| `PG_BACKEND_PID()`           | Current session process ID     |
| `PG_POSTMASTER_START_TIME()` | Server start time              |
| `CURRENT_SETTING()`          | Configuration setting value    |
| `PG_TABLE_SIZE()`            | Table size excluding indexes   |
| `PG_TOTAL_RELATION_SIZE()`   | Table size including indexes   |
| `PG_DATABASE_SIZE()`         | Database size                  |
| `PG_SIZE_PRETTY()`           | Human-readable storage size    |

Next Lesson: PostgreSQL Import and Export

In the next lesson, students will learn how to import data from CSV files into PostgreSQL and export query results or table data into CSV files using pgAdmin and SQL commands.