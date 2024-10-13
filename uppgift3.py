import threading

def find_primes(n, results):
    for num in range(2, n):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            results.append(num)

# Find primes using threads
results = []
threads = []
for i in range(4):  # Using 4 threads
    thread = threading.Thread(target=find_primes, args=(100000, results))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()

print(f"Python Found Primes Count: {len(results)}")
