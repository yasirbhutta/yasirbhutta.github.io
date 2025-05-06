
## switch statement

- The PHP switch statement is a control structure that allows you to execute different blocks of code based on the value of a variable or expression. It's a cleaner alternative to multiple if-else statements when dealing with numerous conditions. ([Codecademy][1])

**Syntax:**

```php
switch ($variable) {
    case 'value1':
        // Code to execute if $variable == 'value1'
        break;
    case 'value2':
        // Code to execute if $variable == 'value2'
        break;
    default:
        // Code to execute if $variable doesn't match any case
}
```

**Key points:**

* **Evaluation:** The expression inside the switch is evaluated once.
* **Case Matching:** Each case is compared to the switch expression using loose comparison (`==`).
* **Break Statement:** The `break` keyword prevents the code from running into the next case. Omitting `break` can lead to unintended fall-through behavior.
* **Default Case:** The `default` case is executed if no matching case is found. It's good practice to include it to handle unexpected values.([W3Schools.com][2], [DEV Community][3], [Stack Overflow][4])

**Example:**

```php
$day = 'Monday';

switch ($day) {
    case 'Monday':
        echo "Start of the work week.";
        break;
    case 'Friday':
        echo "End of the work week.";
        break;
    default:
        echo "Midweek days.";
}
```



In this example, if `$day` is 'Monday', it will output "Start of the work week." If it's 'Friday', it will output "End of the work week." For any other value, it will output "Midweek days."([Wikipedia][5])

**Best Practices:**

* **Use `break` Statements:** Always include `break` statements to prevent fall-through unless intentionally desired.
* **Default Case:** Include a `default` case to handle unexpected values.
* **Avoid Complex Expressions:** Keep case expressions simple to maintain readability.
* **Consistent Syntax:** Stick to a consistent syntax style (either colons or semicolons) for clarity.([TutorialsPoint][6], [Wikipedia][5])

The statement list for a case can also be empty, which simply passes control into the statement list for the next case.

### Example #2 switch with empty case example

```php
<?php
switch ($i) {
    case 0:
    case 1:
    case 2:
        echo "i is less than 3 but not negative";
        break;
    case 3:
        echo "i is 3";
}
?>
```

**Explanation:** To understand how this example works in detail, see [Switch-Case Example in PHP: Handling Multiple Cases Together](switch/solutions/switch-example3.md).

A special case is the default case. This case matches anything that wasn't matched by the other cases. For example:

### Example #3 default case

```php
<?php

$i = 1
switch ($i) {
    case 0:
        echo "i equals 0";
        break;
    case 1:
        echo "i equals 1";
        break;
    case 2:
        echo "i equals 2";
        break;
    default:
       echo "i is not equal to 0, 1 or 2";
}
?>
```

### Example #4 switch example

```php
<!DOCTYPE html>
<html lang="en">

<head>
    <title>PHP - Switch</title>
</head>

<body>
    <h1>PHP - Switch</h1>
    <?php
$favcolor = "blue";
echo "<h2>My favorite color is " . $favcolor . "</h2>";
switch ($favcolor) {
    case "red":
        echo "<h2 style='color:" . $favcolor . "'>Your favorite color is red!</h2>";
        break;
    case "blue":
        echo "<h2 style='color:" . $favcolor . "'>Your favorite color is blue!</h2>";
        break;
    case "green":
        echo "<h2 style='color:" . $favcolor . "'>Your favorite color is green!</h2>";
        break;
    default:
        echo "Your favorite color is neither red, blue, nor green!";
}
?>
</body>
</html>
```

For more detailed information, refer to the [PHP Manual on switch statements](https://www.php.net/manual/en/control-structures.switch.php).

## References and Bibliography

[1]: https://www.codecademy.com/resources/docs/php/switch "Switch - PHP - Codecademy"
[2]: https://www.w3schools.com/php/php_switch.asp "PHP switch Statement - W3Schools"
[3]: https://dev.to/klnjmm/be-careful-about-the-switch-statement-in-php-d8d "Be careful about the switch statement in PHP - DEV Community"
[4]: https://stackoverflow.com/questions/37881440/switch-case-statement-in-php "Switch case statement in PHP - Stack Overflow"
[5]: https://en.wikipedia.org/wiki/PHP_syntax_and_semantics "PHP syntax and semantics"
[6]: https://www.tutorialspoint.com/php/php_switch_statement.htm "PHP Switch Statement - Tutorialspoint"
