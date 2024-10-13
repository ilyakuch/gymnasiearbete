#include <iostream>

double compute_sum(int n) {
    double total = 0.0;
    for (int i = 0; i < n; ++i) {
        total += 0.1;
    }
    return total;
}

int main() {
    double result = compute_sum(10000000);
    std::cout << "C++ Result: " << result << std::endl;
    return 0;
}