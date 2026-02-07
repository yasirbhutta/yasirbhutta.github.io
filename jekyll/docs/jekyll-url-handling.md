---
layout: page
title: Understanding URL Handling in Jekyll: Filters, Configs, and Best Practices
description: Learn how to handle URL in jekyll to filters and configure urls of static website.
keywords: "url, site, href, page, your, jekyll, example, blog"
---

# Understanding URL Handling in Jekyll: Filters, Configs, and Best Practices

In Jekyll, URLs are handled using the `url` and `relative_url` filters, and by using variables defined in your `_config.yml` file. Here's a quick rundown on how to use URLs in Jekyll:

---

### 🔗 1. **Basic Site URL Configuration**
In your `_config.yml`, you usually define:

```yaml
url: "https://example.com"      # your domain name
baseurl: "/blog"                # if your site is in a subdirectory ("" if in root)
```

---

### 🏷️ 2. **Using the `url` Filter**
This will convert a relative path into a full URL.

```liquid
<a href="{{ '/about/' | url }}">About</a>
```

**Output:**  
`https://example.com/blog/about/` (based on the config above)

---

### 🏠 2. **Site URL (`site.url`)**
This is typically set in your `_config.yml` file and represents the base URL of your site:

```yaml
# _config.yml
url: "https://example.com"
```

Then in your layouts or templates, you might use it like this:

```liquid
<a href="{{ site.url }}/about">About</a>
```

Or better yet, combine with `site.baseurl`:

```liquid
<a href="{{ site.url }}{{ site.baseurl }}/about">About</a>
```

---

### 📄 3. **Page/Post URL (`page.url`)**
This gives the relative URL of the current page or post. Example usage:

```liquid
<!-- Outputs something like: /blog/my-post/ -->
{{ page.url }}
```

This is useful for canonical links, social shares, or navigation highlighting.

---

### 💡 Example Use Case:
```liquid
<!-- Full link to the current page -->
<link rel="canonical" href="{{ site.url }}{{ page.url }}">
```

### 🔁 4. **Using the `relative_url` Filter**
This is safer for local development (doesn't include the domain):

```liquid
<a href="{{ '/about/' | relative_url }}">About</a>
```

**Output:**  
`/blog/about/`

---

### 🧠 5. **Linking to Posts or Pages**
You can also use built-in variables:

```liquid
<a href="{{ page.url | relative_url }}">{{ page.title }}</a>
```

Or for posts:

```liquid
<a href="{{ post.url | relative_url }}">{{ post.title }}</a>
```

---

### 🛠️ 6. **Linking Static Assets**
```liquid
<img src="{{ '/assets/images/logo.png' | relative_url }}" alt="Logo">
```

---

### ✅ Pro Tip:
If you're working in development (`jekyll serve`), `site.url` might be blank unless you set it. So you may want to guard against that in templates:

```liquid
{% if site.url %}
  <a href="{{ site.url }}{{ page.url }}">Permalink</a>
{% else %}
  <a href="{{ page.url }}">Permalink</a>
{% endif %}
```

---