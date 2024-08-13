import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('youtube-wh.csv')

# Plotting the line chart
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Watch_Hours'], marker='o', linestyle='-', color='r')

# Adding title and labels
plt.title('Watch Hours Over Time')
plt.xlabel('Date')
plt.ylabel('Watch Hours')

# Display the grid
plt.grid(True)

# Show the plot
plt.show()

