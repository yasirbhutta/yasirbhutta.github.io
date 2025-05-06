
# Switch-Case Example in PHP: Handling Multiple Cases Together

This PHP example demonstrates how to use the `switch` statement to handle multiple conditions for a variable. It shows how different `case` labels can be grouped to execute the same block of code, which is useful when multiple values require the same output or logic. Specifically, the code checks the value of `$i` and:

* Outputs a common message for values `0`, `1`, or `2`
* Outputs a separate message when `$i` is `3`
* Does nothing if `$i` doesn't match any case

The `break` statement is used to prevent fall-through to other cases after a match is found.


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

### Explanation:

* `switch ($i)` checks the value of the variable `$i` and matches it against the cases provided.
* `case 0:`, `case 1:`, and `case 2:` are grouped together **without a `break` between them**, which means if `$i` is 0, 1, or 2, it will execute the same block of code.

  * It will print: `i is less than 3 but not negative`
* The `break;` statement stops the switch-case execution after matching case 0/1/2.
* `case 3:` is a separate case that will print `i is 3` if `$i == 3`.

### Example Outputs:

* If `$i = 1`, output will be: `i is less than 3 but not negative`
* If `$i = 3`, output will be: `i is 3`
* If `$i = 5`, there is **no matching case**, so it will **output nothing**




