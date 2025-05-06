---
layout: page
title: "Why You Should Always Use unset($value); After a foreach Loop in PHP"
description: Learn why using unset($value); after a foreach loop in PHP is essential to prevent unexpected behavior. Understand how references work and how to safely modify array elements with examples.
keywords: PHP foreach loop, unset($value); in PHP, PHP references, PHP foreach reference bug, PHP array manipulation, PHP foreach loop best practices, PHP array modification by reference, Break reference in PHP foreach, PHP unset function usage
toc: toc/php.html
course: php
topic: "control-flow"
mini_project: true
prev: /php/docs/loops-foreach/
---

When you use `&$value` in a `foreach` loop, like this:

```php
foreach ($arr as &$value) {
    $value = $value * 2;
}
```

PHP creates a **reference** to the array element, not a copy. After the loop ends, `$value` still **points to the last element** of the array.

That means if you **use `$value` later in your code**, you might accidentally change the last element of the array — even without realizing it.

---

### ⚠️ Example Without `unset($value);`

```php
<?php
$arr = [1, 2, 3];

foreach ($arr as &$value) {
    // Doubles each element
    $value *= 2;
}

// Oops! This modifies the last element again!
$value = 99;

print_r($arr);
?>
```

**Output:**

```
Array
(
    [0] => 2
    [1] => 4
    [2] => 99  // ← unexpected!
)
```

---

### ✅ Example With `unset($value);`

```php
<?php
$arr = [1, 2, 3];

foreach ($arr as &$value) {
    $value *= 2;
}
unset($value); // break the reference

$value = 99; // Now this does NOT affect $arr

print_r($arr);
?>
```

**Output:**

```
Array
(
    [0] => 2
    [1] => 4
    [2] => 6  // ← safe and expected
)
```

---

### 🔑 Summary:

* Use `unset($value);` to **break the lingering reference** after a `foreach` loop with `&`.
* This helps prevent accidental changes to your original array.

