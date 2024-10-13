def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Compute the factorial
result = factorial(1000)  # Adjust this number for larger test
print(f"Python Factorial Result: {result}")
