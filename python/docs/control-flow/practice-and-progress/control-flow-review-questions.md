# Python Control Flow Statements: Review Questions

**for loop:**
- What is the difference between a for loop and a while loop in Python?
- Can you use a for loop to iterate over a string?

**if statement:**

- Can you have multiple elif blocks in an if-elif-else statement?
- What is the purpose of nesting if statements?

- **Question**: What is printed when `mystery_loop()` is called? Explain why the loop terminates early. 
   
```python  
def mystery_loop():  
    x = 5  
    while x > 0:  
        print(x)  
        x -= 1  
        if x == 2:  
            break  
    print("Loop ended!")  
```  
 
- **Question**: What does `check_value(7)` print? What happens if the order of the `elif` statements is reversed? 
  
```python  
def check_value(n):  
    if n > 10:  
        print("A")  
    elif n > 5:  
        print("B")  
    elif n > 3:  
        print("C")  
    else:  
        print("D")  
```  
 
- **Question**: What is the final output? Why does this happen? How would you fix it to remove all even numbers?  
- 

```python  
numbers = [1, 2, 3, 4]  
for num in numbers:  
    if num % 2 == 0:  
        numbers.remove(num)  
print(numbers)  
```  

- **Question**: Which case is printed? Explain how operator precedence affects the outcome.  

```python  
a, b, c = True, False, True  
if not a or b and c:  
    print("Case 1")  
else:  
    print("Case 2")  
```  
---

- **Question**: Why does this loop run infinitely? How would you fix it?  

```python  
def countdown(n):  
    while n > 0:  
        print(n)  
        n += 1  
    print("Blastoff!")  
```  

- **Question**: This code incorrectly classifies some leap years (e.g., 2000). Identify the flaw and fix the logic.  

```python  
def is_leap_year(year):  
    if year % 4 == 0:  
        return True  
    elif year % 100 == 0:  
        return False  
    elif year % 400 == 0:  
        return True  
    else:  
        return False  
```  
---
