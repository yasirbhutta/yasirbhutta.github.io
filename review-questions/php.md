# Review Questions

## Introduction to PHP

1. How does a Web server determine whether a requested document includes PHP code?

1. What are the syntax and semantics of the include construct?

1. Which parts of PHP are case sensitive and which are not?

1. What are the four scalar types of PHP?

1. How many bytes are used to store a character in PHP?

1. What are the differences between single- and double-quoted literal strings?

1. If a variable stores a string, how can the character at a specific position in that string be referenced?

1. How can the type of a variable be determined?

1. If a string is compared with a number, what happens?

1. What keys are used when an array is created but no keys are specified?

1. Must all of the values of an array be of the same type?

1. Must all of the keys of an array be of the same type?

1. What exactly do the array_keys and array_values functions do?

1. Describe the actions of the next, reset, and prev functions.

1. What are the syntax and semantics of the two forms of the foreach statement?

1. Describe the result of using the sort function on an array that has both string and numeric values.

1. What is the difference betweeen the sort and asort functions?

1. What happens if a script defines the same function more than once?

1. Are function names case sensitive?

1. What value is returned by a function if its execution does not end by executing a return statement?
 
1. What are the two ways you can specify that a parameter is to be passed by reference?

1. How can a variable used outside a function be accessed by the function?

1. How can you define a variable in a function so that its lifetime extends beyond the time the function is in its first execution?

1. How can the value of a form element be accessed by a PHP script?

1. Write function to sum two arguments and return value in PHP? 

1. Write an example of foreach loop using PHP code? 

1. Declare Global scope variable and explain use of global keyword with example?

1. Write code for comments in PHP language?

1. In what two ways can arrays in PHP to be created. 

1. Write an example of foreach loop using PHP code? 

1. Explain the purpose following string functions with examples in PHP: **strlen**, **strrev**, **strops**, **str_replace**

1. Write an example of foreach loop using PHP code?

1. Specify the PHP code to create an array with following items: **garlic**, **pepper**, **salt**, **chilli** and write code to display array values?

1. Write html code to display following FORM and also write PHP code to connect with database and store date in database? [Click here to view image](../images/html-form-user.png)

1. Write html code to display following FORM; PHP code to connect with database and store date in database and also code to select data from MySQL table using PHP. [Click here to view image](../images/html-form-user.png)

1. What will be the output of the following code?

```php
<?php 

    function track() {     static $count = 0;    $count++;    echo $count;    }     

 track();     track();    track();    ?> 
 ```
