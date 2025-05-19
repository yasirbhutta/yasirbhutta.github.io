---
layout: page
title: "MySQL with PHP: Database Connection Guide & Examples"
description: Learn how to connect MySQL with PHP using mysqli & PDO. Step-by-step guide on database queries, CRUD operations, security best practices, and error handling.
keywords: MySQL PHP integration, PHP MySQL connection, mysqli tutorial, PDO PHP, PHP database queries, MySQL CRUD operations, PHP MySQL examples, secure database PHP, PHP MySQL fetch data, PHP MySQL insert data, PHP MySQL update delete, prepared statements PHP, PHP MySQL error handling, PHP MySQL best practices, connect database to PHP
author: Muhammad Yasir Bhutta
course: php
topic: mysql-php
toc: toc/php.html
prev: /php/docs/forms/
next: /php/docs/projects/
breadcrumb:
  - title: Home
    url: /
  - title: PHP
    url: /php/
---

### WHAT IS MYSQL?

- `MySQL` is the world's most popular open source database.
- With its proven performance, reliability and ease-of-use, MySQL has become the leading database choice for web-based applications, used by high profile web properties including Facebook, Twitter, YouTube, Yahoo! and many more.
- MySQL uses standard SQL.
- MySQL compiles on a number of platforms (windows, linux)
- MySQL is free to download and use
- MySQL is developed, distributed, and supported by Oracle Corporation

### MYSQL

- The data in a MySQL database are stored in tables.
- A table is a collection of related data, and it consists of columns and rows.

### PHP + MYSQL DATABASE SYSTEM

PHP combined with MySQL are cross-platform (you can develop in Windows and serve on a Unix platform)

## PHP CONNECT TO MYSQL

PHP 5 and later can work with a MySQL database using:

- MySQLi (object-oriented)
- MySQLi (procedural)
- PDO (PHP Data Objects)

### MYSQLI VS PDO

- PDO will work on 12 different database systems, where as MySQLi will only work with MySQL databases.
- Both are object-oriented, but MySQLi also offers a procedural API.

### TOOLS

- MYSQL Workbench
[Download](https://dev.mysql.com/downloads/workbench/)
- PHPMyAdmin
[Download](https://www.phpmyadmin.net/downloads/)
-[https://www.heidisql.com/](https://www.heidisql.com/)
-Navicat GUI | DB Admin Tool for MySQL, PostgreSQL
[https://www.navicat.com/en/](https://www.navicat.com/en/)

### mysqli

- open a new connection to the MYSQL server.

#### Parameters

- **hostname:**
  - can either a host name or an IP address. The local host is assumed when passing the null value or the string "localhost" to this paramter.
  - When possible, pipes will be used instead of the TCP/IP. The TCP/IP protocol is used if 
    a host name and port number are provided together e.g. localhost:3308
- **username:** the MySQL user name.
- **password:** if not provided or null, the MySQL server will attempt to authenticate the user against 
those user records which have no password only. This allows one username to be used
with different permissions (depending on if a password is provided or not).
- **database:** if provided will specify the default database to be used when performing queries.
- **port:** specifies the port number to attempt to connect to the MySQL server.
- **socket:** Specifies the socket or named pipe that should be used.

### mysqli::$connnect_error

- Returns the error message from the last connection attempt.

#### Parameters

The function has no parameters

#### Return Values

A string that describes the error. null is returned if no error occured.

### die

- Output a message and terminate the current script.
- Equivalent to exit().

#### Example #1 Connect with mySQL

```php
<?php
$servername = "localhost";
$username = "root"; // user name
$password = "paki123"; // password 

// Create connection
$conn = new mysqli($servername, $username, $password);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
echo "Connected successfully";
?>
```

### mysqli::query

- Performs a query on the database
- Returns FALSE on failure. For successful SELECT, SHOW, DESCRIBE or EXPLAIN queries mysqli_query() will return a mysqli_result object. For other successful queries mysqli_query() will return TRUE.
- The mysqli_result class: Represents the result set obtained from a query against the database.

### mysqli::$error

- Returns the last error message fo the most recent MySQLi function call that can succeed or fail.

### mysqli::close

- Closes a previously opened database connection.
- Open non-persistent MySQL connections and result sets are automatically
closed when their objects are destroyed.
- Explicitly closing open connections and freeing result sets is optional. However, it's a good
idea to close the connection as soon as the script finishes performing all of its database operations, if it still has a lot of processing to do after getting the results.

#### Return Values

Returns true on sucess or false on failure.

### === Operator in PHP

- In PHP, the **==** is an comparison operator that checks if two values are equals. It returns a boolean value of 'true' if the values are equal, and 'false' if they are not.
- On the other hand, '===' is also a comparision operator in PHP, but it is stricker than '=='. It checks not only if the values are equals, but also if they are of the same type. This means that '===' will only return 'true' if the values are equal and of the same type.

```php
$x = "10";
$y = 10;

if ($x==$y){
    //this condition will be true
}

if ($x===$y){
    // this condition will be false
}
```

In above example, '$x' is a string and '$y' is an integer. when we use '==', the comparison is true becuase '$x' and '$y' have the same value, even though they are different types. However, when we use '===', the comparison is false because '$x' and '$y' are not the same type.

#### Example #2 Create Database

```php
<?php
$servername = "localhost";
$username = "root"; // user name
$password = "paki123"; // password 

// Create connection
$conn = new mysqli($servername, $username, $password);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
// Create database
$sql = "CREATE DATABASE hr5";
if ($conn->query($sql) === TRUE) {
    echo "Database created successfully";
} else {
    echo "Error creating database: " . $conn->error;
}

$conn->close();
?>
```

file name is **conn-db.php**

#### Example #3 Connect with Database

```php
<?php
$servername = "localhost";
$username = "root";
$password = "paki123";
$dbname = "hr5";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
echo "Connected successfully with <strong> $dbname </strong> database<br>";
?>
```

#### Example  Create Tables

```php
<?php include('conn-db.php');

// sql to create DEPARTMENTS table
$sql = "CREATE TABLE DEPARTMENTS(
department_id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
department_name VARCHAR(30) NOT NULL
)";

if ($conn->query($sql) === TRUE) {
    echo "Table DEPARTMENTS created successfully<br>";
} else {
    echo "Error creating table: " . $conn->error;
}
// sql to create EMPLOYEES table
$sql = "CREATE TABLE EMPLOYEES(
employee_id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
first_name VARCHAR(30) NOT NULL,
last_name VARCHAR(30) NOT NULL,
email VARCHAR(30),
phone_number VARCHAR(20),
hire_date DATE,
salary INT(6),
department_id INT(6)
)";

if ($conn->query($sql) === TRUE) {
    echo "Table EMPLOYEES created successfully";
} else {
    echo "Error creating table: " . $conn->error;
}

$conn->close();
?>
```

### PHP: include
The include statement includes and evaluates the specified file.

### PHP:require

- require is identical to include except upon failure it will also produce a fatal E_COMPILE_ERROR level error.
- In other words, it will halt the script whereas include only emits a warning (E_WARNING) which allows the script to continue.

- When a file is included, the code it contains inherits the variable scope of the line on which the include occurs. Any variables available at that line in the calling file will be available within the called file, from that point foward. However, all functions and classes defined in the included file have the global scope.

Basic include example

vars.php

```php
<?php
$color = 'green';
$fruit = 'apply';
?>
```

test.php

```php
<?php

echo "A $color $fruit"; // A 

include 'vars.php';

echo "A $color $fruit"; // A green apple
?>
```

#### Example #5 insert date in Employees table

```php
<?php include('conn-db.php');
//
// 
//

$sql = "INSERT INTO EMPLOYEES (first_name, last_name, email, 
phone_number, hire_date, salary, department_ID)
VALUES ('Muhammad', 'Ahmad', 
'mahmad@example..com','0300-0000000','2016-12-19',10000,1)";

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>
```

#### Example #6 Add new department

save file with php extension.

```php
<!DOCTYPE html>
<html lang="en">

<head>
    <title> Add New Department</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="css/style.css" rel="stylesheet">
</head>

<body>
    <h3> Add new Department </h3>
    <form action="insert-dept.php" method="POST">
        <label>Department Name:<input type="text" name="txtDepartmentName"/> </label>
        <input type="submit" />
    </form>
</body>

</html>
```

save the below as **insert-dept.php**

```php
<?php include('conn-db.php');
//
// insert date in Employees table 
//
$department_name = $_POST["txtDepartmentName"];
$sql = "INSERT INTO DEPARTMENTS (department_name) 
VALUES ('$department_name')";

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully<br>";
    echo "Department Name: $department_name";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>
```

mysqli::multi_query
multi_query() - function performs one or more queries against the database. The queries are separated with a semicolon.

#### Example #7 run multiple queries

```php
<?php include('conn-db.php');
//
// Multiple statement
//

$sql =  "INSERT INTO DEPARTMENTS (department_name) 
VALUES ('CS and IT');";
$sql .= "INSERT INTO DEPARTMENTS (department_name) 
VALUES ('zoology');";
$sql .= "INSERT INTO DEPARTMENTS (department_name) 
VALUES ('botany');";
$sql .= "INSERT INTO DEPARTMENTS (department_name) 
VALUES ('english');";
$sql .= "INSERT INTO DEPARTMENTS (department_name) 
VALUES ('urdu');";
$sql .= "INSERT INTO DEPARTMENTS (department_name) 
VALUES ('math');";


if ($conn->multi_query($sql) === TRUE) {
    echo "New records created successfully<br>";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>
```

mysqli_result::$num_rows
num_rows - Gets the number of rows in a result

mysqli_result::fetch_assoc

- Returns an associative array of strings representing the fetched row in the result set, where each key in the array represents the name of one of the result set's columns or NULL if there are no more rows in resultset.
- Field names returned by this function are case-sensitive.

#### Example #8 select data

```php
<?php include('conn-db.php');
//
// Select Data
//
$sql = "SELECT department_id, department_name FROM DEPARTMENTS";

$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    echo 'Department ID' . ' - ' . 'Department Name' . "<br>";
    while($row = $result->fetch_assoc()) {
        echo $row["department_id"]. "  -----  " . $row["department_name"] ."<br>";
    }
} else {
    echo "0 results";
}
$conn->close();
?>
```

#### Example #9 select data

```php
<?php include('conn-db.php');
//
// Select Data
//
$sql = "SELECT department_id, department_name FROM DEPARTMENTS";

$result = $conn->query($sql);

if (!($result->num_rows > 0)) {
die('select query failed' . $conn->error);
}
?>
<html>
<head>
	<title>Displaying MySQL Data in HTML Table</title>
    <!-- link bootstrap -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    </head>
<body>
    <h1>Select Data from Departments</h1>
    <table class="table table-striped">
        <caption>Departments</caption>
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
            </tr>
        </thead>
        <tbody>
		<?php
		while ($row = $result->fetch_assoc())
		{
			echo '<tr>
					<td>'.$row['department_id'].'</td>
					<td>'.$row['department_name'].'</td>
				</tr>';
			
		}?>
		</tbody>
		<tfoot>
			<tr>
				<th>Total </th>
				<th><?php echo $result->num_rows; ?></th>
			</tr>
		</tfoot>
	</table>

    <?php $conn->close(); ?>
</body>
</html>
```

## References and Bibliography

[1]: https://www.mysql.com/ "MySQL"
[2]: http://www.w3schools.com/php/php_mysql_intro.asp "PHP MySQL Database - w3schools"
[3]: http://php.net/manual/en/function.include.php "include - PHP Documentation"

