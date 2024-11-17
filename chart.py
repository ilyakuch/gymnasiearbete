import matplotlib.pyplot as plt
import numpy as np

# Define the input range
n = np.linspace(1, 10, 100)

# Define the functions for each time complexity
O_1 = np.ones_like(n)      # O(1) is a constant function
O_n = n                   # O(n) is linear
O_n2 = n**2               # O(n^2) is quadratic

# Create the plot with extended x-axis and 1:1 aspect ratio
plt.figure(figsize=(10, 6))

# Plot the functions
plt.plot(n, O_1, label="O(1)", color='blue')
plt.plot(n, O_n, label="O(n)", color='green')
plt.plot(n, O_n2, label="O(n^2)", color='red')

# Add annotations near the respective graphs
plt.text(5, 1.2, "O(1)", fontsize=12, color='blue')
plt.text(8, 8, "O(n)", fontsize=12, color='green')
plt.text(6, 40, "O(n^2)", fontsize=12, color='red')

# Adjust axes for a 1:1 aspect ratio but extend the x-axis range
plt.gca().set_aspect('auto', adjustable='box')

# Add labels and title

plt.xlabel("Input Size")
plt.ylabel("Operations")

# Remove tick values (but keep the axes)
plt.gca().set_xticklabels([])
plt.gca().set_yticklabels([])

# Show the plot with grid
plt.grid(True)
plt.show()
