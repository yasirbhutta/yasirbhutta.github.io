---
layout: page
title: "PHP foreach Loop Tutorial with Syntax and Examples"
description: earn how to iterate over arrays using the foreach loop in PHP. See real-world examples, syntax breakdown, and use cases for better PHP code.
keywords: php foreach loop, foreach php example, php array loop, php loops tutorial, php foreach syntax, php programming, control structures in php, php docs
toc: toc/php.html
course: php
topic: "control-flow"
mini_project: true
prev: /php/docs/loops-for/
next: /php/docs/loops-while/
---

## 🔄 PHP `foreach` Loop

The `foreach` loop is used to **iterate over arrays or objects** in PHP. It’s the easiest way to go through each element in an array.

---

### ✅ Basic Syntax

There are two main ways to use `foreach`:

```php
// Value only
foreach ($array as $value) {
    // Code using $value
}
```

```php
// Key and value
foreach ($array as $key => $value) {
    // Code using $key and $value
}
```

* `$value` holds the current item in the array.
* `$key` holds the current key (index or name) of the item.

---

### 🛠 Modifying Array Items

If you want to **change the array values directly**, use `&` to reference the value:

```php
foreach ($array as &$value) {
    $value = $value * 2;
}
unset($value); // Always unset to avoid unexpected bugs!
```
for more details about `unset`, see [Why You Should Always Use unset($value); After a foreach Loop in PHP](unset.md)
---

### 🚨 Important:

* `foreach` **only works with arrays and objects**.
* Always `unset($value)` after using a reference to prevent accidental changes later.

---

## 🔍 Examples

### 🔸 Example 1: Simple `foreach` Loop

```php
<?php
$colors = array("red", "green", "blue");

foreach ($colors as $color) {
    echo "Color: $color <br>";
}
?>
```

**Output:**

```
Color: red  
Color: green  
Color: blue
```

---

### 🔸 Example 2: Using Keys and Values

```php
<?php
$prices = array("apple" => 50, "banana" => 20);

foreach ($prices as $item => $cost) {
    echo "$item costs $cost rupees<br>";
}
?>
```

**Output:**

```
apple costs 50 rupees  
banana costs 20 rupees
```

---

### 🔸 Example 3: Styling with HTML

```php
<!DOCTYPE html>
<html>
<head><title>Colors</title></head>
<body>

<?php
$colors = array("red", "green", "blue");

foreach ($colors as $color) {
    echo "<h2 style='background-color:$color;'>$color</h2>";
}
?>

</body>
</html>
```

---

### 🔸 Example 4: Nested Arrays

```php
<?php
$matrix = [
    [1, 2],
    [3, 4]
];

foreach ($matrix as $row) {
    foreach ($row as $item) {
        echo "$item ";
    }
    echo "<br>";
}
?>
```

**Output:**

```
1 2  
3 4
```

---

### 🔸 Example 5: Inline Array

```php
<?php
foreach (array("a", "b", "c") as $letter) {
    echo $letter . "<br>";
}
?>
```

---

## 🧠 Key Tips

* Use `foreach` when working with arrays — it’s simpler and safer than a `for` loop.
* If you don’t need the key, use the shorter form: `foreach ($arr as $value)`.
* Always be careful when modifying array elements by reference (use `unset()` afterward).

---

Would you like an infographic or diagram explaining how `foreach` works step-by-step?


Further reading:

- [foreach - Manual - PHP](https://www.php.net/manual/en/control-structures.foreach.php)
