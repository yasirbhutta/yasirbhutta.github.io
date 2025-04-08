---
layout: default
title: Understanding Python's os.getcwd(): Get Current Working Directory with Examples
description: "Learn how to use Python's os.getcwd() to get the current working directory with examples. Enhance your coding skills with this beginner-friendly guide."
---

# Understanding Python's os.getcwd(): Get Current Working Directory with Examples

`os.getcwd()` is a function in Python that returns the current working directory (CWD) of the script. The "current working directory" is the folder from which your Python script is running. It is useful for figuring out the exact location of the script during execution.

**Explanation:**
- **`os`**: This is the module in Python that provides a way to interact with the operating system.
- **`getcwd()`**: This function within the `os` module returns a string representing the current working directory.

**Example:**

```python
import os

# Get the current working directory
current_directory = os.getcwd()

# Print the current working directory
print("Current Working Directory:", current_directory)
```

**Output:**
If you run this script, you might get an output like this (depending on where the script is being executed):

```
Current Working Directory: /Users/yourusername/Documents/my_project
```

This tells you that the script is being run from the `/Users/yourusername/Documents/my_project` directory.

**Use Case:**
Imagine you are writing a script that needs to read or write files. Knowing the current working directory will help ensure you reference the correct paths to those files.

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1602443888929206"
     crossorigin="anonymous"></script>
<ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-1602443888929206"
     data-ad-slot="6296238623"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>