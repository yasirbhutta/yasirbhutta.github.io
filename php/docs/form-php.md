# PHP

- [PHP](../docs/index.md)

**updated on:** 19-Dec-2022

## Form PHP

- [Download PDF](https://drive.google.com/drive/folders/1X7QUy7Yep4t1DefMlCWeRu4uXaheD5FU?usp=sharing)
- [Download examples code](https://github.com/yasirbhutta/php-examples/tree/master/forms)

### Example #1 

```html
<html>

<body>

    <form action="welcome-get.php" method="get">
        Name: <input type="text" name="name"><br> E-mail: <input type="text" name="email"><br>
        <input type="submit">
    </form>

</body>

</html>
```

welcome-get.php

```php
<html>
<body>

Welcome <?php echo $_GET["name"]; ?><br>
Your email address is: <?php echo $_GET["email"]; ?>

</body>
</html>
```

### Example #2

welcome.html

```html
<html>
<body>
    <form action="welcome.php" method="post">
       <label> Name: <input type="text" name="name"></label><br/><br/>
        <label>Email: <input type="text" name="email"></label><br/><br/>
        <input type="submit">
    </form>

</body>

</html>
Footer
```

welcome.php

```php
<!DOCTYPE html>
<html lang="en">
    <head>
        <title></title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="css/style.css" rel="stylesheet">
    </head>
    <body>
        <p>
    Welcome 
    <?php echo $_POST["name"];?> </p>
    <br/>
    <p>
Your email address is: 
<?php echo $_POST["email"];?></p>

    </body>
</html>

```

### Example #3

```php
<!-- https://html.form.guide/php-form/php-form-action-self/-->


<?php
if(isset($_POST['submit'])) 
{ 
    $name = $_POST['name'];
    echo "User Has submitted the form and entered this name : <b> $name </b>";
    echo "<br>You can use the following form again to enter a new name."; 
}
?>

<form method="post" action="<?php echo $_SERVER['PHP_SELF']; ?>">
   <input type="text" name="name"><br>
   <input type="submit" name="submit" value="Submit Form"><br>
</form>


<!-- PHP_SELF variable can be exploited. using following URL -->
<!-- http://www.yourdomain.com/form-action.php/%22%3E%3Cscript%3Ealert('xss')%3C/script%3E%3Cfoo%22 -->
```

### Example #4

```php
<!-- https://html.form.guide/php-form/php-form-action-self/-->

<?php
if(isset($_POST['submit'])) 
{ 
    $name = $_POST['name'];
    echo "User Has submitted the form and entered this name : <b> $name </b>";
    echo "<br>You can use the following form again to enter a new name."; 
}
?>

<form name="test" action="<?php echo htmlentities($_SERVER['PHP_SELF']); ?>" method="post">
   <input type="text" name="name"><br>
   <input type="submit" name="submit" value="Submit Form"><br>
</form>


<!-- PHP_SELF variable can be exploited. using following URL -->
<!-- http://www.yourdomain.com/form-action.php/%22%3E%3Cscript%3Ealert('xss')%3C/script%3E%3Cfoo%22 -->

<!-- output of htmlentities -->

<!-- <form name="test" method="post" 
action="form-action.php/&quot;&gt;&lt;script&gt;alert('xss')&
lt;/script&gt;&lt;foo"> -->
```

### Example #5

```php
<html>
<head>
<style>
.error {color: red;}
</style>
</head>
<body>
<?php
$name=$email="";
$nameErr=$emailErr="";
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    //
    // validation of name 
    //
  if (empty($_POST["name"])) 
  {
  $nameErr = "Name is required";}
    else
    {
    $name=$_POST["name"];
    }
    //
    // validation of email
    //
  if (empty($_POST["email"])) 
  {
  $emailErr = "Email is required";}
    else
    {
    $email=$_POST["email"];
    }
}

?>

    <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>" method="post">

       <label> Name: <input type="text" name="name" value="<?php echo $name;?>"></label>
       <!-- span for error message -->
       <span class="error">* <?php echo $nameErr;?></span>
       <br/><br/>
        <label>Email: <input type="text" name="email"  value="<?php echo $email;?>"></label>
        <!-- span for error message -->
       <span class="error">* <?php echo $emailErr;?></span>
        <br/><br/>
        <input type="submit">
        <input type="reset">
    </form>

    <?php
    echo "<br>";
    echo "<br>";
echo "<h2>Your Input:</h2>";
echo $name;
echo "<br>";
echo $email;

?>

</body>

</html>

```

### Example #6

```php
<!DOCTYPE HTML>  
<html>
<head>
<style>
.error {color: #FF0000;}
</style>
</head>
<body>  

<?php
// define variables and set to empty values
$nameErr = $emailErr = $genderErr = $websiteErr = "";
$name = $email = $gender = $comment = $website = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  if (empty($_POST["name"])) {
    $nameErr = "Name is required";
  } else {
    $name = test_input($_POST["name"]);
    // check if name only contains letters and whitespace
    if (!preg_match("/^[a-zA-Z ]*$/",$name)) {
      $nameErr = "Only letters and white space allowed"; 
    }
  }
  
  if (empty($_POST["email"])) {
    $emailErr = "Email is required";
  } else {
    $email = test_input($_POST["email"]);
    // check if e-mail address is well-formed
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
      $emailErr = "Invalid email format"; 
    }
  }
    
  if (empty($_POST["website"])) {
    $website = "";
  } else {
    $website = test_input($_POST["website"]);
    // check if URL address syntax is valid (this regular expression also allows dashes in the URL)
    if (!preg_match("/\b(?:(?:https?|ftp):\/\/|www\.)[-a-z0-9+&@#\/%?=~_|!:,.;]*[-a-z0-9+&@#\/%=~_|]/i",$website)) {
      $websiteErr = "Invalid URL"; 
    }
  }

  if (empty($_POST["comment"])) {
    $comment = "";
  } else {
    $comment = test_input($_POST["comment"]);
  }

  if (empty($_POST["gender"])) {
    $genderErr = "Gender is required";
  } else {
    $gender = test_input($_POST["gender"]);
  }
}

function test_input($data) {
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}
?>

<h2>PHP Form Validation Example</h2>
<p><span class="error">* required field.</span></p>
<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">  
  Name: <input type="text" name="name" value="<?php echo $name;?>">
  <span class="error">* <?php echo $nameErr;?></span>
  <br><br>
  E-mail: <input type="text" name="email" value="<?php echo $email;?>">
  <span class="error">* <?php echo $emailErr;?></span>
  <br><br>
  Website: <input type="text" name="website" value="<?php echo $website;?>">
  <span class="error"><?php echo $websiteErr;?></span>
  <br><br>
  Comment: <textarea name="comment" rows="5" cols="40"><?php echo $comment;?></textarea>
  <br><br>
  Gender:
  <input type="radio" name="gender" <?php if (isset($gender) && $gender=="female") echo "checked";?> value="female">Female
  <input type="radio" name="gender" <?php if (isset($gender) && $gender=="male") echo "checked";?> value="male">Male
  <span class="error">* <?php echo $genderErr;?></span>
  <br><br>
  <input type="submit" name="submit" value="Submit">  
</form>

<?php
echo "<h2>Your Input:</h2>";
echo $name;
echo "<br>";
echo $email;
echo "<br>";
echo $website;
echo "<br>";
echo $comment;
echo "<br>";
echo $gender;
?>

</body>
</html>

```