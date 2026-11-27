---
layout: page
title: "C++ Array Coding Exercises — Practice Problems and Solutions"
description: "Practice C++ one-dimensional array concepts with coding exercises on sizeof(), even-number filtering, reverse copying, loops, and array element access."
keywords: C++ array coding exercises, C++ array practice problems, one-dimensional array exercises, C++ array examples, sizeof array exercise, copy array elements C++, reverse array C++, even numbers array C++, beginner C++ arrays
---

## Contents

- [C++ One-Dimensional Arrays — Coding Exercises](#cpp-arrays)
  
<a id="cpp-arrays"></a>

# Section 1: `C++ One-Dimensional Arrays`  

## Problem Statement 1: Copying Even Numbers into a Second Array

**Exercise ID:** `ARR-COD-030`

**Solution:** [View Solution](../../solutions/loops/for-solutions.md#loop-cod-030)

Write a C++ program that stores 10 integers in the first array. Copy only the even numbers from the first array into a second array.

**Tasks:**

1. Declare and initialize the first array with 10 integers.
2. Calculate the length of the first array using `sizeof()`.
3. Declare a second array to store even numbers.
4. Use a `for` loop to check each element of the first array.
5. Copy only even numbers into the second array.
6. Display the elements of the second array.

**Requirements:**

- Use two separate arrays.
- Use `sizeof()` to calculate the first array's length.
- Use the modulus operator (`%`) to identify even numbers.
- Use a `for` loop to process array elements.
- Use a separate variable to track the number of even numbers copied.
- Display only the even numbers stored in the second array.

### Problem Statement 2:  Copying Array Elements in Reverse Order

Write a C++ program that stores 7 integers in the first array and copies all its elements into a second array in reverse order.

**Tasks:**

1. Declare and initialize the first array with 7 integers.
2. Calculate the length of the first array using `sizeof()`.
3. Declare a second array of the same size.
4. Use a `for` loop to access the elements of the first array in reverse order.
5. Copy the elements into the second array.
6. Display the elements of the second array.

**Requirements:**

- Use two separate arrays.
- Use `sizeof()` to calculate the array length.
- Use a `for` loop for copying elements.
- Use the expression `first[arr_size - 1 - i]` to access elements in reverse order.
- Store the reversed elements in the second array.
- Display the second array after copying.