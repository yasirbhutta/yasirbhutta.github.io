---
layout: page
title: "How to Install Oracle JDK and Configure VS Code for Java Development"
description: "Complete step-by-step guide to install Oracle JDK 17 LTS and set up Visual Studio Code for Java programming with all required extensions and configurations."
keywords: "Oracle JDK installation, VS Code Java setup, JDK 17 Windows, Java development environment, VS Code Java extension, Java configuration"
---

# 🔹 Step-by-Step: Oracle JDK + VS Code Setup

## ✅ STEP 1: Install Oracle JDK

### 1️⃣ Download Oracle JDK

👉 [https://www.oracle.com/java/technologies/downloads/](https://www.oracle.com/java/technologies/downloads/)

* Choose **Java 25 (LTS)**
* Download **Windows x64 Installer (.exe)**
* Accept the license

### 2️⃣ Install

* Double-click installer
* Click **Next → Install → Finish**
* Default path (recommended):

  ```
  C:\Program Files\Java\jdk-25
  ```

---

## ✅ STEP 2: Verify Oracle JDK Installation

1. Open **Command Prompt**
2. Run:

```bash
java -version
```

Expected output:

```
java version "25.x.x"
Java(TM) SE Runtime Environment
```

If this works → Oracle JDK is installed correctly ✔️

---

## ✅ STEP 3: Set JAVA_HOME (Important)

### 1️⃣ Open Environment Variables

* Press **Win + R**
* Type:

  ```
  sysdm.cpl
  ```
* Go to **Advanced → Environment Variables**

### 2️⃣ Add JAVA_HOME

* Under **System Variables** → Click **New**

  * Variable name:

    ```
    JAVA_HOME
    ```
  * Variable value:

    ```
    C:\Program Files\Java\jdk-25.0.2
    ```

### 3️⃣ Update PATH

* Select **Path** → Edit
* Click **New**
* Add:

  ```
  %JAVA_HOME%\bin
  ```

### 4️⃣ Click **OK → OK**

🔁 Close & reopen Command Prompt

Verify again:

```bash
javac -version
```

✔️ Compiler working

---

## ✅ STEP 4: Install VS Code

👉 [https://code.visualstudio.com](https://code.visualstudio.com)

During installation, **check these boxes**:
✔ Add to PATH
✔ Register Code as an editor

---

## ✅ STEP 5: Install Java Extensions in VS Code

1. Open **VS Code**
2. Go to **Extensions (Ctrl + Shift + X)**
3. Search:

```
Extension Pack for Java
```

4. Click **Install**

📦 Includes:

* Java Language Support
* Debugger for Java
* Maven
* Project Manager

---

## ✅ STEP 6: Tell VS Code to Use Oracle JDK

VS Code usually detects it automatically, but let’s be explicit.

### 1️⃣ Open Settings (JSON)

* Press **Ctrl + Shift + P**
* Type:

  ```
  Preferences: Open User Settings (JSON)
  ```

### 2️⃣ Add this:

```json
{
  "java.jdt.ls.java.home": "C:\\Program Files\\Java\\jdk-25.0.2"
}
```

⚠️ Use **double backslashes** in Windows paths

Save the file

---

## ✅ STEP 7: Create & Run First Java Program

### 1️⃣ Create Folder

```
JavaPractice
```

Open it in VS Code

### 2️⃣ Create File

```
HelloWorld.java
```

### 3️⃣ Code

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Oracle JDK + VS Code works!");
    }
}
```

### 4️⃣ Run

* Click **Run ▶** above `main()`
  OR

```bash
javac HelloWorld.java
java HelloWorld
```

🎉 Output:

```
Oracle JDK + VS Code works!
```

---

## 🔹 Common Issues & Fixes

### ❌ `javac is not recognized`

✔ JAVA_HOME not set correctly
✔ PATH not updated
✔ Restart Command Prompt / VS Code

---

## 🔹 You’re Now Ready For:

* Java **OOP deep dive**
* Interfaces & design patterns
* Maven / Gradle projects
* Spring Boot backend


