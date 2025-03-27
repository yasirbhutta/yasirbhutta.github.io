# Common Python Class Attribute Mistakes and How to Fix Them

Sure! Let's consider another example to illustrate the misuse of class attributes and the correct approach. This time, we'll create a `Library` class where each library keeps track of its own collection of books.

## Mistaken Use of Class Attributes

### Incorrect Implementation

In this incorrect implementation, we mistakenly use a class attribute to store the books:

```python
class Library:
    # Class attribute (incorrect use for storing books)
    books = []

    def __init__(self, name):
        self.name = name

    def add_book(self, book):
        self.books.append(book)

    def get_books(self):
        return self.books

# Create instances of the Library class
library1 = Library("City Library")
library2 = Library("Community Library")

# Add books to each library
library1.add_book("1984")
library2.add_book("To Kill a Mockingbird")

# Print books in each library
print(f"{library1.name} books: {library1.get_books()}")
print(f"{library2.name} books: {library2.get_books()}")
```

### Output

```plaintext
City Library books: ['1984', 'To Kill a Mockingbird']
Community Library books: ['1984', 'To Kill a Mockingbird']
```

### Explanation

In this incorrect implementation, `books` is a class attribute. When `add_book` is called, it modifies the class attribute, which is shared among all instances of the `Library` class. As a result, both `library1` and `library2` end up sharing the same list of books.

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

## Correct Implementation

To fix this, we should use an instance attribute for storing books:

```python
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []  # Instance attribute

    def add_book(self, book):
        self.books.append(book)

    def get_books(self):
        return self.books

# Create instances of the Library class
library1 = Library("City Library")
library2 = Library("Community Library")

# Add books to each library
library1.add_book("1984")
library2.add_book("To Kill a Mockingbird")

# Print books in each library
print(f"{library1.name} books: {library1.get_books()}")
print(f"{library2.name} books: {library2.get_books()}")
```

### Output

```plaintext
City Library books: ['1984']
Community Library books: ['To Kill a Mockingbird']
```

### Explanation

In the correct implementation, `books` is an instance attribute, initialized within the `__init__` method. This ensures that each instance of `Library` has its own separate collection of books. When `add_book` is called, it modifies the instance's own list, not a shared list.

## Summary

The example shows how using class attributes for instance-specific data can lead to unintended sharing of state between instances. By initializing `books` inside the `__init__` method, each `Library` instance maintains its own collection of books, avoiding the issue of shared state.

