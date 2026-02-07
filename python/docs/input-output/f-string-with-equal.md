---
layout: page
title: "Python f-Strings with = and Format Specifiers (Debugging Made Easy)"
description: Learn how to use Python f-strings with the = symbol and format specifiers to simplify debugging and output formatting.
keywords: python f-strings, f-string equals sign, python debugging f-string, format specifiers in f-strings, python 3.12 f-string, expression in f-string, python string formatting, python print debug
course: python
topic: input-output
show_toc: true
toc: toc/python.html
show_practice_progress: true
show_mini_project: false
prev: /python/docs/input-output/f-string.html
next: /python/docs/input-output/input.html
breadcrumb: 
- title: Input - Output
url: /python/docs/input-output/
---

## ✅ **`=` for Debugging + Format Specifiers**

You can now include the **expression itself** along with the value **in the same f-string** — very handy for debugging and clean output.

---

### 🧪 Example 1: Expression with `=`

```python
name = "Yasir"
age = 30

print(f"{name=}, {age=}")
```

📤 Output:

```
name='Yasir', age=30
```

> It shows **both the variable name and its value**. No need to manually write: `print("name =", name)`.

---

### 🧪 Example 2: Expression with `=` and Format Specifiers

```python
pi = 3.1415926535

print(f"{pi=:.2f}")
```

📤 Output:

```
pi=3.14
```

> This uses **`= for showing expression`** and `:.2f` for **2 decimal places formatting**.

---

### 🧪 Example 3: Debug an Expression

```python
x = 5
y = 10

print(f"{x + y=}")
```

📤 Output:

```
x + y=15
```

> Super useful when debugging calculations or complex logic.

---

### ✅ Summary

| Feature           | Syntax Example | Output     |
| ----------------- | -------------- | ---------- |
| Show name + value | `f"{x=}"`      | `x=5`      |
| With formatting   | `f"{x=:.2f}"`  | `x=5.00`   |
| For expressions   | `f"{x + y=}"`  | `x + y=15` |

---

Absolutely! Here's a **short quiz and practice code** to reinforce your understanding of **f-strings with `=` and format specifiers** in Python.

---

## 🧠 **Quick Quiz (Multiple Choice)**

**Q1.** What will the output be?

```python
x = 5
print(f"{x=}")
```

A) x: 5
B) x=5
C) x
D) 5

---

**Q2.** Which f-string correctly formats `pi = 3.14159` to 2 decimal places *and* shows the expression?

A) `f"{pi:.2f=}"`
B) `f"{=pi:.2f}"`
C) `f"{pi=:.2f}"`
D) `f"{pi:.2f}"`

---

**Q3.** What does `f"{x + y=}"` display if `x = 10` and `y = 5`?

A) x + y = 15
B) x+y=15
C) x + y=15
D) 15

---

## Task: 🧪 **Practice Code**

Try running and modifying this code:

```python
name = "Alice"
score = 87.456
passed = True

# Print with variable names using f-strings
print(f"{name=}")
print(f"{score=:.1f}")     # One decimal place
print(f"{passed=}")

# Debugging an expression
print(f"{score > 50=}")
print(f"{len(name)=}")
print(f"{score/10=:.2f}")
```

🔁 **Try This:**

* Change values of `score` or `name`.
* Add more expressions like `f"{name.upper()=}"`.

---

## 📘 **Related Topics**

* **F-Strings in Python** – F-strings (formatted string literals) are a feature introduced in Python 3.6 that provide a concise and readable way to embed expressions inside string literals. 
  👉 [Learn more](f-string.md)
* [**Python `print` Function**](print.md)
* [`input()` Function](input.md) 

