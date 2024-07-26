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

- [Exercise #11: How to Swap Variables in One Line of Code using Tuple Unpacking](https://www.youtube.com/watch?v=MCeTYJVktmU&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=45)
- 
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
- **Python set examples:**
- [How to Find Duplicates in a List using Set and List Functions](https://www.youtube.com/watch?v=FgTrz4h9YV8&list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja&index=46)

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


## Key Terms

## True/False (Mark T for True and F for False)

**Answer Key (True/False):**

## Multiple Choice (Select the best answer)

1. **Which function would you use to determine the type of a variable in Python?**
   - A) id()
   - B) type()
   - C) str()
   - D) isinstance()

**What is the output of the following code? [Python Quiz #15]**

```python
a = ('34.5')
print(type(a))
```

- A) <class 'list'>
- B) <class 'tuple'>
- C) <class 'int'>
- D) <class 'str'>

**Watch the video for the answer:** [https://youtube.com/shorts/uMtHVgPSymw](https://youtube.com/shorts/uMtHVgPSymw)



What is the data type of the following value?
frozenset({1, 2, 3})
a) list b) tuple c) set d) frozenset

Answer: d) frozenset

What is the data type of the following value?
{1, 2, 3}
a) list b) tuple c) set d) dict

Answer: c) set

What is the data type of the following value?
{1, 2, 3}
a) list b) tuple c) set d) dict

Answer: c) set

What is the data type of the following value?
(1, 2, 3)
a) list b) tuple c) set d) dict

Answer: b) tuple

What is the data type of the following value?
{"name": "Alice", "age": 25}
a) list b) tuple c) set d) dict

Answer: d) dict

What is the data type of the following value?
[1, 2, 3]
a) list b) tuple c) set d) dict

Answer: a) list

What is the correct way to create a set in Python?

a) set = [1, 2, 3] b) set = (1, 2 ,3) c) set = {1, 2 ,3} d) set = <1, 2 ,3>

Answer: c) set = {1, 2 ,3}

#58 What is the correct way to create a loop in Python?

a) for i in range(10): 
b) while i < 10: 
c) repeat i = 0 to 9: 
d) either a or b

Answer: d) either a or b

#53 What is the correct way to create a dictionary in Python?

a) dict = [key: value]
 b) dict = (key: value) 
c) dict = {key: value} 
d) dict = <key: value>

Answer: c) dict = {key: value}

#52 What is the correct way to create a list in Python?

a) list = [1, 2, 3] 
b) list = (1, 2, 3) 
c) list = {1, 2, 3} 
d) list = <1, 2, 3>

**Watch this video for the answer:**

#47 In Python, What is the output of the following code?

a = [1, 2, 3, 4]
b = [5, 7, 4, 9,2]
print (a[-1] in b)

Follow me 
https://www.facebook.com/yasirbhutta786

True
False
Error
None

#35 What is the output of the following code?

def fun(arr):
    arr = arr[::-1]
    
arr = [1,2,3,4,5]
fun(arr)
print(arr)

Watch the Video Tutorial for the Answer: https://youtube.com/shorts/Ix-h6WR-vQM?feature=share

#python #pythonpoll #MCQsTest #yasirbhutta

[1,2,3,4,5]
[5,4,3,2,1]
[]
Error

Answer: A.

#24 What is the syntax to create a union of two sets in Python?

Watch the Video Tutorial for the Answer: https://youtu.be/YDyCNYCUK9A

#python #pythonpoll #MCQsTest #yasirbhutta

a. set1 + set2
b. set1.union(set2)
c. set1 & set2
d. set1.merge(set2)

Answer: b. set1.union(set2)

#26 What is the result of the following code?

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.union(set2)
print(set3)

Watch the Video Tutorial for the Answer: https://youtu.be/YDyCNYCUK9A

#python #pythonpoll #MCQsTest #yasirbhutta


a. {1, 2, 3}
b. {3, 4, 5}
c. {1, 2, 3, 4, 5}
d. {3}
Answer: c. {1, 2, 3, 4, 5}

Is it possible to use the union operator | to combine sets with different data types?
a. Yes
b. No
Answer: b. No

#25 Can the union of two sets contain duplicates?

Watch the Video Tutorial for the Answer: https://youtu.be/YDyCNYCUK9A

#python #pythonpoll #MCQsTest #yasirbhutta

a. Yes
b. No
Answer: b. No

#27 What happens when you try to add an element to a set that already exists in the set?

Watch the Video Tutorial for the Answer: https://youtu.be/YDyCNYCUK9A

#python #pythonpoll #MCQsTest #yasirbhutta


a. A TypeError occurs
b. The element is added as a duplicate
c. Nothing happens, the element is not added

Answer: c. Nothing happens, the element is not added.

What is the output of the following code?

list1 = [10,20,10,'10',20]
set1 = set(list1)
print(set1)

5
3
2
4
Answer: B) 3

What is the output of the following code?

set1 = {1,2,3}
set2 = {1,2,3}
print(*(set1+set2))

Error
{2,4,6}
[2,4,6]
[1,2,3]

Answer: A) error + operator is not supported for set

What does the "in" operator do in Python?
a) check if a value is present in a list
b) check if a value is equal to another value
c) check if a variable is defined
Answer: a) check if a value is present in a list

Can the "in" operator be used with dictionaries in Python?
a) yes
b) no
Answer: a) yes

How would you check if the value "dog" is in the list ['cat', 'dog', 'elephant'] using the "in" operator?
a) 'dog' in ['cat', 'dog', 'elephant']
b) ['dog'] in ['cat', 'dog', 'elephant']
Answer: a) 'dog' in ['cat', 'dog', 'elephant']


Can the "in" operator be used to check if an element is present in a set in Python?
a) yes
b) no
Answer: a) yes

How would you check if the value "dog" is in the set {'cat', 'dog', 'elephant'} using the "in" operator?
a) 'dog' in {'cat', 'dog', 'elephant'}
b) {'dog'} in {'cat', 'dog', 'elephant'}
Answer: a) 'dog' in {'cat', 'dog', 'elephant'}

#14 Is the "in" operator faster for checking if an element is present in a set compared to a list in Python?

https://lucasmagnum.medium.com/pythontip-list-vs-set-performance-experiments-dfbe4f72d47f

a) yes
b) no
Answer: a) yes

#13 What does the "in" operator do in Python?

a) check if a value is present in a list
b) check if a value is equal to another value
c) check if a variable is defined
Answer: a) check if a value is present in a list

Can the "in" operator be used with dictionaries in Python?

a) yes
b) no
Answer: a) yes

How would you check if the value "dog" is in the list ['cat', 'dog', 'elephant'] using the "in" operator?

a) 'dog' in ['cat', 'dog', 'elephant']
b) ['dog'] in ['cat', 'dog', 'elephant']
Answer: a) 'dog' in ['cat', 'dog', 'elephant']

What is the operator used to check if an element is present in a set in python?

in
contains
has 
exit

Answer: A) in


What is the output of the following code?


>>>t=(1,2,4,3)
>>>t[1:3]
a) (1, 2)
b) (1, 2, 4)
c) (2, 4)
d) (2, 4, 3)

#8 What is the output of the following code?

z=set('stri$ng')
print('r' in z)

Python YouTube Playlist: https://www.youtube.com/playlist?list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja

a) Error
b) True
c) False
d) No output

Which of the following is a Python tuple?

Python YouTube Playlist: https://www.youtube.com/playlist?list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja

a) {1, 2, 3}
b) {}
c) [1, 2, 3]
d) (1, 2, 3)

#9 Which of the following Python statements will result in the output: 6

A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

Python YouTube Playlist: https://www.youtube.com/playlist?list=PLKYRx0Ibk7Vi-CC7ik98qT0VKK0F7ikja


a) A[2][1]
b) A[1][2]
c) A[3][2]
d) A[2][3]

Answer: b
Explanation: The output that is required is 6, that is, row 2, item 3. This position is represented by the statement: A[1][2].

11# Which of the following statements is used to create an empty set in Python?

related video:https://youtube.com/shorts/nmI7BGXPA4I

a) ( )
b) [ ]
c) { }
d) set()
Explanation: { } creates a dictionary not a set. Only set() creates an empty set.


#15 What method is used to add an element to the end of a list in Python?

Watch the Video Tutorial for the Answer:https://youtu.be/x98wvk-4MHw

#python #pythonpoll #MCQsTest

A) append()
B) insert()
C) extend()
D) append_list()
Answer: A) append()

#16 How do you add an element to a specific index in a list in Python?

Watch the Video Tutorial for the Answer: https://youtu.be/x98wvk-4MHw

#python #pythonpoll #MCQsTest 

A) add_index()
B) insert()
C) extend()
D) append()
Answer: B) insert()

#17 What function is used to remove the last element from a list in Python?

Watch the Video Tutorial for the Answer:https://youtu.be/x98wvk-4MHw

#python #pythonpoll #MCQsTest #yasirbhutta


A) del_last()
B) remove_last()
C) pop()
D) delete_end()
Answer: C) pop()

#18 How can you remove the first occurrence of an element from a list in Python?

Watch the Video Tutorial for the Answer: https://youtu.be/x98wvk-4MHw

#python #pythonpoll #MCQsTest #yasirbhutta

A) remove()
B) delete_first()
C) pop_first()
D) del_first()
Answer: A) remove()

What is the output of the following code?

list1 = [12,98,23,70,66]
list1[1:4] = [20]
print(list1)

[12,20,66] 
[12,20,23,70,66]
 [12,98,23,20,66]
Error

Which of the following is not a core data type in Python?
a) List
b) Tuple
c) Dictionary
d) Class

How would you create a tuple with only one element?

a) my_tuple = (1,)
b) my_tuple = (1)
c) my_tuple = [1]
d) my_tuple = {1}

What is the result of the following code?

x = [1, 2, 3]
y = x
y[1] = 4
print(x)

a) [1, 2, 3]
b) [1, 4, 3]
c) [4, 2, 3]
d) [1, 2, 4]

What is the result of the following code?

x = [1, 2, 3]
y = x
y = [4, 5, 6]

print(x)
a) [1, 2, 3]
b) [4, 5, 6]
c) [1, 4, 5, 6]
d) [4, 5, 6, 1, 2, 3]

How would you add an element to the end of a list in Python?
a) list.append(element)
b) list += element
c) list.push(element)
d) list = list + [element]

#5 What is the result of the following code?

x = {1: 'a', 2: 'b', 3: 'c'}
y = x.copy()
y[1] = 'd'
print(x)

related video: https://youtube.com/shorts/PXp9uzvKFdU?feature=share

a) {1: 'a', 2: 'b', 3: 'c'}
b) {1: 'd', 2: 'b', 3: 'c'}
c) {1: 'd', 2: 'b', 3: 'c', 4: 'd'}
d) {1: 'a', 2: 'b', 3: 'c', 1: 'd'}

How do you create an empty tuple in Python?

related video: https://youtu.be/nGIWcYXj580

a) tuple()
b) {}
c) ()
d) []
Answer: c) ()

How do you create a tuple with multiple elements in Python?
related video: https://youtu.be/QpRiHuQycXg

a) tuple(1, 2, 3)
b) (1, 2, 3)
c) {1, 2, 3}
d) [1, 2, 3]
Answer: b) (1, 2, 3)

What is the correct way to create a tuple with a single element in Python?
related video: https://youtu.be/nGIWcYXj580

a) tuple(1)
b) (1,)
c) {1}
d) [1]
Answer: b) (1,)

How do you add an element to an existing tuple in Python?
a) tuple.append(element)
b) tuple + (element,)
c) tuple.extend(element)
d) Tuples are immutable, so it is not possible to add an element to an existing tuple.
Answer: d) Tuples are immutable, so it is not possible to add an element to an existing tuple.

How do you remove an element from a tuple in Python?
a) tuple.remove(element)
b) tuple.pop(element)
c) Tuples are immutable, so it is not possible to remove an element from a tuple.
d) del tuple[element]
Answer: c) Tuples are immutable, so it is not possible to remove an element from a tuple.


What is the output of this code in PYTHON?
list1=[1,2,3,4,5]
print(list1[:4].pop())

[1,2,3,4]
5
[1,2,3,5]
4

What is the output of this code in PYTHON?
list1=[1,2,34,5]
print(list1[:4].pop())

[1,2,3,4]
5
[1,2,3,5]
4







**Answer key (Mutiple Choice):**

## Fill in the Blanks

**Answer Key (Fill in the Blanks):**

## Exercises

## Review Questions

## References and Bibliography

