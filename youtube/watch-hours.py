import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('youtube-wh.csv')

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,10))

# Plot Watch Hours on the first subplot
ax1.plot(df['Date'], df['Watch_Hours'], marker='o', linestyle='-', color='b')
ax1.set_title('Watch Hours Over Time')
ax1.set_xlabel('Date')
ax1.set_ylabel('Watch Hours')
ax1.grid(True)

# Plot Subscribers on the second subplot
ax2.plot(df['Date'], df['Subscribers'], marker='s', linestyle='--', color='r')
ax2.set_title('Subscribers Over Time')
ax2.set_xlabel('Date')
ax2.set_ylabel('Subscribers')
ax2.grid(True)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()