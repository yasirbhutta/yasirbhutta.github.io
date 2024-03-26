# MATLAB: Vectors and Matrices

Connect with me: [Youtube](https://www.youtube.com/yasirbhutta) \| [LinkedIn](https://www.linkedin.com/in/yasirbhutta/) \| [WhatsApp Channel](https://whatsapp.com/channel/0029VaC3BC160eBZZSs3CW0c) \| [Web](https://yasirbhutta.github.io/) \| [Facebook](https://www.facebook.com/yasirbhutta786) \| [Twitter](https://twitter.com/yasirbhutta)

- [Download PDF](https://yasirbhutta.github.io/matlab/docs/vectors-matrices.pdf)

- To access the updated handouts, please click on the following link:
[https://yasirbhutta.github.io/matlab/docs/vectors-matrices.html](https://yasirbhutta.github.io/matlab/docs/vectors-matrices.html)

## Vector Products

**Important:** To perform matrix multiplication, the first matrix must have the same number of columns as the second matrix has rows. The number of rows of the resulting matrix equals the number of rows of the first matrix, and the number of columns of the resulting matrix equals the number of columns of the second matrix. [1]


**Important:** In MATLAB, the concept of conjugate refers to the complex conjugate of a number or element within a matrix. The complex conjugate of a complex number is a new number with the same real part but the imaginary part negated.


## Vectors in MATLAB

Vectors are one-dimensional arrays used to store a collection of numbers. You can create them in different ways:

1. **Using square brackets `[]`:**
   ```matlab
   myVector = [1 2 3 4 5];
   ```

2. **Using the colon operator `:`:**
   ```matlab
   rangeVector = 1:5;  % Creates a vector from 1 to 5 (inclusive)
   ```

### Accessing Elements

There are two main ways to access individual elements within a vector:

1. **Using Indices:**

   - MATLAB uses **one-based indexing**, meaning the first element has an index of 1, the second has an index of 2, and so on.
   - To access a specific element, enter the vector name followed by the index in parentheses:
     ```matlab
     myVector(2)  % Accesses the second element (value 2)
     rangeVector(4)  % Accesses the fourth element (value 4)
     ```

2. **Using Colon Operator `:`:**

   - The colon operator allows you to select a range of elements:
     - `vector(start:end)`: Accesses elements from `start` (inclusive) to `end` (inclusive).
     - `vector(start:step:end)`: Accesses elements with a specific `step` between them (similar to Python slicing).
     - `vector(:)`: Accesses all elements of the vector.
     ```matlab
     myVector(2:4)  % Accesses elements from index 2 (value 2) to index 4 (value 4)
     rangeVector(1:2:5)  % Accesses elements 1, 3, and 5 (with a step of 2)
     myVector(:)  % Accesses all elements (same as `myVector`)
     ```

3. **Creating and Accessing a Vector:**
   ```matlab
   fruits = ["apple" "banana" "orange"];  % Create a vector of strings
   secondFruit = fruits(2);  % Access the second element ("banana")
   ```

4. **Extracting Sub-vectors:**
   ```matlab
   temperatures = [20 32 25 18];
   firstTwo = temperatures(1:2);  % Extract the first two elements ([20 32])
   evenIndices = temperatures(2:2:end);  % Extract elements at even indices ([32 18])
   ```

**Tips**

- Remember one-based indexing.
- Use `end` as an index to refer to the last element: `myVector(end)`.
- The colon operator is versatile for selecting elements or creating new vectors.

**See also:**

- [Matrix Indexing in MATLAB - MathWorks Docs](https://www.mathworks.com/company/technical-articles/matrix-indexing-in-matlab.html)

## Generating Row Vectors with Even Spacing in MATLAB

### **a. linspace**
Linspace in MATLAB is a function used to generate a row vector containing **evenly spaced values** between two specified endpoints. 

**Syntax:**
- `y = linspace(x1, x2)`: This creates a row vector with 100 (default) points between `x1` and `x2`.
- `y = linspace(x1, x2, n)`: This allows you to specify the number of points (`n`) in the vector.

**Key Points:**
- The spacing between values is calculated as: `(x2 - x1) / (n - 1)`.
- It includes both the starting (`x1`) and ending (`x2`) points in the output vector.
- Linspace is similar to the colon operator (`:`) but offers more control over the number of points.

**Use Cases:**
   - Creating data points for plotting functions.
   - Setting up evenly spaced grid points for numerical calculations.
   - Controlling the sampling rate for simulations.

**See also:**
- **MATLAB Documentation:** [https://www.mathworks.com/help/matlab/ref/linspace.html](https://www.mathworks.com/help/matlab/ref/linspace.html)


### **b. logspace**
In MATLAB, the `logspace` function is used to generate a row vector containing **logarithmically spaced values** between two specified points. It's the logarithmic counterpart of the `linspace` function you saw earlier.

**Syntax:**
- `y = logspace(a, b)`: This creates a row vector with 50 points (default) between decades of 10^a and 10^b.
- `y = logspace(a, b, n)`: This allows you to specify the number of points (`n`) in the vector.
- `y = logspace(a, pi)`: This is useful for creating logarithmically spaced frequencies (especially in digital signal processing) in the interval [10^a, pi].

**Key Points:**
  - The spacing is based on logarithms, not linear values. Points are closer together at lower values and farther apart at higher values.
  - It includes an approximation of the starting point (10^a) and the ending point (might not be exactly pi if used) in the output vector.
 
* **Use Cases:**
   - Generating frequencies for simulations or filter design.
   - Sampling data across a wide range of values.
   - Creating logarithmic axes for plotting data that exhibits exponential growth or decay.

**See also**

- **MATLAB Documentation:** [https://www.mathworks.com/help/matlab/ref/logspace.html](https://www.mathworks.com/help/matlab/ref/logspace.html)

## Vector Functions

### 1. sum(x)
### 2. mean(x)
### 3. length(x)
### 4. max(x)
### 5. min(x)
### 6. prod(x)
### 7. sign(x)
### 8. find(x)

- The `find` function in MATLAB is a versatile tool for finding specific elements or their indices within a vector. 

**1. Finding Non-Zero Elements:**

* The simplest usage is `k = find(v)`. This returns a vector `k` containing the linear indices of all non-zero elements in vector `v`.

**Example:**

```matlab
v = [1, 0, 3, 0, 5];
k = find(v);
disp(k)  % Output: 1 3 5
```

**2. Finding a Specific Number of Elements:**

- You can specify the number of elements to find:
    * `k = find(v, n)` returns the first `n` indices of non-zero elements.
    * `k = find(v, n, 'last')` returns the last `n` indices of non-zero elements.

**Example:**

```matlab
v = [2, 0, -1, 4, 0];
first_two = find(v, 2);  % Find the first two non-zero elements
last_two = find(v, 2, 'last');  % Find the last two non-zero elements
disp(first_two)  % Output: 1 3
disp(last_two)  % Output: 3 4
```

**3. Finding Elements Based on Conditions:**

* Use relational operators (`<`, `>`, `<=`, `>=`, `==`, `~=`) within `find` to locate elements meeting specific criteria.

**Example:**

```matlab
v = [8, 2, 6, 1, 9];
greater_than_5 = find(v > 5);  % Find indices of elements greater than 5
equal_to_2 = find(v == 2);  % Find indices of elements equal to 2
disp(greater_than_5)  % Output: 1 4 5
disp(equal_to_2)  % Output: 2
```

Remember, the `find` function is a powerful tool for manipulating vectors in MATLAB. Explore the documentation [https://www.mathworks.com/help/matlab/ref/find.html](https://www.mathworks.com/help/matlab/ref/find.html) for more details and advanced usage scenarios.

### 9. fix(x)
### 10. floor
### 11. ceil
### 12. round
### 13. sort
### 14. mod

The `mod` function in MATLAB is useful for finding the remainder after element-wise division of vectors. Here are some examples of how to use it with vectors:

**1. Modulo with a Scalar:**

* This calculates the remainder for each element of the vector divided by the scalar value.

**Example:**

```matlab
v = [10, 5, 18, 3, 12];
mod_result = mod(v, 4);  % Find remainder after dividing each element by 4
disp(mod_result)  % Output: 2 1 2 3 0
```

**2. Modulo Between Vectors:**

* You can perform modulo between two vectors of the same size. The operation is performed element-wise.

**Example:**

```matlab
v1 = [7, 11, 15];
v2 = [3, 4, 5];
mod_result = mod(v1, v2);
disp(mod_result)  % Output: 1 3 0 (Remainder of v1(i) / v2(i))
```

**Key points:**

* The `mod` function follows the convention that `mod(a,0) returns a`. In other words, the remainder when dividing by zero is the original dividend itself.
* For floating-point input arguments, the output data type of `mod` is the same as the inputs.

By understanding these examples, you can effectively use the `mod` function to perform modulo operations on vectors in MATLAB.

### 15. rem

The `rem` function in MATLAB behaves very similarly to `mod` for vectors, but with a subtle difference. Here's how to use it with vectors:

**1. Rem with a Scalar:**

* This calculates the remainder for each element of the vector divided by the scalar value.

**Example:**

```matlab
v = [10, 5, 18, 3, 12];
rem_result = rem(v, 4);  % Find remainder after dividing each element by 4
disp(rem_result)  % Output: 2 1 2 3 0
```

**2. Rem Between Vectors:**

* You can perform element-wise modulo between two vectors of the same size.

**Example:**

```matlab
v1 = [7, 11, 15];
v2 = [3, 4, 5];
rem_result = rem(v1, v2);
disp(rem_result)  % Output: 1 3 0 (Remainder of v1(i) / v2(i))
```

**3. Key Difference from mod:**

* The key difference between `rem` and `mod` lies in the handling of negative dividends. 
    * `mod` always returns a non-negative remainder between 0 and the divisor minus one. 
    * `rem` however, signs the remainder according to the sign of the dividend.

**Example:**

```matlab
v = [-10, 5, -18, 3, -12];
rem_result = rem(v, 4);  % Remainder considering sign of dividend
disp(rem_result)  % Output: -2 1 -2 3 -0
```
## Matrices

### Creating Matrices: Entering elements directly

**Example #:** Creating a 2x2 Matrix

```matlab
A = [1 2; 3 4];
disp(A);
```
This creates a 2x2 matrix `A` with elements:
```
1  2
3  4
```

**Example #:** Creating a 3x3 Matrix
```matlab
% Create a 3x3 matrix
matrix = [1 2 3; 4 5 6; 7 8 9]
```

**Example #:** Create a 2x3 matrix

```matlab
C = [1 2 3; 4 5 6]
```

**Example #:** Specifying elements with spaces or commas

Elements within a row can be separated by either commas ( , ) or spaces. Both notations achieve the same result.

```matlab
% Using commas
matrix_comma = [1, 4, 7; 2, 5, 8; 3, 6, 9]

% Using spaces
matrix_space = [1 4 7; 2 5 8; 3 6 9]
```

In MATLAB, you can create matrices by entering elements directly. Here are some examples:


**Example #:** Creating a 4x2 Matrix
```matlab
C = [2, 4; 6, 8; 10, 12; 14, 16];
```
This creates a 4x2 matrix `C` with elements:
```
2   4
6   8
10  12
14  16
```

**Example #:** Creating a 3x4 Matrix
```matlab
D = [1, 2, 3, 4; 5, 6, 7, 8; 9, 10, 11, 12];
```
This creates a 3x4 matrix `D` with elements:
```
1   2   3   4
5   6   7   8
9   10  11  12
```

**Example #:** Creating a 1x5 Row Vector
```matlab
E = [1, 2, 3, 4, 5];
```
This creates a 1x5 row vector `E` with elements:
```
1   2   3   4   5
```

**Example #:** Creating a 5x1 Column Vector:
```matlab
F = [6; 7; 8; 9; 10];
```
This creates a 5x1 column vector `F` with elements:
```
6
7
8
9
10
```

**See also:**
- [Creating Matrices and Arrays - MathWorks Help Center](https://www.mathworks.com/help/matlabmobile/ug/creating-matrices-and-arrays.html)
  
### Matrix Indexing in MATLAB


## Key Terms

## True/False (Mark T for True and F for False)

**Answer Key (True/False):**

## Multiple Choice (Select the best answer)

## Fill in the Blanks

**Answer Key (Fill in the Blanks):**

## Practice Exercises

1. Create a vector of your favorite numbers and access the third element.
2. Create a vector of temperatures and extract the elements for Monday and Wednesday (assuming even indices represent Wednesdays).
3. Experiment with the colon operator to create sub-vectors with different intervals.

## Review Questions

## References and Bibliography

[1] “M.2 Matrix Arithmetic | STAT ONLINE,” PennState: Statistics Online Courses. https://online.stat.psu.edu/statprogram/reviews/matrix-algebra/arithmetic
‌
