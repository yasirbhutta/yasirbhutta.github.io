# **Walrus Operator (`:=`) in Python**

The **walrus operator** (`:=`) is an **assignment expression** introduced in **Python 3.8**. It allows you to **assign a value to a variable as part of an expression**, making your code more concise and readable.  

## **Syntax**  
```python
variable := expression
```
Here, `variable` is assigned the value of `expression`, and the whole expression evaluates to the value.

---

## **Examples of Walrus Operator Usage**

### **1. Using in `if` Condition**
Instead of:  
```python
value = len(my_list)
if value > 5:
    print(f"List is long: {value}")
```
We can use:  
```python
my_list = [1, 2, 3, 4, 5, 6, 7]
if (value := len(my_list)) > 5:
    print(f"List is long: {value}")
```
**Why?** It avoids writing `len(my_list)` twice, making it more efficient.

---

### **2. Using in `while` Loops**
Instead of:  
```python
data = input("Enter something: ")
while len(data) > 0:
    print(f"You entered: {data}")
    data = input("Enter something: ")
```
We can use:  
```python
while (data := input("Enter something: ")):
    print(f"You entered: {data}")
```
**Why?** This avoids calling `input()` twice, making the loop cleaner.

---

**Example: Walrus Operator in Python**

<iframe class="yt-short" src="https://www.youtube.com/embed/vhEz75XZlJI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### **3. Using in List Comprehensions**
Instead of:  
```python
numbers = [10, 15, 20, 25, 30]
filtered = []
for num in numbers:
    square = num ** 2
    if square > 400:
        filtered.append(square)
```
We can use:  
```python
numbers = [10, 15, 20, 25, 30]
filtered = [square for num in numbers if (square := num ** 2) > 400]
print(filtered)  # Output: [625, 900]
```
**Why?** The walrus operator lets us **compute the square once** instead of repeating it.

---

### **4. Using in `match` Statements (Python 3.10+)**
```python
def categorize(number):
    match number:
        case n if (n := number) > 50:
            print(f"Large number: {n}")
        case _:
            print(f"Small number: {n}")

categorize(60)  # Output: Large number: 60
```
**Why?** We assign `n` inside `case n if ...`, making the code cleaner.

---

## **Real-Life Usage of Walrus Operator**
1. **Efficient Logging**:  
   ```python
   import logging
   if (msg := "Error occurred!") and is_critical:
       logging.error(msg)
   ```
   **Why?** The message is assigned and logged in one step.

2. **Optimized API Calls**:  
   ```python
   if (response := fetch_data()).status_code == 200:
       print(response.json())
   ```
   **Why?** It avoids making multiple API calls.

3. **Reading Files Line by Line Efficiently**:  
   ```python
   with open("data.txt") as file:
       while (line := file.readline().strip()):
           print(line)
   ```
   **Why?** It prevents extra file reads.

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


## **Tasks Using the Walrus Operator**
### **Task 1: Count User Inputs Until "exit"**
Write a Python program that takes user input and counts how many times a user enters something before typing "exit".  

**Solution:**
```python
count = 0
while (user_input := input("Enter something (or 'exit' to stop): ")) != "exit":
    count += 1
print(f"You entered {count} times before exiting.")
```

---

### **Task 2: Find the First Long Word in a List**
Given a list of words, find and print the first word that has more than 7 letters.  
```python
words = ["apple", "banana", "strawberry", "kiwi", "pineapple"]
if (long_word := next((word for word in words if len(word) > 7), None)):
    print(f"First long word: {long_word}")
```
**Why?** This finds the first long word efficiently.

---

### **Task 3: Sum Numbers Until a Negative Number**
Write a program that keeps taking numbers from the user and sums them until the user enters a negative number.  
```python
total = 0
while (num := int(input("Enter a number: "))) >= 0:
    total += num
print(f"Total sum: {total}")
```
**Why?** This makes the code more compact.

---

## **Conclusion**
The **walrus operator (`:=`)** improves readability and efficiency by **combining assignment and expressions** in a single step. However, **use it wisely**—overusing it can make code harder to read.

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