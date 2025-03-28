# Python Control Flow Statements: Match Statement (Python 3.10+)

The match statement offers a more concise way to handle multiple comparison cases.

```python
def get_fruit_color(fruit):
    match fruit:
        case "apple":
            return "red"
        case "banana":
            return "yellow"
        case _:
            return "unknown"
```
