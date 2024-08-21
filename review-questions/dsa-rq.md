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



