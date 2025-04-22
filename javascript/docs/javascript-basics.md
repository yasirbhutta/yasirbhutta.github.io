---
layout: page
title: "Javascript Basics" 
description: ""  
keywords: ""
toc: ""
topic: ""
course: ""
prev: /python/docs/control-flow.html
next: /python/docs/functions.html
---

```javascript
<!DOCTYPE html>
<html lang="en">

<head>
    <title>JavaScript - Hello world </title>
</head>

<body>
    <p>Before the script ....</p>
    <script type="text/javascript">
        document.write("Hello World Wide Web");
    </script>
</body>

</html>
```

```javascript
<!DOCTYPE html>
<html lang="en">

<head>
    <title>JavaScript - Hello world </title>
</head>

<body>
    <p>Before the script ....</p>
    <script>
        alert('Hello, world!');
    </script>
</body>

</html>
```

### example

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <title>JavaScript - Hello world </title>
    
</head>

<body>
    <h1 id="demo">ALLAH</h1>
    <p>And speak to people good words.</p>
    <form>
        <input type="button" value="click" onclick="msg()" />
    </form>
    <script type="text/javascript" src="../javascript-examples/scripts/hello.js"></script>
</body>

</html>
```

javascript file in subfolder 'scripts/hello.js'

```javascript
function msg() {
    //
    // The innerHTML property sets or returns the HTML content (inner HTML) of an element.
    //
    document.getElementById("demo").innerHTML = "Ya ALLAH!....";
}  
```

## use of prompt()

### Example

```javascript
<!DOCTYPE html>
<html lang="en">

<head>
    <title>JavaScript -Functions </title>
</head>
<body>
    <h1> JavaScript Functions </h1>
    <blockquote> "You have to dream before your dreams can come true." 
        - A. P. J. Abdul Kalam</blockquote>
    <form>
        <button onclick="doShowName()"> Click here</button>
    </form>
    <script type="text/javascript">
        function doShowName() {
            var name = prompt('What is your name ?');
            alert(name + ', you just did something awesome!');
        }
    </script>
</body>
</html>
```

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <title>JavaScript -Functions </title>
</head>
<body>
    <h1> JavaScript Functions </h1>
    <blockquote> "You have to dream before your dreams can come true." 
        - A. P. J. Abdul Kalam</blockquote>
    <script type="text/javascript">
        function multiply(num1, num2) {
            var result = num1 * num2;
            return result;
        }
        a = multiply(5, 6);
        alert('Multiple  = ' + a);
        b = multiply(8, 4);
        alert('Multiple  = ' + b);
    </script> 
</body>
</html>
```

```javascript
<!DOCTYPE html>
<html lang="en">

<head>
    <title>JavaScript - Functions </title>

</head>

<body>
    <h1 id="demo">.............. </h1>
    <p>Ya Allah, give me eyes that see the best in people, a heart that forgives the worst, a mind that forgets the bad, and
        a soul that never loses faith. Ameen.
    </p>
    <script type="text/javascript">
        document.getElementById("demo").innerHTML = "Ya ALLAH!....";
    </script>
</body>

</html>
```

```javascript
<!DOCTYPE html>
<html lang="en">

<head>
    <title>JavaScript - Variables </title>

</head>

<body>
    <script type="text/javascript">
        //
        // String
        //
        var str;
        str = 'Hello world';  // or "Hello world"
        document.write(str);
        document.write("<br />")
        //
        // Number
        //
        var a = 5, b = 10;
        c = a + b;
        document.writeln(c);
        //
        //
        //
        var myVar = 1;   // variable tye is number
        myVar = "Allah is the Greatest" // string
        document.write("<h1>"+myVar+"</h1>");

    </script>
</body>
</html>
```

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

### Using `defer` (modern best practice)

You can place your script in the `<head>` **with** `defer`:

```html
<head>
  <script src="script.js" defer></script>
</head>
```

- `defer` tells the browser to download the script while parsing HTML but only run it after the DOM is fully parsed.

---
