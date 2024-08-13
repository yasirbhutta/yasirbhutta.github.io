## Error and Exception Handling

- [Python Exception Handling run-time error : division by zero](https://www.youtube.com/watch?v=1fj8HifChyE&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=93)

## Key Terms

## Fix the Error in Python

### 7. **`else` Block After `try` Without `except`**

**Code:**
```python
try:
    result = 10 / 2
else:
    print("Division successful!")
```

**Mistake:**  
An `else` block is used incorrectly after `try` without an `except` block.

**Corrected Code:**
```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("Division successful!")
```
- Now, the `else` block runs only if no exception occurs.



## True/False (Mark T for True and F for False)

**Answer Key (True/False):**

## Multiple Choice (Select the best answer)

1. **Which function would you use to determine the type of a variable in Python?**
   - A) id()
   - B) type()
   - C) str()
   - D) isinstance()

What is the correct way to raise an exception in Python?
a) raise Exception("error message")
b) throw Exception("error message")
c) exit("error message")
d) halt("error message")

**Watch this video for the answer:**

**Answer key (Mutiple Choice):**

## Fill in the Blanks

**Answer Key (Fill in the Blanks):**

## Exercises

## Review Questions

## References and Bibliography


