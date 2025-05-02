Great! Here's the Find and Fix the Mistakes – Lambda Functions worksheet for beginners, now including:

The mistake code

A brief issue statement

The corrected code


Arranged from easy to hard:


---

Find and Fix the Mistakes – Lambda Functions (Beginner Level)


---

Question 1: Missing Colon

Code with Mistake:

double = lambda x x * 2
print(double(4))

Issue: Missing colon (:) in the lambda definition.

Fixed Code:

double = lambda x: x * 2
print(double(4))


---

Question 2: Missing Argument

Code with Mistake:

add = lambda a, b: a + b
print(add(5))

Issue: The function requires two arguments, but only one is provided.

Fixed Code:

add = lambda a, b: a + b
print(add(5, 3))


---

Question 3: Incorrect Lambda Call

Code with Mistake:

print(lambda x: x + 1(3))

Issue: Missing parentheses around the lambda function to call it.

Fixed Code:

print((lambda x: x + 1)(3))


---

Question 4: Too Many Arguments

Code with Mistake:

is_even = lambda x: x % 2 == 0
print(is_even(4, 2))

Issue: Lambda function expects 1 argument, but 2 are given.

Fixed Code:

is_even = lambda x: x % 2 == 0
print(is_even(4))


---

Question 5: Extra Argument in Call

Code with Mistake:

square = lambda x: x * x
print(square(5, 2))

Issue: Function expects 1 argument, but 2 are passed.

Fixed Code:

square = lambda x: x * x
print(square(5))


---

Question 6: Return Statement in Lambda

Code with Mistake:

add = lambda a, b: return a + b
print(add(3, 4))

Issue: lambda functions cannot use the return statement.

Fixed Code:

add = lambda a, b: a + b
print(add(3, 4))


---

Question 7: Missing Iterable in map()

Code with Mistake:

doubled = map(lambda x: x * 2)
print(list(doubled))

Issue: map() is missing the list to apply the function to.

Fixed Code:

doubled = map(lambda x: x * 2, [1, 2, 3])
print(list(doubled))


---

Question 8: Undefined Variable in If-Else

Code with Mistake:

max = lambda a, b : x if (a > b) else b
print(max(1, 2))

Issue: Uses x which is not defined; should use a.

Fixed Code:

max = lambda a, b: a if a > b else b
print(max(1, 2))


---

Question 9: Invalid If-Else Syntax

Code with Mistake:

max = lambda x, y: if x > y then x else y
print(max(3, 7))

Issue: Incorrect syntax for if-else in lambda expression.

Fixed Code:

max = lambda x, y: x if x > y else y
print(max(3, 7))


---

Would you like this formatted as a PDF worksheet for print, or a slide-friendly version for classroom use?

