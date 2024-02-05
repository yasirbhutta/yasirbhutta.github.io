# Python

## Data Structures and Sequences

### Tuple

- In python, a tuple is an immutable sequence of elements. it is similar to a list, but the elements of a tuple cannot be modified once they are created.
- Tuple is a collection data type in python. It is usefule for storing multiple related values as a single unit.
- Sequence types in python - list, tuple and range

#### Creating a Tuple

- A tuple is creatd by placing all the items (elements) inside parentheses () and separated by commas. The parentheses are optiona, however, it is a good practive to use them. 

#### Example 1

Some common ways to create tuples in Python include:

```python
tup = (1,2,3)
print(tup) # Output: (1, 2, 3)
# check the type of variable
print(type(tup)) # Output: <class 'tuple'>

# another example to create tuple
tup1 = 4,5,6
print(tup1) # Output: (4, 5, 6)

# tuple with mixed datatypes
tup_mixed = (7, "String", 7.8)
print(tup_mixed)

# Tuples may be nested
nested_tup = tup1, (7,8)
print(nested_tup) #Output: ((4, 5,6), (7, 8)) 

# using the 'tuple()' function 
tup3 = ([7,2,9])
print(tup3) #Output (7,2,9)

tup4 = tuple('string')
print(tup4) # Output: ('s','t','r','i','n','g')

```
A nested tuple is a tuple that contains one or more tuples as element.

#### Empty and single item tuple

- A special problem is the construction of tuples containing 0 or 1 item.
- Empty tuples are constructed by an empty pair of parentheses
- A tuple with one item is constructed by following a value with a comma (it is not sufficient to enclose a single value in parentheses.

#### Accessing the elements of Tuple

#### Example #2

```python
# Tuples are immutable
# but they can contain mutable objects
```
#### Unpacking tuples
#### Tuple methods


### Tuple

- [#1 Tuple Assignment](https://www.youtube.com/watch?v=ebhkBYgR7QI&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=104)
- [#2 Tuple Assignment](https://www.youtube.com/watch?v=fi-nvcQukRc&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=105)
-[How to create a tuple in Python](https://www.youtube.com/watch?v=QpRiHuQycXg&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=84)
- [Learn how to print elements of a tuple](https://www.youtube.com/watch?v=MGgazFPSrS4&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=32)
- [How to Calculate the Sum of a Tuple Using a For Loop](https://www.youtube.com/watch?v=PFNJl8i4y1c&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=33)
- [How to create an Empty tuple and Single value tuple](https://www.youtube.com/watch?v=nGIWcYXj580&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=83)
- [How to: Access Tuple Items in Python](https://www.youtube.com/watch?v=6dZUdvI8V_Q&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=81)

### List

- [How to use list](https://www.youtube.com/watch?v=LKZmCAL92pI&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=103)
- [Python List Slicing](https://www.youtube.com/watch?v=ELA_-RxwDB8&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=110)
- [Python Nested List](https://www.youtube.com/watch?v=BOIn5oW868A&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=111)
- [How to modify a list by replacing multiple elements with a single element](https://www.youtube.com/watch?v=uvdT5kczvCg&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=80)
- [Adding and Removing Elements from a Python List](https://www.youtube.com/watch?v=x98wvk-4MHw&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=76)
- [Check if Data Structure is Empty Using 'not' Operator](https://www.youtube.com/watch?v=K4WUapBO_E0&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=2)
- [Remove duplicate elements from a list](https://www.youtube.com/watch?v=RekQ2j4yzIQ&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=1)
- [List Index Function: Find the Index of an Element in a List](https://www.youtube.com/watch?v=thYJRk4huGE&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=41)
- [List pop() Method](https://www.youtube.com/watch?v=S6HkdH4Xnog&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=84)

### Built-in Sequence Functions

- [#1 Python zip() Function](https://www.youtube.com/watch?v=7ix3cDWAsUc&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=57)
- [#2 Python Zip Function: Handling Lists with Different Numbers of Elements](https://www.youtube.com/watch?v=TOxTxP9x4ME&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=56)
- [Python Iterators and Iterables: How to Loop Over Lists and Iterators](https://www.youtube.com/watch?v=D2YDffp1Oag&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=34)
- [How to Iterate Over Tuples with the Enumerate Function](https://www.youtube.com/watch?v=QtjIK_knBLo&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=31)
- [Finding the maximum value in a list using a one-liner](https://www.youtube.com/watch?v=S-c7WrZSyaQ&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=4)
- [Find the sum of all even numbers between 1 and 100 using a one-liner](https://www.youtube.com/watch?v=tOxaYOtN-8s&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=3)
- [Counting the number of occurrences of an element in a list](https://www.youtube.com/watch?v=S2el4USCp5k&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=2)

### dict

- [Use of dict](https://www.youtube.com/watch?v=WOjUtknwLMQ&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=100)
- [How to Print a Dictionary](https://www.youtube.com/watch?v=gAbLxC40Tgc&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=40)
- [Python Dictionary with For Loop](https://www.youtube.com/watch?v=NNeZTEMNKhw&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=99)
- [How to Merge Dictionaries with the \| Operator](https://www.youtube.com/watch?v=ZJ9uidFIVhs&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=1)
- [dictionary copy() method](https://www.youtube.com/watch?v=PXp9uzvKFdU&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=82)

### set

- [How to: Add or Remove Elements in a Set](https://www.youtube.com/watch?v=96f2SKK_QZk&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=98)
- [How to: Create Empty Set in Python](https://www.youtube.com/watch?v=nmI7BGXPA4I&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=77)
- [Find the Union of Two Sets in Python](https://www.youtube.com/watch?v=YDyCNYCUK9A&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=72)

### List, Set and Dict Comprehensions

#### List Comprehensions

**List comprehension examples:**

- [List Comprehension with Easy-to-Understand Code Example](https://www.youtube.com/watch?v=1fVckZom4K0&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=71)
- [Create a list of squares of all even numbers](https://www.youtube.com/watch?v=4qy1QRTn6r4&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=70)
- [How to Convert List Elements to Upper Case](https://www.youtube.com/watch?v=RXKMwEGYKs4&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=63)
- [How to: Use list comprehension for DATA CLEANING](https://www.youtube.com/watch?v=geI-5gXMrks&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=62)
- [Real-Life Use Case for List Comprehension](https://www.youtube.com/watch?v=MZwEfGXgpfI&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=61)

#### Dict Comprehension


Dictionary comprehensions are a powerful and concise way to create dictionaries in Python.

**Syntax:**

```python
{key_expression: value_expression for item in iterable if condition}
```

- Python Challenge to test your knowledge [Quiz1](https://www.youtube.com/watch?v=x7zh_WqO1e4&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=21) [Quiz2](https://www.youtube.com/watch?v=rEDmm9ry7wE&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=5) [Quiz3](https://www.youtube.com/watch?v=ZWB4dfUYz1k&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=4)

