---
layout: default
title: How to Install Dev C++ and Configure the Compiler on Windows 11
description: Learn c++ programming from scratch with our free, beginner-friendly tutorials. Access open-source content, download PDF lessons, and start coding today!.
keywords: "c++ tutorial for beginners, learn c++ programming, free c++ lessons, c++ pdf tutorials, open-source c++ guide, c++ coding for beginners, c++ exercises and projects, c++ programming basics, downloadable c++ resources, c++ step-by-step guide"
---

I can guide you step by step on **installing Dev C++ on Windows 11** and configuring the compiler so you can run C++ programs smoothly. Let's go through it carefully.

---

## **Step 1: Download Dev C++**

1. Go to the official Dev C++ website: [https://sourceforge.net/projects/orwelldevcpp/](https://sourceforge.net/projects/orwelldevcpp/)
2. Click **Download**. You’ll get an `.exe` installer (usually named something like `Dev-Cpp-2022.exe`).

> ⚠️ Make sure to download the **latest version**, which comes with the GCC compiler built-in. This avoids separate compiler configuration.

---

## **Step 2: Install Dev C++**

1. Run the downloaded `.exe` file.
2. Follow the installation wizard:

   * Click **Next** on welcome screen.
   * Choose installation location (default is fine, e.g., `C:\Program Files\Dev-Cpp`).
   * Click **Next** and **Install**.
3. Wait for the installation to complete and click **Finish**.

---

## **Step 3: Launch Dev C++**

1. Open **Dev C++** from Start Menu or desktop shortcut.
2. You should see the main IDE window.

---

## **Step 4: Configure the Compiler (if needed)**

Newer Dev C++ versions usually include MinGW GCC compiler. But if your installation doesn’t detect the compiler:

1. Go to **Tools → Compiler Options → Compiler Settings → Executables**.
2. Check the **Compiler's installation directory** path:

   * Default: `C:\Program Files\Dev-Cpp\MinGW64` (or similar).
3. Make sure the following executables exist in `bin` folder inside the compiler directory:

   * `gcc.exe`
   * `g++.exe`
   * `gdb.exe` (optional for debugging)
4. If not, you may need to **download MinGW** separately and set the path.

---

## **Step 5: Test the Compiler**

1. Open Dev C++ → **File → New → Source File**.
2. Write a simple program:

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hello, World!" << endl;
    return 0;
}
```

3. Save the file as `hello.cpp`.
4. Click **Execute → Compile & Run** (or press `F11`).
5. You should see a console window displaying:

```
Hello, World!
```

✅ If this works, your Dev C++ installation and compiler are properly configured.

---

## **Optional Step 6: Set Environment Variable (for command-line use)**

If you want to compile programs using Command Prompt:

1. Add the path to the `bin` folder of your MinGW compiler to **Windows PATH**:

   * Right-click **This PC → Properties → Advanced system settings → Environment Variables → Path → Edit → New → Paste path to bin**.
   * Example: `C:\Program Files\Dev-Cpp\MinGW64\bin`
2. Open Command Prompt and type:

   ```
   g++ --version
   ```

   You should see the GCC version.

---

