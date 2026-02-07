---
layout: page
title: The `htmlspecialchars()` function in PHP is used to **convert special characters to HTML entities**. This is commonly used to **prevent Cross-Site Scripting (XSS)** attacks by making sure that HTML tags or JavaScript code entered by users are displayed as text and not executed by the browser.
description: The `htmlspecialchars()` function in PHP is used to convert special characters to HTML entities. This is commonly used to prevent Cross-Site Scripting...
keywords: html, htmlspecialchars, used, xss, script
---
The `htmlspecialchars()` function in PHP is used to **convert special characters to HTML entities**. This is commonly used to **prevent Cross-Site Scripting (XSS)** attacks by making sure that HTML tags or JavaScript code entered by users are displayed as text and not executed by the browser.

### 🔐 Why use it?

To make sure that:

* `<`, `>`, `"` and `'` are **not interpreted as HTML** or JavaScript.
* User-generated content is safely displayed in the browser.

---

### 🧪 Example:

```php
$user_input = "<script>alert('XSS');</script>";
$safe_output = htmlspecialchars($user_input);

echo $safe_output;
// Output: &lt;script&gt;alert(&#039;XSS&#039;);&lt;/script&gt;
```

---

### 🏷️ Common Flags:

| Flag           | Description                             |
| -------------- | --------------------------------------- |
| `ENT_COMPAT`   | Converts double quotes only (default).  |
| `ENT_QUOTES`   | Converts both double and single quotes. |
| `ENT_NOQUOTES` | Does not convert any quotes.            |
| `ENT_HTML401`  | Handle HTML 4.01 (default).             |
| `ENT_HTML5`    | Use for HTML5 documents.                |

---

### 📝 Notes:

* Always use `htmlspecialchars()` when displaying user input in HTML.
* Use `htmlspecialchars_decode()` if you need to revert the conversion.


