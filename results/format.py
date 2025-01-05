def process_file(file_path):
    import re

    def format_number(num):
        """Format number to 4 decimal digits, avoiding scientific notation."""
        num = float(num)  # Ensure it's a float
        return f"{num:.4f}" if abs(num) >= 1e-4 else f"{num:.10f}".rstrip('0').rstrip('.')

    with open(file_path, 'r') as file:
        lines = file.readlines()

    processed_lines = []

    for line in lines:
        line = line.strip()  # Remove leading/trailing whitespace

        if not line:  # Skip empty lines
            processed_lines.append("")
            continue

        match = re.match(r"^(-?\d+\.?\d*),\s*(-?\d+(?:\.\d+|[eE][-+]?\d+)?)$", line)
        if match:  # Match x,y pair
            x, y = match.groups()
            y = format_number(y)  # Format y number
            processed_lines.append(f"{x},{y}")
        else:  # Leave strings untouched
            processed_lines.append(line)

    # Write the processed lines back to a new file
    output_file_path = file_path.replace('.txt', '_processed.txt')
    with open(output_file_path, 'w') as file:
        file.write('\n'.join(processed_lines) + '\n')

    print(f"Processed file saved as: {output_file_path}")

# Example usage
# process_file('input.txt')



process_file('results/csv.txt')
