---
layout: default
---

<h1>Microsoft Excel Articles</h1>

<h2>Beginners</h2>

{% assign beginner_posts = site.posts | where_exp: "post", "post.categories contains 'beginners'" %}
{% assign beginner_posts = beginner_posts | where_exp: "post", "post.categories contains 'ms-excel'" %}
{% for post in beginner_posts %}
- [{{ post.title }}]({{ site.url }}{{ post.url }})
{% endfor %}

<h2>Intermediate</h2>

<h3>Advanced</h3>