Here are some multiple-choice questions (MCQs) related to tuple operations, slicing, and methods in Python:

### **Tuple Basics**
1. **What is a tuple in Python?**  
   a) A mutable sequence of elements  
   b) An immutable sequence of elements  
   c) A key-value pair collection  
   d) A single value container  
   **Answer: b) An immutable sequence of elements**

2. **How do you create an empty tuple?**  
   a) `t = ()`  
   b) `t = tuple()`  
   c) Both a and b  
   d) `t = []`  
   **Answer: c) Both a and b**

3. **Which of the following is a valid tuple declaration?**  
   a) `t = (1)`  
   b) `t = (1,)`  
   c) `t = 1,`  
   d) Both b and c  
   **Answer: d) Both b and c** *(A single-element tuple requires a comma.)*

---

### **Tuple Operations**
4. **What is the output of `(1, 2) + (3, 4)`?**  
   a) `(1, 2, 3, 4)`  
   b) `(4, 6)`  
   c) `(1, 2)(3, 4)`  
   d) Error  
   **Answer: a) `(1, 2, 3, 4)`** *(Tuples can be concatenated.)*

5. **What is the result of `(1, 2) * 3`?**  
   a) `(3, 6)`  
   b) `(1, 2, 1, 2, 1, 2)`  
   c) `(1, 2, 3)`  
   d) Error  
   **Answer: b) `(1, 2, 1, 2, 1, 2)`** *(Repetition operation on tuples.)*

6. **Which operation is NOT allowed on tuples?**  
   a) Concatenation (`+`)  
   b) Repetition (`*`)  
   c) Modifying an element (`t[0] = 5`)  
   d) Slicing (`t[1:3]`)  
   **Answer: c) Modifying an element (`t[0] = 5`)** *(Tuples are immutable.)*

---

### **Tuple Slicing**
7. **What is the output of `t = (10, 20, 30, 40, 50); print(t[1:4])`?**  
   a) `(20, 30, 40)`  
   b) `(10, 20, 30)`  
   c) `(20, 30, 40, 50)`  
   d) `(10, 20)`  
   **Answer: a) `(20, 30, 40)`** *(Slicing includes start index, excludes end index.)*

8. **What does `t[::-1]` do?**  
   a) Reverses the tuple  
   b) Deletes the tuple  
   c) Returns the first element  
   d) Raises an error  
   **Answer: a) Reverses the tuple** *(Step `-1` reverses the sequence.)*

9. **If `t = (5, 10, 15, 20)`, what is `t[-2]`?**  
   a) `10`  
   b) `15`  
   c) `20`  
   d) `5`  
   **Answer: b) `15`** *(Negative indexing starts from the end.)*

---

### **Tuple Methods**
10. **Which method returns the index of the first occurrence of a value in a tuple?**  
    a) `find()`  
    b) `index()`  
    c) `search()`  
    d) `get()`  
    **Answer: b) `index()`** *(Example: `t.index(10)` finds the position of `10`.)*

11. **What does the `count()` method do for tuples?**  
    a) Returns the total number of elements  
    b) Counts occurrences of a specified value  
    c) Sums all elements  
    d) Converts tuple to a list  
    **Answer: b) Counts occurrences of a specified value** *(Example: `t.count(5)` gives the number of `5`s.)*

12. **Which of the following is NOT a tuple method?**  
    a) `index()`  
    b) `count()`  
    c) `append()`  
    d) None of the above  
    **Answer: c) `append()`** *(Tuples are immutable, so they don’t support `append`.)*

---

### **Miscellaneous**
13. **Can tuples contain elements of different data types?**  
    a) Yes  
    b) No  
    **Answer: a) Yes** *(Example: `(1, "hello", 3.14)` is valid.)*

14. **What is the result of `len((1, 2, 3, 4))`?**  
    a) `4`  
    b) `3`  
    c) `1`  
    d) `10`  
    **Answer: a) `4`** *(The `len()` function returns the number of elements.)*

15. **What happens if you try to modify a tuple?**  
    a) It works fine  
    b) Raises `TypeError`  
    c) Raises `ValueError`  
    d) The tuple becomes a list  
    **Answer: b) Raises `TypeError`** *(Tuples are immutable.)*

---

These MCQs cover fundamental concepts of tuples in Python, including operations, slicing, and methods. Let me know if you'd like more questions or explanations! 🚀
---

2. What will be the output?

class X:
    def greet(self):
        print("Hello from X")

class Y:
    def greet(self):
        print("Hello from Y")

class Z(X, Y):
    pass

z = Z()
z.greet()

A) Hello from X
B) Hello from Y
C) Error
D) No output

Answer: A) Hello from X


---

3. What will be the output?

class P:
    def display(self):
        print("Inside P")

class Q(P):
    def display(self):
        print("Inside Q")

class R(P):
    pass

class S(Q, R):
    pass

s = S()
s.display()

A) Inside P
B) Inside Q
C) Inside R
D) Error

Answer: B) Inside Q
(Explanation: S inherits Q first, and Q overrides display.)


---

4. What will be the output?

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.mro())

A) [D, B, C, A, object]
B) [D, C, B, A, object]
C) [D, A, B, C, object]
D) [D, B, A, C, object]

Answer: A) [D, B, C, A, object]

---

7. What is the output of this code?

class Parent1:
    var = "Parent1"

class Parent2:
    var = "Parent2"

class Child(Parent1, Parent2):
    pass

print(Child.var)

A) Parent1
B) Parent2
C) Error
D) None

Answer: A) Parent1


---

8. What will this print?

class One:
    def foo(self):
        print("One")

class Two:
    def foo(self):
        print("Two")

class Three(One, Two):
    def bar(self):
        self.foo()

t = Three()
t.bar()

A) One
B) Two
C) Error
D) None

Answer: A) One


---

9. What is the output?

class X:
    def __init__(self):
        print("X init")

class Y:
    def __init__(self):
        print("Y init")

class Z(X, Y):
    def __init__(self):
        super().__init__()

z = Z()

A) X init
B) Y init
C) X init and Y init
D) Error

Answer: A) X init
(Explanation: super() follows MRO, so X’s constructor runs.)


---



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







