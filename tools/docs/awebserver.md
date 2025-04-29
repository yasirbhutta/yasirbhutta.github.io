---
layout: page
title: "How to Install AWebServer (Apache, PHP, SQL) on Android Phone"
description: Step-by-step guide to install and configure AWebServer on your Android device. Learn how to set up Apache, PHP, and MariaDB for mobile web development.
keywords: AWebServer, Android Apache server, PHP on Android, MariaDB Android, Mobile web server, Install AWebServer, Configure AWebServer, Android localhost server
---

To install and configure **AWebServer** (a mobile app that includes Apache, PHP, and SQL support) on your **Android** phone, follow this step-by-step guide:

---

### ✅ **Requirements**
- Android phone (with decent storage and RAM)
- Internet connection
- Basic knowledge of file management

---

### 🔧 **Step-by-Step Installation and Configuration**

#### **Step 1: Install AWebServer**
1. Open the **Google Play Store**.
2. Search for: `AWebServer: PHP, MySQL, FTP`
3. Tap **Install** and wait for the app to download.

#### **Step 2: Launch the App**
1. Open the **AWebServer** app.
2. Grant required permissions (especially **storage access**).

#### **Step 3: Setup Root Directory**
1. On first run, the app will prompt you to set a **root directory**.
   - This is where your PHP and HTML files will go.
   - Choose a folder (e.g., `/storage/emulated/0/www`) or accept the default.
2. You can copy your project files (`.php`, `.html`, etc.) into this folder using a file manager.

#### **Step 4: Configure the Server**
- Open the app menu → Tap on **Settings**.
- You will find options for:
  - Apache port (default: `8080`)
  - PHP version (select the default or available one)
  - Index file (e.g., `index.php`)

> Optional: You can change the port from `8080` to `80` if no other app is using it.

#### **Step 5: Start the Server**
1. Go back to the main screen of the app.
2. Tap **Start Server**.
3. You will see a message like:  
   `Server running at http://127.0.0.1:8080`

#### **Step 6: Test with a PHP File**
1. In your root folder (e.g., `www`), create a file named `info.php` with this content:

   ```php
   <?php
   phpinfo();
   ?>
   ```

2. Open a browser on your phone and go to:  
   `http://127.0.0.1:8080/info.php`

3. You should see the PHP info page — this confirms PHP is working.

#### **Step 7: Using SQL (MariaDB)**
1. AWebServer uses **MariaDB** (a MySQL-compatible DB).
2. By default, the database runs with:
   - Host: `127.0.0.1`
   - Port: `3306`
   - User: `root`
   - Password: (may be blank or configured in settings)

3. You can connect using:
   - **phpMyAdmin** (included in some versions of AWebServer)
   - Or use PHP scripts like:

   ```php
   <?php
   $conn = new mysqli("127.0.0.1", "root", "", "test");
   if ($conn->connect_error) {
       die("Connection failed: " . $conn->connect_error);
   }
   echo "Connected successfully";
   ?>
   ```

---

### ⚙️ **Optional: Add phpMyAdmin**
1. Download `phpMyAdmin` from [https://www.phpmyadmin.net/](https://www.phpmyadmin.net/)
2. Extract it and place it in your root folder under `/phpmyadmin`
3. Access it in the browser:  
   `http://127.0.0.1:8080/phpmyadmin`

---

### 📌 Tips
- Don't forget to **stop the server** when not in use to save battery.
- To use it on another device (same Wi-Fi), find your **local IP** (e.g., `192.168.x.x`) and access it like:  
  `http://192.168.x.x:8080`

---
