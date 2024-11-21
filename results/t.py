import csv

# Function to read CSV and return list of tuples
def read_csv_to_tuples(file_path):
    data = []
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header, if any
            for row in reader:
                # Convert x and y to float, assuming numeric data
                x, y = int(row[0]), float(row[1])
                data.append((x, y))
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except ValueError as e:
        print(f"Error processing data: {e}")
    return data

# Example usage
file_path = 'C:/Users/ilyak/Desktop/t.txt'  # Replace with your file path
tuples = read_csv_to_tuples(file_path)

if tuples:
    print("Data as list of tuples:")
    print(tuples)