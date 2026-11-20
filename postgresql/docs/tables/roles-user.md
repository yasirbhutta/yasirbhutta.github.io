# Student Notes: PostgreSQL Roles and User Management

## 1. Introduction

In PostgreSQL, different people may need access to the same database.

For example, in a university database:

- An administrator manages the complete database.
- A teacher views student records.
- An admission officer enters admission information.
- A student may only view their own information.

PostgreSQL provides a security system to manage these users and their permissions.

In this lesson, we will learn how to create users, create roles, assign permissions, and control database access.

## 2. What Is a User in PostgreSQL?

A user is an account that can connect to a PostgreSQL server and perform permitted operations.

For example:

- `postgres`
- `teacher_user`
- `admin_user`
- `student_user`

A user normally connects using a username and password.

## 3. What Is a Role in PostgreSQL?

A role is an account or a collection of permissions in PostgreSQL.

PostgreSQL uses roles to manage database access.

A role can:

- Log in to PostgreSQL.
- Create databases.
- Create tables.
- Read records.
- Insert records.
- Update records.
- Delete records.
- Manage other roles, if authorized.

Important: In PostgreSQL, users and groups are both implemented through roles.

The main difference is:

- A role with the `LOGIN` attribute can connect to PostgreSQL.
- A role without `LOGIN` is commonly used to group permissions.

## 4. Creating a User

We can create a user using the `CREATE USER` command.

Syntax:

```
CREATE USER username WITH PASSWORD 'password';
```

Example:

```
CREATE USER teacher_user
WITH PASSWORD 'teacher123';
```

This creates a user named `teacher_user`.

The user can authenticate using the specified password, subject to PostgreSQL connection settings.

## 5. Creating a Role

We can create a role using the `CREATE ROLE` command.

Syntax:

```
CREATE ROLE role_name;
```

Example:

```
CREATE ROLE teachers;
```

This creates a role named `teachers`.

By default, it does not have the `LOGIN` attribute.

We can use this role to group permissions for multiple teachers.

## 6. Creating a Role That Can Log In

We can create a role with the `LOGIN` attribute.

Example:

```
CREATE ROLE teacher_user
WITH LOGIN PASSWORD 'teacher123';
```

This creates a login role.

It is functionally similar to:

```
CREATE USER teacher_user
WITH PASSWORD 'teacher123';
```

Remember: `CREATE USER` is essentially a convenient form of `CREATE ROLE` with `LOGIN`.

## 7. Viewing Existing Roles

PostgreSQL provides commands to view existing roles.

In the `psql` terminal, execute:

```
\du
```

This displays the roles and their attributes.

To view additional details:

```
\du+
```

You can also use an SQL query:

```
SELECT rolname
FROM pg_roles;
```

This displays the names of available roles.

## 8. Assigning a Role to a User

Suppose we have created:

- A user named `teacher_user`.
- A role named `teachers`.

We can assign the `teachers` role to the user.

Command:

```
GRANT teachers TO teacher_user;
```

Now `teacher_user` is a member of the `teachers` role.

The user can use the permissions associated with that role according to PostgreSQL's role-membership rules.

## 9. Removing a Role from a User

We can remove role membership using `REVOKE`.

Syntax:

```
REVOKE role_name FROM username;
```

Example:

```
REVOKE teachers FROM teacher_user;
```

This removes the membership of `teacher_user` in the `teachers` role.

It does not delete the user account.

## 10. Granting Database Access

Creating a user does not automatically give that user access to every database.

We must grant the required permissions.

Suppose we have a database named `university_db`.

Command:

```
GRANT CONNECT ON DATABASE university_db
TO teacher_user;
```

This allows the role to connect to `university_db`, subject to other connection restrictions.

Important: `CONNECT` permission does not automatically allow the user to read or modify tables.

## 11. Granting Permission to Use a Schema

A schema is a logical container for database objects such as tables and views.

Suppose our tables are inside the `public` schema.

We can grant schema access:

```
GRANT USAGE ON SCHEMA public
TO teacher_user;
```

This allows the role to access objects in the schema when it has the necessary object permissions.

## 12. Granting SELECT Permission

The `SELECT` permission allows a user to read data from a table.

Syntax:

```
GRANT SELECT ON TABLE table_name
TO username;
```

Example:

```
GRANT SELECT ON TABLE public.students
TO teacher_user;
```

Now `teacher_user` can read records from the `students` table.

Example query, when connected as `teacher_user`:

```
SELECT *
FROM public.students;
```

## 13. Granting INSERT Permission

The `INSERT` permission allows a user to add new records.

Example:

```
GRANT INSERT ON TABLE public.students
TO teacher_user;
```

Now the user can insert new student records, provided any other required permissions and constraints are satisfied.

## 14. Granting UPDATE Permission

The `UPDATE` permission allows a user to modify existing records.

Example:

```
GRANT UPDATE ON TABLE public.students
TO teacher_user;
```

Now the user can update records in the `students` table.

Example:

```
UPDATE public.students
SET student_name = 'Ali'
WHERE student_id = 101;
```

## 15. Granting DELETE Permission

The `DELETE` permission allows a user to remove records.

Example:

```
GRANT DELETE ON TABLE public.students
TO teacher_user;
```

Now the user can delete records from the `students` table.

Example:

```
DELETE FROM public.students
WHERE student_id = 101;
```

## 16. Granting Multiple Permissions at Once

We can grant multiple permissions in one command.

Example:

```
GRANT SELECT, INSERT, UPDATE
ON TABLE public.students
TO teacher_user;
```

This allows the user to:

- Read records.
- Insert records.
- Update records.

The user does not receive `DELETE` permission.

## 17. Granting All Table Permissions

We can use `ALL PRIVILEGES` to grant all applicable table-level privileges.

Example:

```
GRANT ALL PRIVILEGES
ON TABLE public.students
TO teacher_user;
```

This grants the available table privileges, such as `SELECT`, `INSERT`, `UPDATE`, `DELETE`, and other table-level privileges.

Important: It does not make the user a superuser or automatically grant permissions on every other table.

## 18. Granting Permissions on All Tables in a Schema

Suppose the `public` schema contains many tables.

Instead of granting permissions individually, we can use:

```
GRANT SELECT
ON ALL TABLES IN SCHEMA public
TO teacher_user;
```

This grants `SELECT` permission on all existing tables and views in the schema.

To grant multiple permissions:

```
GRANT SELECT, INSERT, UPDATE
ON ALL TABLES IN SCHEMA public
TO teacher_user;
```

Important: These commands affect existing objects. They do not automatically grant permissions on tables created in the future.

## 19. Setting Default Permissions for Future Tables

To grant permissions automatically on future tables created by a particular role, use `ALTER DEFAULT PRIVILEGES`.

Example:

```
ALTER DEFAULT PRIVILEGES
IN SCHEMA public
GRANT SELECT
ON TABLES TO teacher_user;
```

This applies to future tables created by the role executing the command.

If a different role creates tables, its default privileges must be configured separately.

## 20. Revoking Permissions

We can remove previously granted permissions using the `REVOKE` command.

Syntax:

```
REVOKE permission_name
ON TABLE table_name
FROM username;
```

Example:

```
REVOKE INSERT
ON TABLE public.students
FROM teacher_user;
```

This removes the `INSERT` permission from `teacher_user` on the `students` table.

To remove multiple permissions:

```
REVOKE INSERT, UPDATE
ON TABLE public.students
FROM teacher_user;
```

## 21. Changing a User's Password

We can change a user's password using `ALTER ROLE`.

Syntax:

```
ALTER ROLE username
WITH PASSWORD 'new_password';
```

Example:

```
ALTER ROLE teacher_user
WITH PASSWORD 'newTeacher456';
```

This changes the password of `teacher_user`.

## 22. Renaming a User

We can rename an existing role using `ALTER ROLE`.

Example:

```
ALTER ROLE teacher_user
RENAME TO faculty_user;
```

The role is now named `faculty_user`.

Its existing permissions and role memberships remain associated with the renamed role.

## 23. Deleting a User or Role

We can delete a role using `DROP ROLE`.

Syntax:

```
DROP ROLE role_name;
```

Example:

```
DROP ROLE teacher_user;
```

PostgreSQL will not allow the role to be dropped if it still owns database objects or has certain privileges or dependencies.

We may need to transfer ownership or remove dependencies first.

For example, in the appropriate database:

```
REASSIGN OWNED BY teacher_user TO postgres;
```

Then:

```
DROP OWNED BY teacher_user;
```

Finally:

```
DROP ROLE teacher_user;
```

Warning: `DROP OWNED` can remove privileges and drop objects owned by the role in the current database. Use it carefully.

## 24. Understanding Common PostgreSQL Permissions

| Permission   | Purpose                                                        |
| ------------ | -------------------------------------------------------------- |
| `CONNECT`    | Connect to a database                                          |
| `CREATE`     | Create objects in a database or schema, depending on the grant |
| `USAGE`      | Use a schema or certain database objects                       |
| `SELECT`     | Read table data                                                |
| `INSERT`     | Add new records                                                |
| `UPDATE`     | Modify existing records                                        |
| `DELETE`     | Delete records                                                 |
| `TRUNCATE`   | Remove all rows from a table                                   |
| `REFERENCES` | Create foreign key references                                  |
| `TRIGGER`    | Create triggers on a table                                     |

## 25. Practical Example: Creating a Teacher Account

Suppose we want to create a teacher account that can:

- Connect to `university_db`.
- Read student records.
- Insert student records.
- Update student records.
- Not delete student records.

Follow these steps.

Step 1: Create a user

```
CREATE USER teacher_user
WITH PASSWORD 'teacher123';
```

Step 2: Grant database connection permission

```
GRANT CONNECT
ON DATABASE university_db
TO teacher_user;
```

Step 3: Grant schema access

```
GRANT USAGE
ON SCHEMA public
TO teacher_user;
```

Step 4: Grant table permissions

```
GRANT SELECT, INSERT, UPDATE
ON TABLE public.students
TO teacher_user;
```

Step 5: Test the account

Connect to PostgreSQL using `teacher_user` and try:

```
SELECT *
FROM public.students;
```

Then try inserting or updating a record in a test database.

A `DELETE` operation should fail if the user has no other source of `DELETE` permission.

## 26. Important Security Concepts

- Follow the principle of least privilege: give users only the permissions they need.
- Avoid using the `postgres` superuser account for ordinary application work.
- Use strong passwords.
- Do not share database passwords.
- Review user permissions regularly.
- Use separate roles for different responsibilities.
- Test permissions using the actual user account.

## 27. Practice Exercises

### Beginner Level

1. Create a user named `student_user`.
2. Create a role named `students`.
3. Display all PostgreSQL roles.
4. Change the password of `student_user`.
5. Rename `student_user` to `learner_user`.

### Intermediate Level

6. Create a user named `teacher_user`.
7. Grant the user permission to connect to `university_db`.
8. Grant `USAGE` on the `public` schema.
9. Grant `SELECT` permission on the `students` table.
10. Grant `INSERT` and `UPDATE` permissions.
11. Revoke the `UPDATE` permission.
12. Grant `SELECT` permission on all existing tables in the `public` schema.

### Advanced Level

13. Create a role named `faculty`.
14. Create two users and assign both to the `faculty` role.
15. Grant table permissions to the `faculty` role.
16. Test whether both users can use the granted permissions.
17. Configure default privileges for future tables.
18. Remove one user's membership from the `faculty` role.

## 28. Review Questions

1. What is a role in PostgreSQL?
2. What is the difference between a user and a role?
3. Which command creates a user?
4. Which command creates a role?
5. What is the purpose of `GRANT`?
6. What is the purpose of `REVOKE`?
7. What is the difference between `CONNECT` and `SELECT`?
8. How can we change a user's password?
9. How can we assign a role to a user?
10. What is the purpose of `ALTER DEFAULT PRIVILEGES`?

## 29. Quick Revision

| Command                    | Purpose                                    |
| -------------------------- | ------------------------------------------ |
| `CREATE USER`              | Create a login role                        |
| `CREATE ROLE`              | Create a role                              |
| `\du`                      | Display roles in psql                      |
| `GRANT`                    | Assign permissions                         |
| `REVOKE`                   | Remove permissions                         |
| `ALTER ROLE`               | Modify a role                              |
| `DROP ROLE`                | Delete a role                              |
| `GRANT CONNECT`            | Allow database connections                 |
| `GRANT USAGE`              | Allow schema usage                         |
| `GRANT SELECT`             | Allow reading data                         |
| `ALTER DEFAULT PRIVILEGES` | Set default permissions for future objects |

Next Lesson: PostgreSQL Schema Management

Students will learn how to create, rename, alter, delete, and manage schemas, and how schemas organize database objects.