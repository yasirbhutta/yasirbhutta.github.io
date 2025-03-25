# HTML: **Difference Between `id` and `name` in Form Submission**  

Both `id` and `name` attributes are used in HTML forms, but they serve different purposes.

---

## **1. `name` Attribute:**
- **Purpose:** Used for form submission to identify data.
- **Required for:** Sending data to the server.
- **Scope:** Multiple elements can have the same `name` (useful for radio buttons).
- **Usage in Form Submission:** When the form is submitted, only fields with a `name` are included in the request.

✅ **Example:**
```html
<form action="submit.php" method="POST">
    <label for="username">Username:</label>
    <input type="text" id="username" name="username">
    <input type="submit" value="Submit">
</form>
```
- The server receives:  
  ```
  username=JohnDoe
  ```

---

## **2. `id` Attribute:**
- **Purpose:** Used to uniquely identify an element in JavaScript or CSS.
- **Required for:** Label association (`for` attribute), JavaScript, and styling.
- **Scope:** Must be unique within the page (cannot be repeated).
- **Usage in Form Submission:** **Does not affect data submission**.

✅ **Example:**
```html
<form action="submit.php" method="POST">
    <label for="email">Email:</label>
    <input type="email" id="email" name="user_email">
    <input type="submit" value="Submit">
</form>
```
- The server receives:
  ```
  user_email=example@mail.com
  ```
- The `id="email"` is used for the `<label>` but does **not** affect form submission.

---

### **Key Differences:**
| Feature     | `name` | `id` |
|------------|--------|------|
| Used for   | Form data submission | JavaScript, CSS |
| Server-side | Yes, data is sent with this name | No impact on submission |
| Uniqueness | Can be repeated (e.g., radio buttons) | Must be unique in the document |
| Associated with | Form processing | Styling, JavaScript, `<label>` |

---

### **When to Use Which?**
✔ **Use `name`** for submitting form data to the server.  
✔ **Use `id`** for JavaScript, CSS, or linking `<label>` with inputs.  
