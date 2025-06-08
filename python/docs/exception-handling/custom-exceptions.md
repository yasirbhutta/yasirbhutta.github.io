---
layout: page
title: Creating Custom Exceptions
description: Learn how to handle Python errors and exceptions effectively. Fix common Python errors like SyntaxError, TypeError, and NameError with practical examples.
keywords: Python errors, Python exceptions, fix Python errors, SyntaxError Python, TypeError Python, NameError Python, Python error handling, Python debugging, Python try-except, Python exception handling
toc: toc/python.html
---

### 6. **Creating Custom Exceptions**
   - You can create your own exception classes by inheriting from Python's built-in `Exception` class.

   Example:
   ```python
   class NegativeNumberError(Exception):
       pass

   def check_number(num):
       if num < 0:
           raise NegativeNumberError("Negative numbers are not allowed.")
       else:
           print("Number is valid.")

   try:
       check_number(-5)
   except NegativeNumberError as e:
       print(f"Error: {e}")
   ```
