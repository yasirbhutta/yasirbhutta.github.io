---
layout: page
title: "C++ One-Dimensional Arrays — Syntax & Examples"
description: "Beginner-friendly guide to C++ one-dimensional arrays: declaration, initialization, indexing, accessing elements, loops, and practical examples."
keywords: C++, arrays, one-dimensional array, array initialization, array indexing, accessing elements, array examples, for loop, beginner tutorial, programming basics
---

## Learning Objectives

After completing this lesson, students will be able to:

1. Understand the concept of an array using a real-life example.
2. Define an array and explain its purpose.
3. Declare and initialize a one-dimensional array.
4. Understand array indexes and access individual elements.
5. Assign and update array elements.
6. Use `for` loops to input and display array elements.
7. Perform basic operations on arrays, such as calculating their sum.
8. Examples
   
---

## 1. Understanding Arrays Through a Real-Life Example

Suppose a teacher wants to store the marks of 5 students in a programming class.

One way is to declare a separate variable for each student's marks.

### Without Using an Array

```cpp
int student1 = 85;
int student2 = 90;
int student3 = 75;
int student4 = 88;
int student5 = 92;
```

Here, we have declared five separate variables to store the marks of five students.

**Problem:** What if a teacher wants to store the marks of 100 students? Declaring 100 separate variables would make the program difficult to manage.

### Using an Array

C++ provides an array that allows us to store multiple values of the same data type under a single variable name.

```cpp
int marks[5] = {85, 90, 75, 88, 92};
```

Now, all five students' marks are stored in a single array named `marks`.

### Understanding the Code

| Code                   | Meaning                            |
| ---------------------- | ---------------------------------- |
| `int`                  | Data type of the elements          |
| `marks`                | Name of the array                  |
| `[5]`                  | Number of elements in the array    |
| `{85, 90, 75, 88, 92}` | Initial values stored in the array |

**Remember:** An array stores multiple values of the same data type using a single variable name.

---

## 2. What is an Array?

An **array** is a collection of multiple values of the same data type stored in contiguous memory locations and accessed using a single variable name with different indexes.

Instead of declaring separate variables for multiple values, we can use an array.

### Example

```cpp
int marks[5];
```

This statement declares an array named `marks` that can store five integer values.

### Important Characteristics of an Array

1. An array can store multiple values.
2. All elements must have the same data type.
3. Elements are stored in contiguous memory locations.
4. Each element is accessed using an index.
5. Array indexing starts from zero in C++.

---

## 3. One-Dimensional Array

A **one-dimensional array** stores elements in a single sequence (a single row).

For example, the marks of five students can be stored in a one-dimensional array.

```cpp
int marks[5] = {85, 90, 75, 88, 92};
```

### Visual Representation of an Array

| Index | 0  | 1  | 2  | 3  | 4  |
| ----- | -- | -- | -- | -- | -- |
| Marks | 85 | 90 | 75 | 88 | 92 |

Each box represents one element of the array.

- The array name is `marks`.
- The array contains five elements.
- Each element has a different index.

---

## 4. Declaring a One-Dimensional Array

**Declaration** means creating an array by specifying its data type, name, and size.

### General Syntax

```cpp
data_type array_name[size];
```

### Example

```cpp
int numbers[5];
```

### Understanding the Code

| Part      | Explanation                               |
| --------- | ----------------------------------------- |
| `int`     | Each element will store an integer value. |
| `numbers` | Name of the array.                        |
| `[5]`     | The array can store five elements.        |

**Important:** When an ordinary local array is declared without initialization, its elements are not automatically initialized. Assign values before reading them.

![array structure](https://res.cloudinary.com/da0pjikvw/image/upload/v1766479462/array-structure-in-cpp_wljlrp.png)

---

## 5. Understanding Array Indexes

An **index** is a number used to identify and access a particular element of an array.

In C++, array indexing starts from `0`, not `1`.

Consider the following array:

```cpp
int marks[5] = {85, 90, 75, 88, 92};
```

### Array Index Table

| Student   | Array Index | Marks |
| --------- | ----------- | ----- |
| Student 1 | 0           | 85    |
| Student 2 | 1           | 90    |
| Student 3 | 2           | 75    |
| Student 4 | 3           | 88    |
| Student 5 | 4           | 92    |

[C++ Arrays With Examples](https://images.openai.com/static-rsc-4/EFu0oxb8-IxpJlxcmV19VL_kjySbyirrNo-EdiCLZzK5YzMQwnuzQictNNETvynj007JbxUSEpJwOQV-X8cEw1jC52LdEl_Et5VpNdaelQtrqL9cohkpIM4FKPipY2L950yWqxO84nsi8u_0_-QVJZ87bpfEefIHhZgzu3HeOm0?purpose=inline)

[algoflame.com](https://www.algoflame.com/blog/what-is-array/)

### Important Rules

- The first element has index `0`.
- The second element has index `1`.
- The last element has index `size - 1`.

**Formula:**

Last Index = Array Size - 1

For an array of size 5:

Last Index = 5 - 1 = 4

Therefore, the valid indexes are `0, 1, 2, 3, 4`.

---

## 6. Array Initialization

**Initialization** means assigning initial values to an array.

There are three common ways to initialize an array.

### Method 1: Initialize at Declaration

We can declare an array and assign values at the same time.

```cpp
int numbers[5] = {10, 20, 30, 40, 50};
```

Here, five integer values are assigned to the array.

### Method 2: Let the Compiler Calculate the Size

We can omit the array size when values are provided during initialization.

```cpp
int numbers[] = {5, 10, 15, 20};
```

The compiler calculates the array size as 4.

### Method 3: Initialize Elements One by One

We can declare an array first and assign values to individual elements later.

```cpp
int numbers[3];

numbers[0] = 10;
numbers[1] = 20;
numbers[2] = 30;
```

Here, values are assigned using their respective indexes.

**Remember:** The array size must be sufficient to store all the elements.

---

## 7. Accessing Individual Array Elements

We use the array name followed by an index inside square brackets to access an individual element.

### Example 1:

```cpp
int numbers[5] = {10, 20, 30, 40, 50};

cout << numbers[0] << endl;
cout << numbers[3] << endl;
```

### Output

```
10
40
```

### Understanding the Code

- `numbers[0]` accesses the first element, which is `10`.
- `numbers[3]` accesses the fourth element, which is `40`.

**Important:** The index identifies the position of an element, not its actual value.

---

## 8. Assigning Values to Individual Array Elements

We can assign values to array elements using their indexes.

### Example 2:

```cpp
#include <iostream>
using namespace std;

int main()
{
    int numbers[5];

    // Assigning values
    numbers[0] = 10;
    numbers[1] = 20;
    numbers[2] = 30;
    numbers[3] = 40;
    numbers[4] = 50;

    // Displaying values
    cout << numbers[0] << endl;
    cout << numbers[1] << endl;
    cout << numbers[2] << endl;
    cout << numbers[3] << endl;
    cout << numbers[4] << endl;

    return 0;
}
```

### Understanding the Code

**Step 1: Declare the array**

```cpp
int numbers[5];
```

Creates an array that can store five integers.

**Step 2: Assign values**

```cpp
numbers[0] = 10;
numbers[1] = 20;
numbers[2] = 30;
```

Assigns values to the first three elements. The remaining two elements are also assigned in the program.

**Step 3: Display values**

```cpp
cout << numbers[0] << endl;
```

Displays the value stored at index `0`.

### Output

```
10
20
30
40
50
```

### Memory Representation

| Index | Value |
| ----- | ----- |
| 0     | 10    |
| 1     | 20    |
| 2     | 30    |
| 3     | 40    |
| 4     | 50    |

---

## 9. Accessing Array Elements Using a `for` Loop

Imagine an array contains 100 elements. Writing 100 separate output statements would be time-consuming.

We can use a `for` loop to access and display all array elements.

### Example 3: 

```cpp
#include <iostream>
using namespace std;

int main()
{
    int numbers[5] = {10, 20, 30, 40, 50};

    for(int i = 0; i < 5; i++)
    {
        cout << numbers[i] << endl;
    }

    return 0;
}
```

### Output

```
10
20
30
40
50
```

### Understanding the Code

```cpp
for(int i = 0; i < 5; i++)
```

The loop runs five times.

| Iteration | Value of `i` | Accessed Element | Output |
| --------- | ------------ | ---------------- | ------ |
| 1         | 0            | `numbers[0]`     | 10     |
| 2         | 1            | `numbers[1]`     | 20     |
| 3         | 2            | `numbers[2]`     | 30     |
| 4         | 3            | `numbers[3]`     | 40     |
| 5         | 4            | `numbers[4]`     | 50     |

**Important Points:**

- `i` represents the array index.
- `i = 0` starts from the first element.
- `i < 5` ensures that the loop accesses five elements.
- `i++` increases the index by one after each iteration.
- `numbers[i]` accesses the element at the current index.

### Modify the Code

Try the following modifications:

1. Change the array values to `{5, 10, 15, 20, 25}`.
2. Display all elements on a single line instead of separate lines.
3. Display only the elements at indexes `1` and `3`.
4. Change the array size to 3 and update the loop condition.

---

## 10. Taking Input and Displaying Array Elements

So far, we have assigned values directly in the program.

In practical applications, we often need to take values from the user.

We can use `cin` with a `for` loop to input values into an array.

### Problem

Write a C++ program to store and display the marks of five students.

### Example 4:

```cpp
#include <iostream>
using namespace std;

int main()
{
    int marks[5];

    // Taking input
    cout << "Enter marks of 5 students:" << endl;

    for(int i = 0; i < 5; i++)
    {
        cin >> marks[i];
    }

    // Displaying output
    cout << "Marks of students are:" << endl;

    for(int i = 0; i < 5; i++)
    {
        cout << marks[i] << endl;
    }

    return 0;
}
```

### Understanding the Code

**Step 1: Declare the array**

```cpp
int marks[5];
```

Creates an array that can store marks of five students.

**Step 2: Take input using a loop**

```cpp
for(int i = 0; i < 5; i++)
{
    cin >> marks[i];
}
```

- The loop starts with index `0`.
- `cin >> marks[i]` takes input from the user.
- Each entered value is stored at the current index.
- The loop repeats until all five values are entered.

**Step 3: Display the array elements**

```cpp
for(int i = 0; i < 5; i++)
{
    cout << marks[i] << endl;
}
```

Displays all five stored values one by one.

### Sample Input

```
Enter marks of 5 students:
78
85
90
66
88
```

### Sample Output

```
Marks of students are:
78
85
90
66
88
```

### How Data is Stored

| Index | Student   | Stored Marks |
| ----- | --------- | ------------ |
| 0     | Student 1 | 78           |
| 1     | Student 2 | 85           |
| 2     | Student 3 | 90           |
| 3     | Student 4 | 66           |
| 4     | Student 5 | 88           |

---

## 11. Example 5: Calculating the Sum of Array Elements

We can perform mathematical operations on array elements.

For example, suppose we want to calculate the total of five numbers stored in an array.

### Problem

Write a C++ program to store five numbers in an array and calculate their sum.

### Program

```cpp
#include <iostream>
using namespace std;

int main()
{
    int numbers[5] = {10, 20, 30, 40, 50};
    int sum = 0;

    for(int i = 0; i < 5; i++)
    {
        sum = sum + numbers[i];
    }

    cout << "Sum = " << sum << endl;

    return 0;
}
```

### Understanding the Code

**Step 1: Declare and initialize the array**

```cpp
int numbers[5] = {10, 20, 30, 40, 50};
```

Stores five numbers in the array.

**Step 2: Initialize the sum variable**

```
int sum = 0;
```

Creates a variable named `sum` and initializes it with zero.

**Step 3: Calculate the sum**

```cpp
for(int i = 0; i < 5; i++)
{
    sum = sum + numbers[i];
}
```

The loop accesses each array element and adds its value to `sum`.

### Dry Run

| Iteration | Index (`i`) | Array Value | Previous Sum | New Sum |
| --------- | ----------- | ----------- | ------------ | ------- |
| 1         | 0           | 10          | 0            | 10      |
| 2         | 1           | 20          | 10           | 30      |
| 3         | 2           | 30          | 30           | 60      |
| 4         | 3           | 40          | 60           | 100     |
| 5         | 4           | 50          | 100          | 150     |

### Sample Output

```
Sum = 150
```

### Modify the Code

1. Change the array values.
2. Take five numbers from the user instead of initializing them directly.
3. Calculate the sum of only the first three elements.
4. Display the sum and the number of elements.

---

## 12. Common Mistakes to Avoid

| Mistake                                      | Correct Approach                          |
| -------------------------------------------- | ----------------------------------------- |
| Accessing the first element using index `1`  | Use index `0`.                            |
| Accessing an element outside the array size  | Use valid indexes from `0` to `size - 1`. |
| Using different data types in the same array | Use the same element data type.           |
| Reading an uninitialized array element       | Assign a value before reading it.         |
| Using `i <= 5` for an array of size 5        | Use `i < 5`.                              |

---

## 13. Example 6: Find the Largest and Smallest Element

### **Problem**

Suppose we have marks of five students:

`75, 80, 65, 90, 85`

We want to find:

- The highest marks.
- The lowest marks.

### **Complete C++ Code**

```cpp
#include <iostream>
using namespace std;

int main()
{
    int marks[5] = {75, 80, 65, 90, 85};

    int largest = marks[0];
    int smallest = marks[0];

    for (int i = 1; i < 5; i++)
    {
        if (marks[i] > largest)
        {
            largest = marks[i];
        }

        if (marks[i] < smallest)
        {
            smallest = marks[i];
        }
    }

    cout << "Largest Marks: " << largest << endl;
    cout << "Smallest Marks: " << smallest << endl;

    return 0;
}
```

### **Understand the Code**

**Step 1: Declare and initialize the array**

```cpp
int marks[5] = {75, 80, 65, 90, 85};
```

- `int` means the array stores integers.
- `marks` is the array name.
- `5` means the array contains five elements.
- Values are stored at indexes 0 to 4.

**Step 2: Initialize largest and smallest**

```cpp
int largest = marks[0];
int smallest = marks[0];
```

We assume the first element is both the largest and smallest.

Initially:

- Largest = 75
- Smallest = 75

**Step 3: Traverse the array**

```cpp
for (int i = 1; i < 5; i++)
```

The loop starts from index 1 because index 0 is already assigned to both variables.

**Step 4: Find the largest value**

```cpp
if (marks[i] > largest)
{
    largest = marks[i];
}
```

If the current element is greater than the largest value, update `largest`.

**Step 5: Find the smallest value**

```cpp
if (marks[i] < smallest)
{
    smallest = marks[i];
}
```

If the current element is smaller than the smallest value, update `smallest`.

### **Dry Run**

| Index | Marks | Largest | Smallest |
| ----- | ----- | ------- | -------- |
| 0     | 75    | 75      | 75       |
| 1     | 80    | 80      | 75       |
| 2     | 65    | 80      | 65       |
| 3     | 90    | 90      | 65       |
| 4     | 85    | 90      | 65       |

Final Result

Largest = 90, Smallest = 65.

### **Modify the Code**

**Modification 1:** Change the array values to:

```cpp
int marks[5] = {45, 88, 92, 67, 55};
```

Predict the largest and smallest values before running the program.

**Modification 2:** Change the array size from 5 to 10 and enter ten student marks using `cin`.

## 14. Example 7: Search an Element in an Array (Linear Search)

### **Problem**

Suppose we have the following student marks:

`75, 80, 65, 90, 85`

We want to search for a particular number.

For example, is 90 present in the array?

### **Complete C++ Code**

```cpp
#include <iostream>
using namespace std;

int main()
{
    int marks[5] = {75, 80, 65, 90, 85};

    int search;

    cout << "Enter marks to search: ";
    cin >> search;

    bool found = false;

    for (int i = 0; i < 5; i++)
    {
        if (marks[i] == search)
        {
            cout << "Element found at index: " << i << endl;

            found = true;
            break;
        }
    }

    if (found == false)
    {
        cout << "Element not found";
    }

    return 0;
}
```

### **Understand the Code**

**Step 1: Declare a variable for searching**

```cpp
int search;
```

This variable stores the value entered by the user.

**Step 2: Take input**

```cpp
cin >> search;
```

Suppose the user enters 90.

**Step 3: Declare a Boolean variable**

```cpp
bool found = false;
```

- `bool` stores either `true` or `false`.
- Initially, we assume the element is not found.

**Step 4: Check every array element**

```cpp
for (int i = 0; i < 5; i++)
```

The loop checks elements one by one.

**Step 5: Compare the current element**

```cpp
if (marks[i] == search)
```

The `==` operator checks whether two values are equal.

**Step 6: Update the result**

```cpp
found = true;
break;
```

- `found = true` means the element exists.
- `break` stops the loop because we have found the element.

### **Dry Run**

Searching for 90:

| Index | Array Value | Comparison | Result |
| ----- | ----------- | ---------- | ------ |
| 0     | 75          | 75 == 90   | False  |
| 1     | 80          | 80 == 90   | False  |
| 2     | 65          | 65 == 90   | False  |
| 3     | 90          | 90 == 90   | True   |

The search stops at index 3.

### **Modify the Code**

1. Search for a student roll number instead of marks.
2. Display the message `Student Found` instead of `Element Found`.
3. Remove `break` and observe what happens if duplicate values exist.
4. Modify the program to count how many times a searched value appears.

## 15. Example 8: Count Even and Odd Numbers

### **Problem**

Suppose we have these numbers:

`10, 15, 20, 25, 30, 35`

We want to count:

- Total even numbers.
- Total odd numbers.

### **Complete C++ Code**

```cpp
#include <iostream>
using namespace std;

int main()
{
    int numbers[6] = {10, 15, 20, 25, 30, 35};

    int even = 0;
    int odd = 0;

    for (int i = 0; i < 6; i++)
    {
        if (numbers[i] % 2 == 0)
        {
            even++;
        }
        else
        {
            odd++;
        }
    }

    cout << "Even Numbers: " << even << endl;
    cout << "Odd Numbers: " << odd << endl;

    return 0;
}
```

### **Understand the Code**

**Step 1: Initialize counters**

```
int even = 0;
int odd = 0;
```

Both counters start from zero.

**Step 2: Traverse the array**

```cpp
for (int i = 0; i < 6; i++)
```

The loop checks all six numbers.

**Step 3: Check even numbers**

```cpp
if (numbers[i] % 2 == 0)
```

The `%` operator returns the remainder.

For example:

- `10 % 2 = 0` → Even
- `15 % 2 = 1` → Odd

**Step 4: Increase the counter**

```
even++;
```

The `++` operator increases the counter by one.

It is equivalent to:

```
even = even + 1;
```

### **Dry Run**

| Number | Remainder | Even | Odd |
| ------ | --------- | ---- | --- |
| 10     | 0         | 1    | 0   |
| 15     | 1         | 1    | 1   |
| 20     | 0         | 2    | 1   |
| 25     | 1         | 2    | 2   |
| 30     | 0         | 3    | 2   |
| 35     | 1         | 3    | 3   |

**Output:**

```
Even Numbers: 3
Odd Numbers: 3
```

### **Modify the Code**

1. Count positive and negative numbers.
2. Count numbers greater than 50.
3. Count numbers divisible by 5.
4. Count even and odd numbers entered by the user.

## 16. Example 9: Reverse an Array

### **Problem**

Suppose an array contains:

`10, 20, 30, 40, 50`

We want to display its elements in reverse order:

`50, 40, 30, 20, 10`

### **Complete C++ Code**

```cpp
#include <iostream>
using namespace std;

int main()
{
    int numbers[5] = {10, 20, 30, 40, 50};

    for (int i = 4; i >= 0; i--)
    {
        cout << numbers[i] << " ";
    }

    return 0;
}
```

### **Understand the Code**

**Step 1: Understand array indexes**

| Index | Value |
| ----- | ----- |
| 0     | 10    |
| 1     | 20    |
| 2     | 30    |
| 3     | 40    |
| 4     | 50    |

**Step 2: Start from the last index**

```cpp
int i = 4;
```

The last index of an array of size 5 is 4.

**Step 3: Set the loop condition**

```cpp
i >= 0;
```

Continue until index 0.

**Step 4: Decrease the index**

```cpp
i--;
```

Move one position backwards.

**Step 5: Display the current element**

```cpp
cout << numbers[i] << " ";
```

This displays elements from the last index to the first.

### **Dry Run**

| Iteration | Index | Value |
| --------- | ----- | ----- |
| 1         | 4     | 50    |
| 2         | 3     | 40    |
| 3         | 2     | 30    |
| 4         | 1     | 20    |
| 5         | 0     | 10    |

### **Modify the Code**

1. Take five numbers from the user.
2. Display the array in reverse order.
3. Modify the program to actually reverse the array values instead of only displaying them in reverse order.

## 17 **Example: Copy One Array into Another**

### **Problem**

Suppose we have an array containing five student marks.

We want to copy all its values into another array.

Original array:

`10, 20, 30, 40, 50`

Copied array:

`10, 20, 30, 40, 50`

### **Complete C++ Code**

```cpp
#include <iostream>
using namespace std;

int main()
{
    int first[5] = {10, 20, 30, 40, 50};

    int second[5];

    for (int i = 0; i < 5; i++)
    {
        second[i] = first[i];
    }

    cout << "Copied Array: ";

    for (int i = 0; i < 5; i++)
    {
        cout << second[i] << " ";
    }

    return 0;
}
```

### **Understand the Code**

**Step 1: Create the original array**

```
int first[5] = {10, 20, 30, 40, 50};
```

This array contains the original values.

**Step 2: Declare another array**

```cpp
int second[5];
```

This array will store copied values.

**Step 3: Copy elements**

```cpp
second[i] = first[i];
```

This statement copies one element at a time.

For example:

- `second[0] = first[0]`
- `second[1] = first[1]`
- `second[2] = first[2]`

The loop continues until all elements are copied.

### **Dry Run**

| Index | First Array | Second Array |
| ----- | ----------- | ------------ |
| 0     | 10          | 10           |
| 1     | 20          | 20           |
| 2     | 30          | 30           |
| 3     | 40          | 40           |
| 4     | 50          | 50           |

### **Modify the Code**

1. Take values from the user instead of initializing the first array.
2. Copy only even numbers into the second array.
3. Copy the elements in reverse order.

## 18. **Example 10: Sort Array Elements (Bubble Sort)**

### **Problem**

Suppose we have five student marks:

`50, 20, 40, 10, 30`

We want to arrange them in ascending order:

`10, 20, 30, 40, 50`

[Explore Bubble Sort – Interactive Step-by-Step Animation](https://algomaster.io/animations/dsa/bubble-sort)

### **Dry Run – Bubble Sort (Step-by-Step)**

Let's understand how Bubble Sort arranges an array in **ascending order** by comparing and swapping adjacent elements.

**Initial Array:**

`50, 20, 40, 10, 30`

**Step 1: First Pass**

In the first pass, compare each pair of adjacent elements. If the left element is greater than the right element, swap their positions.

| Step | Comparison | Action | Array After Comparison |
| ---- | ---------- | ------ | ---------------------- |
| 1    | 50 and 20  | Swap   | 20, 50, 40, 10, 30     |
| 2    | 50 and 40  | Swap   | 20, 40, 50, 10, 30     |
| 3    | 50 and 10  | Swap   | 20, 40, 10, 50, 30     |
| 4    | 50 and 30  | Swap   | 20, 40, 10, 30, 50     |

End of Pass 1

Array after the first pass:

`20, 40, 10, 30, 50`

**What happened?**

- Four comparisons were performed.
- Four swaps were made.
- The largest element, `50`, moved to the last position.
- The last position is now sorted.

**Step 2: Second Pass**

Now compare the remaining unsorted elements. There is no need to compare the last element because `50` is already in its correct position.

| Step | Comparison | Action  | Array After Comparison |
| ---- | ---------- | ------- | ---------------------- |
| 1    | 20 and 40  | No Swap | 20, 40, 10, 30, 50     |
| 2    | 40 and 10  | Swap    | 20, 10, 40, 30, 50     |
| 3    | 40 and 30  | Swap    | 20, 10, 30, 40, 50     |

End of Pass 2

Array after the second pass:

`20, 10, 30, 40, 50`

**What happened?**

- Three comparisons were performed.
- Two swaps were made.
- The second-largest element, `40`, reached its correct position.

**Step 3: Third Pass**

Compare the remaining unsorted elements.

| Step | Comparison | Action  | Array After Comparison |
| ---- | ---------- | ------- | ---------------------- |
| 1    | 20 and 10  | Swap    | 10, 20, 30, 40, 50     |
| 2    | 20 and 30  | No Swap | 10, 20, 30, 40, 50     |

End of Pass 3

Array after the third pass:

`10, 20, 30, 40, 50`

**Step 4: Fourth Pass**

Compare the remaining two elements.

| Step | Comparison | Action  | Array After Comparison |
| ---- | ---------- | ------- | ---------------------- |
| 1    | 10 and 20  | No Swap | 10, 20, 30, 40, 50     |

End of Pass 4

**Final Sorted Array**

**10, 20, 30, 40, 50**

The array is now sorted in ascending order.

### **Complete C++ Code**

```cpp
#include <iostream>
using namespace std;

int main()
{
    int numbers[5] = {50, 20, 40, 10, 30};

    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4 - i; j++)
        {
            if (numbers[j] > numbers[j + 1])
            {
                int temp = numbers[j];

                numbers[j] = numbers[j + 1];

                numbers[j + 1] = temp;
            }
        }
    }

    cout << "Sorted Array: ";

    for (int i = 0; i < 5; i++)
    {
        cout << numbers[i] << " ";
    }

    return 0;
}
```

### **Understand the Code**

Bubble Sort uses two loops.

**Step 1: Outer loop**

```cpp
for (int i = 0; i < 4; i++)
```

- The outer loop controls the number of passes.
- For five elements, we need at most four passes.

**Step 2: Inner loop**

```cpp
for (int j = 0; j < 4 - i; j++)
```

- Compares adjacent elements.
- The number of comparisons decreases after each pass.
- The already sorted elements at the end do not need to be compared again.

**Step 3: Compare two elements**

```cpp
if (numbers[j] > numbers[j + 1])
```

If the left element is greater than the right element, they must be swapped.

**Step 4: Understand swapping**

```cpp
int temp = numbers[j];

numbers[j] = numbers[j + 1];

numbers[j + 1] = temp;
```

Suppose:

- `numbers[j] = 50`
- `numbers[j + 1] = 20`

The temporary variable stores 50.

Then 20 is placed in the first position, and 50 is placed in the second position.

**Swapping example**

BEFORE

**50**

**20**

AFTER

**20**

**50**


### **10.5 Modify the Code**

1. Change ascending order to descending order.
2. Take five numbers from the user.
3. Find the highest marks after sorting.

## 19. **Example 11: Finding Array Length and Copying an Array in Reverse Order**

```cpp
#include <iostream>
using namespace std;
int main()
{
 int first[7] = {10, 20, 30, 40, 50, 60, 70};
 int second[7];
 int arr_size = sizeof(first)/sizeof(first[0]);
 cout << "Array Size = " << arr_size << endl;
 for (int i = 0; i < arr_size; i++)
 {
 second[i] = first[arr_size-1-i];
 }
 cout << "Copied Array: ";
 for (int i = 0; i < arr_size; i++)
 {
 cout << second[i] << " ";
 }
 return 0;
}
```
for more detail about `Array Length`, see [C++ Array Length — How to Get Array Size with sizeof ](cpp-array-length.md)


## 📘 **Related Topics**

- [C++ Array Length — How to Get Array Size with sizeof & std::size](array-length.md)
- [C++ Structures (struct) — Definition, Initialization & Best Practices](cpp-structures.md)

## References

- [1] TylerMSFT, “Arrays (C++),” MicrosoftLearn, May 19, 2025. https://learn.microsoft.com/en-us/cpp/cpp/arrays-cpp?view=msvc-170 (accessed Nov. 26, 2026).
