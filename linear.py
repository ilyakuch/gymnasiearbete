import timeit

def linear(input_size):
    for i in range(input_size):
        pass


MAX_SIZE = 10000000
INCREMENT = 100000
MAX_RUNTIME = 10

input_size = 0
measurment = 0

results = []

while input_size <= MAX_SIZE and measurment/2 <= MAX_RUNTIME:

    measurment = timeit.timeit(lambda: linear(input_size), number=2)

    print(f"{input_size},{(measurment*500):.5f}")
    
    results.append([input_size, round((measurment*500), 5)])

    input_size = input_size + INCREMENT