import timeit

def quadratic(input_size):
    for i in range(input_size):
        for j in range(input_size):
            pass


MAX_SIZE = 10000000
INCREMENT = 1000
MAX_RUNTIME = 10

input_size = 0
measurment = 0

results = []

while input_size <= MAX_SIZE and measurment <= MAX_RUNTIME:

    measurment = timeit.timeit(lambda: quadratic(input_size), number=1)

    print(f"Round: {input_size}  Time: {measurment}")

    results.append([input_size, measurment])

    input_size = input_size + INCREMENT

print("\n\nComplete\ncsv\n\nx,y")
for i in results:
    print(*i, sep = ",")