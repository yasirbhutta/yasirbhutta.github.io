# IT-401 DATA STRUCTURES & ALGORITHMS 4(3-1)

[Download PDF](dsa-rq.pdf)

## Chapter #2

**Questions**

1. What is Big O notation?

- **Answer:** Big O notation is a mathematical concept used in computer science to describe how the performance of an algorithm changes as the size of the input data grows. It gives you an idea of the worst-case scenario for how long an algorithm will take to run or how much space (memory) it will need.
**Key Concepts:**
  1. **Input Size (n):** This is usually the size of the data you're working with. For example, if you're sorting a list of numbers, "n" would be the number of items in that list.

  2. **Operations:** When we talk about Big O, we're usually counting the number of basic operations an algorithm performs (like comparisons, assignments, etc.).

  3. **Growth Rate:** Big O notation helps us understand how the number of operations grows as the input size increases. This is important because even if an algorithm is fast for small inputs, it might become very slow for large inputs.

2. **List and briefly explain the common Big O notations used to describe the time complexity of algorithms.**

**Common Big O Notations:**

   1. **O(1):** **Constant time**. The algorithm takes the same amount of time, no matter how large the input is. Example: Accessing an element in an array by index.
   
   2. **O(n):** **Linear time**. The time it takes to run the algorithm increases directly in proportion to the size of the input. Example: Looping through all items in a list.
   
   3. **O(log n):** **Logarithmic time**. The algorithm's time grows slower as the input size increases. Example: Binary search in a sorted array.

   4. **O(n log n):** This is common in more efficient sorting algorithms like Merge Sort or Quick Sort.

   5. **O(n²):** **Quadratic time**. The time it takes to run the algorithm is proportional to the square of the input size. Example: Nested loops, like in Bubble Sort.

   6. **O(2^n):** **Exponential time**. The time doubles with each additional element in the input. Example: Recursive algorithms that solve a problem of size "n" by solving smaller sub-problems multiple times.

   7.  **O(n!):** **Factorial time**. The time grows extremely fast with the input size. Example: Generating all permutations of a list.

3.  Why is Big O Important?
    
- **Answer:** Big O notation helps you compare different algorithms and choose the one that will perform better, especially with large data sets. It focuses on the worst-case scenario, ensuring that the algorithm can handle the largest possible input efficiently.

**Example:**

Imagine you have a list of 1000 numbers, and you want to find a specific number.

- If you're using **O(n)** time (linear search), you might have to check each number, so it could take up to 1000 steps.
- If you're using **O(log n)** time (binary search), you could find the number in about 10 steps.

Big O notation helps you predict these differences in performance.

4. **Write a note on the Best Case, Average Case, and Worst Case scenarios of algorithms, including their significance in algorithm analysis.**
   
In algorithm analysis, the best, average, and worst cases describe the different scenarios that can occur depending on the input data. These cases help us understand how an algorithm performs under varying conditions.

1. **Best Case:**
   - **Definition:** The best-case scenario is when the algorithm performs the fewest possible operations. It represents the most favorable input situation where the algorithm completes its task as quickly as possible.
   - **Example:** For a linear search algorithm, the best case occurs when the target element is the first element in the list. The search completes in O(1) time.

2. **Average Case:**
   - **Definition:** The average case represents the expected time complexity for a typical input. It considers the performance of the algorithm over all possible inputs, averaged out.
   - **Example:** In a linear search, the average case assumes that the target element could be anywhere in the list. On average, it will take O(n/2) time, which simplifies to O(n).

3. **Worst Case:**
   - **Definition:** The worst-case scenario occurs when the algorithm takes the most time or operations to complete. It represents the most challenging input situation for the algorithm.
   - **Example:** For the linear search algorithm, the worst case happens when the target element is not in the list at all or is the last element. The search will take O(n) time.

- Why Are These Cases Important?
Understanding the best, average, and worst cases helps developers and computer scientists evaluate the efficiency of an algorithm across different scenarios. This knowledge is crucial for selecting the right algorithm for a given task, ensuring that it performs well under all potential conditions.

5. Find the computational complexity for the following loop:
```cpp
for (cnt1 = 0, i = 1; i <= n; i++)
    for (j = 1; j <= n; j++)
        cnt1++;
```

**Answer:** 

- The outer loop runs from `i = 1` to `i <= n`, so it executes `n` times.
- The inner loop runs from `j = 1` to `j <= n`, so it also executes `n` times for each iteration of the outer loop.

**Total operations:** `n` (outer loop) * `n` (inner loop) = `n^2`

**Complexity:** O(n²)

## Chapter #3

**Questions**

- Define a singly linked list?
- What is Doubly Linked Lists?
- What is Circular Lists?
- 
## Chapter #4

**Questions**

1. What is a stack, and how does it operate in terms of data storage and retrieval? [4.1]
2. Why is a stack called a LIFO (Last In, First Out) structure? Provide an example that illustrates this concept.
3. Explain the difference between the push(el) and pop() operations in a stack.
4. Explain how to add the numbers 592 and 3,784 using stack data structures. Describe each step in detail, including all stack operations performed, and illustrate the state of the stacks at each step of the addition process
5. What is a queue, and how does it differ from a stack?
6. Explain the FIFO (First In, First Out) principle in the context of a queue.
7. How does the enqueue operation differ from the dequeue operation in a queue?
8. What will be the state of the queue after the following operations:
- enqueue(3)
- enqueue(7)
- dequeue()
- enqueue(10)?
9. If a queue initially contains the elements [2, 4, 6], what will the queue look like after one dequeue() and two enqueue(8) operations?
10. What is a priority queue, and how does it differ from a simple queue?
- **Answer:** A priority queue is a type of queue where elements are dequeued based on their priority rather than their order of arrival. Unlike a simple queue that follows the FIFO (First In, First Out) principle, a priority queue serves elements with higher priority first, regardless of their position in the queue.
11. Why might a priority queue be necessary in real-world scenarios?
- **Answer:** Priority queues are necessary when certain tasks, people, or processes need to be prioritized over others. Examples include giving priority to emergency vehicles at tollbooths or ensuring that a critical system process is executed before less important ones, even if it arrives later.
12. What are the two variations of linked lists used to represent priority queues?

## Chapter #5

**Questions**

1. **What is the purpose of recursive definitions in programming?**
   - **Answer:** Recursive definitions in programming are used to define functions that call themselves in order to solve a problem by breaking it down into simpler subproblems.

2. **What is the C++ code for calculating the factorial of a number using recursion?**
   - **Answer:** The C++ code for calculating the factorial of a number using recursion is:
     ```cpp
     unsigned int factorial(unsigned int n) {
         if (n == 0)
             return 1;
         else
             return n * factorial(n - 1);
     }
     ```

3. **What is Recrusive definition?** 
 
- A recursive definition is a method used to define a set or a concept in terms of itself. It typically consists of two main parts:

  1. **Anchor (or Ground Case):** This is the base case or the simplest, most fundamental element of the set. It represents the starting point or foundation of the recursive definition. For example, in the set of natural numbers, the anchor case is `0`. This case defines the initial element that other elements are built upon.

  2. **Recursive Rule:** This part provides the method for constructing new elements from the basic or previously defined elements. It describes how to generate more complex elements by applying certain operations to the elements already defined. In the case of the natural numbers, the recursive rule is: "If \( n \) is a natural number, then \( n + 1 \) is also a natural number." This rule allows for the generation of new numbers by incrementing the existing numbers.

To illustrate this with the example of natural numbers:

- **Anchor Case:** 0 is in the set of natural numbers \( N \). This establishes 0 as the starting point.

- **Recursive Rule:** If \( n \) is a natural number (i.e., \( n \in N \)), then \( n + 1 \) is also a natural number. This rule allows you to generate new numbers by adding 1 to any number that is already in the set.

- **Closure:** There are no other objects in the set \( N \) except those generated by the anchor case and the recursive rule. This means that every element of the set can be derived from the anchor case and the recursive rule, and nothing else is included.

In summary, recursive definitions use a base case to establish the starting point and recursive rules to build upon that base case, generating new elements in a structured manner. This approach is widely used in mathematics, computer science, and other fields to define and work with sets, sequences, and functions.

4. **What is the recursive definition of the factorial function? Provide an example to illustrate how it works.**

The factorial of a non-negative integer \( n \), denoted as \( n! \), is the product of all positive integers less than or equal to \( n \). It is defined recursively as follows:

1. **Anchor (Ground Case):**
   - The simplest case or the base case is defined. For the factorial function, the base case is:
     \[
     0! = 1
     \]
   - This means that the factorial of 0 is 1. This is the starting point for the recursion.

2. **Recursive Rule:**
   - This rule describes how to compute the factorial of a number greater than 0 using the factorial of a smaller number. It is defined as:
     \[
     n! = n x (n - 1)!
     \]
   - In other words, the factorial of \( n \) is \( n \) multiplied by the factorial of \( n - 1 \). This rule allows you to compute the factorial of any number greater than 0 by referring to the factorial of a smaller number.

3. **Closure (Exclusivity):**
   - The set of values that satisfy the recursive definition includes only those numbers generated by applying the anchor case and recursive rule. No other values are part of the set.

### Example of Recursive Definition for Factorials

To compute \( 4! \) using the recursive definition:

1. **Start with the number 4:**
   \[
   4! = 4 x (4 - 1)!
   \]
   \[
   4! = 4 x 3!
   \]

2. **Compute \( 3! \) using the same rule:**
   \[
   3! = 3 x (3 - 1)!
   \]
   \[
   3! = 3 x 2!
   \]

3. **Compute \( 2! \) using the same rule:**
   \[
   2! = 2 x (2 - 1)!
   \]
   \[
   2! = 2 x 1!
   \]

4. **Compute \( 1! \) using the same rule:**
   \[
   1! = 1 x (1 - 1)!
   \]
   \[
   1! = 1 x 0!
   \]

5. **Use the anchor case to determine \( 0! \):**
   \[
   0! = 1
   \]

6. **Substitute back into the previous calculations:**
   \[
   1! = 1 x 0! = 1 x 1 = 1
   \]
   \[
   2! = 2 x 1 = 2
   \]
   \[
   3! = 3 x 2 = 6
   \]
   \[
   4! = 4 x 6 = 24
   \]

Thus, \( 4! = 24 \), which is the result of applying the recursive definition and the base case.

In summary, the recursive definition for the factorial function includes a base case (anchor) that provides the simplest value and a recursive rule that builds upon this value to compute factorials of larger numbers. This approach elegantly captures the essence of the factorial function through a self-referential process.


## Multiple Choice (Select the best answer)

### Chapter 2: Algorithm Analysis and Big O Notation

**1. What does Big O notation represent?**  
- a) The best-case complexity of an algorithm  
- b) The worst-case complexity of an algorithm  
- c) The space complexity of an algorithm  
- d) The best, worst, and average-case complexities of an algorithm  
- **Answer:** b) The worst-case complexity of an algorithm

**2. What is the time complexity of binary search in a sorted array?**  
- a) O(n)  
- b) O(n²)  
- c) O(log n)  
- d) O(1)  
- **Answer:** c) O(log n)

**3. Which of the following is an example of an algorithm with O(1) time complexity?**  
- a) Binary search  
- b) Accessing an element in an array by index  
- c) Insertion sort  
- d) Merging two sorted lists  
- **Answer:** b) Accessing an element in an array by index

**4. If an algorithm has a time complexity of O(n²), what does this mean?**  
- a) The algorithm's performance doubles when the input size doubles  
- b) The algorithm performs at the same speed regardless of input size  
- c) The algorithm's time grows proportional to the square of the input size  
- d) The algorithm's performance decreases as input size increases  
- **Answer:** c) The algorithm's time grows proportional to the square of the input size

**5. Which of the following sorting algorithms has a time complexity of O(n log n) in the average case?**  
- a) Bubble Sort  
- b) Quick Sort  
- c) Insertion Sort  
- d) Selection Sort  
- **Answer:** b) Quick Sort

**6. Which scenario describes the worst-case time complexity of a linear search?**  
- a) The target element is the first in the list  
- b) The target element is the last in the list  
- c) The target element is somewhere in the middle of the list  
- d) The list is empty  
- **Answer:** b) The target element is the last in the list

**7. What is the best-case time complexity of the bubble sort algorithm?**  
- a) O(n²)  
- b) O(n log n)  
- c) O(n)  
- d) O(log n)  
- **Answer:** c) O(n)

**8. What is the growth rate of an algorithm with time complexity O(2^n)?**  
- a) Exponential  
- b) Linear  
- c) Logarithmic  
- d) Constant  
- **Answer:** a) Exponential

### Chapter 3: Linked Lists

**9. What is a singly linked list?**  
- a) A list where each node points to the previous node  
- b) A list where each node points to both the next and previous node  
- c) A list where each node points only to the next node  
- d) A circular list with no start and end  
- **Answer:** c) A list where each node points only to the next node

**10. What is a doubly linked list?**  
- a) A list where each node points to the previous node  
- b) A list where each node points to both the next and previous node  
- c) A list where each node points only to the next node  
- d) A list that ends where it starts  
- **Answer:** b) A list where each node points to both the next and previous node

**11. What distinguishes a circular linked list from a singly linked list?**  
- a) The nodes form a loop, connecting the last node to the first  
- b) It allows bidirectional traversal  
- c) It has a head and tail node  
- d) It has a node pointing to multiple nodes  
- **Answer:** a) The nodes form a loop, connecting the last node to the first

### Chapter 4: Stacks and Queues

**12. Why is a stack called a LIFO structure?**  
- a) The first element added is the first element removed  
- b) The last element added is the first element removed  
- c) The elements are removed in random order  
- d) The stack remains unchanged until it's full  
- **Answer:** b) The last element added is the first element removed

**13. What does the pop() operation do in a stack?**  
- a) Inserts an element at the top  
- b) Removes the bottom element  
- c) Removes the top element  
- d) Retrieves an element without removing it  
- **Answer:** c) Removes the top element

**14. Which of the following represents a queue?**  
- a) LIFO structure  
- b) Priority-based order  
- c) Circular structure  
- d) FIFO structure  
- **Answer:** d) FIFO structure

**15. What operation would remove the front element of a queue?**  
- a) Enqueue  
- b) Dequeue  
- c) Pop  
- d) Push  
- **Answer:** b) Dequeue

**16. In a queue, after the operations enqueue(3), enqueue(7), dequeue(), and enqueue(10), what will be at the front?**  
- a) 7  
- b) 10  
- c) 3  
- d) None  
- **Answer:** a) 7

**17. What is a priority queue?**  
- a) A queue where elements are dequeued in random order  
- b) A queue where elements are dequeued based on priority  
- c) A queue where elements are processed in LIFO order  
- d) A queue where elements are dequeued in the order they are enqueued  
- **Answer:** b) A queue where elements are dequeued based on priority

### Chapter 5: Recursion

**18. What is a recursive function?**  
- a) A function that calls itself to solve subproblems  
- b) A function that only solves one problem  
- c) A function that terminates immediately  
- d) A function that uses iteration  
- **Answer:** a) A function that calls itself to solve subproblems

**19. What is the base case in recursion?**  
- a) The condition that causes the recursion to continue indefinitely  
- b) The condition that stops the recursion  
- c) The recursive call within the function  
- d) The first call made by the recursive function  
- **Answer:** b) The condition that stops the recursion

**20. Which of the following code snippets represents a factorial function using recursion in C++?**  
- a)  
```cpp
unsigned int factorial(unsigned int n) {
    if (n == 0) return 1;
    else return n * factorial(n - 1);
}
```  
- b)  
```cpp
unsigned int factorial(unsigned int n) {
    return n * factorial(n + 1);
}
```  
- c)  
```cpp
unsigned int factorial(unsigned int n) {
    while (n > 0) return n * factorial(n - 1);
}
```  
- d)  
```cpp
unsigned int factorial(unsigned int n) {
    return n;
}
```  
- **Answer:** a) 

### Chapter 2: Algorithm Analysis and Big O Notation

**21. Which of the following is NOT a characteristic of Big O notation?**  
- a) Describes the worst-case scenario  
- b) Measures an algorithm's efficiency  
- c) Focuses on both time and space complexity  
- d) Guarantees constant time for every algorithm  
- **Answer:** d) Guarantees constant time for every algorithm

**22. What is the time complexity of an algorithm that splits the input data in half each time it runs?**  
- a) O(n²)  
- b) O(n)  
- c) O(log n)  
- d) O(n log n)  
- **Answer:** c) O(log n)

**25. What is the primary goal of algorithm analysis?**  
- a) To determine the most complicated algorithm  
- b) To ensure that the algorithm uses the least possible memory  
- c) To evaluate the performance in terms of time and space complexity  
- d) To guarantee that an algorithm solves a problem correctly  
- **Answer:** c) To evaluate the performance in terms of time and space complexity

**26. The computational complexity of the following code snippet is:**
```cpp
for (int i = 0; i < n; i++)
    for (int j = 0; j < n; j++)
        cout << i * j;
```  
- a) O(n)  
- b) O(log n)  
- c) O(n²)  
- d) O(1)  
- **Answer:** c) O(n²)

**27. Which of the following time complexities represents the most efficient algorithm for large input sizes?**  
- a) O(n log n)  
- b) O(n²)  
- c) O(n!)  
- d) O(2^n)  
- **Answer:** a) O(n log n)

**28. Which Big O notation is used to describe an algorithm whose time complexity grows exponentially with input size?**  
- a) O(1)  
- b) O(n!)  
- c) O(2^n)  
- d) O(n)  
- **Answer:** c) O(2^n)

**30. What is the purpose of Big O notation in algorithm analysis?**  
- a) To measure the accuracy of an algorithm  
- b) To determine the correctness of an algorithm  
- c) To predict the scalability of an algorithm with increasing input sizes  
- d) To evaluate the complexity of an algorithm for small inputs  
- **Answer:** c) To predict the scalability of an algorithm with increasing input sizes

### Chapter 3: Linked Lists

**31. What is the key difference between a singly linked list and a doubly linked list?**  
- a) Singly linked lists can store only integers  
- b) Singly linked lists have a tail node, but doubly linked lists do not  
- c) Singly linked lists store data only in one direction, while doubly linked lists store data in both directions  
- d) Singly linked lists use more memory than doubly linked lists  
- **Answer:** c) Singly linked lists store data only in one direction, while doubly linked lists store data in both directions

**32. Which of the following is a major advantage of linked lists over arrays?**  
- a) Faster access to elements  
- b) Faster sorting  
- c) Dynamic memory allocation  
- d) Ability to store floating-point numbers  
- **Answer:** c) Dynamic memory allocation

**33. What is the time complexity of inserting an element at the beginning of a singly linked list?**  
- a) O(1)  
- b) O(n)  
- c) O(n²)  
- d) O(log n)  
- **Answer:** a) O(1)

**34. Which of the following data structures is commonly implemented using linked lists?**  
- a) Hash table  
- b) Stack  
- c) Binary search tree  
- d) Array  
- **Answer:** b) Stack

**35. Which of the following operations has a time complexity of O(n) in a singly linked list?**  
- a) Accessing the first element  
- b) Inserting at the beginning  
- c) Accessing the last element  
- d) Inserting at the end  
- **Answer:** c) Accessing the last element

### Chapter 4: Stacks and Queues

**36. Which of the following operations is specific to a stack?**  
- a) Enqueue  
- b) Pop  
- c) Dequeue  
- d) Front  
- **Answer:** b) Pop

**37. How does a stack differ from a queue?**  
- a) A stack follows the FIFO principle, while a queue follows LIFO  
- b) A stack follows the LIFO principle, while a queue follows FIFO  
- c) A stack is linear, while a queue is circular  
- d) Both stack and queue follow the same principle  
- **Answer:** b) A stack follows the LIFO principle, while a queue follows FIFO

**38. What is the result of the following operations on a stack: push(1), push(2), pop(), push(3), pop()?**  
- a) 2  
- b) 3  
- c) 1  
- d) Empty stack  
- **Answer:** c) 1

**39. What is the result of the following operations on a stack: push(5), push(7), pop(), push(9), pop(), pop()?**  
- a) 9  
- b) 5  
- c) 7  
- d) Empty stack  
- **Answer:** b) 5

---

**40. After the following sequence of stack operations, what is the element at the top of the stack? Operations: push(10), push(20), pop(), push(30), push(40), pop()?**  
- a) 20  
- b) 40  
- c) 30  
- d) Empty stack  
- **Answer:** c) 30

---

**3. Consider the stack operations: push(4), push(8), pop(), push(12), push(15), pop(), pop(). What is the top element of the stack now?**  
- a) 12  
- b) 8  
- c) 4  
- d) Empty stack  
- **Answer:** c) 4

---

**4. What is the output of the following stack operations: push(2), push(4), push(6), pop(), pop(), pop()?**  
- a) 6  
- b) 4  
- c) 2  
- d) Empty stack  
- **Answer:** d) Empty stack

**5. What is the result of the following operations on a queue: enqueue(2), enqueue(4), dequeue(), enqueue(6), dequeue()?**  
- a) 2  
- b) 4  
- c) 6  
- d) Empty queue  
- **Answer:** c) 6


**6. After the operations enqueue(5), enqueue(9), dequeue(), enqueue(11), dequeue(), enqueue(13), dequeue(), what element will be at the front of the queue?**  
- a) 5  
- b) 9  
- c) 13  
- d) Empty queue  
- **Answer:** c) 13

**7. What will be the state of the queue after the following operations: enqueue(1), enqueue(3), dequeue(), enqueue(5), enqueue(7), dequeue()?**  
- a) [5, 7]  
- b) [3, 5]  
- c) [5]  
- d) Empty queue  
- **Answer:** a) [5, 7]

**8. In a circular queue with a capacity of 3, what happens after the following operations: enqueue(1), enqueue(2), enqueue(3), dequeue(), enqueue(4)?**  
- a) Queue is full  
- b) [2, 3, 4]  
- c) [1, 4, 3]  
- d) Empty queue  
- **Answer:** b) [2, 3, 4]

**9. What is the time complexity of the following loop?**
```cpp
for (int i = 1; i <= n; i *= 2) {
    // do something
}
```  
- a) O(n)  
- b) O(log n)  
- c) O(n²)  
- d) O(1)  
- **Answer:** b) O(log n)

**40. Which of the following is true about a priority queue?**  
- a) Elements are processed based on their order of insertion  
- b) Elements are processed based on their priority  
- c) Elements are processed in LIFO order  
- d) Elements are processed randomly  
- **Answer:** b) Elements are processed based on their priority

## Fill in the Blanks

### Chapter 2: Algorithm Analysis and Big O Notation

1. Big O notation describes the __________ of an algorithm in terms of time or space complexity.
2. The time complexity of binary search is __________.
3. The __________ case describes the scenario where an algorithm performs the maximum number of operations.
4. For an algorithm with O(n²) complexity, the performance __________ as the input size increases.
5. The __________ complexity of an algorithm measures the amount of memory used by the algorithm.
6. A loop that runs a constant number of times has a time complexity of __________.
7. The time complexity of merge sort is __________.
8. An algorithm that solves smaller subproblems and then combines them is an example of __________.
9. The time complexity of an algorithm that checks every element in a list sequentially is __________.
10. In Big O notation, the base of the logarithm is typically assumed to be __________.

---

### Chapter 3: Linked Lists

11. A singly linked list stores data in __________ direction(s).
12. In a __________ linked list, each node has pointers to both the next and previous nodes.
13. The time complexity for inserting an element at the beginning of a singly linked list is __________.
14. The __________ node of a linked list does not point to any other node.
15. A circular linked list has its last node pointing to the __________.
16. In a doubly linked list, each node contains data and __________ pointers.
17. To delete a node in a singly linked list, you need to modify the __________ pointer of the previous node.
18. __________ linked lists allow traversal in both directions.
19. The time complexity of searching for an element in a linked list is typically __________.
20. The structure where the first node in the list is called the __________ node.

---

### Chapter 4: Stacks and Queues

21. A stack follows the __________ principle for data management.
22. The operation of adding an element to a stack is called __________.
23. In a stack, the element that is removed last was __________ first.
24. The operation used to remove an element from a queue is called __________.
25. A queue follows the __________ principle.
26. In a priority queue, elements are dequeued based on their __________.
27. The function used to add an element to the rear of a queue is called __________.
28. The time complexity of both enqueue and dequeue operations in a simple queue is __________.
29. The __________ operation is used to check the top element of a stack without removing it.
30. In a circular queue, the front pointer moves in a __________ manner when an element is dequeued.

---

### Chapter 5: Recursion

31. A function that calls itself during its execution is said to be __________.
32. The base case in a recursive function prevents the function from entering an __________ loop.
33. The factorial function can be defined using __________.
34. The __________ case of a recursive function provides a solution without making further recursive calls.
35. When the recursive call is made with a smaller value of the input, the recursion is said to __________.
36. Every recursive function must have a base case to avoid __________.
37. A recursive function to compute the Fibonacci sequence calls itself __________ times for each non-base case.
38. In recursion, each function call is added to the __________, which is used to keep track of the function calls.
39. If a recursive function has no base case, it will lead to a __________.
40. The factorial of 5 (5!) is calculated recursively as 5 * __________.


### Chapter 2: Algorithm Analysis and Big O Notation

1. **performance**
2. **O(log n)**
3. **worst**
4. **increases**
5. **space**
6. **O(1)**
7. **O(n log n)**
8. **divide and conquer**
9. **O(n)**
10. **2**

---

### Chapter 3: Linked Lists

11. **one**
12. **doubly**
13. **O(1)**
14. **last**
15. **first node**
16. **two**
17. **next**
18. **Doubly**
19. **O(n)**
20. **head**

---

### Chapter 4: Stacks and Queues

21. **LIFO (Last In, First Out)**
22. **push**
23. **added**
24. **dequeue**
25. **FIFO (First In, First Out)**
26. **priority**
27. **enqueue**
28. **O(1)**
29. **peek**
30. **circular**

---

### Chapter 5: Recursion

31. **recursive**
32. **infinite**
33. **recursion**
34. **base**
35. **reduce**
36. **infinite recursion**
37. **two**
38. **call stack**
39. **stack overflow**
40. **4! (24)**

## True/false

### Chapter 2: Algorithm Analysis and Big O Notation

1. **True or False:** Big O notation measures the worst-case time complexity of an algorithm.  
   **Answer:** True

2. **True or False:** O(n²) time complexity is better than O(n log n) for large input sizes.  
   **Answer:** False

3. **True or False:** The time complexity of accessing an element in an array by index is O(1).  
   **Answer:** True

4. **True or False:** Big O notation is used to measure the space complexity of algorithms as well.  
   **Answer:** True

5. **True or False:** An algorithm with O(2^n) time complexity is considered efficient for large inputs.  
   **Answer:** False

6. **True or False:** The average case time complexity of an algorithm is always the same as the worst case.  
   **Answer:** False

7. **True or False:** O(log n) grows slower than O(n) as the input size increases.  
   **Answer:** True

8. **True or False:** Constant time algorithms are always faster than linear time algorithms for all input sizes.  
   **Answer:** False

9. **True or False:** Best case time complexity is more important than worst case when analyzing algorithms.  
   **Answer:** False

10. **True or False:** Recursive algorithms are always less efficient than their iterative counterparts.  
    **Answer:** False

---

### Chapter 3: Linked Lists

11. **True or False:** A singly linked list allows traversal in both directions.  
    **Answer:** False

12. **True or False:** In a circular linked list, the last node points to the first node in the list.  
    **Answer:** True

13. **True or False:** The time complexity for inserting an element at the end of a singly linked list is O(1).  
    **Answer:** False

14. **True or False:** A doubly linked list has pointers to both the next and previous nodes.  
    **Answer:** True

15. **True or False:** The head node of a linked list always points to the first element in the list.  
    **Answer:** True

16. **True or False:** Circular linked lists are often used in applications that require continuous looping through elements.  
    **Answer:** True

17. **True or False:** A linked list requires more memory than an array due to storing additional pointer information.  
    **Answer:** True

18. **True or False:** In a singly linked list, deleting a node requires updating the next pointer of the previous node.  
    **Answer:** True

19. **True or False:** A linked list cannot be resized dynamically.  
    **Answer:** False

20. **True or False:** The time complexity of searching for an element in a linked list is O(log n).  
    **Answer:** False


### Chapter 4: Stacks and Queues

21. **True or False:** A stack follows the LIFO principle, where the last element added is the first one removed.  
    **Answer:** True

22. **True or False:** In a queue, the dequeue operation removes the element from the rear of the queue.  
    **Answer:** False

23. **True or False:** A priority queue is a type of queue where elements are dequeued based on their priority.  
    **Answer:** True

24. **True or False:** Enqueuing an element to a queue has a time complexity of O(n).  
    **Answer:** False

25. **True or False:** Stacks are commonly used in recursive function calls due to their LIFO structure.  
    **Answer:** True

26. **True or False:** In a circular queue, the rear pointer moves circularly when elements are enqueued.  
    **Answer:** True

27. **True or False:** A stack's pop operation removes the top element from the stack.  
    **Answer:** True

28. **True or False:** Queues operate based on the LIFO principle, just like stacks.  
    **Answer:** False

29. **True or False:** The peek operation in a stack returns the top element without removing it.  
    **Answer:** True

30. **True or False:** Stacks and queues both follow the same ordering principles for insertion and removal.  
    **Answer:** False


## Practical Tasks


### Chapter 5:

1. **What is the C++ code for calculating the factorial of a number using recursion?**
   
   - **Answer:** The C++ code for calculating the factorial of a number using recursion is:
     ```cpp
     unsigned int factorial(unsigned int n) {
         if (n == 0)
             return 1;
         else
             return n * factorial(n - 1);
     }
     ```

## Final Term Contents

### Review Question

1. **What is the insertion sort algorithm, and how does it work? Demonstrate with an example.**

**Answer:**  
Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time. It works similarly to the way you sort playing cards in your hands.

- Start with the second element, compare it with elements to its left and insert it in the correct position. Repeat this process for all elements.

**Example:**
Consider sorting the array `[3, 1, 4, 1, 5]` using insertion sort:
1. **Start with the second element (1)**: Compare it with the first element (3). Since 1 is smaller, insert it before 3. Array becomes: `[1, 3, 4, 1, 5]`.
2. **Move to the third element (4)**: 4 is larger than 3, so it stays in place. Array remains: `[1, 3, 4, 1, 5]`.
3. **Move to the fourth element (1)**: Compare it with 4 and 3, and insert it at the correct position. Array becomes: `[1, 1, 3, 4, 5]`.
4. **Move to the fifth element (5)**: 5 is larger than 4, so it stays in place. Final array: `[1, 1, 3, 4, 5]`.


2. **Explain the merge sort algorithm and its key steps.**

**Answer:**  
Merge sort is a divide-and-conquer algorithm that divides the array into two halves, recursively sorts each half, and then merges the two sorted halves.

Key steps:
1. **Divide:** Split the array into two halves.
2. **Conquer:** Recursively sort the two halves.
3. **Combine:** Merge the two sorted halves to produce the final sorted array.

Merge sort has a time complexity of O(n log n), which is better for larger datasets compared to simpler algorithms like insertion sort.

**Example:**
To sort the array `[3, 1, 4, 1, 5]`:
- Split into `[3, 1, 4]` and `[1, 5]`
- Recursively sort: `[1, 3, 4]` and `[1, 5]`
- Merge to get `[1, 1, 3, 4, 5]`

  
3. **Describe the quick sort algorithm. How does it work?**

**Answer:**  
Quick sort is another divide-and-conquer algorithm that works by selecting a "pivot" element and partitioning the array so that elements smaller than the pivot are on the left, and elements larger than the pivot are on the right. The process is then repeated recursively on the left and right partitions.

Steps:
1. **Select a pivot** (usually the first or last element).
2. **Partition:** Rearrange elements so that those less than the pivot are on one side and those greater than the pivot are on the other.
3. **Recursion:** Apply quick sort on the left and right partitions.

Quick sort generally performs well with O(n log n) time complexity, although its worst-case is O(n^2), depending on how the pivot is chosen.

**Example:**
To sort `[3, 1, 4, 1, 5]`:
- Choose 5 as the pivot. Partition the array into `[3, 1, 4, 1] | [5]`.
- Recursively sort `[3, 1, 4, 1]`. Choose 1 as the pivot. Partition into `[1] | [3, 4, 1]`.
- Recursively sort `[3, 4, 1]`. Choose 1 as the pivot. Partition into `[1] | [3, 4]`.
- Combine and get `[1, 1, 3, 4, 5]`.


4. **Explain how the selection sort algorithm works.**

**Answer:**  
Selection sort works by repeatedly finding the minimum element from the unsorted portion of the array and swapping it with the first unsorted element. This continues until the entire array is sorted.

Steps:
1. **Find the minimum element** in the unsorted array.
2. Swap it with the element at the beginning of the unsorted portion.
3. Move the boundary between sorted and unsorted parts one element to the right.
4. Repeat the process until the array is sorted.

**Example:**
Sorting `[3, 1, 4, 1, 5]` using selection sort:
1. Find the minimum (1) and swap with the first element: `[1, 3, 4, 1, 5]`.
2. Find the next minimum (1) and swap with the second element: `[1, 1, 4, 3, 5]`.
3. Find the next minimum (3) and swap with the third element: `[1, 1, 3, 4, 5]`.
4. The array is now sorted.


5. **What is a Binary Search Tree (BST) and How Does it Work? Explain with an Example.**

**Answer:**  
A **Binary Search Tree (BST)** is a type of binary tree where each node has at most two children (left and right), and it maintains the following properties:

1. **Left Subtree Rule:** All nodes in the left subtree of a node have values **less than** the node’s value.
2. **Right Subtree Rule:** All nodes in the right subtree of a node have values **greater than** the node’s value.
3. **No Duplicate Values:** In a typical BST, no two nodes have the same value (some variations may allow duplicates).

BSTs provide efficient searching, insertion, and deletion operations with average time complexity of O(log n) for balanced trees. This is because the tree structure allows you to skip half the nodes at each step, similar to binary search.

### **Example:**
Let’s say we insert the following values into a BST: `8, 3, 10, 1, 6, 14, 4, 7, 13`.

**Step-by-Step Insertion:**
1. Start with the root node: **8**
2. Insert **3**: Since 3 < 8, it goes to the left of 8.
3. Insert **10**: Since 10 > 8, it goes to the right of 8.
4. Insert **1**: Since 1 < 8 and 1 < 3, it goes to the left of 3.
5. Insert **6**: Since 6 < 8 but 6 > 3, it goes to the right of 3.
6. Insert **14**: Since 14 > 8 and 14 > 10, it goes to the right of 10.
7. Insert **4**: Since 4 < 8 and 4 > 3 but 4 < 6, it goes to the left of 6.
8. Insert **7**: Since 7 < 8 and 7 > 3 but 7 > 6, it goes to the right of 6.
9. Insert **13**: Since 13 < 14 but 13 > 10, it goes to the left of 14.

This will result in the following BST structure:

```
         8
       /   \
     3     10
    /  \      \
   1    6     14
       /  \   /
      4    7 13
```

### **Operations on BST:**
1. **Search:** To search for a value, compare it to the root and decide whether to move left or right, continuing until the value is found or a leaf node is reached.
2. **Insert:** Similar to search, but once the correct location is found (where the left or right pointer is `null`), the value is inserted.
3. **Delete:** Deletion is more complex, as it depends on whether the node is a leaf, has one child, or two children. If it has two children, the node’s value is usually replaced with the in-order predecessor (the largest value in the left subtree) or the in-order successor (the smallest value in the right subtree).

### **What is Breadth-First Traversal (BFS)? Explain with an Example.**

**Answer:**  
**Breadth-First Traversal (BFS)** is a tree/graph traversal algorithm that explores all the nodes at the present depth level before moving on to nodes at the next depth level. BFS uses a **queue** to keep track of the nodes to be visited next.

### **How it Works:**
1. Start from the root (or any starting node in a graph).
2. Visit the node and add all its adjacent nodes (children for trees) to a queue.
3. Dequeue the first node from the queue, visit it, and enqueue its unvisited adjacent nodes.
4. Repeat this process until all nodes have been visited.

BFS is particularly useful for finding the shortest path in an unweighted graph.

### **Example:**
Consider the following binary tree:

```
         1
       /   \
      2     3
     / \   / \
    4   5 6   7
```

**BFS Traversal:**
1. Start at the root: `1`.
2. Enqueue its children: `2, 3`.
3. Visit `2`, enqueue its children: `4, 5`.
4. Visit `3`, enqueue its children: `6, 7`.
5. Continue visiting in this order: `4, 5, 6, 7`.

**BFS Order:** `1, 2, 3, 4, 5, 6, 7`.

### **What is Depth-First Traversal (DFS)? Explain with an Example.**

**Answer:**  
**Depth-First Traversal (DFS)** is a tree/graph traversal algorithm that explores as far as possible along a branch before backtracking. DFS uses a **stack** (either implicitly with recursion or explicitly) to track the nodes to be visited.

### **How it Works:**
1. Start from the root (or any starting node in a graph).
2. Visit the node and push its children (or adjacent nodes) onto the stack.
3. Continue visiting the top node on the stack, pushing its children onto the stack, until you can no longer go deeper.
4. Backtrack by popping nodes from the stack and continue exploring new paths.
5. Repeat this process until all nodes have been visited.

DFS is useful for exploring all possible paths in a graph, detecting cycles, and solving maze-like problems.

### **Example:**
Using the same binary tree as before:

```
         1
       /   \
      2     3
     / \   / \
    4   5 6   7
```

**DFS Traversal (Pre-order):**
1. Start at the root: `1`.
2. Visit the left child: `2`.
3. Visit the left child of `2`: `4` (no further children, backtrack).
4. Visit the right child of `2`: `5` (no further children, backtrack to `1`).
5. Visit the right child of `1`: `3`.
6. Visit the left child of `3`: `6` (no further children, backtrack).
7. Visit the right child of `3`: `7` (no further children).

**DFS Order (Pre-order):** `1, 2, 4, 5, 3, 6, 7`.

DFS can also be performed in **in-order** or **post-order** traversal depending on when you visit the node compared to its children.


**Question:**  
What is a heap, and what are its key properties?

**Answer:**  
A **heap** is a specialized tree-based data structure that satisfies the **heap property**. Heaps are commonly used to implement priority queues.

There are two main types of heaps:
1. **Max-Heap:** In a max-heap, for every node `i`, the value of `i` is greater than or equal to the values of its children. The maximum value is always at the root.
2. **Min-Heap:** In a min-heap, for every node `i`, the value of `i` is less than or equal to the values of its children. The minimum value is always at the root.

### **Key Properties:**
- **Complete Binary Tree:** Heaps are complete binary trees, meaning all levels are fully filled except possibly for the last level, which is filled from left to right.
- **Heap Property:** The value at any parent node is either greater than or equal to (max-heap) or less than or equal to (min-heap) the values of its children.

**Example:**
A min-heap with elements `[2, 3, 4, 7, 6, 5, 8]` would look like:

```
         2
       /   \
      3     4
     / \   / \
    7   6 5   8
```

### **What are the Primary Operations of a Heap?**

**Answer:**  
The primary operations of a heap are:
1. **Insert:** Insert a new element into the heap while maintaining the heap property.
   - **How it works:** Add the new element at the next available position (to keep the tree complete) and "heapify up" by comparing the new element with its parent, swapping them if necessary. Continue this process until the heap property is restored.

2. **Delete/Extract (usually the root):** Remove the root element (which is the max for a max-heap or min for a min-heap).
   - **How it works:** Replace the root with the last element in the heap and then "heapify down" by comparing it with its children, swapping it with the smaller child in a min-heap (or larger in a max-heap) until the heap property is restored.

3. **Peek/Get Minimum/Maximum:** Retrieve the minimum or maximum element (the root) without removing it.

### **Example:**
For a max-heap `[20, 18, 15, 13, 14, 10, 8]`, inserting `22` would involve:
- Add `22` as a leaf.
- "Heapify up" by comparing with its parent `15` and swapping, then comparing with `20` and swapping again. The final heap would be `[22, 20, 15, 18, 14, 10, 8, 13]`.

### **How is a Heap Implemented Using an Array?**

**Answer:**  
A heap can be efficiently implemented using an **array** (or list), without needing explicit pointers for parent and child nodes, due to its complete binary tree structure.

### **Mapping Between Array Indices and Heap Nodes:**
- For a node at index `i`:
  - **Parent:** Located at index `(i - 1) // 2`.
  - **Left Child:** Located at index `2 * i + 1`.
  - **Right Child:** Located at index `2 * i + 2`.

### **Example:**
Consider a max-heap represented by the array `[22, 20, 15, 18, 14, 10, 8, 13]`.

- The element at index `0` (value `22`) is the root.
- The element at index `1` (value `20`) is the left child of the root, and the element at index `2` (value `15`) is the right child.
- The parent of the element at index `3` (value `18`) is the element at index `1` (value `20`).

This array-based implementation allows efficient access and manipulation of heap properties in O(log n) time.


### **What is Heap Sort, and How Does it Work?**

**Answer:**  
**Heap Sort** is a comparison-based sorting algorithm that uses a heap to sort an array. It works by first building a max-heap (for ascending order) and then repeatedly extracting the maximum element from the heap and placing it at the end of the array.

### **Steps:**
1. **Build a Max-Heap:** Convert the unsorted array into a max-heap. This is done by heapifying all elements starting from the last non-leaf node up to the root.
2. **Extract the Maximum:** Swap the root (the largest element) with the last element in the array and reduce the heap size by one.
3. **Heapify:** Restore the heap property by heapifying down from the root.
4. **Repeat:** Continue extracting the maximum and heapifying until all elements are sorted.

### **Example:**
To sort the array `[4, 10, 3, 5, 1]` using heap sort:
1. Build a max-heap: `[10, 5, 3, 4, 1]`.
2. Swap `10` with `1`, yielding `[1, 5, 3, 4, 10]`, and heapify the reduced heap `[1, 5, 3, 4]` to get `[5, 4, 3, 1, 10]`.
3. Swap `5` with `1`, yielding `[1, 4, 3, 5, 10]`, and heapify the reduced heap `[1, 4, 3]` to get `[4, 1, 3, 5, 10]`.
4. Continue until the array is sorted: `[1, 3, 4, 5, 10]`.

Heap sort has a time complexity of O(n log n) and is an in-place sorting algorithm but is not stable.

**Question:**  
What is memory management, and why is it important in computer systems?

**Answer:**  
**Memory Management** refers to the process of controlling and coordinating computer memory, assigning blocks of memory to various running programs to optimize performance, and ensuring efficient use of available memory.

### **Key Responsibilities of Memory Management:**
1. **Allocation:** Assigning memory blocks to processes when requested.
2. **Deallocation:** Reclaiming memory when it is no longer needed by the process.
3. **Tracking:** Keeping track of which parts of memory are in use and which are free.
4. **Protection:** Ensuring that processes cannot access memory assigned to other processes (memory isolation).

Memory management is critical for preventing memory leaks, ensuring that multiple programs run smoothly without interfering with one another, and maintaining overall system stability and performance.

**Question:**  
What is garbage collection, and how does it work in memory management?

**Answer:**  
**Garbage Collection (GC)** is an automatic memory management process that identifies and frees up memory that is no longer in use by the program. This helps prevent memory leaks and optimizes the use of memory resources.

### **How Garbage Collection Works:**
1. **Automatic Identification:** The garbage collector automatically identifies objects or memory spaces that are no longer referenced or used by the program.
2. **Reclaiming Memory:** The identified memory is reclaimed so it can be reused by the program or system.
3. **Running in Background:** GC runs in the background and triggers at specific times to ensure efficient memory usage without disrupting the main program execution.

Garbage collection is widely used in languages like Java, Python, and C#, where memory management is handled automatically by the runtime environment, freeing developers from manually managing memory.

**Question:**  
Explain the difference between static memory allocation and dynamic memory allocation.

**Answer:**  
Memory can be allocated in two primary ways:

1. **Static Memory Allocation:**
   - Memory is allocated at **compile-time**.
   - The size and location of the memory block are determined before the program starts running.
   - Variables like global variables, constants, and static variables use static memory allocation.
   - Once allocated, the memory cannot be resized or reallocated during runtime.
   - Example: In C, an array declared with a fixed size, like `int arr[100];`, is statically allocated.

2. **Dynamic Memory Allocation:**
   - Memory is allocated at **run-time**.
   - The size of the memory block can be determined during the program's execution, and the memory can be resized or freed as needed.
   - Functions like `malloc()`, `calloc()`, and `free()` in C, or the `new` keyword in C++ and Java, are used for dynamic memory allocation.
   - Example: In C, using `int* arr = malloc(100 * sizeof(int));` dynamically allocates memory for an array of 100 integers.

Static memory allocation is more predictable and faster, but dynamic memory allocation provides greater flexibility, especially for handling variable amounts of data.

### **What are Memory Leaks, and How Can They Be Prevented?**

**Answer:**  
A **memory leak** occurs when a program fails to release memory that is no longer in use, causing the system to run out of memory over time. This often happens when dynamic memory is allocated but never deallocated.

### **Strategies to Prevent Memory Leaks:**
1. **Manual Memory Management:** In languages like C and C++, always pair memory allocation (`malloc()` or `new`) with corresponding deallocation (`free()` or `delete`) when the memory is no longer needed.
2. **Garbage Collection:** Use languages with built-in garbage collectors (like Java or Python) to automatically manage memory and reduce the risk of memory leaks.
3. **Avoid Circular References:** In languages using reference counting, ensure that objects don't hold circular references, or use weak references to break such cycles.
4. **Smart Pointers:** In C++, use smart pointers like `std::unique_ptr` or `std::shared_ptr` to automatically manage memory and prevent leaks when objects go out of scope.
5. **Testing Tools:** Use memory profiling and analysis tools like Valgrind, Purify, or LeakSanitizer to detect and fix memory leaks during development.

By ensuring proper memory allocation and deallocation practices, memory leaks can be effectively minimized.


### **What is Hashing in Data Structures?**

**Question:**  
What is hashing, and how is it used in data structures?

**Answer:**  
**Hashing** is a technique used to map data to a fixed-size integer (called a **hash value** or **hash code**) using a **hash function**. This hash value is typically used as an index in an array (called a **hash table**) to store or retrieve data efficiently.

### **How it Works:**
1. A **hash function** takes input (such as a string or number) and returns a fixed-size integer.
2. This integer is used as an index in a **hash table** where the data is stored.
3. When retrieving the data, the same hash function is applied to compute the index, and the data can be accessed in **constant time** (O(1)).

### **Example:**
Consider a hash table with a size of 10, and the hash function `hash(x) = x % 10`. To store the value `25`, the hash function will compute `25 % 10 = 5`. The value `25` will be stored in the array at index `5`.

Hashing is commonly used in data structures like **hash maps**, **dictionaries**, and **sets** to provide efficient insertion, deletion, and lookup operations.

### **What is Indexing in Data Structures?**

**Answer:**  
**Indexing** refers to creating a data structure that improves the speed of data retrieval operations by efficiently mapping keys to their locations in a data collection. Indexes act as a guide or reference to quickly locate and access data in large datasets without having to scan through every record.

### **Types of Indexing:**
1. **Primary Indexing:**  
   The index is created on the **primary key** of a dataset (e.g., a unique identifier like a database's `id` field). The index directly maps to the storage location of the data.
   
2. **Secondary Indexing:**  
   Indexing is performed on **non-primary attributes**, such as names or other fields, to provide quick access based on these attributes.
   
3. **Multi-level Indexing:**  
   When the size of the index becomes too large to fit into memory, multi-level indexing is used. Indexes are structured in a hierarchical fashion (like B-trees) to allow faster access.

### **Importance of Indexing:**
Indexing dramatically speeds up search operations by reducing the time complexity of searches from O(n) to O(log n) or even O(1) in certain scenarios. Indexing is widely used in databases, file systems, and search engines to improve performance.

### **How Does Hashing Differ from Indexing?**

**Answer:**  
**Hashing** and **Indexing** are both techniques used to improve data retrieval, but they work differently:

1. **Hashing:**
   - **Purpose:** Used to map a key to a specific location (index) in a hash table using a hash function.
   - **Time Complexity:** Provides constant-time (O(1)) operations in average cases.
   - **Structure:** Usually implemented using a **hash table**.
   - **Collisions:** Hashing must handle collisions when multiple keys hash to the same index.
   - **Use Case:** Best suited for scenarios requiring fast lookups with exact matches (e.g., dictionaries, sets).

2. **Indexing:**
   - **Purpose:** Creates a structured reference to locate data within a collection quickly without scanning the entire dataset.
   - **Time Complexity:** Typically reduces search complexity to O(log n) in large datasets (e.g., using trees or B-trees).
   - **Structure:** Usually involves **tree-like** structures (e.g., B-trees, B+ trees) or other ordered structures.
   - **Use Case:** Best suited for databases and large datasets, particularly when range queries or sorting is involved.

## True/False (Mark T for True and F for False)

1. **Binary search requires the array to be sorted.**
   - True (✔)
   - False

2. **Merge sort is an in-place sorting algorithm.**
   - True
   - False (✔)

3. **The time complexity of quicksort in the worst case is O(n^2).**
   - True (✔)
   - False

4. **Insertion sort is efficient for large datasets.**
   - True
   - False (✔)

5. **A hash function is used to resolve collisions in a hash table.**
   - True
   - False (✔)

6. **Radix sort is a comparison-based sorting algorithm.**
   - True
   - False (✔)

7. **A binary heap can be used to implement a priority queue.**
   - True (✔)
   - False

8. **The worst-case time complexity of bubble sort is O(n log n).**
   - True
   - False (✔)

9. **An AVL tree is a self-balancing binary search tree.**
   - True (✔)
   - False

10. **Depth-first search (DFS) uses a queue to keep track of vertices.**
    - True
    - False (✔)

11. **The time complexity of BFS is O(V + E), where V is the number of vertices and E is the number of edges.**
    - True (✔)
    - False

12. **In dynamic programming, overlapping subproblems are solved only once.**
    - True (✔)
    - False

13. **The Bellman-Ford algorithm can handle negative weight edges.**
    - True (✔)
    - False

14. **A binary search tree (BST) is always balanced.**
    - True
    - False (✔)

15. **The Floyd-Warshall algorithm finds the shortest path between all pairs of vertices.**
    - True (✔)
    - False

16. **Greedy algorithms always provide the optimal solution for all problems.**
    - True
    - False (✔)

17. **In a min-heap, the smallest element is always at the root.**
    - True (✔)
    - False

18. **Kruskal’s algorithm builds the minimum spanning tree by adding edges in increasing order of weight.**
    - True (✔)
    - False

19. **Depth-first search (DFS) is typically implemented using recursion.**
    - True (✔)
    - False

20. **Selection sort repeatedly selects the smallest element from the unsorted part of the array and puts it at the beginning.**
    - True (✔)
    - False

21. **In a hash table, chaining is a technique used to handle collisions.**
    - True (✔)
    - False

22. **The time complexity of accessing an element in a hash table with separate chaining is O(1) in the worst case.**
    - True
    - False (✔)

23. **The Traveling Salesman Problem (TSP) is a problem that can be solved using dynamic programming.**
    - True (✔)
    - False

24. **In a priority queue implemented with a binary heap, the operations insert and extract-min have the same time complexity.**
    - True
    - False (✔)

25. **The merge sort algorithm is a stable sorting algorithm.**
    - True (✔)
    - False

26. **Breadth-first search (BFS) can be used to find the shortest path in an unweighted graph.**
    - True (✔)
    - False

27. **Quick sort is always faster than merge sort.**
    - True
    - False (✔)

28. **The N-Queens problem is an example of a problem that can be solved using backtracking.**
    - True (✔)
    - False

29. **In an AVL tree, the height of the tree is O(log n).**
    - True (✔)
    - False

30. **The Knapsack problem can be solved using a greedy approach.**
    - True
    - False (✔)

## Multiple Choice (Select the best answer)

### Insertion Sort

1. What is the time complexity of insertion sort in the worst case?
   - A) O(n)
   - B) O(n log n)
   - C) O(n^2) (✔)
   - D) O(1)

2. In which scenario is insertion sort most efficient?
   - A) Randomized data
   - B) Sorted data (✔)
   - C) Reverse sorted data
   - D) None of the above

3. In insertion sort, which element is the first to be considered for insertion?
   - A) First element
   - B) Second element (✔)
   - C) Last element
   - D) Middle element

4. What is the key operation in insertion sort?
   - A) Comparing adjacent elements
   - B) Splitting the array
   - C) Shifting elements (✔)
   - D) Partitioning the array

### Merge Sort

5. What is the best-case time complexity of merge sort?
   - A) O(n^2)
   - B) O(n log n) (✔)
   - C) O(n)
   - D) O(log n)

6. Merge sort uses which algorithmic technique?
   - A) Greedy
   - B) Divide-and-conquer (✔)
   - C) Dynamic programming
   - D) Backtracking

7. How is merging done in merge sort?
   - A) By swapping adjacent elements
   - B) By splitting and combining sorted arrays (✔)
   - C) By comparing the middle element
   - D) By partitioning the array

8. What is the space complexity of merge sort?
   - A) O(n log n)
   - B) O(n) (✔)
   - C) O(log n)
   - D) O(1)

### Quick Sort

9. What is the worst-case time complexity of quicksort?
   - A) O(n^2) (✔)
   - B) O(n log n)
   - C) O(n)
   - D) O(log n)

10. What is the average-case time complexity of quicksort?
   - A) O(n^2)
   - B) O(n log n) (✔)
   - C) O(n)
   - D) O(log n)

11. In quicksort, the pivot element is used for what purpose?
   - A) Sorting
   - B) Partitioning (✔)
   - C) Swapping
   - D) Merging

12. Which strategy does quicksort use?
   - A) Divide-and-conquer (✔)
   - B) Greedy
   - C) Dynamic programming
   - D) Backtracking

### Selection Sort

13. What is the time complexity of selection sort in the worst case?
   - A) O(n^2) (✔)
   - B) O(n log n)
   - C) O(n)
   - D) O(log n)

14. In selection sort, which element is selected during each iteration?
   - A) The maximum element
   - B) The minimum element (✔)
   - C) The middle element
   - D) A random element

15. How does selection sort differ from insertion sort?
   - A) It sorts one element at a time
   - B) It finds the minimum in each iteration (✔)
   - C) It divides the array into subarrays
   - D) It uses a pivot

16. What is the space complexity of selection sort?
   - A) O(n)
   - B) O(log n)
   - C) O(1) (✔)
   - D) O(n^2)

### Binary Search Tree (BST)

17. Which of the following is true for a binary search tree?
   - A) All left children are greater than their parent
   - B) All right children are less than their parent
   - C) All left children are smaller than their parent (✔)
   - D) All nodes have two children

18. What is the time complexity of searching in a balanced binary search tree?
   - A) O(log n) (✔)
   - B) O(n)
   - C) O(n^2)
   - D) O(n log n)

19. In a binary search tree, what is the position of the smallest element?
   - A) Root node
   - B) Leftmost leaf node (✔)
   - C) Rightmost leaf node
   - D) Middle node

20. Which operation is not possible in a binary search tree?
   - A) Search
   - B) Insert
   - C) Merge (✔)
   - D) Delete

### Breadth-First Search (BFS)

21. What data structure is used to implement breadth-first search?
   - A) Stack
   - B) Queue (✔)
   - C) Priority queue
   - D) Deque

22. BFS explores nodes in which order?
   - A) Depth first
   - B) Breadth first (✔)
   - C) Randomly
   - D) In decreasing order of depth

23. What is the time complexity of BFS?
   - A) O(log n)
   - B) O(n) (✔)
   - C) O(n^2)
   - D) O(n log n)

### Depth-First Search (DFS)

24. DFS can be implemented using which data structure?
   - A) Stack (✔)
   - B) Queue
   - C) Priority queue
   - D) Deque

25. What is the primary difference between DFS and BFS?
   - A) DFS uses a stack, BFS uses a queue (✔)
   - B) DFS is faster
   - C) BFS is slower
   - D) Both use a stack

26. What is the time complexity of DFS for a graph with `V` vertices and `E` edges?
   - A) O(V + E) (✔)
   - B) O(V)
   - C) O(E)
   - D) O(V * E)

### Heaps

27. What is a heap?
   - A) A type of sorted array
   - B) A complete binary tree (✔)
   - C) A circular linked list
   - D) A stack of elements

28. In a min-heap, the root node contains:
   - A) The largest element
   - B) The smallest element (✔)
   - C) The middle element
   - D) A random element

29. What is the time complexity of inserting an element into a heap?
   - A) O(n)
   - B) O(log n) (✔)
   - C) O(1)
   - D) O(n log n)

30. In a max-heap, which of the following is true?
   - A) The left child is larger than the right child
   - B) The parent is larger than its children (✔)
   - C) The right child is larger than the parent
   - D) The tree is incomplete

### Heap Sort

31. Heap sort is based on which data structure?
   - A) Linked list
   - B) Binary search tree
   - C) Heap (✔)
   - D) Stack

32. What is the time complexity of heap sort?
   - A) O(n)
   - B) O(n^2)
   - C) O(n log n) (✔)
   - D) O(log n)

33. What is the first step of heap sort?
   - A) Partition the array
   - B) Build a heap (✔)
   - C) Merge two halves
   - D) Find the pivot

34. Heap sort is a(n) ____ algorithm.
   - A) Stable
   - B) In-place (✔)
   - C) Recursive
   - D) Non-in-place

### Memory Management

35. What is memory management?
   - A) The allocation and deallocation of memory (✔)
   - B) The use of memory in algorithms
   - C) The tracking of memory access
   - D) None of the above

36. Which of the following is an automatic memory management technique?
   - A) Manual memory allocation
   - B) Static memory allocation
   - C) Garbage collection (✔)
   - D) Paging

37. In dynamic memory allocation, which function is used to allocate memory in C?
   - A) malloc() (✔)
   - B) free()
   - C) delete
   - D) calloc()

38. What does the `free()` function in C do?
   - A) Allocates memory
   - B) Releases memory (✔)
   - C) Resizes memory
   - D) Copies memory

### Garbage Collection

39. Garbage collection is a process of:
   - A) Allocating memory
   - B) Releasing memory that is no longer in use (✔)
   - C) Copying data to new memory blocks
   - D) Rearranging memory addresses

40. Which of the following programming languages uses garbage collection?
   - A) C
   - B) Java (✔)
   - C) Assembly
   - D) C++

Here are more multiple-choice questions (MCQs) that continue to explore advanced sorting algorithms, data structures, and algorithm concepts.

### Binary Search

43. What is the time complexity of binary search in the best case?
   - A) O(n)
   - B) O(log n)
   - C) O(1) (✔)
   - D) O(n^2)

44. Binary search can only be applied to:
   - A) Unsorted arrays
   - B) Sorted arrays (✔)
   - C) Arrays with negative numbers
   - D) Arrays of even length

45. In binary search, how many comparisons are made in the worst case for an array of size 32?
   - A) 2
   - B) 4
   - C) 5
   - D) 6 (✔)

46. Which data structure can benefit most from binary search?
   - A) Linked list
   - B) Heap
   - C) Sorted array (✔)
   - D) Unsorted array

### Quick Sort (Advanced)

47. Quick sort is typically faster than merge sort for:
   - A) Small input sizes (✔)
   - B) Large input sizes
   - C) Linked lists
   - D) Arrays with repeated elements

48. In the best case, the pivot in quicksort divides the array:
   - A) Into two equal halves (✔)
   - B) Into three parts
   - C) Into a sorted and unsorted part
   - D) Into one part

49. When does quicksort perform the worst?
   - A) When all elements are distinct
   - B) When all elements are equal
   - C) When the pivot is the smallest or largest element (✔)
   - D) When there are many duplicate elements

50. What is the key disadvantage of quicksort compared to merge sort?
   - A) Higher time complexity
   - B) Unstable sorting (✔)
   - C) Extra memory usage
   - D) Requires pre-sorted input

### Radix Sort

51. Radix sort is best suited for sorting:
   - A) Strings
   - B) Integers (✔)
   - C) Floating point numbers
   - D) Linked lists

52. Radix sort operates on:
   - A) The least significant digit first (✔)
   - B) The most significant digit first
   - C) The middle digit first
   - D) The largest element first

53. What is the time complexity of radix sort for `n` keys with `d` digits?
   - A) O(n log n)
   - B) O(d * n) (✔)
   - C) O(n^2)
   - D) O(log n)

54. Radix sort is:
   - A) Stable (✔)
   - B) Unstable
   - C) In-place
   - D) Recursive

### Hashing

55. Hashing is mainly used for:
   - A) Sorting elements
   - B) Searching elements (✔)
   - C) Merging elements
   - D) Reversing elements

56. In hashing, collisions occur when:
   - A) The hash table is full
   - B) Two keys map to the same index (✔)
   - C) The hash function is complex
   - D) The hash function is non-injective

57. What is the best-case time complexity of searching in a hash table?
   - A) O(n)
   - B) O(log n)
   - C) O(1) (✔)
   - D) O(n log n)

58. Which technique is used to resolve hash collisions?
   - A) Linear probing (✔)
   - B) Quicksort
   - C) Binary search
   - D) Divide-and-conquer

### Dynamic Programming

67. Which of the following problems is best solved using dynamic programming?
   - A) Insertion sort
   - B) Binary search
   - C) Longest common subsequence (✔)
   - D) Quick sort

68. What is the main principle behind dynamic programming?
   - A) Recursion
   - B) Divide-and-conquer
   - C) Optimal substructure and overlapping subproblems (✔)
   - D) Greedy strategy

69. Which of the following is an example of a dynamic programming problem?
   - A) Minimum spanning tree
   - B) Fibonacci sequence (✔)
   - C) Binary search
   - D) Quick select

70. What is the time complexity of the dynamic programming solution to the knapsack problem with `n` items and capacity `W`?
   - A) O(n * W) (✔)
   - B) O(n log n)
   - C) O(n^2)
   - D) O(log n)

### Divide-and-Conquer Algorithms

71. Which of the following sorting algorithms uses divide-and-conquer?
   - A) Insertion sort
   - B) Merge sort (✔)
   - C) Heap sort
   - D) Selection sort

72. In divide-and-conquer algorithms, the subproblems are:
   - A) Independent of each other (✔)
   - B) Dependent on each other
   - C) Solved in parallel
   - D) Solved one by one

73. What is the time complexity of the divide step in merge sort?
   - A) O(n)
   - B) O(n^2)
   - C) O(log n) (✔)
   - D) O(1)

74. Which of the following algorithms does not use the divide-and-conquer strategy?
   - A) Quick sort
   - B) Binary search
   - C) Merge sort
   - D) Bubble sort (✔)

## Fill in the Blanks

Sure! Here are 30 fill-in-the-blank questions related to algorithms and data structures:

1. **In a binary search, the array must be __________.**
   - Answer: sorted
2. **The time complexity of insertion sort is O(n^2) in the __________ case.**
   - Answer: worst
3. **Merge sort is an __________ sorting algorithm.**
   - Answer: external
4. **Quick sort is generally faster than __________ sort.**
   - Answer: bubble
5. **A __________ table is used to store key-value pairs.**
   - Answer: hash
6. **The radix sort algorithm is based on __________ operations.**
   - Answer: digit
7. **In a binary heap, the smallest element is at the __________.**
   - Answer: root
8. **A binary search tree is also known as a __________ search tree.**
   - Answer: ordered
9. **The time complexity of breadth-first search (BFS) is O(V + E), where V is the number of __________ and E is the number of edges.**
   - Answer: vertices
10. **In a min-heap, every parent node is less than or equal to its __________ nodes.**
    - Answer: child
11. **In a depth-first search (DFS), the vertices are explored by going __________ first.**
    - Answer: deeper
12. **Selection sort repeatedly selects the __________ element from the unsorted part.**
    - Answer: smallest
13. **In hash tables, __________ is a technique used to handle collisions.**
    - Answer: chaining
14. **The time complexity of accessing an element in a hash table with open addressing is O(1) in the __________ case.**
    - Answer: average
15. **Greedy algorithms make the __________ choice at each step.**
    - Answer: local
16. **In a priority queue implemented with a binary heap, the __________ operation takes O(log n) time.**
    - Answer: insert
17. **Breadth-first search (BFS) uses a __________ to keep track of vertices.**
    - Answer: queue
18. **In a priority queue implemented with a binary heap, the __________ element is always at the root.**
    - Answer: minimum (or maximum, depending on min-heap or max-heap)
19. **The merge sort algorithm is __________, meaning it preserves the order of equal elements.**
    - Answer: stable
20. **The Traveling Salesman Problem (TSP) is known to be a __________ problem.**
    - Answer: NP-hard
21. **In depth-first search (DFS), the vertices are typically explored using __________ traversal.**
    - Answer: recursive
22. **The __________ sort algorithm involves partitioning an array into subarrays and sorting each subarray.**
    - Answer: quick

