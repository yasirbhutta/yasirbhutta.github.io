# Python Exercise for Regular Expressions: Password Validator Program

**Objective:**  
Write a Python program that asks the user to enter a password and checks whether it is **valid** based on the following rules:

1. The password must be **at least 8 characters long**.  
2. It must contain **at least one uppercase letter** (A–Z).  
3. It must contain **at least one lowercase letter** (a–z).  
4. It must contain **at least one number** (0–9).  
5. It must contain **at least one special character** (e.g., `!@#$%^&*()_+-=[]{}|;:'",.<>?/`).

**Your program should:**
- Tell the user if the password is valid or not.
- If invalid, print the specific rule(s) that were not met.

**Code Challenge:** Allow the user to keep trying until they enter a valid password.

## Solution

```python
import re

def is_valid_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):  # At least one uppercase letter
        return False
    if not re.search(r"[a-z]", password):  # At least one lowercase letter
        return False
    if not re.search(r"\d", password):     # At least one digit
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):  # Special character
        return False
    return True

# Example usage
password = input("Enter your password: ")
if is_valid_password(password):
    print("Valid password")
else:
    print("Invalid password")
```

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

---

Here’s an enhanced version that tells the user exactly which rules their password failed:

```python
import re

def validate_password(password):
    errors = []

    if len(password) < 8:
        errors.append("Password must be at least 8 characters long.")
    if not re.search(r"[A-Z]", password):
        errors.append("Password must contain at least one uppercase letter.")
    if not re.search(r"[a-z]", password):
        errors.append("Password must contain at least one lowercase letter.")
    if not re.search(r"\d", password):
        errors.append("Password must contain at least one number.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        errors.append("Password must contain at least one special character.")

    return errors

# Example usage
password = input("Enter your password: ")
validation_errors = validate_password(password)

if not validation_errors:
    print("Valid password.")
else:
    print("Invalid password:")
    for error in validation_errors:
        print("-", error)
```

For more python exercises, see [Python Exercises](../index.md)

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1602443888929206"
     crossorigin="anonymous"></script>
<!-- display square -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-1602443888929206"
     data-ad-slot="9845543342"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

