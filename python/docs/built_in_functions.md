# Built-in Functions

The Python interpreter has a number of functions and types built into it that are always available. 

## Built-in Functions

### Filter()

- In Python, the 'filter()' function is used to filter a sequence (e.g. list, tuple, etc.) by applying a certain test to each eleent of the sequence and returning only the elements that pass the test.
- The 'filter()' function takes two arguments: function and an iterable. The function is applied to each element of the iterable, and if the function retuns 'True' for that element, the element is included in the resulting iterable.

### Example #5 use of lambda in filter() function

```python

numbers = [1,2,3,4,5,6,7,8,9,10] # list

even_numbers= list(filter(lambda x : x % 2 == 0,numbers))

print(even_numbers)

```

### Map()

- In Python, the 'map()' function is used to apply a certain function to each element of an iterable (e.g. list, tuple, etc.) and return an iterable containing the results.
- The 'map()' function takes two arguments: a function and an iterable. The function is applied to each element of the iterable, and the result of the function is included in the resulting iterable. 

**Example #6:** use of lambda in map() function

```python

numbers = [1,2,3,4,5,6,7,8,9,10]

squared_numbers = map(lambda x : x **2 ,numbers)

print(list(squared_numbers))

```

[need to add details]

**See also:**

- [Video: How to: use a LAMBDA function as an argument in filter() and map()](https://www.youtube.com/watch?v=xUKmtRJBWuA&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=82)

**See also:**

- [Built-in Functions - Python 3.12.1 documentation](https://docs.python.org/3/library/stdtypes.html)
  

## Key Terms

## True/False (Mark T for True and F for False)

**Answer Key (True/False):**

## Multiple Choice (Select the best answer)

**Answer key (Mutiple Choice):**

**What is the output of the following Python code?**

numbers = [10, 32, 98, 38, 47, 34]
print(max(numbers))

    - **A.** 10 
    - **B.** 32 
    - **C.** 98 
    - **D.** 38

**Watch this video for the answer:** [https://youtube.com/shorts/x7zh_WqO1e4](https://youtube.com/shorts/x7zh_WqO1e4)

**What is the output of the following code?** [Python Quiz #11]

```python
def my_func(fruit):
    if fruit:
        return  True
    return  False

fruits = ["apple","", "orange"
,"mango" ]

print(list(filter(my_func,fruits)))
```python

**A)** ['apple', 'orange', 'mango']
**B)** ['apple', '', 'orange', 'mango']
**C)** ['', '', '']
**D)** ['True', 'False', 'True', 'True']

**Watch this video for the answer:** [https://youtube.com/shorts/gkGpJfxsDew](https://youtube.com/shorts/gkGpJfxsDew)

#43 What is the output of the zip() function when one iterable is shorter than the others?

Watch the Video Tutorial for the Answer: https://youtube.com/shorts/TOxTxP9x4ME?feature=share

#python #pythonpoll #MCQsTest #yasirbhutta

a) The function raises an exception
b) The function returns only the tuples that have corresponding elements in all iterables
c) The function pads the shorter iterable with None values
d) The function pads the shorter iterable with the last value of the iterable

Answer: b) The function returns only the tuples that have corresponding elements in all iterables

#42 What does the zip() function in Python do?

Watch the Video Tutorial for the Answer: https://youtube.com/shorts/7ix3cDWAsUc?feature=share

#python #pythonpoll #MCQsTest #yasirbhutta

a) Compresses a file into a ZIP archive
b) Combines two or more iterables into a single iterable of tuples, where each tuple contains one element from each iterable
c) Creates a dictionary from two iterables, with keys from one iterable and values from another iterable
d) Calculates the checksum of a file


Answer: b) Combines two or more iterables into a single iterable of tuples, where each tuple contains one element from each iterable

Q: What is the syntax for the zip() function in Python?
a) zip(iterable1, iterable2)
b) zip(iterable1, iterable2, ...)
c) zip(*iterables)
d) zip(iterables)

Answer: c) zip(*iterables)



Q: How can you use the zip() function to unzip a list of tuples?
a) list(zip(*tuples_list))
b) tuple(zip(*tuples_list))
c) set(zip(*tuples_list))
d) dict(zip(*tuples_list))

Answer: a) list(zip(*tuples_list))



## Fill in the Blanks

**Answer Key (Fill in the Blanks):**

## Exercises

## Review Questions

## References and Bibliography

[1]“Built-in Functions — Python 3.12.4 documentation,” docs.python.org. [https://docs.python.org/3/library/functions.html](https://docs.python.org/3/library/functions.html)
‌
