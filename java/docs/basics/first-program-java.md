---
layout: page
title: "Java Hello World Program Explained for Beginners | First Java Program Guid"
description: "Learn how to write and run your first Java program with a simple HelloWorld example. Step-by-step explanation of code structure, compilation, JVM execution, and beginner tips."
keywords: "Java Hello World program, first Java program, Java beginner tutorial, HelloWorld.java example, Java basics, Java main method explained, how to compile Java code, Java JVM explanation, learn Java programming, Java tutorial for beginners"
---

## Your First Program: `HelloWorld.java`

In Java, every piece of code must live inside a **class**. Here is what the code looks like:

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}

```

### Breaking Down the Code

Don't worry if this looks like a secret code at first. Here is what each part actually does:

* **`public class HelloWorld`**: This defines the "bucket" for your code. In Java, the filename must match the class name (so this file must be saved as `HelloWorld.java`).
* **`public static void main(String[] args)`**: This is the **entry point**. It’s the door the computer walks through to start running your program. Without this specific line, your program won't run.
* **`System.out.println`**: This is the command that tells the computer to "print" or display text on the screen.
* **The Semicolon (`;`)**: Think of this as a period at the end of a sentence. It tells Java the instruction is finished.

---

## How Java Works

Unlike some languages that run directly, Java uses a two-step process to ensure it can run on any device (Windows, Mac, or Linux).

1. **Compile**: You run your code through a compiler (`javac`), which turns your readable text into "Bytecode."
2. **Run**: The Java Virtual Machine (JVM) reads that bytecode and executes it on your specific computer.

---

## 3 Steps to Run It

If you have the Java Development Kit (JDK) installed, you can try this right now:

1. **Save**: Copy the code above into a text editor (like Notepad or TextEdit) and save it as `HelloWorld.java`.
2. **Compile**: Open your terminal or command prompt and type:
`javac HelloWorld.java`
3. **Execute**: Type:
`java HelloWorld`

## 📘 **Related Topics**

- [Java IDEs for OOP Coding](../tools-java.md)
- [How to Install Oracle JDK and Configure VS Code for Java Development](../vscode-jdk.md)

