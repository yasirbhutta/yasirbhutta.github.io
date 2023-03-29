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
``
#### Unpacking tuples
#### Tuple methods


