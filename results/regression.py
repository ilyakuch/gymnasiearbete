import numpy as np

# Define regression models
def constant_model(x, a):
    return a

def linear_model(x, a, b):
    return a * x + b

def quadratic_model(x, a, b, c):
    return a * x**2 + b * x + c

def fit_model(x, y, model_type):
    """Fits a regression model based on the selected type."""
    if model_type == 1:
        a = np.mean(y)
        return constant_model, [a]
    elif model_type == 2:
        coeffs = np.polyfit(x, y, 1)
        return linear_model, coeffs[::-1]
    elif model_type == 3:
        coeffs = np.polyfit(x, y, 2)
        return quadratic_model, coeffs[::-1]
    else:
        raise ValueError("Invalid model type. Choose 1 (constant), 2 (linear), or 3 (quadratic).")

def main():
    file_path = "results/temp.txt"
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
        return

    data = []
    for line in lines:
        if line.strip():
            try:
                x, y = map(float, line.split(','))
                data.append((x, y))
            except ValueError:
                print(f"Invalid input skipped: {line.strip()}")

    if not data:
        print("No valid data found in the file. Exiting.")
        return

    x, y = zip(*data)
    x, y = np.array(x), np.array(y)

    print("Select regression model:")
    print("1. Constant")
    print("2. Linear")
    print("3. Quadratic")
    try:
        model_type = int(input("Enter model type (1, 2, or 3): "))
        model, params = fit_model(x, y, model_type)

        if model_type == 1:
            print(f"Fitted model: y = {params[0]:.6e}")
        elif model_type == 2:
            print(f"Fitted model: y = {params[0]:.6e} * x + {params[1]:.6e}")
        elif model_type == 3:
            print(f"Fitted model: y = {params[0]:.6e} * x^2 + {params[1]:.6e} * x + {params[2]:.6e}")

    except ValueError:
        print("Invalid selection. Please enter 1, 2, or 3.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
