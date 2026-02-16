---
layout: page
title: "How to Install Oracle JDK and Configure VS Code for Java Development"
description: "Complete step-by-step guide to install Oracle JDK 17 LTS and set up Visual Studio Code for Java programming with all required extensions and configurations."
keywords: "Oracle JDK installation, VS Code Java setup, JDK 17 Windows, Java development environment, VS Code Java extension, Java configuration"
---

Here’s an improved, **student-friendly version of your notes** with clearer explanations, better structure, examples, and learning tips.

---

# Java Variables – Beginner Notes

Great job reaching this step! 🎉
So far, your program could only print fixed text. Now you’ll learn how to make programs **store information** and use it dynamically using **variables**.

---

## What Is a Variable?

A **variable** is like a labeled container that stores data in memory so your program can use it later.

👉 Think of it as a box:

* The **label** = variable name
* The **content** = stored value

Example:

```java
String name = "Alex";
```

Here:

* `String` → type of data
* `name` → variable label
* `"Alex"` → stored value

---

## The "Greet Me" Program

```java
public class HelloName {
    public static void main(String[] args) {

        // Variable storing text
        String name = "Alex"; 

        // Print message using variable
        System.out.println("Hello, " + name + "!");
    }
}
```

---

## Code Breakdown

### 1️⃣ Variable Creation

```java
String name = "Alex";
```

This line:

* Creates a variable called `name`
* Stores the text `"Alex"` inside it

---

### 2️⃣ Concatenation (Joining Text)

```java
"Hello, " + name + "!"
```

The `+` operator joins text and variables together.

Result printed:

```
Hello, Alex!
```

---

### 3️⃣ Output Statement

```java
System.out.println(...);
```

Displays text on the screen.

---

## Java Is Strongly Typed

Java requires you to **declare the data type** of every variable.

| Type      | Stores          | Example  |
| --------- | --------------- | -------- |
| `String`  | Text            | `"Java"` |
| `int`     | Whole numbers   | `25`     |
| `double`  | Decimal numbers | `9.99`   |
| `boolean` | True/False      | `true`   |

📌 Why types matter:
They tell Java how much memory to use and what operations are allowed.

---

## Rules for Naming Variables

✔ Allowed

```
name
studentAge
totalMarks
```

❌ Not allowed

```
1name
student age
class
```

**Tips**

* Must start with a letter, `_`, or `$`
* Cannot use spaces
* Cannot use Java keywords
* Use camelCase → `favoriteNumber`

---

## Tasks

### Task #1

Create variables for:

* Your name
* Your favorite number

Then print:

```
Ali's favorite number is 7
```

Hint:

```java
System.out.println(name + "'s favorite number is " + myNumber);
```

---

## Common Beginner Mistakes

❌ Forgetting semicolon

```
String name = "Ali"
```

✔ Correct

```
String name = "Ali";
```

---

❌ Wrong type

```
int name = "Ali";
```

✔ Correct

```
String name = "Ali";
```

---

## Challenge Question (Think Like a Programmer)

What will this print?

```java
int x = 5;
int y = 10;
System.out.println(x + y);
```

Answer:
➡ It prints `15` because both are numbers, so Java adds them.

---

✅ **Next Skill to Learn:**
Taking input from the user using keyboard (Scanner class).
