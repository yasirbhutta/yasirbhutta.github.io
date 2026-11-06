---
layout: page
title: **Beware of Mutable Default Arguments in Python – A Common Mistake Explained!**
description: One common mistake in Python is using a mutable default argument like a list (`[]`). When a mutable object is used as a default parameter, it persists...
keywords: apple, cart, banana, call, data
---
# **Beware of Mutable Default Arguments in Python – A Common Mistake Explained!**

## Understanding Mutable Default Arguments in Python  

### The Issue with Mutable Default Arguments  

One common mistake in Python is using a **mutable default argument** like a list (`[]`). When a mutable object is used as a default parameter, it **persists across multiple function calls**, leading to unexpected behavior.  

---

## **How Default Arguments Work in Python**  

In Python, **default argument values are evaluated only once at the time of function definition**. This means that if a mutable object (like a list or dictionary) is used as a default value, it will be **shared across multiple function calls** instead of creating a new one each time.  

---

## **Example 1: The Unexpected Behavior**  

### **Code:**  
```python
def add_item(item, cart=[]):  # cart is assigned a mutable default list
    cart.append(item)  # Appends the item to the same list
    return cart  # Returns the modified list

print(add_item("apple"))  # First call
print(add_item("banana"))  # Second call
print(add_item("orange"))  # Third call
```

### **Execution Breakdown:**  

1. **First call:** `add_item("apple")`  
   - `cart` is initially `[]` (empty).
   - `"apple"` is appended → `cart = ["apple"]`
   - Returns `["apple"]`.  

2. **Second call:** `add_item("banana")`  
   - The **same** `cart = ["apple"]` is used from the first call.
   - `"banana"` is appended → `cart = ["apple", "banana"]`
   - Returns `["apple", "banana"]`.  

3. **Third call:** `add_item("orange")`  
   - The **same** `cart = ["apple", "banana"]` is used again.
   - `"orange"` is appended → `cart = ["apple", "banana", "orange"]`
   - Returns `["apple", "banana", "orange"]`.  

---

### **Output:**  
```
['apple']
['apple', 'banana']
['apple', 'banana', 'orange']
```
This is **not** what we expected! Instead of creating a new list each time, the same list is being modified repeatedly.  

---

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

## **Fix: Using `None` as the Default Value**  

To ensure that each function call gets a **new list**, use `None` as the default argument and create a new list inside the function.  

### **Corrected Code:**  
```python
def add_item(item, cart=None):
    if cart is None:  
        cart = []  # Creates a new list for each function call
    cart.append(item)
    return cart

print(add_item("apple"))  # ['apple']
print(add_item("banana"))  # ['banana']
print(add_item("orange"))  # ['orange']
```

### **Fixed Output:**  
```
['apple']
['banana']
['orange']
```
Now, each function call gets a **new list**, preventing the issue.  

---

## **Example 2: Mutable Default Arguments with Dictionaries**  

### **Problem Code:**  
```python
def add_to_dict(key, value, data={}):
    data[key] = value
    return data

print(add_to_dict("name", "Alice"))
print(add_to_dict("age", 25))
```
### **Unexpected Output:**  
```
{'name': 'Alice'}
{'name': 'Alice', 'age': 25}
```
The dictionary is **shared across calls**, so `"age": 25` gets added to the previous dictionary.  

### **Corrected Code:**  
```python
def add_to_dict(key, value, data=None):
    if data is None:
        data = {}  # Creates a new dictionary for each function call
    data[key] = value
    return data

print(add_to_dict("name", "Alice"))  # {'name': 'Alice'}
print(add_to_dict("age", 25))  # {'age': 25}
```
### **Correct Output:**  
```
{'name': 'Alice'}
{'age': 25}
```

---

## **Key Takeaways:**  
✅ **Mutable default arguments (lists, dictionaries, etc.) persist across function calls.**  
✅ **Use `None` as a default value and initialize the mutable object inside the function.**  
✅ **Each function call should create a new object to avoid unexpected behavior.**  

By following these best practices, you can **avoid hidden bugs** and ensure your functions behave as expected!