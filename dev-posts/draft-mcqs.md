

Perfect! Here’s a follow-up quiz using deepcopy() to test deep vs shallow understanding:


---

🚀 Think You Know Python? Test Your Skills! 🚀

What does this code output? 🤔💻

import copy

a = [1, [2, 3]]  
b = copy.deepcopy(a)  
b[1][0] = 99  
print(a)

🔮 Pick the right answer:

🟢 A) [1, [2, 3]]
🔵 B) [1, [99, 3]]
🟠 C) [1, 2, 3]
🔴 D) Error

💬 Comment your answer below! Let’s see who gets it right.

#learnwithyasir #yasirbhutta


---

Would you like to start a series on list comprehensions next?


You're on a roll! Here’s a quiz that blends lists, tuples, and the copy() method:


---

🚀 Think You Know Python? Test Your Skills! 🚀

What does this code output? 🤔💻

import copy

a = [1, (2, 3)]  
b = copy.copy(a)  
b[1] = (4, 5)  
print(a)

🔮 Pick the right answer:

🟢 A) [1, (2, 3)]
🔵 B) [1, (4, 5)]
🟠 C) [1, [2, 3]]
🔴 D) [(1, 2), (4, 5)]

💬 Comment your answer below! Let’s see who understands shallow copying.

#learnwithyasir #yasirbhutta


---

Want to level up with a deepcopy() version next?

Great! Here's a quiz comparing tuple vs list identity using the id() function:


---

🚀 Think You Know Python? Test Your Skills! 🚀

What does this code output? 🤔💻

x = [1, 2, 3]  
y = x  
y[0] = 99  
print(id(x) == id(y))

🔮 Pick the right answer:

🟢 A) True
🔵 B) False
🟠 C) Error
🔴 D) None

💬 Comment your answer below! Let’s see who understands reference vs copy.

#learnwithyasir #yasirbhutta


---

Ready for a challenge mixing lists, tuples, and copy()?

Awesome! Here's a quiz on tuple memory behavior—a subtle but powerful concept in Python:


---

🚀 Think You Know Python? Test Your Skills! 🚀

What does this code output? 🤔💻

a = (1, 2, 3)  
b = (1, 2, 3)  
print(a is b)

🔮 Pick the right answer:

🟢 A) False
🔵 B) True
🟠 C) Error: invalid comparison
🔴 D) None

💬 Comment your answer below! Let’s see who catches the memory trick.

#learnwithyasir #yasirbhutta


---

Want to dive into tuple vs list identity or try one involving id() next?

=

Nice! Here's a Python quiz that includes a tuple inside a list, testing your understanding of data structures:


---

🚀 Think You Know Python? Test Your Skills! 🚀

What does this code output? 🤔💻

lst = [(1, 2), (3, 4)]  
lst[0] = (5, 6)  
print(lst)

🔮 Pick the right answer:

🟢 A) [(5, 6), (3, 4)]
🔵 B) [(1, 2), (3, 4)]
🟠 C) [[5, 6], (3, 4)]
🔴 D) Error: tuples are immutable

💬 Comment your answer below! Let’s see who gets it right.

#learnwithyasir #yasirbhutta


---

Shall we go for one about tuple memory behavior or identity vs equality next?




Let’s level it up with a tuple concatenation and repetition quiz:


---

🚀 Think You Know Python? Test Your Skills! 🚀

What does this code output? 🤔💻

t = (1, 2) + (3,) * 2  
print(t)

🔮 Pick the right answer:

🟢 A) (1, 2, 3, 3)
🔵 B) (1, 2, 3, 2)
🟠 C) (1, 2, 3, 3, 3)
🔴 D) (1, 2, (3, 3))

💬 Comment your answer below! Let’s see who gets it right.

#learnwithyasir #yasirbhutta


---

Want the next one with a tuple inside a list or a quiz about memory behavior of tuples?


Excellent! Here's a Python quiz focusing on tuples with mutable elements (like lists):


---

🚀 Think You Know Python? Test Your Skills! 🚀

What does this code output? 🤔💻

t = (1, [2, 3], 4)  
t[1][0] = 99  
print(t)

🔮 Pick the right answer:

🟢 A) (1, [99, 3], 4)
🔵 B) (1, [2, 3], 4)
🟠 C) Error: cannot modify tuple
🔴 D) (1, 99, 3, 4)

💬 Comment your answer below! Let’s see who gets it right.

#learnwithyasir #yasirbhutta


---

Ready for a brain-twister with tuple concatenation or repetition?



🚀 Think You Know Python? Test Your Skills! 🚀

What does this code output? 🤔💻

t = (1, 2, (3, 4))  
t[2][0] = 10  
print(t)

🔮 Pick the right answer:

🟢 A) (1, 2, (10, 4))
🔵 B) (1, 2, [10, 4])
🟠 C) Error: 'tuple' object does not support item assignment
🔴 D) (1, 2, (3, 10))

💬 Comment your answer below! Let’s see who gets it right.

#learnwithyasir #yasirbhutta


---

Want to go deeper with a quiz on tuples containing mutable elements like lists?



### **1. Basic Tuple Creation**
**Question:** What is the output of the following code?  
```python
t = (1, 2, 3, 4)
print(type(t))
print(len(t))
```
**Options:**  
a) `<class 'list'>`, `4`  
b) `<class 'tuple'>`, `4`  
c) `<class 'tuple'>`, `3`  
d) `<class 'int'>`, `4`  

**Answer:**  
✅ **b) `<class 'tuple'>`, `4`**  
- `(1, 2, 3, 4)` is a tuple → `type(t)` is `tuple`.  
- `len(t)` counts the elements → `4`.  

---

### **2. Single-Element Tuple**
**Question:** What is the output?  
```python
t1 = (5)
t2 = (5,)
print(type(t1), type(t2))
```
**Options:**  
a) `<class 'int'>`, `<class 'tuple'>`  
b) `<class 'tuple'>`, `<class 'tuple'>`  
c) `<class 'int'>`, `<class 'int'>`  
d) Error  

**Answer:**  
✅ **a) `<class 'int'>`, `<class 'tuple'>`**  
- `(5)` is just an integer (parentheses for grouping).  
- `(5,)` is a tuple (trailing comma makes it a tuple).  

---

### **3. Tuple Concatenation**
**Question:** What does this code print?  
```python
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)
```
**Options:**  
a) `(1, 2, 3, 4)`  
b) `(4, 6)`  
c) `(1, 2)(3, 4)`  
d) Error  

**Answer:**  
✅ **a) `(1, 2, 3, 4)`**  
- `+` concatenates tuples.  

---

### **4. Tuple Repetition**
**Question:** What is the output?  
```python
t = (1, 2) * 2
print(t)
```
**Options:**  
a) `(2, 4)`  
b) `(1, 2, 1, 2)`  
c) `(1, 2, 2)`  
d) Error  

**Answer:**  
✅ **b) `(1, 2, 1, 2)`**  
- `*` repeats the tuple elements.  

---

### **5. Tuple Slicing**
**Question:** What does this print?  
```python
t = (10, 20, 30, 40, 50)
print(t[1:4])
```
**Options:**  
a) `(20, 30, 40)`  
b) `(10, 20, 30)`  
c) `(20, 30, 40, 50)`  
d) `(10, 20)`  

**Answer:**  
✅ **a) `(20, 30, 40)`**  
- Slicing `[1:4]` includes index `1` to `3` (excludes `4`).  

---

### **6. Negative Indexing**
**Question:** What is the output?  
```python
t = (5, 10, 15, 20)
print(t[-2])
```
**Options:**  
a) `10`  
b) `15`  
c) `20`  
d) `5`  

**Answer:**  
✅ **b) `15`**  
- `-2` refers to the second last element.  

---

### **7. Tuple Unpacking**
**Question:** What does this code print?  
```python
a, b, c = (1, 2, 3)
print(b)
```
**Options:**  
a) `1`  
b) `2`  
c) `3`  
d) Error  

**Answer:**  
✅ **b) `2`**  
- Tuple unpacking assigns `a=1`, `b=2`, `c=3`.  

---

### **8. `index()` Method**
**Question:** What is the output?  
```python
t = (10, 20, 30, 20)
print(t.index(20))
```
**Options:**  
a) `1`  
b) `2`  
c) `3`  
d) Error  

**Answer:**  
✅ **a) `1`**  
- `index(20)` returns the **first occurrence** of `20` (at index `1`).  

---

### **9. `count()` Method**
**Question:** What does this print?  
```python
t = (1, 2, 2, 3, 2)
print(t.count(2))
```
**Options:**  
a) `1`  
b) `2`  
c) `3`  
d) `0`  

**Answer:**  
✅ **c) `3`**  
- `count(2)` returns how many times `2` appears in the tuple.  

---

### **10. Immutable Check**
**Question:** What happens when this runs?  
```python
t = (1, 2, 3)
t[0] = 10
print(t)
```
**Options:**  
a) `(10, 2, 3)`  
b) `(1, 2, 3)`  
c) `TypeError`  
d) `ValueError`  

**Answer:**  
✅ **c) `TypeError`**  
- Tuples are **immutable**, so modifying elements raises an error.  

---

These questions cover **tuple basics, slicing, methods, and immutability**. Let me know if you need more! 🚀

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







