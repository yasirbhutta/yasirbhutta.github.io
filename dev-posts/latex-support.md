# Adding LaTeX Support to GitHub Pages

GitHub Pages doesn't natively support LaTeX rendering, but you can add it using JavaScript libraries. Here are the best methods to enable LaTeX math formula rendering on your GitHub Pages site:

## Method 1: Using MathJax (Recommended)

### Step 1: Add MathJax to your HTML
Include this script in your `<head>` section or before closing `</body>`:

```html
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
```

### Step 2: Write LaTeX in your Markdown
Use standard LaTeX delimiters:
- Inline math: `\( ... \)` or `$ ... $`
- Display math: `\[ ... \]` or `$$ ... $$`

Example:
```markdown
When \(a \ne 0\), there are two solutions to \(ax^2 + bx + c = 0\) and they are:
$$x = {-b \pm \sqrt{b^2-4ac} \over 2a}$$
```

## Method 2: Using Katex (Lighter Alternative)

### Step 1: Add Katex to your HTML
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js" 
    onload="renderMathInElement(document.body);"></script>
```

### Step 2: Configure Katex (optional)
Add this script to customize delimiters:
```html
<script>
    document.addEventListener("DOMContentLoaded", function() {
        renderMathInElement(document.body, {
            delimiters: [
                {left: '$$', right: '$$', display: true},
                {left: '$', right: '$', display: false},
                {left: '\\(', right: '\\)', display: false},
                {left: '\\[', right: '\\]', display: true}
            ],
            throwOnError: false
        });
    });
</script>
```

## Method 3: For Jekyll Sites

If you're using Jekyll, add this to `_config.yml`:

```yaml
markdown: kramdown
kramdown:
  math_engine: mathjax
```

Then add the MathJax script as shown in Method 1.

## Testing Your Setup

Create a test post with:

```markdown
Here's an inline formula: \(E = mc^2\)

And a displayed equation:

$$\int_{-\infty}^\infty e^{-x^2} dx = \sqrt{\pi}$$
```

## Troubleshooting

1. **Equations not rendering?**
   - Check browser console for errors
   - Ensure scripts are loading (no ad blockers interfering)
   - Verify correct delimiters are used

2. **For GitHub Markdown preview:**
   - The preview won't show rendered equations
   - They'll only render when published

3. **Performance considerations:**
   - MathJax is full-featured but heavier
   - KaTeX is faster but has fewer features

Would you like me to provide specific instructions for a particular static site generator you're using with GitHub Pages?

# LaTeX Examples for Beginners

Here's a collection of basic LaTeX examples to help you get started with mathematical typesetting. These examples work in most LaTeX environments including Overleaf, academic papers, and GitHub Pages with MathJax/Katex support.

## Basic Syntax

### 1. Inline vs Display Math

**Inline math** (in a sentence):
```latex
Einstein's famous equation is \(E = mc^2\) which relates energy and mass.
```
or with dollar signs:
```latex
Einstein's famous equation is $E = mc^2$ which relates energy and mass.
```

**Display math** (centered on its own line):
```latex
The quadratic formula is:
\[ x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} \]
```
or with double dollar signs:
```latex
The quadratic formula is:
$$ x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} $$
```

## Common Mathematical Expressions

### 2. Fractions
```latex
$\frac{1}{2}$ hour is 30 minutes

Displayed fraction:
\[ \frac{x+1}{x-1} \]
```

### 3. Superscripts and Subscripts
```latex
$x^2 + y^2 = z^2$

Chemical formula: $H_2O$

Combination: $x_i^{2n}$
```

### 4. Greek Letters
```latex
$\alpha, \beta, \gamma, \Gamma, \pi, \Pi, \Omega$
```

### 5. Sums, Products, and Integrals
```latex
Summation: $\sum_{i=1}^n i^2 = \frac{n(n+1)(2n+1)}{6}$

Product: $\prod_{i=1}^n (x_i + 1)$

Integral: $\int_0^1 x^2 \, dx = \frac{1}{3}$

Double integral: $\iint_D f(x,y) \, dx\,dy$
```

### 6. Matrices
```latex
\[
\begin{matrix}
a & b \\
c & d 
\end{matrix}
\quad
\begin{pmatrix}
a & b \\
c & d 
\end{pmatrix}
\quad
\begin{bmatrix}
1 & 2 \\
3 & 4 
\end{bmatrix}
\]
```

### 7. Cases (Piecewise Functions)
```latex
\[
|x| = 
\begin{cases} 
x & \text{if } x \geq 0 \\
-x & \text{if } x < 0 
\end{cases}
\]
```

## Formatting Text in Math Mode

### 8. Text Inside Equations
```latex
\[ \text{Area} = \pi r^2 \text{ where } r \text{ is the radius} \]
```

### 9. Bold and Special Symbols
```latex
$\mathbf{Ax} = \mathbf{b}$ (bold for vectors/matrices)

$\mathbb{R}$ (real numbers), $\mathbb{Z}$ (integers)

$\mathcal{L}$ (Lagrangian), $\mathscr{H}$ (Hamiltonian)
```

## Aligned Equations

### 10. Equation Alignment
```latex
\[
\begin{align*}
(x+1)^2 &= (x+1)(x+1) \\
&= x^2 + x + x + 1 \\
&= x^2 + 2x + 1
\end{align*}
\]
```

## Common Symbols

### 11. Relational Operators
```latex
$=, \neq, \approx, \equiv, \leq, \geq, \subset, \subseteq, \in$
```

### 12. Arrows
```latex
$\rightarrow, \Rightarrow, \leftrightarrow, \Leftrightarrow, \mapsto$
```

### 13. Dots
```latex
$1, 2, \ldots, n$ (horizontal dots)

$\vdots$ (vertical dots)

$\ddots$ (diagonal dots)
```

## Physics Examples

### 14. Basic Physics Equations
```latex
Newton's second law: $\mathbf{F} = m\mathbf{a}$

Schrödinger equation: $i\hbar\frac{\partial}{\partial t}\Psi = \hat{H}\Psi$

Maxwell's equations:
\[
\begin{aligned}
\nabla \cdot \mathbf{E} &= \frac{\rho}{\epsilon_0} \\
\nabla \times \mathbf{E} &= -\frac{\partial \mathbf{B}}{\partial t}
\end{aligned}
\]
```

## Chemistry Examples

### 15. Chemical Equations
```latex
Chemical reaction: $2H_2 + O_2 \rightarrow 2H_2O$

Equilibrium: $A + B \rightleftharpoons C$

Rate equation: $v = k[A]^m[B]^n$
```

## Tips for Beginners

1. Always match your delimiters (`\( \)`, `$ $`, `\[ \]`)
2. Use spaces around LaTeX code in text for better readability: `We have $x=1$ and $y=2$`
3. Escape special characters with backslash: `\{`, `\}`, `\$`
4. For complex expressions, build them piece by piece
5. Use online editors like Overleaf to practice

Would you like me to provide examples for any specific mathematical area (calculus, linear algebra, statistics, etc.)?