# Python: Variables

Connect with me: [Youtube](https://www.youtube.com/yasirbhutta) \| [LinkedIn](https://www.linkedin.com/in/yasirbhutta/) \| [WhatsApp Channel](https://whatsapp.com/channel/0029VaC3BC160eBZZSs3CW0c) \| [Web](https://yasirbhutta.github.io/) \| [Facebook](https://www.facebook.com/yasirbhutta786) \| [Twitter](https://twitter.com/yasirbhutta)

- [Download PDF](https://yasirbhutta.github.io/python/docs/variables.pdf)
- To access the updated handouts, please click on the following link:
[https://yasirbhutta.github.io/python/docs/variables.html](https://yasirbhutta.github.io/python/docs/variables.html)

## Variables

- Storage containers for data (numbers, text, etc.).

## What is a variable

- A variable is a named storage location in a computer's memory that is used to hold data or values. It allows programmers to store and manipulate data within a program.

**Purpose:** Variables provide a way to store and manage data that can be used and manipulated throughout a program. They make programs more flexible and allow for dynamic data storage.

**Assignment statement:** in Python is used to assign a value to a variable. Its primary purpose is to store and manage data within a program.

**Imagine variables as labeled boxes:**

- You have boxes for storing different things (numbers, words, etc.).
- Each box has a name (label) to identify what's inside.
- You can put things in, take them out, and change what's inside.

## Variable names

In Python, valid variable names must adhere to the following rules:

- **Begin with a letter or an underscore:** The first character of a variable name must be a letter (a-z, A-Z) or an underscore (_).

- **Followed by letters, digits, or underscores:** After the first character, the variable name can contain letters, digits (0-9), or underscores.

- **Case-sensitive:** Variable names are case-sensitive. For example, myVariable and myvariable would be considered different variables.

- **No reserved keywords:** Variable names cannot be Python reserved keywords (e.g., if, for, while, class, etc.).
  
[video:Function and Variable Naming \|Python Best Practices](https://youtube.com/shorts/IDzqrCz4nYI)
[video:Python Variables and Assignment](https://www.youtube.com/watch?v=CRiu33tEDIM)
[video: Meaningful Variable Names \| Python Best Practices](https://youtube.com/shorts/lQy1Le8fnRs?si=kU0YflJx7lLzp_TT)
[video: Asterisk (*) in Variable Assignment](https://www.youtube.com/watch?v=xCwfASassNs)

**Example #1:** Storing a name

```python
name = "Muhammad Hamza"
print(name)
```

**Example #2:** Tracking a score:

```python
score = 0
score = score + 10 # adds 10 to the score
print(score)
```

**Example #3:** Remembering a favorite color

```python
favorite_color = "blue" #stores "blue"  in variable
print(favorite_color)
```

**Example #4:** Calculating the area of a rectangle

```python
length = 10
width = 5

# calculates the area
area = length * width
print(area)
```

**Example 5**: [How to assign multiple values to multiple variables?](https://youtu.be/ur8rkDPzuSU)
**Example 6:** [How to Swap Variables Without a Third Variable in Python](https://youtu.be/CVy3A48WXeE)
**Example 7:** [Calculate the Area of a Circle with Radius](https://www.youtube.com/watch?v=QoECA8v_2tQ)
**Example 8:** [Python Variable Names: Case-Sensitive? Avoid This Coding Mistake!](https://youtu.be/hEoVi5hZHVg)

**Key Points:**

- **[Choose meaningful names](https://youtube.com/shorts/lQy1Le8fnRs?si=kU0YflJx7lLzp_TT):** Use names that describe what the variable stores (e.g., pizza_slices instead of x).
  - [video: Meaningful Variable Names \| Python Best Practices](https://youtube.com/shorts/lQy1Le8fnRs?si=kU0YflJx7lLzp_TT)
- **Assign values using =:** The equals sign is used to put a value into a variable.
- **Change values:** You can update a variable's value later in your code.
- **Use variables in calculations and operations:** Variables can be used just like regular numbers or text in expressions.
- **Think of variables as placeholders:** They hold information that can change as your program runs.

## Key Terms

## Fix the Errors!

# Using an undefined variable 

```python
name = "Ahmad"
print(f"Hello, {lastname}")  # lastname not defined
```

## True/False (Mark T for True and F for False)

1. Variable names in Python are case-sensitive.
2. In Python, variables must be declared with a specific data type before they can be used.
3. The statement x = 5 both creates the variable x and assigns it the value 5.

**Answer Key (True/False):**

1. True
2. False
3. True

## Multiple Choice (Select the best answer)

1. **What is a variable in Python?**
   - A) A reserved word in Python
   - B) A placeholder for storing data values
   - C) A function that prints data
   - D) A built-in library in Python

2. **Which statement best describes a variable in Python?**
   - A) A variable can hold multiple values at once.
   - B) A variable must be declared with a data type.
   - C) A variable is a name that refers to a value.
   - D) A variable is used only in loops.
  
3. **What is the output of the following code?**

   ```python
   x = 10
   print(x)
   ```
   - A) `10`
   - B) `x`
   - C) `Error`
   - D) `None`

4. **Which of the following is not true about variables in Python?**
   - A) Variables can be reassigned to different data types.
   - B) Variables must start with a letter or an underscore.
   - C) Variables are case-sensitive.
   - D) Variables must be declared before use.

5. **What will be the output of the following code?** [Python Quiz #76]

   ```python
   x = 5
   y = x
   x = 7
   print(y)
   ```
      - A) `7`
      - B) `5`
      - C) `0`
      - D) `None`

6. **Why is it important to use meaningful variable names?**
   - A) It is required by the Python interpreter.
   - B) It helps make the code more readable and maintainable.
   - C) It increases the execution speed of the program.
   - D) It is necessary for the code to run without errors.

7. **What will be the output of the following code?** [Python Quiz #77]

   ```python
   a = 1
   b = a
   a = a + 1
   print(a, b)
   ```
      - A) `1 1`
      - B) `2 1`
      - C) `1 2`
      - D) `2 2`

8. **Which of the following is a valid variable name in Python?**
   - A) `2ndValue`
   - B) `value#2`
   - C) `_value2`
   - D) `value-2`

9.  **Which of the following is a correct way to declare a variable in Python?**
   - A) `int x = 5`
   - B) `x = 5`
   - C) `declare x = 5`
   - D) `var x = 5`
   
10. **What is the output of the following code?** [Python Quiz 78]
   ```python
   x = 5
   y = "Hello"
   print(x + y)
   ```
      - A) `5Hello`
      - B) `Hello5`
      - C) `TypeError`
      - D) `Hello 5`
   
11.  **Which of the following is not a valid variable name in Python?**
   - A) `my_var`
   - B) `_var`
   - C) `2var`
   - D) `var2`

12. **Which of the following statements is true about variable assignment in Python?**
   - A) Variables must be declared before they are assigned a value.
   - B) Variables are created when they are first assigned a value.
   - C) Variable names must begin with a number.
   - D) Python variables must be declared with a type.
   

# 38 What is the purpose of declaring a variable in Python?
a) To reserve memory space for the variable
b) To give the variable a name
c) To initialize the variable with a value
d) All of the above
Answer: d


   
**Answer key (Mutiple Choice):**

1. B) A placeholder for storing data values
2. C) A variable is a name that refers to a value.
3. A) `10`
4. D) Variables must be declared before use.
5. B) `5`
6. B) It helps make the code more readable and maintainable.
7. B) `2 1`
8. C) `_value2`
9. B) `x = 5`
10. C) `TypeError`
    - **Explanation:** In Python, the + operator is used for both arithmetic addition and string concatenation. However, it cannot be used to add an integer and a string directly. The code provided attempts to add an integer (x = 5) to a string (y = "Hello"), which is not a valid operation and will result in a TypeError.
11. C) `2var`
    - **Explanation:** In Python, variable names must start with a letter or an underscore and cannot start with a number. Thus, my_var, _var, and var2 are valid, but 2var is not.
12. B) Variables are created when they are first assigned a value.
13. A) `5`   

## Fill in the Blanks

1. Variable names in Python must start with a letter or an __________.
2. Variables in Python are __________, meaning they can change type when assigned a new value.
3. The assignment operator in Python is the __________ symbol.

**Answer Key (Fill in the Blanks):**

1.  underscore (_)
2.  dynamic
3.  equals (=)
   
## Exercises

### Exercise 1: Basic Variable Assignment

1. Create a variable called `name` and assign your name to it.
2. Create a variable called `age` and assign your age to it.
3. Create a variable called `city` and assign the city you live in to it.
4. Print all three variables.

### Exercise 2: Variable Reassignment

1. Create a variable called `favorite_color` and assign your favorite color to it.
2. Print the value of `favorite_color`.
3. Reassign a new color to `favorite_color`.
4. Print the new value of `favorite_color`.

### Exercise 3: Variable Operations

1. Create two variables called `a` and `b` and assign them the values 5 and 10, respectively.
2. Create a new variable called `sum` and assign it the value of `a` plus `b`.
3. Create a new variable called `difference` and assign it the value of `a` minus `b`.
4. Create a new variable called `product` and assign it the value of `a` times `b`.
5. Print the values of `sum`, `difference`, and `product`.

### Exercise 4: String Concatenation

1. Create a variable called `first_name` and assign your first name to it.
2. Create a variable called `last_name` and assign your last name to it.
3. Create a new variable called `full_name` and assign it the value of `first_name` concatenated with `last_name` (with a space in between).
4. Print the value of `full_name`.

**Example Solution:**
```python
first_name = "Alice"
last_name = "Johnson"

full_name = first_name + " " + last_name
print(full_name)
```

### Exercise 5: Input and Variables

1. Use the `input()` function to get the user's name and store it in a variable called `user_name`.
2. Use the `input()` function to get the user's age and store it in a variable called `user_age`.
3. Print a message saying "Hello [user_name], you are [user_age] years old."

**Example Solution:**
```python
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")

print("Hello", user_name + ", you are", user_age, "years old.")
```
6. Calculate the Area of a Circle with Radius [Example Solution](https://www.youtube.com/watch?v=QoECA8v_2tQ)
7. How to Swap Variables Without a Third Variable in Python. [Example Solution](https://youtu.be/CVy3A48WXeE)
8.  How to assign multiple values to multiple variables. [Example Solution](https://youtu.be/ur8rkDPzuSU)

## Review Questions

**1. What is a variable in computer programming?**
**Answer:** A variable is a named storage location in a computer's memory that is used to hold data or values. It allows programmers to store and manipulate data within a program.

**2. What is the purpose of using variables in programming?**
**Answer:** Variables provide a way to store and manage data that can be used and manipulated throughout a program. They make programs more flexible and allow for dynamic data storage.

**3. What is the difference between declaring and initializing a variable?**
**Answer:** Declaring a variable involves specifying its name and data type, while initializing a variable means giving it an initial value. Initialization usually follows declaration but is not always required.

4. What is a variable in computer programming? Give examples of integer, string, float, and Boolean variables.

## References and Bibliography



