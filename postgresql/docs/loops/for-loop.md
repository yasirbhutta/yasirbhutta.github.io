---
layout: page
title: "PostgreSQL FOR Loop – Introduction, Syntax, Examples and Practice"
description: Learn how to use the PostgreSQL PL/pgSQL FOR loop to iterate over numeric ranges, run repeated statements, and print values in ascending or descending order.
keywords: PostgreSQL FOR loop, PL/pgSQL FOR loop, PostgreSQL loop, numeric range loop, REVERSE loop, RAISE NOTICE, DO block, PostgreSQL loops
---

## 1. Introduction

A `FOR` loop in PostgreSQL is used to repeat a block of SQL statements a specific number of times.

It automatically increases or decreases the counter variable during each iteration.

Real-life example:

Suppose a teacher wants to print the numbers of students from 1 to 5. Instead of writing five separate statements, we can use a `FOR` loop.

## 2. Purpose of FOR Loop

The `FOR` loop is useful when:

- You want to repeat a task a specific number of times.
- You want to process a range of numbers.
- You want to execute statements repeatedly.
- You want to reduce repeated code.

## 3. Syntax

```sql
FOR counter IN start_value..end_value
LOOP
    -- Statements to execute
END LOOP;
```

Explanation:

| Component     | Description                              |
| ------------- | ---------------------------------------- |
| `FOR`         | Starts the loop.                         |
| `counter`     | Variable that stores the current number. |
| `start_value` | Starting number of the loop.             |
| `..`          | Defines the range.                       |
| `end_value`   | Ending number of the loop.               |
| `LOOP`        | Starts the block of statements.          |
| `END LOOP`    | Ends the loop.                           |

Important: The `FOR` loop automatically declares its counter variable. You do not need to declare it separately.

## 4. Example 1: Print Numbers from 1 to 5

Let's print numbers from 1 to 5 using a `FOR` loop.

**SQL Code:**

```sql
DO $$
BEGIN
    FOR i IN 1..5
    LOOP
        RAISE NOTICE 'Number: %', i;
    END LOOP;
END $$;
```

Output:

```
NOTICE: Number: 1
NOTICE: Number: 2
NOTICE: Number: 3
NOTICE: Number: 4
NOTICE: Number: 5
```

## 5. Understanding the Example

- `DO $$` starts an anonymous PL/pgSQL block.
- `BEGIN` starts the executable section.
- `FOR i IN 1..5` starts the loop from 1 to 5.
- `LOOP` starts the statements to be repeated.
- `RAISE NOTICE` displays the current value of `i`.
- `END LOOP` ends the loop.
- `END $$` ends the PL/pgSQL block.

## 6. Dry Run

A dry run shows how the loop executes step by step.

| Iteration | Value of `i` | Output    |
| --------- | ------------ | --------- |
| 1         | 1            | Number: 1 |
| 2         | 2            | Number: 2 |
| 3         | 3            | Number: 3 |
| 4         | 4            | Number: 4 |
| 5         | 5            | Number: 5 |

Total iterations: 5

## 7. Example 2: Print Numbers from 5 to 1

We can also use a `REVERSE` keyword to execute a loop in descending order.

```sql
DO $$
BEGIN
    FOR i IN REVERSE 5..1
    LOOP
        RAISE NOTICE 'Number: %', i;
    END LOOP;
END $$;
```

Output:

```
NOTICE: Number: 5
NOTICE: Number: 4
NOTICE: Number: 3
NOTICE: Number: 2
NOTICE: Number: 1
```

## 8. Practice Task

Task: Write a PostgreSQL `FOR` loop to print numbers from 1 to 10.
