---
layout: default
title: Beginner’s Guide to Jekyll- Understanding Nested Layouts for Static Websites.
description: Learn how to use nested layouts in Jekyll to build flexible and reusable templates for static websites. This beginner-friendly guide includes examples, folder structure, and step-by-step instructions.
---

# 🔄 What is a Nested Layout?

Nested layouts let you **stack multiple layouts**, so a layout can be based on another layout.

### 💡 Analogy:
Think of `default.html` as the **main frame**, and `fix-mistakes.html` as a **template inside that frame**.

---

## 🧱 Folder Structure

```
_layouts/
├── default.html
└── fix-mistakes.html
```

---

## 📄 1. `default.html` — Base Layout

This layout includes common HTML structure: header, footer, etc.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{{ page.title }}</title>
</head>
<body>
  <header>
    <h1>My Jekyll Site</h1>
  </header>

  <main>
    {{ content }}  <!-- Injects the child layout's content here -->
  </main>

  <footer>
    <p>© 2025 MySite</p>
  </footer>
</body>
</html>
```

---

## 📄 2. `fix-mistakes.html` — Child Layout

This layout inherits from `default.html` and provides specific content for “fix-mistakes” pages.

```liquid
---
layout: default
---

<h2>{{ page.title }}</h2>
<p>{{ page.description }}</p>

<h3>Code with Mistakes:</h3>
<pre><code>{{ page.buggy_code | escape }}</code></pre>

<h3>Mistakes:</h3>
<ul>
  {% for mistake in page.mistakes %}
    <li>{{ mistake }}</li>
  {% endfor %}
</ul>

<h3>Corrected Code:</h3>
<pre><code>{{ page.corrected_code | escape }}</code></pre>
```

This becomes the **`{{ content }}`** block in `default.html`.

---

## 📄 3. Markdown Page Using `fix-mistakes` Layout

```markdown
---
layout: fix-mistakes
title: Debug Python Class
description: A quick exercise to debug constructor and method mistakes in a Python class.
buggy_code: |
  class Person:
      def __init__(name, age):
          name = name
          age = age
      def greet():
          print("Hi, I'm " + self.name)
  person1 = Person("Alice", 30)
  person1.greet()
mistakes:
  - "`self` missing in constructor"
  - "`self.name = name` not used"
  - "`self` missing in greet method"
corrected_code: |
  class Person:
      def __init__(self, name, age):
          self.name = name
          self.age = age
      def greet(self):
          print("Hi, I'm " + self.name)
  person1 = Person("Alice", 30)
  person1.greet()
---
```

---

## ✅ Why Use Nested Layouts?

- **DRY**: Don’t Repeat Yourself — `default` handles site-wide structure.
- **Flexibility**: Create specialized layouts (e.g., quizzes, tutorials, posts) that still follow the main design.
- **Cleaner templates**: Easier to maintain.

---

Want to go further? You can also nest more levels or combine with `{% include %}` for partials like reusable hints, navs, or quiz blocks. Want an example of that too?