---
layout: page
title: "How to Use PHP: Installation Guide for Windows & Mobile Devices (2025)"
description: Learn how to use PHP with step-by-step installation guides for Windows and mobile phones. Set up PHP using XAMPP, manual installation, or VS Code. Start coding PHP today!.
keywords: how to use PHP, PHP installation Windows, install PHP on mobile, XAMPP PHP setup, manual PHP install, PHP with Visual Studio Code, PHP mobile app, PHP online compiler, run PHP locally, PHP tutorial beginners
toc: toc/php.html
course: php
topic: "basics"
mini_project: true
---

## Table of Contents
- [How to Install on Windows](#how-to-install-on-windows)
- [How to Install on Mobile phone](#how-to-install-on-windows)
- [Online PHP Compilers](#online-php-compilers)

## How to Install on Windows

To use PHP on Windows, you need to set up a local development environment that can run PHP scripts. Here are **3 main ways** to do it:

---

### ✅ Method 1: **Using XAMPP (Easiest Way)**
**XAMPP** is a free and easy-to-install package that includes Apache (web server), MySQL, and PHP.

### Install XAMPP Server

XAMPP is a completely free, easy to install Apache distribution containing MariaDB, PHP, and Perl. The XAMPP open source package has been set up to be incredibly easy to install and to use.[6]

### Steps:
1. **Download XAMPP**:  
   Go to [https://www.apachefriends.org/download.html](https://www.apachefriends.org/download.html) and download the Windows version.

2. **Install XAMPP**:  
   Run the installer and choose to install Apache and PHP (MySQL is optional).

3. **Start Apache**:  
   Open the XAMPP Control Panel and click **Start** next to Apache.

4. **Write PHP Code**:  
   Save your PHP files in the `htdocs` folder (usually in `C:\xampp\htdocs`), e.g.:
   ```php
   <?php
   echo "Hello, PHP!";
   ?>
   ```

5. **Run in Browser**:  
   Open your browser and go to:  
   ```
   http://localhost/yourfilename.php
   ```

---

### ✅ Method 2: **Install PHP Manually (for advanced users)**

### Steps:
1. **Download PHP**:  
   Get it from [https://windows.php.net/download](https://windows.php.net/download) (choose the Thread Safe version for use with a server).

2. **Extract PHP**:  
   Unzip it to a folder like `C:\php`.

3. **Configure Environment Variable**:  
   Add `C:\php` to your system `PATH`.

4. **Test in Command Prompt**:  
   Open CMD and type:
   ```
   php -v
   ```
   You should see the PHP version.

5. **Run a PHP Script**:
   Save a file `test.php` with:
   ```php
   <?php
   echo "My first php page.";
   ?>
   ```
   Then run:
   ```
   php test.php
   ```
for more details, see [How to install php](install-php.md)

---

### ✅ Method 3: **Use Visual Studio Code + PHP + Browser**

1. Install **VS Code**.
2. Install the **PHP Extension Pack**.
3. Write and save `.php` files.
4. Use XAMPP/Apache or run PHP from terminal (`php -S localhost:8000`) to test in a browser.


## How to Install on Mobile phone

**Step 1: Use a Code Editor App**  

Since PHP is a server-side language, you need an environment that supports it. Try these mobile apps:  
- **ACode** – Allows PHP coding on Android.  

**Step 2: Install AWebServer (Apache, PHP, SQL) on Android Phone**

for more details, see [How to Install AWebServer (Apache, PHP, SQL) on Android Phone](/tools/docs/awebserver.md)

## Online PHP Compilers  
Since installing a local server on a phone is tricky, online compilers are a great alternative:  
- [PHP Fiddle](https://phpfiddle.org/)  
- [Replit](https://replit.com/)  
- [JDoodle](https://www.jdoodle.com/php-online-compiler)  

## Use a Web Hosting Service  
Some free hosting services allow PHP execution, such as:  
- **000webhost** (free hosting with PHP and MySQL)  
- **InfinityFree** (supports PHP and databases)  

## References 

[1] AWebServer – PHP, MySQL, FTP [Mobile App], Ice Cold Apps. [Online]. Available: <https://play.google.com/store/apps/details?id=com.icecoldapps>.awebserver

[2] phpMyAdmin Team, *phpMyAdmin*. [Online]. Available: <https://www.phpmyadmin.net/>

[3] Apache Software Foundation, *Apache HTTP Server Documentation*. [Online]. Available: <https://httpd.apache.org/docs/>

[4] PHP Group, *PHP Manual*. [Online]. Available: <https://www.php.net/manual/en/>

[5] MariaDB Corporation, *MariaDB Knowledge Base*. [Online]. Available: <https://mariadb.com/kb/en/>

[6] Apache Friends, *XAMPP - Apache, MySQL, PHP, Perl*. [Online]. Available: <https://www.apachefriends.org/>


