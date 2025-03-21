# **Why Can’t the Assignment Operator (`=`) Be Used in Expressions in Python?**  

In Python, the **assignment operator (`=`)** is **not an expression** but a **statement**. This means it **does not return a value**, so using it inside expressions (like `if` or `while` conditions) will cause a **SyntaxError**.  

---

## **1. Incorrect Usage of `=` in Expressions (SyntaxError)**  
```python
if (x = 10):  # ❌ SyntaxError
    print(x)
```
🔴 **Error Output:**  
```
SyntaxError: invalid syntax
```
✅ **Fix:** You must assign `x` outside the `if` condition.  
```python
x = 10
if x > 5:
    print(f"x is {x}")  # ✅ Works correctly
```
---

## **2. Using the Walrus Operator (`:=`) Instead**  
Python 3.8 introduced the **walrus operator (`:=`)**, which **allows assignment within expressions**.  

✅ **Correct Usage with `:=`**
```python
if (x := 10) > 5:
    print(f"x is {x}")  # Output: x is 10
```
💡 **Why does this work?**  
- `x := 10` assigns `10` to `x` and returns `10`, which is then used in the `if` condition.

---

## **3. Using `:=` in `while` Loops**  
Before Python 3.8, you had to assign values outside the loop.  
```python
data = input("Enter something: ")
while len(data) > 0:
    print(f"You entered: {data}")
    data = input("Enter something: ")
```
🔴 **Problem:** `input()` is called twice.  

✅ **Using Walrus Operator (`:=`) to Simplify**  
```python
while (data := input("Enter something: ")):  # Stops when input is empty
    print(f"You entered: {data}")
```
✔ **Cleaner and avoids calling `input()` twice.**  

---

## **4. Using `:=` in List Comprehensions**
Before `:=`, you had to write:  
```python
numbers = [10, 20, 30, 40]
squared = [num ** 2 for num in numbers if num ** 2 > 500]
```
🔴 **Problem:** `num ** 2` is computed twice.  

✅ **With `:=` (Avoids Recalculation)**  
```python
numbers = [10, 20, 30, 40]
squared = [square for num in numbers if (square := num ** 2) > 500]
print(squared)  # Output: [900, 1600]
```
✔ **Efficient because `square` is computed once.**  

