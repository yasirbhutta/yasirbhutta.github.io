# Micrsoft Excel Articles

## Beginners

- [Install Excel App on Android Phone - Mobile Me Excel Kaise Chalaye](install-excel-android.md)

{% assign beginner_posts = site.pages | where_exp: "post", "post.path contains 'ms-excel/posts' and post.category == 'beginners'" %}
{% for post in beginner_posts %}
- [{{ post.title }}]({{ post.url }})
{% endfor %}

## Intermediate

## Advanced  