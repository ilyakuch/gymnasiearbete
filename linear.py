import timeit

def linear(input_size):
    for i in range(input_size):
        pass


MAX_SIZE = 1000000
INCREMENT = 2
MAX_RUNTIME = 2

input_size = 1
measurment = 0

results = []

while input_size <= MAX_SIZE and measurment <= MAX_RUNTIME:

    measurment = timeit.timeit(lambda: linear(input_size))

    print(f"Round: {input_size}  Time: {measurment}")

    results.append([input_size, measurment])

    input_size = input_size * INCREMENT

print("\n\nComplete\ncsv\n\nx,y")
for i in results:
    print(*i, sep = ",")