Here’s an example of **multiple subplots** using **PyWaffle**, with both **horizontal and vertical layouts**. This is useful for comparing categorical data across different groups.

---

### Example: Multiple Subplots with Vertical Layout (default)

```python
import matplotlib.pyplot as plt
from pywaffle import Waffle

fig = plt.figure(
    FigureClass=Waffle,
    plots={
        111: {  # subplot position (1 row, 1 column, 1st plot)
            'values': {'Tea': 40, 'Coffee': 60},
            'title': {'label': 'Morning Preferences', 'loc': 'center'},
            'legend': {'loc': 'upper left', 'bbox_to_anchor': (1, 1)}
        },
        112: {
            'values': {'Tea': 30, 'Coffee': 70},
            'title': {'label': 'Afternoon Preferences', 'loc': 'center'},
        },
    },
    rows=5,
    figsize=(8, 6)
)

plt.show()
```

---

### Example: Multiple Subplots with Horizontal Layout

Use `ncols=2` to display subplots side by side.

```python
import matplotlib.pyplot as plt
from pywaffle import Waffle

fig = plt.figure(
    FigureClass=Waffle,
    plots={
        '311': {  # subplot position
            'values': {'Tea': 40, 'Coffee': 60},
            'title': {'label': 'Morning Preferences', 'loc': 'center'},
        },
        '312': {
            'values': {'Tea': 50, 'Coffee': 50},
            'title': {'label': 'Noon Preferences', 'loc': 'center'},
        },
        '313': {
            'values': {'Tea': 30, 'Coffee': 70},
            'title': {'label': 'Evening Preferences', 'loc': 'center'},
        }
    },
    rows=5,
    figsize=(12, 4)  # Wider for horizontal layout
)

plt.show()
```

---

### Tips

* Use `figsize` to adjust chart width/height.
* Use `plots` dictionary to define each subplot.
* Use `subplot code` like `'311'` for 3 rows, 1 column, 1st subplot (classic matplotlib format).

Let me know if you want a 2x2 grid or custom subplot layout with icons/colors!

Here’s a **simple beginner-friendly example** to demonstrate the **difference between horizontal and vertical layout** in **PyWaffle**. We'll show the same data in both layouts.

---

### 1. **Vertical Layout** (default)

```python
import matplotlib.pyplot as plt
from pywaffle import Waffle

# Vertical: stacked one below the other
fig = plt.figure(
    FigureClass=Waffle,
    plots={
        211: {  # 2 rows, 1 column, 1st subplot
            'values': {'Yes': 70, 'No': 30},
            'title': {'label': 'Survey Result A'}
        },
        212: {  # 2nd subplot
            'values': {'Yes': 45, 'No': 55},
            'title': {'label': 'Survey Result B'}
        }
    },
    rows=5,
    figsize=(6, 6)
)

plt.show()
```

---

### 2. **Horizontal Layout** (side-by-side)

```python
import matplotlib.pyplot as plt
from pywaffle import Waffle

# Horizontal: side by side
fig = plt.figure(
    FigureClass=Waffle,
    plots={
        121: {  # 1 row, 2 columns, 1st subplot
            'values': {'Yes': 70, 'No': 30},
            'title': {'label': 'Survey Result A'}
        },
        122: {  # 2nd subplot
            'values': {'Yes': 45, 'No': 55},
            'title': {'label': 'Survey Result B'}
        }
    },
    rows=5,
    figsize=(10, 4)
)

plt.show()
```

---

### Key Differences

* **Vertical Layout:** Use `211`, `212`, etc. for top-to-bottom stacking.
* **Horizontal Layout:** Use `121`, `122`, etc. for side-by-side display.
* `figsize`: Adjust width and height depending on layout direction.

Let me know if you want to add icons, percentages, or custom colors!
