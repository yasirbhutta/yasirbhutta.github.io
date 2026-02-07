---
layout: page
title: Streamlit
description: Streamlit is an open-source Python library designed for creating and sharing web applications for data science and machine learning. It makes it easy...
keywords: streamlit, data, app, write, number
---
# Streamlit

Streamlit is an open-source Python library designed for creating and sharing web applications for data science and machine learning. It makes it easy to build interactive, data-driven applications with minimal code and allows you to share them directly with others.

Here’s an introduction to using Streamlit:

### Installation
To install Streamlit, use:
```bash
pip install streamlit
```

### Basic Example
Streamlit apps are written in Python scripts. Here’s a simple app to get started:

```python
# my_app.py
import streamlit as st

st.title("Hello, Streamlit!")
st.write("This is a simple web app created with Streamlit.")

# Add an interactive slider
number = st.slider("Pick a number", 0, 100)
st.write("The selected number is:", number)
```

To run the app, navigate to the folder where `my_app.py` is saved, and run:
```bash
streamlit run my_app.py
```

This opens a new browser window with your app.

### Key Features

1. **Widgets**: Streamlit includes easy-to-use widgets like sliders, buttons, file uploaders, and more:
   - `st.button("Click me!")`
   - `st.text_input("Enter text:")`
   - `st.selectbox("Choose an option:", ["A", "B", "C"])`

2. **Charts and DataFrames**: You can visualize data directly using libraries like Matplotlib, Seaborn, Plotly, and Altair, as well as display pandas DataFrames.
   ```python
   import pandas as pd
   import numpy as np

   df = pd.DataFrame(np.random.randn(20, 3), columns=['A', 'B', 'C'])
   st.line_chart(df)
   ```

3. **Interactive Layouts**: Streamlit allows you to use columns, expanders, and containers for structuring the layout.
   ```python
   col1, col2 = st.columns(2)
   col1.write("Column 1")
   col2.write("Column 2")
   ```

4. **Session State**: Streamlit provides a way to maintain state between interactions, which is helpful for applications that need to retain information across user actions.

### Advantages
- No front-end experience is needed.
- Simple and clean UI.
- Quick prototyping and sharing (e.g., data exploration, dashboards).
