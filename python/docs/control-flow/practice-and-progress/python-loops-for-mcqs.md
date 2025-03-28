# Python for loop (MCQs)

1. **What is the output of the following code snippet in Python?** [Python Quiz #3](https://bit.ly/3WKH9wE)

```python
for i in range(10):
    if i % 2 == 0:
        print(i)
```

A) 0 1 2 3 4 5 6 7 8 9
B) 0 2 4 6 8
C) 2 4 6 8
D) IndentationError: expected an indented block

**Watch the video for answer:** [https://bit.ly/3WKH9wE](https://bit.ly/3WKH9wE)

2. **What is the correct syntax for a for loop in Python?**

- A) for (int i = 0; i < 10; i++):
- B) for i in range(10):
- C) for i = 0 to 9:
- D) for i in 10:

**watch the video for the answer:** [https://youtu.be/2mhrDgBEp10](https://youtu.be/2mhrDgBEp10)

3. **What will be the output of the following code?** [Python Quiz #36](https://bit.ly/3WqjjEP)

```python
for i in range(5):
  print(i * 2)
```

    - A) 0 1 2 3 4
    - B) 2 4 6 8 10
    - C) 10 8 6 4 2
    - D) 0 2 4 6 8

**Watch this video for the answer:** [https://bit.ly/3WqjjEP](https://bit.ly/3WqjjEP)

4. **How many times is the print statement executed?** [Python Quiz #37](https://youtu.be/CYeZI3uCiTI)
```python
for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")
```

    - A) 3 times
    - B) 5 times
    - C) 6 times
    - D) 9 times

**Watch this video for the answer:** [https://youtu.be/CYeZI3uCiTI](https://youtu.be/CYeZI3uCiTI) 

1. **What will the program output if the `number` variable is set to `5`?**
```python
# Get user input
number = int(input("Enter non-negative number:"))

if number < 0:
    print("Factorial is not defined for negative numbers.")
    result = None
elif number == 0 or number ==1:
    result = 1
else:
    result = 1
    for i in range(2, number + 1):
        result *= i

if result is not None:
    print("Factorial of", number, "is", result)
```

- A) Factorial is not defined for negative numbers.
- B) Factorial of 5 is 5
- C) Factorial of 5 is 120
- D) Factorial of 5 is 24

**Watch this video for the answer:** [https://youtu.be/K5LV5I2hFg4](https://youtu.be/K5LV5I2hFg4)

6. **What will happen if the `number` variable is set to `0`?**

```python
# Get user input
number = int(input("Enter non-negative number:"))

if number < 0:
    print("Factorial is not defined for negative numbers.")
    result = None
elif number == 0 or number ==1:
    result = 1
else:
    result = 1
    for i in range(2, number + 1):
        result *= i

if result is not None:
    print("Factorial of", number, "is", result)
```

- A) The program will raise an error.
- B) The program will print "Factorial of 0 is 1".
- C) The program will print "Factorial is not defined for negative numbers."
- D) The program will print "Factorial of 0 is 0".

**Watch this video for the answer:** [https://youtu.be/K5LV5I2hFg4](https://youtu.be/K5LV5I2hFg4)

**What is the primary purpose of a for loop in Python?**

    - A) To define a function
    - B) To iterate over a sequence
    - C) To create a conditional statement
    - D) To perform mathematical operations

**In Python, what does the range() function do when used in a for loop?**
    - A) Generates a sequence of numbers
    - B) Defines a list
    - C) Calculates the average
    - D) Determines the length of a string

**How can you create a nested loop in Python?**

    - A) by using a loop inside another loop with proper indentation
    - B) by using a loop inside another loop with parentheses
    - C) by using a nested keyword before the inner loop
    - D) by using a colon after the outer loop and before the inner loop

**Answer:** A

### Question 4
**Consider the following code:**
```python
total = 0
for i in range(1, 6):
    total += i
print(total)
```
**What does this code accomplish?**

A) It prints numbers from 1 to 5.
B) It calculates the sum of numbers from 1 to 5.
C) It prints the sum of numbers from 1 to 6.
D) It calculates the sum of numbers from 0 to 5.

*Explanation:* The loop iterates over the range from 0 to 5 (inclusive), summing up the values. The `total` variable accumulates this sum.

### Question 6

**How can a `for` loop be used in a real-life scenario involving data processing?**

A) To count the number of words in a large document.
B) To open a web browser.
C) To create a new file on the desktop.
D) To turn off a computer.

*Explanation:* A `for` loop can be used to iterate through the words in a document to count them, making it useful for data analysis tasks.

**Answer:** A

**Why might you use a `for` loop instead of manually performing repeated tasks?**

    - A) To reduce the chance of human error.
    - B) To make the program run slower.
    - C) To avoid using variables.
    - D) To limit the program to one iteration.

*Explanation:* Using a `for` loop automates repetitive tasks, which helps prevent errors and saves time, especially when processing large datasets or performing repetitive calculations.

**Answer:** A

**What does the following code print?**
```python
for x in range(5, 8):
    print(x)
```
    - A) 5 6 7
    - B) 5 6 7 8
    - C) 4 5 6 7
    - D) 5 6 7 8 9

*Explanation:* The `range(5, 8)` function generates numbers starting from 5 up to, but not including, 8.

**Answer:** A

**What does the following code output?**
```python
for i in range(1, 4):
    for j in range(1, 3):
        print(i, j)
```
A) 1 1 1 2 2 1 2 2 3 1 3 2
B) 1 2 2 3 3 4
C) 1 3 2 3 3 3
D) 1 1 2 2 3 3

*Explanation:* This is a nested loop, where the outer loop runs from 1 to 3 (inclusive) and the inner loop runs from 1 to 2 (inclusive). It prints all combinations of `i` and `j`.

**Answer:** A

**What will be the output of this code?**
```python
for i in range(3):
    print(i * i)
```
A) 0 1 4
B) 0 1 2
C) 1 4 9
D) 0 2 4

*Explanation:* The loop iterates over the range 0, 1, 2. For each iteration, it prints the square of the current index `i`.

**Answer:** A

**What will the following code output?**
```python
for i in range(5, 10, 2):
    print(i)
```
A) 5 7 9

B) 5 6 7 8 9

C) 5 7 9 11

D) 5 7 8

*Explanation:* The `range(5, 10, 2)` generates numbers starting from 5 up to, but not including, 10 with a step of 2, resulting in 5, 7, and 9.

**Answer:** A

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1602443888929206"
     crossorigin="anonymous"></script>
<ins class="adsbygoogle"
     style="display:block"
     data-ad-format="autorelaxed"
     data-ad-client="ca-pub-1602443888929206"
     data-ad-slot="7879511511"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
