import timeit

def constant(input_size):
    pass


MAX_SIZE = 10000000
INCREMENT = 100000
MAX_RUNTIME = 10

input_size = 0
measurment = 0

results = []

while input_size <= MAX_SIZE and measurment/2 <= MAX_RUNTIME:

    measurment = timeit.timeit(lambda: constant(input_size), number=2)

    print(f"Round: {input_size}  Time: {measurment}  Avg: {measurment/2}")

    results.append([input_size, measurment/2])

    input_size = input_size + INCREMENT

print("\n\nComplete\ncsv\n\nx,y")
for i in results:
    print(*i, sep = ",")