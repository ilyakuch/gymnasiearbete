#include <iostream>
#include <vector>
#include <thread>
#include <cmath>

void find_primes(int n, std::vector<int>& results) {
    for (int num = 2; num < n; ++num) {
        bool is_prime = true;
        for (int i = 2; i <= std::sqrt(num); ++i) {
            if (num % i == 0) {
                is_prime = false;
                break;
            }
        }
        if (is_prime) {
            results.push_back(num);
        }
    }
}

int main() {
    std::vector<int> results;
    std::vector<std::thread> threads;
    for (int i = 0; i < 4; ++i) {  // Using 4 threads
        threads.emplace_back(find_primes, 100000, std::ref(results));
    }
    for (auto& thread : threads) {
        thread.join();
    }
    std::cout << "C++ Found Primes Count: " << results.size() << std::endl;
    return 0;
}
