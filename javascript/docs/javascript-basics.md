


## FAQ 

### ✅ Yes, you *can* write JavaScript in the `<body>`:
You can put `<script>` tags in the `<body>` to execute JavaScript when the page loads:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Example</title>
  </head>
  <body>
    <h1>Hello World</h1>

    <script>
      alert("This runs from inside the body!");
    </script>
  </body>
</html>
```

### 📍 **Best location for JavaScript?**
The **best practice** is to place JavaScript **at the end of the `<body>`**, just before the closing `</body>` tag.

```html
<body>
  <!-- Page content here -->

  <script src="script.js"></script>
</body>
```

### ✅ Why?
- ✅ **Page loads faster** – The browser can load and render HTML content first.
- ✅ **DOM is ready** – If your script manipulates the DOM, placing it at the end ensures all elements are already loaded.
- ✅ **Avoids blocking** – JavaScript in the `<head>` can block HTML rendering unless you use the `defer` or `async` attributes.

---

### Bonus Tip: Using `defer` (modern best practice)

You can place your script in the `<head>` **with** `defer`:

```html
<head>
  <script src="script.js" defer></script>
</head>
```

- `defer` tells the browser to download the script while parsing HTML but only run it after the DOM is fully parsed.

---
