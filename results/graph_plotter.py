import matplotlib.pyplot as plt
import pandas as pd

def plot_csv(csv_file):
    # Read the CSV file using pandas
    data = pd.read_csv(csv_file)

    # Check if the CSV contains two columns
    if data.shape[1] != 2:
        print("CSV file must have two columns: x and y")
        return

    # Extract x and y values
    x = data.iloc[:, 0]  # First column (x values)
    y = data.iloc[:, 1]  # Second column (y values)

    # Create the plot
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label='Data', color='b', marker='o')

    # Add labels and title
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('X vs Y Plot')
    plt.legend()

    # Display the plot
    plt.grid(True)
    plt.show()

# Example usage:
csv_file = r'C:\Users\ilyak\Documents\GitHub Repos\gymnasiearbete\csv.txt'
plot_csv(csv_file)