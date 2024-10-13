import random

def create_and_sort(n):
    data = [random.randint(0, 1000000) for _ in range(n)]
    data.sort()
    return data

# Sort the data
sorted_data = create_and_sort(10**6)
print(f"Python Sorted Count: {len(sorted_data)}")