---
layout: page
title: "C++ Escape Sequences Tutorial"
description: "Learn C++ escape sequences with practical examples. Understand newline, tab, quote, backslash, and other special characters used in output strings and beginner C++ programs."
keywords: C++ escape sequences, C++ newline escape sequence, C++ tab escape, C++ backslash escape, escape characters in C++, C++ string special characters, C++ output formatting, learn C++ escape sequences, C++ tutorial, C++ examples
---

## What are Escape Sequences?

**Escape sequences** are special characters used inside a C++ string to perform a specific action or display special characters.

An escape sequence usually starts with a **backslash (`\`)**.

### Common Escape Sequences

| Escape Sequence | Name            | Purpose                                               |
| --------------- | --------------- | ----------------------------------------------------- |
| `\n`            | Newline         | Moves the cursor to the next line                     |
| `\t`            | Tab             | Adds a horizontal tab space                           |
| `\\`            | Backslash       | Displays a backslash `\`                              |
| `\"`            | Double Quote    | Displays a double quotation mark `"`                  |
| `\'`            | Single Quote    | Displays a single quotation mark `'`                  |
| `\r`            | Carriage Return | Moves the cursor to the beginning of the current line |

---

# 1. Newline – `\n`

### What is `\n`?

The `\n` escape sequence is used to **move the cursor to the next line**.

It is similar to using `endl`.

### Question

Write a C++ program that prints two lines of text using the newline escape sequence `\n`.

### Example

```cpp
#include <iostream>
using namespace std;

int main() {

    cout << "Hello World!\n";
    cout << "Welcome to C++.";

    return 0;
}
```

### Output

```text
Hello World!
Welcome to C++.
```

### Understand the Code

```cpp
cout << "Hello World!\n";
```

The `\n` moves the cursor to the next line. Therefore, the second `cout` statement starts on a new line.

### Remember

```text
\n → New line
```

---

# 2. Tab – `\t`

### What is `\t`?

The `\t` escape sequence inserts a **horizontal tab space**.

It is useful for creating simple columns in output.

### Question

Write a C++ program that displays a list of items and their prices using `\t` to separate the columns.

### Example

```cpp
#include <iostream>
using namespace std;

int main() {

    cout << "Item\tPrice\n";
    cout << "Apple\t100\n";
    cout << "Mango\t150\n";

    return 0;
}
```

### Output

```text
Item    Price
Apple   100
Mango   150
```

### Understand the Code

```cpp
cout << "Apple\t100\n";
```

* `\t` adds a tab space between `Apple` and `100`.
* `\n` moves the cursor to the next line.

### Remember

```text
\t → Tab space
```

---

# 3. Backslash – `\\`

### What is `\\`?

The backslash character `\` has a special meaning in C++.

If we want to **display an actual backslash**, we use two backslashes:

```cpp
\\
```

### Question

Write a C++ program that displays a Windows file path containing backslashes.

### Example

```cpp
#include <iostream>
using namespace std;

int main() {

    cout << "File path: C:\\Users\\Student\\Documents";

    return 0;
}
```

### Output

```text
File path: C:\Users\Student\Documents
```

### Understand the Code

In the program:

```cpp
C:\\Users\\Student\\Documents
```

Each `\\` represents **one actual backslash** in the output.

### Remember

```text
\\ → Displays \
```

---

# 4. Double Quote – `\"`

### What is `\"`?

A double quotation mark `"` normally marks the beginning or end of a string.

If we want to display a double quotation mark **inside a string**, we use:

```cpp
\"
```

### Question

Write a C++ program that prints a sentence containing double quotation marks.

### Example

```cpp
#include <iostream>
using namespace std;

int main() {

    cout << "He said, \"C++ is fun!\"";

    return 0;
}
```

### Output

```text
He said, "C++ is fun!"
```

### Understand the Code

```cpp
\"C++ is fun!\"
```

The `\"` tells C++ to display a quotation mark instead of treating it as the end of the string.

### Remember

```text
\" → Displays "
```

---

# 5. Single Quote – `\'`

### What is `\'`?

The `\'` escape sequence can be used to display a **single quotation mark**.

### Question

Write a C++ program that prints a character enclosed in single quotation marks.

### Example

```cpp
#include <iostream>
using namespac
```
