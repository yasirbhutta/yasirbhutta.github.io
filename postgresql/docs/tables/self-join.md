# Student Notes: SELF JOIN in PostgreSQL

## 1. Introduction

In a database, sometimes records in the same table are related to each other.

For example, a university may maintain an employee table containing:

- Employee ID
- Employee Name
- Designation
- Manager ID

A manager is also an employee of the university. Therefore, both employee and manager information is stored in the same table.

How can we display each employee's name along with their manager's name?

We can use a SELF JOIN.

## 2. What is a SELF JOIN?

A SELF JOIN is a technique in which a table is joined with itself.

It allows us to compare or retrieve related records from the same table.

Real-life examples:

- Display employees with their managers.
- Display students with their assigned mentors.
- Display departments with their parent departments.
- Display employees with their supervisors.

Important: SELF JOIN is not a separate JOIN keyword. We use a regular JOIN, such as `INNER JOIN` or `LEFT JOIN`, with two aliases for the same table.

## 3. Prepare a Sample Table

Let's create a table named `employees`.

```
CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY,
    employee_name VARCHAR(100),
    designation VARCHAR(100),
    manager_id INTEGER
);
```

Insert sample records:

```
INSERT INTO employees
(employee_id, employee_name, designation, manager_id)
VALUES
(1, 'Ahmed', 'Director', NULL),
(2, 'Ali', 'Manager', 1),
(3, 'Sara', 'Manager', 1),
(4, 'Usman', 'Developer', 2),
(5, 'Ayesha', 'Developer', 2),
(6, 'Hassan', 'Accountant', 3);
```

View all records:

```
SELECT * FROM employees;
```

Output:

| employee_id | employee_name | designation | manager_id |
| ----------- | ------------- | ----------- | ---------- |
| 1           | Ahmed         | Director    | NULL       |
| 2           | Ali           | Manager     | 1          |
| 3           | Sara          | Manager     | 1          |
| 4           | Usman         | Developer   | 2          |
| 5           | Ayesha        | Developer   | 2          |
| 6           | Hassan        | Accountant  | 3          |

## 4. Understand the Relationship

Look at the `manager_id` column.

- Ahmed has no manager.
- Ali's manager is employee 1 (Ahmed).
- Sara's manager is employee 1 (Ahmed).
- Usman's manager is employee 2 (Ali).
- Ayesha's manager is employee 2 (Ali).
- Hassan's manager is employee 3 (Sara).

The `manager_id` column refers to another employee's `employee_id` in the same table.

[Create organizational chart with Xamarin.iOS Diagram | Syncfusion](https://images.openai.com/static-rsc-4/xOavX1xrZI9S-m6vDfVE0uF4IyI9cH80O5-gHN_qwL7bpWH4tgV_2tSTN1NoIfw1Cysug5niPo6kUKokab7DdcjyYnOLlIv-Ri_eUgMXtynoGA3WqHJ0o-igV-6PaintWKdGI6EwI14NNTNm6zrhgWGCtRBYtS9vZm2A8KOuF6g?purpose=inline)

[syncfusion.com](https://www.syncfusion.com/xamarin-ios-ui-controls/diagram/organizational-chart?utm_source=chatgpt.com)

## 5. Basic SELF JOIN Example

Suppose we want to display employee names along with their manager names.

SQL Query:

```
SELECT
    e.employee_name AS employee,
    m.employee_name AS manager
FROM employees AS e
INNER JOIN employees AS m
ON e.manager_id = m.employee_id;
```

Output:

| employee | manager |
| -------- | ------- |
| Ali      | Ahmed   |
| Sara     | Ahmed   |
| Usman    | Ali     |
| Ayesha   | Ali     |
| Hassan   | Sara    |

Explanation:

1. `employees AS e` creates an alias named `e` for the employee records.
2. `employees AS m` creates another alias named `m` for the manager records.
3. `ON e.manager_id = m.employee_id` matches each employee's manager ID with another employee's ID.
4. `e.employee_name` displays the employee's name.
5. `m.employee_name` displays the manager's name.

Remember: Both `e` and `m` refer to the same `employees` table.

## 6. SELF JOIN Using LEFT JOIN

In the previous example, Ahmed was not displayed because he does not have a manager.

If we want to display all employees, including employees without managers, we can use `LEFT JOIN`.

SQL Query:

```
SELECT
    e.employee_name AS employee,
    m.employee_name AS manager
FROM employees AS e
LEFT JOIN employees AS m
ON e.manager_id = m.employee_id;
```

Output:

| employee | manager |
| -------- | ------- |
| Ahmed    | NULL    |
| Ali      | Ahmed   |
| Sara     | Ahmed   |
| Usman    | Ali     |
| Ayesha   | Ali     |
| Hassan   | Sara    |

Explanation:

- `LEFT JOIN` keeps all employees.
- Matching manager names are displayed.
- If an employee has no manager, the manager column contains NULL.

## 7. SELF JOIN with Designation

We can retrieve additional information from the same table.

Example: Display employee names, their designations, and their manager names.

```
SELECT
    e.employee_name AS employee,
    e.designation AS employee_designation,
    m.employee_name AS manager,
    m.designation AS manager_designation
FROM employees AS e
LEFT JOIN employees AS m
ON e.manager_id = m.employee_id;
```

This query displays:

- Employee name.
- Employee designation.
- Manager name.
- Manager designation.

## 8. SELF JOIN with WHERE

We can use the `WHERE` clause to filter SELF JOIN results.

Example: Display employees who report to Ahmed.

```
SELECT
    e.employee_name AS employee,
    m.employee_name AS manager
FROM employees AS e
INNER JOIN employees AS m
ON e.manager_id = m.employee_id
WHERE m.employee_name = 'Ahmed';
```

Output:

| employee | manager |
| -------- | ------- |
| Ali      | Ahmed   |
| Sara     | Ahmed   |

Explanation:

- The SELF JOIN matches employees with their managers.
- The WHERE clause selects only those records where the manager's name is Ahmed.

## 9. Difference Between Regular JOIN and SELF JOIN

| Regular JOIN                                                | SELF JOIN                                                         |
| ----------------------------------------------------------- | ----------------------------------------------------------------- |
| Joins two or more different tables.                         | Joins a table with itself.                                        |
| Usually combines related information from different tables. | Retrieves related records within the same table.                  |
| Uses aliases when useful.                                   | Uses aliases to distinguish the two references to the same table. |

## 10. Important Points to Remember

1. SELF JOIN joins a table with itself.
2. It uses the same table more than once in a query.
3. Table aliases make it easier to distinguish between the two references.
4. SELF JOIN can use `INNER JOIN` or `LEFT JOIN`.
5. A common use is displaying employees and their managers.
6. The join condition identifies the relationship between records.

## 11. Practice Exercises

Use the `employees` table to solve the following exercises.

Beginner Level

1. Display employee names with their manager names using INNER JOIN.
2. Display all employees with their manager names using LEFT JOIN.
3. Display employee names and manager names using table aliases.

Intermediate Level

4. Display employees who report to Ahmed.
5. Display employees who report to Ali.
6. Display employee names, employee designations, and manager designations.
7. Display only employees whose manager is also a Manager.

Advanced Level

8. Display all employees, including those without managers, sorted alphabetically by employee name.
9. Display the employee ID, employee name, manager ID, and manager name.
10. Count how many employees report to each manager.

## 12. Review Questions

1. What is a SELF JOIN?
2. Why do we use SELF JOIN?
3. Does SELF JOIN require two different tables?
4. Why do we use aliases in SELF JOIN?
5. What is the purpose of `e.manager_id = m.employee_id`?
6. What is the difference between INNER JOIN and LEFT JOIN in SELF JOIN?
7. Can we use WHERE with SELF JOIN?
8. Give two real-life examples of SELF JOIN.

## 13. Quick Revision

Basic SELF JOIN:

```
SELECT
    e.employee_name AS employee,
    m.employee_name AS manager
FROM employees AS e
INNER JOIN employees AS m
ON e.manager_id = m.employee_id;
```

SELF JOIN with LEFT JOIN:

```
SELECT
    e.employee_name AS employee,
    m.employee_name AS manager
FROM employees AS e
LEFT JOIN employees AS m
ON e.manager_id = m.employee_id;
```

## 14. Next Lesson

Subqueries in PostgreSQL

Learn how to write a query inside another query to retrieve information, such as finding students whose fees are higher than the average student fee.