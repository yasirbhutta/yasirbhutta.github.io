---
layout: page
title: "Step-by-Step Guide to install PHP on Windows (without XAMPP)"
description: Learn how to install PHP on Windows (without XAMPP).
keywords: php on windows, install php, guide to install php, php
toc: toc/php.html
course: php
topic: "basics"
mini_project: true
prev: /php/docs/basics/
---

# Step-by-Step Guide to install PHP on Windows (without XAMPP):


## ✅ **Step 1: Download PHP for Windows**
1. Go to the official PHP site:  
   [https://windows.php.net/download](https://windows.php.net/download)

2. Download the latest **Thread Safe Zip** version (for example, PHP 8.x for Windows).

---

## ✅ **Step 2: Extract PHP**
1. Create a folder `C:\php`
2. Extract the downloaded ZIP file into `C:\php`

---

## ✅ **Step 3: Add PHP to System PATH**
1. Press `Win + S`, search **"Environment Variables"**, and open it.
2. Under **System Variables**, find and select `Path`, then click **Edit**.
3. Click **New** and enter:
   ```
   C:\php
   ```
4. Click OK to save.

![Environment variables](/assets/images/windows/win10-envirvariables.webp)

**Image Source:** [computerhope.com](https://www.computerhope.com/issues/ch000549.htm)
---

## ✅ **Step 4: Test PHP Installation**
1. Open **Command Prompt** (CMD).
2. Type:
   ```
   php -v
   ```
3. You should see the PHP version info like:
   ```
   PHP 8.x.x (cli) ...
   ```

---

## ✅ **Step 5: (Optional) Create php.ini File**
1. In `C:\php`, you’ll find:
   - `php.ini-development`
   - `php.ini-production`
2. Copy and rename one to `php.ini`
3. Open it in a text editor and enable necessary extensions (e.g., `extension=mysqli` for MySQL).

---

## ✅ **Step 6: Run a PHP Script**
1. Create a file `test.php` with:
   ```php
   <?php
   echo "PHP is working!";
   ?>
   ```
2. Run it in CMD:
   ```
   php test.php
   ```

OR run a local web server:
   ```
   php -S localhost:8000
   ```
Then open [http://localhost:8000](http://localhost:8000) in a browser.

---

