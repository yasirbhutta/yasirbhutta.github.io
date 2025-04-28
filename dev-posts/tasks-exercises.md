

---

Task 1:
Write a lambda function that adds 10 to a number.

Input: 5

Expected Output: 15



---

Task 2:
Write a lambda function that multiplies two numbers.

Input: 4, 6

Expected Output: 24

---


Task 5:
Write a lambda to find the maximum of two numbers.

Input: 8, 12

Expected Output: 12


Here are 15 beginner-friendly lambda function tasks with sample inputs and expected outputs to practice Python lambda functions:

---

### **Task 1: Add Two Numbers**
**Description**: Create a lambda function that adds two numbers.  
**Input**: `3, 5`  
**Expected Output**: `8`  
**Solution**:  
```python
add = lambda x, y: x + y
print(add(3, 5))  # Output: 8
```

---

### **Task 2: Check Even Number**
**Description**: Create a lambda function that returns `True` if a number is even.  
**Input**: `6`  
**Expected Output**: `True`  
**Solution**:  
```python
is_even = lambda x: x % 2 == 0
print(is_even(6))  # Output: True
```

---

### **Task 3: Reverse a String**
**Description**: Create a lambda function to reverse a string.  
**Input**: `"hello"`  
**Expected Output**: `"olleh"`  
**Solution**:  
```python
reverse = lambda s: s[::-1]
print(reverse("hello"))  # Output: olleh
```

---

### **Task 4: Check Substring**
**Description**: Create a lambda function that returns `True` if a substring exists in a string.  
**Input**: `"world", "hello world"`  
**Expected Output**: `True`  
**Solution**:  
```python
has_substring = lambda sub, s: sub in s
print(has_substring("world", "hello world"))  # Output: True
```

---

### **Task 5: Calculate Rectangle Area**
**Description**: Create a lambda function to calculate the area of a rectangle.  
**Input**: `4, 7`  
**Expected Output**: `28`  
**Solution**:  
```python
area = lambda l, w: l * w
print(area(4, 7))  # Output: 28
```

---

### **Task 6: Cube of a Number**
**Description**: Create a lambda function to compute the cube of a number.  
**Input**: `3`  
**Expected Output**: `27`  
**Solution**:  
```python
cube = lambda x: x ** 3
print(cube(3))  # Output: 27
```

---

### **Task 7: Square List Elements (with `map`)**
**Description**: Use a lambda with `map` to square each element in a list.  
**Input**: `[1, 2, 3, 4]`  
**Expected Output**: `[1, 4, 9, 16]`  
**Solution**:  
```python
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(squared)  # Output: [1, 4, 9, 16]
```

---

### **Task 8: Filter Even Numbers (with `filter`)**
**Description**: Use a lambda with `filter` to extract even numbers from a list.  
**Input**: `[1, 2, 3, 4, 5, 6]`  
**Expected Output**: `[2, 4, 6]`  
**Solution**:  
```python
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # Output: [2, 4, 6]
```


---

### **Task 10: Maximum of Two Numbers**
**Description**: Create a lambda function to return the maximum of two numbers.  
**Input**: `8, 12`  
**Expected Output**: `12`  
**Solution**:  
```python
max_num = lambda a, b: a if a > b else b
print(max_num(8, 12))  # Output: 12
```

---

### **Task 11: Uppercase Conversion**
**Description**: Create a lambda function to convert a string to uppercase.  
**Input**: `"lambda"`  
**Expected Output**: `"LAMBDA"`  
**Solution**:  
```python
uppercase = lambda s: s.upper()
print(uppercase("lambda"))  # Output: LAMBDA
```

---

### **Task 12: Combine Strings**
**Description**: Create a lambda function to concatenate two strings with a space.  
**Input**: `"Hello", "World"`  
**Expected Output**: `"Hello World"`  
**Solution**:  
```python
combine = lambda s1, s2: f"{s1} {s2}"
print(combine("Hello", "World"))  # Output: Hello World
```

---

### **Task 13: Check Palindrome**
**Description**: Create a lambda function to check if a string is a palindrome.  
**Input**: `"madam"`  
**Expected Output**: `True`  
**Solution**:  
```python
is_palindrome = lambda s: s == s[::-1]
print(is_palindrome("madam"))  # Output: True
```

---

### **Task 14: Average of Two Numbers**
**Description**: Create a lambda function to compute the average of two numbers.  
**Input**: `10, 20`  
**Expected Output**: `15.0` 


**Solution**:  
```python
average = lambda x, y: (x + y) / 2
print(average(10, 20))  # Output: 15.0
```

---



