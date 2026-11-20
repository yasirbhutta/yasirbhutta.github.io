# Student Notes: JSON and JSONB in PostgreSQL

## 1. Introduction

Sometimes, database records contain information that is not easily represented using traditional columns.

For example, a university student may have additional information such as:

- Personal contact details
- Address information
- Skills
- Previous qualifications
- Emergency contact information

We can store this information using PostgreSQL's JSON and JSONB data types.

JSON allows us to store structured data in a format similar to JavaScript objects.

For example:

```
{
    "name": "Ali",
    "age": 22,
    "department": "Computer Science"
}
```

This structure contains three properties:

- `name`
- `age`
- `department`

## 2. What Is JSON?

JSON stands for JavaScript Object Notation.

It is a lightweight format used to store and exchange structured data.

JSON stores information using key-value pairs.

Example:

```
{
    "student_id": 101,
    "student_name": "Ali",
    "age": 22,
    "department": "Computer Science"
}
```

In this example:

| Key          | Value            |
| ------------ | ---------------- |
| student_id   | 101              |
| student_name | Ali              |
| age          | 22               |
| department   | Computer Science |

Important: JSON is not limited to JavaScript. PostgreSQL, Python, PHP, Java, and many other technologies support JSON.

## 3. JSON Data Types in PostgreSQL

PostgreSQL provides two data types for storing JSON information:

1. `JSON`
2. `JSONB`

Both store JSON-formatted data, but they work differently.

### JSON

The `JSON` data type stores an exact copy of the input JSON text.

It preserves:

- Original formatting
- Spaces
- Key order
- Duplicate keys in the stored text

### JSONB

The `JSONB` data type stores JSON data in a decomposed binary format.

It provides:

- Efficient searching
- Better indexing support
- Faster processing for many operations
- No preservation of original formatting or key order

Comparison:

| Feature        | JSON                    | JSONB                             |
| -------------- | ----------------------- | --------------------------------- |
| Storage        | Original JSON text      | Binary representation             |
| Formatting     | Preserved               | Not preserved                     |
| Key order      | Preserved               | Not preserved                     |
| Duplicate keys | Preserved in input text | Only the last value is retained   |
| Searching      | Less efficient          | Generally more efficient          |
| Indexing       | Limited                 | Supports GIN indexes              |
| Common use     | Preserving JSON text    | Querying and processing JSON data |

Recommendation: Use `JSONB` for most applications where you need to search, filter, or process JSON data.

## 4. Creating a Table with JSON and JSONB Columns

Let's create a table named `students_json`.

```
CREATE TABLE students_json (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    contact_info JSON,
    additional_info JSONB
);
```

Explanation:

- `student_id`: Stores the student's ID.
- `student_name`: Stores the student's name.
- `contact_info`: Stores JSON data.
- `additional_info`: Stores JSONB data.

## 5. Inserting JSON Data

We can insert JSON data using the `INSERT INTO` statement.

```
INSERT INTO students_json
VALUES (
    1,
    'Ali',
    '{"email": "ali@example.com", "phone": "03001234567"}',
    '{"age": 22, "department": "Computer Science"}'
);
```

Insert another record:

```
INSERT INTO students_json
VALUES (
    2,
    'Sara',
    '{"email": "sara@example.com", "phone": "03007654321"}',
    '{"age": 21, "department": "Information Technology"}'
);
```

Display all records:

```
SELECT * FROM students_json;
```

## 6. Accessing JSON Data Using the `->` Operator

The `->` operator retrieves a JSON object field as JSON.

Syntax:

```
column_name -> 'key'
```

Example:

```
SELECT
    student_name,
    additional_info -> 'department' AS department
FROM students_json;
```

This returns the department as a JSON value.

For example:

```
"Computer Science"
```

Notice that the value includes quotation marks because it is returned as JSON.

## 7. Accessing JSON Values Using the `->>` Operator

The `->>` operator retrieves a JSON object field as text.

Syntax:

```
column_name ->> 'key'
```

Example:

```
SELECT
    student_name,
    additional_info ->> 'department' AS department
FROM students_json;
```

Output:

| student_name | department             |
| ------------ | ---------------------- |
| Ali          | Computer Science       |
| Sara         | Information Technology |

Difference between `->` and `->>`:

| Operator | Returns |
| -------- | ------- |
| `->`     | JSON    |
| `->>`    | Text    |

This is an important difference when working with JSON data.

## 8. Accessing Nested JSON Data

JSON objects can contain other JSON objects.

Example:

```
{
    "personal": {
        "age": 22,
        "city": "Dera Ghazi Khan"
    },
    "academic": {
        "department": "Computer Science"
    }
}
```

Let's insert this information:

```
INSERT INTO students_json
VALUES (
    3,
    'Ahmed',
    '{"email": "ahmed@example.com"}',
    '{
        "personal": {
            "age": 23,
            "city": "Dera Ghazi Khan"
        },
        "academic": {
            "department": "Computer Science"
        }
    }'
);
```

Access the nested department:

```
SELECT
    student_name,
    additional_info -> 'academic' ->> 'department' AS department
FROM students_json;
```

Access the nested city:

```
SELECT
    student_name,
    additional_info -> 'personal' ->> 'city' AS city
FROM students_json;
```

Explanation:

- First, `-> 'personal'` accesses the personal object.
- Then, `->> 'city'` retrieves the city as text.

## 9. Accessing JSON Array Elements

JSON also supports arrays.

Example:

```
{
    "skills": ["C++", "Python", "SQL"]
}
```

We can access array elements using their index.

Important: JSON array indexing starts from `0`.

| Index | Value  |
| ----- | ------ |
| 0     | C++    |
| 1     | Python |
| 2     | SQL    |

Insert a record:

```
INSERT INTO students_json
VALUES (
    4,
    'Hina',
    '{"email": "hina@example.com"}',
    '{"skills": ["C++", "Python", "SQL"]}'
);
```

Access the first skill:

```
SELECT
    student_name,
    additional_info -> 'skills' ->> 0 AS first_skill
FROM students_json;
```

Output:

| student_name | first_skill |
| ------------ | ----------- |
| Hina         | C++         |

Access the second skill:

```
SELECT additional_info -> 'skills' ->> 1
FROM students_json
WHERE student_id = 4;
```

Output:

```
Python
```

## 10. Checking Whether a JSON Key Exists

The `?` operator checks whether a JSONB object contains a specified top-level key.

It returns `TRUE` or `FALSE`.

Example:

```
SELECT
    student_name,
    additional_info ? 'age' AS has_age
FROM students_json;
```

For the `additional_info` column, PostgreSQL checks whether the key `age` exists.

Another example:

```
SELECT *
FROM students_json
WHERE additional_info ? 'skills';
```

This query returns records containing a top-level `skills` key.

Note: The `?` operator also checks whether a string exists as an array element when the JSONB value is an array.

## 11. Using JSONB Containment Operator `@>`

The `@>` operator checks whether one JSONB value contains another JSONB value.

Example:

```
SELECT *
FROM students_json
WHERE additional_info @> '{"department": "Computer Science"}';
```

This query finds records whose `additional_info` contains the specified department property.

For nested data:

```
SELECT *
FROM students_json
WHERE additional_info @> '{"academic": {"department": "Computer Science"}}';
```

The query checks for the nested object and its department value.

## 12. Updating JSONB Data

We can update a JSONB value using the `jsonb_set()` function.

Syntax:

```
jsonb_set(target, path, new_value)
```

Example: Update Ali's age.

```
UPDATE students_json
SET additional_info = jsonb_set(
    additional_info,
    '{age}',
    '23'
)
WHERE student_id = 1;
```

Here:

- `additional_info` is the JSONB column.
- `'{age}'` specifies the key to update.
- `'23'` is the new JSON value.

Check the updated record:

```
SELECT *
FROM students_json
WHERE student_id = 1;
```

### Updating a Nested JSONB Value

Update Ahmed's city:

```
UPDATE students_json
SET additional_info = jsonb_set(
    additional_info,
    '{personal,city}',
    '"Multan"'
)
WHERE student_id = 3;
```

Notice that `"Multan"` is enclosed in double quotation marks inside the SQL string because it is a JSON string value.

## 13. Adding a New Key to JSONB

We can use the `||` operator to combine JSONB objects.

This can be used to add a new key.

Example:

```
UPDATE students_json
SET additional_info = additional_info ||
    '{"graduation_year": 2027}'::jsonb
WHERE student_id = 1;
```

Now Ali's JSONB data includes the `graduation_year` key.

Check the result:

```
SELECT additional_info
FROM students_json
WHERE student_id = 1;
```

Important: If the key already exists, the new value replaces the old value.

## 14. Removing a Key from JSONB

The `-` operator removes a key from a JSONB object.

Example:

```
UPDATE students_json
SET additional_info = additional_info - 'age'
WHERE student_id = 1;
```

This removes the top-level `age` key.

To remove a nested key, use the `#-` operator:

```
UPDATE students_json
SET additional_info = additional_info #- '{personal,city}'
WHERE student_id = 3;
```

This removes the nested `city` key from the `personal` object.

## 15. Converting JSON Data to Text

We can use the `::text` cast to convert JSON or JSONB data into text.

Example:

```
SELECT
    student_name,
    additional_info::text AS information
FROM students_json;
```

This displays the JSONB value as text.

## 16. Converting Text into JSONB

Sometimes JSON information is stored in a text value. We can convert it into JSONB using a type cast.

Example:

```
SELECT
    '{"name": "Ali", "age": 22}'::jsonb AS student_data;
```

The `::jsonb` converts the text representation into a JSONB value.

Another example:

```
SELECT
    '{"marks": 85}'::jsonb ->> 'marks' AS marks;
```

Output:

```
85
```

## 17. Using JSONB with WHERE

We can use JSONB values in filtering conditions.

Find students whose age is 22:

```
SELECT *
FROM students_json
WHERE additional_info ->> 'age' = '22';
```

Find students whose department is Computer Science:

```
SELECT *
FROM students_json
WHERE additional_info ->> 'department' = 'Computer Science';
```

For nested department information:

```
SELECT *
FROM students_json
WHERE additional_info -> 'academic' ->> 'department'
    = 'Computer Science';
```

## 18. Creating an Index on a JSONB Column

When a table contains many records, searching JSONB data may become slower.

PostgreSQL supports GIN indexes for JSONB columns.

Example:

```
CREATE INDEX idx_student_additional_info
ON students_json
USING GIN (additional_info);
```

This creates a GIN index on the `additional_info` column.

It can help queries using JSONB operators such as `@>` and `?`.

Note: Index usefulness depends on the query and index type. An index is not guaranteed to improve every query.

## 19. JSON Functions in PostgreSQL

PostgreSQL provides several functions for working with JSON and JSONB.

| Function               | Purpose                                    |
| ---------------------- | ------------------------------------------ |
| `json_typeof()`        | Returns the JSON value type                |
| `jsonb_typeof()`       | Returns the JSONB value type               |
| `json_build_object()`  | Creates a JSON object                      |
| `jsonb_build_object()` | Creates a JSONB object                     |
| `json_agg()`           | Aggregates values into a JSON array        |
| `jsonb_agg()`          | Aggregates values into a JSONB array       |
| `json_array_length()`  | Returns the number of array elements       |
| `jsonb_array_length()` | Returns the number of JSONB array elements |

### Example 1: Check JSONB Data Type

```
SELECT jsonb_typeof('{"name": "Ali", "age": 22}'::jsonb);
```

Output:

```
object
```

### Example 2: Create a JSON Object

```
SELECT jsonb_build_object(
    'name', 'Ali',
    'age', 22,
    'department', 'Computer Science'
);
```

### Example 3: Create a JSON Array

```
SELECT jsonb_agg(student_name)
FROM students_json;
```

This creates a JSONB array containing student names.

### Example 4: Count Array Elements

```
SELECT jsonb_array_length(
    '["C++", "Python", "SQL"]'::jsonb
);
```

Output:

```
3
```

## 20. When Should We Use JSONB?

JSONB is useful when:

- Different records may have different additional properties.
- Data contains nested objects and arrays.
- You need to search inside JSON documents.
- You need to store flexible information.
- You want to create indexes on JSON data.

University example:

A university may store additional student information such as:

```
{
    "student_id": 101,
    "skills": ["C++", "Python", "SQL"],
    "certifications": [
        "Google Data Analytics",
        "Python Programming"
    ],
    "address": {
        "city": "Dera Ghazi Khan",
        "country": "Pakistan"
    }
}
```

This type of information can be stored in a JSONB column.

However, important information such as student ID, department ID, enrollment status, and fee balance should generally use properly designed relational columns and tables.

## 21. Practice Exercises

### Beginner Level

Exercise 1: Create a table named `employee_json` with the following columns:

- `employee_id`
- `employee_name`
- `employee_info` (JSONB)

Exercise 2: Insert three employees with JSONB information containing their age and department.

Exercise 3: Display all employee records.

Exercise 4: Retrieve each employee's department using the `->>` operator.

Exercise 5: Retrieve each employee's age using the `->>` operator.

### Intermediate Level

Exercise 6: Insert a JSONB object containing an employee's skills as an array.

Exercise 7: Retrieve the first skill from the skills array.

Exercise 8: Find employees whose department is `IT`.

Exercise 9: Check whether an employee's JSONB data contains the `age` key.

Exercise 10: Update an employee's age using `jsonb_set()`.

### Advanced Level

Exercise 11: Add a new key named `joining_year` to an employee's JSONB data.

Exercise 12: Remove the `age` key from an employee's JSONB data.

Exercise 13: Create a GIN index on the `employee_info` column.

Exercise 14: Use `jsonb_build_object()` to create an employee JSONB object.

Exercise 15: Use `jsonb_agg()` to return all employee names as a JSONB array.

## 22. Review Questions

1. What is JSON?
2. What is the difference between JSON and JSONB?
3. Why is JSONB generally preferred for querying JSON data?
4. What is the purpose of the `->` operator?
5. What is the purpose of the `->>` operator?
6. How do you access nested JSON data?
7. How do you access an array element in JSON?
8. What is the purpose of the `?` operator?
9. What does the `@>` operator do?
10. How can we update a JSONB value?
11. How can we add a new key to a JSONB object?
12. What is a GIN index?

## 23. Quick Revision

\| Concept | PostgreSQL syntax |\
\|---|---|\
\| JSON data type | `JSON` |\
\| JSONB data type | `JSONB` |\
\| Access JSON value | `->` |\
\| Access text value | `->>` |\
\| Check key existence | `?` |\
\| Check containment | `@>` |\
\| Update JSONB value | `jsonb_set()` |\
\| Add or merge keys | `||` |\
\| Remove a key | `-` |\
\| Remove nested key | `#-` |\
\| Create JSONB object | `jsonb_build_object()` |\
\| Create JSONB array | `jsonb_agg()` |\
\| Create JSONB index | `USING GIN` |

Next Lesson: PostgreSQL System and Information Functions

In the next lesson, students will learn how to retrieve information about the current database, connected user, current schema, server version, and current session.