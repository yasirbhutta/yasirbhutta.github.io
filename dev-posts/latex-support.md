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