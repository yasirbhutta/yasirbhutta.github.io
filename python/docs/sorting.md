---
layout: page
title: Sorting Techniques in Python - Sorting How To
description: Learn Python basics with beginner-friendly tutorials, examples, and exercises. Master Python programming concepts like print function, variables, comments, indentation and more. Perfect for students and professionals starting their Python journey.
keywords: Python basics, Python tutorials for beginners, Python examples, Python exercises, Python print function, python comments Python variables, Python data types, Python programming for beginners, learn Python, Python coding exercises
toc: toc/python.html
---

Python lists have a built-in list.sort() method that modifies the list in-place. There is also a sorted() built-in function that builds a new sorted list from an iterable.

We explore the various techniques for sorting data using Python.

## Sorting Basics

### list.sort()

Sorts the elements of a list in place, meaning it modifies the original list directly.

**Syntax:**

```python
list.sort(key=None, reverse=False)
```

**Parameters:**

**key (optional):** A function that takes a single element from the list and returns a key to be used for sorting. This allows for custom sorting criteria.
**reverse (optional):** A boolean value. If True, sorts the list in descending order. Defaults to False (ascending order).

### Python Code Example: Sorting a List in Ascending and Descending Order

```python
# Creating a list of numbers
numbers = [5, 2, 9, 1, 5, 6]

# Sorting the list in ascending order
numbers.sort()
print("Sorted in ascending order:", numbers)

# Sorting the list in descending order
numbers.sort(reverse=True)
print("Sorted in descending order:", numbers)
```

### Output:
```
Sorted in ascending order: [1, 2, 5, 5, 6, 9]
Sorted in descending order: [9, 6, 5, 5, 2, 1]
```

### Sorting a List of Strings:
```python
# List of names
names = ["John", "Alice", "Bob", "Charlie"]

# Sorting alphabetically
names.sort()
print("Alphabetically sorted:", names)

# Sorting in reverse alphabetical order
names.sort(reverse=True)
print("Reverse alphabetical order:", names)
```

**Example:**

- [Video: List sort() Function](https://www.youtube.com/watch?v=qBBEjpyAJcM&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=48)

### sorted Function

The `sorted()` function in Python is used to return a new sorted list from an iterable (like a list, tuple, or string) without modifying the original list.  

**Syntax:**

```python
sorted(iterable, key=None, reverse=False)
```

**Parameters:**

**iterable:** The iterable object to be sorted (e.g., a list, tuple, string).
**key (optional):** A function that takes a single element from the iterable and returns a key to be used for sorting. This allows for custom sorting criteria.
**reverse (optional):** A boolean value. If True, sorts the iterable in descending order. Defaults to False (ascending order).

### Python Code Example 1: Sorting a List of Numbers

```python
# Original list
numbers = [5, 2, 9, 1, 5, 6]

# Sorting in ascending order
sorted_numbers = sorted(numbers)
print("Sorted in ascending order:", sorted_numbers)

# Sorting in descending order
sorted_numbers_desc = sorted(numbers, reverse=True)
print("Sorted in descending order:", sorted_numbers_desc)

# Original list remains unchanged
print("Original list:", numbers)
```
#### Output:
```
Sorted in ascending order: [1, 2, 5, 5, 6, 9]
Sorted in descending order: [9, 6, 5, 5, 2, 1]
Original list: [5, 2, 9, 1, 5, 6]
```

---

### Python Code Example 2: Sorting a List of Strings
```python
# List of names
names = ["John", "Alice", "Bob", "Charlie"]

# Sorting alphabetically
sorted_names = sorted(names)
print("Alphabetically sorted:", sorted_names)

# Sorting in reverse alphabetical order
sorted_names_desc = sorted(names, reverse=True)
print("Reverse alphabetical order:", sorted_names_desc)
```

---

### Python Code Example 3: Sorting with a Custom Key

You can use the `key` parameter to sort based on custom criteria.

```python
# Sorting words by length
words = ["apple", "banana", "kiwi", "grape"]

# Sorting by word length (shortest to longest)
sorted_words = sorted(words, key=len)
print("Sorted by word length:", sorted_words)
```

#### Output:
```
Sorted by word length: ['kiwi', 'grape', 'apple', 'banana']
```

**Examples:**

- [Video: sorted() Function](https://www.youtube.com/watch?v=Ic58XdR9TS0&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=55)


## Key Functions

Both list.sort() and sorted() have a key parameter to specify a function (or other callable) to be called on each list element prior to making comparisons.

**Examples:**

- [Video: Sorting a List of Colors by Length using Python's sorted() Function](https://www.youtube.com/watch?v=gt1YbVzwxXQ&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=54)
- [Video: How to Sort a List of Fruit Tuples](https://www.youtube.com/watch?v=mtN5WCXzXyo&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=53)
- [Video: Sorting a List of Dictionaries by Age using Lambda Function](https://www.youtube.com/watch?v=dRNiLVkPtRg&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=52)

## Operator Module Functions

## Ascending and Descending

Both list.sort() and sorted() accept a reverse parameter with a boolean value. This is used to flag descending sorts. 

## Sort Stability and Complex Sorts

## Decorate-Sort-Undecorate

## Comparison Functions

## True/False (Mark T for True and F for False)

- The list.sort() method modifies the original list. **True or Fasle**
- The sorted() function returns a new sorted list. **True or False**
- The key parameter is used to specify a custom sorting function. **True or False**
- The reverse parameter is used to reverse the sorting order. **True or False**
- The sorted() function can only sort lists. **True or False**

## Multiple Choice (Select the best answer)

> Which of the following statements sorts a list in descending order?

1. [ ] list.sort(reverse=True)
2. [ ] sorted(list, reverse=True)
3. [ ] list.reverse()
4. [ ] sorted(list, ascending=False)

> What is the output of the following code?

```python
numbers = [3, 1, 4, 2]
numbers.sort(key=lambda x: -x)
print(numbers)
```
1. [ ] [1, 2, 3, 4]
2. [ ] [4, 3, 2, 1]
3. [ ] [1, 4, 2, 3]
4. [ ] [3, 4, 1, 2]

> How would you sort a list of tuples by the second element of each tuple?

1. [ ] list.sort(key=lambda x: x[1])
2. [ ] sorted(list, key=lambda x: x[1])
3. [ ] list.sort(key=operator.itemgetter(1))
4. [ ] All of the above

## Fill in the Blanks

1. The _______ method sorts a list in place.
2. The _______ function returns a new sorted list.
3. The _______ parameter is used to specify a custom sorting function.
4. The _______ parameter is used to reverse the sorting order.

#49 How can you sort a list of dictionaries based on a specific key?

people = [
    {'name': 'Ali', 'age': 25},
    {'name': 'Ahmad', 'age': 30},
    {'name': 'Hamza', 'age': 20}
]

Watch these Videos Tutorial for the Answer: 
https://youtube.com/shorts/dRNiLVkPtRg?feature=share
#python #pythonpoll #MCQsTest #yasirbhutta


a. sorted_people = sorted(people, key='name')
b. sorted_people = sorted(people, key='age')
c. sorted_people = sorted(people, key=lambda  x['name'])
d. sorted_people = sorted(people, key=lambda x: x['age'])


#48 Which of the following is an example of using the sorted() function to sort a list of strings in reverse alphabetical order?

Watch these Videos Tutorial for the Answer: 
https://youtube.com/shorts/qBBEjpyAJcM?feature=share

https://youtube.com/shorts/Ic58XdR9TS0?feature=share

#python #pythonpoll #MCQsTest #yasirbhutta


a. sorted_fruits = sorted(fruits)
b. sorted_fruits = sorted(fruits, reverse=True)
c. sorted_fruits = sorted(fruits, key=len)
d. sorted_fruits = sorted(fruits, key=lambda x: x[-1], reverse=True

#45 What is the difference between the sort() and sorted() functions in Python?




a. sort() is a built-in function that returns a new sorted list, while sorted() is a method that sorts the list in-place.

b. sort() can only be used on any iterable, while sorted() can be used on lists.

c. sort() is a method that sorts the list in-place, while sorted() is a built-in function that returns a new sorted list.

d. sort() returns a new list, while sorted() returns None.



Which of the following is an example of using the sort() method to sort a list of integers in descending order?
a. nums.sort(reverse=True)
b. nums = sort(nums, reverse=True)
c. sorted(nums, reverse=True)
d. nums = nums.sort(reverse=True)

Which of the following is an example of using the sorted() function to sort a list of strings in reverse alphabetical order?
a. sorted_fruits = sorted(fruits)
b. sorted_fruits = sorted(fruits, reverse=True)
c. sorted_fruits = sorted(fruits, key=len)
d. sorted_fruits = sorted(fruits, key=lambda x: x[-1], reverse=True)


How can you sort a list of tuples based on the second element of each tuple?
a. sorted_items = sorted(items, key=lambda x: x[2])
b. sorted_items = sorted(items, key=lambda x: x[1])
c. sorted_items = sorted(items, key=lambda x: x[-1])
d. sorted_items = sorted(items, key=lambda x: x[0])



## Exercises

**1. Sorting Numbers:**

- Create a list of numbers and sort them in ascending order using both `list.sort()` and `sorted()`.
- Sort a list of numbers in descending order.
- Sort a list of numbers in ascending order, but keep the original list intact.
- Sort a list of numbers based on their absolute values.

**2. Sorting Strings:**

- Sort a list of strings alphabetically.
- Sort a list of strings in reverse alphabetical order.
- Sort a list of strings by their length. [solution](https://www.youtube.com/watch?v=gt1YbVzwxXQ&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=54)
- Sort a list of strings alphabetically, but case-insensitively.

**3. Sorting Tuples:**

- Sort a list of tuples by their first element.
- Sort a list of tuples by their second element.
- Sort a list of tuples by the length of their second element.

**4. Sorting Dictionaries:**

- Sort a list of dictionaries by their keys.
- Sort a list of dictionaries by their values.
- Sorting a List of Dictionaries by Age using Lambda Function [Solution](https://youtu.be/dRNiLVkPtRg?si=K-HgUPBIcZ9XNaYh)

**5. Custom Sorting:**

- Sort a list of objects based on a custom attribute.
- Sort a list of words based on the number of vowels in each word.
- Sort a list of employees based on their salary, then by their name if salaries are equal.

**6. Sorting Algorithms:**

- Implement the bubble sort algorithm.
- Implement the insertion sort algorithm.
- Implement the selection sort algorithm.
- Implement the merge sort algorithm.
- Implement the quick sort algorithm.

**7. Advanced Sorting:**

- Sort a large list of numbers efficiently using a suitable algorithm.
- Sort a list of items based on multiple criteria.
- Handle sorting of mixed data types (e.g., numbers, strings, tuples).
- Implement a stable sorting algorithm.

## Review Questions

- Explain the difference between list.sort() and sorted().
- What is the purpose of the key parameter in sorting functions?

## References and Bibliography

- [Sorting HOW TO: Python - Documentation](https://docs.python.org/3/howto/sorting.html)
