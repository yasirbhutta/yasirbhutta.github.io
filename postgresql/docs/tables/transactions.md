# Student Notes: Transactions in PostgreSQL

## 1. Introduction

Imagine a student pays a university fee of Rs. 50,000.

The university's database needs to perform two operations:

1. Deduct Rs. 50,000 from the student's outstanding fee.
2. Record the payment in the fee payment table.

Both operations must be completed successfully.

What happens if the first operation succeeds but the second operation fails?

The database may contain incomplete or incorrect information.

To prevent such problems, PostgreSQL provides Transactions.

A transaction allows us to group multiple SQL operations into one logical unit of work.

## 2. What is a Transaction?

A Transaction is a group of database operations that are treated as one unit.

Either all operations are completed successfully, or the changes are rolled back.

For example, a bank transfer involves:

- Deducting money from Account A.
- Adding money to Account B.

Both operations must succeed together.

If one operation fails, the transaction can be cancelled.

## 3. Why Do We Use Transactions?

Transactions help us:

1. Maintain data accuracy.
2. Prevent incomplete database operations.
3. Protect financial transactions.
4. Handle errors safely.
5. Maintain database consistency.
6. Execute multiple SQL statements as one unit.

## 4. ACID Properties of Transactions

PostgreSQL transactions follow four important properties called ACID.

# A

Atomicity

All operations succeed, or none of their changes are committed.

# C

Consistency

A transaction must preserve database rules and constraints.

# I

Isolation

Concurrent transactions should not interfere in ways that violate the selected isolation level.

# D

Durability

Once a transaction is committed, its changes are preserved, including across a database crash, subject to PostgreSQL's durability configuration.

## 5. Important Transaction Commands

PostgreSQL provides three basic transaction commands.

| Command    | Purpose                               |
| ---------- | ------------------------------------- |
| `BEGIN`    | Starts a transaction                  |
| `COMMIT`   | Saves transaction changes permanently |
| `ROLLBACK` | Cancels uncommitted changes           |

Let's understand each command with practical examples.

## 6. Creating a Sample Table

We will create a table named `accounts`.

```
CREATE TABLE accounts (
    account_id INT PRIMARY KEY,
    account_holder VARCHAR(50),
    balance NUMERIC(10, 2)
);
```

Insert sample records:

```
INSERT INTO accounts
VALUES
    (1, 'Ali', 50000),
    (2, 'Sara', 30000);
```

Display the records:

```
SELECT * FROM accounts;
```

Expected output:

| account_id | account_holder | balance  |
| ---------- | -------------- | -------- |
| 1          | Ali            | 50000.00 |
| 2          | Sara           | 30000.00 |

## 7. BEGIN: Starting a Transaction

The `BEGIN` command starts a new transaction.

Syntax:

```
BEGIN;
```

Example:

```
BEGIN;

UPDATE accounts
SET balance = balance - 5000
WHERE account_id = 1;
```

We have deducted Rs. 5,000 from Ali's account.

However, the transaction has not yet been committed.

The changes can still be rolled back.

## 8. COMMIT: Saving Changes

The `COMMIT` command permanently saves the changes made during the current transaction.

Syntax:

```
COMMIT;
```

Example:

```
BEGIN;

UPDATE accounts
SET balance = balance - 5000
WHERE account_id = 1;

COMMIT;
```

Check the updated records:

```
SELECT * FROM accounts;
```

Expected output:

| account_id | account_holder | balance  |
| ---------- | -------------- | -------- |
| 1          | Ali            | 45000.00 |
| 2          | Sara           | 30000.00 |

The changes are now committed.

## 9. ROLLBACK: Cancelling Changes

The `ROLLBACK` command cancels all uncommitted changes in the current transaction.

Syntax:

```
ROLLBACK;
```

Example:

```
BEGIN;

UPDATE accounts
SET balance = balance - 10000
WHERE account_id = 1;

ROLLBACK;
```

Now check the records:

```
SELECT * FROM accounts;
```

Expected output:

| account_id | account_holder | balance  |
| ---------- | -------------- | -------- |
| 1          | Ali            | 45000.00 |
| 2          | Sara           | 30000.00 |

The balance remains Rs. 45,000 because the update was rolled back.

Remember: ROLLBACK only cancels changes that have not already been committed.

## 10. Practical Example: Bank Money Transfer

Let's transfer Rs. 10,000 from Ali's account to Sara's account.

Two operations are required:

1. Deduct Rs. 10,000 from Ali.
2. Add Rs. 10,000 to Sara.

Both operations should succeed together.

```
BEGIN;

UPDATE accounts
SET balance = balance - 10000
WHERE account_id = 1;

UPDATE accounts
SET balance = balance + 10000
WHERE account_id = 2;

COMMIT;
```

Check the account balances:

```
SELECT * FROM accounts;
```

Expected output:

| account_id | account_holder | balance  |
| ---------- | -------------- | -------- |
| 1          | Ali            | 35000.00 |
| 2          | Sara           | 40000.00 |

The transaction successfully transferred Rs. 10,000.

Important: This example demonstrates the basic transaction concept. A production banking application should also validate balances, check that both accounts exist, and handle errors before committing.

## 11. What Happens When an Error Occurs?

Suppose we execute an invalid SQL statement inside a transaction.

```
BEGIN;

UPDATE accounts
SET balance = balance - 5000
WHERE account_id = 1;

UPDATE accounts
SET unknown_column = 100
WHERE account_id = 2;

COMMIT;
```

The second UPDATE generates an error because `unknown_column` does not exist.

PostgreSQL marks the transaction as failed.

The final `COMMIT` will not save the earlier update.

We must execute:

```
ROLLBACK;
```

This returns the transaction to its state before `BEGIN`.

## 12. SAVEPOINT in PostgreSQL

Sometimes we want to cancel only part of a transaction instead of cancelling the entire transaction.

PostgreSQL provides `SAVEPOINT` for this purpose.

A savepoint creates a point inside a transaction to which we can return.

Syntax:

```
SAVEPOINT savepoint_name;
```

To return to a savepoint:

```
ROLLBACK TO SAVEPOINT savepoint_name;
```

Example:

```
BEGIN;

UPDATE accounts
SET balance = balance - 2000
WHERE account_id = 1;

SAVEPOINT first_update;

UPDATE accounts
SET balance = balance + 2000
WHERE account_id = 2;

ROLLBACK TO SAVEPOINT first_update;

COMMIT;
```

Understand the operations:

1. BEGIN starts the transaction.
2. The first UPDATE deducts Rs. 2,000 from Ali.
3. SAVEPOINT creates a recovery point.
4. The second UPDATE adds Rs. 2,000 to Sara.
5. ROLLBACK TO SAVEPOINT cancels the second UPDATE.
6. COMMIT saves the first UPDATE.

Final result: Ali's balance decreases by Rs. 2,000, while Sara's balance remains unchanged.

## 13. RELEASE SAVEPOINT

After creating a savepoint, we can remove it using `RELEASE SAVEPOINT`.

```
BEGIN;

UPDATE accounts
SET balance = balance - 1000
WHERE account_id = 1;

SAVEPOINT my_savepoint;

UPDATE accounts
SET balance = balance + 1000
WHERE account_id = 2;

RELEASE SAVEPOINT my_savepoint;

COMMIT;
```

The transaction is committed successfully.

Releasing a savepoint does not commit the transaction. It only removes that savepoint.

## 14. Transaction vs Normal SQL Execution

| Normal SQL Execution                                                        | Transaction                                                |
| --------------------------------------------------------------------------- | ---------------------------------------------------------- |
| A statement normally runs in its own transaction when using autocommit      | Multiple statements can be grouped together                |
| Successful statement changes are committed automatically in autocommit mode | Changes remain uncommitted until COMMIT                    |
| Cannot roll back an already committed statement                             | Can roll back uncommitted changes                          |
| Suitable for simple operations                                              | Suitable for related operations that must succeed together |

Note: PostgreSQL automatically executes statements in transactions. When using tools such as pgAdmin with autocommit enabled, each successful statement is committed automatically unless you explicitly start a transaction.

## 15. Common Transaction Commands

| Command                 | Description                            |
| ----------------------- | -------------------------------------- |
| `BEGIN`                 | Starts a transaction                   |
| `START TRANSACTION`     | Alternative way to start a transaction |
| `COMMIT`                | Saves changes                          |
| `ROLLBACK`              | Cancels uncommitted changes            |
| `SAVEPOINT`             | Creates a recovery point               |
| `ROLLBACK TO SAVEPOINT` | Returns to a recovery point            |
| `RELEASE SAVEPOINT`     | Removes a savepoint                    |

## 16. Practice Exercises

Use the `accounts` table created in this lesson.

### Beginner Level

1. Start a transaction using BEGIN.
2. Deduct Rs. 1,000 from Ali's account.
3. Commit the transaction.
4. Start another transaction and add Rs. 2,000 to Sara's account.
5. Roll back the transaction and check the balance.

### Intermediate Level

6. Transfer Rs. 5,000 from Ali to Sara using a transaction.
7. Transfer Rs. 3,000 from Sara to Ali and commit the changes.
8. Update both account balances in one transaction.
9. Create a transaction with two UPDATE statements and roll it back.

### Advanced Level

10. Create a SAVEPOINT after the first UPDATE statement.
11. Perform a second UPDATE and return to the savepoint.
12. Commit the remaining transaction.
13. Write a transaction that checks whether an account has sufficient balance before making a transfer. Consider using a PostgreSQL procedural block or application code for the conditional logic.

## 17. Review Questions

1. What is a transaction in PostgreSQL?
2. Why do we use transactions?
3. What does ACID stand for?
4. What is the purpose of BEGIN?
5. What does COMMIT do?
6. What is the difference between COMMIT and ROLLBACK?
7. Can we roll back a committed transaction?
8. What is a SAVEPOINT?
9. What does ROLLBACK TO SAVEPOINT do?
10. What is the purpose of RELEASE SAVEPOINT?
11. What happens when an SQL statement fails inside a transaction?
12. Why are transactions important in banking systems?

## 18. Quick Revision

Transaction workflow

BEGIN

Start transaction

Execute SQL statements

INSERT, UPDATE, DELETE

COMMIT

Save changes

ROLLBACK

Cancel changes

Remember:

- BEGIN starts a transaction.
- COMMIT saves changes.
- ROLLBACK cancels uncommitted changes.
- SAVEPOINT creates a recovery point.
- ACID ensures reliable transaction processing.

## Next Lesson

Functions in PostgreSQL

You will learn how to create and execute reusable SQL functions, pass parameters, return values, and use built-in PostgreSQL functions.