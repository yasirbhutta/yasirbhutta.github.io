# PHP

- [PHP](../docs/index.md)
- [Download examples code](https://github.com/yasirbhutta/php-examples/tree/master/arrays)

## Array PHP

### What is an Array?

An array is a special variable, which can hold more than one value at a time.

### Create an Array in PHP

In PHP, the array() function is used to create an array:

### Array Types

- **Indexed arrays** - Arrays with a numeric index
- **Associative arrays** - Arrays with named keys
- **Multidimensional arrays** - Arrays containing one or more arrays

### Example #1

```php
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>PHP - Indexed Arrays</title>
    </head>
    <body>
    <?php
// index always starts at 0
// $cars = array("Volvo", "BMW", "Toyota");

$cars[0] = "Volvo";
$cars[1] = "BMW";
$cars[2] = "Toyota";

$cars[10] = "Toyota";

echo "I like " . $cars[0] . ", " . $cars[1] . " and " . $cars[2] . ".";

//
// Get The Length of an Array count()
//

echo "<br>Number of elements" . count($cars);
//
// Loop through an index array
//

$arrlength = count($cars);

for($x = 0; $x < $arrlength; $x++) {
    echo $cars[$x];
    echo "<br>";
}
?>
    </body>
</html>
```

#### Associative Array

- An array in PHP is actually an ordered map.
- A map is a type that associates values to keys. 
- This type is optimized for several different uses; it can be treated as an array, list (vector), hash table (an implementation of a map), dictionary, collection, stack, queue, and probably more.
- As array values can be other arrays, trees and multidimensional arrays are also possible.

##### Syntax

- Specifying with array()
- An array can be created using the array() language construct. It takes any number of comma-separated key => value pairs as arguments.

> array(  
    key  => value,  
    key2 => value2,  
    key3 => value3,  
    ...  
)  

**Note:** A short array syntax exists which replaces array() with [].

#### Example #1 A simple array

```php
<?php
$array = array(
    "foo" => "bar",
    "bar" => "foo",
);

// Using the short array syntax
$array = [
    "foo" => "bar",
    "bar" => "foo",
];
?>
```

The key can either be an int or a string. The value can be of any type.

#### Example #2

```php
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>PHP - Associative Arrays</title>
    </head>
    <body>
    <?php
//Associative arrays are arrays that use named keys that you assign to them.
$age = array("ahmad"=>"35", "ali"=>"37", "hamza"=>"43");

/*$age['ahmad'] = "35";
$age['ali'] = "37";
$age['hamza'] = "43";*/

echo "Ahmad is " . $age['ahmad'] . " years old.";
//
//Loop Through an Associative Array
//
/*foreach($age as $x => $x_value) {
    echo "Key=" . $x . ", Value=" . $x_value;
    echo "<br>";
}*/

?>
    </body>
</html>
```

##### current

- **current** — Return the current element in an array
- Every array has an internal pointer to its "current" element, which is initialized to the first element inserted into the array.
- The current() function simply returns the value of the array element that's currently being pointed to by the internal pointer.
- It does not move the pointer in any way. 
- If the internal pointer points beyond the end of the elements list or the array is empty, current() returns false.

##### next

- **next** — Advance the internal pointer of an array
- **next()** behaves like **current()**, with one difference.It advances the internal array pointer one place forward before returning the element value. That means it returns the next array value and advances the internal array pointer by one.
- Returns the array value in the next place that's pointed to by the internal array pointer, or false if there are no more elements.

##### Example #1 Example use of current(), next() and friends

```php
<?php
$transport = array('foot', 'bike', 'car', 'plane');
$mode = current($transport); // $mode = 'foot';
$mode = next($transport);    // $mode = 'bike';
$mode = next($transport);    // $mode = 'car';
$mode = prev($transport);    // $mode = 'bike';
$mode = end($transport);     // $mode = 'plane';
?>
```

##### key

- **key** — Fetch a key from an array
- **key()** returns the index element of the current array position.
- The key() function simply returns the key of the array element that's currently being pointed to by the internal pointer. It does not move the pointer in any way. 
- If the internal pointer points beyond the end of the elements list or the array is empty, key() returns null.

##### Example #1 key() example

```php
<?php
$array = array(
    'fruit1' => 'apple',
    'fruit2' => 'orange',
    'fruit3' => 'grape',
    'fruit4' => 'apple',
    'fruit5' => 'apple');

// this cycle echoes all associative array
// key where value equals "apple"
while ($fruit_name = current($array)) {
    if ($fruit_name == 'apple') {
        echo key($array), "\n";
    }
    next($array);
}
?>
```

### Further reading

- [Arrays - Manual - PHP](https://www.php.net/manual/en/language.types.array.php)
- [current - Manual - PHP](https://www.php.net/manual/en/function.current.php)
- [next - Manual - PHP](https://www.php.net/manual/en/function.next.php)
- [key - Manual - PHP](https://www.php.net/manual/en/function.key.php)

Muhammad Yasir Bhutta

- [Web](https://yasirbhutta.github.io/)
- [Youtube](https://www.youtube.com/yasirbhutta)
- [Facebook](https://www.facebook.com/yasirbhutta786)
- [Twitter](https://twitter.com/yasirbhutta)
