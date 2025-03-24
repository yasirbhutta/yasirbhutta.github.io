# CSS text Styling

## Fundamental text and font styling

### Fonts

#### Color

- The color property describes the foreground color of an element's text content.

**Syntax:***
```css
color: [color keywords](http://www.w3.org/TR/css3-color/#html4) | [color values](http://www.w3.org/TR/css3-color/#numerical)
```

```html
Here's a simple example of how to use the CSS `color` property for beginners:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Color Property Example</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }

        .red-text {
            color: red;
        }

        .blue-text {
            color: blue;
        }

        .green-text {
            color: green;
        }

        .hex-color {
            color: #ff5733; /* Hex code */
        }

        .rgb-color {
            color: rgb(255, 165, 0); /* RGB code */
        }

        .hsl-color {
            color: hsl(120, 100%, 25%); /* HSL code */
        }
    </style>
</head>
<body>

    <h1>CSS Color Property Example</h1>

    <p class="red-text">This text is red.</p>
    <p class="blue-text">This text is blue.</p>
    <p class="green-text">This text is green.</p>
    <p class="hex-color">This text uses a hex color (#ff5733).</p>
    <p class="rgb-color">This text uses an RGB color (rgb(255, 165, 0)).</p>
    <p class="hsl-color">This text uses an HSL color (hsl(120, 100%, 25%)).</p>

</body>
</html>
```
You can find the finished example on [GitHub](https://yasirbhutta.github.io/html-css-examples/css/text-styling/text-color2.html) (see also the [source code](https://github.com/yasirbhutta/html-css-examples/blob/main/css/text-styling/text-color2.html).

**Explanation:**

- `color: red;` → Uses a color name.
- `color: #ff5733;` → Uses a hex code.
- `color: rgb(255, 165, 0);` → Uses an RGB color format.
- `color: hsl(120, 100%, 25%);` → Uses an HSL color format.



#### Font families

- To set a different font for your text, you use the font-family property — this allows you to specify a font (or list of fonts) for the browser to apply to the selected elements. 
- The browser will only apply a font if it is available on the machine the website is being accessed on; if not, it will just use a browser default font.[1]

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Font Family Example</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }

        .serif {
            font-family: "Times New Roman", Times, serif;
        }

        .monospace {
            font-family: "Courier New", Courier, monospace;
        }

        .cursive {
            font-family: "Brush Script MT", cursive;
        }
    </style>
</head>
<body>

    <h1>Font Family Example</h1>

    <p>This is the default font (Arial, sans-serif).</p>

    <p class="serif">This is a serif font (Times New Roman).</p>

    <p class="monospace">This is a monospace font (Courier New).</p>

    <p class="cursive">This is a cursive font (Brush Script MT).</p>

</body>
</html>
```

You can find the finished example on [GitHub](https://yasirbhutta.github.io/html-css-examples/css/text-styling/font-family.html) (see also the [source code](https://github.com/yasirbhutta/html-css-examples/blob/main/css/text-styling/font-family.html).

- A `system font` or `web-safe` font is one that’s already assumed to be on the vast majority of users’ devices, with no need for a web font to be downloaded. [2] 
- This means that when a website uses a web-safe font, there's a high probability that it will display correctly for most visitors, regardless of their device or operating system. [3]

A "font stack" in web development is essentially a list of font names that a web browser uses to determine which font to display on a webpage. It's a crucial part of CSS (Cascading Style Sheets) that ensures your website's text remains readable and visually consistent, even if a user's computer doesn't have your preferred font. [4]

#### Font size

The `font-size` property in CSS determines the size of the text on a webpage. Understanding how to use this property is fundamental for controlling typography in web design. Here's a beginner-friendly example demonstrating various ways to set font sizes:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS Font Size Example</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }

        .absolute-size {
            font-size: 16px; /* Absolute size in pixels */
        }

        .relative-size {
            font-size: 1.5em; /* Relative size based on parent element */
        }

        .percentage-size {
            font-size: 120%; /* Percentage of parent element's font size */
        }

        .keyword-size {
            font-size: large; /* Predefined keyword */
        }
    </style>
</head>
<body>

    <h1>CSS Font Size Examples</h1>

    <p class="absolute-size">This text has an absolute font size of 16 pixels.</p>

    <p class="relative-size">This text has a relative font size of 1.5em, which is 1.5 times the size of its parent element's font size.</p>

    <p class="percentage-size">This text has a font size set to 120% of its parent element's font size.</p>

    <p class="keyword-size">This text uses the predefined keyword "large" for its font size.</p>

</body>
</html>
```

You can find the finished example on [GitHub](https://yasirbhutta.github.io/html-css-examples/css/text-styling/font-size.html) (see also the [source code](https://github.com/yasirbhutta/html-css-examples/blob/main/css/text-styling/font-size.html).

**Explanation:**

- `.absolute-size`: Sets the font size to a fixed value using pixels (`px`). For example, `font-size: 16px;` sets the text to 16 pixels.

- `.relative-size`: Uses the `em` unit to set the font size relative to the parent element's font size. For instance, `font-size: 1.5em;` makes the text 1.5 times larger than its parent element's font size.

- `.percentage-size`: Specifies the font size as a percentage of the parent element's font size. For example, `font-size: 120%;` sets the text to 120% of the parent element's font size.

- `.keyword-size`: Utilizes predefined keywords like `small`, `medium`, `large`, etc., to set the font size. In this case, `font-size: large;` applies a font size larger than the default.

For a comprehensive list of predefined keywords and more details on the `font-size` property, you can refer to the [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/font-size) and [W3Schools](https://www.w3schools.com/cssref/pr_font_font-size.php).

**See also:**

- [font-size - CSS: Cascading Style Sheets - MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/font-size)

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1602443888929206"
     crossorigin="anonymous"></script>
<ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-1602443888929206"
     data-ad-slot="6296238623"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

#### Font style, font weight, text transform, and text decoration

Understanding CSS properties like `font-style`, `font-weight`, `text-transform`, and `text-decoration` is essential for styling text on web pages. Here's a beginner-friendly example demonstrating how to use these properties:

**Syntax:** 

```css
font-style: normal;
font-style: italic;  /* Makes text italic */

/* <font-weight-absolute> keyword values */
font-weight: normal;
font-weight: bold; /* Makes text bold */

/* Keyword values */
text-transform: none;
text-transform: capitalize; /* Capitalizes the first letter of each word */
text-transform: uppercase;
text-transform: lowercase;

text-decoration: underline;
text-decoration: overline;
text-decoration: none;

text-decoration: underline dotted;
text-decoration: overline red;
text-decoration: underline dotted red;
text-decoration: green wavy underline;
text-decoration: underline overline #ff3028;


```
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS Text Styling Example</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }

        .italic-text {
            font-style: italic; /* Makes text italic */
        }

        .bold-text {
            font-weight: bold; /* Makes text bold */
        }

        .uppercase-text {
            text-transform: uppercase; /* Transforms text to uppercase */
        }

        .underline-text {
            text-decoration: underline; /* Underlines the text */
        }

        .combined-style {
            font-style: oblique; /* Makes text oblique */
            font-weight: 700; /* Sets font weight to 700 (bold) */
            text-transform: capitalize; /* Capitalizes the first letter of each word */
            text-decoration: line-through; /* Adds a line through the text */
        }
    </style>
</head>
<body>

    <h1>CSS Text Styling Examples</h1>

    <p class="italic-text">This text is italicized using the font-style property.</p>

    <p class="bold-text">This text is bold using the font-weight property.</p>

    <p class="uppercase-text">This text is transformed to uppercase using the text-transform property.</p>

    <p class="underline-text">This text is underlined using the text-decoration property.</p>

    <p class="combined-style">This text combines multiple styles: oblique, bold, capitalized, and line-through.</p>

</body>
</html>
```

You can find the finished example on [GitHub](https://yasirbhutta.github.io/html-css-examples/css/text-styling/font-style.html) (see also the [source code](https://github.com/yasirbhutta/html-css-examples/blob/main/css/text-styling/font-style.html).

**Explanation:**

- `.italic-text`: Applies the `font-style: italic;` property to italicize the text.

- `.bold-text`: Uses `font-weight: bold;` to make the text bold. The `font-weight` property can accept keywords like `normal`, `bold`, or numeric values ranging from 100 to 900, with higher numbers indicating thicker text. citeturn0search0

- `.uppercase-text`: Utilizes `text-transform: uppercase;` to convert all characters in the text to uppercase. The `text-transform` property can also be set to `lowercase` or `capitalize`, depending on the desired text transformation. citeturn0search2

- `.underline-text`: Applies `text-decoration: underline;` to underline the text. The `text-decoration` property can also be used to add other decorations like `overline`, `line-through`, or `none`.

- `.combined-style`: Demonstrates the use of multiple properties:
  - `font-style: oblique;` makes the text slanted.
  - `font-weight: 700;` sets the font weight to 700, which is typically bold. citeturn0search0
  - `text-transform: capitalize;` capitalizes the first letter of each word.
  - `text-decoration: line-through;` adds a line through the text.

**See also:**

- [https://developer.mozilla.org/en-US/docs/Web/CSS/font-style](https://developer.mozilla.org/en-US/docs/Web/CSS/font-style)
- [font-weight - CSS: Cascading Style Sheets - MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight)
- [text-transform - CSS: Cascading Style Sheets - MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/text-transform)
- [text-decoration - CSS: Cascading Style Sheets - MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/text-decoration)

#### Text drop shadows

The `text-shadow` property in CSS allows you to add shadow effects to text, enhancing its visual appeal. Here's a beginner-friendly example demonstrating how to apply text drop shadows:

```css
text-shadow: offset-x offset-y blur-radius color;

/* offset-x | offset-y | blur-radius | color */
text-shadow: 1px 1px 2px black;
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Text Shadow Example</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            padding: 20px;
        }

        .text-shadow {
            font-size: 36px;
            color: #333;
            text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);
        }
    </style>
</head>
<body>

    <h1 class="text-shadow">Hello, World!</h1>

</body>
</html>
```

You can find the finished example on [GitHub](https://yasirbhutta.github.io/html-css-examples/css/text-styling/text-shadow.html) (see also the [source code](https://github.com/yasirbhutta/html-css-examples/blob/main/css/text-styling/text-shadow.html).

**Explanation:**

- **HTML Structure:** The HTML consists of a basic structure with a `<head>` and `<body>`. Inside the `<body>`, there's an `<h1>` element with the class `text-shadow`.

- **CSS Styling:**
  - `body`: Sets the font to Arial, applies a light gray background color (`#f0f0f0`), and adds padding around the content.
  - `.text-shadow`: This class applies to the `<h1>` element:
    - `font-size: 36px;`: Sets the font size to 36 pixels.
    - `color: #333;`: Sets the text color to a dark gray.
    - `text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);`: Applies the shadow effect with the following parameters:
      - `2px`: Horizontal shadow offset (moves the shadow 2 pixels to the right).
      - `2px`: Vertical shadow offset (moves the shadow 2 pixels down).
      - `5px`: Blur radius (determines the sharpness of the shadow; higher values create a more blurred effect).
      - `rgba(0, 0, 0, 0.5)`: Shadow color in RGBA format, where `0.5` represents 50% opacity.

By adjusting these values, you can customize the shadow's position, blur intensity, and color to achieve the desired effect.

**See also:**

- For more details on the `text-shadow` property, refer to the [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/text-shadow).

- To explore various text shadow effects and get inspiration, check out these [CSS Text Shadow Effects](https://freefrontend.com/css-text-shadow-effects/).

### Text layout

#### Text alignment

Sure! Here's the **CSS `text-align`** syntax with all possible values included:  

### **Syntax:**
```css
selector {
  text-align: left | right | center | justify;
}
```

### **Possible Values:**
- **`left`** – Aligns text to the left.
- **`right`** – Aligns text to the right.
- **`center`** – Centers the text horizontally.
- **`justify`** – Stretches text so that all lines (except the last) have equal width.


```html
<!DOCTYPE html>
<html>
<head>
<title>Text Alignment Example</title>
<style>
  .left {
    text-align: left;
  }

  .center {
    text-align: center;
  }

  .right {
    text-align: right;
  }

  .justify {
    text-align: justify;
    width: 300px; /* needed for justify to be obvious */
    border: 1px solid black; /* add a border to see the effect */
    padding: 10px;
  }
</style>
</head>
<body>

  <h2 class="left">Left-aligned text</h2>
  <p class="left">This paragraph is left-aligned. Left alignment is the default for most languages.</p>

  <h2 class="center">Centered text</h2>
  <p class="center">This paragraph is centered. It's often used for headings or short pieces of text.</p>

  <h2 class="right">Right-aligned text</h2>
  <p class="right">This paragraph is right-aligned. Right alignment is used in some languages and for specific design purposes.</p>

  <h2 class="justify">Justified text</h2>
  <p class="justify">This paragraph is justified. Justification makes the text evenly spaced between the left and right margins. It's often used in newspapers and books to create a clean, blocky look. It looks best when the lines are relatively long. Here is a very long sentence to show the justify effect, by adding many more words, and words, and words, and even more words.</p>

</body>
</html>
```
You can find the finished example on [GitHub](https://yasirbhutta.github.io/html-css-examples/css/text-styling/text-align.html) (see also the [source code](https://github.com/yasirbhutta/html-css-examples/blob/main/css/text-styling/text-align.html).

**Explanation:**

* **`text-align`:**
    * This is a CSS property that controls how text is aligned within its container (like a paragraph or heading).
* **`left`:**
    * Aligns the text to the left edge of the container. This is the most common alignment.
* **`center`:**
    * Centers the text horizontally within the container.
* **`right`:**
    * Aligns the text to the right edge of the container.
* **`justify`:**
    * Stretches the text to fill the entire width of the container, creating even spacing between words. It adds spaces between words to make each line the same length.
* **HTML Structure:**
    * We use `<h2>` for headings and `<p>` for paragraphs to create different sections of text.
    * We use the class attribute to apply different css styles to each element.
* **CSS Styling:**
    * The `<style>` tag in the `<head>` section contains the CSS rules.
    * We use classes (`.left`, `.center`, `.right`, `.justify`) to apply specific alignments to the corresponding HTML elements.
    * The width and border that are added to the justify class, are added to make the justify effect more obvious.

#### Line height

The `line-height` property in CSS determines the vertical spacing between lines of text, significantly impacting the readability and visual appeal of your content. Here's a beginner-friendly example demonstrating how to use the `line-height` property:

In CSS, the `line-height` property controls the vertical spacing between lines of text.

### **Syntax:**
```css
selector {
  line-height: normal | <number> | <length> | <percentage>;
}
```

### **Possible Values:**
- **`normal`** (default) – Browser sets a reasonable line height.
- **`<number>`** – A unitless value that acts as a **multiplier** of the font size.  
  - Example: `line-height: 1.5;` (1.5 times the font size)
- **`<length>`** – A fixed value using px, em, rem, etc.  
  - Example: `line-height: 24px;`
- **`<percentage>`** – Sets the line height relative to the font size.  
  - Example: `line-height: 150%;` (1.5 times the font size)

### **Example Usage:**
```css
p {
  font-size: 16px;
  line-height: 1.5; /* 1.5 times the font size */
}

h1 {
  line-height: 120%; /* 1.2 times the font size */
}

span {
  line-height: 20px; /* Fixed height */
}
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS Line-Height Example</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }

        .normal-line-height {
            line-height: normal; /* Default line height */
        }

        .unitless-line-height {
            line-height: 1.5; /* 1.5 times the font size */
        }

        .length-line-height {
            line-height: 24px; /* Fixed line height of 24 pixels */
        }

        .percentage-line-height {
            line-height: 150%; /* 150% of the font size */
        }
    </style>
</head>
<body>

    <h1>CSS Line-Height Examples</h1>

    <p class="normal-line-height">
        This paragraph uses the default line height (normal). The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog.
    </p>

    <p class="unitless-line-height">
        This paragraph has a unitless line height of 1.5, meaning the line height is 1.5 times the font size. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog.
    </p>

    <p class="length-line-height">
        This paragraph has a fixed line height of 24 pixels. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog.
    </p>

    <p class="percentage-line-height">
        This paragraph has a line height set to 150% of the font size. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog.
    </p>

</body>
</html>
```
You can find the finished example on [GitHub](https://yasirbhutta.github.io/html-css-examples/css/text-styling/line-height.html) (see also the [source code](https://github.com/yasirbhutta/html-css-examples/blob/main/css/text-styling/line-height.html).

**Explanation:**

- **`.normal-line-height`**: Applies the default line height, which is typically about 1.2 times the font size but can vary depending on the browser and font used. 

- **`.unitless-line-height`**: Sets the line height to 1.5 times the font size. Using a unitless value ensures that the line height scales proportionally with the font size, maintaining consistent spacing. citeturn0search0

- **`.length-line-height`**: Specifies a fixed line height of 24 pixels, regardless of the font size. This approach can be useful when you need precise control over text layout. citeturn0search1

- **`.percentage-line-height`**: Sets the line height to 150% of the font size, effectively making it 1.5 times the font size. This method allows for relative spacing based on the font size. citeturn0search1

Adjusting the `line-height` property can significantly enhance the readability of your text by providing appropriate spacing between lines. Experimenting with different values will help you find the optimal line height for your specific design needs.

**See also:**

- [line-height MDN WEB DOCS](https://developer.mozilla.org/en-US/docs/Web/CSS/line-height)
- [CSS line-height Property - w3schools](https://www.w3schools.com/cssref/pr_dim_line-height.php?utm_source=chatgpt.com)

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1602443888929206"
     crossorigin="anonymous"></script>
<ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-1602443888929206"
     data-ad-slot="6296238623"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

#### Letter and word spacing

Adjusting letter and word spacing in CSS allows you to control the horizontal spacing between characters and words, enhancing the readability and visual appeal of your text. Here's a beginner-friendly example demonstrating how to use the `letter-spacing` and `word-spacing` properties:

In CSS, `letter-spacing` and `word-spacing` control the spacing between characters and words, respectively.

---

### **1. `letter-spacing` (Controls space between characters)**
#### **Syntax:**
```css
selector {
  letter-spacing: normal | <length>;
}
```
#### **Possible Values:**
- **`normal`** – Default spacing set by the browser.
- **`<length>`** – Specifies the space between characters (e.g., `px`, `em`, `%`).
  - **Positive values** increase spacing.
  - **Negative values** decrease spacing.

#### **Example:**
```css
p {
  letter-spacing: 2px; /* Adds 2px space between letters */
}

h1 {
  letter-spacing: -1px; /* Reduces space between letters */
}
```

---

### **2. `word-spacing` (Controls space between words)**

#### **Syntax:**
```css
selector {
  word-spacing: normal | <length>;
}
```
#### **Possible Values:**
- **`normal`** – Default spacing set by the browser.
- **`<length>`** – Specifies the space between words (e.g., `px`, `em`, `%`).
  - **Positive values** increase spacing.
  - **Negative values** decrease spacing.

#### **Example:**
```css
p {
  word-spacing: 5px; /* Adds 5px space between words */
}

h2 {
  word-spacing: -2px; /* Reduces space between words */
}
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS Letter and Word Spacing Example</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }

        .normal-spacing {
            letter-spacing: normal; /* Default letter spacing */
            word-spacing: normal;   /* Default word spacing */
        }

        .increased-letter-spacing {
            letter-spacing: 2px; /* Increases space between characters by 2 pixels */
        }

        .decreased-letter-spacing {
            letter-spacing: -1px; /* Decreases space between characters by 1 pixel */
        }

        .increased-word-spacing {
            word-spacing: 10px; /* Increases space between words by 10 pixels */
        }

        .decreased-word-spacing {
            word-spacing: -5px; /* Decreases space between words by 5 pixels */
        }
    </style>
</head>
<body>

    <h1>CSS Letter and Word Spacing Examples</h1>

    <p class="normal-spacing">
        This paragraph uses the default letter and word spacing. The quick brown fox jumps over the lazy dog.
    </p>

    <p class="increased-letter-spacing">
        This paragraph has increased letter spacing of 2 pixels. The quick brown fox jumps over the lazy dog.
    </p>

    <p class="decreased-letter-spacing">
        This paragraph has decreased letter spacing of 1 pixel. The quick brown fox jumps over the lazy dog.
    </p>

    <p class="increased-word-spacing">
        This paragraph has increased word spacing of 10 pixels. The quick brown fox jumps over the lazy dog.
    </p>

    <p class="decreased-word-spacing">
        This paragraph has decreased word spacing of 5 pixels. The quick brown fox jumps over the lazy dog.
    </p>

</body>
</html>
```
You can find the finished example on [GitHub](https://yasirbhutta.github.io/html-css-examples/css/text-styling/) (see also the [source code](https://github.com/yasirbhutta/html-css-examples/blob/main/css/text-styling/).

**Explanation:**

- **`.normal-spacing`**: Applies the default spacing between letters and words using `letter-spacing: normal;` and `word-spacing: normal;`.

- **`.increased-letter-spacing`**: Increases the space between characters by 2 pixels with `letter-spacing: 2px;`.

- **`.decreased-letter-spacing`**: Decreases the space between characters by 1 pixel with `letter-spacing: -1px;`. Negative values bring characters closer together.

- **`.increased-word-spacing`**: Increases the space between words by 10 pixels using `word-spacing: 10px;`.

- **`.decreased-word-spacing`**: Decreases the space between words by 5 pixels with `word-spacing: -5px;`. Negative values reduce the space between words.

**See also:**

- For more details on the `letter-spacing` property, refer to the [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/letter-spacing).

- For more information on the `word-spacing` property, see the [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/word-spacing).

## Styling lists

In CSS, the `list-style-type` property defines the bullet or numbering style for list items in `<ul>` (unordered lists) and `<ol>` (ordered lists).  

---

### **Syntax:**

```css
selector {
  list-style-type: value;
}
```

---

### **Possible Values:**
#### **For Unordered Lists (`<ul>`)**
- **`disc`** (●) – Default bullet style.
- **`circle`** (○) – Hollow circle.
- **`square`** (■) – Square bullet.
- **`none`** – No bullets.

#### **For Ordered Lists (`<ol>`)**
- **`decimal`** (1, 2, 3, 4, ...)
- **`decimal-leading-zero`** (01, 02, 03, 04, ...)
- **`lower-roman`** (i, ii, iii, iv, ...)
- **`upper-roman`** (I, II, III, IV, ...)
- **`lower-alpha`** (a, b, c, d, ...)
- **`upper-alpha`** (A, B, C, D, ...)
- **`lower-greek`** (α, β, γ, δ, ...)
- **`lower-latin`** (a, b, c, d, ...)
- **`upper-latin`** (A, B, C, D, ...)

---

### **Example Usage:**
```css
ul {
  list-style-type: square; /* Square bullets */
}

ol {
  list-style-type: upper-roman; /* I, II, III, IV, ... */
}

ul.custom {
  list-style-type: none; /* Removes bullets */
}
```

### Bullet list styles

Customizing bullet styles in lists enhances the visual appeal and readability of your web content. Here's a beginner-friendly guide on how to style list bullets using CSS:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS Bullet Styles Example</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }

        /* Default bullet style */
        ul.default {
            list-style-type: disc;
        }

        /* Circle bullet style */
        ul.circle {
            list-style-type: circle;
        }

        /* Square bullet style */
        ul.square {
            list-style-type: square;
        }

        /* Custom image bullet style */
        ul.custom-image {
            list-style-image: url('https://example.com/custom-bullet.png');
        }

        /* Custom bullet color using ::marker pseudo-element */
        ul.custom-color li::marker {
            color: blue;
            font-size: 1.2em;
        }
    </style>
</head>
<body>

    <h1>CSS Bullet Styles Examples</h1>

    <h2>Default Bullet Style</h2>
    <ul class="default">
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
    </ul>

    <h2>Circle Bullet Style</h2>
    <ul class="circle">
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
    </ul>

    <h2>Square Bullet Style</h2>
    <ul class="square">
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
    </ul>

    <h2>Custom Image Bullet Style</h2>
    <ul class="custom-image">
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
    </ul>

    <h2>Custom Bullet Color</h2>
    <ul class="custom-color">
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
    </ul>

</body>
</html>
```
You can find the finished example on [GitHub](https://yasirbhutta.github.io/html-css-examples/css/text-styling/) (see also the [source code](https://github.com/yasirbhutta/html-css-examples/blob/main/css/text-styling/).

**Explanation:**

- **Default Bullet Style:** Uses the browser's default disc-shaped bullets.

- **Circle Bullet Style:** Applies the `list-style-type: circle;` property to display hollow circle bullets.

- **Square Bullet Style:** Uses `list-style-type: square;` to display square-shaped bullets.

- **Custom Image Bullet Style:** The `list-style-image` property allows the use of a custom image as the bullet. Replace `'https://example.com/custom-bullet.png'` with the URL of your desired bullet image.

### Order list styles

Styling ordered lists in HTML enhances their readability and aligns them with your website's design aesthetics. Here's a beginner-friendly guide on how to customize ordered list styles using CSS:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS Ordered List Styles Example</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }

        /* Default ordered list */
        ol.default {
            list-style-type: decimal; /* 1, 2, 3, ... */
        }

        /* Lowercase alphabetic list */
        ol.lower-alpha {
            list-style-type: lower-alpha; /* a, b, c, ... */
        }

        /* Uppercase alphabetic list */
        ol.upper-alpha {
            list-style-type: upper-alpha; /* A, B, C, ... */
        }

        /* Lowercase Roman numerals */
        ol.lower-roman {
            list-style-type: lower-roman; /* i, ii, iii, ... */
        }

        /* Uppercase Roman numerals */
        ol.upper-roman {
            list-style-type: upper-roman; /* I, II, III, ... */
        }

    </style>
</head>

<body>

    <h1>CSS Ordered List Styles Examples</h1>

    <h2>Default Ordered List</h2>
    <ol class="default">
        <li>First item</li>
        <li>Second item</li>
        <li>Third item</li>
    </ol>

    <h2>Lowercase Alphabetic List</h2>
    <ol class="lower-alpha">
        <li>First item</li>
        <li>Second item</li>
        <li>Third item</li>
    </ol>

    <h2>Uppercase Alphabetic List</h2>
    <ol class="upper-alpha">
        <li>First item</li>
        <li>Second item</li>
        <li>Third item</li>
    </ol>

    <h2>Lowercase Roman Numerals</h2>
    <ol class="lower-roman">
        <li>First item</li>
        <li>Second item</li>
        <li>Third item</li>
    </ol>

    <h2>Uppercase Roman Numerals</h2>
    <ol class="upper-roman">
        <li>First item</li>
        <li>Second item</li>
        <li>Third item</li>
    </ol>

</body>
</html>
```
You can find the finished example on [GitHub](https://yasirbhutta.github.io/html-css-examples/css/text-styling/) (see also the [source code](https://github.com/yasirbhutta/html-css-examples/blob/main/css/text-styling/).

**Explanation:**

- **Default Ordered List:** Uses the browser's default numbering style (1, 2, 3, ...).

- **Lowercase Alphabetic List:** Applies `list-style-type: lower-alpha;` to display items with lowercase letters (a, b, c, ...).

- **Uppercase Alphabetic List:** Uses `list-style-type: upper-alpha;` for uppercase letters (A, B, C, ...).

- **Lowercase Roman Numerals:** Sets `list-style-type: lower-roman;` to display items with lowercase Roman numerals (i, ii, iii, ...).

- **Uppercase Roman Numerals:** Applies `list-style-type: upper-roman;` for uppercase Roman numerals (I, II, III, ...).

You can find the finished example on [GitHub](https://yasirbhutta.github.io/html-css-examples/css/text-styling/order-list-styles.html) (see also the [source code](https://github.com/yasirbhutta/html-css-examples/blob/main/css/text-styling/order-list-styles.html).

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1602443888929206"
     crossorigin="anonymous"></script>
<ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-1602443888929206"
     data-ad-slot="6296238623"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

## Styling links

In CSS, links can be styled based on their various interaction states using pseudo-classes. The primary link states are:

1. **`a:link`**: A normal, unvisited link.
2. **`a:visited`**: A link the user has already visited.
3. **`a:hover`**: A link when the user hovers over it with the mouse.
4. **`a:active`**: A link at the moment it is clicked.
5. **`a:focus`**: A link that has been focused on, for example, through keyboard navigation.

It's crucial to define these pseudo-classes in a specific order to ensure styles are applied correctly: `:link`, `:visited`, `:hover`, `:focus`, and `:active`. citeturn0search4

Here's an example demonstrating how to style these different link states:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS Link States Example</title>
    <style>
        /* Unvisited link */
        a:link {
            color: blue;
            text-decoration: none;
        }

        /* Visited link */
        a:visited {
            color: purple;
        }

        /* Hovered link */
        a:hover {
            color: green;
            text-decoration: underline;
        }

        /* Focused link */
        a:focus {
            outline: 2px dashed orange;
        }

        /* Active link */
        a:active {
            color: red;
        }
    </style>
</head>
<body>

    <h1>CSS Link States Example</h1>
    <p><a href="https://www.example.com">Visit Example.com</a></p>

</body>
</html>
```
You can find the finished example on [GitHub](https://yasirbhutta.github.io/html-css-examples/css/text-styling/) (see also the [source code](https://github.com/yasirbhutta/html-css-examples/blob/main/css/text-styling/).

**Explanation:**

- **Unvisited Link (`a:link`)**: Sets the color to blue and removes the underline.
- **Visited Link (`a:visited`)**: Changes the color to purple for links that have been clicked before.
- **Hovered Link (`a:hover`)**: When a user hovers over the link, it turns green and underlines appear.
- **Focused Link (`a:focus`)**: Adds a dashed orange outline when the link is focused, aiding keyboard navigation.
- **Active Link (`a:active`)**: Changes the color to red at the moment the link is clicked.

By styling these link states, you enhance the user experience by providing visual feedback during interactions. Remember to follow the correct order of pseudo-classes to ensure styles are applied as intended.

---

### **Task: Create a Horizontal Navigation Menu using CSS**  

#### **Objective:**  
Create a horizontal navigation bar with five menu items using HTML and CSS. The menu should be visually appealing and responsive.  

#### **Requirements:**  
1. Use an unordered list (`<ul>`) to structure the menu.  
2. Each menu item should be inside a `<li>` element.  
3. Style the menu with CSS to ensure:  
   - The items are displayed horizontally.  
   - There is padding and margin to space out the items.  
   - The text color changes when hovered.  
4. The menu should have a background color.  
5. On hovering over a menu item, change the background color and text color.  

You can find the finished example on [GitHub](https://yasirbhutta.github.io/html-css-examples/posts/menu-using-css/index.html) (see also the [source code](https://github.com/yasirbhutta/html-css-examples/blob/main/posts/menu-using-css/index.html).

[Click here for the solution](../posts/navigation-menu-using-css.md)

## Key Terms

## True/False (Mark T for True and F for False)

**Answer Key (True/False):**

## Multiple Choice (Select the best answer)

1. **Which function would you use to determine the type of a variable in Python?**
   - A) id()
   - B) type()
   - C) str()
   - D) isinstance()
  
**Watch this video for the answer:**

**Answer key (Mutiple Choice):**

## Fill in the Blanks

**Answer Key (Fill in the Blanks):**

## Exercises

1. Skill Level Categories
Define clear categories based on skill levels, such as:

Beginner: Basic concepts and syntax.
Intermediate: More complex problems involving data structures and algorithms.
Advanced: Challenging problems that require in-depth understanding and optimization.

## Review Questions

**Answers to Review Questions:**

## References and Bibliography

- [1] “Fundamental text and font styling - Learn web development | MDN,” MDN Web Docs, Feb. 07, 2025. <https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Text_styling/Fundamentals>
- [2] “System font, or web-safe font – Fonts Knowledge,” Google Fonts. <https://fonts.google.com/knowledge/glossary/system_font_web_safe_font>
- [3] “Understand Web-Safe Fonts,” Higher Logic, Dec. 11, 2024. <https://support.higherlogic.com/hc/en-us/articles/360033055671-Understand-Web-Safe-Fonts> (accessed Mar. 19, 2025).
- [4] “Kickstart Digital,” Kickstart Digital, Jul. 09, 2024. <https://kickstartdigital.co.nz/marketing-content-terms/font-stack/> (accessed Mar. 19, 2025).
- [5] “CSS Basics: Styling Links Like a Boss,” CSS-Tricks, Feb. 15, 2018. <https://css-tricks.com/css-basics-styling-links-like-boss/>
‌
‌

