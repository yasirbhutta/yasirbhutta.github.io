# MATLAB: Polynomials

Connect with me: [Youtube](https://www.youtube.com/yasirbhutta) \| [LinkedIn](https://www.linkedin.com/in/yasirbhutta/) \| [WhatsApp Channel](https://whatsapp.com/channel/0029VaC3BC160eBZZSs3CW0c) \| [Web](https://yasirbhutta.github.io/) \| [Facebook](https://www.facebook.com/yasirbhutta786) \| [Twitter](https://twitter.com/yasirbhutta)

- [Download PDF](polynomials.pdf)  
- To access the updated handouts, please click on the following link:
[index.html](../yasirbhutta.github.io/index.md)


**Polynomial:** A polynomial is an expression consisting of variables (usually denoted by x) raised to non-negative integer powers (like x^2, x^3, etc.), combined with coefficients (numerical values) using addition, subtraction, and multiplication.

## 4.6 Polynomial Multiplication

**Example:** Multiply 2x^2 × 3x

```matlab
x = [2 0 0];
y = [3 0];

z = conv(x,y);
disp(z);
```

**Output:**
```
6     0     0     0
```

The polynomial is **6x^3**

**See also:**

- [Multiplying Polynomials - byjus.com](https://byjus.com/maths/multiplying-polynomials/)
- [Multiplying Polynomials - libretexts.org](https://math.libretexts.org/Bookshelves/Algebra/Beginning_Algebra/05%3A_Polynomials_and_Their_Operations/5.04%3A_Multiplying_Polynomials)

## 4.7 Polynomial DIVISION

**See also:**

- [Polynomial division - byjus.com](https://byjus.com/maths/polynomial-division/)


## 4.8 Formulation of polynomial equation

## 4.9 Characteristic polynomial of a matrix

The characteristic polynomial, in linear algebra, is a polynomial associated with a square matrix. It has several key properties:

**Eigenvalue Relationship:** The eigenvalues of the matrix are the values that make the characteristic polynomial equal to zero. In other words, the roots of the polynomial correspond to the eigenvalues.
**Degree and Size:** The characteristic polynomial is a polynomial of degree n, where n is the dimension of the square matrix. This implies that an n x n matrix can have at most n distinct eigenvalues.

## 4.11 Polynomial Integration

**Polynomial:** A polynomial is an expression consisting of variables (usually denoted by x) raised to non-negative integer powers (like x^2, x^3, etc.), combined with coefficients (numerical values) using addition, subtraction, and multiplication.

**Derivative:** In calculus, the derivative of a function represents the instantaneous rate of change of that function at a specific point. For polynomials, it tells you how fast the polynomial's value changes as its input (x) changes.

## Key Terms

## True/False (Mark T for True and F for False)

1. In MATLAB, polynomial coefficients are stored as a row vector with powers in ascending order. 
2. The conv function in MATLAB is used for polynomial division. 
3. The polyder function in MATLAB is used to find the integral of a polynomial. (T/F)


**Answer Key (True/False):**

1. False
2. False
3. False

## Multiple Choice (Select the best answer)

> In MATLAB, how are polynomial coefficients stored?

- (a) As a column vector with powers in ascending order.
- (b) As a row vector with powers in descending order.
- (c) As a matrix with coefficients on the diagonal.
- (d) None of the above.

> How can you evaluate a polynomial for a specific input value in MATLAB?

- (a) By directly substituting the value into the polynomial - expression.
- (b) Using the polyval(p, x) function, where p is the polynomi- al object and x is the input value. ** <-- Correct Answer**
- (c) The roots(p) function cannot be used for evaluation.
- (d) None of the above.

> Which function is used for polynomial multiplication in MATLAB?

- (a) mult(p1, p2)
- (b) polyprod(p1, p2)
- (c) conv(p1, p2) ** <-- Correct Answer (Convolution is used for poly- nomial multiplication)**
- (d) None of the above.

> How are polynomial coefficients stored in a MATLAB variable?
- a) As a column vector with powers in ascending order.
- b) As a row vector with powers in descending order. CORRECT
- c) As a matrix with rows representing coefficients and columns - representing powers.
- d) None of the above.

> Which MATLAB function evaluates a polynomial for a specific input value?
- a) poly(p)
- b) polyder(p)
- c) polyint(p)
- d) polyval(p, x) CORRECT (where x is the input value)

> The following code snippet p = [2 1 -3]; polyval(p, 2) will evaluate to:
- a) The value of x where the polynomial equals 2.
- b) The derivative of the polynomial evaluated at x = 2.
- c) The integral of the polynomial from 0 to 2.
- d) The value of the polynomial when x = 2. CORRECT (p = [2 1 -3] represents a polynomial, polyval evaluates it at x = 2)

> Which MATLAB function finds the derivative of a polynomial p?
- a) polydiv(p)
- b) polyint(p)
- c) polyder(p) CORRECT
- d) polyval(p, 1)

> When defining a polynomial with missing terms (e.g., x^3 + 2x + 1), you should:
- a) Leave gaps in the coefficient vector.
- b) Insert zeros at the corresponding positions in the vector. - CORRECT
- c) Define separate polynomials for each term.
- d) It is not possible to define such polynomials in MATLAB.

> Which function is used to find the roots of a polynomial in MATLAB?

- A) polyfit
- B) roots
- C) polyval
- D) conv

> Which function evaluates a polynomial for a given set of x values?

- A) polyfit
- B) polyval
- C) polyder
- D) conv

> What does the polyder function do?

- A) Finds the derivative of a polynomial
- B) Integrates a polynomial
- C) Multiplies two polynomials
- D) Fits a polynomial to data

> Given p = [2 -4 3], what is the result of polyval(p, 2)?

- A) 1
- B) 3
- C) 0
- D) 2

> To perform polynomial division, which function is used in MATLAB?

- A) deconv
- B) conv
- C) polyval
- D) roots

> Which MATLAB command converts a vector of roots back to polynomial coefficients?

- A) roots
- B) poly
- C) polyval
- D) conv

> What is the result of the MATLAB command polyval([1 -4 4], 3)?

- A) 5
- B) 7
- C) 4
- D) 1

> Given p = [1 -6 11 -6], what command finds its roots?

- A) poly(p)
- B) polyfit(p)
- C) roots(p)
- D) polyval(p)

> Given a polynomial p = [2 0 -5 1], how can you find its value at x = -1?

- A) polyval(p, -1)
- B) polyfit(p, -1)
- C) conv(p, -1)
- D) roots(p, -1)

> How do you add two polynomials in MATLAB?

- A) Add their coefficient vectors
- B) Use conv() function
- C) Use polyval() fu- nction
- D) Add them directl- y

> What is the degree of the polynomial represented by the coefficient vector [4, 0, 2, 1]?

- A) 3
- B) 2
- C) 4
- D) 1

The degree of polynomials in one variable is the highest power of the variable in the algebraic expression. For example, in the following equation: x2+2x+4. The degree of the equation is 2 . i.e. the highest power of variable in the equation. [Learn more ...](https://www.toppr.com/guides/maths/polynomials/degree-of-polynomials/)

## Fill in the Blanks

**Answer Key (Fill in the Blanks):**

## Exercises

1. Define a polynomial \( p(x) = 3x^4 - 2x^3 + x - 5 \) in MATLAB and find its value at \( x = 2 \).
2. Use the `conv` function to multiply the polynomials \( 2x^2 + 3x + 1 \) and \( x^2 - 2x + 4 \).
3. Find the roots of the polynomial \( x^3 - 6x^2 + 11x - 6 \) using MATLAB.
4. Given the polynomial \( p(x) = 4x^3 - 3x^2 + 2x - 1 \), find its derivative using MATLAB.

These questions cover key concepts about polynomials in MATLAB, ensuring a comprehensive review of the material provided.

## Review Questions

- What is the purpose of evaluating a polynomial at a specific value? Describe how the polyval function is used in MATLAB for this purpose.
- What are the roots of a polynomial, and why are they significant? How does MATLAB's roots function find the roots of a polynomial?

## References and Bibliography