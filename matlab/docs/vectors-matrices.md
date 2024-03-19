# MATLAB: Vectors and Matrices


## Vector Products

**Important:** To perform matrix multiplication, the first matrix must have the same number of columns as the second matrix has rows. The number of rows of the resulting matrix equals the number of rows of the first matrix, and the number of columns of the resulting matrix equals the number of columns of the second matrix. [1]


**Important:** In MATLAB, the concept of conjugate refers to the complex conjugate of a number or element within a matrix. The complex conjugate of a complex number is a new number with the same real part but the imaginary part negated.

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

## Key Terms

## True/False (Mark T for True and F for False)

**Answer Key (True/False):**

## Multiple Choice (Select the best answer)

## Fill in the Blanks

**Answer Key (Fill in the Blanks):**

## Exercises

## Review Questions

## References and Bibliography

[1] “M.2 Matrix Arithmetic | STAT ONLINE,” PennState: Statistics Online Courses. https://online.stat.psu.edu/statprogram/reviews/matrix-algebra/arithmetic
‌
